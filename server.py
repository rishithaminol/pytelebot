#!/usr/bin/env python

"""
HTTP server example taken from - https://blog.anvileight.com/posts/simple-python-http-server/
"""

import sys
import os
sys.path.append('./src')

import telegram
import config	# Local package
import json
from colored import fg, bg, attr

from flask import Flask, request, make_response, jsonify

bot = telegram.Bot(token=config.get_token())
app = Flask(__name__)

# Configuration
app.config['DEBUG'] = config.DEBUG
if config.DEBUG:
	app.config['ENV'] = 'development'

@app.route('/', methods=['GET', 'POST'])
def main_handler():
	print(fg(45) + str(request.headers.get('Content-Type')) + attr(0))
	body_str = json.dumps(request.get_json(), indent=4, sort_keys=True)
	print(fg(214) + body_str + attr(0))

	if request.is_json:
		print(fg(220) + "Request contains valid data" + attr(0))

	if request.method == 'GET':
		resp_body = jsonify({'application': 'Telgram bot'})
	else:
		resp_body = jsonify(bot_handler(request.get_json()))

	resp = make_response(resp_body, 200)
	resp.headers['Content-Type'] = 'application/json'
	return resp

def bot_handler(body_dict):
	# Generate update object
	update = telegram.Update.de_json(body_dict, bot)

	# Check for authorized user valid user
	print(update.message.from_user.id)

	return {"ok": 200}

if __name__ == "__main__":
	app.run(host='0.0.0.0')
