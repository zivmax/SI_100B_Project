import RPi.GPIO as GPIO
import time

BtnPin = 31

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BtnPin, GPIO.IN)
GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def getRespose(self):
    print("get Respose 1")


GPIO.add_event_detect(BtnPin, GPIO.FALLING)
GPIO.add_event_callback(BtnPin, getRespose)

print('start detecting for 4s')

while True:
    if GPIO.event_detected(BtnPin):
        print("event detected")

    time.sleep(4)
    print("restart detecting for 4s")
