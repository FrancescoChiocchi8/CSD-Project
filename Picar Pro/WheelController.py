from time import sleep
import RPi.GPIO as GPIO
import Adafruit_PCA9685 as Adafruit

#servo controller
pwm = Adafruit.PCA9685()
pwmFrequency = 50

#board pins
wheelServoPin = 0
RightMotorPin = 4
LeftMotorPin = 17
RightWheelPin1 = 26
RightWheelPin2 = 21
LeftWheelPin1 = 27
LeftWheelPin2 = 18

#motors directions
forward = 1
backward = 0

#wheelServo positions
left = 150
straight = 300
right = 450

#setup motors
def setup():
	global pwmR, pwmL
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(RightMotorPin, GPIO.OUT)
	GPIO.setup(LeftMotorPin, GPIO.OUT)
	GPIO.setup(RightWheelPin1, GPIO.OUT)
	GPIO.setup(RightWheelPin2, GPIO.OUT)
	GPIO.setup(LeftWheelPin1, GPIO.OUT)
	GPIO.setup(LeftWheelPin2, GPIO.OUT)

	try:
		pwm.set_pwm_freq(pwmFrequency)
		pwmR = GPIO.PWM(RightMotorPin, 1000)
		pwmL = GPIO.PWM(LeftMotorPin, 1000)
	except:
		pass

#move motors forward
def motorForward(speed):
	GPIO.output(LeftWheelPin1, GPIO.LOW)
	GPIO.output(LeftWheelPin2, GPIO.HIGH)
	GPIO.output(RightWheelPin1, GPIO.LOW)
	GPIO.output(RightWheelPin2, GPIO.HIGH)

	pwmL.start(speed)
	pwmR.start(speed)

#move motors backward
def motorBackward(speed):
	GPIO.output(LeftWheelPin1, GPIO.HIGH)
	GPIO.output(LeftWheelPin2, GPIO.LOW)
	GPIO.output(RightWheelPin1, GPIO.HIGH)
	GPIO.output(RightWheelPin2, GPIO.LOW)

	pwmL.start(speed)
	pwmR.start(speed)

#stop motors
def motorStop():
	GPIO.output(RightWheelPin1, GPIO.LOW)
	GPIO.output(RightWheelPin2, GPIO.LOW)
	GPIO.output(LeftWheelPin1, GPIO.LOW)
	GPIO.output(LeftWheelPin2, GPIO.LOW)
	GPIO.output(RightMotorPin, GPIO.LOW)
	GPIO.output(LeftMotorPin, GPIO.LOW)
	pwm.set_pwm(0, 0, 0)
	pwm.set_pwm(1, 0, 0)
	pwm.set_pwm(2, 0, 0)
	pwm.set_pwm(3, 0, 0)
	pwm.set_pwm(4, 0, 0)
	sleep(0.5)

#release resource
def releaseMotors():
	motorStop()
	GPIO.cleanup()

def move(speed, direction, turn, duration):
	if direction == 'forward':
		if turn == 'right': pwm.set_pwm(wheelServoPin, 0, right)
		elif turn == 'left': pwm.set_pwm(wheelServoPin, 0, left)

		sleep(0.5)
		motorForward(speed)

	elif direction == 'backward':
		if turn == 'right': pwm.set_pwm(wheelServoPin, 0, right)
		elif turn == 'left': pwm.set_pwm(wheelServoPin, 0, left)
		
		sleep(0.5)
		motorBackward(speed)

	else:
		motorStop()

	sleep(duration)
	pwm.set_pwm(wheelServoPin, 0, straight)
	motorStop()

if __name__ == '__main__':
	try:
		setup()
		
		#move(speed, 'forward'/'backward', 'left'/'right'/'', duration)
		#move(100, 'forward', 'right', 0.5)
		#move(100, 'forward', 'left', 0.5)
		#move(100, 'backward', '', 1)
		
		releaseMotors()
	except KeyboardInterrupt:
		releaseMotors()