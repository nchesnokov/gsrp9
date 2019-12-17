import logging
from passlib.hash import pbkdf2_sha256
from functools import reduce
from datetime import datetime
from lxml import etree
import os
import csv
import yaml
from yaml import Loader
from os.path import join as opj
from . import genddl
from gsrp5service.orm.model import Model,ModelInherit,Access

__all__ = ['install','uninstall','upgrade','sysinstall','sysupgrade','upgrademoduleslist']

_logger = logging.getLogger('listener.' + __name__)

class XMLValidator(Exception): pass

class KeyBuffer(dict):
	
	def add(self,key,obj,recordkey,value):
		self.setdefault(key,{}).setdefault(obj,{})[recordkey] = value

	def key(self,key,obj,recordkey):
		if key in self  and obj in self[key] and recordkey in self[key][obj]:
			return self[key][obj][recordkey]  
		return None

def _install(cr,pool,uid,registry,able=None, modules = None):
	log = []
	_modules = []
	if able is None or not able:
		able= ['install']

	if type(modules) == str:
		if registry._modules[modules]['meta']['able'] in able:
			_modules.append(modules)
	elif type(modules) in (tuple,list):
		for module in registry._depends:
			if module in modules and registry._modules[module]['meta']['able'] in able:
				_modules.append(module)
	elif modules is None:
		for module in registry._depends:
			if registry._modules[module]['meta']['able'] in able:
				_modules.append(module)

	if modules:
		_logger.info('modules-install: %s' % (modules,))
	depends = []
	for _module in _modules:
		for dep in registry._dependsinstall.install(_module):
			if not dep in depends and registry._modules[dep]['meta']['able'] in able and ('state' in registry._modules[dep] and registry._modules[dep]['state'] in ('i','N',None)):
				depends.append(dep)

		if not 'state' in registry._modules[_module] or registry._modules[_module]['state'] in (None,'N','i'):
			depends.append(_module)
	
	_logger.info('install-with-depends: %s' % (depends,))

	if len(depends) == 0:
		log.append('Not modules for install')
	else:
		for depend in depends:
			registry._load_module(depend)
			_installModule(cr,pool,uid,depend,registry)

			log.append([0,'module: <%s> successfull installed' % (depend,)])

		dep_modules = set()
		for depend in depends:
	
			keys = list(registry._momm[depend].keys())
			for key in keys:
				if 'inherit' in registry._momm[depend][key]['attrs'] and ModelInherit in registry._momm[depend][key]['bases']:
					inherit = registry._momm[depend][key]['attrs']['inherit']
					for ikey in inherit.keys():
						m1 = registry._getLastModule(key)
						if m1:
							dep_modules.add(key)
	
			#log.append([0,'module: <%s> successfull installed' % (depend,)])
	
		all_modules = list(filter(lambda x:x != 'bc',depends+list(dep_modules)))
		registry._reload_modules(all_modules)
	
		for all_module in filter(lambda x: x in all_modules,[node.name for node in registry._graph]):
			for mkey in registry. _getModuleModels(all_module).keys():
				pool[mkey] = registry._create_model(mkey,registry._getLastModule(mkey))
			
			log.append([0,'module: <%s> successfull reloaded' % (all_module,)])
	
	return log

def _uninstall(cr,pool,uid,registry,able=None, modules = None):

	_modules = []

	if able is None or not able:
		able= ['install']
	
	if type(modules) == str:
		if registry._modules[modules]['meta']['able'] in able:
			_modules.append(modules)
	elif type(modules) in (tuple,list):
		for module in reversed(registry._depends):
			if module in modules and registry._modules[module]['meta']['able'] in able:
				_modules.append(module)
	elif modules is None:
		for module in reversed(registry._depends):
			if registry._modules[module]['meta']['able'] in able:
				_modules.append(module)

	depends = []
	for _module in _modules:
		for dep in registry._dependsremove.remove(_module):
			if not dep in depends and registry._modules[dep]['meta']['able'] in able and 'state' in registry._modules[dep] and registry._modules[dep]['state'] in ('I ','r'):
				depends.append(dep)
		if 'state' in registry._modules[_module] and registry._modules[_module]['state'] in ('I','r'):
			depends.append(_module)
	
	log = []
	if len(depends) == 0:
		log.append('Not modules for uninstall')
	else:
		for depend in depends:
			registry._load_module(depend)
			_uninstallModule(cr,pool,uid,depend,registry)
	
			#registry._download_module(depend)
			log.append([0,'module: <%s> successfull uninstalled' % (depend,)])
	
		dep_modules = set()
		for depend in depends:
	
			keys = list(registry._momm[depend].keys())
			for key in keys:
				if 'inherit' in registry._momm[depend][key]['attrs'] and ModelInherit in registry._momm[depend][key]['bases']:
					inherit = registry._momm[depend][key]['attrs']['inherit']
					for ikey in inherit.keys():
						m1 = registry._getLastModule(key)
						if m1:
							dep_modules.add(key)
	
			#log.append([0,'module: <%s> successfull uninstalled' % (depend,)])
	
		registry._download_module(depend)
		
		all_modules = depends+list(dep_modules)
		registry._reload_modules(all_modules)
	
		for all_module in filter(lambda x: x in all_modules,[node.name for node in registry._graph]):
			for mkey in registry. _getModuleModels(all_module).keys():
				pool[mkey] = registry._create_model(mkey,registry._getLastModule(mkey))
			
			log.append([0,'module: <%s> successfull reloaded' % (all_module,)])
	
	return log

def _upgrade(cr,pool,uid,registry,able=None, modules = None):
	log = []
	_modules = []
	if able is None or not able:
		able= ['install']
	
	if type(modules) == str:
		if registry._modules[modules]['meta']['able'] in able:
			_modules.append(modules)
	elif type(modules) in (tuple,list):
		for module in registry._depends:
			if module in modules and registry._modules[module]['meta']['able'] in able:
				_modules.append(module)
	elif modules is None:
		for module in registry._depends:
			if registry._modules[module]['meta']['able'] in able:
				_modules.append(module)

	if modules:
		_logger.info('modules-upgrade: %s' % (modules,))
	depends = []
	for _module in _modules:
		for dep in registry._dependsremove.remove(_module):
			if not dep in depends and registry._modules[dep]['meta']['able'] in able and ('state' in registry._modules[dep] and registry._modules[dep]['state'] in ('I','u',None)):
				depends.append(dep)

		if not 'state' in registry._modules[_module] or registry._modules[_module]['state'] in ('I','u',None):
			depends.append(_module)
	
	_logger.info('upgrade-with-depends: %s' % (depends,))

	if len(depends) == 0:
		log.append('Not modules for upgrade')
	else:
		for depend in depends:
			registry._load_module(depend)
			_upgradeModule(cr,pool,uid,depend,registry)

			log.append([0,'module: <%s> successfull upgraded' % (depend,)])

		dep_modules = set()
		for depend in depends:
	
			keys = list(registry._momm[depend].keys())
			for key in keys:
				if 'inherit' in registry._momm[depend][key]['attrs'] and ModelInherit in registry._momm[depend][key]['bases']:
					inherit = registry._momm[depend][key]['attrs']['inherit']
					for ikey in inherit.keys():
						m1 = registry._getLastModule(key)
						if m1:
							dep_modules.add(key)
	
			#log.append([0,'module: <%s> successfull installed' % (depend,)])
	
		all_modules = list(filter(lambda x:x != 'bc',depends+list(dep_modules)))
		registry._reload_modules(all_modules)
	
		for all_module in filter(lambda x: x in all_modules,[node.name for node in registry._graph]):
			for mkey in registry. _getModuleModels(all_module).keys():
				pool[mkey] = registry._create_model(mkey,registry._getLastModuleLoaded(mkey))
			
			log.append([0,'module: <%s> successfull reloaded' % (all_module,)])
	
	return log

def _installModule(cr,pool,uid,name,registry):
	_logger.info(" Module: %s Install" % (name,))
	models = registry._modules[name]['lom']
	meta = registry._modules[name]['meta']
	sqls = []
	for model in models:
		mm_class_meta = registry._getMetaOfModulesModel(model,name)
		if Model in mm_class_meta['bases']:	
			mm_class = type(mm_class_meta['name'],mm_class_meta['bases'],mm_class_meta['attrs'])
			type.__init__(mm_class,mm_class_meta['name'],mm_class_meta['bases'],mm_class_meta['attrs'])
			m = mm_class()
			#print('m:',m._name,list(m._columns.keys()))
			if isinstance(m,Model):
				sql=genddl.createTable(pool,m.modelInfo())
				sqls.append(sql)
		elif ModelInherit in mm_class_meta['bases']:
			mm_class = type(mm_class_meta['name'],mm_class_meta['bases'],mm_class_meta['attrs'])
			type.__init__(mm_class,mm_class_meta['name'],mm_class_meta['bases'],mm_class_meta['attrs'])
			mm = mm_class()
			imodelinfo = mm_class().modelInfo()
			if imodelinfo['inherit']:
				sql=genddl.AlterTable(pool,imodelinfo)
				sqls.append(sql)

	for model in models:
		m = registry._create_model(model,name)
		if isinstance(m,ModelInherit):	
			continue

		sqls.extend(genddl.getReferencedConstraints(pool,model))
	
	if len(sqls) > 0:
		if len(sqls) == 1:
			cr.execute(sqls[0])
		else:
			cr.execute(reduce(lambda x,y: x + ';' + y, sqls))
			#cr.execute(sqls)
		#cr.commit()

		registry._load_inherit(name)
		mm = registry._createModuleModels(name)

		for k in mm.keys():
			pool[k] = mm[k]
			pool[k]._access = Access(read=True,write=True,create=True,unlink=True,modify=True,insert=True,select=True,update=True,delete=True,upsert=True,browse=True,selectbrowse=True)
			registry._models[k] = pool[k]
			

		if name == 'bc':
			cr.execute('insert into ' + pool.get('bc.users')._table + ' (id,login,password,firstname,lastname,issuperuser) values(%s,%s,%s,%s,%s,%s)',(uid,'admin',pbkdf2_sha256.hash('admin'),'Administartor','System Administarator',True))
			_load_list_allmodules(cr,pool,uid,registry)
			registry._load_module(name)

	
	_loadMetaData(cr,pool,uid,name,registry)
	_loadFiles(cr,pool,uid,name,registry._modules[name])
	_load_env(cr,pool,uid,name)
	
	cr.commit()
	_logger.info("Module: %s Installed:" % (name,))

def _uninstallModule(cr,pool,uid,name,registry):
	_logger.info(" Module: %s Uninstall" % (name,))
	module_models = registry._modules[name]['lom']
	meta = registry._modules[name]['meta']
	mom = registry._momm[name]

	xmldatas = pool.get('bc.model.data').select(cr,pool,uid,['name','module','model','rec_id'],[('module','=',name)])
	xmlmodels = {}
	for xmldata in xmldatas:
		xmlmodels.setdefault(xmldata['model'],[]).append(xmldata['rec_id'])
	
	for key in xmlmodels.keys():
		r = pool.get(key).unlink(cr,pool,uid,xmlmodels[key])
		_logger.info(" Unlink from model: %s records: %s" % (key,len(xmlmodels[key])))

	pool.get('bc.model.data').unlink(cr,pool,uid,list(map(lambda x: x['id'],xmldatas)))

	f = pool.get('bc.module.files').delete(cr,pool,uid,[('module_id','=',name)])
	_logger.info(" Unlink module files: %s records: %s" % (name,len(f)))

	mm = pool.get('bc.models').select(cr,pool,uid,['module_id','name','db_table',{'columns':['model_id']}],[('module_id','=',name)])
	db_models = list(map(lambda x: x['name'],mm))
	for m in mm:
		pool.get('bc.model.columns').unlink(cr,pool,uid,list(map(lambda x: x['id'],m['columns']))) 
	
	pool.get('bc.models').unlink(cr,pool,uid,list(map(lambda x: x['id'],mm))) 

	mmi = pool.get('bc.inherits').select(cr,pool,uid,['module_id',{'columns':['inherit_id']}],[('module_id','=',name)])
	for m in mmi:
		pool.get('bc.bc.inherit.columns').unlink(cr,pool,uid,list(map(lambda x: x['id'],m['columns']))) 
	
	pool.get('bc.inherits').unlink(cr,pool,uid,list(map(lambda x: x['id'],mm))) 

	
	sqls = []
	for models in (module_models,db_models):
		for model in reversed(models):
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
							sqls.append("ALTER TABLE IF EXISTS %s DROP COLUMN IF EXISTS %s CASCADE" % (ikey,icolkey))
						
						mmiv = pool.get('bc.ui.views').select(cr,pool,uid,[{'inherit_views':['name']}],[('model','=',ikey)])
						pool.get('bc.ui.views.inherit').unlink(cr,pool,uid,list(map(lambda x: x['id'],mmiv))) 				
						
				else:
					columns = pool.get(model).modelInfo()['columns']
					for key in filter(lambda x: columns[x]['type'] == 'many2many',columns.keys()):
						rel = genddl.getName(columns[key]['rel'])
						sqls.append("DROP TABLE IF EXISTS %s " % (genddl.getName(rel),))
	
					sqls.append("DROP TABLE IF EXISTS "+table)
	
	if len(sqls) > 0:
		cr.execute(reduce(lambda x,y: x + ';' + y, sqls))
	
	module_id = registry._modules[name]['db_id']
	pool.get('bc.modules').write(cr=cr,pool=pool,uid=uid,records={'id':module_id,'state':'N'})
	registry._modules[name]['state'] = 'N'

	cr.commit()
	_logger.info(" Module: %s Uninstalled" % (name,))

	# registry._download_module(name)
	# for mkey in registry. _getModuleModels(name).keys():
		# pool[mkey] = registry._create_model(mkey,registry._getLastModule(mkey))


def _upgradeModule(cr,pool,uid,name,registry):
	log = []
	_logger.info(" Module: %s Upgrade" % (name,))

	mm = pool.get('bc.models').select(cr,pool,uid,['module_id','name','db_table',{'columns':['model_id']}],[('module_id','=',name)])
	db_models = list(map(lambda x: x['name'],mm))
	db_tables = {}
	for m in mm:
		db_tables[m['name']] = m['db_table']

	module_models = registry._modules[name]['lom']
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
		mm_class_meta = registry._getMetaOfModulesModel(model,name)
		if Model in mm_class_meta['bases']:	
			mm_class = type(mm_class_meta['name'],mm_class_meta['bases'],mm_class_meta['attrs'])
			type.__init__(mm_class,mm_class_meta['name'],mm_class_meta['bases'],mm_class_meta['attrs'])
			m = mm_class()
			#print('m:',m._name,list(m._columns.keys()))
			if isinstance(m,Model):
				sql=genddl.createTable(pool,m.modelInfo())
				sqls.append(sql)
		elif ModelInherit in mm_class_meta['bases']:
			mm_class = type(mm_class_meta['name'],mm_class_meta['bases'],mm_class_meta['attrs'])
			type.__init__(mm_class,mm_class_meta['name'],mm_class_meta['bases'],mm_class_meta['attrs'])
			mm = mm_class()
			imodelinfo = mm_class().modelInfo()
			if imodelinfo['inherit']:
				sql=genddl.AlterTable(pool,imodelinfo)
				sqls.append(sql)

	for model in models_to_create:
		m = registry._create_model(model,name)
		if isinstance(m,ModelInherit):	
			continue

		sqls.extend(genddl.getReferencedConstraints(pool,model))
	
	models_to_upgrade = []
	bc_columns = pool.get('bc.model.columns').columnsInfo()
	columns = list(pool.get('bc.model.columns')._columns.keys())
	
	cols_to_drop = {}
	cols_to_create = {}
	cols_to_check_upgrade = {}
	
	for model in models_to_check_upgrade:
		if isinstance(pool.get(model),ModelInherit):
			continue
		db_cols = pool.get('bc.models').select(cr,pool,uid,[{'columns':columns}],[('name','=',model)])[0]['columns']
		model_cols = list(pool.get(model)._columns.keys())
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
		if isinstance(pool.get(key),ModelInherit):
			continue
		for key1 in cols_to_drop[key]:
			sqls.append('ALTER TABLE IF EXISTS %s DROP COLUMN IF EXISTS %s CASCADE' % (key,key1))

	for key in cols_to_create.keys():
		if isinstance(pool.get(key),ModelInherit):
			continue
		for key1 in cols_to_create[key]:
			ca = pool.get(key).columnsInfo(columns=[key1])
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
	registry._load_module(name)
	_logger.info(" Module: %s Upgraded" % (name,))

# new
def sysinstall(cr,pool,uid,registry):
	log = []
	log.append(_install(cr,pool,uid,registry,['system']))
	log.append(_install(cr,pool,uid,registry,['autoinstall']))
	return log

def install(cr,pool,uid,registry,modules = None):
	return _install(cr,pool,uid,registry,['install'],modules)

def uninstall(cr,pool,uid,registry,modules = None):
	return _uninstall(cr,pool,uid,registry,['install'],modules)

def sysupgrade(cr,pool,uid,registry,modules = None):
	return _upgrade(cr,pool,uid,registry,['system', 'autoinstall'],modules)

def upgrade(cr,pool,uid,registry,modules = None):
	return _upgrade(cr,pool,uid,registry,['install','autoinstall'],modules)

def upgrademoduleslist(cr,pool,uid,registry,db):
	return _upgrademoduleslist(cr,pool,uid,registry,db)

# Load Meta

def _load_list_allmodules(cr,pool,uid,registry):
	records = []
	for module in registry._depends:
		record = {}
		meta = registry._modules[module]['meta']
		columns = registry._create_model('bc.modules','bc').modelInfo()['columns']
		record['code'] = module
		record['state'] = 'N'
		for key in  columns.keys():
			if not columns[key]['type'] in ('one2many','many2one') and key in meta:
				record[key] = meta[key]

		records.append(record)

	ids = pool.get('bc.modules').create(cr, pool, uid, records)
	records = pool.get('bc.modules').read(cr, pool, uid,ids, ['code'])
	#print('MODULES:',records)

	for record in records:
		registry._modules[record['code']]['db_id'] = record['id']
		#print('REGISTRY:',record['code'],registry._modules[record['code']]['db_id'])

def _load_list_modules(cr,pool,uid,registry,db):
	records = []
	cr.execute('SET DATABASE = %s' % (db,))
	_uid = pool.get('bc.users').select(cr,pool,uid,fields=[],cond=[('login','=','admin')])[0]['id'] 
	db_modules = list(map(lambda x: x[1],pool.get('bc.modules').select(cr,pool,uid,fields=['code'],context={'FETCH':'LIST'})))
	#print('db_modules:',db_modules)
	modules = list(filter(lambda x: not x in db_modules,registry._modules.keys()))
	for module in modules:
		if module in db_modules:
			continue
		record = {}
		meta = registry._modules[module]['meta']
		columns = registry._create_model('bc.modules','bc').modelInfo()['columns']
		record['code'] = module
		record['state'] = 'N'
		for key in  columns.keys():
			if not columns[key]['type'] in ('one2many','many2one') and key in meta:
				record[key] = meta[key]

		records.append(record)
	if len(modules) > 0:
		ids = pool.get('bc.modules').create(cr, pool, _uid, records)
		records = pool.get('bc.modules').read(cr, pool, _uid,ids, ['code'])
		cr.commit()
		cr.execute('SET DATABASE = %s' % ('system',))
		#print('MODULES:',records)

		for record in records:
			registry._modules[record['code']]['db_id'] = record['id']
			#print('REGISTRY:',record['code'],registry._modules[record['code']]['db_id'])

		return ['Upgrade modules',modules]

	return ['No modules for upgrade']

def _loadMetaModule(cr,pool,uid,name,registry):
	models = registry._modules[name]['lom']
	meta = registry._modules[name]['meta']
	columns = registry._create_model('bc.modules','bc').modelInfo()['columns']
	module_id = registry._modules[name]['db_id']
	file_records = _loadModuleFile(registry._modules[name]['path'],name)
	for file_record in file_records:
		file_record['module_id'] = module_id
	#print('FILE-RECORDS:',file_records)
	pool.get('bc.module.files').create(cr,pool,uid,file_records)

	model_records = []
	imodel_records = []

	for model in models:
		m = _loadMetaModel(cr,pool,uid,registry,model,name)
		if len(m) > 0:
			m['module_id'] = module_id
			model_records.append(m)
		else:
			im = _loadMetaInherit(cr,pool,uid,registry,model,name)
			if len(im) > 0:
				im['module_id'] = module_id
				imodel_records.append(im)

	if len(model_records) > 0:
			pool.get('bc.models').create(cr,pool,uid,model_records)

	if len(imodel_records) > 0:
			pool.get('bc.inherits').create(cr,pool,uid,imodel_records)
	
	pool.get('bc.modules').write(cr,pool,uid,{'id':module_id,'state':'I'})
	registry._modules[name]['state'] = 'I'

def _loadModuleFile(path,name,ext=['py','xml','csv','yaml','yml','so']):
	records = []
	pwd = os.getcwd()
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

def _loadMetaModel(cr,pool,uid,registry,model,module):
	record = {}
	ref_fields = {'db_table':'table'}
	columns = registry._create_model('bc.models','bc').modelInfo()['columns']
	info_class = registry._create_model(model,module)
	if not info_class:
		return record
	info = info_class.modelInfo()
	columns = pool.get('bc.models').modelInfo()['columns']

	for key in columns.keys():
		if not columns[key]['type'] in ('one2many','many2one','many2many') and key in info or key in ref_fields:
			if key  in ref_fields:
				if ref_fields[key] in info:
					record[key] = info[ref_fields[key]]
			else:
				record[key] = info[key]
	for key in info['columns'].keys():
		column = info['columns'][key]
		c = _loadMetaModelColumns(cr,pool,uid,registry,key,column)	
		record.setdefault('columns',[]).append(c)

	return record		

def _loadMetaInherit(cr,pool,uid,registry,model,module):
	record = {}

	columns = registry._create_model('bc.inherits','bc').modelInfo()['columns']
	
	info_class_meta = registry._getMetaOfModules(model,module)
	if info_class_meta:
		info_class = type.__new__(info_class_meta['cls'],info_class_meta['name'],info_class_meta['bases'],info_class_meta['attrs'])
		type.__init__(info_class,info_class_meta['name'],info_class_meta['bases'],info_class_meta['attrs'])
		info = info_class().modelInfo()
		columns = pool.get('bc.inherits').modelInfo()['columns']
	else:
		return record

	for key in columns.keys():
		if not columns[key]['type'] in ('one2many','many2one','many2many') and key in info:
			record[key] = info[key]

	for key in info['columns'].keys():
		column = info['columns'][key]
		c = _loadMetaInheritColumns(cr,pool,uid,registry,key,column)	
		record.setdefault('columns',[]).append(c)

	return record		


def _loadMetaModelColumns(cr,pool,uid,registry,name,column):
	record = {}
	ref_fields = {'col_name':'name','col_check':'check','col_unique':'unique','col_default':'default','col_family':'family'}
	keys = pool.get('bc.model.columns').modelInfo()['columns'].keys()
	record['col_name'] = name
	record['col_type'] = column['type']
	for key in keys:
		
		if key in column or key in ref_fields:
			if key in ref_fields:
				if ref_fields[key] in column:
					record[key] = column[ref_fields[key]]
			else:
				if key in ('context','domain','selections','relatedy'):
					record[key] = '%s ' % (column[key],)
				else:
					if key == 'size' and type(column[key]) == tuple:
						record[key] = column[key][0]
						record['precision'] = column[key][1]
					else:
						record[key] = column[key]
	
	return record		

def _loadMetaInheritColumns(cr,pool,uid,registry,name,column):
	record = {}
	ref_fields = {'col_name':'name','col_check':'check','col_unique':'unique','col_default':'default','col_family':'family'}
	keys = pool.get('bc.inherit.columns').modelInfo()['columns'].keys()
	record['col_name'] = name
	record['col_type'] = column['type']
	for key in keys:
		
		if key in column or key in ref_fields:
			if key in ref_fields:
				if ref_fields[key] in column:
					record[key] = column[ref_fields[key]]
			else:
				if key in ('context','filtering','domain','selections'):
					record[key] = '%s ' % (column[key],)
				else:
					if key == 'size' and type(column[key]) == tuple:
						record[key] = column[key][0]
						record['precision'] = column[key][1]
					else:
						record[key] = column[key]
	
	return record		


	
def _loadMetaData(cr,pool,uid,name,registry):
	
	models = registry._modules[name]['lom']
	meta = registry._modules[name]['meta']

	record = _loadMetaModule(cr,pool,uid,name,registry)
	return pool.get('bc.modules').create(cr,pool,uid,record)


def _load_env_column(cr,pool,uid,model,column):
	v = {}
	m = pool.get(model)
	obj = pool.get(m.columnsInfo([column],['obj'])[column]['obj'])
	recname = obj._getRecNameName()
	r = obj.select(cr,pool,uid,[recname])
	for k in r:
		v[k[recname]] = k['id']
	
	return v

def _load_class_bc(cr,pool,uid,name):
	bc_models = pool.get('bc.models').select(cr,pool,uid,['name','module_id'],[('module_id','=','bc'),[('name','=','bc.models')]])
	models = pool.get('bc.models').select(cr,pool,uid,['name','module_id'],[('module_id','=',name)])
	mt = {}
	bcm = pool.get('bc.models')
	mod_records = []
	for model in models:
		m = pool.get(model['name'])
		if isinstance(m,ModelInherit):
			continue
		if 'env-fields' in bcm._extra:
			envfields = bcm._extra['env-fields']
			for envfield in envfields:
				mt[envfield] = _load_env_column(cr,pool,uid,bcm._name,envfield)

			mod_record = {'id':model['id']}
			for envfield in envfields:
				ef = getattr(m,'_' + envfield,None)
				if ef:
					mod_record[envfield] = mt[envfield][ef]
			
			mod_records.append(mod_record)
	
	bcm.write(cr,pool,uid,mod_records)
			
def _load_env(cr,pool,uid,name):
	models = pool.get('bc.models').select(cr,pool,uid,['name','module_id'],[('module_id','=',name)])
	mt = {}
	for model in models:
		m = pool.get(model['name'])
		if isinstance(m,ModelInherit) or m._name == 'bc.models':
			continue
		if 'env-fields' in m._extra:
			envfields = m._extra['env-fields']
			for envfield in envfields:
				mt[envfield] = _load_env_column(cr,pool,uid,m._name,envfield)

			r1 = m.select(cr,pool,uid,[m._getRecNameName()])
			mod_records = []
			for k1 in r1:
				mod_record = {'id':k1['id']}
				for envfield in envfields:
					ef = getattr(m,'_' + envfield,None)
					if ef:
						mod_record[envfield] = mt[envfield][ef]
				mod_records.append(mod_record)
			
			m.write(cr,pool,uid,mod_records)

	_load_class_bc(cr,pool,uid,name)

def _loadFiles(cr,pool,uid,name,info):
	pwd = os.getcwd()
	objnames = {'bc.module.files':'filename','bc.modules':'code'}
	metas={'env':info['meta']['env'],'view':info['meta']['view'],'data':info['meta']['data'],'demo':info['meta']['demo'],'test':info['meta']['test']}
	path = info['path']
	for key in metas.keys():
		meta = metas[key]
		for f in meta:
			ext = f.split('.')[-1]
			if ext == 'xml':
				if os.path.exists(opj(path,name,f)):
					_logger.info("loading file: %s" % (opj(path,name,f),))
					_loadXMLFile(cr,pool,uid,info,path,name,f)
					_logger.info("Loaded  file: %s" % (opj(path,name,f),))
				else:
					_logger.critical("Loading  file: %s not found" % (opj(path,name,f),))
			elif ext == 'csv':		
				if os.path.exists(opj(path,name,f)):
					_logger.info("loading file: %s" % (opj(path,name,f),))
					if key == 'test':
						pass
					else:
						_loadCSVFile(cr,pool,uid,info,path,name,f)
					_logger.info("Loaded  file: %s" % (opj(path,name,f),))
				else:
					_logger.critical("Loading  file: %s not found" % (opj(path,name,f),))

def _convertFromYAML(cr,pool,uid,model,records):
	m = pool.get(model)
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
			if columns_info[key]['type'] in ('many2one','related'):
				recname = pool.get(columns_info[key]['obj'])._getRecNameName()
				if recname is None:
					recname = 'id'	
				oid = pool.get(columns_info[key]['obj']).search(cr,pool,uid,[(recname,'=',record[key]),{},1])
				#print('oid:',oid)
				if len(oid) > 0:
					record[key] = oid[0]
			elif columns_info[key]['type'] == 'selection':
				if record[key] and len(record[key]) > 0:
					record[key] = mfs[key][record[key]]
			elif columns_info[key]['type'] == 'one2many':
				_convertFromYAML(cr,pool,uid,columns_info[key]['obj'],record[key])

def _loadCSVFile(cr,pool,uid,info,path,name,fl):
	_buffer = KeyBuffer()
	with open(opj(path,name,fl)) as csvafile:
		areader = csv.DictReader(csvafile)
		if not (areader.fieldnames == ['file','model'] or areader.fieldnames == ['model','file']):
			msg = "Invalid format anotation CSV file: %s\n Must be ['model','file'] or ['file','model']" % (areader.fieldnames,)
			Exception(msg) 
			_logger.critical(msg)

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
					ir = pool.get(model).do_upload_csv(cr,pool,uid,fields,values,context={'FETCH':'LIST'})
					_logger.info("    Loaded annotation file: %s - records:%s" % (opj(path,name,f),len(ir)))

			elif ext == 'yaml':
				with open(opj(path,name,f)) as yamlfile:
					_logger.info("    loading annotation file: %s" % (opj(path,name,f),))
					records = yaml.load(yamlfile,Loader=Loader)					
					#print('records:',records)
					parents = []
					rows = []
					mi = pool.get(model).modelInfo()
					parent_id = mi['names']['parent_id']
					childs_id = mi['names']['childs_id']
					rec_name = mi['names']['rec_name']
					if parent_id and childs_id:
						rows = list(filter(lambda x:x[parent_id] is None,records))
						_convertFromYAML(cr,pool,uid,model,rows)
						while len(rows) > 0:
							ir = pool.get(model).modify(cr,pool,uid,rows,{})
							parents = list(map(lambda x:x[rec_name],rows))
							rows = list(filter(lambda x:parent_id in x and x[parent_id] in parents,records))
							_convertFromYAML(cr,pool,uid,model,rows)
					else:
						_convertFromYAML(cr,pool,uid,model,records)
						ir = pool.get(model).modify(cr,pool,uid,records,{})
					_logger.info("    Loaded annotation file: %s - records:%s" % (opj(path,name,f),len(ir)))

def _loadXMLFile(cr,pool,uid,info,path,name,fl):
	_buffer = KeyBuffer()
	fk = {}
	rng=etree.RelaxNG(etree=etree.parse(opj(os.path.dirname(os.path.abspath(__file__)),'views.rng')))
	obj = 'bc.module.files'
	file_id = pool.get(obj).search(cr=cr,pool=pool,uid=uid,cond=[(pool.get(obj)._getRecNameName(),'=',opj(name,fl))],limit=1)[0]
	for event,el in etree.iterparse(source=opj(path,name,fl),events=('end','start')):
		if el.tag == 'records':
			if event == 'start':
				records = []
				datarecords = []
				model = el.attrib['model']
				modelinfo = pool.get(model).modelInfo()
				columnsinfo = modelinfo['columns']
				columns = list(columnsinfo.keys())
				for column in columns:
					if columnsinfo[column]['type'] == 'selection':
						fkk = {}
						for k,v in columnsinfo[column]['selections']:
							fkk[v] = k
						fk[column] = fkk 
			else:
				ids = pool.get(model).create(cr,pool,uid,records)
				for i in range(len(ids)):
					datarecords[i]['rec_id'] = ids[i]
				pool.get('bc.model.data').create(cr,pool,uid,datarecords)
		elif el.tag == 'record':
			if event == 'start':
				record = {}
				datarecord = {}
			else:
				for key in record.keys():
						column = columnsinfo[key]
						if column['type'] in ('many2one','related'):
							obj = column['obj']
							recname = pool.get(obj)._getRecNameName()

							oid = _buffer.key(key,obj,record[key])
							if not oid:
								if 'ref' in el.attrib:
									oid = pool.get('bc.model.data').select(cr=cr,pool=pool,uid=uid,fields=['rec_id'],cond=[('name','=',el.attrib['ref'])],context= {'FETCH':'LIST'},limit=1)[0]
								else:
									oid = pool.get(obj).search(cr=cr,pool=pool,uid=uid,cond=[(recname,'=',record[key])],context= {'FETCH':'LIST'},limit=1)[0]
									# try:
										# oid = pool.get(obj).search(cr=cr,pool=pool,uid=uid,cond=[(recname,'=',record[key])],context= {'FETCH':'LIST'},limit=1)[0]
									# except:
										# print('RECORD-KEY:',obj,record[key])
									
								
								_buffer.add(key,obj,record[key],oid)

							record[key] = oid
						elif column['type'] in ('selection',):
							record[key] = fk[key][record[key]]

				records.append(record)

				datarecord['name'] = el.attrib['id']
				datarecord['module'] = name
				datarecord['model'] = model
				datarecord['file_id'] = file_id
				#datarecord['file_id'] = pool.get('bc.module.files').search(cr=cr,pool=pool,uid=uid,cond=[(pool.get('bc.module.files')._getRecNameName(),'=',opj(name,fl))],limit=1)[0]
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
						#rec_id = pool.get('bc.model.data').select(cr=cr ,pool=pool, uid=uid, fields=['rec_id'], cond=[('name','=',el.text)])
						#print('el.text:',el.text,rec_id)
						#record[el.attrib['name']] = rec_id[0]['rec_id']
						record[el.attrib['name']] = el.text
					else:
						if 'ref' in el.attrib:
							record[el.attrib['name']] = el.attrib['ref']
						else:
							record[el.attrib['name']] = el.text

def _upgrademoduleslist(cr,pool,uid,registry,db):

	return _load_list_modules(cr,pool,uid,registry,db)
