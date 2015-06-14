import requests
import json
import urllib3
import urllib
from firebase import firebase

requests.packages.urllib3.disable_warnings()

firebase = firebase.FirebaseApplication('https://benkpak.firebaseio.com/', None)


#methods for uber detection
def putIntoFirebaseUber(GPS_Latitude, GPS_Longitude):
    firebase.put('/Uber', "GPS_Latitude", GPS_Latitude)  # Add data to Node Node1
    firebase.put('/Uber', "GPS_Longitude", GPS_Longitude)  # Add data to Node Node1


#put into car methods
def putIntoFirebaseCarBattery_Level(Battery_Level):
    firebase.put('/Car',"Battery_Level", Battery_Level)

def putIntoFirebaseCarHonk_State(Honk_State):
    firebase.put('/Car',"Honk_State", Honk_State)

def putIntoFirebaseCarFuel_Consumption(Fuel_Consumption):
    firebase.put('/Car',"Fuel_Consumption", Fuel_Consumption)

def putIntoFirebaseCarAccelerator_Pedal(Accelerator_Pedal):
    firebase.put('/Car',"Accelerator_Pedal", Accelerator_Pedal)

def putIntoFirebaseCarInside_Temperature(Inside_Temperature):
    firebase.put('/Car',"Inside_Temperature", Inside_Temperature)

def putIntoFirebaseCarFuel_Level(Fuel_Level):
    firebase.put('/Car',"Fuel_Level", Fuel_Level)

def putIntoFirebaseCarTire_Pressure_Front_Left(Tire_Pressure_Front_Left):
    firebase.put('/Car',"Tire_Pressure_Front_Left", Tire_Pressure_Front_Left)

def putIntoFirebaseCarOutside_Air_Temperature(Outside_Air_Temperature):
    firebase.put('/Car',"Outside_Air_Temperature", Outside_Air_Temperature)

def putIntoFirebaseCarOdometer(Odometer):
    firebase.put('/Car',"Odometer", Odometer)

def putIntoFirebaseCarDoor_State_Front_Right(Door_State_Front_Right):
    firebase.put('/Car',"Door_State_Front_Right", Door_State_Front_Right)

def putIntoFirebaseCarTire_Pressure_Rear_Left(Tire_Pressure_Rear_Left):
    firebase.put('/Car',"Tire_Pressure_Rear_Left", Tire_Pressure_Rear_Left)

def putIntoFirebaseCarTire_Pressure_Front_Right(Tire_Pressure_Front_Right):
    firebase.put('/Car',"Tire_Pressure_Front_Right", Tire_Pressure_Front_Right)

def putIntoFirebaseCarTimestamp(Timestamp):
    firebase.put('/Car',"Timestamp", Timestamp)

def putIntoFirebaseCarDoor_State_Rear_Left(Door_State_Rear_Left):
    firebase.put('/Car',"Door_State_Rear_Left", Door_State_Rear_Left)

def putIntoFirebaseCarFuel_Level_Critical(Fuel_Level_Critical):
    firebase.put('/Car',"Fuel_Level_Critical", Fuel_Level_Critical)

def putIntoFirebaseCarDoor_State_Rear_Right(Door_State_Rear_Right):
    firebase.put('/Car',"Door_State_Rear_Right", Door_State_Rear_Right)

def putIntoFirebaseCarVehicle_Speed(Vehicle_Speed):
    firebase.put('/Car',"Vehicle_Speed", Vehicle_Speed)

def putIntoFirebaseCarDoor_State_Front_Left(Door_State_Front_Left):
    firebase.put('/Car',"Door_State_Front_Left", Door_State_Front_Left)

def putIntoFirebaseCarIgnition_State(Ignition_State):
    firebase.put('/Car',"Ignition_State", Ignition_State)

def putIntoFirebaseCarTurn_Indicator_State(Turn_Indicator_State):
    firebase.put('/Car',"Turn_Indicator_State", Turn_Indicator_State)
