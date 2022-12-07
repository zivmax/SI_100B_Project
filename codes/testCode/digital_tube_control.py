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


def refresh(t = 0.1):

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22



    GPIO.output(DCC, GPIO.LOW)
    GPIO.output(A, GPIO.HIGH)
    GPIO.output(B, GPIO.HIGH)
    GPIO.output(C, GPIO.HIGH)
    GPIO.output(D, GPIO.HIGH)
    GPIO.output(E, GPIO.HIGH)
    GPIO.output(F, GPIO.HIGH)
    GPIO.output(G, GPIO.HIGH)
    GPIO.output(DP, GPIO.HIGH)

    time.sleep(t)



def check(t = 1):

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22



    GPIO.output(DCC, GPIO.HIGH)
    GPIO.output(A, GPIO.LOW)
    GPIO.output(B, GPIO.LOW)
    GPIO.output(C, GPIO.LOW)
    GPIO.output(D, GPIO.LOW)
    GPIO.output(E, GPIO.LOW)
    GPIO.output(F, GPIO.LOW)
    GPIO.output(G, GPIO.LOW)
    GPIO.output(DP, GPIO.LOW)

    time.sleep(t)



def display0(t = 1):

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22



    GPIO.output(DCC, GPIO.HIGH)
    GPIO.output(A, GPIO.LOW)
    GPIO.output(B, GPIO.LOW)
    GPIO.output(C, GPIO.LOW)
    GPIO.output(D, GPIO.LOW)
    GPIO.output(E, GPIO.LOW)
    GPIO.output(F, GPIO.LOW)
    GPIO.output(G, GPIO.HIGH)
    GPIO.output(DP, GPIO.HIGH)

    time.sleep(t)


def display1(t = 1):

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22



    GPIO.output(DCC, GPIO.HIGH)
    GPIO.output(A, GPIO.HIGH)
    GPIO.output(B, GPIO.LOW)
    GPIO.output(C, GPIO.LOW)
    GPIO.output(D, GPIO.HIGH)
    GPIO.output(E, GPIO.HIGH)
    GPIO.output(F, GPIO.HIGH)
    GPIO.output(G, GPIO.HIGH)
    GPIO.output(DP, GPIO.HIGH)

    time.sleep(t)


def display2(t = 1):

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22



    GPIO.output(DCC, GPIO.HIGH)
    GPIO.output(A, GPIO.LOW)
    GPIO.output(B, GPIO.LOW)
    GPIO.output(C, GPIO.HIGH)
    GPIO.output(D, GPIO.LOW)
    GPIO.output(E, GPIO.LOW)
    GPIO.output(F, GPIO.HIGH)
    GPIO.output(G, GPIO.LOW)
    GPIO.output(DP, GPIO.HIGH)

    time.sleep(t)



def display3(t = 1):

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22



    GPIO.output(DCC, GPIO.HIGH)
    GPIO.output(A, GPIO.LOW)
    GPIO.output(B, GPIO.LOW)
    GPIO.output(C, GPIO.LOW)
    GPIO.output(D, GPIO.LOW)
    GPIO.output(E, GPIO.HIGH)
    GPIO.output(F, GPIO.HIGH)
    GPIO.output(G, GPIO.LOW)
    GPIO.output(DP, GPIO.HIGH)

    time.sleep(t)



def display4(t = 1):

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.output(DCC, GPIO.HIGH)
    GPIO.output(A, GPIO.HIGH)
    GPIO.output(B, GPIO.LOW)
    GPIO.output(C, GPIO.LOW)
    GPIO.output(D, GPIO.HIGH)
    GPIO.output(E, GPIO.HIGH)
    GPIO.output(F, GPIO.LOW)
    GPIO.output(G, GPIO.LOW)
    GPIO.output(DP, GPIO.HIGH)

    time.sleep(t)



def display5(t = 1):

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22



    GPIO.output(DCC, GPIO.HIGH)
    GPIO.output(A, GPIO.LOW)
    GPIO.output(B, GPIO.HIGH)
    GPIO.output(C, GPIO.LOW)
    GPIO.output(D, GPIO.LOW)
    GPIO.output(E, GPIO.HIGH)
    GPIO.output(F, GPIO.LOW)
    GPIO.output(G, GPIO.LOW)
    GPIO.output(DP, GPIO.HIGH)

    time.sleep(t)



def display6(t = 1):

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22



    GPIO.output(DCC, GPIO.HIGH)
    GPIO.output(A, GPIO.LOW)
    GPIO.output(B, GPIO.HIGH)
    GPIO.output(C, GPIO.LOW)
    GPIO.output(D, GPIO.LOW)
    GPIO.output(E, GPIO.LOW)
    GPIO.output(F, GPIO.LOW)
    GPIO.output(G, GPIO.LOW)
    GPIO.output(DP, GPIO.HIGH)

    time.sleep(t)



def display7(t = 1):

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22



    GPIO.output(DCC, GPIO.HIGH)
    GPIO.output(A, GPIO.LOW)
    GPIO.output(B, GPIO.LOW)
    GPIO.output(C, GPIO.LOW)
    GPIO.output(D, GPIO.HIGH)
    GPIO.output(E, GPIO.HIGH)
    GPIO.output(F, GPIO.HIGH)
    GPIO.output(G, GPIO.HIGH)
    GPIO.output(DP, GPIO.HIGH)

    time.sleep(t)



def display8(t = 1):

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22



    GPIO.output(DCC, GPIO.HIGH)
    GPIO.output(A, GPIO.LOW)
    GPIO.output(B, GPIO.LOW)
    GPIO.output(C, GPIO.LOW)
    GPIO.output(D, GPIO.LOW)
    GPIO.output(E, GPIO.LOW)
    GPIO.output(F, GPIO.LOW)
    GPIO.output(G, GPIO.LOW)
    GPIO.output(DP, GPIO.HIGH)

    time.sleep(t)



def display9(t = 1):

    DCC = 7
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22



    GPIO.output(DCC, GPIO.HIGH)
    GPIO.output(A, GPIO.LOW)
    GPIO.output(B, GPIO.LOW)
    GPIO.output(C, GPIO.LOW)
    GPIO.output(D, GPIO.LOW)
    GPIO.output(E, GPIO.HIGH)
    GPIO.output(F, GPIO.LOW)
    GPIO.output(G, GPIO.LOW)
    GPIO.output(DP, GPIO.HIGH)

    time.sleep(t)
