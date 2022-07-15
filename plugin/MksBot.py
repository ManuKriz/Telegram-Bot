from pyrogram import Client, filters

@Client.on_message(filters.private)
async def onMsg(bot, msg):
  await msg.reply("[Oops](https://t.me/MovieS_HooD/139)")
