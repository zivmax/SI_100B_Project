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
    GPIO.output(DCC, True)


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

    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, False)
    GPIO.output(F, False)
    GPIO.output(G, True)
    GPIO.output(DP, True)


def display1():

    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.output(A, True)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, True)
    GPIO.output(E, True)
    GPIO.output(F, True)
    GPIO.output(G, True)
    GPIO.output(DP, True)


def display2():

    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, True)
    GPIO.output(D, False)
    GPIO.output(E, False)
    GPIO.output(F, True)
    GPIO.output(G, False)
    GPIO.output(DP, False)


def display3():

    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, True)
    GPIO.output(F, True)
    GPIO.output(G, False)
    GPIO.output(DP, False)


def display4():

    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.output(A, True)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, True)
    GPIO.output(E, True)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(DP, False)


def display5():

    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.output(A, False)
    GPIO.output(B, True)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, True)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(DP, False)


def display6():

    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.output(A, False)
    GPIO.output(B, True)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, False)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(DP, False)


def display7():

    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, True)
    GPIO.output(E, True)
    GPIO.output(F, True)
    GPIO.output(G, True)
    GPIO.output(DP, False)


def display8():

    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, False)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(DP, False)


def display9():

    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, True)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(DP, False)
