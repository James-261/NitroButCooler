import psutil
import time
from pynput import keyboard
import os

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def execute():
    print("amogus?????")
    procname = "python.exe"
    for proc in psutil.process_iter():
        if proc.name() == procname:
            proc.kill()


def get_vk(key):
    return key.vk if hasattr(key, 'vk') else key.value.vk

def is_combination_pressed(combination):
    return all([get_vk(key) in pressed_vks for key in combination])

def on_press(key):
    vk = get_vk(key)  
    pressed_vks.add(vk)  

    for combination in COMBINATIONS:  
        if is_combination_pressed(combination):  
            execute()  
            break 

def on_release(key):
    vk = get_vk(key)  
    pressed_vks.remove(vk) 

os.system("C:\\Users\\Kids\\AppData\\Local\\Programs\\Python\\Python38\\pythonw.exe C:\\Users\\Kids\\Desktop\\Nitro\\NitroFinal\\nitro.py")

while True:
    if checkIfProcessRunning('pythonw'):
        pass
    else:
        os.system("C:\\Users\\Kids\\AppData\\Local\\Programs\\Python\\Python38\\pythonw.exe C:\\Users\\Kids\\Desktop\\Nitro\\NitroFinal\\nitro.py")


COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(vk=18)}  # control + alt
]

pressed_vks = set()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
