import requests
import os
from dotenv import load_dotenv
from tools import download_picture


def get_epic_photos(api_key):
	params = {
		'api_key': api_key,
	}
	response = requests.get('https://api.nasa.gov/EPIC/api/natural', params=params)
	response.raise_for_status()
	for num,epic_image in enumerate(response.json()):
		date,time = epic_image["date"].split(" ")
		picture = epic_image
		year,month,day = date.split("-")
		link = "https://api.nasa.gov/Epic/archive/natural/{0}/{1}/{2}/png/{3}".format(year,month,day,picture)
		fname = "Nasa{0}.png".format(num)
		download_picture(link,fname,folder_name)


if __name__ == "__main__":
	load_dotenv()
    api_key = os.getenv("NASSA_API_KEY")
	folder_name = os.getenv("FOLDER_NAME")
	get_epic_photos(api_key)