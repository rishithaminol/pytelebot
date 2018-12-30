#!/usr/bin/env python

import sys
import os
sys.path.append('./src')

from telegram import Bot
from telegram.ext import MessageHandler, Dispatcher, Updater, CommandHandler
import config	# Local package
import json
from colored import fg, bg, attr

updater = Updater(token=config.get_token())
dispatcher = updater.dispatcher

def start_func(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start_func)
dispatcher.add_handler(start_handler)

updater.start_webhook(listen='0.0.0.0', port=5000)
print("hello")
