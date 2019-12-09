import logging
import copy

from copy import deepcopy

_logger = logging.getLogger('listener.' + __name__)

class ServiceModels(object):

	_name = 'ServiceModels'
	
	def _execute(self, session, args):
		rmsg = []
		model = session._models.get(args[0])
		method = getattr(model,args[1])
		print('ARGS-MODELS:',method,callable(method),args)
		if callable(method):
			kwargs = {}
			if args[1] in ('create','read','write','modify','unlink','insert','tree','select','update','upsert','delete','do_action','m2munlink','remote_call','do_compute','do_upload_csv'):
				kwargs['cr'] = session._cursor
				kwargs['pool'] = session._models
				kwargs['uid'] = session._uid		
	
			if len(args) > 2 and type(args[2]) == dict:
				for key in args[2].keys():
					kwargs[key] = args[2][key]

			if args[1] in ('create','read','write','modify','unlink','insert','tree','select','update','upsert','delete','do_action','m2munlink','remote_call','do_compute'):
				rmsg.extend(method(**kwargs))
			else:
				rmsg.append(method(**kwargs))

		print('ARGS-RMSG:',args[1],rmsg)
		if 'context' in kwargs and 'cache' in kwargs['context'] and kwargs['context']['cache'] and args[1] == 'read':
			if len(rmsg) > 0:
				oid = kwargs['context']['cache']
				rmsg[0] = session._cache[oid]._do_read(args[0],rmsg[0])

		return rmsg 
