import time
import digital_tube_control as dtc
import RPi.GPIO as GPIO

GPIO.cleanup()

dtc.setup()
dtc.display9()
time.sleep(1)

GPIO.cleanup()
