from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, ADMINS

class Bot(Client):
    def __init__(self):
        super().__init__("BOT",api_hash=API_HASH,api_id=API_ID,bot_token=BOT_TOKEN,plugins={"root":"plugins"})
        
    async def start(self):
        await super().start()
        for admin in ADMINS:
            try:
                await self.send_message(text=f"{self.username} Re-Started", chat_id=admin)
            except:
                pass
        
Bot().run()

