import config
import requests
import json
import datetime

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

# get historical data for zone 1
zone = '1'
params = (('date', str(datetime.date.today() - datetime.timedelta(days=1))),)
raw = requests.get('https://my.tado.com/api/v2/homes/'+str(homeId)+'/zones/'+zone+'/dayReport', headers=headers, params=params)
res = raw.json()

# parse timestamp and temp for zone 1
for res5 in res['measuredData']['insideTemperature']['dataPoints']:
    print(zone,res5['timestamp'], res5['value']['celsius'])

# get historical data for zone 2
zone = '2'
params = (('date', str(datetime.date.today() - datetime.timedelta(days=1))),)
raw = requests.get('https://my.tado.com/api/v2/homes/'+str(homeId)+'/zones/'+zone+'/dayReport', headers=headers, params=params)
res = raw.json()

# parse timestamp and temp for zone 2
for res5 in res['measuredData']['insideTemperature']['dataPoints']:
    print(zone,res5['timestamp'], res5['value']['celsius'])

# get historical data for zone 3
zone = '3'
params = (('date', str(datetime.date.today() - datetime.timedelta(days=1))),)
raw = requests.get('https://my.tado.com/api/v2/homes/'+str(homeId)+'/zones/'+zone+'/dayReport', headers=headers, params=params)
res = raw.json()

# parse timestamp and temp for zone 3
for res5 in res['measuredData']['insideTemperature']['dataPoints']:
    print(zone,res5['timestamp'], res5['value']['celsius'])

# get historical data for zone 4
zone = '4'
params = (('date', str(datetime.date.today() - datetime.timedelta(days=1))),)
raw = requests.get('https://my.tado.com/api/v2/homes/'+str(homeId)+'/zones/'+zone+'/dayReport', headers=headers, params=params)
res = raw.json()

# parse timestamp and temp for zone 4
for res5 in res['measuredData']['insideTemperature']['dataPoints']:
    print(zone,res5['timestamp'], res5['value']['celsius'])
