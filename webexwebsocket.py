# -*- coding: utf-8 -*-
import json
import asyncio
import string
import random
import logging
import uuid
import websockets
from base64 import b64encode
from webexteamssdk import WebexTeamsAPI

DEVICES_URL = 'https://wdm-a.wbx2.com/wdm/api/v1/devices'
DEVICE_DATA = {
    "deviceName": "pywebsocket-client",
    "deviceType": "DESKTOP",
    "localizedModel": "python",
    "model": "python",
    "name": f"python-webex-client-{''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))}",
    "systemName": "python-webex-client",
    "systemVersion": "0.1"
}

class WebexMessage(object):
    def __init__(self, access_token, on_message=None):
        self.access_token = access_token
        self.webex = WebexTeamsAPI(access_token=access_token)
        self.device_info = None
        self.on_message = on_message

    def _process_message(self, msg):
        print(f"------------------ EVENT: {msg['data']['eventType']}")
        if msg['data']['eventType'] == 'conversation.activity':
            activity = msg['data']['activity']
            if activity['verb'] == 'post':
                #___Convert 'id' and get message text
                uuid = activity['id']
                if "-" in uuid:
                    space_id = (b64encode(f"ciscospark://us/MESSAGE/{uuid}".encode("ascii")).decode("ascii"))
                else:
                    space_id = uuid
                webex_msg_object = self.webex.messages.get(space_id)
                #___Skip messages from the bot itself
                if webex_msg_object.personEmail in self.my_emails:
                    logging.debug('>>> message is from myself, ignoring')
                    return
                #___Process message
                if self.on_message:
                    self.on_message(webex_msg_object)

    def _get_device_info(self):
        logging.debug('>>> getting device list')
        try:
            resp = self.webex._session.get(DEVICES_URL)
            for device in resp['devices']:
                if device['name'] == DEVICE_DATA['name']:
                    self.device_info = device
                    return device
        except:
            pass

        logging.info('>>> device does not exist, creating')

        resp = self.webex._session.post(DEVICES_URL, json=DEVICE_DATA)
        if resp is None:
            logging.error('>>> **ERROR** could not create device')
        self.device_info = resp
        return resp

    def run(self):
        if self.device_info == None:
            if self._get_device_info() is None:
                logging.error('>>> could not get/create device info')
                return

        self.my_emails = self.webex.people.me().emails

        async def _run():
            logging.debug(">>> Opening websocket connection to %s" % self.device_info['webSocketUrl'])
            async with websockets.connect(self.device_info['webSocketUrl']) as ws:
                logging.info(">>> WebSocket Opened\n")
                msg = {'id': str(uuid.uuid4()),
                       'type': 'authorization',
                       'data': {
                          'token': 'Bearer ' + self.access_token
                        }
                      }
                await ws.send(json.dumps(msg))

                while True:
                    message = await ws.recv()
                    logging.debug(">>> WebSocket Received Message(raw): %s\n" % message)
                    try:
                        msg = json.loads(message)
                        loop = asyncio.get_event_loop()
                        loop.run_in_executor(None, self._process_message, msg)
                    except:
                        logging.warning('>>> **ERROR** An exception occurred while processing message. Ignoring. ')

        asyncio.get_event_loop().run_until_complete(_run())