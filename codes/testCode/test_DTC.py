import time
import digital_tube_control as dtc
import RPi.GPIO as GPIO


def main():

    dtc.setup()
    dtc.check()
    dtc.refresh()

 
    dtc.display0()
    dtc.refresh()
    time.sleep(1)

 
    dtc.display1()
    dtc.refresh()
    time.sleep(1)


 
    dtc.display2()
    dtc.refresh()
    time.sleep(1)


 
    dtc.display3()
    dtc.refresh()
    time.sleep(1)


 
    dtc.display4()
    dtc.refresh()
    time.sleep(1)


 
    dtc.display5()
    dtc.refresh()
    time.sleep(1)


 
    dtc.display6()
    dtc.refresh()
    time.sleep(1)   

    
    dtc.display7()
    dtc.refresh()
    time.sleep(1)

 
    dtc.display8()
    dtc.refresh()
    time.sleep(1)

 
    dtc.display9()
    dtc.refresh()
    time.sleep(1)


    GPIO.cleanup()


if __name__ == "__main__":
    main()
