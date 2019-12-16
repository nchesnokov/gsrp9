from .view import view,get_viewname_by_window_action_id,get_view_by_window_action_id,get_view_by_window_action_id_v2,get_meta_by_window_action_id_v2,get_view_by_name,get_view_by_name_v2,get_views_of_model_v2
from .menu import menu
from .action import run
from serviceloader.tools.common import Component
from configparser import ConfigParser

class serviceui_exception(Exception): pass

class Uis(Component):

	def __init__(self,config_file=None):
		if config_file:
			self.configure(config_file)
	
	def configure(self,config_file):
		cf = ConfigParser()
		cf.read(config_file)
		self._config = cf

	def _setup(self,cr,pool,uid):
		self._cr = cr
		self._pool = pool
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
	
	# def get_viewname_by_window_action_id(self,session,cr,pool,uid,registry,action_id):
		# return  get_viewname_by_window_action_id(session,cr,pool,uid,registry,action_id)

	# def get_view_by_window_action_id(self,session,cr,pool,uid,registry,action_id):
		# return get_view_by_window_action_id(session,cr,pool,uid,registry,action_id)

	# def get_view_by_window_action_id_v2(self,session,cr,pool,uid,registry,action_id):
		# return get_view_by_window_action_id_v2(session,cr,pool,uid,registry,action_id)

	# def get_meta_by_window_action_id_v2(self,session,cr,pool,uid,registry,action_id):
		# return get_meta_by_window_action_id_v2(session,cr,pool,uid,registry,action_id)

	# def get_view_by_name(self,session,cr,pool,uid,registry,name):
		# return get_view_by_name(session,cr,pool,uid,registry,name)

	def get_view_by_name_v2(self,cr,pool,uid,name):
		return get_view_by_name_v2(cr,pool,uid,name)

	# def get_views_of_model_v2(self,session,cr,pool,uid,registry,model):
		# return get_views_of_model_v2(session,cr,pool,uid,registry,model)

	# def view(self,session,cr,pool,uid,registry,action_id = None, name = None):
		# return view(session,cr,pool,uid,registry,action_id,name)
		
	def menu(self,cr,pool,uid,context={}):
		return menu(cr,pool,uid,context)
