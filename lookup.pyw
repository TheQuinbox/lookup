import sys
sys.dont_write_bytecode = True
import application
import logging

log = logging.getLogger("main")

def setup():
	app = application.Application()
	app.run()

if __name__ == "__main__":
	setup()
