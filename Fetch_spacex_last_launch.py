import requests
import os
from dotenv import load_dotenv
from tools import download_picture


def fetch_spacex_last_launch(launch_id,folder_name):
    url = 'https://api.spacexdata.com/v5/launches/{0}'.format(launch_id)
    response = requests.get(url)
    response.raise_for_status()
    answer = response.json()
    links = answer["links"]["flickr"]["original"]
    for num,link in enumerate(links):
        picture_name = "SpaceX{0}.jpg".format(num)
        download_picture(link,picture_name,folder_name)
        

def main():
    load_dotenv()
    launch_id = os.getenv("SPACEX_ID")
    folder_name = os.getenv("FOLDER_NAME")
    fetch_spacex_last_launch(launch_id,folder_name)
	

if __name__ == "__main__" :
   main()
