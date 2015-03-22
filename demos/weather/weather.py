import requests
from pprint import pprint
import csv
import datetime

url = "http://api.openweathermap.org/data/2.5/weather?q=Bristol,uk&units=metric"

# fetch the url
r = requests.get(url)
# sometimes the data is invalid - so we handle it nicely
try:
    data = r.json()
except ValueError:
    print("got bad data, quitting")
    exit(1)

# print it nicely
pprint(data)

# grab the bits we want in separate variables
wind = data["wind"]["speed"]
temp = data["main"]["temp"]
# we subtract 800 to get a number from 0 to 5 see link below about
# conditions : http://openweathermap.org/weather-conditions
clouds = data["weather"][0]["id"]-800
# get the date and time
date = datetime.datetime.now()

# write the data as a CSV file
with open('log.csv', 'a') as fh:
    writer = csv.writer(fh)
    writer.writerow([date,wind, temp, clouds])
