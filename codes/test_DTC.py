import time
import digital_tube_control as dtc
import RPi.GPIO as GPIO


def main():


    dtc.setup()
    dtc.display0()
    time.sleep(2)
    GPIO.cleanup()


    dtc.display1()
    time.sleep(2)
    GPIO.cleanup()


    dtc.display2()
    time.sleep(2)
    GPIO.cleanup()


    dtc.display3()
    time.sleep(2)
    GPIO.cleanup()


    dtc.display4()
    time.sleep(2)
    GPIO.cleanup()


    dtc.display5()
    time.sleep(2)
    GPIO.cleanup()


    dtc.display6()
    time.sleep(2)
    GPIO.cleanup()


    dtc.display7()
    time.sleep(2)
    GPIO.cleanup()


    dtc.display8()
    time.sleep(2)
    GPIO.cleanup()


    dtc.display9()
    time.sleep(2)
    GPIO.cleanup()




if __name__ == "__main__":
    main()
