from yapsy.IPlugin import IPlugin
from yapsy.PluginManager import PluginManager

class Plugin(IPlugin):
	def get_text(self):
		pass

	def create_panel(self, frame):
		pass

def get_plugin_manager():
	return PluginManager(
	    directories_list=["plugins", "plugin"], plugin_info_ext="lookup")
