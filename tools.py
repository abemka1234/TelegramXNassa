import requests
import os


def download_picture(link,name,folder_name,api_key = ""):
    params = {
		'api_key': api_key,
	}
    picture_content = requests.get(link,params=params)
    picture_content.raise_for_status()
    os.makedirs(folder_name,exist_ok=True)
    file_path=os.path.join(folder_name,name)
    with open(file_path, 'wb') as file:
        file.write(picture_content.content) 