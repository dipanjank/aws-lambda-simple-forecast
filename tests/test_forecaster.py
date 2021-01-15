from forecaster import average_forecast


def test_average_forecast():
    train_data = [
        {
            'date': f'2020-01-{str(n).zfill(2)}',
            'data': 10.0
        }
        for n in range(1, 31+1)
    ]

    data_dict = {
        'train_data': train_data,
        'start_date': '2020-02-1',
        'end_date': '2020-02-29'
    }
    actual = average_forecast(data_dict)
    expected = [{
        'date': f'2020-02-{str(n).zfill(2)}',
        'data': 10.0
    } for n in range(1, 29+1)]

    assert expected == actual
