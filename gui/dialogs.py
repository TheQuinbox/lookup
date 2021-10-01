import wx

def input_box(title, message, default_value=""):
	dlg = wx.TextEntryDialog(None, message, title, value=default_value)
	dlg.ShowModal()
	result = dlg.GetValue()
	dlg.Destroy()
	return result
