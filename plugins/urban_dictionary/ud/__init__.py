import plugin_handler
from . import api
import wx

class UrbanDictionaryPlugin(plugin_handler.Plugin):
	def get_text(self):
		final = ""
		results = api.get_definition("Quin")
		for i in results:
			final += i.to_string()
		return final

	def create_panel(self, frame):
		panel = wx.Panel(frame)
		sizer = wx.BoxSizer(wx.VERTICAL)
		search_button = wx.Button(panel, -1, "&Search")
		search_button.Bind(wx.EVT_BUTTON, self.on_search)
		sizer.Add(search_button, 0, wx.ALL, 10)
		return panel

	def on_search(self, event=None):
		pass
