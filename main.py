from instabot import Bot
import os
import dotenv

dotenv.load_dotenv()

bot = Bot()
bot.login(username=os.getenv("USER"), password=os.getenv("PASS"))
user_id = bot.get_user_id_from_username("lego")
user_info = bot.get_user_info(user_id)
print(user_info['biography'])