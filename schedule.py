from datetime import time
import tkinter as tk
from tkinter import filedialog
import time_picker
import os

def find_single_media():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    return file_path

def find_multiple_media():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilenames()
    return list(file_path)

def photo_post():
    print("Single photo upload")
    print("Select media")
    
    path = find_single_media()
    if path == '':
        return
    
    caption = input("Enter photo caption, enter '~' to return to main menu: ")
    if caption == '~':
        return
    
    time_picker.pick()
    with open('temp.txt', 'r') as f:
        date = f.read()
    os.remove('temp.txt')
    
    with open('schedule.txt', 'w') as f:
        f.write(str([date, 'single_photo', path, caption]))
    return

while True:
    print("-----Main Menu-----")
    print("1. Schedule Single-Image Post")
    
    try:
        option = int(input("Enter option: "))
    except:
        print("Invalid Option")
    
    if option == 1:
        photo_post()
    else:
        print("Invalid Option")