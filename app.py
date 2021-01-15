import json

from chalice import Chalice

from forecaster import average_forecast

app = Chalice(app_name='avg_forecaster')


@app.route('/forecast', methods=['POST'])
def forecast():
    forecast_data = app.current_request.json_body
    data_dict = json.loads(forecast_data)
    result = make_forecast(data_dict)
    return json.dumps(result)
