from .view import view,get_viewname_by_window_action_id,get_view_by_window_action_id,get_view_by_window_action_id_v2,get_meta_by_window_action_id_v2,get_view_by_name,get_view_by_name_v2,get_views_of_model_v2,get_meta_of_models_v2
from .menu import menu
from .action import run
from serviceloader.tools.common import Component
from configparser import ConfigParser

class serviceui_exception(Exception): pass

class Uis(Component):
	_name = 'uis'
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

	def _call(self, args):
		if args[0][0] == '_':
			raise serviceui_exception("The method <%s> of service <%s> is private. You can not call it remotely." % (args[1],self._name))

		rmsg = []
		if hasattr(self,args[0]):
			method = getattr(self,args[0],None)
			if callable(method):
				kwargs = {}
				kwargs['cr'] = self._cr
				kwargs['pool'] = self._pool
				kwargs['uid'] = self._uid
				
				if len(args) > 1 and type(args[1]) == dict:
					for key in args[1].keys():
						kwargs[key] = args[1][key]
		
				rmsg.extend(method(**kwargs))
			else:
				raise Exception("Method %s of service %s is not callable" % (args[1],self._name))
		else:
			raise Exception("Method %s of service %s is not found" % (args[1],self._name))

		return rmsg

	def action(self,cr,pool,uid,action_id,context):
		return run(cr,pool,uid,action_id,context)
	
	def get_view_by_name_v2(self,cr,pool,uid,name,):
		return get_view_by_name_v2(cr,pool,uid,name)
	
	def get_meta_of_models_v2(self,cr,pool,uid,model,context):
		return [get_meta_of_models_v2(cr,pool,uid,model,context)]
		
	def menu(self,cr,pool,uid,context={}):
		model = pool.get('bc.ui.menus')
		tuid = self._session._mcache(['open',{'mode':'select','context':{}}])[0]
		return menu(model,tuid,context)
