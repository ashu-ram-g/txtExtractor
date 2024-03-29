#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6618274486:AAESKaMTJJ0tOR62pqOPt-a0WcfpTi0y7nk")
    API_ID = int(os.environ.get("API_ID", "6276029"))
    API_HASH = os.environ.get("API_HASH", "6133615836:AAGKs8ABEtWSoeztRyhOVD5VQ8uIaS3ZHHI")
    AUTH_USERS = os.environ.get("AUTH_USERS", "1280494242")
