#! /usr/bin/python

import serial, sys, urllib, urllib3, json
import requests
from uber_connect import call_uber, uber_time_estimate
from firebase import firebase
from Firebase_util import putIntoFirebaseUber
from connect_here import get_speedLimit

requests.packages.urllib3.disable_warnings()
initialTouched = False
leftToRight = False
topToBottom = False
maxTries = 20
# Each test bench is labeled with the serial device name on the USB cable
device_name = '/dev/cu.usbserial-FTGQJ7IM'
baud_rate = 115200

# Set up the serial port connection
ser = ""  # serial.Serial(device_name, baud_rate)
# ser.flushInput()
# ser.flushOutput()


class Shape:  # define parent class
    def identifyShape(self):
        print 'This is super class, never called'


def verifyInitalTouch(c):
    global initialTouched
    if c == 'touchHold' or c == 'touchpadAreaPressed':
        initialTouched = True
        return True
    elif initialTouched == True:
        return True
    else:
        return False


def increasingY():
    newY = 0
    oldY = -1
    start = 1
    while True:
        raw_data = ser.readline()
        parts = raw_data.split()
        command = parts[0]
        params = dict((k, int(v)) for k, v in (p.split(':') for p in parts[1:]))
        if 'y' not in params:
            continue
        newY = params['y']
        if (start == 1):
            if newY < 110:
                start = 0
            else:
                return False
        if command == 'touchAt':
            if newY >= oldY:
                oldY = newY
                if newY > 320:
                    return True
                else:
                    continue
        return False


def verifyTopToBottomSwipe():
    while True:
        raw_data = ser.readline()
        parts = raw_data.split()
        command = parts[0]
        #  print "TB--", command, params
        if command == 'swipeDown':
            if increasingY():
                return True
            else:
                return False
    return False


def increasingX():
    newX = 0
    oldX = -1
    start = 1
    while True:
        raw_data = ser.readline()
        parts = raw_data.split()
        command = parts[0]
        params = dict((k, int(v)) for k, v in (p.split(':') for p in parts[1:]))
        if 'x' not in params:
            continue
        newX = params['x']
        if (start == 1):
            if newX < 140:
                start = 0
            else:
                return False
        if command == 'touchAt':
            if newX >= oldX:
                oldX = newX
                if newX > 250:
                    return True
                else:
                    continue
        return False


def verifyLeftToRightSwipe():
    while True:
        raw_data = ser.readline()
        parts = raw_data.split()
        command = parts[0]
        #  print "TB--", command, params
        if command == 'swipeRight':
            if increasingX():
                return True
            else:
                return False
    return False


class PlusSymbol(Shape):
    def identifyShape(self):
        global initialTouched
        numberOfTimesTried = 0
        while True:
            if (numberOfTimesTried > maxTries):
                print  "Ubering you"
            raw_data = ser.readline()
            parts = raw_data.split()
            command = parts[0]
            params = dict((k, int(v)) for k, v in (p.split(':') for p in parts[1:]))
            # Print for debugging
            print command, params
            if verifyInitalTouch(command) or initialTouched:
                if verifyTopToBottomSwipe():
                    print "Initial auth done."
                    if verifyLeftToRightSwipe():
                        print "You're successful in authenticating your soberness, drive!!"
                    return True

            else:
                print "Please swipe correctly"
                numberOfTimesTried += 1
                initialTouched = False
            # Force the system to flush the data buffer and write the output immediately
            sys.stdout.flush()


def getCurrentLocation():
    url = "http://172.31.99.3/vehicle"
    response = urllib.urlopen(url);
    carData = json.loads(response.read())
    GPS_Latitude = carData['GPS_Latitude']
    GPS_Longitude = carData['GPS_Longitude']

    get_speedLimit(GPS_Latitude, GPS_Longitude)
    putIntoFirebaseUber(GPS_Latitude, GPS_Longitude)

    uber_time_estimate(GPS_Latitude, GPS_Longitude)


if __name__ == "__main__":
    # DON'T DELETE ANYTHING BELOW
    # raw_data = ser.readline()
    #  symbol = PlusSymbol()
    #  symbol.identifyShape()
    getCurrentLocation()
