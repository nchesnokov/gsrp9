# --*-- coding: utf-8 --*--	
import sys
import os
import web_pdb
from copy import deepcopy
from functools import reduce
from os.path import join as opj
import toposort
from .loading import *
from .depmod import Graph,Node,DependsInstall,DependsRemove

import gsrp5service.orm.model
from gsrp5service.orm.model import Model,ModelInherit
from gsrp5service.orm.mm import _getRecNameName,_getChildsIdName

import gsrp5service.orm.report
from gsrp5service.orm.report import Report,ReportInherit

import gsrp5service.orm.dialog
from gsrp5service.orm.dialog import Dialog,DialogInherit

import gsrp5service.orm.wizard
from gsrp5service.orm.wizard import Wizard,WizardInherit

import gsrp5service.orm.query
from gsrp5service.orm.query import Query,QueryInherit

import gsrp5service.orm.link

from serviceloader.tools.common import Service, configManagerFixed

from configparser import ConfigParser

class Exception_Registry(Exception): pass

class Registry(Service):

	_module_paths = {}
	_modules = {}
	
	# Матаданные объектов
	_metas ={}
	# Наследования для объектов
	_inherit = {}
	# Наследуемые объекы
	_inherits = {}
	# Классы объектов модуля
	_objs ={}
	# Экземпляры объектов
	_objects = {}
	# Модуль экземпляра объекта
	_moo = {}
	
	_graph = None
	_pwd = None
	_depends = None
	_dependsinstall = None
	_dependsremove = None
	_packages = []

	def __init__(self, config_file=None):
		cf = ConfigParser()
		cf.read(config_file)
		self._config = configManagerFixed(cf,{'globals':{'module_paths':{'addons':None},'able':None}},dkey=['module_paths'])
		module_paths = self._config['globals']['module_paths']
		able = self._config['globals']['able']
		self._pwd = os.path.dirname(os.path.abspath(__file__))
		if module_paths:
			self._module_paths = module_paths
		else:
			self._module_paths = {'addons':None}

		if able:
			self._able = able
		else:
			self._able = ('system','autoinstall','install','noinstall')

		if self._pwd not in sys.path:
			sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))

		
		for key in self._module_paths.keys():
			self._module_paths[key] = filter(lambda x: os.path.isdir(opj(x)), os.listdir(opj(os.path.dirname(os.path.abspath(__file__)),key)))

		self._graph = Graph()
		self._load_modules_info()

	def _reload(self):
		_module_paths = {}
		_modules = {}
		
		_metas ={}
		_inherit = {}
		_inherits = {}
		_objs = {}
		_objects = {}
		_moo = {}
		self._load_modules_info()
		self._graph = Graph()
		self._pwd = os.path.dirname(os.path.abspath(__file__))
		self._depends = None
		self._dependsinstall = None
		self._dependsremove = None
		self._packages = []
		self._modules.clear()
		self._reload_modules_info()
		self._load_modules()
		self._load_inheritables()

	def _load_module_info(self,path):
		return load_module_info(path)

	def _load_modules_info(self):

		for d in list(self._module_paths.keys()):
			mdir = opj(os.path.dirname(os.path.abspath(__file__)),d)
			self._module_paths[d] = list(filter(lambda x: os.path.isdir(opj(mdir,x)), os.listdir(mdir)))

		for path in list(self._module_paths.keys()):
			for name in self._module_paths[path]:
				if os.path.isdir(opj(self._pwd, path, name)) and os.path.exists(opj(self._pwd, path, name, '__manifest__.info')) and os.path.isfile(opj(self._pwd, path, name, '__manifest__.info')):
					info = self._load_module_info(opj(self._pwd, path, name))
					if not info['able'] in self._able:
						continue
					self._modules[name] = {'meta':info,'path':opj(self._pwd,path),'import':path + '.' + name,'_module':name}
					self._packages.append((name,info))
		self._dependsinstall = DependsInstall(self._packages)
		self._dependsremove = DependsRemove(self._packages)
		self._graph.add_modules(self._packages)
		self._depends = [node.name for node in self._graph]

	def _fromlist(self,module):
		_fl = []
		for d in os.walk(opj(self._pwd,self._modules[module]['import'].replace('.',os.path.sep))):
			for f in filter(lambda x: x[-3:] == '.so',d[2]):
				m = d[0].split(os.path.sep)[-1:]
				m.append(f.split('.')[0])
				_fl.append(reduce(lambda x,y: x+'.'+y,m))

		return tuple(_fl)

	def _load_installed_modules(self):
		modules = filter(lambda x: 'state' in self._modules[x] and self._modules[x]['state'] == 'I',[node.name for node in self._graph])
		
		for module in modules:
			self._load_module(module)

	def _load_modules(self):
		modules = [node.name for node in self._graph]
		
		for module in modules:
			self._load_module(module)
		
	def _load_module(self,module):
		if not 'loaded' in self._modules[module] or not self._modules[module]['loaded']:
			load_module(self._modules[module]['import'],self._fromlist(module))
			self._metas = gsrp5service.orm.metaobjects.MetaObjects.__objects__
			for k in self._metas[module].keys():
				self._modules[module][k] = list(self._metas[module][k].keys())
					
			self._modules[module]['loaded'] = True
			
			for obj in self._metas[module].keys():
				for nm in self._metas[module][obj].keys():
					self._objs.setdefault(module,{}).setdefault(obj,{})[nm] = self._copyMeta(self._metas[module][obj][nm])
					meta = self._objs[module][obj][nm]
					self._setModuleOfObjects(obj,nm,module)
					if '_inherits' in meta['attrs'] and meta['attrs']['_inherits'] and len(meta['attrs']['_inherits']) > 0:
						inherits = meta['attrs']['_inherits']
						for key in inherits.keys():
							self._inherits.setdefault(module,{}).setdefault(obj,{}).setdefault(nm,{})[key] = inherits[key]
					
					if '_inherit' in meta['attrs'] and meta['attrs']['_inherit'] and len(meta['attrs']['_inherit']) > 0:
						inherit = meta['attrs']['_inherit']
						for key in inherit.keys():
							self._inherit.setdefault(module,{}).setdefault(obj,{}).setdefault(nm,{})[key] = inherit[key]
			
				self._metaObject_with_inherits(obj,module)

	def _load_inheritables(self):
		modules = [node.name for node in self._graph]
			
		for module in modules:
			self._load_inheritable(module)

	def _load_inheritable(self,module):
		if 'state' in self._modules[module] and self._modules[module]['state'] == 'I':
			self._metaObject_with_inherit(module)

	def _create_module_object(self,obj,name,module):
		return self._create_object(self._objs[module][obj][name])

	def _create_first_module_object(self,obj,name):
		return self._create_object(self._objs[self._getFirstModuleObject(obj,name)])

	def _create_last_module_object(self,obj,name):
		return self._create_object(self._objs[self._getLastModuleObject(obj,name)])

	def _create_object(self,meta):
		cls = type(meta['name'],meta['bases'],meta['attrs'])
		type.__init__(cls, meta['name'],meta['bases'],meta['attrs'])
		obj = cls()
		obj.__init__()				
		return obj	
#
	def _metaObject_with_inherits(self,obj,module):
		if module in self._inherits and obj in self._inherits[module]:
			inherits = self._inherits[module][obj]
			objs = self._objs[module][obj]
			for dst in inherits.keys():
				meta = objs[dst]
				for src in inherits[dst].keys():
					imeta = self._objs[module][obj][src]
					inherit = inherits[dst][src]
					for c in inherit.keys():
						if c == '_methods':
							for method in inherit[c]:
								meta['attrs'][method] = imeta['attrs'][method]
						elif c == '_columns':
							for column in inherit[c]:
								if c not in meta['attrs'] or column not in meta['attrs'][c]:
									meta['attrs'].setdefault(c,{})[column] = imeta['attrs'][c][column]
								else:
									if meta['attrs'][c][column]._type == 'selection':
										meta['attrs'][c][column].selections.extend(imeta['attrs'][c][column].selections)
									else:
										Exception_Registry("Column: %s of model: %s if exists\n" % (column,key))
	
								meta['attrs'][c][column] = imeta['attrs'][c][column]
						elif c == '_actions':
							for action in inherit[c]:
								meta['attrs'].setdefault(c,{})[action] = imeta['attrs'][c][action]
								meta['attrs'][imeta['attrs'][c][action]['method']] = imeta['attrs'][imeta['attrs'][c][action]['method']]
						elif c == '_states':
							for state in inherit[c]:
								meta['attrs'].setdefault(c,{})[state] = imeta['attrs'][state]
						elif c == '_trigers':
							for triger in inherit[c]:
								meta['attrs'].setdefault(c,{})[triger] = imeta['attrs'][c][triger]
						elif c == '_default':
							for dkey in inherit[c]:
								meta['attrs'].setdefault(c,{})[dkey] = imeta['attrs'][c][dkey]
						elif c == '_constraints':
							meta['attrs'][c].extend(imeta['attrs'][c])
						elif c == '_sql_constraints':
							meta['attrs'][c].extend(imeta['attrs'][c])
			self._objs[module][obj][dst] = meta
#	
	def _metaObject_with_inherit(self,obj,module):
		if module in self._inherit and obj in self._inherit[module]:
			inherits = self._inherit[module][obj]
			objs = self._objs[module][obj]
			for src in inherits.keys():
				imeta = objs[src]
				for dst in inherits[src].keys():
					meta = self._objs[module][obj][dst]
					inherit = inherits[src][dst]
					for c in inherit.keys():
						if c == '_methods':
							for method in inherit[c]:
								meta['attrs'][method] = imeta['attrs'][c][method]
						elif c == '_columns':
							for column in inherit[c]:
								if c not in meta['attrs'] or column not in meta['attrs'][c]:
									meta['attrs'].setdefault(c,{})[column] = imeta['attrs'][c][column]
								else:
									if imeta['attrs'][c][column]._type == 'iProperty':
										for attr in ('accept','actions','label', 'readonly','invisible', 'priority', 'domain', 'context', 'pattern','required', 'size', 'on_delete', 'on_update','on_change','on_check', 'translate', 'selections', 'selectable', 'manual', 'help', 'unique','check','family','timezone','relatedy','obj','rel','id1','id2','ref','offset','limit','compute','store','state','icon','cols','delimiter'):
											if attr in ('selections','domain','cols'):
												if hasattr(imeta['attrs'][c][column],attr):
													if hasattr(meta['attrs'][c][column],attr):
														getattr(meta['attrs'][c][column],attr).extend(getattr(imeta['attrs'][c][column],attr))
											elif attr in ('accept','label','priority','pattern','compute','readonly','on_change','on_check','invisible','on_delete','on_update','translate','selectable','manual','help','offset','limit','icon','delimiter'):
												if hasattr(imeta['attrs'][c][column],attr):
													if hasattr(meta['attrs'][c][column],attr):
														setattr(getattr(meta['attrs'][c][column],attr),attr,getattr(imeta['attrs'][c][column],attr))
											elif attr in ('actions','context','cols','state'):
												if hasattr(imeta['attrs'][c][column],attr):
													if hasattr(meta['attrs'][c][column],attr):
														getattr(meta['attrs'][c][column],attr).update(getattr(imeta['attrs'][c][column],attr))
									else:
										Exception_Registry("Column: %s of model: %s if exists\n" % (column,dst))
						elif c == '_actions':
							for action in inherit[c]:
								meta['attrs'].setdefault(c,{})[action] = imeta['attrs']['_actions'][action]
						elif c == '_states':
							for state in inherit[c]:
								meta['attrs'].setdefault(c,{})[state] = imeta['attrs'][c][state]
						elif c == '_trg_upd_cols':
							meta['attrs'].setdefault(c,[]).extend(imeta['attrs'][c])
						elif c == '_trigers':
							for triger in inherit[c]:
								for tk in triger.keys():
									if not meta['attrs'][c]:
										meta['attrs'][c] = []
									if type(triger[tk]) in ('list','tuple'):
										meta['attrs'].setdefault(c,{}).setdefault(triger,[]).extend(triger[tk])
									else:
										meta['attrs'].setdefault(c,{}).setdefault(triger,[]).append(triger[tk])
						elif c == '_default':
							for dkey in inherit[c]:
								meta['attrs'].setdefault(c,{})[dkey] = imeta['attrs'][c][dkey]
						elif c == '_constraints':
							meta['attrs'].setdefault(c,[]).extend(imeta['attrs'][c])
						elif c == '_sql_constraints':
							meta['attrs'].setdefault(c,[]).extend(imeta['attrs'][c])
						elif c == '_auth':
							meta['attrs'].setdefault(c,[]).extend(imeta['attrs'][c])
			
			self._objs[module][obj][dst] = meta
#	
	
	def _get_inodes(self,inodes,name):
		model = self._objects['models'][name]

		m2orelatedfields = model._m2orelatedfields
		objs = []
		for m2orelatedfield in m2orelatedfields:
			objs.append(model._columns[m2orelatedfield].obj)
			
		if len(objs) > 0 and name not in inodes:
			inodes[name] = set(objs)
			for obj in objs:	
				inodes |= self._get_inodes(inodes,obj)

		o2mfields = model._o2mfields
		for o2mfield in o2mfields:
			obj = model._columns[o2mfield].obj
			if obj not in inodes:
				inodes |= self._get_inodes(inodes,obj)
		web_pdb.set_trace()
		
		return inodes

	
	def _load_schema(self,models):
		for key in models.keys():
			if isinstance(models[key],ModelInherit):
				continue
			inodes = {}
			models[key]._schema = self._get_inodes(inodes,models[key]._name)
			print('SCHEMA:',key,models[key]._schema)

	def _reload_modules(self,modules):
		for module in filter(lambda x: x in modules,[node.name for node in self._graph]):
			self._download_module(module)
			self._load_module(module)

	def _download_module(self,module):
		for o in self._objs[module].keys():
			del self._objs[module]
		nodes = [node.name for node in self._graph]
		idx = nodes.index(module)-1
		if idx > 0:
			load_module = nodes[idx]
			self._load_module(load_module)
#
	def _getMetaOfModulesObject(self,obj,name,module):
		if module in self._objs and name in self._objs[module] and name in self._objs[module][obj]: 
			return self._objs[module][obj][name]

	def _setMetaOfModulesObject(self,obj,name,module,meta):
		if not (module in self._objs and name in self._objs[module] and name in self._objs[module][obj]): 
			self._objs.setdefault(module,{}).setdefault(obj,{})[name] = meta
			self._setModuleOfObject(obj,name,module)

#
#
	def _copyMeta(self,meta):
		m ={}
		m['name'] = deepcopy(meta['name'])
		m['bases'] = deepcopy(meta['bases'])
		m['attrs'] = {}
		for k in meta['attrs'].keys():
			if k == '__classcell__':
				m['attrs'][k] = meta['attrs'][k]
			else:
				m['attrs'][k] = deepcopy(meta['attrs'][k])

		return m


	def _getModuleObjects(self,module):
		if module in self._objs: 
			return self._objs[module]

	def _getKeysModuleObjects(self,module):
		res = {}
		if module in self._objs: 
			for key in self.objs[module].keys():
				res[key] = list(self._objs[module][key].keys())
			
			return res
		
	def _getFirstModuleObject(self,obj,name):
		if obj in self._moo and name in self._moo[obj] and len(self._moo[obj][name]) > 0: 
			return self._moo[obj][name][0]

	def _getLastModuleObject(self,obj,name):
		if obj in self._moo and name in self._moo[obj] and len(self._moo[obj][name]) > 0: 
			return self._moo[obj][name][-1]

	def _getLastModuleObjectLoaded(self,obj,name):
		modules = self._getModulesOfObjects(obj,name)
		if modules:
			for module in reversed(modules):
				if module in self._momm and model in self._momm[module]: 
					return module

			mom = self._mom[model]
			if len(mom) > 0:
				return mom[-1]


	def _getModulesOfObjects(self,obj,name):
		return self._moo[obj]

	def _setModuleOfObjects(self,obj,name,module):
		self._moo.setdefault(obj,{}).setdefault(name,[]).append(module)

#
	def _create_all_objects(self):
		for module in self._objs.keys():
			for obj in self._objs[module].keys():
				for i in self._objs[module][obj].keys():
					self._objects.setdefault(obj,{})[i] = self._create_object(self._objs[module][obj][i])
				
		if  'models' in self._objects:
			self._load_schema(self._objects['models'])
		
		return self._objects
#
	def _create_loaded_objects(self,session):
		for module in self._objs.keys():
			for obj in self._objs[module].keys():
				for nm in self._objs[module][obj].keys():
					self._objects.setdefault(obj,{})[nm] = self._create_module_object(obj,nm,module)
					self._objects[obj][nm]._session = session

		if  'models' in self._objects:
			self._load_schema(self._objects['models'])
		
		return self._objects


	def _set_session(self,session):
		for obj in self._objects.keys():
			for nm in self._objects[obj].keys():
				self._objects[obj][nm]._session = session

#
	def _create_module_objects(self,module):
		
		r = {}
		for obj in self._objs[module].keys():
			for nm in self._objs[module][obj].keys():
				r.setdefault(obj,{})[nm] = self._create_module_object(obj,nm,module)
		
		return r
