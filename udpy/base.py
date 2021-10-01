import json
import sys
from urllib.parse import quote as urlquote
import requests

UD_DEFID_URL = "https://api.urbandictionary.com/v0/define?defid="
UD_DEFINE_URL = "https://api.urbandictionary.com/v0/define?term="
UD_RANDOM_URL = "https://api.urbandictionary.com/v0/random"

class UrbanDictionaryError(Exception):
	pass

class UrbanDefinition:
	def __init__(self, word, definition, example, upvotes, downvotes):
		self.word = word
		self.definition = definition
		self.example = example
		self.upvotes = upvotes
		self.downvotes = downvotes

	def __str__(self):
		return "%s: %s%s (%d, %d)" % (self.word, self.definition[:50], "..." if len(self.definition) > 50 else "", self.upvotes, self.downvotes)

class UrbanClient:
	def __init__(self, session=None):
		self.session = session or requests.Session()

	def _request(self, url):
		result = self.session.get(url)
		return result.json()

	def get_definition(self, term):
		json = self._request(UD_DEFINE_URL + urlquote(term))
		return _parse(json)

	def get_definition_by_id(self, id):
		json = self._request(UD_DEFID_URL + urlquote(str(defid)))
		return _parse(json)

	def get_random_definition(self):
		json = self._request(UD_RANDOM_URL)
		return _parse(json, check_result=False)

def _parse(json, check_result=True):
	result = []
	if json is None or any(e in json for e in ("error", "errors")):
		raise UrbanDictionaryError("Invalid input for Urban Dictionary API")
	if check_result and ("list" not in json or len(json["list"]) == 0):
		return result
	for definition in json["list"]:
		d = UrbanDefinition(definition["word"], definition["definition"], definition["example"], int(definition["thumbs_up"]), int(definition["thumbs_down"]))
		result.append(d)
	return result
