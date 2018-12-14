# Configuration processor

import json

with open('config.json') as f:
	data = json.load(f)

def get_token():
	return data['telegram-token']
