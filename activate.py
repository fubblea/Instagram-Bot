import dotenv
import os
from instagrapi import Client

dotenv.load_dotenv()

bot = Client()
bot.login(os.getenv("USER"), os.getenv("PASS"))