import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BuOT_USERNAME as bu, CHANNEL_UPDATES, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgQAAx0CWrNeBQABDw_wZDvP7uUo9klF1fdkbUjQYcYbux8AAvoPAAJJhhhRrBTCwcQVclYvBA")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f""" ** Hey {message.from_user.mention()} , 🥀\n\n
๏ This is [{bn}](t.me/{bu}) ,  !
➻ The most Powerful telegram music  bot with some awesome and useful features.

──────────────────
๏  All of my command can be used with My command handle : ( / . • $ ^ ~ + * ? )
➻ Made 🖤 by : [ꜰɪɴᴇx🥀](https://t.me/suppienoodles) ** """,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✚ ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴀʏ", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                 ],[
                    InlineKeyboardButton(
                        "📨 ꜱᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{TheNight_city}"
                    ),
                    InlineKeyboardButton(
                        "📨 ᴜᴘᴅᴀᴛᴇꜱ ", url=f"https://t.me/{bothub_xD}"
                    )
                  ],[
                    InlineKeyboardButton(
                        "👤 Bot Owner ", url=f"https://t.me/SuppieNoodles"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 Developer ", url=f"https://t.me/Suppienoodles"
                    ),
                  ],[
                    InlineKeyboardButton(
                        "✅ Inline ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "💡 Git repo "https://graph.org/file/41b82338ab82bca5643eb.mp4"
"
                    )]
            ]
       ),
    )

