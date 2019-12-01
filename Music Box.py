import time
import pyautogui
import serial
 
ArduinoSerial = serial.Serial('COM8', 9600)
prev ='z'
while True:
    x = ArduinoSerial.readline().decode('ascii')
    print(x)
    # l="abcdefghij"
    if "L" in x:
        pyautogui.hotkey('pgup')
        print(x)
    elif "R" in x:
        print(x)
        pyautogui.hotkey('pgdwn')
    elif (x < prev):
        pyautogui.hotkey('up')
        # pyautogui.hotkey('up')
        # pyautogui.hotkey('up')
        pyautogui.hotkey('up')
        print("l")
    elif(prev < x):
        # pyautogui.hotkey('down')
        # pyautogui.hotkey('down')
        pyautogui.hotkey('down')
        pyautogui.hotkey('down')
        print("r")
    prev = x
