def menu(model,uid,context):
	return model.tree(uid,fields=['name','label','parent_id','childs_id','action_id','sequence'])
