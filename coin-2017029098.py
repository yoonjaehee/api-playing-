import requests
import datetime
import time
import pandas as pd
from pandas import DataFrame
import telepot
from apscheduler.schedulers.background import BackgroundScheduler
apikey = "c8e8f36cb6e2429312f2cbd8520c99a827b3cc68f883103ad436c1382564faa7"
url = "https://min-api.cryptocompare.com/data/price"
payload = {
    "api_key": apikey,
    "fsym": "BTC",
    "tsyms": "USD,KRW"
}
## save first line in csv 
df = pd.DataFrame(columns=("Date","Bitfinex-BTC-USD","Bithumb-BTC-KRW"))
bot = telepot.Bot('846530643:AAH5JlK9_cwj0-6S3wDMSDplfCmg6IzsI6s')
base = datetime.datetime.now()
now = base.strftime('%Y-%m-%d-%H:%M')
result = requests.get(url, params=payload).json()
df2 = [now,result['USD'],result['KRW']]
df.loc[len(df)] = df2
df.to_csv("C:\\Users\\ytjh0\\Desktop\\saving.csv",mode='w')
time.sleep(60)
## Compare the current coin value with the coin value 60 seconds ago and repeat every 60 seconds.  
def interval():
    base = datetime.datetime.now()
    now = base.strftime('%Y-%m-%d-%H:%M')
    result = requests.get(url, params=payload).json()
    df2 = [now,result['USD'],result['KRW']]
    df.loc[len(df)] = df2
    df.to_csv("C:\\Users\\ytjh0\\Desktop\\saving.csv",mode='w')
    after = df.iloc[-1]['Bithumb-BTC-KRW']
    before = df.iloc[-2]['Bithumb-BTC-KRW']
    up=after-before
    bot.sendMessage(943659166,"Bithumb-BTC-KRW:{},UP:{}".format(after,up))
sched = BackgroundScheduler()
sched.start()
sched.add_job(interval,'interval',seconds=60,id="testing")
