import plugin_handler
from . import api
import wx

class UrbanDictionaryPlugin(plugin_handler.Plugin):
	def get_text(self):
		results = api.get_definition("Quin")
		return "".join(i.to_string() for i in results)

	def create_panel(self, frame):
		return UrbanDictionaryPanel(frame)

	def on_search(self, event=None):
		pass

class UrbanDictionaryPanel(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		self.sizer = wx.BoxSizer(wx.HORIZONTAL)
		self.search_button = wx.Button(self, -1, "&Search")
		self.sizer.Add(self.search_button, 0, wx.ALL, 10)
		self.SetSizer(self.sizer)
		self.Layout()
