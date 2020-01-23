# --*-- coding: utf-8 --*--	
import sys
import os
from copy import deepcopy
from functools import reduce
from os.path import join as opj
from .loading import *
from .depmod import Graph,Node,DependsInstall,DependsRemove

import gsrp5service.orm.model
from gsrp5service.orm.model import Model,ModelInherit
from gsrp5service.orm.mm import _getRecNameName,_getChildsIdName

from serviceloader.tools.common import Service, configManagerFixed

from configparser import ConfigParser

class Exception_Registry(Exception): pass

def _list_to_dict(s,p):
	res = {}
	prev = None
	for k in s:
		if type(k) == str:
			res[k] = p
			prev = k
		elif type(k) in (list,tuple):
			l = _list_to_dict(k,prev)
			for k in l.keys():
				res[k] = l[k]
	
	return res

def _schema_to_dict(s,prev=None):
	res = {}
	if type(s) == str:
		res[s] = prev
	elif type(s) in (list,tuple):
		for k in s:
			if type(k) == str:
				res[k] = prev
				prev = k
			elif type(k) in (list,tuple):
				l = _list_to_dict(k,prev)
				for k in l.keys():
					res[k] = l[k]
			
	return res

def _schema_to_levels(s,l=0):
	res = {}

	if type(s) == str:
		res.setdefault(l,[]).append(s)
	elif type(s) in (list,tuple):
		for k in s:
			if type(k) == str:
				res.setdefault(l,[]).append(k)
			elif type(k) in (list,tuple):
				r = _schema_to_levels(k,l+1)
				for key in r.keys():
					if key == l+1:
						res.setdefault(l+1,[]).extend(r[key])
					else:
						res[key] = r[key]

	return res

def _build_schema(pool,model):
	res = [model]
	m = pool.get(model)
	#print('_build_schema:'.upper(),model,m)
	if isinstance(m,ModelInherit):
		return res
	o2mfields = m._o2mfields
	for o2mfield in o2mfields:
		if o2mfield ==  _getChildsIdName(m):
			continue
		obj = pool.get(model).columnsInfo([o2mfield],['obj'])[o2mfield]['obj']
		r = _build_schema(pool,obj)
		if len(r) > 0:
			res.append(r)
	
	if model in ('purchase.orders','purchase.order.categories'):
		print('RESULT:',model,res)
	return res

def _to_list(keys):
	res = []
	for key in keys:
		if type(key) == str:
			res.append(key)
		elif type(key) in (list,tuple):
			res.extend(_to_list(key))
	
	return res

def _get_level(name,levels):
	for i,k in enumerate(levels.keys()):
		if name in levels[k]:
			return i
	
	return None

class Registry(Service):

	_module_paths = {}
	_modules = {}
	_mom = {}
	_momm = {}
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

		
		for key in self._module_paths.keys():
			self._module_paths[key] = filter(lambda x: os.path.isdir(opj(x)), os.listdir(opj(os.path.dirname(os.path.abspath(__file__)),key)))

		self._graph = Graph()
		self._load_modules_info()
		self._load_modules()

	def _reload(self):
		self._modules = {}
		self._models = {}
		_self.mom = {}
		self._graph = Graph()
		self._pwd = os.path.dirname(os.path.abspath(__file__))
		self._depends = None
		self._dependsinstall = None
		self._dependsremove = None
		self._packages = []
		self._modules.clear()
		self._reload_modules_info()
		self._load_modules()
	
	def _load_module_info(self,path):
		return load_module_info(path)

	def _reload_modules_info(self):
		self._load_modules_info()
		
	def _load_modules_info(self):
		for d in list(self._module_paths.keys()):
			mdir = opj(os.path.dirname(os.path.abspath(__file__)),d)
			self._module_paths[d] = list(filter(lambda x: os.path.isdir(opj(mdir,x)), os.listdir(mdir)))

			if self._pwd not in sys.path:
				sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))

		for path in list(self._module_paths.keys()):
			for name in self._module_paths[path]:
				if os.path.isdir(opj(self._pwd, path, name)) and os.path.exists(opj(self._pwd, path, name, '__manifest__.info')) and os.path.isfile(opj(self._pwd, path, name, '__manifest__.info')):
					info = self._load_module_info(opj(self._pwd, path, name))
					if not info['able'] in self._able:
						continue
					self._modules[name] = {'meta':info,'path':opj(self._pwd,path),'lom':{},'mom':{},'import':path + '.' + name,'_module':name}
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

	def _load_modules(self):
		modules = [node.name for node in self._graph]
		
		for module in modules:
			self._load_module(module)


	def _load_module(self,module):
		if not 'loaded' in self._modules[module] or not self._modules[module]['loaded']:
			load_module(self._modules[module]['import'],self._fromlist(module))
			meta = gsrp5service.orm.model.MetaModel.__modules__

			self._modules[module]['class'] = []
			self._modules[module]['lom'] = []

			if self._modules[module]['import'] in meta:
				self._modules[module]['class'] =  meta[self._modules[module]['import']]
				self._modules[module]['lom'] = list(meta[self._modules[module]['import']].keys())
					
			self._modules[module]['loaded'] = True
			
			for model in self._modules[module]['lom']:
				meta = self._modules[module]['class'][model]
				self._setMetaOfModulesModel(model,module,meta)
				if '_inherits' in meta['attrs'] and meta['attrs']['_inherits'] and len(meta['attrs']['_inherits']) > 0:
					self._meta_with_inherits(model,module)

	def _load_inherits(self):
		modules = [node.name for node in self._graph]
		r = {}
		for module in modules:
			if 'state' in self._modules[module] and self._modules[module]['state'] == 'I':
				self._load_inherit(module)

		for module in self._momm.keys():
			for model in self._momm[module].keys():
				r[model] = self._create_model(model,module)

		self._load_schema(r)
		
		return r

	
	def _load_inherit(self,module):
		for model in self._modules[module]['lom']:
			meta = self._modules[module]['class'][model]
			if '_inherit' in meta['attrs'] and meta['attrs']['_inherit'] and len(meta['attrs']['_inherit']) > 0:

				self._meta_with_inherit(model,module)
	
	def _create_model(self,model,module):
		meta = self._getMetaOfModulesModel(model,module)
		cls = type(meta['name'],meta['bases'],meta['attrs'])
		type.__init__(cls, meta['name'],meta['bases'],meta['attrs'])
		obj = cls()
		obj.__init__()				
		return obj

	def _meta_with_inherits(self,model,module):
		meta = self._getMetaOfModulesModel(model,module)
		for key in meta['attrs']['_inherits'].keys():
			inherit = meta['attrs']['_inherits'][key]
			imodule= self._getFirstModule(key)
			imeta = self._getMetaOfModulesModel(key,imodule)
			if type(inherit) == dict:
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
			elif type(inherit) in (list,tuple):
				for i in inherit:
					meta['attrs'][i] = imeta['attrs'][i]

		self._setMetaOfModulesModel(model,module,meta)
		
		return meta
	
	def _meta_with_inherit(self,model,module):
		imeta = self._getMetaOfModulesModel(model,module)
		if '_inherits' in imeta['attrs']:
			imeta = self._meta_with_inherits(model,module)
		for key in imeta['attrs']['_inherit'].keys():
			#if self._getFirstModule(key) != module:
			inherit = imeta['attrs']['_inherit'][key]
			meta=self._getMetaOfModulesModel(key,self._getLastModuleLoaded(key))
			imeta1 = self._copyMeta(meta)			
			for c in inherit.keys():
				if c == '_methods':
					for method in inherit[c]:
						imeta1['attrs'][method] = imeta['attrs'][c][method]
				elif c == '_columns':
					for column in inherit[c]:
						if c not in imeta1['attrs'] or column not in imeta1['attrs'][c]:
							imeta1['attrs'].setdefault(c,{})[column] = imeta['attrs'][c][column]
						else:
							if imeta['attrs'][c][column]._type == 'iSelection':
								imeta1['attrs'][c][column].selections.extend(imeta['attrs'][c][column].selections)
							else:
								Exception_Registry("Column: %s of model: %s if exists\n" % (column,key))
				elif c == '_actions':
					for action in inherit[c]:
						imeta1['attrs'].setdefault(c,{})[action] = imeta['attrs']['_actions'][action]
				elif c == '_states':
					for state in inherit[c]:
						imeta1['attrs'].setdefault(c,{})[state] = imeta['attrs'][c][state]
				elif c == '_trigers':
					for triger in inherit[c]:
						imeta1['attrs'].setdefault(c,{})[triger] = imeta['attrs'][c][triger]
				elif c == '_default':
					for dkey in inherit[c]:
						imeta1['attrs'].setdefault(c,{})[dkey] = imeta['attrs'][c][dkey]
				elif c == '_constraints':
					imeta1['attrs'].setdefault(c,[]).extend(imeta['attrs'][c])
				elif c == '_sql_constraints':
					imeta1['attrs'].setdefault(c,[]).extend(imeta['attrs'][c])
				elif c == '_auth':
					imeta1['attrs'].setdefault(c,[]).extend(imeta['attrs'][c])

			self._setMetaOfModulesModel(key,module,imeta1)
		
	def _load_schema(self,models):
		m = set()
		for key in models.keys():
			if key in m or isinstance(models[key],Model) and _getRecNameName(models[key]) is None or isinstance(models[key],ModelInherit):
				continue
			name = models[key]._name
			schema = _build_schema(models,name)
			sc = set(_to_list(schema))
			dc = _schema_to_dict(schema)
			dl = _schema_to_levels(schema)
			for s in sc:
				model = models.get(s)
				#model._schema = dc
				model._schema.update(dc)
				#model._levels = dl
				model._levels.update(dl)
				model._level = _get_level(model._name,model._levels)
			
			m.union(sc)
		
		return models

	def _load_schema1(self,models):
		for key in models.keys():
			if isinstance(models[key],ModelInherit):
				continue
			m2ofields = model._m2ofields
			o2mfields = model._o2mfields
			m2oremove = []
			o2mremove = [] 
			ci = model.columnsInfo(m2ofields + o2mfields,['obj','rel'])

			for m2ofield in m2ofields:
				obj = ci[m2ofield]['obj']
				rel = m2ofield
				cim = models[obj].columnsInfo([m2ofield],['obj','rel'])
				if len(list(filter(lambda x: cim[x]['obj'] == obj and cim[x]['rel'] == rel,cim.keys()))) == 0:
					m2oremove.append(m2ofields)

			for o2mfield in o2mfields:
				obj = ci[o2mfield]['obj']
				rel = ci[o2mfield]['rel']
				cim = models[obj].columnsInfo([rel],['obj'])
				
				if rel not in cim or cim[rel]['obj'] != obj:
					m2oremove.append(m2ofields)


			for f in m2oremove:
				m2ofields.remove(f)

			for f in o2mremove:
				o2mfields.remove(f)
			parents = {}
			childs = {}

			for m2ofield in m2ofields:
				parents[m2ofield] = ci[m2ofield]['obj']

			for o2mfield in o2mfields:
				childs[o2mfield] = ci[o2mfield]['obj']
		
			model._schema1 = (parents,childs)

	def _reload_modules(self,modules):
		for module in filter(lambda x: x in modules,[node.name for node in self._graph]):
			self._download_module(module)
			self._load_module(module)

	def _download_module(self,module):
		if module in self._momm:
			del self._momm[module]

		if 'loaded' in self._modules[module] or self._modules[module]['loaded']:
			self._modules[module]['loaded'] = False

	def _getMetaOfModulesModel(self,model,module):
		if module in self._momm and model in self._momm[module]: 
			return self._momm[module][model]

	def _setMetaOfModulesModel(self,model,module,meta):
		if module not in self._momm or model not in self._momm[module]:
			self._momm.setdefault(module,{})[model] = meta
			self._setModuleOfModel(model,module)

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


	def _getModuleModels(self,module):
		if module in self._momm: 
			return self._momm[module]

	def _getKeysModuleModels(self,module):
		if module in self._momm: 
			return list(self._momm[module].keys())


	def _getModels(self):
		return self._momm
		
	def _getFirstModule(self,model):
		mom = self._mom[model]
		if len(mom) > 0:
			return mom[0]

	def _getLastModule(self,model):
		mom = self._mom[model]
		if len(mom) > 0:
			return mom[-1]

	def _getLastModuleLoaded(self,model):
		for module in reversed(self._mom[model]):
			if module in self._momm and model in self._momm[module]: 
				return module

		mom = self._mom[model]
		if len(mom) > 0:
			return mom[-1]


	def _getModulesOfModel(self,model):
		return self._mom[model]

	def _setModuleOfModel(self,model,module):
		if model not in self._mom:
			self._mom.setdefault(model,[]).append(module)
		else:
			if module not in self._mom[model]:
				self._mom[model].append(module)

	def _createAllModels(self):
		r = {}
		for module in self._momm.keys():
			for model in self._momm[module].keys():
				r[model] = self._create_model(model,module)
				
		r = self._load_schema(r)
		self._load_schema1(r)
		for k in r.keys():
			if k[:9] == 'purchase.':
				print('SCHEMA-1:',k, r[k]._schema1)
		self._models = r
		
		return r

	def _createInstalledModels(self):
		r = {}
		for module in self._momm.keys():
			models = self._momm[module].keys()
			for model in models:
				m = self._create_model(model,module)
				if m:
					r[model] = m 
		
		return r

	def _createModuleModels(self,module):
		r = {}
		for model in self._momm[module].keys():
			r[model] = self._create_model(model,module)
		
		return r
