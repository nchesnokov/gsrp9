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

import gsrp5service.orm.report
from gsrp5service.orm.report import Report,ReportInherit

import gsrp5service.orm.dialog
from gsrp5service.orm.dialog import Dialog,DialogInherit

import gsrp5service.orm.wizard
from gsrp5service.orm.wizard import Wizard,WizardInherit

import gsrp5service.orm.query
from gsrp5service.orm.query import Query,QueryInherit

from serviceloader.tools.common import Service, configManagerFixed

from configparser import ConfigParser

class Exception_Registry(Exception): pass

class Registry(Service):

	_module_paths = {}
	_modules = {}
	
	_mom = {}
	_momm = {}
	_omomm = {}

	_rom = {}
	_romm = {}
	_oromm = {}

	_dom = {}
	_domm = {}
	_odomm = {}

	_wom = {}
	_womm = {}
	_owomm = {}

	_qom = {}
	_qomm = {}
	_oqomm = {}

	
	_graph = None
	_pwd = None
	_depends = None
	_dependsinstall = None
	_dependsremove = None
	_packages = []

	_models = {}
	_inherits = {}
	_inherit = {}

	_reports = {}
	_inheritsReport = {}
	_inheritReport = {}

	_dialogs = {}
	_inheritsDialog = {}
	_inheritDialog = {}

	_wizards = {}
	_inheritsWizard = {}
	_inheritWizard = {}

	_queries = {}
	_inheritsQuery = {}
	_inheritQuery = {}

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
		#self._load_modules()
		#self._load_inheritables()

	def _reload(self):
		self._modules = {}
		self._models = {}
		self._reports = {}
		self._dialogs = {}
		self._wizards = {}
		self._queries = {}
		self._mom = {}
		self._rom = {}
		self._dom = {}
		self._wom = {}
		self._wom = {}
		self._momm = {}
		self._romm = {}
		self._domm = {}
		self._womm = {}
		self._qomm = {}
		self._omomm = {}
		self._oromm = {}
		self._odomm = {}
		self._owomm = {}
		self._owomm = {}
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

	def _reload_modules_info(self):
		self._load_modules_info()
		
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
		modules = filter(lambda x: self._modules[x]['state'] == 'I',[node.name for node in self._graph])
		
		for module in modules:
			self._load_module(module)

	def _load_modules(self):
		modules = [node.name for node in self._graph]
		
		for module in modules:
			self._load_module(module)
		
	def _load_module(self,module):
		if not 'loaded' in self._modules[module] or not self._modules[module]['loaded']:
			load_module(self._modules[module]['import'],self._fromlist(module))
			metaModel = gsrp5service.orm.model.MetaModel.__modules__
			metaReport = gsrp5service.orm.report.MetaReport.__modules__
			metaDialog = gsrp5service.orm.dialog.MetaDialog.__modules__
			metaWizard = gsrp5service.orm.wizard.MetaWizard.__modules__
			metaQuery = gsrp5service.orm.query.MetaQuery.__modules__

			self._modules[module]['class'] = []
			self._modules[module]['lom'] = []

			self._modules[module]['report'] = []
			self._modules[module]['lor'] = []

			self._modules[module]['dialog'] = []
			self._modules[module]['lod'] = []

			self._modules[module]['wizard'] = []
			self._modules[module]['low'] = []

			self._modules[module]['query'] = []
			self._modules[module]['loq'] = []

			if self._modules[module]['import'] in metaModel:
				self._modules[module]['class'] =  metaModel[self._modules[module]['import']]
				self._modules[module]['lom'] = list(metaModel[self._modules[module]['import']].keys())

			if self._modules[module]['import'] in metaReport:
				self._modules[module]['report'] =  metaReport[self._modules[module]['import']]
				self._modules[module]['lor'] = list(metaReport[self._modules[module]['import']].keys())

			if self._modules[module]['import'] in metaDialog:
				self._modules[module]['dialog'] =  metaDialog[self._modules[module]['import']]
				self._modules[module]['lod'] = list(metaDialog[self._modules[module]['import']].keys())

			if self._modules[module]['import'] in metaWizard:
				self._modules[module]['wizard'] =  metaWizard[self._modules[module]['import']]
				self._modules[module]['low'] = list(metaWizard[self._modules[module]['import']].keys())

			if self._modules[module]['import'] in metaQuery:
				self._modules[module]['query'] =  metaQuery[self._modules[module]['import']]
				self._modules[module]['loq'] = list(metaQuery[self._modules[module]['import']].keys())
					
			self._modules[module]['loaded'] = True
			
			for model in self._modules[module]['lom']:
				self._models[model] = self._copyMeta(self._modules[module]['class'][model])
				meta = self._models[model]
				self._setModuleOfModel(model,module)
				if '_inherits' in meta['attrs'] and meta['attrs']['_inherits'] and len(meta['attrs']['_inherits']) > 0:
					inherits = meta['attrs']['_inherits']
					for key in inherits.keys():
						self._inherits.setdefault(module,{}).setdefault(model,{})[key] = inherits[key]
					
				if '_inherit' in meta['attrs'] and meta['attrs']['_inherit'] and len(meta['attrs']['_inherit']) > 0:
					inherit = meta['attrs']['_inherit']
					for key in inherit.keys():
						self._inherit.setdefault(module,{}).setdefault(model,{})[key] = inherit[key]
			
			self._metaModel_with_inherits(module)

			for report in self._modules[module]['lor']:
				self._reports[report] = self._copyMeta(self._modules[module]['report'][report])
				meta = self._reports[report]
				self._setModuleOfReport(report,module)
				if '_inherits' in meta['attrs'] and meta['attrs']['_inherits'] and len(meta['attrs']['_inherits']) > 0:
					inherits = meta['attrs']['_inherits']
					for key in inherits.keys():
						self._inherits.setdefault(module,{}).setdefault(report,{})[key] = inherits[key]
					
				if '_inherit' in meta['attrs'] and meta['attrs']['_inherit'] and len(meta['attrs']['_inherit']) > 0:
					inherit = meta['attrs']['_inherit']
					for key in inherit.keys():
						self._inherit.setdefault(module,{}).setdefault(report,{})[key] = inherit[key]
			
			self._metaReport_with_inherits(module)


	def _load_inheritables(self):
		modules = [node.name for node in self._graph]
			
		for module in modules:
			self._load_inheritable(module)

	def _load_inheritable(self,module):
		if 'state' in self._modules[module] and self._modules[module]['state'] == 'I':
			#self._meta_with_inherits(module)
			self._metaModel_with_inherit(module)
			self._metaReport_with_inherit(module)
			self._metaDialog_with_inherit(module)
			self._metaWizard_with_inherit(module)
			self._metaQuery_with_inherit(module)

	
	def _create_module_model(self,model,module):
		#print('_create_module_model:'.upper(),model,module)
		meta = self._modules[module]['class'][model]
		cls = type(meta['name'],meta['bases'],meta['attrs'])
		type.__init__(cls, meta['name'],meta['bases'],meta['attrs'])
		obj = cls()
		obj.__init__()				
		return obj

	def _create_module_report(self,report,module):
		#print('_create_module_model:'.upper(),model,module)
		meta = self._modules[module]['class'][report]
		cls = type(meta['name'],meta['bases'],meta['attrs'])
		type.__init__(cls, meta['name'],meta['bases'],meta['attrs'])
		obj = cls()
		obj.__init__()				
		return obj

	def _create_module_dialog(self,dialog,module):
		#print('_create_module_model:'.upper(),model,module)
		meta = self._modules[module]['dialog'][dialog]
		cls = type(meta['name'],meta['bases'],meta['attrs'])
		type.__init__(cls, meta['name'],meta['bases'],meta['attrs'])
		obj = cls()
		obj.__init__()				
		return obj

	def _create_module_wizard(self,wizard,module):
		#print('_create_module_model:'.upper(),model,module)
		meta = self._modules[module]['wizard'][wizard]
		cls = type(meta['name'],meta['bases'],meta['attrs'])
		type.__init__(cls, meta['name'],meta['bases'],meta['attrs'])
		obj = cls()
		obj.__init__()				
		return obj

	def _create_module_query(self,query,module):
		#print('_create_module_model:'.upper(),model,module)
		meta = self._modules[module]['query'][query]
		cls = type(meta['name'],meta['bases'],meta['attrs'])
		type.__init__(cls, meta['name'],meta['bases'],meta['attrs'])
		obj = cls()
		obj.__init__()				
		return obj

	def _create_first_module_model(self,model):
		meta = self._modules[self._getFirstModuleModel(model)]['class'][model]
		cls = type(meta['name'],meta['bases'],meta['attrs'])
		type.__init__(cls, meta['name'],meta['bases'],meta['attrs'])
		obj = cls()
		obj.__init__()				
		return obj

	def _create_first_module_report(self,report):
		meta = self._modules[self._getFirstModuleReport(report)]['report'][report]
		cls = type(meta['name'],meta['bases'],meta['attrs'])
		type.__init__(cls, meta['name'],meta['bases'],meta['attrs'])
		obj = cls()
		obj.__init__()				
		return obj

	def _create_first_module_dialog(self,dialog):
		meta = self._modules[self._getFirstModuleDialog(dialog)]['dialog'][dialog]
		cls = type(meta['name'],meta['bases'],meta['attrs'])
		type.__init__(cls, meta['name'],meta['bases'],meta['attrs'])
		obj = cls()
		obj.__init__()				
		return obj

	def _create_first_module_wizard(self,wizard):
		meta = self._modules[self._getFirstModuleWizard(wizard)]['wizard'][wizard]
		cls = type(meta['name'],meta['bases'],meta['attrs'])
		type.__init__(cls, meta['name'],meta['bases'],meta['attrs'])
		obj = cls()
		obj.__init__()				
		return obj

	def _create_first_module_query(self,query):
		meta = self._modules[self._getFirstModuleQuery(query)]['query'][query]
		cls = type(meta['name'],meta['bases'],meta['attrs'])
		type.__init__(cls, meta['name'],meta['bases'],meta['attrs'])
		obj = cls()
		obj.__init__()				
		return obj

	def _create_model(self,model):
		meta = self._models[model]
		cls = type(meta['name'],meta['bases'],meta['attrs'])
		type.__init__(cls, meta['name'],meta['bases'],meta['attrs'])
		obj = cls()
		obj.__init__()				
		return obj

	def _create_report(self,report):
		meta = self._reports[report]
		cls = type(meta['name'],meta['bases'],meta['attrs'])
		type.__init__(cls, meta['name'],meta['bases'],meta['attrs'])
		obj = cls()
		obj.__init__()				
		return obj

	def _create_dialog(self,dialog):
		meta = self._dialogs[dialog]
		cls = type(meta['name'],meta['bases'],meta['attrs'])
		type.__init__(cls, meta['name'],meta['bases'],meta['attrs'])
		obj = cls()
		obj.__init__()				
		return obj

	def _create_wizard(self,wizard):
		meta = self._wizards[wizard]
		cls = type(meta['name'],meta['bases'],meta['attrs'])
		type.__init__(cls, meta['name'],meta['bases'],meta['attrs'])
		obj = cls()
		obj.__init__()				
		return obj

	def _create_query(self,query):
		meta = self._queries[query]
		cls = type(meta['name'],meta['bases'],meta['attrs'])
		type.__init__(cls, meta['name'],meta['bases'],meta['attrs'])
		obj = cls()
		obj.__init__()				
		return obj
#
	def _metaModel_with_inherits(self,module):
		if module in self._inherits:
			inherits = self._inherits[module]
			for dst in inherits.keys():
				meta = self._models[dst]
				for src in inherits[dst].keys():
					imeta = self._models[src]
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
			self._models[dst] = meta
#
	def _metaReport_with_inherits(self,module):
		if module in self._inheritsReport:
			inherits = self._inheritsReport[module]
			for dst in inherits.keys():
				meta = self._reports[dst]
				for src in inherits[dst].keys():
					imeta = self._reports[src]
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
			self._reports[dst] = meta
#
	def _metaDialog_with_inherits(self,module):
		if module in self._inheritsDialog:
			inherits = self._inheritsDialog[module]
			for dst in inherits.keys():
				meta = self._dialogs[dst]
				for src in inherits[dst].keys():
					imeta = self._dialogs[src]
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
			self._dialogs[dst] = meta
#
	def _metaWizard_with_inherits(self,module):
		if module in self._inheritsWizard:
			inherits = self._inheritsWizard[module]
			for dst in inherits.keys():
				meta = self._wizards[dst]
				for src in inherits[dst].keys():
					imeta = self._wizards[src]
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
			self._wizards[dst] = meta
#
	def _metaQuery_with_inherits(self,module):
		if module in self._inheritsQuery:
			inherits = self._inheritsQuery[module]
			for dst in inheritsQuery.keys():
				meta = self._queriesQury[dst]
				for src in inheritsQuery[dst].keys():
					imeta = self._queries[src]
					inherit = inheritsQuery[dst][src]
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
			self._queries[dst] = meta
#		
	def _metaModel_with_inherit(self,module):
		if module in self._inherit:
			inherits = self._inherit[module]
			for src in inherits.keys():
				imeta = self._models[src]
				for dst in inherits[src].keys():
					meta = self._models[dst]
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
										Exception_Registry("Column: %s of model: %s if exists\n" % (column,key))
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
			
			self._models[dst] = meta
#
	def _metaReport_with_inherit(self,module):
		if module in self._inheritReport:
			inherits = self._inheritReport[module]
			for src in inherits.keys():
				imeta = self._reports[src]
				for dst in inherits[src].keys():
					meta = self._reports[dst]
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
										Exception_Registry("Column: %s of model: %s if exists\n" % (column,key))
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
			
			self._reports[dst] = meta
#
	def _metaDialog_with_inherit(self,module):
		if module in self._inheritDialog:
			inherits = self._inheritDialog[module]
			for src in inherits.keys():
				imeta = self._dialogs[src]
				for dst in inherits[src].keys():
					meta = self._dialogs[dst]
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
										Exception_Registry("Column: %s of model: %s if exists\n" % (column,key))
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
			
			self._dialogs[dst] = meta
#	
	def _metaWizard_with_inherit(self,module):
		if module in self._inheritWizard:
			inherits = self._inheritWizard[module]
			for src in inherits.keys():
				imeta = self._wizards[src]
				for dst in inherits[src].keys():
					meta = self._wizards[dst]
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
										Exception_Registry("Column: %s of model: %s if exists\n" % (column,key))
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
			
			self._wizards[dst] = meta
#
	def _metaQuery_with_inherit(self,module):
		if module in self._inheritQuery:
			inherits = self._inheritQuery[module]
			for src in inherits.keys():
				imeta = self._queries[src]
				for dst in inherits[src].keys():
					meta = self._queries[dst]
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
										Exception_Registry("Column: %s of model: %s if exists\n" % (column,key))
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
			
			self._queries[dst] = meta
#	
	def _load_schema(self,models):
		root_models = []
		for key in models.keys():
			if isinstance(models[key],ModelInherit):
				continue
			model = models[key]
			m2ofields = model._m2orelatedfields
			o2mfields = model._o2mfields

			ci = model.columnsInfo(m2ofields + o2mfields,['obj','rel'])
			childs_name = model._getChildsIdName()
			parent_name = model._getParentIdName()

			m2oremove = []
			o2mremove = [] 
			
			if childs_name and childs_name in o2mfields and ci[childs_name]['obj'] == model._name:
				o2mfields.remove(childs_name)
			
			if parent_name and parent_name in m2ofields and ci[parent_name]['obj'] == model._name:
				m2ofields.remove(parent_name)
			
			for m2ofield in m2ofields:
				obj = ci[m2ofield]['obj']
				rel = m2ofield
				mobj = models[obj]
				if len(mobj._o2mfields) > 0:
					cim = mobj.columnsInfo(mobj._o2mfields,['obj','rel'])
					if len(list(filter(lambda x: cim[x]['obj'] == model._name and cim[x]['rel'] == rel,cim.keys()))) == 0:
						m2oremove.append(m2ofield)

			for o2mfield in o2mfields:
				obj = ci[o2mfield]['obj']
				rel = ci[o2mfield]['rel']
				mobj = models[obj]
				if rel in mobj._columns:
					cim = mobj.columnsInfo([rel],['obj'])
					if rel not in cim or cim[rel]['obj'] != model._name:
						o2mremove.append(o2mfield)
				else:
					pass
					#print('NOT MAPPED O2MFIELD:',model._name,o2mfield,obj,rel)


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
		
			model._schema = [parents,childs]
			
			if len(model._schema[0]) == 0 and len(model._schema[1]) > 0:
				root_models.append(key)
			#if key[:9] == 'purchase.':
				#print('MODEL:',model._name,model._schema)
		
		return models

	def _reload_modules(self,modules):
		for module in filter(lambda x: x in modules,[node.name for node in self._graph]):
			self._download_module(module)
			self._load_module(module)

	def _download_module(self,module):
		for model in self._modules[module]['lom']:
			if model in self._models:
				del self._models[model]

		for report in self._modules[module]['lor']:
			if report in self._reports:
				del self._reports[report]

		for dialog in self._modules[module]['lod']:
			if dialog in self._dialogs:
				del self._dialogs[dialog]

		for wizard in self._modules[module]['low']:
			if wizard in self._wizards:
				del self._wizards[wizard]

		for query in self._modules[module]['loq']:
			if query in self._queries:
				del self._queries[query]

		if 'loaded' in self._modules[module] or self._modules[module]['loaded']:
			self._modules[module]['loaded'] = False
#
	def _getMetaOfModulesModel(self,model,module):
		if module in self._momm and model in self._momm[module]: 
			return self._momm[module][model]

	def _setMetaOfModulesModel(self,model,module,meta):
		if module not in self._momm or model not in self._momm[module]:
			self._momm.setdefault(module,{})[model] = meta
			self._setModuleOfModel(model,module)

	def _getMetaOfOnlyModulesModel(self,model,module):
		if module in self._omomm and model in self._omomm[module]: 
			return self._omomm[module][model]

		return self._getMetaOfModulesModel(model,self._getFirstModule(model))
		
	def _setMetaOfOnlyModulesModel(self,model,module,meta):
		if module not in self._omomm or model not in self._omomm[module]:
			self._omomm.setdefault(module,{})[model] = meta
#
	def _getMetaOfModulesReport(self,report,module):
		if module in self._romm and report in self._romm[module]: 
			return self._romm[module][report]

	def _setMetaOfModulesReport(self,report,module,meta):
		if module not in self._romm or report not in self._romm[module]:
			self._romm.setdefault(module,{})[report] = meta
			self._setModuleOfReport(report,module)

	def _getMetaOfOnlyModulesReport(self,report,module):
		if module in self._oromm and report in self._oromm[module]: 
			return self._oromm[module][report]

		return self._getMetaOfModulesReport(report,self._getFirstModuleReport(report))
		
	def _setMetaOfOnlyModulesReport(self,report,module,meta):
		if module not in self._oromm or report not in self._oromm[module]:
			self._oromm.setdefault(module,{})[report] = meta
#
	def _getMetaOfModulesDialog(self,dialog,module):
		if module in self._domm and dialog in self._domm[module]: 
			return self._domm[module][dialog]

	def _setMetaOfModulesDialog(self,dialog,module,meta):
		if module not in self._domm or dialog not in self._domm[module]:
			self._domm.setdefault(module,{})[dialog] = meta
			self._setModuleOfDialog(dialog,module)

	def _getMetaOfOnlyModulesDialog(self,dialog,module):
		if module in self._odomm and dialog in self._odomm[module]: 
			return self._odomm[module][dialog]

		return self._getMetaOfModulesDialog(dialog,self._getFirstModuleDialog(dialog))
		
	def _setMetaOfOnlyModulesDialog(self,dialog,module,meta):
		if module not in self._odomm or dialog not in self._odomm[module]:
			self._odomm.setdefault(module,{})[dialog] = meta
#
	def _getMetaOfModulesWizard(self,wizard,module):
		if module in self._womm and wizard in self._womm[module]: 
			return self._womm[module][wizard]

	def _setMetaOfModulesWizard(self,wizard,module,meta):
		if module not in self._womm or wizard not in self._womm[module]:
			self._womm.setdefault(module,{})[wizard] = meta
			self._setModuleOfWizard(wizard,module)

	def _getMetaOfOnlyModulesWizard(self,wizard,module):
		if module in self._owomm and wizard in self._owomm[module]: 
			return self._owomm[module][wizard]

		return self._getMetaOfModulesWizard(wizard,self._getFirstModuleWizard(wizard))
		
	def _setMetaOfOnlyModulesWizard(self,wizard,module,meta):
		if module not in self._owomm or wizard not in self._owomm[module]:
			self._owomm.setdefault(module,{})[wizard] = meta
#
	def _getMetaOfModulesQuery(self,query,module):
		if module in self._qomm and query in self._qomm[module]: 
			return self._qomm[module][query]

	def _setMetaOfModulesQuery(self,query,module,meta):
		if module not in self._qomm or query not in self._qomm[module]:
			self._qomm.setdefault(module,{})[query] = meta
			self._setModuleOfQuery(query,module)

	def _getMetaOfOnlyModulesQuery(self,query,module):
		if module in self._oqomm and query in self._oqomm[module]: 
			return self._oqomm[module][query]

		return self._getMetaOfModulesQuery(query,self._getFirstModuleQuery(query))
		
	def _setMetaOfOnlyModulesquery(self,query,module,meta):
		if module not in self._oqomm or query not in self._oqomm[module]:
			self._oqomm.setdefault(module,{})[query] = meta
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


	def _getModuleModels(self,module):
		if module in self._momm: 
			return self._momm[module]

	def _getKeysModuleModels(self,module):
		if module in self._momm: 
			return list(self._momm[module].keys())


	def _getModels(self):
		return self._momm
		
	def _getFirstModuleModel(self,model):
		mom = self._mom[model]
		if len(mom) > 0:
			return mom[0]

	def _getLastModuleModel(self,model):
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

#
	def _create_all_models(self):
		r = {}
		for model in self._models.keys():
			if Model in self._models[model]['bases']:
				r[model] = self._create_model(model)
				
		r = self._load_schema(r)
		
		return r

	def _create_all_reports(self):
		r = {}
		for report in self._reports.keys():
			if Report in self._reports[report]['bases']:
				r[report] = self._create_report(report)
				
		return r

	def _create_all_dialogs(self):
		r = {}
		for dialog in self._dialogs.keys():
			if Dialog in self._dialogs[dialog]['bases']:
				r[dialog] = self._create_dialog(dialog)
				
		return r

	def _create_all_wizards(self):
		r = {}
		for wizard in self._wizards.keys():
			if Wizard in self._wizards[wizard]['bases']:
				r[wizard] = self._create_=wizard(wizard)
				
		return r

	def _create_all_queries(self):
		r = {}
		for query in self._queries.keys():
			if Query in self._queries[query]['bases']:
				r[query] = self._create_query(query)
		
		return r

#
	def _create_loaded_models(self):
		r = {}
		for model in self._models.keys():
			if Model in self._models[model]['bases']:
				r[model] = self._create_model(model)
				
		r = self._load_schema(r)
		
		return r

	def _create_loaded_reports(self):
		r = {}
		for report in self._reports.keys():
			if Report in self._reports[report]['bases']:
				r[report] = self._create_report(report)
	
		return r

	def _create_loaded_dialogs(self):
		r = {}
		for dialog in self._dialogs.keys():
			if Dialog in self._dialogs[dialog]['bases']:
				r[dialog] = self._create_dialog(dialog)

		return r

	def _create_loaded_wizards(self):
		r = {}
		for wizard in self._wizards.keys():
			if Wizard in self._wizards[wizard]['bases']:
				r[wizard] = self._create_wizard(wizard)
				
		return r

	def _create_loaded_queries(self):
		r = {}
		for query in self._queries.keys():
			if Query in self._queries[query]['bases']:
				r[query] = self._create_query(query)
				
		return r
#
	def _create_module_models(self,module):
		
		r = {}
		for model in self._modules[module]['lom']:
			r[model] = self._create_module_model(model,module)
		
		return r

	def _create_module_reports(self,module):
		
		r = {}
		for report in self._modules[module]['lor']:
			r[report] = self._create_module_report(report,module)
		
		return r

	def _create_module_dialogs(self,module):
		
		r = {}
		for dialog in self._modules[module]['lod']:
			r[dialog] = self._create_module_dialog(dialog,module)
		
		return r

	def _create_module_wizards(self,module):
		
		r = {}
		for wizard in self._modules[module]['low']:
			r[wizard] = self._create_module_wizard(wizard,module)
		
		return r

	def _create_module_queries(self,module):
		
		r = {}
		for query in self._modules[module]['loq']:
			r[query] = self._create_module_query(query,module)
		
		return r
