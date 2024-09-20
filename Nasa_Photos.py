import requests
import os
from pprint import pprint
import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
def nasa_photos(api_key,name,amount):
	params = {
		'api_key': api_key,
		'count': amount,
	}
	response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
	answer = response.json()
	prname = name
	# pprint(answer)
	i=0
	for photo in answer:
		name=prname
		path = photo['hdurl']
		name= name+str(i)
		name = name+get_expansion(path)
		content= requests.get(path)
		fname = 'Nassa/{0}'.format(name)
		with open(fname, 'wb') as file:
			file.write(content.content)
		fname=""
		i+=1


def get_expansion(filename):
	pathparts=os.path.splitext(filename)
	return pathparts[1]
nasa_photos(API_KEY,'Nassa',1)