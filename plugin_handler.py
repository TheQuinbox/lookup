import yapsy

class Plugin(yapsy.IPlugin.IPlugin):
	def get_text(self):
		pass

def Get_plugin_manager():
	manager = yapsy.PluginManager.PluginManager(directories_list=["plugins", "plugin"], plugin_info_ext="lookup")
	return manager
