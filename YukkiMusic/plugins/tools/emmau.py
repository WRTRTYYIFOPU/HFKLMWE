#Tepthon
import random
from pyrogram import Client, filters
from pyrogram.types import Message
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from typing import Union
from YukkiMusic import app

@app.on_message(
    command(["البوب","المبرمج البوب","المطور بوب","بوب المطور","elpop"])
    & ~filters.edited
)
async def zohary(client: Client, message: Message):
    usr = await client.get_users(5820455440)
    name = usr.first_name
    user = await client.get_chat(5820455440)
    Bio = user.bio
    async for photo in client.iter_profile_photos(5820455440, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""ᦔꫀꪜ | - [{usr.first_name}](https://t.me/PW_BOB) 🕷
                        
ꪊ𝘴ꫀ𝘳 ᦔꫀꪜ | - @PW_BOB 🕷
                           
ႦᎥ᥆ | - {Bio} 🕷           
                          
Ꭵժ | - 5820455440 🕷 """, 
reply_markup=InlineKeyboardMarkup(
          [                   
            [                   
              InlineKeyboardButton (name, url=f"https://t.me/FH_KN")
            ],               
          ]              
       )              
    )                     
                    sender_id = message.from_user.id
                    zoharyus = "@PW_BOB"
                    message_link = await Telegram.get_linok(message)
                    sender_name = message.from_user.first_name
                    invitelink = await client.export_chat_invite_link(message.chat.id)
                    await app.send_message(5820455440, f"مبرمجي العزيز {zoharyus}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name} \n\n لينك الماسدج : {message_link} \n\n لينك البار : {invitelink}")
                    if await is_on_off(config.LOG):
                           return await app.send_message(
                           config.LOG_GROUP_ID,
                           f"مبرمجي العزيز {zoharyus}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}",)
