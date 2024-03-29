#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6846325385:AAGF5EQTa54YpQdBe21op8RCwi6WJMz96JQ")
    API_ID = int(os.environ.get("API_ID", "25919081"))
    API_HASH = os.environ.get("API_HASH", "0bc2fdba14b16b44f0d89729ed8d2118")
    AUTH_USERS = os.environ.get("AUTH_USERS", "1826828317")
