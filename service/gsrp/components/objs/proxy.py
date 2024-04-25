
class ModelProxy(object):
	_methods = {}
	
	def __init__(self,proxy):
		self._methods['call'] = proxy._call
		self._methods['cr'] = proxy._getCursor
		self._methods['uid'] = proxy._getUid
		self._methods['pool'] = proxy._getPool
		self._methods['interface'] = proxy._getInterface
		self._methods['_mcache'] = proxy._getMCache
		self._methods['get'] = proxy._getModel
		self._methods['lib'] = proxy._getLib
		self._methods['_lang2id'] = proxy._getLangID
	
	
	def __getattr__(self,name):
		if name in self._methods:
			return self._methods[name]
	
