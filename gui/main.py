import wx
import sys
import bored
from . import info, dialogs, ud
from PyDictionary import PyDictionary
import json
import udpy
from keyboard_handler.wx_handler import WXKeyboardHandler

class MainFrame(wx.Frame):
	def __init__(self, app):
		self.app = app
		self.hidden = False
		self.ud_client = udpy.UrbanClient()
		self.options = ["Fetch a random activity from the Bored API", "Get the definition of a word", "Search Urban Dictionary"]
		wx.Frame.__init__(self, None, title=f"{self.app.name} V{self.app.version}", size=wx.DefaultSize)
		self.handler = WXKeyboardHandler(self)
		self.handler.register_key(self.app.config.shortcut, self.on_hide)
		self.panel = wx.Panel(self)
		self.main_box = wx.BoxSizer(wx.VERTICAL)
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
		self.go.Bind(wx.EVT_BUTTON, self.on_go)
		self.Bind(wx.EVT_CLOSE, self.on_close)
		self.close.Bind(wx.EVT_BUTTON, self.on_close)
		self.panel.Layout()

	def on_close(self, event=None):
		self.Destroy()
		sys.exit()

	def on_go(self, event=None):
		if self.combo.GetValue() == self.options[0]:
			self.on_bored()
		if self.combo.GetValue() == self.options[1]:
			self.on_define()
		elif self.combo.GetValue() == self.options[2]:
			self.on_urban()
		else:
			pass

	def on_bored(self):
		activity = bored.getRandomActivity().activity
		info_gui = info.InfoGui(f"{self.app.name}", "&Activity", activity)
		info_gui.Show()

	def on_define(self):
		word = dialogs.input_box("Word", "Enter the word to define.")
		definition = ""
		dict = PyDictionary(word)
		temp = dict.getMeanings()
		for key in temp.keys():
			definition += f"{key.capitalize()}:\n"
			for k in temp[key].keys():
				definition += f"{k.capitalize()}:\n"
				for m in temp[key][k]:
					definition += f"{m.capitalize()}.\n"
		define_gui = info.InfoGui("Word Definer", "&Definition", f"{definition}")
		define_gui.Show()

	def on_urban(self):
		term = dialogs.input_box("Term", "Enter the term to search for.")
		try:
			defs = self.ud_client.get_definition(term)
		except UrbanDictionaryError:
			wx.MessageBox("Invalid query", "Error", wx.ICON_ERROR)
			return
		ud_gui = ud.UdGui("Urban Dictionary", defs)
		ud_gui.Show()

	def on_hide(self):
		if self.hidden:
			self.hidden = False
			self.Show()
		else:
			self.hidden = True
			self.Hide()
