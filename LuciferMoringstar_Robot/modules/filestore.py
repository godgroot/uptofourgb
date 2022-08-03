from config import Config
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import base64



@Client.on_message(filters.private & filters.command('batch'))
async def batchfilestore(client, message):
 
    
    while True:
        try:
            first_message = await client.ask(text = "Forward the First Message from the DB Channel (with Quotes)..", chat_id = message.from_user.id, filters=filters.forwarded, timeout=30)
        except:
            return

              
        if first_message.forward_from_chat:
            if first_message.forward_from_chat.id == Config.FILE_STORE_CHANNEL:
                f_msg_id = first_message.forward_from_message_id
                break
        await first_message.reply_text("Forward from the Assigned Channel only...", quote = True)
        continue
    
    while True:
        try:
            second_message = await client.ask(text = "Forward the Last Message from DB Channel (with Quotes)..", chat_id = message.from_user.id, filters=filters.forwarded, timeout=30)
        except:
            return

    
      
        if second_message.forward_from_chat:
            if second_message.forward_from_chat.id == Config.FILE_STORE_CHANNEL:
                s_msg_id = second_message.forward_from_message_id
                break
        await second_message.reply_text("Forward from the Assigned Channel only...", quote = True)
        continue
       
    string = f"get-{f_msg_id}-{s_msg_id}"
    string_bytes = string.encode("ascii")
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode("ascii")
    link = f"https://t.me/{Config.BOT_USERNAME}?start={base64_string}"
    buttons = [[ InlineKeyboardButton("🎋 open here 🎋", url=link) ]]
    await second_message.reply_text(f"<b>Here is your link</b>\n\n{link}", quote=True, reply_markup=InlineKeyboardMarkup(buttons))
