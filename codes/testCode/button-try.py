import RPi.GPIO as GPIO


BtnPin = 31
LedPin = 33
Led_status = False


def main():

    setup()

    loop()


def setup():

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(LedPin, False)


def swLed(ev=None):

    global Led_status

    Led_status = not Led_status

    GPIO.output(LedPin, Led_status)

    if Led_status == False:

        print('led off...')

    else:

    	print('...led on')


def loop():

    GPIO.add_event_detect(BtnPin, GPIO.FALLING)
    GPIO.add_event_callback(BtnPin, swLed)

    while True:

        pass


if __name__ == '__main__':     # Program start from here

    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("")
