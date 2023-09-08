import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(4, GPIO.OUT)

pwm = GPIO.PWM(4, 50)
pwm.start(0)

def set_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(4, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(4, False)
    pwm.ChangeDutyCycle(0)

set_angle(45)
