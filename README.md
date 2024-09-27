# TelegramXNassa
This project let you send Nassa photos in telegram.
# Warning
All steps are done in directory of project!
# How to use
1. Download all files.
2. Create .env file.
3. Edit it:
``` 
ID =  "1111"(Your Value(Id of launch APOD))
TELEGRAM_ID = "1111"(Your Value(ID of group))
Telegram_API = "1111"(Your Value(Api code of bot))
API_KEY = "1111"(Your Value(NASSA))
UPL_FRQ = '1'(Your Value)
```
- If you dont create UPL_FRQ script will send pictures every 4 hours.
4. Create folder "images" and place here.If you dont have photos,use files to get Apod photos,Epic earth photos,and Nassa photos.
5. If you need to sent pictures move them to images.
6.Final step. Type in Terminal of your system:
```
py -m pip install -r requirements.txt
```  
# Launching
1.Use Terminal of your system and type:
```
python Telegramxnassa.py
```
