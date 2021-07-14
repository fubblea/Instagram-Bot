from instagrapi import Client
import os
import dotenv
from datetime import datetime

dotenv.load_dotenv()

print("Logging in...")
bot = Client()
bot.login(os.getenv("USER"),os.getenv("PASS"))

posts = []
print("Bot Running")
while len(posts) == 0:
    with open('schedule.txt', 'r') as f:
        for line in f:
            if line != '':
                line = line.rstrip()
                line = line.replace("'","")
                line = line.strip('][').split(', ')                   
                posts.append(line)
    
    if len(posts) > 0:
        for post in posts:
            if datetime.now() >= datetime.strptime(post[0], '%m/%d/%y %H:%M:%S'):
                print(post)