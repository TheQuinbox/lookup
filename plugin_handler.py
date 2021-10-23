from yapsy.IPlugin import IPlugin
from yapsy.PluginManager import PluginManager
import logging

class Plugin(IPlugin):
	def __init__(self):
		self.log = logging.getLogger("plugin_handler")

	def get_text(self):
		pass

	def create_panel(self, frame):
		pass

def get_plugin_manager():
	manager = PluginManager(directories_list=["plugins", "plugin"], plugin_info_ext="lookup")
	return manager
