import RPi.GPIO as GPIO
import time

TriggerPin = 11
EchoPin = 8

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TriggerPin, GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(EchoPin, GPIO.IN)

#check distance
def checkdist():
    GPIO.output(TriggerPin, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(TriggerPin, GPIO.LOW)
    while not GPIO.input(EchoPin):
        pass
    t1 = time.time()
    while GPIO.input(EchoPin):
        pass
    t2 = time.time()
    return round((t2-t1)*340/2,2)