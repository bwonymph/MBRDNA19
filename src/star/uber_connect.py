__author__ = 'aravind.selvan'

import json
import os
import requests
import urllib3
from urlparse import urlparse
from rauth import OAuth2Service

requests.packages.urllib3.disable_warnings()

with open('config.json') as f:
    config = json.load(f)

UBER_SECRET_KEY = 'GESzipNI5RurLAKWrz2K3UPZXWACNzmyriFFceLS'
UBER_CLIENT_ID = 'EXBIvkr2X4zbRlzeZKOMua8Z9-XhUjmM'
UBER_SERVER_TOKEN = 'uUG4wiGBkfllHmLP8Yc3kkFdwJT7MrR9ozxp556F'

uber_api = OAuth2Service(
    client_id=UBER_CLIENT_ID,
    client_secret=UBER_SECRET_KEY,
    name='INSERT_APP_NAME',
    authorize_url='https://login.uber.com/oauth/authorize',
    access_token_url='https://login.uber.com/oauth/token',
    base_url='https://api.uber.com/v1/',
)

parameters = {
    'response_type': 'code',
    'scope': 'profile',
}

# Redirect user here to authorize your application
login_url = uber_api.get_authorize_url(**parameters)


def uber_time_estimate(latitude, longitude):
    print "time estimate uber"
    url = 'https://api.uber.com/v1/estimates/time'
    parameters1 = {
        'server_token': UBER_SERVER_TOKEN,
        'start_latitude': latitude,
        'start_longitude': longitude,
    }
    response = requests.get(url, params=parameters1)
    data = response.json()
    print data


def call_uber(latitude, longitude):
    print "calling uber"
    url = 'https://api.uber.com/v1/products'
    parameters1 = {
        'server_token': UBER_SERVER_TOKEN,
        'latitude': latitude,
        'longitude': longitude,
    }

    response = requests.get(url, params=parameters1)

    data = response.json()

    print data
