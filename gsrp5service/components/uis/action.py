import web_pdb
from .view import get_meta_by_window_action_id_v2

def run(pool,type_obj,action_id,context):
	#web_pdb.set_trace()
	r = pool.get('bc.ui.obj.actions').select(['name','view_id'],[('type_obj','=',type_obj),('name','=',action_id)],context)
	if len(r) > 0:
		return [{'model':get_meta_by_window_action_id_v2(pool,action_id,context)[0]}]

