import logging
import copy

from copy import deepcopy

_logger = logging.getLogger('listener.' + __name__)

from configparser import ConfigParser
from serviceloader.tools.common import Component


class Models(Component):

	def __init__(self,config_file=None):
		if config_file:
			self.configure(config_file)
	
	def configure(self,config_file):
		cf = ConfigParser()
		cf.read(config_file)
		self._config = cf

	def _setup(self,cr,pool,uid,session):
		self._cr = cr
		self._pool = pool
		self._uid = uid
		self._session = session
	
	def _setupUID(self,uid):
		self._uid = uid

	def _call(self,args):
		rmsg = []
		model = self._pool.get(args[0])
		method = getattr(model,args[1])
		if callable(method):
			kwargs = {}
			if args[1] in ('create','read','write','modify','unlink','insert','tree','select','update','upsert','delete','do_action','m2munlink','remote_call','do_compute','do_upload_csv'):
				kwargs['cr'] = self._cr
				kwargs['pool'] = self._pool
				kwargs['uid'] = self._uid		
	
			if len(args) > 2 and type(args[2]) == dict:
				for key in args[2].keys():
					kwargs[key] = args[2][key]

			if args[1] in ('create','read','write','modify','unlink','insert','tree','select','update','upsert','delete','do_action','m2munlink','remote_call','do_compute'):
				rmsg.extend(method(**kwargs))
			else:
				rmsg.append(method(**kwargs))

		if 'context' in kwargs and 'cache' in kwargs['context'] and kwargs['context']['cache']:
			oid = kwargs['context']['cache']
			if args[1] == 'read':
				if len(rmsg) > 0:
					rmsg[0] = self._session._cache[oid]._do_read(args[0],rmsg[0])
		
		return rmsg 
