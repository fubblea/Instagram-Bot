from instagrapi import Client
import os
import dotenv
from datetime import datetime

dotenv.load_dotenv()

print("Logging in...")
bot = Client()
bot.login(os.getenv("USER"),os.getenv("PASS"))

def update_schedule(posts):
    os.remove('schedule.txt')
    with open('schedule.txt', 'w') as f:
        for post in posts:
            f.write(str(post))
            f.write('\n')

posts = []
print("Bot Running")
while True:
    with open('schedule.txt', 'r') as f:
        for line in f:
            if line != '':
                #TODO Albums path error
                line = line.rstrip()
                line = line.replace("'","")
                line = line.strip('][').split('. ')               
                posts.append(line)
    
    if len(posts) > 0:
        i=0
        length = len(posts)
        while i < length:
            scheduled_date = datetime.strptime(posts[i][0], '%m/%d/%y %H:%M:%S')
            if datetime.now() >= scheduled_date:
                if posts[i][1] == 'single_photo':
                    bot.photo_upload(path=posts[i][2], caption=posts[i][3])
                    print(f"Uploaded post scheduled for {scheduled_date}")
                    posts.pop(i)
                    update_schedule(posts)
                    i=0
                elif posts[i][1] == 'single_video':
                    bot.video_upload(path=posts[i][2], caption=posts[i][3])
                    print(f"Uploaded post scheduled for {scheduled_date}")
                    posts.pop(i)
                    update_schedule(posts)
                    i=0
                elif posts[i][1] == 'album':
                    paths = posts[i][2].strip('][').split(', ')  
                    bot.album_upload(paths, caption=posts[i][3])
                    print(f"Uploaded post scheduled for {scheduled_date}")
                    posts.pop(i)
                    update_schedule(posts)
                    i=0
            else:
                i+=1
            
            length = len(posts)