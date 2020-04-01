from .module import *
from serviceloader.tools.common import Component
from configparser import ConfigParser

class moduless_exception(Exception): pass

class Modules(Component):
	_name = 'modules'
	def __init__(self,config_file=None):
		if config_file:
			self.configure(config_file)
	
	def configure(self,config_file):
		cf = ConfigParser()
		cf.read(config_file)
		self._config = cf

	def _setup(self,cr,pool,uid,registry):
		self._cr = cr
		self._pool = pool
		self._uid = uid
		self._registry = registry

	def _call(self,args):
		if args[0][0] == '_':
			raise modules_exception("The method <%s> of service <%s> is private. You can not call it remotely." % (args[0],self._name))

		rmsg = []
		method = getattr(self,args[0],None)
		if method is None:
			raise moduless_exception("The method <%s> of service <%s> not found. You can not call it remotely." % (args[0],self._name))
		if callable(method):
			kwargs = {}
			if len(args) > 1 and type(args[1]) == dict:
				for key in args[1].keys():
					kwargs[key] = args[1][key]
			rmsg.extend(method(**kwargs))

		return rmsg 

	def install(self,modules):
		return install(self._cr,self._pool,self._uid,self._registry,modules)
		
	def uninstall(self,modules):
		return uninstall(self._cr,self._pool,self._uid,self._registry,modules)

	def upgrade(self,modules):
		return upgrade(self._cr,self._pool,self._uid,self._registry,modules)
	
	def sysinstall(self):
		self._registry._load_modules()
		return sysinstall(self._cr,self._pool,self._uid,self._registry)

	def sysupgrade(self):
		return sysupgrade(self._cr,self._pool,self._uid,self._registry)

	def upgrademoduleslist(self,db):
		return upgrademoduleslist(self._cr,self._pool,self._uid,self._registry,db)
