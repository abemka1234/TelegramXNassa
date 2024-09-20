from telegram import *
import requests
import os
from pprint import pprint
import datetime
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
while True:
	t = time.localtime()
	k = random.randint(1,3)
	if k == 1:
		i=os.listdir(path='images/')[random.randint(0,len(os.listdir(path='images/'))-1)]
		i = "images/" + i
		print("Публикую фото:",i,time.strftime("%H:%M:%S", t))
		with open(i,"rb") as f:
		    bot.send_photo(photo=f,chat_id=TELEGRAM_ID)
	if k==2:
		i = os.listdir(path='Nassa/')[random.randint(0,len(os.listdir(path='Nassa/'))-1)]
		i = "Nassa/" + i
		print("Публикую фото:",i,time.strftime("%H:%M:%S", t))
		with open(i,"rb") as f:
		    bot.send_photo(photo=f,chat_id=TELEGRAM_ID)
	if k==3:
		i = os.listdir(path='Epic/')[random.randint(0,len(os.listdir(path='Epic/'))-1)]
		i = "Epic/" + i
		print("Публикую фото:",i,time.strftime("%H:%M:%S", t))
		with open(i,"rb") as f:
		    bot.send_photo(photo=f,chat_id=TELEGRAM_ID)
	time.sleep(int(upload_frequency))