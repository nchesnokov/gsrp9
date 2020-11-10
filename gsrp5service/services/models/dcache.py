import web_pdb

class DCache(object):
	_oid_keys = {}
	_model_keys = {}
	
	def __init__(self,data):
		if type(data) in (list,tuple):
			oids = self._getList(data)
		elif type(data) == dict:
			oid = self._getDict(data)

	def _getDict(self,data):
		pass
