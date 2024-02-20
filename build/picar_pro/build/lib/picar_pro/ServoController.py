from adafruit_servokit import ServoKit
from time import sleep

kit = ServoKit(channels=16, frequency=50)

def move(servoPin, angle):
    kit.servo[servoPin].angle = angle
    
def main():
    move(0, 60)   

if __name__ == '__main__':
    main()