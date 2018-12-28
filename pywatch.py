#!/usr/bin/env python

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from subprocess import Popen

devnull = open(os.devnull, 'wb')

def start_server():
	return Popen(['./server.py'])

class CustomObserver(Observer):
	def __init__(self):
		Observer.__init__(self)

	def on_thread_start(self):
		print('Thread starting')
		self.server_py = start_server()
		print(dir(self.server_py))

	def on_thread_stop(self):
		print('Thread stopping')
		self.server_py.terminate()

	def on_modified(self, event):
		print('event type: {e_type} path: {e_src}'.format(e_type=event.event_type,
						e_src=event.src_path))
		self.server_py.terminate()
		self.server_py = start_server()

if __name__ == "__main__":
	event_handler = FileSystemEventHandler()
	observer = CustomObserver()
	event_handler.on_modified = observer.on_modified
	observer.schedule(event_handler, './', recursive=True)

	try:
		observer.start()
		observer.join()
	except KeyboardInterrupt:
		observer.stop()
