#!/usr/bin/env python

"""
HTTP server example taken from - https://blog.anvileight.com/posts/simple-python-http-server/
"""

import sys
import os
sys.path.append('./src')

import telegram
import config
import json

bot = telegram.Bot(token=config.get_token())

# updates = bot.get_updates()

# chat_id = updates[-1].message.chat_id
# print("chat_id: " + str(chat_id))
# bot.send_message(chat_id=chat_id, text="Hello rishitha Minol")

# a = """
# <b style="color: green">bold</b> <i>italic</i> <a href="http://google.com">link</a>
# """

# bot.send_message(chat_id=-1001280280300, 
#                   text=a, 
#                   parse_mode=telegram.ParseMode.HTML)

from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.end_headers()
		self.wfile.write(b'Hello, world!')

	def do_POST(self):
		content_length = int(self.headers['Content-Length'])
		body = self.rfile.read(content_length)
		json_string = body.decode("utf-8")
		body_dict = json.loads(json_string)
		print(json_string)
		update = telegram.Update.de_json(body_dict, bot)
		# a = bot.process_new_updates([update])
		print(update)
		self.send_response(200)
		self.end_headers()

	def log_message(self, format, *args):
		if config.DEBUG:
			print(args)
		
		return True

httpd = HTTPServer(('localhost', 5000), SimpleHTTPRequestHandler)
httpd.serve_forever()
