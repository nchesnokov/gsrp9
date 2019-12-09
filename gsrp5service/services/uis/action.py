from .view import get_meta_by_window_action_id_v2

def run(cr,pool,uid,action_id,context):
	r = pool.get('bc.actions').select(cr,pool,uid,['name','ta'],[('name','=',action_id)],context)
	tp = r[0]['ta']
	if tp == 'view':
		return [{tp:get_meta_by_window_action_id_v2(cr,pool,uid,action_id)[0]}]
	elif tp == 'report':	
		return [Exception('Type аction %s not implemented' % (tp,))]
	elif tp == 'wks':
		return [Exception('Type аction %s not implemented' % (tp,))]
	elif tp == 'server':
		return [Exception('Type аction %s not implemented' % (tp,))]		

