import logging
import itertools
from functools import reduce

import tools

_logger = logging.getLogger(__name__)


class Graph(dict):
	""" Modules dependency graph.
    The graph is a mapping from module name to Nodes.
	"""
	def add_node(self, name, info):
		max_depth, father = 0, None
		for d in info['depends']:
			n = self.get(d) or Node(d, self, None)  # lazy creation, do not use default value for get()
			if n.depth >= max_depth:
				father = n
				max_depth = n.depth
		if father:
			return father.add_child(name, info)
		else:
			return Node(name, self, info)

	def add_modules(self,packages):
		len_graph = len(self)
		dependencies = dict([(p, info['depends']) for p, info in packages])
		current, later = set([p for p, info in packages]), set()

		while packages and current > later:
			package, info = packages[0]
			deps = info['depends']

			# if all dependencies of 'package' are already in the graph, add 'package' in the graph
			if reduce(lambda x, y: x and y in self, deps, True):
				if not package in current:
					packages.pop(0)
					continue
				later.clear()
				current.remove(package)
				node = self.add_node(package, info)
				#for kind in ('init', 'demo', 'update'):
					#if package in tools.config[kind] or 'all' in tools.config[kind] or kind in force:
						#setattr(node, kind, True)
			else:
				later.add(package)
				packages.append((package, info))
			packages.pop(0)

		#self.update_from_db(cr)

		for package in later:
			unmet_deps = filter(lambda p: p not in self, dependencies[package])
			_logger.error('module %s: Unmet dependencies: %s', package, ', '.join(unmet_deps))

		return len(self) - len_graph


	def __iter__(self):
		level = 0
		done = set(self.keys())
		while done:
			level_modules = sorted((name, module) for name, module in self.items() if module.depth==level)
			for name, module in level_modules:
				done.remove(name)
				yield module
			level += 1

	def __str__(self):
		return '\n'.join(str(n) for n in self if n.depth == 0)


class Node(object):
	""" One module in the modules dependency graph.
	Node acts as a per-module singleton. A node is constructed via
	Graph.add_module() or Graph.add_modules(). Some of its fields are from
	ir_module_module (setted by Graph.update_from_db()).
	"""
	def __new__(cls, name, graph, info):
		if name in graph:
			inst = graph[name]
		else:
			inst = object.__new__(cls)
			graph[name] = inst
		return inst

	def __init__(self, name, graph, info):
		self.name = name
		self.graph = graph
		self.info = info or getattr(self, 'info', {})
		if not hasattr(self, 'children'):
			self.children = []
		if not hasattr(self, 'depth'):
			self.depth = 0

	@property
	def data(self):
		return self.info

	def add_child(self, name, info):
		node = Node(name, self.graph, info)
		node.depth = self.depth + 1
		if node not in self.children:
			self.children.append(node)
		for attr in ('init', 'update', 'demo'):
			if hasattr(self, attr):
				setattr(node, attr, True)
		self.children.sort(key=lambda x: x.name)
		return node

	def __setattr__(self, name, value):
		super(Node, self).__setattr__(name, value)
		if name in ('init', 'update', 'demo'):
			tools.config[name][self.name] = 1
			for child in self.children:
				setattr(child, name, value)
		if name == 'depth':
			for child in self.children:
				setattr(child, name, value + 1)

	def __iter__(self):
		return itertools.chain(iter(self.children), *map(iter, self.children))

	def __str__(self):
		return self._pprint()

	def _pprint(self, depth=0):
		s = '%s\n' % self.name
		for c in self.children:
			s += '%s`-> %s' % ('   ' * depth, c._pprint(depth+1))
		return s
	
class DependsInstall(dict):

	def __init__(self,packages):
		for p,info in packages:
			self[p] = info['depends']
	
	def _depends(self,depends):
		deps = []
		for depend in depends:
			deps.append(depend)
			if depend in self:
				deps.extend(self._depends(self[depend]))
		return deps

	def install(self,name):
		if name in self:
			return list(set(self._depends(self[name])))

		return []

		
class DependsRemove(dict):

	def __init__(self,packages):
		for p,info in packages:
			for m in info['depends']:
				self.setdefault(m,[]).append(p)
	
	def _depends(self,depends):
		deps = []
		for depend in depends:
			deps.append(depend)
			if depend in self:
				deps.extend(self._depends(self[depend]))
		return deps


	def remove(self,name):
		if name in self:
			return list(set(self._depends(self[name])))

		return []

