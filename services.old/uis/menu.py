def menu(pool,context):
	return pool.get('bc.ui.menus').tree(fields=['name','label','parent_id','childs_id','action_id','sequence'])
