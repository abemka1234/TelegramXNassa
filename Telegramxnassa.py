from telegram import *
import requests
import os
import random
from dotenv import load_dotenv
import time

load_dotenv()
upload_frequency= os.getenv("UPL_FRQ")
TELEGRAM_ID = int(os.getenv("TELEGRAM_ID"))
Telegram_API = os.getenv("Telegram_API")
if upload_frequency == None:
	upload_frequency = 14400
bot = Bot(token=Telegram_API)
for root, dirs, files in os.walk('images'):
	random.shuffle(files)
	for image_name in files:
		image_path = os.path.join("images",image_name)
		with open(image_path,"rb") as f:
		    bot.send_photo(photo=f,chat_id=TELEGRAM_ID)
		time.sleep(upload_frequency)