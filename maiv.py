import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(10,GPIO.OUT)
GPIO.output(10,GPIO.HIGH)

import time

GPIO.output(18,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(10,GPIO.LOW)

try:
    while 1:
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(10,GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
