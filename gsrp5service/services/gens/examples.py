import os
import logging
from os.path import join as opj
import csv
import yaml
from yaml import Dumper

import datetime
from datetime import date,time,datetime
from gsrp5service.orm.model import Model, ModelInherit

_logger = logging.getLogger('listener.' + __name__)


def _remove_dirs(folders):
	import os, shutil
	if type(folders) == str:
		folders = [folders]
	for folder in folders: 
		for filename in os.listdir(folder):
			file_path = os.path.join(folder, filename)
			try:
				if os.path.isfile(file_path) or os.path.islink(file_path):
					os.unlink(file_path)
				elif os.path.isdir(file_path):
					shutil.rmtree(file_path)
			except Exception as e:
				print('Failed to delete %s. Reason: %s' % (file_path, e))
# download

def _download_imodules(cr,pool,uid,path,module,imodules,registry,ext='csv'):
	for k in imodules.keys():
		a = open(opj(path,module,'demo','annotation-1.csv'),'w')
		aw = csv.DictWriter(a,['model','file'])
		aw.writeheader()
		aw = csv.DictWriter(a,['model','file'])
		for model in imodules[k].keys():	
			fields = imodules[k][model]['fields']
			c2 = imodules[k][model]['sf']
			vcl = imodules[k][model]['vcl']
			m = pool.get(model)
			columns_info = m.columnsInfo(attributes=['type','selections','timezone'])
			sfs = list(filter(lambda x: x in c2,m._selectionfields))
			sfs2 = list(filter(lambda x: x in fields,m._selectionfields))
			mfs = {}
			cond = []
			for sf in sfs:
				sls = tuple(filter(lambda y: y in vcl[sf],map(lambda x: x[0],registry._getMetaOfModulesModel(model,module)['attrs']['_columns'][sf].selections)))
				cond.append((sf,'in',sls))
			
			for sf2 in sfs2:				
				for k2,v2 in registry._getMetaOfModulesModel(model,module)['attrs']['_columns'][sf2].selections:
				#for k2,v2 in columns_info[sf2]['selections']:
					mfs.setdefault(sf2,{})[k2] = v2 

			#print('COND:',cond)
			records = m.select(cr,pool,uid,fields,cond)
			if len(records) > 0:
				if m._name[:3] == 'md.':
					c = 'data'
				else:
					c = 'examples' 
	
				_logger.info('GenExamples write file: %s' % (opj(path,module,'demo',c,m._table+'_'+k+'.' + ext),));
				am = open(opj(path,module,'demo',c,m._table+'_'+k+'.' + ext),'w')
				#print('MFS:',mfs)
				for row in records:
					for key in row.keys():
						if key == 'id':
							continue
						if columns_info[key]['type'] in ('many2one','related'):
							if 'name' in row[key] and row[key]['name'] and len(row[key]['name']) > 0:
								row[key] = row[key]['name']
							else:
								row[key] = row[key]['id']
						elif columns_info[key]['type'] == 'selection':
							if row[key] and len(row[key]) > 0:
								row[key] = mfs[key][row[key]]
							else:
								row[key] = ''
						elif columns_info[key]['type'] == 'datetime':
							if row[key] is not None and ext == 'csv' and type(row[key]) == datetime.datetime:
								if columns_info[key]['timezone']:
									row[key] = row[key].strftime('%Y-%m-%d %H:%M:%S%z')
								else:
									row[key] = row[key].strftime('%Y-%m-%d %H:%M:%S')					
						elif columns_info[key]['type'] == 'date':
							if row[key] is not None  and ext == 'csv' and type(row[key]) == datetime.date:
								row[key] = row[key].strftime('%Y-%m-%d')
						elif columns_info[key]['type'] == 'time' and ext == 'csv':
							if row[key] is not None and ext == 'csv' and type(row[key]) == datetime.datetime:
								if columns_info[key]['timezone']:
									row[key] = row[key].strftime('%H:%M:%S%z')
								else:
									row[key] = row[key].strpfime('%H:%M:%S')
								
				if ext == 'csv':
					amw = csv.DictWriter(am,fields)
					amw.writeheader()
					amw.writerows(records)
					am.close()
				elif ext == 'yaml':
					with open(opj(path,module,'demo',c,m._table+'_'+k+'.yaml'),'w') as outfile:
						yaml.dump(records, outfile, Dumper, default_flow_style=False)
				
				aw.writerow({'model':m._name,'file':opj('demo',c,m._table+'_'+k+'.' + ext)})
		a.close()


def _download(cr,pool,uid,path,module,imodules,models,imodels,registry,ext='csv'):
	_remove_dirs([opj(path,module,'demo','data'),opj(path,module,'demo','examples'),opj(path,module,'demo','cust'),])
	
	a = open(opj(path,module,'demo','annotation-1.csv'),'w')
	aw = csv.DictWriter(a,['model','file'])
	aw.writeheader()
	for model in models:
		fields = list(model._columns.keys())
		columns_info = model.columnsInfo(attributes=['type','selections','timezone'])
		sfs = list(filter(lambda x: x in fields,model._selectionfields))
		mfs = {}
		cond = []
		for sf in sfs:
			sls = tuple(map(lambda x: x[0],registry._models[model._name]['attrs']['_columns'][sf].selections))
			cond.append((sf,'in',sls))
			#print('COND:',model._name,cond)
			for k,v in columns_info[sf]['selections']:
				mfs.setdefault(sf,{})[k] = v 
		records = model.select(cr,pool,uid,fields,cond)
		if len(records) >= 0:
			if model._class_model == 'C':
				c = 'cust'
			else:
				if model._name[:3] == 'md.':
					c = 'data'
				else:
					c = 'examples' 

			_logger.info('GenExamples write file: %s' % (opj(path,module,'demo',c,model._table+'.' + ext),));
			am = open(opj(path,module,'demo',c,model._table+'.' + ext),'w')
			for row in records:
				for key in row.keys():
					if key == 'id':
						continue
					if columns_info[key]['type'] in ('many2one','related'):
						if 'name' in row[key] and row[key]['name'] and len(row[key]['name']) > 0:
							row[key] = row[key]['name']
						else:
							row[key] = row[key]['id']
					elif columns_info[key]['type'] == 'selection':
						if row[key] and len(row[key]) > 0:
							row[key] = mfs[key][row[key]]
						else:
							row[key] = ''
					elif columns_info[key]['type'] == 'datetime':
						if row[key] is not None and ext == 'csv' and type(row[key]) == datetime.datetime:
							if columns_info[key]['timezone']:
								row[key] = row[key].strftime('%Y-%m-%d %H:%M:%S%z')
							else:
								row[key] = row[key].strftime('%Y-%m-%d %H:%M:%S')					
					elif columns_info[key]['type'] == 'date':
						if row[key] is not None  and ext == 'csv' and type(row[key]) == datetime.date:
							row[key] = row[key].strftime('%Y-%m-%d')
					elif columns_info[key]['type'] == 'time' and ext == 'csv':
						if row[key] is not None and ext == 'csv' and type(row[key]) == datetime.datetime:
							if columns_info[key]['timezone']:
								row[key] = row[key].strftime('%H:%M:%S%z')
							else:
								row[key] = row[key].strpfime('%H:%M:%S')
							
			if ext == 'csv':
				amw = csv.DictWriter(am,fields)
				amw.writeheader()
				amw.writerows(records)
				am.close()
			elif ext == 'yaml':
				with open(opj(path,module,'demo',c,model._table+'.yaml'),'w') as outfile:
					yaml.dump(records, outfile, Dumper=Dumper, default_flow_style=False)
			
			aw.writerow({'model':model._name,'file':opj('demo',c,model._table+'.' + ext)})
	a.close()
	#_download_imodules(cr,pool,uid,path,module,imodules,registry,ext)
# download

def Area(cr, pool, uid, registry, modules = None, context={}):
	pwd = os.getcwd()
	if not modules:
		modules = registry._depends
	else:
		modules = list(filter(lambda x: x in modules,registry._depends))
	logmodules = []
	#print('MODULES:',modules)
	if 'ext' not in context:
		context['ext'] = 'yaml'
	for module in filter(lambda x: not x in ('bc','system') and 'state' in registry._modules[x] and registry._modules[x]['state'] == 'I',modules):
		path = registry._modules[module]['path']
		imodules = {}
		models = []
		imodels = []
		module_models = registry._modules[module]['lom']
		#print('MODULE-MODELS:',module_models)
		for model in module_models:
			if model in pool:
				mm = pool[model]
			else:
				mm = registry._create_model(model)
			if isinstance(mm,Model):
				models.append(mm)
			elif isinstance(mm,ModelInherit):
				if hasattr(mm,'_inherit') and getattr(mm,'_inherit',None):
					imodels.append(mm)
					if hasattr(mm,'_inherit'):
						inherit = getattr(mm,'_inherit',None)
						if inherit:
							for k in inherit.keys():
								if '_columns' in inherit[k]:
									first_module = registry._getFirstModule(k)
									imodules.setdefault(first_module,{})[k] = inherit[k]['_columns']


		if len(models) > 0 or len(imodules) > 0:
			#print('MODELS:',module,imodules,models,imodels)
			#_download_imodules(cr,pool,uid,path,module,imodules,registry,ext=context['ext'])
			_download(cr,pool,uid,path,module,imodules,models,imodels,registry,ext=context['ext'])
			logmodules.append(module)

	_logger.info('Download examples of modules %s' % (logmodules,))
	
	return ['Download examples of modules %s' % (logmodules,)]


