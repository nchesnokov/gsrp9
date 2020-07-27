import logging
import copy

import web_pdb

from copy import deepcopy

_logger = logging.getLogger('listener.' + __name__)

from configparser import ConfigParser
from serviceloader.tools.common import Component

class orm_exception(Exception): pass

class Models(Component):

	def __init__(self,config_file=None):
		if config_file:
			self.configure(config_file)
	
	def configure(self,config_file):
		cf = ConfigParser()
		cf.read(config_file)
		self._config = cf

	@property
	def _cr(self):
		return self._session._cursor

	@property
	def _pool(self):
		return self._session._models

	@property
	def _uid(self):
		return self._session._uid

	def _setup(self,session):
		self._session = session
	
	def _setupUID(self,uid):
		self._uid = uid

	def _call(self,args):
		if args[1][0] == '_':
			raise orm_exception('Your can`t call private method: <%s> of model: <%s>' % (args[1],args[0]))
		rmsg = []
		model = self._pool.get(args[0])
		method = getattr(model,args[1])
		if callable(method):
	
			if len(args) > 2 and type(args[2]) == dict:
				kwargs = args[2]
				context = {}
				
				if  'context' in kwargs:
					context = kwargs['context']
				
				if 'cache' in context:
					kwargs['uid'] = kwargs['context']['cache']
				else:
					kwargs['uid'] = self._session._mcache(['open',{'mode':args[1],'context':kwargs['context']}])[0]
				rmsg.extend(method(**kwargs))

		return rmsg 
