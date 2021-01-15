import pandas as pd


def make_forecast(data_dict):
    """
    Take daily data and return the average of the training data as forecast from
    ``data_dict['start_date']`` and ``data_dict['end_date']``. Dates expected in YYYY-MM-DD
    format.

    :param data_dict: The train data and the predict start and end dates.
    :return: The prediction result as a list of dictionaries, with keys 'date' and 'data'.
    """
    train_df = pd.DataFrame(data_dict['train_data'])
    if 'date' not in train_df.columns:
        raise ValueError('No "date" column provided.')
    if 'data' not in train_df.columns:
        raise ValueError('No "data" column provided.')

    avg_forecast = train_df.data.mean()

    # Return the average value as the forecast for each day between start and end date
    predict_dates = pd.date_range(
        start=data_dict['start_date'],
        end=data_dict['end_date'],
        freq='D'
    )

    predict_df = pd.Series(index=predict_dates, name='data', data=avg_forecast)
    return [
        {'date': date.strftime('%Y-%m-%d'), 'data': data}
            for date, data in predict_df.items()
    ]
