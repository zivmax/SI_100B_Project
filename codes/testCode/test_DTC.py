import digital_tube_control as dtc
import RPi.GPIO as GPIO
import time


def main():

    dtc.setup()
    
    dtc.display0()
    time.sleep(1)

    dtc.display1()
    time.sleep(1)

    dtc.display2()
    time.sleep(1)

    dtc.display3()
    time.sleep(1)

    dtc.display4()
    time.sleep(1)

    dtc.display5()
    time.sleep(1)

    dtc.display6()
    time.sleep(1)

    dtc.display7()
    time.sleep(1)

    dtc.display8()
    time.sleep(1)

    dtc.display9()
    time.sleep(1)


if __name__ == "__main__":
    main()
