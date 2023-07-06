def menu(pool,context):
	return pool.get('bc.ui.obj.menus').tree(fields=['type_obj','name','label','parent_id','childs_id','action_id','sequence'])
