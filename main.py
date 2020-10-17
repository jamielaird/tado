import config
import requests
import json
import datetime
import psycopg2

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

# set query date
# date = '2020-10-14' # <-- set a specific date
date = str(datetime.date.today() - datetime.timedelta(days=1)) # <-- set date to yesterday

# get historical data for zone 1
zone = '1'
params = (('date',date),)
raw = requests.get('https://my.tado.com/api/v2/homes/'+str(homeId)+'/zones/'+zone+'/dayReport', headers=headers, params=params)
res = raw.json()

# open database connection
conn = psycopg2.connect('dbname=tado')
cursor = conn.cursor()

# iterate through results to check date is today, parse zone, timestamp and temperature and write to postgres (tado.inside_temperature)
for res5 in res['measuredData']['insideTemperature']['dataPoints']:
    if str(res5['timestamp'])[:10] == date:
        cursor.execute("INSERT INTO inside_temperature (zone, timestamp, temperature) VALUES (%s, %s, %s)",(int(zone),str(res5['timestamp']),float(res5['value']['celsius'])))

# commit and close database connection
conn.commit()
cursor.close()
conn.close()

# get historical data for zone 2
zone = '2'
params = (('date', date),)
raw = requests.get('https://my.tado.com/api/v2/homes/'+str(homeId)+'/zones/'+zone+'/dayReport', headers=headers, params=params)
res = raw.json()

# open database connection
conn = psycopg2.connect('dbname=tado')
cursor = conn.cursor()

# iterate through results to parse zone, timestamp and temperature and write to postgres (tado.inside_temperature)
for res5 in res['measuredData']['insideTemperature']['dataPoints']:
    if str(res5['timestamp'])[:10] == date:
        cursor.execute("INSERT INTO inside_temperature (zone, timestamp, temperature) VALUES (%s, %s, %s)",(int(zone),str(res5['timestamp']),float(res5['value']['celsius'])))



# commit and close database connectionfor res5 in res['measuredData']['insideTemperature']['dataPoints']:
conn.commit()
cursor.close()
conn.close()

# get historical data for zone 3
zone = '3'
params = (('date', date),)
raw = requests.get('https://my.tado.com/api/v2/homes/'+str(homeId)+'/zones/'+zone+'/dayReport', headers=headers, params=params)
res = raw.json()

# open database connection
conn = psycopg2.connect('dbname=tado')
cursor = conn.cursor()

# iterate through results to parse zone, timestamp and temperature and write to postgres (tado.inside_temperature)
for res5 in res['measuredData']['insideTemperature']['dataPoints']:
    if str(res5['timestamp'])[:10] == date:
        cursor.execute("INSERT INTO inside_temperature (zone, timestamp, temperature) VALUES (%s, %s, %s)",(int(zone),str(res5['timestamp']),float(res5['value']['celsius'])))


# commit and close database connection
conn.commit()
cursor.close()
conn.close()

# get historical data for zone 4
zone = '4'
params = (('date', date),)
raw = requests.get('https://my.tado.com/api/v2/homes/'+str(homeId)+'/zones/'+zone+'/dayReport', headers=headers, params=params)
res = raw.json()

# open database connection
conn = psycopg2.connect('dbname=tado')
cursor = conn.cursor()

# iterate through results to parse zone, timestamp and temperature and write to postgres (tado.inside_temperature)
for res5 in res['measuredData']['insideTemperature']['dataPoints']:
    if str(res5['timestamp'])[:10] == date:
        cursor.execute("INSERT INTO inside_temperature (zone, timestamp, temperature) VALUES (%s, %s, %s)",(int(zone),str(res5['timestamp']),float(res5['value']['celsius'])))

# commit and close database connection
conn.commit()
cursor.close()
conn.close()
