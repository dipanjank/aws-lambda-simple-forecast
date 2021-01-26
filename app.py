import json
import os

import boto3
from chalice import Chalice

from chalicelib.forecaster import average_forecast

app = Chalice(app_name='avg_forecaster')


@app.route('/forecast', methods=['POST'])
def simple_forecast():
    forecast_data = app.current_request.json_body
    result = average_forecast(forecast_data)
    return json.dumps(result)


@app.on_s3_event(bucket=os.environ['INPUT_BUCKET'], events=['s3:ObjectCreated:*'])
def simple_forecast_async(event):
    # Expect files from INPUT_BUCKET with .json extension
    if not event.key.endswith('.json'):
        raise ValueError(f'Expecting a json file, instead got: {event.key}')

    # Read the file from S3
    s3_client = boto3.client('s3')
    file_obj = s3_client.get_object(Bucket=event.bucket, Key=event.key)
    content = file_obj['Body'].read().decode('utf-8')
    app.log.info(f"Processing: {content}")
    forecast_data = json.loads(content)

    # Make a forecast
    result = average_forecast(forecast_data)
    result_str = json.dumps(result)

    # Write the result to the output bucket
    out_bucket = os.environ['OUTPUT_BUCKET']
    output_key = event.key.replace('.json', '.results.json')
    s3_client.put_object(Key=output_key, Bucket=out_bucket, Body=result_str.encode('utf-8'))

