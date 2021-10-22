import wx

class MainFrame(wx.Frame):
	def __init__(self):
		wx.Dialog.__init__(self, None, title="Lookup", size=wx.DefaultSize)
		self.panel = wx.Panel(self)
		self.main_box = wx.BoxSizer(wx.VERTICAL)
		self.panel.Layout()
