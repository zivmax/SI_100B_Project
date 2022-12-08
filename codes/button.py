import RPi.GPIO as GPIO
from time import sleep


def main():

    setup()

    detecting()





def setup():

    global BtnPin
    BtnPin = 31

    global LedPin
    LedPin = 33

    global Led_status
    Led_status = False


    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(LedPin, False)


def getRespose(ev=None):
    print("get Respose 1")


def detecting():

    GPIO.add_event_detect(BtnPin, GPIO.FALLING)
    GPIO.add_event_callback(BtnPin, getRespose)

    print('start detecting for 4s')

    while True:
        if GPIO.event_detected(BtnPin):
            print("event detected")

        sleep(4)
        print("restart detecting for 4s")



if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("")
