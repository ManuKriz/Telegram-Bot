from pyrogram import Client, filters

@Client.on_message(filters.private)
async def onMsg(bot, msg):
  await msg.reply(f"Hey {msg.from_user.first_name} I'm Alive")
