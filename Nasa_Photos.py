import requests
import os
from dotenv import load_dotenv
from tools import download_picture


def get_expansion(filename):
	pathparts=os.path.splitext(filename)
	return pathparts[1]


def nasa_photos(api_key,folder_name,amount):
	params = {
		'api_key': api_key,
		'count': amount,
	}
	response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
	response.raise_for_status()
	answer = response.json()
	for num,photo in enumerate(answer):
		path = photo['hdurl']
		print(path)
		file_name = "Nassa{0}{1}".format(num,get_expansion(path))
		download_picture(path,file_name,"Pictures")


def main():
	load_dotenv()
	apod_api_key = os.getenv("APOD_API_KEY")
	amount = os.getenv("APOD_PICTURES_AMOUNT")
	path = os.getenv("FOLDER_NAME")
	nasa_photos(apod_api_key,'Nassa',amount,path)

	
if __name__ == "__main__":
	main()