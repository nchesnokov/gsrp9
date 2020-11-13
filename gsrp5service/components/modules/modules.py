from .module import *
from serviceloader.tools.common import Component
from configparser import ConfigParser

import web_pdb

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

	def _setup(self,session):
		self._session = session

	@property
	def _cr(self):
		return self._session._cursor

	@property
	def _pool(self):
		return self._session._models

	@property
	def _uid(self):
		return self._session._uid

	@property
	def _registry(self):
		return self._session._registry


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

	def load(self,modules):
		return load(self,modules)

	def install(self,modules):
		return install(self,modules)
		
	def uninstall(self,modules):
		return uninstall(self,modules)

	def upgrade(self,modules):
		return upgrade(self,modules)
	
	def sysinstall(self):
		return sysinstall(self)

	def sysupgrade(self):
		return sysupgrade(self)

	def upgrademoduleslist(self,db):
		return upgrademoduleslist(self,db)
