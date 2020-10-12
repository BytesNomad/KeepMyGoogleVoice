#!/usr/bin/python3
# -*- coding: utf-8 -*-

from googlevoice import Voice
import os

def run():
    voice = Voice()
    voice.login(email = os.environ.get('GMAIL'), passwd = os.environ.get("PASSWORD"))

    phoneNumber = "8336721001"
    text = "cloudflare.com"

    voice.send_sms(phoneNumber, text)


__name__ == "__main__" and run()
