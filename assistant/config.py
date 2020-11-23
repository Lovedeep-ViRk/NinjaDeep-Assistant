# Copyright (C) 2020 by LovedeepViRk@Github, < https://github.com/Lovedeep-ViRk >.
#
# This file is part of < https://github.com/Lovedeep-ViRk/NinjaDeep-Assistant > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/NinjaDeep-Assistant/blob/master/LICENSE >
#
# All rights reserved.

__all__ = ["Config"]

import os

from dotenv import load_dotenv

if os.path.isfile("config.env"):
    load_dotenv("config.env")


class Config:
    """ assistant configs """
    APP_ID = int(os.environ.get("APP_ID", 0))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    AUTH_CHATS = set([-1001194584100])  # @NinjaDeepOT
    if os.environ.get("AUTH_CHATS"):
        AUTH_CHATS.update(map(int, os.environ.get("AUTH_CHATS").split()))
    WHITELIST_CHATS = set([-1001127399056])  # @NinjaDeepSpam
    if os.environ.get("WHITELIST_CHATS"):
        WHITELIST_CHATS.update(
            map(int, os.environ.get("WHITELIST_CHATS").split()))
    DEV_USERS = (
        1470165323,  # @Lovedeep_ViRk
    )
    ADMINS = {}
    MAX_MSG_LENGTH = 4096
