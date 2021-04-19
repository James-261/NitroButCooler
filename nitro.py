import time
import sys
import psutil
from os import listdir
from os.path import isfile, join

try:
    from pynput import keyboard
except ImportError:
    print("Missing pynput, pip install pynput==1.6.8")
    time.sleep(1000)
    sys.exit()

try:
    import tkinter as tk
except ImportError:
    print("Missing tkinter, pip install tk")
    time.sleep(1000)
    sys.exit()

try:
    import tkinter.ttk as ttk
except ImportError:
    print("Missing ttk")
    time.sleep(1000)
    sys.exit()

try:
    import pyperclip
except ImportError:
    print("Missing pyperclip, pip install pyperclip")
    time.sleep(1000)
    sys.exit()

try:
    import os
except ImportError:
    print("Missing os, pip install os")
    time.sleep(1000)
    sys.exit()

COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(vk=162)}  # shift + control
]

class Widget(tk.Frame):
    def __init__(self, parent, abc, **kw):
        self.abc = abc
        tk.Frame.__init__(self, parent, **kw)
        self.b1 = tk.Button(self)
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        file_a = os.path.join(THIS_FOLDER, ("pack1\\" + abc))
        self.emojia = tk.PhotoImage(file=file_a)
        self.filename = (file_a.split("\\"))[-1]
        self.b1.configure(anchor='n', font='TkDefaultFont', image=self.emojia, text='AMOGUS', command=self.github)
        self.b1.pack(side='top')
    
    def quita(self):
        #self.destroy()
        sys.exit()

    def github(self):
        pyperclip.copy("https://raw.githubusercontent.com/James-261/nitrotest/main/" + self.filename)
        self.quita()
        #Widget.destroy(self)


def execute():
    if __name__ == '__main__':
        amogus = []
        root = tk.Tk()
        root.attributes('-topmost', True)
        root.update()
        root.attributes('-topmost', False)
        folder = os.path.dirname(os.path.abspath(__file__))
        #file_b = os.path.join(folder, "pack1\\emojis.txt")
        #emoji_list = open(file_b, "r")
        #amog = emoji_list.readlines()
        #for elem in amog:
            #amogus.extend(elem.strip().split('\n'))  
        amogus = os.listdir(folder + "\\pack1")
        print(amogus)
        for b in amogus:
            print(b)
            widget = Widget(root, b)
            widget.pack(expand=True, fill='both')
        root.mainloop()
        print("amogs")
        #root.destroy()    #Need to make it close the window after

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

pressed_vks = set()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()