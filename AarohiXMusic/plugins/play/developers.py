import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
from random import  choice, randint

#          
                
@app.on_message(
    filters.command(["المبرمج","رامو","مبرمج السورس","المطور"], "")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/f717bb3aaef5d24b229a1.mp4",
        caption=f"""**⩹━★⊷━⌞ 𝗦𝗼𝘂𝗿𝗰𝗲  𝐑𝙄𝙆𝙊⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم المبرمج\nللتحدث مع السورس السورس اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ 𝗦𝗼𝘂𝗿𝗰𝗲  𝐑𝙄𝙆𝙊 ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᯓ𓆩˹ 𝗠𝗥  𝑹𝑨𝑴𝑶 ˼𓆪𓆃", url=f"https://t.me/C_lxl_C"), 
                 ],[
                   InlineKeyboardButton(
                        "𝗦𝗼𝘂𝗿𝗰𝗲  𝐑𝙄𝙆𝙊", url=f"https://t.me/R_surce"),
                ],

            ]

        ),

    )
