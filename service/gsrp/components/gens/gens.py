import logging
from . import roles,menus,views,examples,tests,i18n,tr

from serviceloader.tools.common import Service, Component
from configparser import ConfigParser

class servicegens_exception(Exception): pass

_logger = logging.getLogger('listener.' + __name__)

class Gens(Component):

	def __init__(self,config_file=None):
		if config_file:
			self.configure(config_file)
	
	@property
	def _cr(self):
		return self._session._cursor

	@property
	def _models(self):
		return self._session._models

	@property
	def _uid(self):
		return self._session._uid

	@property
	def _registry(self):
		return self._session._registry

	def configure(self,config_file):
		cf = ConfigParser()
		cf.read(config_file)
		self._config = cf

	
	def _setup(self,session):
		self._session = session

	def _call(self,args):
		if args[0][0] == '_':
			raise servicegens_exception("The method <%s> of service <%s> is private. You can not call it remotely." % (args[1],self._name))

		rmsg = []
		method = getattr(self,args[0],None)
		if method and callable(method):
			kwargs = {}
			if len(args) > 1 and type(args[1]) == dict:
				for key in args[1].keys():
					kwargs[key] = args[1][key]
			rmsg.extend(method(**kwargs))

		return rmsg 


	def role(self,modules=None, context={}):
		return roles.Area(self,modules,context)

	def menu(self,modules=None, context={}):
		return menus.Area(self,modules,context)

	def view(self,modules = None, context={}):
		return views.Area(self,modules,context)

	def ui(self,modules=None, context={}):
		log = []

		log.append(views.Area(self,modules,context))
		log.append(roles.Area(self,modules, context))
		log.append(menus.Area(self,modules, context))

		return log

	def examples(self,modules = None, context={}):
		return examples.Area(self,modules, context)

	def tests(self,modules = None, context={}):
		return tests.Area(self,modules, context)

	def i18n(self,modules = None, context={}):
		return i18n.Area(self,modules, context)

	def tr(self,modules = None, context={}):
		log = []
		return tr.Area(self,modules, context)
	
	def all(self,modules = None, context={}):
		log = []

		log.append(views.Area(self,modules, context))
		log.append(roles.Area(self,modules, context))
		log.append(menus.Area(self._registry,modules, context))

		log.append(examples.Area(self,modules, context))
		log.append(tests.Area(self,modules, context))
		log.append(i18n.Area(self,modules, context))
		log.append(tr.Area(self,modules, context))

		return log
