import threading
import time, urllib, json, urllib3, requests
import Firebase_util as fire
requests.packages.urllib3.disable_warnings()


def pushToFireBaseBulk(carData):
    fire.putIntoFirebaseCarBattery_Level(carData['Battery_Level'])
    fire.putIntoFirebaseCarHonk_State(carData['Honk_State'])
    fire.putIntoFirebaseCarFuel_Consumption(carData['Fuel_Consumption'])
    fire.putIntoFirebaseCarAccelerator_Pedal(carData['Accelerator_Pedal'])
    fire.putIntoFirebaseCarInside_Temperature(carData['Inside_Temperature'])
    fire.putIntoFirebaseCarFuel_Level(carData['Fuel_Level'])
    fire.putIntoFirebaseCarOutside_Air_Temperature(carData['Outside_Air_Temperature'])
    fire.putIntoFirebaseCarOdometer(carData['Odometer'])

    fire.putIntoFirebaseCarDoor_State_Front_Left(carData['Door_State_Front_Left'])
    fire.putIntoFirebaseCarDoor_State_Front_Right(carData['Door_State_Front_Right'])
    fire.putIntoFirebaseCarDoor_State_Rear_Left(carData['Door_State_Rear_Left'])
    fire.putIntoFirebaseCarDoor_State_Rear_Right(carData['Door_State_Rear_Right'])


    fire.putIntoFirebaseCarTire_Pressure_Front_Left(carData['Tire_Pressure_Front_Left'])
    fire.putIntoFirebaseCarTire_Pressure_Front_Right(carData['Tire_Pressure_Front_Right'])
    fire.putIntoFirebaseCarTire_Pressure_Rear_Left(carData['Tire_Pressure_Rear_Left'])
    fire.putIntoFirebaseCarTire_Pressure_Rear_Right(carData['Tire_Pressure_Rear_Right'])


    fire.putIntoFirebaseCarTimestamp(carData['Timestamp'])
    fire.putIntoFirebaseCarFuel_Level_Critical(carData['Fuel_Level_Critical'])
    fire.putIntoFirebaseCarVehicle_Speed(carData['Vehicle_Speed'])
    fire.putIntoFirebaseCarIgnition_State(carData['Turn_Indicator_State'])
    fire.putIntoFirebaseCarTurn_Indicator_State(carData['Turn_Indicator_State'])

class background_daemon(object):
    """ Threading example class

    The run() method will be started and it will run in the background
    until the application exits.
    """
 
    def __init__(self, interval=1):
        """ Constructor

        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval
 
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution
 
    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            url = "http://172.31.99.4/vehicle"
            response = urllib.urlopen(url);
            carData = json.loads(response.read())
            print('Doing something imporant in the background')
            pushToFireBaseBulk(carData)
            print "reporting finished"
            time.sleep(self.interval)


