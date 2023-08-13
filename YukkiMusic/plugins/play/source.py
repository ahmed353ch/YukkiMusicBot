import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()



@app.on_message(
    command(["سورس ليوا","سورس","السورس","يا سورس"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/998bb255810b601f246dd.jpg",
        caption=f"""╭──── • ◈ • ────╮ 
么  𝚊𝚕𝚎𝚡𝚊 𝚜𝚘𝚞𝚛𝚌𝚎
么 𝙴𝚁𝚁𝙾𝚁
╰──── • ◈ • ────╯ 
  
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᗴᖇᖇOᖇ", url=f"https://t.me/S4ASA"), 
                ],[
                    InlineKeyboardButton(
                        "ᗩᒪE᙭ᗩ", url=f"https://t.me/RDPDDP"),
                ],[
                    InlineKeyboardButton(
                        "اضغط لاضافه البوت لمجموعتك✅.", url=f"https://t.me/q8lbot?startgroup=true"),
                ],

            ]

        ),

    )
"https://t.me/q8lbot?startgroup=true"),
                ],

            ]

        ),

    )
