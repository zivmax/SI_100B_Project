import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, True)

time.sleep(10)

GPIO.output(11, False)
GPIO.cleanup()
