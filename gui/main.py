import wx
import plugin_handler
import sys

class MainFrame(wx.Frame):
	def __init__(self):
		self.manager = None
		self.plugins = {}
		wx.Dialog.__init__(self, None, title="Lookup", size=wx.DefaultSize)
		self.panel = wx.Panel(self)
		self.main_box = wx.BoxSizer(wx.VERTICAL)
		self.list_label = wx.StaticText(self.panel, -1, "&Choices")
		self.main_box.Add(self.list_label, 0, wx.ALL, 10)
		self.list = wx.ListBox(self.panel, -1)
		self.main_box.Add(self.list, 0, wx.ALL, 10)
		self.list.SetFocus()
		self.list.Bind(wx.EVT_LISTBOX, self.on_list_change)
		self.plugin_panel = wx.Panel(self)
		self.load_plugins()
		if not self.list.IsEmpty():
			self.list.SetSelection(0)
			self.on_list_change()
		self.exit_button = wx.Button(self.panel, -1, "E&xit")
		self.exit_button.Bind(wx.EVT_BUTTON, self.on_exit)
		self.main_box.Add(self.exit_button, 0, wx.ALL, 10)
		self.panel.Layout()

	def on_go(self, event=None):
		if self.list.IsEmpty():
			return

	def on_list_change(self, event=None):
		result = list(self.plugins)[self.list.GetSelection()].plugin_object.create_panel(self)
		self.plugin_panel.Hide()
		self.plugin_panel = result
		self.plugin_panel.Show()

	def on_exit(self, event=None):
		self.Destroy()
		sys.exit()

	def load_plugins(self):
		self.manager = plugin_handler.get_plugin_manager()
		self.manager.collectPlugins()
		for plugin in self.manager.getAllPlugins():
			self.manager.activatePluginByName(plugin.name)
			self.plugins[plugin] = plugin.plugin_object
		self.list.Clear()
		for plugin_info, plugin_object in self.plugins.items():
			self.list.Append(plugin_info.name, plugin_object)
