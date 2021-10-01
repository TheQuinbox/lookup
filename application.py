import wx
import logging
import sys
from gui import main
from logger import logger

log = logging.getLogger("application")

class Application:
	def __init__(self):
		self.name = "Lookup"
		self.version = "0.12"
		log.debug(f"Starting {self.name} V{self.version}")
		self.running = False
		self.wx = wx.App()
		log.debug("WX initialized.")
		self.main_frame = main.MainFrame(self)
		log.debug("GUI initialized.")

	def run(self):
		self.running = True
		log.debug("Application running.")
		self.main_frame.Show()
		self.wx.MainLoop()
