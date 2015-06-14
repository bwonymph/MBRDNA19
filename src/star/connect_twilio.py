from twilio.rest import TwilioRestClient
import Firebase_util as fire
import time

# put your own credentials here 
ACCOUNT_SID = "AC9920d26a6e014273f8704eb3ee500de2"
AUTH_TOKEN = "2b208c767753a358be86a29d541ea023"

TO_NUMBER = "+14242535865"

def send_msg():
    try:
        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
        client.messages.create(from_="+14124533008",
                               to=TO_NUMBER,
                               body="I am taking a Uber,"
                                    " keep an eye for me.")
        call = client.calls.create(from_="+14124533008",
                                   to=TO_NUMBER,
                                   url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient",
                                   method="GET",
                                   fallback_method="GET",
                                   status_callback_method="GET",
                                   record="false")

        print "Emergency call/msgs done from Twilio. call id:" + call.sid
        fire.putIntoFirebaseTwilio('Varun Ved', TO_NUMBER, time.time())
    except twilio.TwilioRestException as e:
        print e
