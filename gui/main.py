import wx
import plugin_handler
import sys

class MainFrame(wx.Frame):
	def __init__(self):
		self.manager = None
		wx.Dialog.__init__(self, None, title="Lookup", size=wx.DefaultSize)
		self.panel = wx.Panel(self)
		self.main_box = wx.BoxSizer(wx.VERTICAL)
		self.list_label = wx.StaticText(self.panel, -1, label="&Choices")
		self.main_box.Add(self.list_label, 0, wx.ALL, 10)
		self.list = wx.ListBox(self.panel, -1)
		self.main_box.Add(self.list, 0, wx.ALL, 10)
		self.list.SetFocus()
		self.go_button = wx.Button(self.panel, -1, "&Go")
		self.go_button.SetDefault()
		self.go_button.Bind(wx.EVT_BUTTON, self.on_go)
		self.main_box.Add(self.go_button, 0, wx.ALL, 10)
		self.exit_button = wx.Button(self.panel, -1, "E&xit")
		self.exit_button.Bind(wx.EVT_BUTTON, self.on_exit)
		self.main_box.Add(self.exit_button, 0, wx.ALL, 10)
		self.panel.Layout()
		self.load_plugins()

	def on_go(self, event=None):
		pass

	def on_exit(self, event=None):
		self.Destroy()
		sys.exit()

	def load_plugins(self):
		self.manager = plugin_handler.get_plugin_manager()
		self.manager.collectPlugins()
		for plugin in self.manager.getAllPlugins():
			self.manager.activatePluginByName(plugin.name)
