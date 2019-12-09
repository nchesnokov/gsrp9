def menu(cr,pool,uid,context):
	return pool.get('bc.ui.menus').tree(cr,pool,uid,fields=['name','label','parent_id','childs_id','action_id','sequence'])
