def menu(pool,context):
	return pool.get('devel.ui.model.menus').tree(fields=['name','label','parent_id','childs_id','action_id','sequence'])
