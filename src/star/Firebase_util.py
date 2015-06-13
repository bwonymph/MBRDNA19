import requests
import json
import urllib3
import urllib
from firebase import firebase

requests.packages.urllib3.disable_warnings()

firebase = firebase.FirebaseApplication('https://benkpak.firebaseio.com/', None)

def putIntoFirebaseCar(GPS_Latitude, GPS_Longitude):
    firebase.put('/Car', "GPS_Latitude", GPS_Latitude)  # Add data to Node Node1
    firebase.put('/Car', "GPS_Longitude", GPS_Longitude)  # Add data to Node Node1