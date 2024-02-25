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
    pwm.set_pwm(1, 0, 0)
    pwm.set_pwm(2, 0, 0)
    pwm.set_pwm(3, 0, 0)
    pwm.set_pwm(4, 0, 0)
    sleep(0.5)
