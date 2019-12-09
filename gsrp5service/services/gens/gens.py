import logging
from services.gens import roles,menus,views,examples,tests,i18n,tr

class servicegens_exception(Exception): pass

_logger = logging.getLogger('listener.' + __name__)

class ServiceGen(object):

	_name = 'gen'
	
	def __init__(self,cr,pool,uid,registry):
		self._cr = cr
		self._pool = pool
		self._uid = uid
		self._registry = registry

	def role(self,modules=None, context={}):
		return roles.Area(self._cr,self._pool,self_uid,self._registry,modules,context)

	def menu(self,modules=None, context={}):
		return menus.Area(self._cr,self._pool,self_uid,self._registry,modules,context)

	def view(self,modules = None, context={}):
		return views.Area(self._cr,self._pool,self_uid,self._registry,modules,context)

	def ui(self,modules=None, context={}):
		log = []

		log.append(views.Area(self._cr,self._pool,self_uid,self._registry,modules,context))
		log.append(roles.Area(self._cr,self._pool,self_uid,self._registry,modules, context))
		log.append(menus.Area(self._cr,self._pool,self_uid,self._registry,modules, context))

		return log

	def examples(self,modules = None, context={}):
		return examples.Area(self._cr,self._pool,self_uid,self._registry,modules, context)

	def tests(self,modules = None, context={}):
		return tests.Area(self._cr,self._pool,self_uid,self._registry,modules, context)

	def i18n(self,modules = None, context={}):
		return i18n.Area(self._cr,self._pool,self_uid,self._registry,modules, context)

	def tr(self,modules = None, context={}):
		log = []
		return tr.Area(self._cr,self._pool,self_uid,self._registry,modules, context)
	
	def all(self,modules = None, context={}):
		log = []

		log.append(views.Area(self._cr,self._pool,self_uid,self._registry,modules, context))
		log.append(roles.Area(self._cr,self._pool,self_uid,self._registry,modules, context))
		log.append(menus.Area(self._cr,self._pool,self_uid,self._registry,modules, context))

		log.append(examples.Area(self._cr,self._pool,self_uid,self._registry,modules, context))
		log.append(tests.Area(self._cr,self._pool,self_uid,self._registry,modules, context))
		log.append(i18n.Area(self._cr,self._pool,self_uid,self._registry,modules, context))
		log.append(tr.Area(self._cr,self._pool,self_uid,self._registry,modules, context))

		return log
