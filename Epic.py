import requests
import os
import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
def get_expansion(filename):
	pathparts=os.path.splitext(filename)
	return pathparts[1]
def EPIC(api_key):
	response = requests.get('https://api.nasa.gov/EPIC/api/natural?api_key=9g0e8P6Ah5N5SJpPV33t0TtNuhjRG7JbUp4LVxYe')
	for num,i in enumerate(response.json()):
		b=i['date']
		c=i['image'] 
		d = datetime.datetime.fromisoformat(b)
		f = d.month
		g = d.day
		if f<10:
			f='0'+str(f)
		else:
			f=str(f)
		if g<10:
			g='0'+str(g)
		else:
			g=str(g)
		part = str(d.year) + '/'+ f + '/'+ g +'/png/'+ c +'.png'+'?api_key={0}'.format(api_key)
		h = 'https://api.nasa.gov/EPIC/archive/natural/{0}'.format(part)
		content= requests.get(h)
		fname = 'images/Nasa{0}.png'.format(num)
		with open(fname, 'wb') as file:
			file.write(content.content)
		fname=""
EPIC(API_KEY)