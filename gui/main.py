import wx
import sys
import logging

log = logging.getLogger("gui.main")

class MainFrame(wx.Frame):
	def __init__(self, app):
		self.app = app
		wx.Frame.__init__(self, None, title=f"{self.app.name} V{self.app.version}", size=wx.DefaultSize)
		log.debug("Frame created.")
		self.panel = wx.Panel(self)
		log.debug("Panel created.")
		self.main_box = wx.BoxSizer(wx.VERTICAL)
		log.debug("Main Sizer created.")
		self.Bind(wx.EVT_CLOSE, self.on_close)
		log.debug("WX Events bound.")
		self.panel.Layout()

	def on_close(self, event=None):
		log.debug(f"{self.app.name} exiting.")
		self.Destroy()
		sys.exit()
