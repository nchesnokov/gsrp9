import os
import logging
from os.path import join as opj
import csv
import yaml
from yaml import Dumper

import datetime
from datetime import date,time,datetime
from gsrp5service.orm.model import Model, ModelInherit

import web_pdb

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

def _download_imodules(self,path,module,imodules,models,imodels,registry,ext='csv'):
	pool = self._pool
	#pool = models
	#web_pdb.set_trace()
	for k in imodules.keys():
		a = open(opj(path,module,'demo','annotation-1.csv'),'w')
		aw = csv.DictWriter(a,['model','file'])
		aw.writeheader()
		aw = csv.DictWriter(a,['model','file'])
		for model in imodules[k].keys():	
			fields = imodules[k][model]['_columns']
			imodules[k][model]['sf'] = []
			imodules[k][model]['vcl'] = []
			for field in fields:
				imodel = imodules[k][model]['_imodel']
				im = imodels[imodel]
				if  im._columns[field]._type == 'iProperty' and hasattr(im._columns[field],'selections'):
					for ks,kn in im._columns[field].selections:
						imodules[k][model]['sf'].append(ks)
						imodules[k][model]['vcl'].append(ks)
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
			records = m.select(fields,cond)
			if len(records) > 0:
				if m._class_model == 'A':
					if m._name[:3] == 'md.':
						c = 'data'
					else:
						c = 'examples' 
				elif m._class_model == 'C':
					c = 'cust'
	
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


def _download(self,path,module,imodules,models,imodels,registry,ext='csv'):
	pool = self._pool
	#pool = models
	_remove_dirs([opj(path,module,'demo','data'),opj(path,module,'demo','examples'),opj(path,module,'demo','cust'),])
	
	a = open(opj(path,module,'demo','annotation-1.csv'),'w')
	aw = csv.DictWriter(a,['model','file'])
	aw.writeheader()
	for model in models:
		fields = model._rowfields
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
		records = model.select(fields,cond)
		if len(records) >= 0:
			if model._class_model == 'A':
				if model._name[:3] == 'md.':
					c = 'data'
				else:
					c = 'examples' 
			elif model._class_model == 'C':
				c = 'cust'

			_logger.info('GenExamples write file: %s - records:%s'  % (opj(path,module,'demo',c,model._table+'.' + ext),len(records)));
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

def Area(self, modules = None, context={}):
	pwd = os.getcwd()
	pool = self._pool
	registry = self._registry
	if not modules:
		modules = registry._depends
	else:
		modules = list(filter(lambda x: x in modules,registry._depends))
	logmodules = []
	if 'ext' not in context:
		context['ext'] = 'yaml'
	for module in filter(lambda x: not x in ('bc','system') and 'state' in registry._modules[x] and registry._modules[x]['state'] == 'I',modules):
		path = registry._modules[module]['path']
		imodules = {}
		models = {}
		imodels = {}
		module_models = registry._modules[module]['lom']
		for model in module_models:
			if model in pool:
				if type(pool[model]) == dict:
					mm = registry._create_model(model)
				else:
					mm = pool[model]
				if isinstance(mm,Model):
					models[model] = mm
			else:
				if module in self._registry._inherit:
					imodels_module = self._registry._inherit[module]
					for imodel_module in imodels_module.keys():
						for mkey in imodels_module[imodel_module].keys():
							if '_columns' in imodels_module[imodel_module][mkey]:
								for col in imodels_module[imodel_module][mkey]['_columns']:
									first_module = registry._getFirstModuleModel(mkey)
									imodules.setdefault(first_module,{}).setdefault(mkey,{})['_columns'] = imodels_module[imodel_module][mkey]['_columns']
									imodules.setdefault(first_module,{}).setdefault(mkey,{})['_imodel'] = model
									imm = registry._create_model(model)
									if isinstance(imm,ModelInherit):
										imodels[model] = imm
									

		if len(models) > 0 or len(imodules) > 0:
			print('MODELS:',module,imodules,models,imodels)
			_download_imodules(self,path,module,imodules,models,imodels,registry,ext=context['ext'])
			_download(self,path,module,imodules,models,imodels,registry,ext=context['ext'])
			logmodules.append(module)

	_logger.info('Download examples of modules %s' % (logmodules,))
	
	return ['Download examples of modules %s' % (logmodules,)]


