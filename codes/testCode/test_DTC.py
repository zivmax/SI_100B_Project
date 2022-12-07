import time
import digital_tube_control as dtc
import RPi.GPIO as GPIO


def main():

    dtc.setup()

    dtc.refresh()

    dtc.display0()
    time.sleep(3)

    GPIO.cleanup()
    dtc.setup()

    dtc.display1()
    time.sleep(3)


    GPIO.cleanup()
    dtc.setup()


    dtc.display2()
    time.sleep(3)


    GPIO.cleanup()
    dtc.setup()


    dtc.display3()
    time.sleep(3)


    GPIO.cleanup()
    dtc.setup()

    dtc.display4()

    GPIO.cleanup()
    dtc.setup()

    dtc.display5()

    dtc.display6()

    dtc.display7()

    dtc.display8()

    dtc.display9()

    GPIO.cleanup()

if __name__ == "__main__":
    main()
