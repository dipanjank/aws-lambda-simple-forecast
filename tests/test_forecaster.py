import numpy as np

from chalicelib.forecaster import average_forecast

RAND = np.random.RandomState(100)


def test_average_forecast():
    values = RAND.randint(low=50, high=200, size=31)
    dates = [f'2020-01-{str(n).zfill(2)}' for n in range(1, 31+1)]

    train_data = [{'date': d, 'data': v} for d, v in zip(dates, values)]

    data_dict = {
        'train_data': train_data,
        'start_date': '2020-02-01',
        'end_date': '2020-02-29'
    }
    actual = average_forecast(data_dict)
    expected = [{
        'date': f'2020-02-{str(n).zfill(2)}',
        'data': 134.48387096774192
    } for n in range(1, 29+1)]

    assert expected == actual
