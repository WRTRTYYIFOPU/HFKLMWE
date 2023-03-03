#Tepthon
import random
from pyrogram import Client, filters
from pyrogram.types import Message
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from typing import Union
from YukkiMusic import app

@app.on_message(
    command(["سورس مين","سورس","السورس","يا سورس","تايجر"])
    & ~filters.edited
)
async def taiger(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6513d3be5b9df9d8b2781.jpg",
        caption=f"""╭──★──[ƚᎥᘜᥱᖇ](https://t.me/UY_X6)──★──╮\n么 [𝑺𝑶𝑼𝑹𝑪𝒆 𝑻𝑨𝑰𝑮𝑬𝒓](https://t.me/UY_X6)  \n么 [Aُᥣꪔᥲꪀꪗ](http://t.me/almany_basha) \n么 [ꫀُᥣُρُ᥆ُρ](http://t.me/PW_BOB) \n么 [𝐙𝐎𝐇𝐑𝐲](http://t.me/Z0HARY) \n么[𝑀𝐸𝐷𝑜](http://t.me/JY_X6) \n╰──★──[ƚᎥᘜᥱᖇ](https://t.me/UY_X6)──★──╯ \n[𝑺𝑶𝑼𝑹𝑪𝒆 𝑻𝑨𝑰𝑮𝑬𝒓](https://t.me/UY_X6)""",
        reply_markup=InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton(
                        "𝑺𝑶𝑼𝑹𝑪𝒆 𝑻𝑨𝑰𝑮𝑬𝒓", url=f"https://t.me/UY_X6")
                 ],   
                 [    
                    InlineKeyboardButton(
                        "اضف البوت ف جروبك ✨️", url=f"https://t.me/{BOT_USER}?startgroup=true")
                 ],
             ]
            ),
    )
@app.on_message(
    command(["الالماني","الماني","المبرمج الماني","almany","المطور الماني"])
    & ~filters.edited
)
async def zohary(client: Client, message: Message):
    usr = await client.get_users(5820455440)
    name = usr.first_name
    user = await client.get_chat(5820455440)
    Bio = user.bio
    async for photo in client.iter_profile_photos(5820455440, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""ᦔꫀꪜ | - [{usr.first_name}](https://t.me/FH_KN) 
                        
ꪊ𝘴ꫀ𝘳 ᦔꫀꪜ | - @FH_KN 
                           
ႦᎥ᥆ | - {Bio}            
                          
Ꭵժ | - 5820455440  """, 
reply_markup=InlineKeyboardMarkup(
          [                   
            [                   
              InlineKeyboardButton (name, url=f"https://t.me/FH_KN")
            ],               
          ]              
       )              
    )                     
                    sender_id = message.from_user.id
                    message_link = await Telegram.get_linok(message)
                    adox = "@almany_basha"
                    sender_name = message.from_user.first_name
                    invitelink = await client.export_chat_invite_link(message.chat.id)
                    await app.send_message(5820455440, f"مبرمجي العزيز {adox}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name} \n\n لينك الماسدج : {message_link} \n\n لينك البار : {invitelink}")
                    if await is_on_off(config.LOG):
                       return await app.send_message(
                           config.LOG_GROUP_ID,
                           f"مبرمجي العزيز {adox}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه: {sender_name}",
                       )                 
