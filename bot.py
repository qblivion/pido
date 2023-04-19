from loader import *
from pyrogram.handlers import MessageHandler
from pyrogram import enums

edit_text = False
edit_text_id = 0
cap = False
@bot.on_message(filters.all)
async def main(client, message):
    global edit_text, edit_text_id, cap
    if (message.from_user.id == 897469116 or message.from_user.id == 950155405) and edit_text:
        try:
            if not cap:
                await bot.edit_message_text(chat_id=group_chat_id, message_id=edit_text_id, text=message.text, reply_markup=new_reply_markup)
                print(message.text)
            else:
                await bot.edit_message_caption(chat_id=group_chat_id, message_id=edit_text_id, caption=message.text, reply_markup=new_reply_markup)
        except Exception:
            pass
        cap = False
        edit_text = False
    if message.chat.id != 5789878404:
        return
    sent_message = await bot.copy_message(chat_id=group_chat_id, from_chat_id=message.chat.id, message_id=message.id)
    await bot.edit_message_reply_markup(chat_id=group_chat_id, message_id=sent_message.id, reply_markup=new_reply_markup)


@bot.on_callback_query(filters.regex('post'))
async def post(client, call):
    await call.answer(text='Пост отправлен!')
    await bot.edit_message_reply_markup(chat_id=group_chat_id, message_id=call.message.id, reply_markup=None)
    # await bot.edit_message_text(chat_id=group_chat_id, message_id=call.message.id, text=call.message.text + "[Банка Неймана. Подписаться](https://t.me/neymanbank)", parse_mode=enums.ParseMode.MARKDOWN)
    try:
        if call.message.text:
            await bot.edit_message_text(chat_id=group_chat_id, message_id=call.message.id, text=call.message.text + "\n\n[Банка Неймана. Подписаться](https://t.me/neymanbank)", parse_mode=enums.ParseMode.MARKDOWN, disable_web_page_preview=True)
            print(call.message.text)
        if call.message.caption:
            await bot.edit_message_caption(chat_id=group_chat_id, message_id=call.message.id, caption=call.message.caption + "\n\n[Банка Неймана. Подписаться](https://t.me/neymanbank)", parse_mode=enums.ParseMode.MARKDOWN)
    except Exception:
        pass
    await bot.copy_message(chat_id=channel_chat_id, from_chat_id=group_chat_id, message_id=call.message.id)

@bot.on_callback_query(filters.regex('edit'))
async def edit(client, call):
    await call.answer('Отправьте новый текст!')
    global edit_text, edit_text_id, cap
    edit_text = True
    edit_text_id = call.message.id
    if call.message.caption:
        cap = True
bot.run()  