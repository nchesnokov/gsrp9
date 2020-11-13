import os
import logging
from os.path import join as opj
import csv
import yaml

import datetime
from datetime import date,time,datetime

from gsrp5service.orm.model import Model

_logger = logging.getLogger('listener.' + __name__)

def _download_csv(cr,pool,uid,path,module,models):
	a = open(opj(path,module,'examples','annotation-1.csv'),'w')
	aw = csv.DictWriter(a,['model','file'])
	aw.writeheader()
	for model in models:
		m = pool.get(model)
		columns_info = m.columnsInfo(attributes=['type','selections','timezone'])
		fields = list(filter(lambda x: not columns_info[x]['type'] in ('one2many','many2many','referenced'),m._storefields))
		sfs = list(filter(lambda x: x in fields,m._selectionfields))
		mfs = {}
		for sf in sfs:
			for k,v in columns_info[sf]['selections']:
				mfs.setdefault(sf,{})[k] = v 
		records = m.select(cr,pool,uid,fields)
		if len(records) > 0:
			#print('FILE:',opj(path,module,'examples',m._table+'.csv'))
			_logger.info('GenExamples write file: %s' % (opj(path,module,'examples',m._table+'.csv'),));
			am = open(opj(path,module,'examples',m._table+'.csv'),'w')
			amw = csv.DictWriter(am,fields)
			amw.writeheader()
			for record in records:
				row = {}
				for key in filter(lambda x: x != 'id',record.keys()):
					row[key] = record[key]
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
						if not row[key] is None:
							if columns_info[key]['timezone']:
								row[key] = row[key].strftime('%Y-%m-%d %H:%M:%S%z')
							else:
								row[key] = row[key].strftime('%Y-%m-%d %H:%M:%S')					
					elif columns_info[key]['type'] == 'date':
						if not row[key] is None:
							row[key] = row[key].strftime('%Y-%m-%d')
					elif columns_info[key]['type'] == 'time':
						if not row[key] is None:
							if columns_info[key]['timezone']:
								row[key] = row[key].strftime('%H:%M:%S%z')
							else:
								row[key] = row[key].strpfime('%H:%M:%S')

				amw.writerow(row)
			am.close()
			aw.writerow({'model':m._name,'file':opj('examples',m._table+'.csv')})
	a.close()

def _buildFields(cr,pool,uid,model,lm):
	#print('LM:',lm)
	res = []
	m = pool.get(model)
	fields = m._storefields + m._o2mfields
	ci = pool.get(model).columnsInfo()
	f = []
	for field in fields:
		if ci[field]['type'] == 'one2many' and field != pool.get(model)._getChildsIdName():
			obj = ci[field]['obj']
			if obj in lm:
				r = _buildFields(cr,pool,uid,obj,lm)
				f.append({field:r})
		else:
			f.append(field)

	return f

def _convertToYAML(cr,pool,uid,model,records,rel=None):
	
	m = pool.get(model)
	
	columns_info = m.columnsInfo(attributes=['type','selections','timezone','obj','rel'])
	fields = m._storefields + m._o2mfields
	sfs = list(filter(lambda x: x in fields,m._selectionfields))
	mfs = {}
	for sf in sfs:
		for k,v in columns_info[sf]['selections']:
			mfs.setdefault(sf,{})[k] = v 
	#print('mfs:',mfs)
	rows = []
	if len(records) > 0:
		for record in records:
			row = {}
			for key in filter(lambda x: x != 'id' and not (rel and x == rel),record.keys()):
				row[key] = record[key]
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
				elif columns_info[key]['type'] == 'one2many':
					row[key] = _convertToYAML(cr,pool,uid,columns_info[key]['obj'],row[key],columns_info[key]['rel'])
			
			rows.append(row)
		
	return rows


def _download_yaml(cr,pool,uid,path,module,models):
	a = open(opj(path,module,'tests','annotation-1.csv'),'w')
	aw = csv.DictWriter(a,['model','file'])
	aw.writeheader()
	for model in models:
		m = pool.get(model)
		if m._name in m._schema and m._schema[m._name] is None:
			fields = _buildFields(cr,pool,uid,model,set(m._schema))
			#print('fields:',model,fields)
			records = m.select(cr,pool,uid,fields)
			#print('records:',records)
			rows = _convertToYAML(cr,pool,uid,model,records)
			if len(rows) > 0:
				aw.writerow({'model':m._name,'file':opj('tests',m._table+'.yaml')})
		
				with open(opj(path,module,'tests',m._table+'.yaml'),'w') as outfile:
					yaml.dump(rows, outfile, default_flow_style=False)
				
				_logger.info('GenTests write file: %s records: %s' % (opj(path,module,'tests',m._table+'.yaml'),len(rows)));
	a.close()

def Area(cr, pool, uid, registry, modules = None):
	pwd = os.getcwd()
	if not modules:
		modules = registry._depends
	else:
		modules = list(filter(lambda x: x in modules,registry._depends))
	logmodules = []
	for module in filter(lambda x: not x in ('bc','md','system') and 'state' in registry._modules[x] and registry._modules[x]['state'] == 'I',modules):
		path = registry._modules[module]['path']
		models = []
		#print('EXAMPLES MODULE:',module,registry._modules[module]['lom'])
		for model in registry._modules[module]['lom']:
			#print('EXAMPLES MODULE MODEL:',module,model)
			#if module=='srm_ru':
				#print('INHERIT:',model,registry._models[model]._inherit is None,registry._models[model]._inherit)
			if model in registry._models and registry._models[model]._inherit is None:
				models.append(model)
		#print('MODELS:',models)
		if len(models) > 0:
			#print('MODULE:',module)
			_download_yaml(cr,pool,uid,path,module,models)
			logmodules.append(module)
	_logger.info('Download tests of modules %s' % (logmodules,))
	
	return ['Download tests of modules %s' % (logmodules,)]


