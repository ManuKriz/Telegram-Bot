import os
API_ID = int(os.environ['API_ID'])
API_HASH = os.environ['API_HASH']
BOT_TOKEN = os.environ['BOT_TOKEN']
ADMINS = []
for admin in os.environ['ADMINS'].split(" "):
  ADMINS.append(int(admin))
  
