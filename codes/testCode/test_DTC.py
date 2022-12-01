import RPi.GPIO as GPIO
import time
import digital_tube_control as dtc


def main():


    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 21
    DP = 22

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(DCC, GPIO.OUT)
    GPIO.setup(A, GPIO.OUT)
    GPIO.setup(B, GPIO.OUT)
    GPIO.setup(C, GPIO.OUT)
    GPIO.setup(D, GPIO.OUT)
    GPIO.setup(E, GPIO.OUT)
    GPIO.setup(F, GPIO.OUT)
    GPIO.setup(G, GPIO.OUT)
    GPIO.setup(DP, GPIO.OUT)    
    

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
