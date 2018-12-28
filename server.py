#!/usr/bin/env python

"""
HTTP server example taken from - https://blog.anvileight.com/posts/simple-python-http-server/
"""

import sys
import os
sys.path.append('./src')

import signal
import telegram
import config	# Local package
import json
from colored import fg, bg, attr
from http.server import HTTPServer, BaseHTTPRequestHandler

bot = telegram.Bot(token=config.get_token())

def signal_handler(sig, frame):
	print('SIGINT signal received')
	sys.exit(0)

def is_json(jsonstr):
	try:
		json_obj = json.loads(jsonstr)
	except ValueError as e:
		return False

	return True

"""
check whether the request is application/json and body
contains valid json data as our needs
	req_body - string(josn string)
	headers - request headers as a list
"""
def is_json_req(req_body, headers):
	if headers['Content-Type'] == 'application/json' and is_json(req_body):
		return True

	return False

class CustomRequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.end_headers()
		self.wfile.write(b'Hello, world!')

	def do_POST(self):
		content_length = int(self.headers['Content-Length'])
		body = self.rfile.read(content_length)
		json_string = body.decode("utf-8")

		for header in self.headers:
			print(fg(198) + header + ": " + self.headers[header] + attr(0))

		# Check for valid json request
		if is_json_req(json_string, self.headers):
			print(fg(220) + "Request contains valid data" + attr(0))
		else:
			self.send_response(404)
			self.end_headers()
			return

		# Convert json to dictionary
		body_dict = json.loads(json_string)
		print(fg(27) + json.dumps(body_dict, indent=4) + attr(0))

		# Generate update object
		update = telegram.Update.de_json(body_dict, bot)
		print(fg(119) + json.dumps(update.to_dict(), indent=4) + attr(0))

		# Check for authorized user valid user
		print(update.message.from_user.id)
		print(self.client_address)

		# print("sending reply: ")
		# update.message.reply_text("Hello world");
		self.send_response(200)
		self.end_headers()

	def log_message(self, format, *args):
		if config.DEBUG:
			print(args)

		return True


httpd = HTTPServer(('localhost', 5000), CustomRequestHandler)
try:
	print("Starting server http://localhost:5000")
	httpd.serve_forever()
except KeyboardInterrupt:
	print("stopping server due to keyboard interrupt")
	httpd.shutdown()
