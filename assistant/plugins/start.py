# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge-Assistant > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Userge-Assistant/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import (
    Message, InlineKeyboardMarkup, InlineKeyboardButton)

from assistant import bot

@bot.on_message(filters.private)
async def _start_(_, msg: Message):
    await msg.reply(
        "Welcome To NinjaDeep - Assistant Bot This Bot Only Made For NinjaDeep Group Need Any Help So Visit @NinjaDeepSUPPORT/n ~Thanks"
        disable_web_page_preview=True,
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
                "UserBot",
                url="https://github.com/Lovedeep-ViRk/NinjaDeep"
            ),
            InlineKeyboardButton(
                "🤖 Use Inline!",
                switch_inline_query=""
            )
        ]])
    )
