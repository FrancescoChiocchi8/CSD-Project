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
right = 196 #124.5
straight = 316 #94.5
left = 436 #64.5

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
	
	pwm.set_pwm(0, 0, straight)

def turnWheels(turn):
	pwm.set_pwm(0, 0, turn)

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
	sleep(0.5)

def releaseMotors():
	motorStop()
	turnWheels(straight)
	GPIO.cleanup()

def move(speed, direction, turn, duration):
	setup()
	turnWheels(straight)

	if direction == 'forward':
		if turn == 'right': turnWheels(right)
		elif turn == 'left': turnWheels(left)

		sleep(0.5)
		motorForward(speed)

	elif direction == 'backward':
		if turn == 'right': turnWheels(right)
		elif turn == 'left': turnWheels(left)
		
		sleep(0.5)
		motorBackward(speed)

	sleep(duration)
	motorStop()
	releaseMotors()