from yapsy.IPlugin import IPlugin
from yapsy.PluginManager import PluginManager

class Plugin(IPlugin):
	def get_text(self):
		pass

def Get_plugin_manager():
	manager = PluginManager(directories_list=["plugins", "plugin"], plugin_info_ext="lookup")
	return manager
