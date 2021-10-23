import requests

URL = "http://api.urbandictionary.com/v0/define"

class UrbanDefinition:
	def __init__(self, term, definition, example=""):
		self.term = term
		self.definition = definition
		self.example = example

class UrbanDictionaryError(Exception):
	pass

def get_definition(term):
	r = requests.get(URL, params={"term": term})
	try:
		json = r.json()
	except ValueError as e:
		raise UrbanDictionaryError(f"Error parsing json response. {e}")
	try:
		res = []
		for entry in json["list"]:
			temp = UrbanResult(entry["word"], entry["definition"], entry["example"])
			res.append(temp)
	except KeyError as e:
		raise UrbanDictionaryError(f"Error parsing result: {e}")
	return res
