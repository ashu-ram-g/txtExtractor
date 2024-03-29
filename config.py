#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6491187222:AAH3ZLQVAa4dptxirjCWCkYlMifgmN0tGhc")
    API_ID = int(os.environ.get("API_ID", "29337172"))
    API_HASH = os.environ.get("API_HASH", "34b3a05a2038e77119115c6ee1ec9d56")
    AUTH_USERS = os.environ.get("AUTH_USERS", "1280494242")
