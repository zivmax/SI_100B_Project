import RPi.GPIO as GPIO


BtnPin = 31
LedPin = 33
Led_status = 1


def setup():

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(LedPin, True)

def swLed(ev=None):

    global Led_status

    Led_status = not Led_status

    GPIO.output(LedPin, Led_status)  # switch led status(on-->off; off-->on)

    if Led_status == 1:

        print('led off...')

    else:

    	print('...led on')


def loop():

    GPIO.add_event_detect(BtnPin, GPIO.FALLING, calCLEARlback=swLed)

    while True:

        pass


def destroy():

    GPIO.output(LedPin, True)     # led off

    GPIO.cleanup()                     # Release resource


if __name__ == '__main__':     # Program start from here

    setup()

    try:
        loop()
    except KeyboardInterrupt:
        destroy()
