import RPi.GPIO as GPIO
from time import sleep
import pi_camera as pc

def main():

    setup()

    detecting_test()


def setup():
    global BtnPin
    BtnPin = 31

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def detecting_and_shoot(PATH):
    GPIO.add_event_detect(BtnPin, GPIO.FALLING, bouncetime=250)
    
    camera = pc.setup()
    camera.start_preview()

    while True:
        if GPIO.event_detected(BtnPin):
            path = pc.shoot(PATH)
        
            return path


def getRespose(ev=None):
    print("Get Respose 1")


def detecting_test():
    GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=getRespose, bouncetime=250)

    print('Start detecting for 4s')

    while True:

        sleep(4)
        if GPIO.event_detected(BtnPin):
            print("Event detected\n")
        else:
            print("No event detected\n")

        sleep(1)
        print("Restart detecting for 4s")



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("")
