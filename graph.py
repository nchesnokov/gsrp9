import ctypes
from toposort import toposort,toposort_flatten

class Graph(dict):
	def __init__(self,vals):
		if type(vals) == dict:
			self[id(vals)] = set()
			for key,val in vals.items():
				if type(val) in (list,tuple):
					for v1 in val:
						if type(v1) == dict:
							self._graph(v1,id(vals))
		elif type(vals) in (list,tuple):
			for val in vals:
				if type(val) == dict:
					self[id(val)] = set()
					for key,val1 in val.items():
						if type(val1) in (list,tuple):
							for v1 in val1:
								if type(v1) == dict:
									self._graph(v1,id(val))


	def _graph(self,vals,oid):
		self.setdefault(id(vals),set()).add(oid)
		for key,val in vals.items():
			if type(val) in (list,tuple):
				for v1 in val:
					if type(v1) == dict:
						self._graph(v1,oid)

if __name__ == '__main__':
	a=[{'a':'d','b':'e'},{'e':'f'}]
	b=[{'h':'i','k':'l'},{'x':'y'}]
	a2 = 2
	a3 = 3 
	v = [{'a1':[{'aa1':a}],'b1':a3,'c1':a2},{'a2':a,'b2':b,'c2':a3}]
	g = Graph(v)
	print('G:',g)
	r = list(toposort(g))
	print('R:',r)
	for l in r:
		for k in list(l):
			if k:
				print('K:',k,ctypes.cast(k, ctypes.py_object).value)
