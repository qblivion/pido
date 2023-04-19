from dotenv import load_dotenv
import os

from pyrogram import Client, filters, types
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import logging

logging.basicConfig(level=logging.INFO)
load_dotenv()

#ЗАГРУЖАЕМ ДАННЫЕ О БОТЕ И ПРИЛОЖЕНИИ
bot_token = os.getenv('BOT_TOKEN')  
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

#ЗАПУСКАЕМ КЛИЕНТ И БОТА
bot = Client('bot', bot_token=bot_token, api_id=api_id, api_hash=api_hash)

app = Client("my_account", api_id=api_id, api_hash=api_hash)



#ДОБАВЛЯЕМ ГРУППУ И КАНАЛ
channel_chat_id = -1001986854900
group_chat_id = -1001853111586
bot_chat_id = 1804656547

#КЛАВИАТУРА ДЛЯ УПРАВЛЕНИЯ ОТПРАВКОЙ
new_reply_markup = types.InlineKeyboardMarkup(
    [
        [
            types.InlineKeyboardButton("Запостить", callback_data="post"),
            types.InlineKeyboardButton("Редактировать", callback_data="edit")
        ]
    ]
)

