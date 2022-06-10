
class ModelProxy(object):
	_methods = {}
	
	def __init__(self,session):
		self._methods['call'] = session._call
		self._methods['cr'] = session._getCursor
		self._methods['uid'] = session._getUid
		self._methods['pool'] = session._getPool
		self._methods['interface'] = session._getInterface
		self._methods['_mcache'] = session._getMCache
		self._methods['get'] = session._getModel
	
	
	def call(*args,**kwars):
		return self._methods['call'](*args,**kwargs)

	@property
	def cr(self):
		return self._methods['cr']()
	
	@property
	def uid(self):
		return self._methods['uid']()

	@property
	def pool(self):
		return self._methods['pool']()

	def interface(self,key,name,*args,**kwargs):
		return self._methods['interface'](key,name,*args,**kwargs)

	def _mcache(self,args):
		return self._methods['_mcache'](args)
			

	def get(self,key):
		return self._methods['get'](key)
	
