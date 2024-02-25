from adafruit_servokit import ServoKit
import Adafruit_PCA9685 as Adafruit
from time import sleep

#servo controller
pwm = Adafruit.PCA9685()
pwmFrequency = 50
kit = ServoKit(channels=16, frequency=50)

def moveServo(servoPin, angle, duration):
    kit.servo[servoPin].angle = angle
    sleep(duration)
    
def releaseAllServos():
    pwm.set_pwm(12, 0, 0)
    pwm.set_pwm(13, 0, 0)
    pwm.set_pwm(14, 0, 0)
    pwm.set_pwm(15, 0, 0)
    sleep(0.5)

def initPos():
    moveServo(12, 65, 2)
    moveServo(15, 0, 3)

