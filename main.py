from instagrapi import Client
import os
import dotenv

dotenv.load_dotenv()

bot = Client()
bot.login(os.getenv("USER"), os.getenv("PASS"))

def photo_post(bot):
    print("Single photo upload")
    
    path = input("Enter path to photo, enter '~' to return to main menu: ")
    if path == '~':
        return
    
    caption = input("Enter photo caption, enter '~' to return to main menu: ")
    if caption == '~':
        return
    
    bot.photo_upload(path, caption)
    return

while True:
    print("-----Main Menu-----")
    print("1. Upload Single-Image Post")
    
    try:
        option = int(input("Enter option: "))
    except:
        print("Invalid Option")
    
    if option == 1:
        photo_post(bot)
    else:
        print("Invalid Option")