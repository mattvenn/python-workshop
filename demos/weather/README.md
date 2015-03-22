# Reading weather data with an API and requests

A great way to demonstrate the power of python combined with the internet is to
show how we can automate fetching data. In the past I've used this to 

* notify me when stock arrives in an online shop,
* fetch solar wind speed from a space agency website,
* fetch frequency changes on the UK national grid.

This example uses a very simple API to get weather data for any city in the
world.

## What is an API

API stands for [application programming
interface](http://en.wikipedia.org/wiki/Application_programming_interface). It
makes it easy for a program to communicate with another program.

When we want to find the weather using a computer, we go to a website, read the
info and we're done. But what if we want to keep a note of it, or make it do
something fun. Imagine running the code on a raspberry pi, hooked up with a fan.
The fan blows proportionally to the current wind speed.

## The open weather map API

I found a great site called [openweathermap.org](http://openweathermap.org)
The [API documentation is here](http://openweathermap.org/api)

You can read the docs if you want, but when we fetch this URL

    http://api.openweathermap.org/data/2.5/weather?q=Bristol,uk&units=metric

We get [JSON](http://en.wikipedia.org/wiki/JSON) data like this (I've formatted
it nicely)

    {u'base': u'cmc stations',
     u'clouds': {u'all': 0},
     u'cod': 200,
     u'coord': {u'lat': 51.46, u'lon': -2.6},
     u'dt': 1427061424,
     u'id': 2654675,
     u'main': {u'humidity': 91,
               u'pressure': 1021,
               u'temp': 3.37,
               u'temp_max': 5.3,
               u'temp_min': 1.7},
     u'name': u'Bristol',
     u'sys': {u'country': u'GB',
              u'id': 5076,
              u'message': 0.0096,
              u'sunrise': 1427004458,
              u'sunset': 1427048806,
              u'type': 1},
     u'weather': [{u'description': u'Sky is Clear',
                   u'icon': u'01n',
                   u'id': 800,
                   u'main': u'Clear'}],
     u'wind': {u'deg': 260, u'speed': 1.5}}

Which we can then easily grab the bits we're interested in.

# The program

The program uses the excellent requests library which you'll have to 
[install first](#requirements).

Have a [look at the program](weather.py), it's well commented takes you through
what's happening. After fetching the data, the date, wind speed, temperature and
cloud cover are stored in a CSV file so I can turn it into a graph later. We
could instead:

* turn an LED different colours depending on temperature,
* send a text at sunrise,
* spin a fan to represent wind speed... 

# Requirements 

the requests module:

* Linux/Mac: on the command line: sudo pip install requests
* Windows: install requests from http://www.lfd.uci.edu/~gohlke/pythonlibs/
