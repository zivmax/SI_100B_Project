import time
import digital_tube_control as dtc
import RPi.GPIO as GPIO


def main():

    dtc.check()

    dtc.setup()
    dtc.display0()
    GPIO.cleanup()

    dtc.set
    dtc.display1()
    GPIO.cleanup()

    dtc.set
    dtc.display2()
    GPIO.cleanup()

    dtc.set
    dtc.display3()
    GPIO.cleanup()

    dtc.set
    dtc.display4()
    GPIO.cleanup()

    dtc.set
    dtc.display5()
    GPIO.cleanup()

    dtc.set
    dtc.display6()
    GPIO.cleanup()

    dtc.set
    dtc.display7()
    GPIO.cleanup()

    dtc.set
    dtc.display8()
    GPIO.cleanup()

    dtc.set
    dtc.display9()
    GPIO.cleanup()


    GPIO.cleanup()


if __name__ == "__main__":
    main()
