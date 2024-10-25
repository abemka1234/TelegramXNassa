from telegram import *
import os
import random
from dotenv import load_dotenv
import time


def main():
	load_dotenv()
	upload_frequency= os.getenv("UPL_FRQ")
	telegram_id = int(os.getenv("TELEGRAM_CHAT_ID"))
	telegram_api = os.getenv("TELEGRAM_API")
	folder_name = os.getenv("FOLDER_NAME")
	while True:
		bot = Bot(token=telegram_api)
		for root, dirs, files in os.walk(folder_name):
			random.shuffle(files)
			for image_name in files:
				image_path = os.path.join(folder_name,image_name)
				with open(image_path,"rb") as f:
					bot.send_photo(photo=f,chat_id=telegram_id)
				time.sleep(5)
		time.sleep(upload_frequency)


if __name__ == "__main__":
	main()