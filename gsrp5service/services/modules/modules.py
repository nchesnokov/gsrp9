from services.modules.module import *

class ServiceModules(object):

	_name = "modules"

	def __init__(self,cr,pool,uid,registry):
		self._cr = cr
		self._pool = pool
		self._uid = uid
		self._registry = registry

	def install(self,modules):
		return install(self._cr,self._pool,self._uid,self._registry,modules)
		
	def uninstall(self,modules):
		return uninstall(self._cr,self._pool,self._uid,self._registry,modules)

	def upgrade(self,cr,pool,uid,registry,sid,modules):
		return upgrade(self._cr,self._pool,self._uid,self._registry,modules)
	
	def sysinstall(self):
		return sysinstall(self._cr,self._pool,self._uid,self._registry,modules)

	def sysupgrade(self):
		return sysupgrade(self._cr,self._pool,self._uid,self._registry)

	def upgrademoduleslist(self,db):
		return upgrademoduleslist(self._cr,self._pool,self._uid,self._registry,db)
