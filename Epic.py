import requests
import os
from dotenv import load_dotenv
from tools import download_picture


def get_epic_photos(api_key,folder_name):
	params = {
		'api_key': api_key,
	}
	response = requests.get('https://api.nasa.gov/EPIC/api/natural', params=params)
	response.raise_for_status()
	for num,epic_image in enumerate(response.json()):
		date,time = epic_image["date"].split(" ")
		picture_name = epic_image["image"]
		year,month,day = date.split("-")
		link = "https://api.nasa.gov/EPIC/archive/natural/{0}/{1}/{2}/png/{3}.png".format(year,month,day,picture_name)
		fname = "Nasa{0}.png".format(num)
		download_picture(link,fname,folder_name,api_key)


def main():
	load_dotenv()
	api_key = os.getenv("APOD_API_KEY")
	folder_name = os.getenv("FOLDER_NAME")
	get_epic_photos(api_key,folder_name)


if __name__ == "__main__":
	main()