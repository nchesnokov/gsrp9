# from treelib import Node, Tree
# import toposort
# class Topology(object):
	# def _get_inodes(self,inodes,name):
		# model = self._objects['models'][name]

		# m2orelatedfields = model._m2orelatedfields
		# objs = []
		# for m2orelatedfield in m2orelatedfields:
			# objs.append(model._columns[m2orelatedfield].obj)
			
		# if len(objs) > 0 and name not in inodes:
			# inodes[name] = set(objs)
			# for obj in objs:	
				# inodes |= self._get_inodes(inodes,obj)

		# o2mfields = model._o2mfields
		# for o2mfield in o2mfields:
			# obj = model._columns[o2mfield].obj
			# if obj not in inodes:
				# inodes |= self._get_inodes(inodes,obj)
		# #web_pdb.set_trace()
		
		# childs = dict(list(filter(lambda x: type(x[1]) in (list,tuple),values.items()))))
		# for key in childs.keys():
			# pass
		
		# return inodes

	# def _load_schema(self,models):
		# for key in models.keys():
			# if isinstance(models[key],ModelInherit):
				# continue
			# inodes = {}
			# inodes = self._get_inodes(inodes,models[key]._name)
			# self._schema = (list(toposort.toposort(inodes)),toposort.toposort_flatten(inodes, sort=True))
			# print('SCHEMA:',key,models[key]._schema)

# tree = Tree()
# tree.create_node("Harry", "harry")  # root node
# tree.create_node("Jane", "jane", parent="harry")
# tree.create_node("Bill", "bill", parent="harry")
# tree.create_node("Diane", "diane", parent="jane")
# tree.create_node("Mary", "mary", parent="diane")
# tree.create_node("Mary-1", "mary-1", parent="harry")
# tree.create_node("Mary-2", "mary-2", parent="diane")
# tree.create_node("Mark", "mark", parent="jane")
# tree.create_node("Diane-2", "diane-2", parent="jane")
# tree.show()
