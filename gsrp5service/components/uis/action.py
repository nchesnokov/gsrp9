import web_pdb
from .view import get_meta_by_window_action_id_v2

def run(pool,action_id,context):
	#web_pdb.set_trace()
	r = pool.get('bc.actions').select(['name','ta'],[('name','=',action_id)],context)
	tp = r[0]['ta']
	if tp == 'model':
		return [{tp:get_meta_by_window_action_id_v2(pool,action_id,context)[0]}]
	elif tp == 'report':	
		return [Exception('Type аction %s not implemented' % (tp,))]
	elif tp == 'wks':
		return [Exception('Type аction %s not implemented' % (tp,))]
	elif tp == 'server':
		return [Exception('Type аction %s not implemented' % (tp,))]		

