import plugin_handler
from . import api

class UrbanDictionaryPlugin(plugin_handler.Plugin):
	def get_text(self):
		return api.define("Quin")
