import sys
sys.dont_write_bytecode = True
from gui import main
import wx
import logger
import logging

log = logging.getLogger("main")

if __name__ == "__main__":
	log.debug("Starting Lookup...")
	app = wx.App()
	log.debug("WX App created.")
	frame = main.MainFrame()
	frame.Show()
	log.debug("GUI created.")
	log.debug("Running.")
	app.MainLoop()
