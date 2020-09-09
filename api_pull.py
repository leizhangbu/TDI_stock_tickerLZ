import pandas as pd
from pandas import DataFrame
import requests
import simplejson as json
from datetime import datetime, date


def get_data(ticker):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY'

    params = {'api_key':'VEGV3MZYOH1TFOX8', 'qopts.columns':'date,close'}
    params['ticker'] = ticker
    
    today = date.today()
    start_date = today.replace(year=today.year if today.month > 1 else today.year - 1, month=today.month - 1 if today.month >1 else 12)
    print(today,start_date)
    resp = requests.get(url+'&symbol='+str(ticker)+'&outputsize=compact&apikey=VEGV3MZYOH1TFOX8')

    
    json = resp.json()
    print(json)
    df = pd.DataFrame.from_dict(json['Time Series (Daily)'],orient='index')
    print('1',df[:10])
    df ['date'] = pd.to_datetime(df.index)
    print('2',df[:10])
    datatable = df ['date']
    print('3',df[:10])
    df['4. close'].astype('float')
    print('4',df[:10])
    try:
        df.index = pd.to_datetime(df.index)
        print('5',df[:10])
        print(df[start_date:today]['4. close'])
        return df[start_date:today]['4. close']
    except Exception as e:
        df = []
        return df

