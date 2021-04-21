# import ctypes

# class Node(dict):
	# _parents = {}
	# _childs = {}
	# _oid = None
	
	# def __init__(self,row):
		# for k,v in row.items():
			# if type(v) in (list,tuple):
				# self._childs[k] = ArrayNode(v)
			# else:
				# self[k] = v
		# self._oid = str(id(row))
	
	# def __del__(self):
		# for p in list(self._parents.keys()):
			# del self._parents[p]
		
		# for c in list(self._childs.keys()):
			# del self._childs[c]
	
	# def _addParent(self, key, row):
		# self._parents[key] = Node(row)

	# def _addChild(self, key,row):
		# self._childs[key] = Node(row)


	# def _deleteParent(self, rid):
		# del self._parents[rid]

	# def _deleteChild(self, rid):
		# self._childs[rid]
		
	# def __str__(self):
		# return f"\n\tNode:[{self._oid} parents:{'-'.join([dict.__str__(v) for k,v in self._parents.items()])} childs:{'-'.join([object.__str__(v) for k,v in self._childs.items()])}"+ ']'

# class NodeRef(dict):
	# _parents = {}
	# _childs = {}
	# _oid = {}
	# def __init__(self,node):
		# if isinstance(node,Node):
			# for p in node._parents.key():
				# self._parents[p] = p
			# for c in node._childs.key():
				# self._childs[c] = c
	
			# self._oid[node._oid] = node._oid
		
		# elif isinstance(node,dict):
			# for k,v in node.items():
				# if type(v) in (list,tuple):
					# self._childs[k] = ArrayNodeRef(v)
			# self._oid[str(id(row))] = str(id(row))

	# def __str__(self):
		# return f"NodeRef:[{self._oid} parents: {'-'.join([self._parents[k].__str__() for k in self._parents.keys()])} childs:{'-'.join([object.__str(v) for k,v in self._childs.items()])}" +']'

			
# class ArrayNode(list):
	# _oids = []
	# def __init__(self,rows=[]):
		# for row in rows:
			# super(ArrayNode,self).append(Node(row))	
			# self._oids.append(str(id(row)))
	# def append(self,row):
		# super(ArrayNode,self).append(Node(row))
		# self._oids.append(str(id(row)))

	# def remove(self,row):
		# super(ArrayNode,self).remove(row)
		# self._oids.remove(str(id(row)))
	
	# def clear(self):
		# super(ArrayNode,self).clear()
		# self._oids.clear()
	
	# def  insert(i,row):
		# super(ArrayNode,self).insert(i,Node(row))
		# self._oids.insert(i,str(id(row)))

	# def  pop(i):
		# self._oids.pop(i)
		# return super(ArrayNode,self).pop(i)
	
	# def __str__(self):
		# return '\n\t\tArrayNode:['+','.join([list.__str__(v) for v in self]) +'\n\t]'
		
# class ArrayNodeRef(dict):
	# def __init__(self,arraynode):
		# if isinstance(arraynode,ArrayNode):
			# for idx,oid in enumerate(arraynode._oids):
				# self[oid] = NodeRef(arraynode[idx])	
		# elif isinstance(arraynode,[list,tuple]):
			# for row in arraynode:
				# super(ArrayNodeRef,self).append(NodeRef(row))	
				# self._oids.append(str(id(row)))

	# def __str__(self):
		# return 'ArrayNodeRef:['+','.join([dict.__str__(v) for v in self]) +']'

# class EntryNode(list):
	# _oids = []
	# def __init__(self,v):
		# if type(v) == dict:
			# super(EntryNode,self).append(Node(v))	
		# elif type(v) in (list,tuple):
			# super(EntryNode,self).append(ArrayNode(v))	

		# self._oids.append(str(id(v)))
	
	# def append(self,row):
		# super(EntryNode,self).append(Node(row))
		# self._oids.append(str(id(row)))

	# def remove(self,row):
		# super(EntryNode,self).remove(row)
		# self._oids.remove(str(id(row)))
	
	# def clear(self):
		# super(EntryNode,self).clear()
		# self._oids.clear()
	
	# def  insert(i,row):
		# super(EntryNode,self).insert(i,Node(row))
		# self._oids.insert(i,str(id(row)))

	# def  pop(i):
		# self._oids.pop(i)
		# return super(EntryNode,self).pop(i)
	
	# def __str__(self):
		# return 'EntryNode:[\n'+','.join([str(v) for v in self]) + '\n\t]'
		
# class EntryNodeRef(list):
	# def __init__(self,entrynode):
		# self.extend(entrynode._oids)				

# def diffNode(n1,n2):
	# diffs = {}
	# if isinstance(n1,NodeRef) and isinstance(n2,Node) or isinstance(n2,NodeRef) and isinstance(n1,Node):
		# if isinstance(n2,Node):
			# x1 = n1
			# x2 = NodeRef(n2)
			# v = ctypes.cast(int(n1._oid), ctypes.py_object).value
			
			# v1 = set(v.keys())
			# v2 = set(n2.keys())
			# diffs_v_d = v1-v2
			# diffs_v_i = v2-v1
			# diffs_v_u = v2.intersection(v1)
			# diffs_u = {}
			# for k in diffs_v_u:
				# if v[k] != n2[k]:
					# diffs_u.setdefault(x2._ois,{})[k] = v[k]
		# else:
			# x1 = NodeRef(n2)
			# x2 = n1

			# v = ctypes.cast(int(n2._oid), ctypes.py_object).value
			
			# v2 = set(v.keys())
			# v1 = set(n1.keys())
			# diffs_v_d = v1-v2
			# diffs_v_i = v2-v1
			# diffs_v_u = v1.intersection(v2)

			# diffs_u_i = {}
			# for k in diffs_v_i:
				# diffs_u_i.setdefault(x1._oid,{})[k] = v[k]


			# diffs_u = {}
			# for k in diffs_v_u:
				# if v[k] != n1[k]:
					# diffs_u.setdefault(x1._oid,{})[k] = v[k]
			
		# p1 = set(n1._parents.keys())
		# c1 = set(n1._childs.keys())
	
		# p2 = set(n2._parents.keys())
		# c2 = set(n2._childs.keys())
		
		# diffs_p_d = p1-p2
		# diffs_p_i = p2-p1

		# diffs_c_d = c1-c2
		# diffs_c_i = c2-c1

		# if len(diffs_p_d) > 0:
			# diffs.setdefault('__remove_parents__',[]).extend(list(diffs_p_d))

		# if len(diffs_p_i) > 0:
			# diffs.setdefault('__append_parents__',[]).extend(list(diffs_p_i))

		# if len(diffs_c_d) > 0:
			# diffs.setdefault('__remove_childs__',[]).extend(list(diffs_c_d))

		# if len(diffs_c_i) > 0:
			# diffs.setdefault('__append_childs__',[]).extend(list(diffs_c_i))
			
		# if len(diffs_v_d) > 0:
			# diffs.setdefault('__delete__',[]).extend(list(diffs_c_i))
			
		# if len(diffs_v_i) > 0:
			# diffs.setdefault('__insert__',{}).update(diffs_u_i)

		# if len(diffs_u) > 0:
			# diffs.setdefault('__update__',{}).update(diffs_u)

	# return diffs

# def diffArrayNode(a1,a2):
	# diffs = {}
	# if isinstance(a1,ArrayNodeRef) and isinstance(a2,ArrayNode) or isinstance(a2,ArrayNodeRef) and isinstance(a1,ArrayNode):
		# if isinstance(a2,Node):
			# x1 = a1
			# x2 = ArrayNodeRef(a2)
		
			# v1 = set(a1)
			# v2 = set(a2._oids)
			# diffs_v_d = v1-v2
			# diffs_v_i = v2-v1
			# diffs_v_u = v2.intersection(v1)
			# diffs_u = {}
			# for k in diffs_v_u:
				# d2 = a2[a2._oids.index(k)]
				# d1 = ctypes.cast(int(k), ctypes.py_object).value
				# diffs_u.update(diffNode(d1,d2))
		# else:
			# x1 = NodeRef(a2)
			# x2 = a1
			
			# v2 = set(a2)
			# v1 = set(a1._oids)
			# diffs_v_d = v1-v2
			# diffs_v_i = v2-v1
			# diffs_v_u = v1.intersection(v2)

			# diffs_u = {}
			# for k in diffs_v_u:
				# d1 = a1[a1._oids.index(k)]
				# d2 = ctypes.cast(int(k), ctypes.py_object).value
				# diffs_u.update(diffNode(d2,d1))

		# if len(diffs_p_d) > 0:
			# diffs.setdefault('__remove_',[]).extend(list(diffs_p_d))

		# if len(diffs_p_i) > 0:
			# diffs.setdefault('__append__',[]).extend(list(diffs_p_i))

		# if len(diffs_u) > 0:
			# diffs.update(diffs_u)


	# return diffs
	

# if __name__ == '__main__':
	# v = {'a':1,'b':'c','c':[{'t1':1},{'e2':'c2'}]}
	
	# d = EntryNode(v)
	# print(d)
