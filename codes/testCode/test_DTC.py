import time
import digital_tube_control as dtc
import RPi.GPIO as GPIO


def main():

    dtc.setup()
    dtc.display0()
    time.sleep(3)
    GPIO.cleanup()

    dtc.setup()
    dtc.display3()
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
    time.sleep(3)
    GPIO.cleanup()


    dtc.setup()
    dtc.display5()
    time.sleep(3)
    GPIO.cleanup()


    dtc.setup()
    dtc.display6()
    time.sleep(3)   
    GPIO.cleanup()

    dtc.setup()   
    dtc.display7()
    time.sleep(3)
    GPIO.cleanup()

    dtc.setup()
    dtc.display8()
    time.sleep(3)
    GPIO.cleanup()

    dtc.setup()
    dtc.display9()
    time.sleep(3)
    GPIO.cleanup()





if __name__ == "__main__":
    main()
