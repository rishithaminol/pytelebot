#!/usr/bin/env python

import telegram
import config

bot = telegram.Bot(token=config.get_token())

updates = bot.get_updates()

chat_id = updates[-1].message.chat_id
print("chat_id: " + str(chat_id))
bot.send_message(chat_id=chat_id, text="Hello rishitha Minol")

a = """
<b style="color: green">bold</b> <i>italic</i> <a href="http://google.com">link</a>
"""

bot.send_message(chat_id=-1001280280300, 
                  text=a, 
                  parse_mode=telegram.ParseMode.HTML)
print(updates.effective_user.id)
