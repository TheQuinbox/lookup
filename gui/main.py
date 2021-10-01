import wx
import sys
import logging
import bored
from . import info

log = logging.getLogger("gui.main")

class MainFrame(wx.Frame):
	def __init__(self, app):
		self.app = app
		self.options = ["Fetch a random activity from the Bored API"]
		wx.Frame.__init__(self, None, title=f"{self.app.name} V{self.app.version}", size=wx.DefaultSize)
		log.debug("Frame created.")
		self.panel = wx.Panel(self)
		log.debug("Panel created.")
		self.main_box = wx.BoxSizer(wx.VERTICAL)
		log.debug("Main Sizer created.")
		self.label = wx.StaticText(self.panel, label="&Select what you want to do", style=wx.ALIGN_CENTRE)
		self.main_box.Add(self.label, 0, wx.EXPAND | wx.ALL, 5)
		self.combo = wx.ComboBox(self.panel, choices=self.options, style=wx.CB_SORT | wx.CB_READONLY)
		self.main_box.Add(self.combo, 1, wx.EXPAND | wx.ALL, 5)
		self.combo.SetSelection(0)
		self.go = wx.Button(self.panel, wx.ID_DEFAULT, "&Go")
		self.main_box.Add(self.go, 0, wx.ALL, 10)
		self.go.SetDefault()
		self.close = wx.Button(self.panel, wx.ID_CANCEL, "E&xit")
		self.main_box.Add(self.close, 0, wx.ALL, 10)
		log.debug("Widgets spawned.")
		self.go.Bind(wx.EVT_BUTTON, self.on_go)
		self.Bind(wx.EVT_CLOSE, self.on_close)
		self.close.Bind(wx.EVT_BUTTON, self.on_close)
		log.debug("WX Events bound.")
		self.panel.Layout()

	def on_close(self, event=None):
		log.debug(f"{self.app.name} exiting.")
		self.Destroy()
		sys.exit()

	def on_go(self, event=None):
		if self.combo.GetValue() == self.options[0]:
			log.debug("Bored API selected.")
			self.on_bored()
		else:
			log.debug("Nothing selected.")
			pass

	def on_bored(self):
		activity = bored.getRandomActivity().activity
		info_gui = info.InfoGui(f"{self.app.name}", "&Activity", activity)
		info_gui.Show()
