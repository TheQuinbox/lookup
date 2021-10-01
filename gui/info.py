import wx

class InfoGui(wx.Dialog):
	def __init__(self, title, label, text):
		self.title = title
		self.label = label
		self.text = text
		wx.Dialog.__init__(self, None, title=self.title, size=wx.DefaultSize)
		self.panel = wx.Panel(self)
		self.main_box = wx.BoxSizer(wx.VERTICAL)
		self.text_label = wx.StaticText(self.panel, -1, self.label)
		self.text_field = wx.TextCtrl(self.panel, style=wx.TE_READONLY | wx.TE_MULTILINE, size=(600, 600))
		self.main_box.Add(self.text_field, 0, wx.ALL, 10)
		self.text_field.SetValue(self.text)
		self.close = wx.Button(self.panel, wx.ID_CANCEL, "&Close")
		self.main_box.Add(self.close, 0, wx.ALL, 10)
		self.Bind(wx.EVT_CLOSE, self.on_close)
		self.close.Bind(wx.EVT_BUTTON, self.on_close)
		self.panel.Layout()

	def on_close(self, event=None):
		self.Destroy()
