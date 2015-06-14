#! /usr/bin/python

import serial, sys, urllib, urllib3, json
import requests
from uber_connect import call_uber, uber_time_estimate
from firebase import firebase
from Firebase_util import putIntoFirebaseSpeedLimit
from pprint import pprint

HERE_APP_ID = 'CVT1d4hPZwdBitMF4uhM'
HERE_APP_CODE = 'tqzZ2QHmKKKFWFkb-5Fp-g'

# Util, don't delete
with open('data.json') as data_file:
    data1 = json.load(data_file)
# pprint(data1)

def get_speedLimit(GPS_Latitude, GPS_Longitude):
    position = str(GPS_Latitude)
    position += ','
    position += str(GPS_Longitude)
    position += ','
    position += '150'
    print position
    url = 'http://reverse.geocoder.cit.api.here.com/6.2/reversegeocode.json'
    parameters1 = {
        'gen': 8,
        'locationattributes': 'linkInfo',
        'maxresults': 1,
        'mode': 'trackPosition',
        'pos': position,
        'app_id': HERE_APP_ID,
        'app_code': HERE_APP_CODE,
    }
    response = requests.get(url, params=parameters1)
    data = response.json()
    speedLimit_data = data['Response']['View'][0]['Result'][0]['Location']['LinkInfo']['SpeedLimit']
    speedLimit_unit = speedLimit_data[0]['Unit']
    speedLimit_value = speedLimit_data[0]['Value']

    putIntoFirebaseSpeedLimit(speedLimit_value, speedLimit_unit)
