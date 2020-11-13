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

def _download_imodules(self,path,module,imodels,registry,ext='csv'):
	afile = opj(path,module,'demo','annotation-1.csv')
	if  os.path.exists(afile):
		a = open(opj(path,module,'demo','annotation-1.csv'),'a')
	else:
		a = open(opj(path,module,'demo','annotation-1.csv'),'w')
		aw = csv.DictWriter(a,['model','file'])
		aw.writeheader()
	aw = csv.DictWriter(a,['model','file'])
	for model in imodels.keys():	
		m = imodels[model]['model']
		fields = imodels[model]['columns']
		columns_info = m.columnsInfo(columns=fields,attributes=['type','selections'])
		mfs = {}
		for field in fields:
			if columns_info[field]['type'] == 'selection':
				for x,y in columns_info[field]['selections']:
					mfs.setdefault(field,{})[x] = y

		records = m.select(fields,[])
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


def _download(self,path,module,models,registry,ext='csv'):
	#pool = self._pool
	#pool = models
	_remove_dirs([opj(path,module,'demo','data'),opj(path,module,'demo','examples'),opj(path,module,'demo','cust'),])
	
	a = open(opj(path,module,'demo','annotation-1.csv'),'w')
	aw = csv.DictWriter(a,['model','file'])
	aw.writeheader()
	for key in models.keys():
		model = models[key]
		fields = model._rowfields
		columns_info = model.columnsInfo(columns=fields,attributes=['type','selections'])
		mfs = {}
		for field in fields:
			if columns_info[field]['type'] == 'selection':
				for x,y in columns_info[field]['selections']:
					mfs.setdefault(field,{})[x] = y
		
		records = model.select(fields,[])
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
		if module in registry._metas and 'models' in registry._metas[module]:
			for key in registry._metas[module]['models'].keys():
				mm = self._models[key]
				if isinstance(mm,Model):
					models[key] = mm

		if module in self._registry._inherit:
			#web_pdb.set_trace()
			imodels_module = self._registry._inherit[module]['models']
			for imodel_module in imodels_module.keys():
				im = registry._create_module_object('models',imodel_module,module)
				for mkey in imodels_module[imodel_module].keys():
					last_module = registry._getLastModuleObject('models',mkey)
					imm = registry._create_module_object('models',mkey,last_module)
					for col in imodels_module[imodel_module][mkey]['_columns']:
						if  im._columns[col]._type not in ('one2many','many2many','iProperty') :
							imodels.setdefault(mkey,{}).setdefault('columns',[]).append(col)
					if mkey in imodels:
						imodels.setdefault(mkey,{})['model'] = imm				

		if len(models) > 0 or len(imodels) > 0:
			print('MODELS:',module,models,imodels)
			_download(self,path,module,models,registry,ext=context['ext'])
			_download_imodules(self,path,module,imodels,registry,ext=context['ext'])
			logmodules.append(module)

	_logger.info('Download examples of modules %s' % (logmodules,))
	
	return ['Download examples of modules %s' % (logmodules,)]


