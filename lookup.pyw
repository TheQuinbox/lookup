import sys
sys.dont_write_bytecode = True
from gui import main
import wx

if __name__ == "__main__":
	app = wx.App()
	frame = main.MainFrame()
	frame.Show()
	app.MainLoop()
