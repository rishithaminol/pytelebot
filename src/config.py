# Configuration processor

import json

with open('config.json') as f:
	data = json.load(f)

if data['production'] == 'false':
	DEBUG = True
else:
	DEBUG = False

def get_token():
	return data['telegram-token']

def allowed_users():
	return data['allowed-users']
