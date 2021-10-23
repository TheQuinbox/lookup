import plugin_handler
from . import api
import wx

class UrbanDictionaryPlugin(plugin_handler.Plugin):
	def __init__(self):
		super().__init__()

	def get_text(self):
		final = ""
		results = api.get_definition("Quin")
		for i in results:
			final += i.to_string()
		return final

	def create_panel(self, frame):
		panel = UrbanDictionaryPanel(frame)
		return panel

	def on_search(self, event=None):
		pass

class UrbanDictionaryPanel(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		self.sizer = wx.BoxSizer(wx.HORIZONTAL)
		self.search_button = wx.Button(self, -1, "&Search")
		self.sizer.Add(self.search_button, 0, wx.All, 10)
		self.SetSizer(self.sizer)
		self.Layout()
