from telegram import *
import requests
import os
import random
from dotenv import load_dotenv
import time
if __name__ == "__main__":
	main()
def main():
	load_dotenv()
	upload_frequency= os.getenv("UPL_FRQ")
	telegram_id = int(os.getenv("TELEGRAM_ID"))
	telegram_api = os.getenv("Telegram_API")
	if upload_frequency == None:
		upload_frequency = 14400
	bot = Bot(token=telegram_api)
	for root, dirs, files in os.walk('images'):
		random.shuffle(files)
		for image_name in files:
			image_path = os.path.join("images",image_name)
			with open(image_path,"rb") as f:
				bot.send_photo(photo=f,chat_id=telegram_id)
			time.sleep(upload_frequency)