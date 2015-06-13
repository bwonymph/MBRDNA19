import requests
import json
import urllib3
import urllib
from firebase import firebase
requests.packages.urllib3.disable_warnings()

firebase = firebase.FirebaseApplication('https://benkpak.firebaseio.com/', None)

#posts data to the cloud
def postData():
    url = "http://172.31.99.3/vehicle"
    response = urllib.urlopen(url);
    data = json.loads(response.read()) # Get data from terminal
    #print(data)
    localGPSlat = data['GPS_Latitude']
    localGPSlong = data['GPS_Longitude']

    firebase.put('/Car', "GPS_Latitude", localGPSlat) # Add data to Node Node1
    firebase.put('/Car', "GPS_Longitude", localGPSlong) # Add data to Node Node1

postData();
