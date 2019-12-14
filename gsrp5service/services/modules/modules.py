from .module import *
from serviceloader.tools.common import Service
from configparser import ConfigParser


class Modules(Service):

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
		print('ServiceModules-execute:',args)
		if args[0][0] == '_':
			raise serviceslots_exception("The method <%s> of service <%s> is private. You can not call it remotely." % (args[1],self._name))

		rmsg = []
		method = getattr(self,args[0],None)
		if method and callable(method):
			kwargs = {}
			if len(args) > 1 and type(args[1]) == dict:
				for key in args[1].keys():
					print('modules-args1-key:',args[1][key])
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
		return sysinstall(self._cr,self._pool,self._uid,self._registry)

	def sysupgrade(self):
		return sysupgrade(self._cr,self._pool,self._uid,self._registry)

	def upgrademoduleslist(self,db):
		return upgrademoduleslist(self._cr,self._pool,self._uid,self._registry,db)
