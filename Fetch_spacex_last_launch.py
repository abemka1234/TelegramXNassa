import requests
import os
from dotenv import load_dotenv

load_dotenv()
ID = os.getenv("ID")
def fetch_spacex_last_launch(id_of_launch):
	if id_of_launch == '':
		id_of_launch = 'latest'
	response=requests.get('https://api.spacexdata.com/v5/launches/{0}'.format(id_of_launch))
	answer = response.json()
	links = answer["links"]["flickr"]["original"]
	# print(links)
	i = 0
	for link in links:
		content= requests.get(link)
		name = 'images/spacex_{0}.jpg'.format(i)
		i=i+1
		with open(name, 'wb') as file:
			file.write(content.content)
fetch_spacex_last_launch(ID)
