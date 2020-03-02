import logging
import copy

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

	def _setup(self,cr,pool,uid,session):
		self._cr = cr
		self._pool = pool
		self._uid = uid
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
			#if args[1] in ('create','read','write','modify','unlink','insert','tree','select','update','upsert','delete','do_action','m2munlink','remote_call','do_compute','do_upload_csv'):
			kwargs = {'cr':self._cr,'pool':self._pool,'uid':self._uid}
	
			if len(args) > 2 and type(args[2]) == dict:
				for key in args[2].keys():
					kwargs[key] = args[2][key]

			# if args[1] in ('create','read','write','modify','unlink','insert','tree','select','update','upsert','delete','do_action','m2munlink','remote_call','do_compute'):
				# rmsg.extend(method(**kwargs))
			# else:
				# rmsg.append(method(**kwargs))

			if args[1] == 'read':
				if 'context' in kwargs and 'cache' in kwargs['context'] and kwargs['context']['cache']:
					oid = kwargs['context']['cache']
					rmsg.append(self._session._cache[oid]._do_read(args[0],kwargs))
			elif args[1] == 'create-1':
					rmsg[0] = self._session._cache[oid]._do_create(args[0],kwargs)
			elif args[1] == 'write-1':
					rmsg[0] = self._session._cache[oid]._do_write(args[0],kwargs)
			elif args[1] == 'modify-1':
					rmsg[0] = self._session._cache[oid]._do_modify(args[0],kwargs)
			elif args[1] == 'unlink-1':
					rmsg[0] = self._session._cache[oid]._do_unlink(args[0],kwargs)
			elif args[1] == 'insert-1':
					rmsg[0] = self._session._cache[oid]._do_insert(args[0],kwargs)
			elif args[1] == 'select-1':
					rmsg[0] = self._session._cache[oid]._do_select(args[0],kwargs)
			elif args[1] == 'update-1':
					rmsg[0] = self._session._cache[oid]._do_update(args[0],kwargs)
			elif args[1] == 'upsert-1':
					rmsg[0] = self._session._cache[oid]._do_upsert(args[0],kwargs)
			elif args[1] == 'delete-1':
					rmsg[0] = self._session._cache[oid]._do_delete(args[0],kwargs)
			elif args[1] == 'tree-1':
					rmsg[0] = self._session._cache[oid]._do_tree(args[0],kwargs)

			else:
				v = method(**kwargs)
				if type(v) in (list,tuple):
					rmsg.extend(v)
				else:
					rmsg.append(v)

		return rmsg 
