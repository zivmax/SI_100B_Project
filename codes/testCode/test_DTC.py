import time
import digital_tube_control as dtc
import RPi.GPIO as GPIO


def main():

    dtc.setup()
    dtc.check()
    dtc.refresh()

 
    dtc.display0()
    dtc.refresh()


 
    dtc.display1()
    dtc.refresh()



 
    dtc.display2()
    dtc.refresh()



 
    dtc.display3()
    dtc.refresh()



 
    dtc.display4()
    dtc.refresh()



 
    dtc.display5()
    dtc.refresh()



 
    dtc.display6()
    dtc.refresh()
   

    
    dtc.display7()
    dtc.refresh()


 
    dtc.display8()
    dtc.refresh()


 
    dtc.display9()
    dtc.refresh()



    GPIO.cleanup()


if __name__ == "__main__":
    main()
