# -*- coding: utf-8 -*-
"""Webex Websockets Bot code.
GOAL: Webex Bot code that uses Websockets to communicate with the cloud. 
BASED ON: https://github.com/cgascoig/ciscospark-websocket
Copyright (c) 2022 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at      https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""
__author__ = "Dirk-Jan Uittenbogaard"
__email__ = "duittenb@cisco.com"
__version__ = "0.1"
__date__ = "15-July-2022"
__copyright__ = "Copyright (c) 2022 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

from webexwebsocket import WebexMessage
from webexteamssdk import WebexTeamsAPI
import logging
import os
import sys

# Put your BOT token in environment variable "MY_BOT_TOKEN" or replace the 4 lines below with: my_bot_token="your_bot_token"
my_bot_token = os.getenv('MY_BOT_TOKEN')
if my_bot_token is None:
    print("**ERROR** environment variable 'MY_BOT_TOKEN' not set, stopping.")
    sys.exit(-1)


def process_message(message_obj):  # Process messages that the bot receives.
    # Access incoming message content with: message_obj.personEmail, message_obj.text, etc. Example API msg at the end of this code.
    #___ incoming message contains the word 'hello'
    if "hello" in message_obj.text.lower():
        print("___ HELLO message received!")
        msg_result = api.messages.create(toPersonEmail=message_obj.personEmail, markdown="# Hello to you to!")
    else:
        print(f"___ OTHER message received: repeat message '{message_obj.text}'")
        msg_result = api.messages.create(toPersonEmail=message_obj.personEmail, markdown="**You just said:** " + message_obj.text)
    return msg_result


if __name__ == '__main__':
    webex=None
    #___Configure Logging
    logging.basicConfig(level=logging.WARNING, format='[%(levelname)s] %(message)s')
    # logging.basicConfig(level=logging.WARNING, format='%(asctime)s  [%(levelname)s]  [%(module)s.%(name)s.%(funcName)s]:%(lineno)s %(message)s')
    api = WebexTeamsAPI(access_token=my_bot_token)
    webex = WebexMessage(access_token=my_bot_token, on_message=process_message)
    logging.warning('\n\n___Bot_started_____')
    webex.run()


# REFERENCE:
# ____BELOW: message data example
# {
#   "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNWI0ODQwZTAtYjY1NS0xMWVjLWJmNjUtYjc1NjQzYThhNGI4",
#   "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vMzc4ZGYyYzAtM2NjYi0xMWVjLTg2YjMtNWIwZDIyOTNiMDZk",
#   "roomType": "direct",
#   "text": "how are you bot?",
#   "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS83MzMxNzBiYi02YjY3LTQ4N2EtYmJmOC03ZGIzMmIzNGY0ZDE",
#   "personEmail": "duittenb@cisco.com",
#   "created": "2022-04-07T09:30:26.158Z"
# }
