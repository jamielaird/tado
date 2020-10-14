import config
import requests
import json
import datetime
from datetime import date, timedelta

# get bearer token
data = {
  'client_id': 'tado-web-app',
  'grant_type': 'password',
  'scope': 'home.user',
  'username': config.username,
  'password': config.password,
  'client_secret': config.client_secret
}
raw = requests.post('https://auth.tado.com/oauth/token', data=data)
res = raw.json()
access_token = res['access_token']
headers = {'Authorization': 'Bearer '+access_token,}

# get homeId
raw = requests.get('https://my.tado.com/api/v1/me', headers=headers)
res = raw.json()
homeId = res['homeId']

# get zones
url = 'https://my.tado.com/api/v2/homes/'+str(homeId)+'/zones'
raw = requests.get(url, headers=headers)
res = raw.json()
zone = '1'

# get historical data 
# params = (('date', '2020-10-12'),)
params = (('date', str(datetime.date.today() - datetime.timedelta(days=1))),)

raw = requests.get('https://my.tado.com/api/v2/homes/'+str(homeId)+'/zones/'+zone+'/dayReport', headers=headers, params=params)
res = raw.json()

# parse timestamp and temp
for res5 in res['measuredData']['insideTemperature']['dataPoints']:
    print(zone,res5['timestamp'], res5['value']['celsius'])
