from .. import loader, utils
from pyrogram import Client, filters, types, raw


@bot.on_message(filters.regex("Гоу1"))
async def prin(bot, message):
 for i in range(1, 50):
   await bot.send_message('tonRocketBot', i)
