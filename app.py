import json

from chalice import Chalice
from chalicelib.forecaster import average_forecast
app = Chalice(app_name='avg_forecaster')


@app.route('/forecast', methods=['POST'])
def forecast():
    forecast_data = app.current_request.json_body
    result = average_forecast(forecast_data)
    return json.dumps(result)
