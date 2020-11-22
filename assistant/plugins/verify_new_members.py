# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.

#

# This file is part of < https://github.com/UsergeTeam/Userge-Assistant > project,

# and is released under the "GNU v3.0 License Agreement".

# Please see < https://github.com/Userge-Assistant/blob/master/LICENSE >

#

# All rights reserved.

import asyncio

from pyrogram import filters

from pyrogram.types import (

    Message, ChatPermissions, CallbackQuery,

    InlineKeyboardMarkup, InlineKeyboardButton)

from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant

from assistant import bot, cus_filters

from assistant.utils import check_bot_rights

@bot.on_message(

    filters.group & filters.new_chat_members & cus_filters.auth_chats)

async def _verify_msg_(_, msg: Message):

    """ Verify Msg for New chat Members """

    chat_id = msg.chat.id

    for member in msg.new_chat_members:

        try:

            user_status = (await msg.chat.get_member(member.id)).status

            if user_status in ("restricted", "kicked"):

                continue

        except Exception:

            pass

        if member.is_bot or not await check_bot_rights(chat_id, "can_restrict_members"):

            file_id, file_ref, text, buttons = await wc_msg(member)

            reply = await msg.reply_animation(

                animation=file_id, file_ref=file_ref,

                caption=text, reply_markup=buttons

            )

            await asyncio.sleep(120)

            await reply.delete()

        el
