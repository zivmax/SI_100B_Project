import RPi.GPIO as GPIO
import time


def setup():

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
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


def refresh():

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.output(DCC, False)
    GPIO.output(A, True)
    GPIO.output(B, True)
    GPIO.output(C, True)
    GPIO.output(D, True)
    GPIO.output(E, True)
    GPIO.output(F, True)
    GPIO.output(G, True)
    GPIO.output(DP, True)


def display0():

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.output(DCC, True)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, False)
    GPIO.output(F, False)
    GPIO.output(G, True)
    GPIO.output(DP, True)

    time.sleep(1)


def display1():

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22


    GPIO.output(DCC, True)
    GPIO.output(A, True)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, True)
    GPIO.output(E, True)
    GPIO.output(F, True)
    GPIO.output(G, True)
    GPIO.output(DP, True)

    time.sleep(1)


def display2():

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.output(DCC, True)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, True)
    GPIO.output(D, False)
    GPIO.output(E, False)
    GPIO.output(F, True)
    GPIO.output(G, False)
    GPIO.output(DP, False)

    time.sleep(1)



def display3():

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.output(DCC, True)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, True)
    GPIO.output(F, True)
    GPIO.output(G, False)
    GPIO.output(DP, False)

    time.sleep(1)



def display4():

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.output(DCC, True)
    GPIO.output(A, True)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, True)
    GPIO.output(E, True)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(DP, False)

    time.sleep(1)



def display5():

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.output(DCC, True)
    GPIO.output(A, False)
    GPIO.output(B, True)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, True)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(DP, False)

    time.sleep(1)



def display6():

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.output(DCC, True)
    GPIO.output(A, False)
    GPIO.output(B, True)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, False)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(DP, False)

    time.sleep(1)



def display7():

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.output(DCC, True)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, True)
    GPIO.output(E, True)
    GPIO.output(F, True)
    GPIO.output(G, True)
    GPIO.output(DP, False)

    time.sleep(1)



def display8():

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.output(DCC, True)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, False)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(DP, False)

    time.sleep(1)



def display9():

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.output(DCC, True)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, True)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(DP, False)

    time.sleep(1)
