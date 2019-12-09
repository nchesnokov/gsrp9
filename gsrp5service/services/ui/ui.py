from .view import view,get_viewname_by_window_action_id,get_view_by_window_action_id,get_view_by_window_action_id_v2,get_meta_by_window_action_id_v2,get_view_by_name,get_view_by_name_v2,get_views_of_model_v2
from .menu import menu
from .action import run

class serviceui_exception(Exception): pass

class ServiceUI(object):

	_name = "ServiceUI"

	def _execute(self, session,args):
		#print('execute-modules:',args)
		if args[0][0] == '_':
			raise serviceui_exception("The method <%s> of service <%s> is private. You can not call it remotely." % (args[1],self._name))

		rmsg = []
		if hasattr(self,args[0]):
			method = getattr(self,args[0],None)
			if callable(method):
				#kwargs = {'session':session}
				kwargs = {}
				kwargs['cr'] = session._cursor
				kwargs['pool'] = session._sid._models
				kwargs['uid'] = session._uid
				#kwargs['registry'] = session._sid._registry
				
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
