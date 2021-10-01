import wx
import logging

log = logging.getLogger("gui.dialogs")

def input_box(title, message, default_value=""):
	dlg = wx.TextEntryDialog(None, message, title, value=default_value)
	log.debug("Input box initialized.")
	dlg.ShowModal()
	log.debug("Input box shown.")
	result = dlg.GetValue()
	dlg.Destroy()
	log.debug("Input box destroyed.")
	return result
