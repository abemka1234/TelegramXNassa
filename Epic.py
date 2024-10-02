import requests
import os
from dotenv import load_dotenv


def get_expansion(filename):
    pathparts = os.path.splitext(filename)
    return pathparts[1]


def EPIC(api_key):
	params = {
		'api_key': api_key,
	}
	response = requests.get('https://api.nasa.gov/EPIC/api/natural', params=params)
	if response:
	    for num, epic_image in enumerate(response.json()):
		        date,time = epic_image["date"].split(" ")
		        picture = epic_image["image"]
		      	year,month,day = date.split("-")
		        print(date)

		        ##strdate = datetime.datetime.fromisoformat(date)
		        # month = date.month
		        # day = date.day
		        # part = (
		        #     str(date.year)
		        #     + "/"
		        #     + month
		        #     + "/"
		        #     + day
		        #     + "/png/"
		        #     + picture
		        #     + ".png"
		        # )
		        link = "https://api.nasa.gov/EPIC/archive/natural/{0}".format(part)
		        content = requests.get(link,params=params)
		        fname = "images/Nasa{0}.png".format(num)
		        ##with open(fname, "wb") as file:
		            ##file.write(content.content)
		        ##fname = ""


if __name__ == "__main__":
    load_dotenv()
    API_KEY = os.getenv("NASSA_API_KEY")
    EPIC(API_KEY)
