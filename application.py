import wx
from gui import main

class Application:
	def __init__(self):
		self.name = "Lookup"
		self.version = "0.12"
		self.running = False
		self.wx = wx.App()
		self.main_frame = main.MainFrame(self)

	def run(self):
		self.running = True
		self.main_frame.Show()
		self.wx.MainLoop()
