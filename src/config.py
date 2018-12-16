# Configuration processor

import json

with open('config.json') as f:
	data = json.load(f)

if data['debug'] == 'true':
	DEBUG = True
else:
	DEBUG = False

def get_token():
	return data['telegram-token']
