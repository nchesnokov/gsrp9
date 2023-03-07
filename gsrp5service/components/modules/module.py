import logging
import web_pdb
from passlib.hash import pbkdf2_sha256
from functools import reduce
from datetime import datetime
from lxml import etree
import os
import csv
import yaml
import json
import polib
from yaml import Loader
from os.path import join as opj
import toposort
import copy
from . import genddl
from gsrp5service.orm.model import Model,ModelInherit,Access

__all__ = ['install','uninstall','upgrade','sysinstall','sysupgrade','upgrademoduleslist','load']

_logger = logging.getLogger('listener.' + __name__)

class XMLValidator(Exception): pass

class KeyBuffer(dict):
	
	def add(self,key,obj,recordkey,value):
		self.setdefault(key,{}).setdefault(obj,{})[recordkey] = value

	def key(self,key,obj,recordkey):
		if key in self  and obj in self[key] and recordkey in self[key][obj]:
			return self[key][obj][recordkey]  
		return None

def load(self,modules = None,context = {'lang':'en','tz':'UTC'}):
	return _load(self,['install','autoinstall'],modules, context)

def _load(self,able=None, modules = None, context = {'lang':'en','tz':'UTC'}):
	log = []
	_modules = []
	_chunks = {}
	if able is None or not able:
		able= ['install','autoinstall']


	if modules is None:
		modules = list(filter(lambda x:self._registry._modules[x]['meta']['able'] in able,self._registry._modules.keys()))

	if type(modules) == str:
		module = modules
		if self._registry._modules[modules]['meta']['able'] in able and self._registry._modules[module]['state'] == 'I':
			_modules.append(modules)
			_chunks[modules] = ['module','depends','env','view','cust','example','data','demo','test','i18n']
	elif type(modules) == dict:
		mkeys = list(modules.keys())
		for module in mkeys:
			if module in mkeys and self._registry._modules[module]['meta']['able'] in able and self._registry._modules[module]['state'] == 'I':
				_modules.append(module)
		_chunks = modules
	elif type(modules) in (tuple,list):
		for module in modules:
			if module in modules and self._registry._modules[module]['meta']['able'] in able and self._registry._modules[module]['state'] == 'I':
				_modules.append(module)
				_chunks[module] = ['module','depends','env','view','cust','example','data','demo','test','i18n']
	elif modules is None:
		for module in self._registry._depends:
			if self._registry._modules[module]['meta']['able'] in able and self._registry._modules[module]['state'] == 'I':
				_modules.append(module)
				_chunks[module] = ['module','depends','env','view','cust','example','data','demo','test','i18n']

	if _modules:
		_logger.info('modules-load: %s' % (modules,))
	depends = []
	for _module in _modules:
		if 'module' in _chunks[_module] and 'depends' in _chunks[_module]:
			for dep in self._registry._dependsinstall.install(_module):
				if not dep in depends and self._registry._modules[dep]['meta']['able'] in able and ('state' in self._registry._modules[dep] and self._registry._modules[dep]['state'] in ('I',)):
					depends.append(dep)

		if 'state' in self._registry._modules[_module] and self._registry._modules[_module]['state'] in ('I',):
			depends.append(_module)
	
	if len(depends) == 0:
		log.append('Not modules for loading')
	else:
		self._registry._load_module('bc')
		for depend in depends:
			self._registry._load_module(depend)
			chunk = _chunks[depend]

			metas = {}
			info = self._registry._modules[depend]
		
			if 'env' in chunk and 'env' in info['meta']:
				metas['env'] = info['meta']['env']
			
			if 'view' in chunk and 'view' in info['meta']:
				metas['view'] = info['meta']['view']

			if 'cust' in chunk and 'cust' in info['meta']:
				metas['cust'] = info['meta']['cust']
			
			if 'example' in chunk:
				if 'data' in info['meta']:
					metas['data'] = info['meta']['data']
				if 'demo' in info['meta']:
					metas['demo'] = info['meta']['demo']
			else:
				if 'data' in chunk and 'data' in info['meta']:
					metas['data'] = info['meta']['data']
				if 'demo' in chunk and 'demo' in info['meta']:
					metas['demo'] = info['meta']['demo']
			
			if 'test' in chunk and 'test' in info['meta']:
				metas['test'] = info['meta']['test']
			
			if 'i18n' in chunk and 'i18n' in info['meta']:
				metas['i18n'] = info['meta']['i18n']
				
			self._registry._load_module(depend)
			_loadFiles(self,depend,self._registry._modules[depend],metas,context)
			self._cr.commit()
			#if 'env' in metas:
				#_load_env(self,depend)
			
			self._cr.commit()
			_logger.info("Module: %s loaded:" % (depend,))
			

			log.append([0,'module: <%s> successfull loaded' % (depend,)])

	return log

def _install(self,able=None, modules = None, context = {'lang':'en','tz':'UTC'}):
	log = []
	_modules = []
	_chunks = {}
	if able is None or not able:
		able= ['install']


	if modules is None:
		modules = list(filter(lambda x:self._registry._modules[x]['meta']['able'] in able,self._registry._modules.keys()))

	if type(modules) == str:
		module = modules
		if self._registry._modules[module]['meta']['able'] in able:
			dis = set()
			for di in self._registry._dependsinstall.install(module):
				if self._registry._modules[di]['state'] == 'I':
					continue
				dis.add(di)
			for m in list(dis):
				_modules.append({m:['module','depends','env','view','example','data','demo','test','i18n']})				
			_modules.append(module)
			_chunks[module] = ['module','depends','env','view','example','data','demo','test','i18n']
	elif type(modules) == dict:
		mkeys = list(modules.keys())
		for module in mkeys:
			if module in mkeys and self._registry._modules[module]['meta']['able'] in able:
				dis = set()
				for di in self._registry._dependsinstall.install(module):
					if self._registry._modules[di]['state'] == 'I':
						continue
					dis.add(di)
				for m in list(dis):
					_modules.append({m:['module','depends','env','view','example','data','demo','test','i18n']})				
				_modules.append(module)
		_chunks = modules
	elif type(modules) in (tuple,list):
		for module in modules:
			if module in modules and self._registry._modules[module]['meta']['able'] in able:
				dis = set()
				for di in self._registry._dependsinstall.install(module):
					if self._registry._modules[di]['state'] == 'I':
						continue

					dis.add(di)
				for m in list(dis):
					_chunks[m] = ['module','depends','env','view','example','data','demo','test','i18n']
					_modules.append(m)
				_modules.append(module)
				_chunks[module] = ['module','depends','env','view','example','data','demo','test','i18n']
	elif modules is None:
		for module in self._registry._depends:
			if self._registry._modules[module]['state'] == 'I':
				continue
			if self._registry._modules[module]['meta']['able'] in able:
				_modules.append(module)
				_chunks[module] = ['module','depends','env','view','example','data','demo','test','i18n']

	if _modules:
		_logger.info('modules-install: %s' % (modules,))
	depends = []
	for _module in _modules:
		if 'module' in _chunks[_module] and 'depends' in _chunks[_module]:
			for dep in self._registry._dependsinstall.install(_module):
				if not dep in depends and self._registry._modules[dep]['meta']['able'] in able and ('state' in self._registry._modules[dep] and self._registry._modules[dep]['state'] in ('i','N',None)):
					depends.append(dep)
					_chunks[dep] = ['module','depends','env','view','example','data','demo','test','i18n']

		if 'module' in _chunks[_module] and not 'state' in self._registry._modules[_module] or 'module' in _chunks[_module] and self._registry._modules[_module]['state'] in (None,'N','i') or ('state' in self._registry._modules[_module] and self._registry._modules[_module]['state'] == 'I' and ('module' not in _chunks[_module] or 'nomodule' not in _chunks[_module]) and  ('env' in _chunks[_module] or 'view' in _chunks[_module] or 'example' in _chunks[_module] or 'data' in _chunks[_module] or 'demo' in _chunks[_module] or 'test' in _chunks[_module] or 'i18n' in _chunks[_module])):
			depends.append(_module)
	
	_logger.info('modules-install-with-depends: %s' % (depends,))

	if len(depends) == 0:
		log.append('Not modules for install')
	else:
		for depend in depends:
			self._registry._load_module(depend)
			_installModule(self,depend,_chunks[depend],context)
			log.append([0,'module: <%s> successfull installed' % (depend,)])

	
		# for depend in depends:
			# chunk = _chunks[depend]
			# info = self._registry._modules[depend]
			# metas ={}
			# if 'example' in chunk:
				# if 'data' in info['meta']:
					# metas['data'] = info['meta']['data']
				# if 'demo' in info['meta']:
					# metas['demo'] = info['meta']['demo']
			# else:
				# if 'data' in chunk and 'data' in info['meta']:
					# metas['data'] = info['meta']['data']
				# if 'demo' in chunk and 'demo' in info['meta']:
					# metas['demo'] = info['meta']['demo']

			# _loadFiles(self,depend,self._registry._modules[depend],metas)
			# self._cr.commit()
			# log.append([0,'module: <%s> data successfull loaded' % (depend,)])

		# dep_modules = set()
		# for depend in depends:
			# keys = list(self._registry._metas[depend]['models'].keys())
			# for key in keys:
				# if 'inherit' in self._registry._modules[depend]['class'][key]['attrs'] and ModelInherit in self._registry._modules[depend]['class'][key]['bases']:
					# inherit = self._registry._modules[depend]['class'][key]['attrs']['inherit']
					# for ikey in inherit.keys():
						# m1 = self._registry._getLastModule(key)
						# if m1:
							# dep_modules.add(key)

		# all_modules = list(filter(lambda x:x != 'bc',depends+list(dep_modules)))
	
		# for all_module in filter(lambda x: x in all_modules,[node.name for node in self._registry._graph]):
			
			# log.append([0,'module: <%s> successfull reloaded' % (all_module,)])
	
	return log

def _uninstall(self,able=None, modules = None):

	_modules = []

	if able is None or not able:
		able= ['install']
	
	if type(modules) == str:
		if self._registry._modules[modules]['meta']['able'] in able:
			_modules.append(modules)
	elif type(modules) in (tuple,list):
		for module in reversed(self._registry._depends):
			if module in modules and self._registry._modules[module]['meta']['able'] in able:
				_modules.append(module)
	elif modules is None:
		for module in reversed(self._registry._depends):
			if self._registry._modules[module]['meta']['able'] in able:
				_modules.append(module)

	depends = []
	for _module in _modules:
		for dep in self._registry._dependsremove.remove(_module):
			if not dep in depends and self._registry._modules[dep]['meta']['able'] in able and 'state' in self._registry._modules[dep] and self._registry._modules[dep]['state'] in ('I ','r'):
				depends.append(dep)
		if 'state' in self._registry._modules[_module] and self._registry._modules[_module]['state'] in ('I','r'):
			depends.append(_module)
	
	log = []
	if len(depends) == 0:
		log.append('Not modules for uninstall')
	else:
		for depend in depends:
			self._registry._load_module(depend)
			_uninstallModule(self,depend)
	
		dep_modules = set()
		for depend in depends:
	
			keys = list(self._registry._objs[depend]['models'].keys())
			for key in keys:
				if 'inherit' in self._registry._objs[depend]['models'][key]['attrs'] and ModelInherit in self._registry._objs[depend]['models'][key]['bases']:
					inherit = self._registry._objs[depend]['models'][key]['attrs']['inherit']
					for ikey in inherit.keys():
						m1 = self._registry._getLastModuleObject('models',key)
						if m1:
							dep_modules.add(key)
	
		self._registry._download_module(depend)
					
		log.append([0,'module: <%s> successfull uninstalled' % (depend,)])	
	
	return log

def _upgrade(self,able=None, modules = None):
	log = []
	_modules = []
	if able is None or not able:
		able= ['install']
	
	if type(modules) == str:
		if self._registry._modules[modules]['meta']['able'] in able:
			_modules.append(modules)
	elif type(modules) in (tuple,list):
		for module in self._registry._depends:
			if module in modules and self._registry._modules[module]['meta']['able'] in able:
				_modules.append(module)
	elif modules is None:
		for module in self._registry._depends:
			if self._registry._modules[module]['meta']['able'] in able:
				_modules.append(module)

	if modules:
		_logger.info('modules-upgrade: %s' % (modules,))
	depends = []
	for _module in _modules:
		for dep in self._registry._dependsremove.remove(_module):
			if not dep in depends and self._registry._modules[dep]['meta']['able'] in able and ('state' in self._registry._modules[dep] and self._registry._modules[dep]['state'] in ('I','u',None)):
				depends.append(dep)

		if not 'state' in self._registry._modules[_module] or self._registry._modules[_module]['state'] in ('I','u',None):
			depends.append(_module)
	
	_logger.info('upgrade-with-depends: %s' % (depends,))

	if len(depends) == 0:
		log.append('Not modules for upgrade')
	else:
		for depend in depends:
			self._registry._load_module(depend)
			_upgradeModule(self,depend,self._registry)

			log.append([0,'module: <%s> successfull upgraded' % (depend,)])

		dep_modules = set()
		for depend in depends:
	
			keys = list(self._registry._objs[depend]['models'].keys())
			for key in keys:
				if 'inherit' in self._registry._momm[depend][key]['attrs'] and ModelInherit in self._registry._momm[depend][key]['bases']:
					inherit = self._registry._momm[depend][key]['attrs']['inherit']
					for ikey in inherit.keys():
						m1 = self._registry._getLastModule(key)
						if m1:
							dep_modules.add(key)
	
		# self._registry._reload_modules(all_modules)
	
		# for all_module in filter(lambda x: x in all_modules,[node.name for node in self._registry._graph]):
			# for mkey in self._registry. _getModuleModels(all_module).keys():
				# self._session._models[mkey] = self._registry._create_module_object('models',mkey,self._registry._getLastModuleLoaded(mkey))
			
			# log.append([0,'module: <%s> successfull reloaded' % (all_module,)])
	
	return log

def _installModule(self,name,chunk,context):
	_logger.info("Module: %s Install" % (name,))

	self._registry._load_module(name)
	#web_pdb.set_trace()
	self._session._objects = self._registry._create_loaded_objects(self._session)
	sqls = []
	if 'module' in chunk:
		models = self._registry._getKeysModuleObjects(name)['models']
		for model in models:
			m = self._session._models[model]
			if isinstance(m,Model):
				sql=genddl.createTable(self._session._models,m.modelInfo())
				if len(sql) > 0:
					sqls.append(sql)
			elif isinstance(m,ModelInherit):
				if  m._inherit:
					sql=genddl.AlterTable(self._session._models,m.imodelInfo())
					if len(sql) > 0:
						sqls.append(sql)
	
		for model in models:
			m = self._session._models[model]
			if isinstance(m,ModelInherit):	
				continue
			at = genddl.getReferencedConstraints(self._session._models,model)
			if len(at) > 0:
				sqls.extend(at)

		for model in models:
			m = self._session._models[model]
			if isinstance(m,ModelInherit):	
				continue
			if len(m._i18nfields) > 0:
				sql = genddl.createI18NTable(self._session._models,m.modelInfo())
				if len(sql) > 0:
					sqls.append(sql)
		
		if len(sqls) > 0:
			self._cr.commit()
			_logger.info("Creating tables")
			if len(sqls) == 1:
				self._cr.execute(sqls[0])
			else:
				self._cr.execute(reduce(lambda x,y: x + ';' + y, sqls))

			self._cr.commit()
	
			_logger.info("Tables created")
	
			self._registry._load_inheritable(name)
			#web_pdb.set_trace()
			for k in self._session._models.keys():
				self._session._access.setdefault('models',{})[k] = Access(read=True,write=True,create=True,unlink=True,modify=True,insert=True,select=True,update=True,delete=True,upsert=True,browse=True,selectbrowse=True)

				#self._session._models[k]._access = Access(read=True,write=True,create=True,unlink=True,modify=True,insert=True,select=True,update=True,delete=True,upsert=True,browse=True,selectbrowse=True)
			
			if name == 'bc':
				self._cr.execute('insert into ' + self._session._models.get('bc.users')._table + ' (id,login,password,firstname,lastname,issuperuser) values(%s,%s,%s,%s,%s,%s)',(self._uid,'admin',pbkdf2_sha256.hash('admin'),'Administartor','System Administarator',True))
				_load_list_allmodules(self)
	
			_loadMetaData(self,chunk,name,context)
			self._cr.commit()
	else:
		self._session._objects[name] = self._registry._create_module_objects(name)

		for k in self._session._objects[name]['models'].keys():
			self._session._objects[name]['models'][k]._access = Access(read=True,write=True,create=True,unlink=True,modify=True,insert=True,select=True,update=True,delete=True,upsert=True,browse=True,selectbrowse=True)
	
	info = self._registry._modules[name]

	metas = {}

	#if 'env' in chunk and 'env' in info['meta']:
		#metas['env'] = info['meta']['env']
	
	if 'view' in chunk and 'view' in info['meta']:
		metas['view'] = info['meta']['view']
	
	if 'example' in chunk:
		if 'data' in info['meta']:
			metas['data'] = info['meta']['data']
		if 'demo' in info['meta']:
			metas['demo'] = info['meta']['demo']
	else:
		if 'data' in chunk and 'data' in info['meta']:
			metas['data'] = info['meta']['data']
		if 'demo' in chunk and 'demo' in info['meta']:
			metas['demo'] = info['meta']['demo']
	
	if 'test' in chunk and 'test' in info['meta']:
		metas['test'] = info['meta']['test']
	
	if 'i18n' in chunk and 'i18n' in info['meta']:
		metas['i18n'] = info['meta']['i18n']
		
	_loadFiles(self,name,self._registry._modules[name],metas,context)
	self._cr.commit()
	#_load_env(self,name)
	
	#self._cr.commit()
	self._session._setLangs()
	_logger.info("Module: %s Installed:" % (name,))

def _uninstallModule(self,name):
	_logger.info(" Module: %s Uninstall" % (name,))
	#module_models = self._registry._objs[name]['models'].keys()
	module_models = self._registry._metas[name]['models'].keys()
	meta = self._registry._modules[name]['meta']
	mom = self._registry._objs[name]['models']

	# xmldatas = self._session._models.get('bc.model.data').select(['name','module','model','rec_id'],[('module','=',name)])
	# xmlmodels = {}
	# for xmldata in xmldatas:
		# xmlmodels.setdefault(xmldata['model'],[]).append(xmldata['rec_id'])
	
	# for key in xmlmodels.keys():
		# r = self._session._models.get(key).unlink(xmlmodels[key])
		# _logger.info(" Unlink from model: %s records: %s" % (key,len(xmlmodels[key])))

	# self._session._models.get('bc.model.data').unlink(list(map(lambda x: x['id'],xmldatas)))

	# f = self._session._models.get('bc.module.files').delete([('module_id','=',name)])
	# _logger.info(" Unlink module files: %s records: %s" % (name,len(f)))

	mm = self._session._models.get('bc.models').select(['module_id','code','db_table',{'columns':['model_id']}],[('module_id','=',name)])
	db_models = list(map(lambda x: x['code'],mm))
	for m in mm:
		self._session._models.get('bc.model.columns').unlink(list(map(lambda x: x['id'],m['columns']))) 
	
	self._session._models.get('bc.models').unlink(list(map(lambda x: x['id'],mm))) 

	mmi = self._session._models.get('bc.model.inherits').select(['module_id',{'columns':['inherit_id']}],[('module_id','=',name)])
	for m in mmi:
		self._session._models.get('bc.model.inherit.columns').unlink(list(map(lambda x: x['id'],m['columns']))) 
		self._session._models.get('bc.model.inherit.inherits').unlink(list(map(lambda x: x['id'],m['columns']))) 
	
	self._session._models.get('bc.model.inherits').unlink(list(map(lambda x: x['id'],mmi))) 

	
	sqls = []
	for models in (module_models,db_models):
		for model in reversed(models):
			if model in mom:
				mods = mom[model]
				table = None
				inherit = None
				if '_table' in mods['attrs']:
					table = mods['attrs']['_table']
				else:
					table = mods['attrs']['_name'].replace('.','_')
		
				if '_inherit' in mods['attrs'] and mods['attrs']['_inherit']:
					inherit = mods['attrs']['_inherit']
		
				if table:
					if inherit:
						for ikey in inherit.keys():
							for icolkey in inherit[ikey]['_columns']:
								if mods['attrs']['_columns'][icolkey]._type not in ('iProperty','referenced'):
									sqls.append("ALTER TABLE IF EXISTS %s DROP COLUMN IF EXISTS %s CASCADE" % (ikey,icolkey))
							
							mmiv = self._session._models.get('bc.ui.model.views').select([{'inherit_views':['name']}],[('model','=',ikey)])
							self._session._models.get('bc.ui.model.view.column.inherits').unlink(list(map(lambda x: x['id'],mmiv))) 				
							
					else:
						if model in self._session._models:
							m = self._session._models.get(model)
							if isinstance(m,Model):
								columns = m.modelInfo(['columns'])['columns']
								for key in filter(lambda x: columns[x]['type'] == 'many2many',columns.keys()):
									rel = genddl.getName(columns[key]['rel'])
									sqls.append("DROP TABLE IF EXISTS %s " % (genddl.getName(rel),))
			
						sqls.append("DROP TABLE IF EXISTS "+table)
	
	if len(sqls) > 0:
		self._cr.commit()
		_logger.info("Drop tables")

		self._cr.execute(reduce(lambda x,y: x + ';' + y, sqls))

		_logger.info("Tables dropped")


	xmldatas = self._session._models.get('bc.model.data').select(['name','module','model','rec_id'],[('module','=',name)])
	xmlmodels = {}
	for xmldata in xmldatas:
		xmlmodels.setdefault(xmldata['model'],[]).append(xmldata['rec_id'])
	
	for key in xmlmodels.keys():
		r = self._session._models.get(key).unlink(xmlmodels[key])
		_logger.info(" Unlink from model: %s records: %s" % (key,len(xmlmodels[key])))

	self._session._models.get('bc.model.data').unlink(list(map(lambda x: x['id'],xmldatas)))

	f = self._session._models.get('bc.module.files').delete([('module_id','=',name)])
	_logger.info(" Unlink module files: %s records: %s" % (name,len(f)))




	module_id = self._registry._modules[name]['db_id']
	self._session._models.get('bc.modules').write({'id':module_id,'state':'N'},{})
	self._registry._modules[name]['state'] = 'N'

	self._cr.commit()

	_logger.info(" Module: %s Uninstalled" % (name,))

def _upgradeModule(self,name):
	log = []
	_logger.info(" Module: %s Upgrade" % (name,))

	mm = self._session._models.get('bc.models').select(['module_id','name','db_table',{'columns':['model_id']}],[('module_id','=',name)])
	db_models = list(map(lambda x: x['name'],mm))
	db_tables = {}
	for m in mm:
		db_tables[m['name']] = m['db_table']

	module_models = self._registry._objs[name]['models'].keys()
	models_to_drop = list(filter(lambda x: x not in module_models,db_models))
	models_to_create = list(filter(lambda x: x not in db_models,module_models))
	models_to_check_upgrade = list(filter(lambda x: x in module_models,db_models))
	print('DROP-MODEL:',name,models_to_drop)
	print('CREATE-MODEL:',name,models_to_create)
	print('UPGRADE-MODEL:',name,models_to_check_upgrade)
	
	sqls = []
	for model in models_to_drop:
		sqls.append('DROP TABLE IF EXISTS %$' % (db_tables[model]))

	for model in models_to_create:
		mm_class_meta = self._registry._getMetaOfModulesModel(model,name)
		if Model in mm_class_meta['bases']:	
			mm_class = type(mm_class_meta['name'],mm_class_meta['bases'],mm_class_meta['attrs'])
			type.__init__(mm_class,mm_class_meta['name'],mm_class_meta['bases'],mm_class_meta['attrs'])
			m = mm_class()
			if isinstance(m,Model):
				sql=genddl.createTable(self._session._models,m.modelInfo())
				sqls.append(sql)
		elif ModelInherit in mm_class_meta['bases']:
			mm_class = type(mm_class_meta['name'],mm_class_meta['bases'],mm_class_meta['attrs'])
			type.__init__(mm_class,mm_class_meta['name'],mm_class_meta['bases'],mm_class_meta['attrs'])
			mm = mm_class()
			imodelinfo = mm_class().modelInfo()
			if imodelinfo['inherit']:
				sql=genddl.AlterTable(self._session._models,imodelinfo)
				sqls.append(sql)

	for model in models_to_create:
		m = self._registry._create_module_object('models',model,name)
		if isinstance(m,ModelInherit):	
			continue

		sqls.extend(genddl.getReferencedConstraints(self._session._models,model))
	
	models_to_upgrade = []
	bc_columns = self._session._models.get('bc.model.columns').columnsInfo()
	columns = list(self._session._models.get('bc.model.columns')._columns.keys())
	
	cols_to_drop = {}
	cols_to_create = {}
	cols_to_check_upgrade = {}
	
	for model in models_to_check_upgrade:
		if isinstance(self._session._models.get(model),ModelInherit):
			continue
		db_cols = self._session._models.get('bc.models').select([{'columns':columns}],[('name','=',model)])[0]['columns']
		model_cols = list(self._session._models.get(model)._columns.keys())
		cd = list(filter(lambda x:x not in model_cols,db_cols))
		if len(cd) > 0:
			cols_to_drop[model] = cd
		cc = list(filter(lambda x:x not in db_cols,model_cols))
		if len(cc) > 0:
			cols_to_create[model] = cc
		ccu = list(filter(lambda x:x in model_cols,db_cols))
		if len(ccu) > 0:
			cols_to_check_upgrade[model] = ccu

	print('DROP-COLS:',cols_to_drop)
	print('CREATE-COLS:',cols_to_create)
	print('UPGRADE-COLS:',cols_to_check_upgrade)


	for key in cols_to_drop.keys():
		if isinstance(self._session._models.get(key),ModelInherit):
			continue
		for key1 in cols_to_drop[key]:
			sqls.append('ALTER TABLE IF EXISTS %s DROP COLUMN IF EXISTS %s CASCADE' % (key,key1))

	for key in cols_to_create.keys():
		if isinstance(self._session._models.get(key),ModelInherit):
			continue
		for key1 in cols_to_create[key]:
			ca = self._session._models.get(key).columnsInfo(columns=[key1])
			if 'size' in ca[key1]:
				if ca[key1]['size'] is  None:
					sz = ''
				elif type(ca[key1]['size']) == tuple:
					sz = '%s' % (ca[key1]['size'],)
				else:
					sz = '(%s)' % (ca[key1]['size'],)
			else:
				sz = ''
			sqls.append('ALTER TABLE IF EXISTS %s ADD COLUMN IF NOT EXISTS %s %s%s' % (key,key1,ca[key1]['db_type'],sz))


	print('SQL-UPGRADE:',sqls)
	self._registry._load_module(name)
	_logger.info(" Module: %s Upgraded" % (name,))

def sysinstall(self):
	log = []
	log.append(_install(self,['system']))
	log.append(_install(self,['autoinstall']))
	return log

def install(self,modules = None):
	return _install(self,['install'],modules)

def uninstall(self,modules = None):
	return _uninstall(self,['install'],modules)

def sysupgrade(self,modules = None):
	return _upgrade(self,['system', 'autoinstall'],modules)

def upgrade(self,modules = None):
	return _upgrade(self,['install','autoinstall'],modules)

def upgrademoduleslist(self,db):
	return _upgrademoduleslist(self,db)

def _load_list_allmodules(self):
	records = []
	for module in self._registry._depends:
		record = {}
		meta = self._registry._modules[module]['meta']
		#columns = self._registry._create_module_model('bc.modules','bc').modelInfo()['columns']
		columns = self._session._models.get('bc.modules').columnsInfo()
		record['code'] = module
		record['state'] = 'N'
		for key in  columns.keys():
			if not columns[key]['type'] in ('one2many','many2one') and key in meta:
				record[key] = meta[key]

		records.append(record)

	ids = self._session._models.get('bc.modules').create(records,{})
	records = self._session._models.get('bc.modules').read(ids, ['code'])

	for record in records:
		self._registry._modules[record['code']]['db_id'] = record['id']

def _load_list_modules(self,db):
	records = []
	self._cr.execute('SET DATABASE = %s' % (db,))
	_uid = self._session._models.get('bc.users').select(fields=[],cond=[('login','=','admin')],context={})[0]['id'] 
	db_modules = list(map(lambda x: x[1],self._session._models.get('bc.modules').select(fields=['code'],context={'FETCH':'LIST'})))
	modules = list(filter(lambda x: not x in db_modules,self._registry._modules.keys()))
	for module in modules:
		if module in db_modules:
			continue
		record = {}
		meta = self._registry._modules[module]['meta']
		#columns = self._registry._create_module_model('bc.modules','bc').modelInfo()['columns']
		columns = self._session._models.get('bc.modules').columnsInfo()
		record['code'] = module
		record['state'] = 'N'
		for key in  columns.keys():
			if not columns[key]['type'] in ('one2many','many2one') and key in meta:
				record[key] = meta[key]

		records.append(record)
	if len(modules) > 0:
		ids = self._session._models.get('bc.modules').create(records,{})
		records = self._session._models.get('bc.modules').read(ids, ['code'],{})
		self._cr.commit()
		self._cr.execute('SET DATABASE = %s' % ('system',))

		for record in records:
			self._registry._modules[record['code']]['db_id'] = record['id']

		return ['Upgrade modules',modules]

	return ['No modules for upgrade']

def _loadMetaModule(self,name,context):
	models = list(self._registry._metas[name]['models'].keys())
	columns = self._session._models.get('bc.modules').columnsInfo()
	module_id = self._registry._modules[name]['db_id']
	# file_records = _loadModuleFile(self._registry._modules[name]['path'],name)
	# for file_record in file_records:
		# file_record['module_id'] = module_id

	# self._session._models.get('bc.module.files').create(file_records,{})

	model_records = []
	imodel_records = []
	
	for model in models:
		m = _loadMetaModel(self,model,name,context)
		if len(m) > 0:
			m['module_id'] = module_id
			#model_records.append(m)
			self._session._models.get('bc.models').create(m,context)
		else:
			im = _loadMetaInherit(self,model,name,context)
			if len(im) > 0:
				im['module_id'] = module_id
				#imodel_records.append(im)
				oid = self._session._models.get('bc.model.inherits').create(im,context)[0]
				icols = {}
				imcols = self._session._models.get('bc.model.inherit.columns').select(fields=['inherit_id','col','moc'],cond=[('inherit_id','r=',oid)],context=context)
				for imcol in imcols:
					if imcol['moc']['type'] != 'iProperty':
						icols[imcol['col']] = imcol['id']
					
				inherit = self._registry._create_module_object('models',model,name)._inherit
				if inherit:
					imc_records = []
					for mkey in inherit.keys():
						mid = self._session._models.get('bc.models').select(fields=[],cond=[('code','=',mkey)])[0]['id']
						if '_columns' in inherit[mkey]:
							imc_record = {}
							for c in inherit[mkey]['_columns']:
								if c in icols:
									imc_record['inherit_id'] = oid
									imc_record['model_id'] = mid
									imc_record['col'] = icols[c]
							if len(imc_record) > 0:
								imc_records.append(imc_record)
					#web_pdb.set_trace()
					self._session._models.get('bc.model.inherit.inherits').create(imc_records,context)			
	# if len(model_records) > 0:
		# self._session._models.get('bc.models').create(model_records,context)

	# if len(imodel_records) > 0:
		# oids = self._session._models.get('bc.model.inherits').create(imodel_records,{})
		# imodel_inherit_records = []

		# for oid in oids:
			# pass
		# if len(imodel_inherit_records) > 0:
			# self._session._models.get('bc.model.inherit.inherits').create(imodel_inherit_records,{})
	
	
	self._session._models.get('bc.modules').write({'id':module_id,'state':'I'},context)
	self._registry._modules[name]['state'] = 'I'

def _loadModuleFiles(self,name,context):
	#web_pdb.set_trace()
	module_id = self._registry._modules[name]['db_id']
	file_records = _loadModuleFile(self._registry._modules[name]['path'],name)

	for file_record in file_records:
		file_record['module_id'] = module_id

	self._session._models.get('bc.module.files').create(file_records,context)


def _loadModuleFile(path,name,ext=['py','xml','csv','yaml','yml','so']):
	records = []
	pwd = opj(reduce(lambda x,y: x + os.path.sep + y ,os.path.dirname(os.path.abspath(__file__)).split(os.path.sep)[:-1]),'self._registry')
	offset = len(opj(pwd,path,name))
	for curdir,dirs,files in os.walk(opj(pwd,path,name)):
		for f in files:
			if f.split('.')[-1] in ext:
				f1 = opj(curdir[offset:],f)
				if f1.startswith(os.path.sep):
					f1 = f1[1:]
				f2 = opj(curdir,f)
				st = os.stat(f2)
				record = {}
				record['filename'] = opj(name,f1)
				record['size'] = st.st_size
				record['ctime'] = datetime.fromtimestamp(st.st_ctime)
				record['mtime'] = datetime.fromtimestamp(st.st_mtime)
				records.append(record)
	return records

def _loadMetaModel(self,model,module,context):
	record = {}
	info_class = self._registry._create_module_object('models',model,module)
	
	class_model = self._session._models.get('bc.class.models')
	class_model_category = self._session._models.get('bc.class.model.categories')
	if not info_class or isinstance(info_class,ModelInherit):
		return record
	info_model = info_class.modelInfo()
	columns = info_model['columns']
	del info_model['columns']
	
	record['code'] = info_model['name']
	record['descr'] = info_model['description']
	record['class_model'] = class_model.search([('code','=', info_model['class_model'])])[0]
	if info_model['class_model_category']:
		cat = class_model_category.search([('code','=', info_model['class_model_category'])],context)
		if len(cat) > 0:
			record['class_model_category'] = cat
	record['oom'] = info_model
	
	for idx,col in enumerate(columns.keys()):
		record.setdefault('columns',[]).append({'seq':idx * 10,'model_name':model,'col':col,'moc':columns[col]})

	return record		

def _loadMetaInherit(self,model,module,context):
	record = {}
	info_class = self._registry._create_module_object('models',model,module)
	if not info_class or isinstance(info_class,Model):
		return record
	
	info_model = info_class.imodelInfo()
	columns = {}
	for col in info_model['columns'].keys():
		if info_model['columns'][col]['type'] == 'iProperty':
			continue
		columns[col] = info_model['columns'][col]

	del info_model['columns']
	
	record['code'] = info_model['name']
	record['descr'] = info_model['description']
	record['momi'] = info_model
	
	for idx,col in enumerate(columns.keys()):
		record.setdefault('columns',[]).append({'seq':idx * 10,'col':col,'moc':columns[col]})

	# if info_model['inherit']:
		# for mkey in info_model['inherit'].keys():
			# info_class_inherit = self._session._models.get('bc.models')
			# if '_columns' in info_model['inherit'][mkey]:
				# for mcol in info_model['inherit'][mkey]['_columns']:
					# #model_id = info_class_inherit.search([('code','=',mkey)])[0]
					# model_id = info_class_inherit.select(fields=['code'],cond=[('code','=',mkey)])[0]
					# model_id['name'] = model_id['code']
					# del model_id['code']  
					# record.setdefault('models',[]).append({'model_id':model_id,'col':mcol})
		
		
	return record		

def _loadMetaColumnInherit(self,model,module,context):
	record = {}
	info_class = self._registry._create_module_object('models',model,module)
	if not info_class or isinstance(info_class,Model):
		return record
	
	info_model = info_class.imodelInfo()
	columns = {}
	for col in info_model['columns'].keys():
		if info_model['columns'][col]['type'] == 'iProperty':
			continue
		columns[col] = info_model['columns'][col]

	del info_model['columns']
	
	record['code'] = info_model['name']
	record['descr'] = info_model['description']
	record['momi'] = info_model
	
	# for idx,col in enumerate(columns.keys()):
		# record.setdefault('columns',[]).append({'seq':idx * 10,'col':col,'moc':columns[col]})

	if info_model['inherit']:
		for mkey in info_model['inherit'].keys():
			info_class_inherit = self._session._models.get('bc.models')
			if '_columns' in info_model['inherit'][mkey]:
				for mcol in info_model['inherit'][mkey]['_columns']:
					#model_id = info_class_inherit.search([('code','=',mkey)])[0]
					model_id = info_class_inherit.select(fields=['code'],cond=[('code','=',mkey)])[0]
					model_id['name'] = model_id['code']
					del model_id['code']  
					record.setdefault('models',[]).append({'model_id':model_id,'col':imcol})
		
		
	return record		

# def _loadMetaModelColumn(self,name,column):
	# return {'moc': self.columnsInfo(columns=[name])}
	# record = {}
	# ref_fields = {'col_name':'name','col_check':'check','col_unique':'unique','col_default':'default','col_family':'family'}
	# keys = self._session._models.get('bc.model.columns').modelInfo(['columns'])['columns'].keys()
	# record['col_name'] = name
	# record['col_type'] = column['type']
	# for key in keys:
		
		# if key in column or key in ref_fields:
			# if key in ref_fields:
				# if ref_fields[key] in column:
					# record[key] = column[ref_fields[key]]
			# else:
				# if key in ('context','domain','selections','relatedy'):
					# record[key] = '%s ' % (column[key],)
				# else:
					# if key == 'size' and type(column[key]) == tuple:
						# record[key] = column[key][0]
						# record['precision'] = column[key][1]
					# else:
						# record[key] = column[key]
	
	# return record		

# def _loadMetaInheritColumns(self,name,column):
	# record = {}
	# ref_fields = {'col_name':'name','col_check':'check','col_unique':'unique','col_default':'default','col_family':'family'}
	# keys = self._session._models.get('bc.inherit.columns').modelInfo(['columns'])['columns'].keys()
	# record['col_name'] = name
	# record['col_type'] = column['type']
	# for key in keys:
		
		# if key in column or key in ref_fields:
			# if key in ref_fields:
				# if ref_fields[key] in column:
					# record[key] = column[ref_fields[key]]
			# else:
				# if key in ('context','filtering','domain','selections'):
					# record[key] = '%s ' % (column[key],)
				# else:
					# if key == 'size' and type(column[key]) == tuple:
						# record[key] = column[key][0]
						# record['precision'] = column[key][1]
					# else:
						# record[key] = column[key]
	
	# return record		


	
def _loadMetaData(self,chunk,name,context):
	_loadModuleFiles(self,name,context)
	_loadEnvModule(self,chunk,name,context)
	record = _loadMetaModule(self,name,context)
	return self._session._models.get('bc.modules').create(record,context)

def _loadEnvModule(self,chunk,name,context):
	info = self._registry._modules[name]
	metas = {}
	if 'env' in chunk and 'env' in info['meta']:
		metas['env'] = info['meta']['env']
		_loadFiles(self,name,self._registry._modules[name],metas,context)


# def _load_env_column(self,model,column):
	# v = {}
	# m = self._session._models.get(model)
	# obj = self._session._models.get(m.columnsInfo([column],['obj'])[column]['obj'])
	# recname = obj._getRecNameName()
	# r = obj.select([recname],{})
	# for k in r:
		# v[k[recname]] = k['id']
	
	# return v

# def _load_class_bc(self,name):
	# bc_models = self._session._models.get('bc.models').select(['name','module_id'],[('module_id','=','bc'),[('name','=','bc.models')]],{})
	# models = self._session._models.get('bc.models').select(['name','module_id'],[('module_id','=',name)],{})
	# mt = {}
	# bcm = self._session._models.get('bc.models')
	# mod_records = []
	# for model in models:
		# m = self._session._models.get(model['name'])
		# if isinstance(m,ModelInherit):
			# continue
		# if 'env-fields' in bcm._extra:
			# envfields = bcm._extra['env-fields']
			# for envfield in envfields:
				# mt[envfield] = _load_env_column(self,bcm._name,envfield)

			# mod_record = {'id':model['id']}
			# for envfield in envfields:
				# ef = getattr(m,'_' + envfield,None)
				# if ef:
					# mod_record[envfield] = mt[envfield][ef]
			
			# mod_records.append(mod_record)
	
	# bcm.write(mod_records,{})
			
# def _load_env(self,name):
	# models = self._session._models.get('bc.models').select(['name','module_id'],[('module_id','=',name)],{})
	# mt = {}
	# for model in models:
		# m = self._session._models.get(model['name'])
		# if not m or isinstance(m,ModelInherit) or m._name == 'bc.models':
			# continue
		# if 'env-fields' in m._extra:
			# envfields = m._extra['env-fields']
			# for envfield in envfields:
				# mt[envfield] = _load_env_column(self,m._name,envfield)

			# r1 = m.select([m._getRecNameName()],{})
			# mod_records = []
			# for k1 in r1:
				# mod_record = {'id':k1['id']}
				# for envfield in envfields:
					# ef = getattr(m,'_' + envfield,None)
					# if ef:
						# mod_record[envfield] = mt[envfield][ef]
				# mod_records.append(mod_record)
			
			# m.write(mod_records,{})

	# _load_class_bc(self,name)

def _loadFiles(self,name,info,metas,context):
	path = info['path']
	for key in metas.keys():
		meta = metas[key]
		for f in meta:
			ext = f.split('.')[-1]
			if ext == 'xml':
				if os.path.exists(opj(path,name,f)):
					_logger.info("loading file: %s" % (opj(path,name,f),))
					_loadXMLFile(self,info,path,name,f,context)
					_logger.info("Loaded  file: %s" % (opj(path,name,f),))
				else:
					_logger.critical("Loading  file: %s not found" % (opj(path,name,f),))
			elif ext == 'csv':		
				if os.path.exists(opj(path,name,f)):
					_logger.info("loading file: %s" % (opj(path,name,f),))
					if key == 'test':
						pass
					else:
						_loadCSVFile(self,info,path,name,f,context)
					_logger.info("Loaded  file: %s" % (opj(path,name,f),))
				else:
					_logger.critical("Loading  file: %s not found" % (opj(path,name,f),))
			elif ext == 'po':		
				if os.path.exists(opj(path,name,f)):
					_logger.info("loading file: %s" % (opj(path,name,f),))
					res = _load_i18n(path,name,f)
					for lang in res.keys():
						r = self._session._models.get('bc.langs').search([('code','=',lang)],context)
						if len(r) > 0:
							for model in res[lang].keys():
								r1 = self._session._models.get('bc.models').search([('code','=',model)],context)
								if len(r1) > 0:
									v = res[lang][model]
									self._session._models.get('bc.model.translations').modify({'lang':r[0],'model':r1[0],'tr':json.dumps(v)},context)
							
						
					_logger.info("Loaded  file: %s" % (opj(path,name,f),))
				else:
					_logger.critical("Loading  file: %s not found" % (opj(path,name,f),))

def _convertFromYAML(self,model,records,context):
	m = self._session._models.get(model)
	columns_info = m.columnsInfo()
	sfs = m._selectionfields
	mfs = {}
	for sf in sfs:
		for k,v in columns_info[sf]['selections']:
			mfs.setdefault(sf,{})[v] = k 

	for record in records:
		for key in record.keys():
			if key == 'id':
				continue
			if columns_info[key]['type'] in ('many2one','referenced','related'):
				recname = self._session._models.get(columns_info[key]['obj'])._getRecNameName()
				if recname is None:
					recname = 'id'	
				if record[key] is not None:
					cond = [(recname,'=',record[key])]
					if columns_info[key]['type'] == 'related':
						for rel in columns_info[key]['relatedy']:
							cond.append((rel,'=',record[rel]))
					oids = self._session._models.get(columns_info[key]['obj']).search(cond,context,1)
					if len(oids) > 0:
						record[key] = oids[0]
			elif columns_info[key]['type'] in ('datetime','time') and columns_info[key]['timezone']:
				if record[key]:
					record[key] = record[key].astimezone()
			elif columns_info[key]['type'] == 'selection':
				if record[key] and len(record[key]) > 0:
					record[key] = mfs[key][record[key]]
			elif columns_info[key]['type'] == 'one2many':
				_convertFromYAML(self,columns_info[key]['obj'],record[key],context)

def _loadCSVFile(self,info,path,name,fl,context):
	with open(opj(path,name,fl)) as csvafile:
		_buffer = KeyBuffer()
		areader = csv.DictReader(csvafile)
		if not (areader.fieldnames == ['file','model'] or areader.fieldnames == ['model','file']):
			msg = "Invalid format anotation CSV file: %s\n Must be ['model','file'] or ['file','model']" % (areader.fieldnames,) 
			_logger.critical(msg)
			Exception(msg)
		
		for row in areader:
			model = row['model']
			f = row['file']
			ext = f.split('.')[-1]
			if ext == 'csv':
				with open(opj(path,name,f)) as csvfile:
					_logger.info("    loading annotation file: %s" % (opj(path,name,f),))
					reader = csv.DictReader(csvfile)
					fields = reader.fieldnames
					values = []
					value = []
					for row in reader:
						value = []
						for field in fields:
							value.append(row[field])
	
						values.append(value)
					ir = self._session._models.get(model).do_upload_csv(self,fields,values,context.copy().update({'FETCH':'LIST'}))
					_logger.info("    Loaded annotation file: %s - records:%s" % (opj(path,name,f),len(ir)))

			elif ext == 'yaml':
				with open(opj(path,name,f)) as yamlfile:
					_logger.info("    loading annotation file: %s" % (opj(path,name,f),))
					records = yaml.load(yamlfile,Loader=Loader)					
					parents = []
					rows = []
					mi = self._session._models.get(model).modelInfo()
					parent_id = mi['names']['parent_id']
					childs_id = mi['names']['childs_id']
					rec_name = mi['names']['rec_name']
					ir = []
					if parent_id and childs_id:						
						ts = {}
						for record in records:
							ts.setdefault(record[rec_name],set()).add(record[parent_id])
						tss = list(toposort.toposort(ts))
						#print('TSS:',tss)
						#web_pdb.set_trace()
						for keys in tss:
							for key in keys:
								rows = list(filter(lambda x:x[parent_id] == key,copy.deepcopy(records)))
								if len(rows) > 0:
									_convertFromYAML(self,model,rows,context)
									ir = self._session._models.get(model).modify(rows,context)
									self._session._cursor._commit()								
					else:
						_convertFromYAML(self,model,records,context)
						ir = self._session._models.get(model).modify(records,context)
					_logger.info("    Loaded annotation file: %s - records:%s" % (opj(path,name,f),len(ir)))

def _loadXMLFile(self,info,path,name,fl,context):
	_buffer = KeyBuffer()
	fk = {}
	rng=etree.RelaxNG(etree=etree.parse(opj(os.path.dirname(os.path.abspath(__file__)),'views.rng')))
	obj = 'bc.module.files'
	file_id = self._session._models.get(obj).search(cond=[(self._session._models.get(obj)._getRecNameName(),'=',opj(name,fl))],context=context,limit=1)[0]
	for event,el in etree.iterparse(source=opj(path,name,fl),events=('end','start')):
		if el.tag == 'records':
			if event == 'start':
				records = []
				datarecords = []
				model = el.attrib['model']
				modelinfo = self._session._models.get(model).modelInfo()
				columnsinfo = modelinfo['columns']
				columns = list(columnsinfo.keys())
				for column in columns:
					if columnsinfo[column]['type'] == 'selection':
						fkk = {}
						for k,v in columnsinfo[column]['selections']:
							fkk[v] = k
						fk[column] = fkk 
			else:
				ids = self._session._models.get(model).create(records,context)
				for i in range(len(ids)):
					datarecords[i]['rec_id'] = ids[i]
				self._session._models.get('bc.model.data').create(datarecords,context)
		elif el.tag == 'record':
			if event == 'start':
				record = {}
				datarecord = {}
			else:
				for key in record.keys():
						column = columnsinfo[key]
						if column['type'] in ('many2one','referenced','related'):
							obj = column['obj']
							recname = self._session._models.get(obj)._getRecNameName()

							oid = _buffer.key(key,obj,record[key])
							if not oid:
								if 'ref' in el.attrib:
									ctx = context.copy()
									ctx.update({'FETCH':'LIST'})
									oid = self._session._models.get('bc.model.data').select(fields=['rec_id'],cond=[('name','=',el.attrib['ref'])],context = ctx,limit=1)[0]
								else:
									try:
										ctx = context.copy()
										ctx.update({'FETCH':'LIST'})
										oid = self._session._models.get(obj).search(cond=[(recname,'=',record[key])],context = ctx,limit=1)[0]
									except:
										web_pdb.set_trace()
										print('RECORD-KEY:',obj,record[key])
									
								
								_buffer.add(key,obj,record[key],oid)

							record[key] = oid
						elif column['type'] in ('selection',):
							record[key] = fk[key][record[key]]

				records.append(record)

				datarecord['name'] = el.attrib['id']
				datarecord['module'] = name
				datarecord['model'] = model
				datarecord['file_id'] = file_id
				datarecord['date_init'] = datetime.utcnow()
				
				datarecords.append(datarecord)
		elif el.tag == 'column':
			if event == 'end':

				if not el.attrib['name'] in columns:
					raise XMLValidator('colums: %s not found in: %s file: %s' % (el.attrib['name'],model,opj(name,fl)))
				if 'type' in el.attrib and el.attrib['type'] in ('Xml','Html'):
					try:
						rng.assert_(el.getchildren()[0])
					except:
						_logger.critical(rng.error_log)
												
					record['type'] = el.attrib['type']
					try:
						if len(el.getchildren()) > 0:
							record[el.attrib['name']] = '<?xml version="1.0" encoding="utf-8" standalone="yes" ?>\n\t %s' % (etree.tostring(el.getchildren()[0]).decode('utf-8').replace('\t',' '),)
						else:
							_logger.critical('FILE:%s-NAME%s-DATARECORD:%s-CHILDREN: %s' % (opj(name,fl),el.attrib['name'],datarecord,el.getchildren()))
					except:
						_logger.critical('FILE:%s-NAME%s-DATARECORD:%s-CHILDREN: %s' % (opj(name,fl),el.attrib['name'],datarecord,el.getchildren()))
				else:
					if model == 'bc.ui.views.inherit' and el.attrib['name'] == 'view_id':
						record[el.attrib['name']] = el.text
					else:
						if 'ref' in el.attrib:
							record[el.attrib['name']] = el.attrib['ref']
						else:
							record[el.attrib['name']] = el.text

def _upgrademoduleslist(self,db):

	return _load_list_modules(self,db)

def _load_i18n(path,name,f):
	res = {}
	fn = opj(path,name,f)
	if os.path.exists(fn):
		lang = f.split('.')[0].split('/')[1].upper()
		po = polib.pofile(fn)
		res[lang] = {}
		for entry in po:
			if entry.msgstr:
				for o in entry.occurrences:
					v = dict(map(lambda x:x.split('@'),o[0].split('|')))
					model = v['model']
					for attr in ('_description','__doc__','_columns'):
						if attr in v:	
							if attr == '_columns':
								col_name,col_attr = v['_columns'].split('$')
								if col_attr in ('label','manual','help'):															
									res[lang].setdefault(model,{}).setdefault(attr,{}).setdefault(col_name,{})[col_attr] = entry.msgstr
								elif col_attr[:10] == 'selections':
									sel_val = col_attr.split('#')[1]
									res[lang].setdefault(model,{}).setdefault(attr,{}).setdefault(col_name,{}).setdefault(col_attr[:10],[]).append({'__tuple__':(sel_val,entry.msgstr)})
							else:
								res[lang].setdefault(model,{})[attr] = entry.msgstr

	return res
