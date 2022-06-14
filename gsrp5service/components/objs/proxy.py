
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
		self._methods['_lang2id'] = proxy._getLangID
	
	
	def __getattr__(self,name):
		if name in self._methods:
			return self._methods[name]
	
	# def call(*args,**kwars):
		# return self._methods['call'](*args,**kwargs)

	# @property
	# def cr(self):
		# return self._methods['cr']()
	
	# @property
	# def uid(self):
		# return self._methods['uid']()

	# @property
	# def pool(self):
		# return self._methods['pool']()

	# def interface(self,key,name,*args,**kwargs):
		# return self._methods['interface'](key,name,*args,**kwargs)

	# def _mcache(self,args):
		# return self._methods['_mcache'](args)
			

	def get(self,key):
		return self._methods['get'](key)
	
