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

# download

def _download_imodules(cr,pool,uid,path,module,imodules,registry,ext='csv'):
	for k in imodules.keys():
		a = open(opj(path,module,'demo','annotation-1.csv'),'a')
		aw = csv.DictWriter(a,['model','file'])
		for model in imodules[k].keys():	
			fields = imodules[k][model]['fields']
			c2 = imodules[k][model]['sf']
			m = pool.get(model)
			columns_info = m.columnsInfo(attributes=['type','selections','timezone'])
			sfs = list(filter(lambda x: x in c2,m._selectionfields))
			sfs2 = list(filter(lambda x: x in fields,m._selectionfields))
			mfs = {}
			cond = []
			for sf in sfs:
				sls = tuple(map(lambda x: x[0],registry._getMetaOfModulesModel(model,module)['attrs']['_columns'][sf].selections))
				cond.append((sf,'in',sls))
			
			for sf2 in sfs2:				
				for k2,v2 in tuple(map(lambda x: x[0],registry._getMetaOfModulesModel(model,module)['attrs']['_columns'][sf2].selections)):
				#for k2,v2 in columns_info[sf2]['selections']:
					mfs.setdefault(sf2,{})[k2] = v2 

			records = m.select(cr,pool,uid,fields,cond)
			if len(records) > 0:
				if m._name[:3] == 'md.':
					c = 'data'
				else:
					c = 'examples' 
	
				_logger.info('GenExamples write file: %s' % (opj(path,module,'demo',c,m._table+'_'+k+'.' + ext),));
				am = open(opj(path,module,'demo',c,m._table+'_'+k+'.' + ext),'w')
				print('MFS:',mfs)
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


def _download(cr,pool,uid,path,module,imodules,models,registry,ext='csv'):
	a = open(opj(path,module,'demo','annotation-1.csv'),'w')
	aw = csv.DictWriter(a,['model','file'])
	aw.writeheader()
	for model in models.keys():
		fields = models[model]
		m = pool.get(model)
		columns_info = m.columnsInfo(attributes=['type','selections','timezone'])
		sfs = list(filter(lambda x: x in fields,m._selectionfields))
		mfs = {}
		cond = []
		for sf in sfs:
			sls = tuple(map(lambda x: x[0],registry._getMetaOfModulesModel(model,module)['attrs']['_columns'][sf].selections))
			cond.append((sf,'in',sls))
			for k,v in columns_info[sf]['selections']:
				mfs.setdefault(sf,{})[k] = v 
		records = m.select(cr,pool,uid,fields,cond)
		if len(records) > 0:
			if m._name[:3] == 'md.':
				c = 'data'
			else:
				c = 'examples' 

			_logger.info('GenExamples write file: %s' % (opj(path,module,'demo',c,m._table+'.' + ext),));
			am = open(opj(path,module,'demo',c,m._table+'.' + ext),'w')
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
				with open(opj(path,module,'demo',c,m._table+'.yaml'),'w') as outfile:
					yaml.dump(records, outfile, Dumper=Dumper, default_flow_style=False)
			
			aw.writerow({'model':m._name,'file':opj('demo',c,m._table+'.' + ext)})
	a.close()
	_download_imodules(cr,pool,uid,path,module,imodules,registry,ext)
# download

def Area(cr, pool, uid, registry, modules = None, context={}):
	pwd = os.getcwd()
	if not modules:
		modules = registry._depends
	else:
		modules = list(filter(lambda x: x in modules,registry._depends))
	logmodules = []
	print('MODULES:',modules)
	if 'ext' not in context:
		context['ext'] = 'yaml'
	for module in filter(lambda x: not x in ('bc','system') and 'state' in registry._modules[x] and registry._modules[x]['state'] == 'I',modules):
		path = registry._modules[module]['path']
		imodules = {}
		models = {}
		for model in registry._momm[module].keys():
			#print('MODULES:',model,registry._getModulesOfModel(model),registry._momm[module][model])
			meta = registry._getMetaOfModulesModel(model,registry._getFirstModule(model))
			#print('META:',meta)
			if issubclass(type(meta['name'],meta['bases'],meta['attrs']),ModelInherit):
				if '_inherit' in meta['attrs'] and meta['attrs']['_inherit']:
					inherit = meta['attrs']['_inherit']
					for k in inherit.keys():
						if '_columns' in inherit[k]:
							mi = pool.get(k)
							m = pool.get(model)
							ci = m.columnsInfo(inherit[k]['_columns'],['type'])
							ici = meta['attrs']['_columns']
							c = list(filter(lambda x:  x in mi._storefields and ci[x]['type'] not in ('one2many','many2many','referenced') and ici[x]._type != 'iSelection',inherit[k]['_columns']))
							c1 = list(filter(lambda x: ici[x]._type == 'iSelection',inherit[k]['_columns']))
							#print('SF:',c,c1)
							if len(c) > 0 or len(c1) > 0:
								if len(c) > 0:
									models.setdefault(k,[]).extend(c)
								if len(c1) > 0:
									#fm = registry._getFirstModule(k)
									#lm = registry._getLastModule(k)
									#imodules.setdefault(fm,{})[k] = {'sf':c1,'fields':list(registry._getMetaOfModulesModel(k,fm)['attrs']['_columns'].keys())}
									imodules.setdefault(module,{})[k] = {'sf':c1,'fields':list(registry._getMetaOfModulesModel(k,module)['attrs']['_columns'].keys())}

			else:
				if registry._getFirstModule(model) == module:
					m = pool.get(model)
					columns_info = m.columnsInfo(attributes=['type','selections','timezone'])
					#print('AREA:',module,model)
					fmc = list(meta['attrs']['_columns'].keys())
					fields = ['id']
					fields.extend(list(filter(lambda x: x in fmc and columns_info[x]['type'] not in ('one2many','many2many','referenced','iSelection'),m._storefields)))
					models.setdefault(model,[]).extend(fields)

		if len(models) > 0 or len(imodules) > 0:
			print('MODELS:',module,imodules,models)
			_download(cr,pool,uid,path,module,imodules,models,registry,ext=context['ext'])
			logmodules.append(module)

	_logger.info('Download examples of modules %s' % (logmodules,))
	
	return ['Download examples of modules %s' % (logmodules,)]


