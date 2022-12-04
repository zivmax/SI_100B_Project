# General purpose
import os
import numpy as np
from time import sleep
import time

# GPIO related
import RPi.GPIO as GPIO

# camera related
from picamera import PiCamera, Color

# GPIO mode: GPIO.BOARD, GPIO.BCM
GPIO.setmode(GPIO.BOARD)
mode = GPIO.getmode()
# Close GPIO warning
GPIO.setwarnings(False)

# get the project path
PRJ_PATH = os.getcwd()

def image_split_column(a)->list:
    """
    Function description: Split the image by column.
    Tips:
    1. Calculate the number of elements with a value of 255 in each column.
    2. When the number of 255 changes from zero to non-zero, it indicates the beginning of the digits area. Use startList to record the starting column index.
    3. When the number of 255 changes from non-zero to zero, it indicates the end of the digits area. Use endList to record the end column index.
    4. Use flag to represent the current state, outside or inside the digits area.
    
    :param img: input image to be splited by column.
    :return: output image after splited by column. It is a list, but its elements are np.ndarray.
    """
    
    ### write your codes here ###
    #############################
    n = 0
    white = []
    black = []
    white_max = 0
    black_max = 0
    (height, width) = a.shape
    startList = []
    endList = []
    ret = []
    for i in range(width):
        s = 0
        t = 0
        for j in range(height):
            if a[j][i] == 255:
                s += 1
            if a[j][i] == 0:
                t += 1
        white_max = max(white_max, s)
        black_max = max(black_max, t)
        white.append(s)
        black.append(t)
    for j in range(0, len(a)-1):
        if a[j] == 0 and a[j+1] != 0:
            startList.append(j)
    for k in range(0, len(a)-1):
        if a[k] != 0 and a[k+1] == 0:
            endList.append(k)
    for l in range(0, len(startlist)):
        ret.append(a[startList[l]:endList[l], :])

    return ret



def image_split_row(a)->list:
    """
    Function description: Split the image by row.
    Tips:
    1. Calculate the number of elements with a value of 255 in each row.
    2. When the number of 255 changes from zero to non-zero, it indicates the beginning of the digits area. Use startList to record the starting row index.
    3. When the number of 255 changes from non-zero to zero, it indicates the end of the digits area. Use endList to recorder the end row index.
    4. Use flag to represent the current state, outside or inside the digits area.
    
    :param img: input image to be splited by row.
    :return: output image after splited by row. It is a list, but its elements are np.ndarray.
    """
    
    ### write your codes here ###
    #############################
    n = 0
    startList = []
    endList = []
    ret = []
    for i in a:
        if i == 255:
            n += 1
    for j in range(0, len(a) - 1):
        if a[j] == 0 and a[j + 1] != 0:
            startList.append(j)
    for k in range(0, len(a) - 1):
        if a[k] != 0 and a[k + 1] == 0:
            endList.append(k)
    for l in range(0, len(startlist)):
        ret.append(a[:, startList[l]:endList[l]])

    return ret




def led_display(numList:list)->None:
    """
    Function description: Build a digital tube display circuit on the breadboard. Display the result with the digital tube.
    Tips:
    1.The GPIO mode we used is GPIO.BOARD. 
    2.The digital tube is common anode. Use GPIO port to input high level for digital tube power pin.
    3. After the LED lamp pin of the digital tube is connected to the GPIO pin, the corresponding relationship can be confirmed by lighting the led one by one.
    4. Check "function introduction.xlsx" for GPIO functions.
    
    :para numList: input numbers in list to be displayed.
    :return: None
    """

    ### write your codes here ###
    #############################87----    # step 1:
    # Clarify the relationship between led pins and GPIO pins
    # Set the GPIO pins to GPIO.OUT mode and give them the right output
    
    
    
    
    
    # step 2:
    # Clarify the led composition of each number
    
    
    
    
        
    # step 3:
    # Display the numbers in the list one by one
    # Display every number for 1 second
    # Wait two seconds when displaying different lines
    
    
    
    
    ret = None
    return ret


def take_photo()->str:
    """
    Function description: Build the camera control circuit on the breadboard. After pressing the control button, the shooting indicator(led light) lights up and the camera takes a picture.
    Tips:
    1. Use the 3.3v and GND pins on the Raspberry Pi as the power and ground of the circuit.
    2. Use the GPIO port as a signal line to sense the occurrence of key events. Set the correct GPIO mode
    3. Create a camera obj and wait for a button press to take a photo.
    4. Save the picture to /UserData/.
    5. Clean the camera.
    
    :para
    :return: a string which contains the picture location
    """

    ### write your codes here ###
    #############################
    # step 1: 
    #set a GPIO as an input channel for detecting
    
    
    
    
    
    
    
    
    # step 2: 
    # create the camera obj and wait for a button to take a photo
    # recorder the saving path
    # clear the camera
    
    
    
    
    
    
    # step3:
    # return the saving path
    
    
    
    
    ret = None
    return ret