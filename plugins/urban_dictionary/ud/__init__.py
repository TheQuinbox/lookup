import plugin_handler
from . import api

class UrbanDictionaryPlugin(plugin_handler.Plugin):
	def get_text(self):
		final = ""
		results = api.get_definition("Quin")
		for i in results:
			final += i.to_string()
		return final
