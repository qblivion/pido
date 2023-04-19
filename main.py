from loader import *
from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram import filters
from pyrogram.types import InputMediaPhoto, InputMediaVideo


async def handler(client, message):
    if message.media_group_id or message.outgoing == True or message.chat.id == group_chat_id:
        return
    await app.send_message(chat_id=group_chat_id, text=f'Сообщение из чата @{message.chat.username} {message.chat.title}')
    await app.copy_message(chat_id=bot_chat_id, from_chat_id=message.chat.id, message_id=message.id)




app.add_handler(MessageHandler(handler))
app.run()

