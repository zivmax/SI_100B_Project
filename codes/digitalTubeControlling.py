Marsh_Mallow 2022/11/30 22:48:04


22-豫-CS-杨润康 13:32:26
import RPi.GPIO as GPIO
import time

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



def Act0():
    GPIO.output(DCC, True)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, False)
    GPIO.output(F, False)
    GPIO.output(G, True)
    GPIO.output(DP, False)
    time.sleep(5)
    GPIO.cleanup()
def Act1():
    GPIO.output(DCC, True)
    GPIO.output(A, True)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, True)
    GPIO.output(E, True)
    GPIO.output(F, True)
    GPIO.output(G, True)
    GPIO.output(DP, False)
    time.sleep(5)
    GPIO.cleanup()
def Act2():
    GPIO.output(DCC, True)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, True)
    GPIO.output(D, False)
    GPIO.output(E, False)
    GPIO.output(F, True)
    GPIO.output(G, False)
    GPIO.output(DP, False)
    time.sleep(5)
    GPIO.cleanup()
def Act3():
    GPIO.output(DCC, True)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, True)
    GPIO.output(F, True)
    GPIO.output(G, False)
    GPIO.output(DP, False)
    time.sleep(5)
    GPIO.cleanup()
def Act4():
    GPIO.output(DCC, True)
    GPIO.output(A, True)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, True)
    GPIO.output(E, True)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(DP, False)
    time.sleep(5)
    GPIO.cleanup()
def Act5():
    GPIO.output(DCC, True)
    GPIO.output(A, False)
    GPIO.output(B, True)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, True)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(DP, False)
    time.sleep(5)
    GPIO.cleanup()
def Act6():
    GPIO.output(DCC, True)
    GPIO.output(A, False)
    GPIO.output(B, True)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, False)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(DP, False)
    time.sleep(5)
    GPIO.cleanup()
def Act7():
    GPIO.output(DCC, True)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, True)
    GPIO.output(E, True)
    GPIO.output(F, True)
    GPIO.output(G, True)
    GPIO.output(DP, False)
    time.sleep(5)
    GPIO.cleanup()
def Act8():
    GPIO.output(DCC, True)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, False)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(DP, False)
    time.sleep(5)
    GPIO.cleanup()
def Act9():
    GPIO.output(DCC, True)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, True)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(DP, False)
    time.sleep(5)
    GPIO.cleanup()

