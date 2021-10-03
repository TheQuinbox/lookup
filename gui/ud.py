import wx

class UdGui(wx.Dialog):
	def __init__(self, title, defs):
		self.title = title
		self.defs = defs
		wx.Dialog.__init__(self, None, title=self.title, size=wx.DefaultSize)
		self.panel = wx.Panel(self)
		self.main_box = wx.BoxSizer(wx.VERTICAL)
		self.list_label = wx.StaticText(self.panel, -1, label="&Results")
		self.list = wx.ListBox(self.panel, -1)
		self.main_box.Add(self.list, 0, wx.ALL, 10)
		for d in self.defs:
			self.list.Insert("%s%s" % (d.definition[:50], "..." if len(d.definition) > 50 else ""), self.list.GetCount())
		self.list.SetSelection(0)
		self.list.SetFocus()
		self.text_label = wx.StaticText(self.panel, -1, "&Info")
		self.main_box.Add(self.text_label, 0, wx.ALL, 10)
		self.text = wx.TextCtrl(self.panel, style=wx.TE_READONLY | wx.TE_MULTILINE, size=(600, 600))
		self.main_box.Add(self.text, 0, wx.ALL, 10)
		self.on_list_change()
		self.close = wx.Button(self.panel, wx.ID_CANCEL, "&Close")
		self.main_box.Add(self.close, 0, wx.ALL, 10)
		self.Bind(wx.EVT_CLOSE, self.on_close)
		self.list.Bind(wx.EVT_LISTBOX, self.on_list_change)
		self.close.Bind(wx.EVT_BUTTON, self.on_close)
		self.panel.Layout()

	def on_close(self, event=None):
		self.Destroy()

	def on_list_change(self, event=None):
		self.text.SetValue(f"Word: {self.defs[self.list.GetSelection()].word}\nDefinition: {self.defs[self.list.GetSelection()].definition}\nExample: {self.defs[self.list.GetSelection()].example}\nUpvotes: {self.defs[self.list.GetSelection()].upvotes}\nDownvotes: {self.defs[self.list.GetSelection()].downvotes}")
