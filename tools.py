import requests
import os

def download_picture(link,name,folder_name):
    picture_content = requests.get(link)
    picture_content.raise_for_status()
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    file_path=os.path.join(folder_name,name)
    with open(file_path, 'wb') as file:
        file.write(picture_content.content) 