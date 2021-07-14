import tkinter as tk
from tkinter import filedialog
import time_picker
import os
import sys

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
    
    with open('schedule.txt', 'a') as f:
        f.write(f"[{date}. 'album'. {path}. {caption}]" + '\n')
    return

def video_post():
    print("Single video upload")
    print("Select media")
    
    path = find_single_media()
    if path == '':
        return
    
    caption = input("Enter video caption, enter '~' to return to main menu: ")
    if caption == '~':
        return
    
    time_picker.pick()
    
    with open('temp.txt', 'r') as f:
        date = f.read()
    os.remove('temp.txt')
    
    with open('schedule.txt', 'a') as f:
        f.write(f"[{date}. 'album'. {path}. {caption}]" + '\n')
    return

def album_post():
    print("Album upload")
    print("Select media")
    
    path = find_multiple_media()
    if path == '':
        return
    
    caption = input("Enter album caption, enter '~' to return to main menu: ")
    if caption == '~':
        return
    
    time_picker.pick()
    
    with open('temp.txt', 'r') as f:
        date = f.read()
    os.remove('temp.txt')
    
    with open('schedule.txt', 'a') as f:
        f.write(f"[{date}. 'album'. {path}. {caption}]" + '\n')
    return

while True:
    print("-----Main Menu-----")
    print("0. Exit")
    print("1. Schedule Single-Image Post")
    print("2. Schedule Single-Video Post")
    print("3. Schedule Album Post")
    
    try:
        option = int(input("Enter option: "))
    except:
        print("Invalid Option")
    
    if option == 0:
        sys.exit()
    elif option == 1:
        photo_post()
    elif option == 2:
        video_post()
    elif option == 3:
        album_post()
    else:
        print("Invalid Option")