#!/usr/bin/env python3

from dotenv import load_dotenv
load_dotenv()
import requests, sys, os

tbot_token = os.getenv('TBOT_TOKEN')
tbot_chat_id = os.getenv("CHAT_ID")
tbot_url = 'https://api.telegram.org/bot{}/'.format(tbot_token)

class TGUrlConstructor(object):
    def construct_url(self):
        final_url = []
        for key, val in self.parameter_dict.items():
            if val is not None:
                final_url.append("{key}={val}".format(key=key, val=val))

        final_url = "&".join(final_url)

        return tbot_url + self.constructor_id + '?' + final_url
    
    def send(self):
        respon = requests.get(self.construct_url())
        print(respon)

class sendMessage(TGUrlConstructor):
    def __init__(self, chat_id=None, text=None, parse_mode=None, disable_web_page_preview=None,
                    reply_to_message_id=None, reply_markup=None):
        self.chat_id = chat_id
        self.text = text
        self.parse_mode = parse_mode

        self.constructor_id = 'sendMessage'
        self.parameter_dict = {
            'chat_id': self.chat_id,
            'text': self.text,
            'parse_mode': self.parse_mode
        }

<<<<<<< HEAD:server.py
x = sendMessage(chat_id=-364409911, text='|'.join(sys.argv[1:]), parse_mode='HTML')
x.construct_url()
x.send()
=======
x = sendMessage(chat_id=tbot_chat_id, text='|'.join(sys.argv[1:]), parse_mode='HTML')
print(x.construct_url())
print(x.send())
>>>>>>> 7ff19acc41879f152688c8ffbfe0d615f42e086e:pytelebot.py

# send_message(tbot_url, tbot_chat_id, '|'.join(sys.argv[1:]))
