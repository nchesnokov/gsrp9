import os
import logging
from os.path import join as opj
from .common import concat, _remove_dirs
from gsrp5service.orm.model import Model,ModelInherit

import csv
import yaml
from yaml import Dumper

import web_pdb

from gsrp5service.orm.common import DEFAULT_MODEL_NAMES as DMN

from .generate import * 

#FRAMEWORKS = ('element-plus','vuetify','devextrme')
FRAMEWORKS = ('element-plus',)

_logger = logging.getLogger('listener.' + __name__)


GENTEMPLATES = {'element-plus':gen_template_el,'vuetify':gen_template_vuetify,'devextrme':gen_template_devextrme}
GENSRCIPTS = {'element-plus':gen_script_el,'vuetify':gen_script_vuetify,'devextrme':gen_script_devextrme}
GENSTYLES = {'element-plus':gen_style_el,'vuetify':gen_style_vuetify,'devextrme':gen_style_devextrme}

def ModelsColumns( view, columns):
	res = []
	exclude = EXCLUDE['models'][view]
	for idx,col in enumerate(columns):
		res.append({'seq':idx * 10,'col':col})

	return res

def Views(framework,model,info):
	res = []
	ci = info['columns']
	for view in EXCLUDE['models'].keys():
		columns = isAllow(view,'models',info,list(ci.keys()))
		if len(columns) == 0:
			continue
		standalone = False
		record = {'model':info['name'],'vtype':framework + '/' + view,'cols':ModelsColumns(view,columns)}
		if standalone:	
			record['standalone'] = standalone
			record['template'] = GENTEMPLATES[framework][view](info,columns)
			record['script'] = GENSRCIPTS[framework][view](info,columns)
			record['style'] = GENSTYLES[framework][view](info,columns)
			record['sfc'] = record['template'] +'\n' + record['script'] if len(record['script']) > 0 else '' + record['setup'] if len(record['setup']) > 0 else '' + '\n' + record['style']
		
		res.append(record)

	return res

def iViews(framework, imodel, info, model, icolumns,views):
	res = []
	icolumns_info = info['columns']
	for view in views:
		exclude = EXCLUDE['models'][view]
		for icolumn in icolumns:
			if icolumns_info[icolumn]['type'] not in exclude:
				res.append({'view_id':model + '/' + framework + '/' + view,'col':icolumn})  

	return res

def Area(self, modules = None,context={}):
	pwd = os.getcwd()
	pool = self._models
	registry = self._registry
	if not modules:
		modules = registry._depends
	else:
		modules = list(filter(lambda x: x in modules,registry._depends))
	logmodules = []
	for module in modules:
		path = registry._modules[module]['path']
		objs = {}
		iobjs = {}
		if module in registry._metas:
			for cat in filter(lambda x: x in ('models',),registry._metas[module].keys()):
				for key in registry._metas[module][cat]:
					obj = registry._create_module_object(cat,key,module)
					if isinstance(obj,Model):
						objs.setdefault(cat,[]).append(obj)
					elif isinstance(obj,ModelInherit):
						if hasattr(obj,'_inherit') and getattr(obj,'_inherit',None):
							iobjs.setdefault(cat,[]).append(obj)
		
		if len(objs) + len(iobjs) > 0:
			if len(objs) > 0:
				#_remove_dirs(opj(path,module,'views'))
				fmode = 'w'
				a = open(opj(path,module,'views','views.csv'),fmode)
				if fmode == 'w':
					aw = csv.DictWriter(a,['model','file'])
					aw.writeheader()
					for framework in FRAMEWORKS:
						if os.path.exists(opj(path,module,'views',framework)):
							_remove_dirs(opj(path,module,'views',framework))

				for framework in FRAMEWORKS:
					if not os.path.exists(opj(path,module,'views',framework)):
						os.mkdir(opj(path,module,'views',framework))
					for model in objs['models']:	
						with open(opj(path,module,'views',framework,model._table+'.yaml'),'w') as outfile:
							yaml.dump(Views(framework,model._name,model.modelInfo()), outfile, Dumper, default_flow_style=False)
					
						aw.writerow({'model': 'bc.ui.model.views','file':opj('views',framework,model._table+'.yaml' )})
			if len(iobjs) > 0:
				if len(objs) == 0:
					a = open(opj(path,module,'views','views.csv'),'w')
					aw = csv.DictWriter(a,['model','file'])
					aw.writeheader()
					for framework in FRAMEWORKS:
						_remove_dirs(opj(path,module,'inherits',framework))

				if not os.path.exists(opj(path,module,'views','inherits')):
					os.mkdir(opj(path,module,'views','inherits'))
				
				for framework in FRAMEWORKS:
					if not os.path.exists(opj(path,module,'views','inherits',framework)):
						os.mkdir(opj(path,module,'views','inherits',framework))
					for imodel in iobjs['models']:	
						inherit = getattr(imodel,'_inherit')
						for m in inherit.keys():
							if '_columns' in inherit[m]:
								cols =  inherit[m]['_columns']
								nm = m + '.' +imodel._name
								views = []
								mobj = registry._create_module_object('models',m,registry._getLastModuleObject('models',m))
								info = mobj.modelInfo()
								ci = info['columns']
								for view in EXCLUDE['models'].keys():
									columns = isAllow(view,'models',info,list(ci.keys()))
									if len(columns) == 0:
										continue
									views.append(view)
								with open(opj(path,module,'views','inherits',framework,nm.replace('.','_') + '.yaml'),'w') as outfile:
									yaml.dump(iViews(framework,imodel._name,imodel.imodelInfo(),m,cols,views), outfile, Dumper, default_flow_style=False)
					
							aw.writerow({'model': 'bc.ui.model.view.column.inherits','file':opj('views','inherits',framework,nm.replace('.','_') + '.yaml' )})
				
			logmodules.append(module)
	_logger.info('Gen views of modules %s' % (logmodules,))
	return ['Gen views of modules %s' % (logmodules,)]

def isAllowDashboards(view,info):
	r = False
	return r

def isAllowModels(view,info,columns):
	res = []
	ci = info['columns']
	if 	not (view == 'search' and (info['names']['row_name'] or info['names']['rec_name'] or info['names']['full_name']) or view == 'find' and len(list(filter(lambda x: 'selectable' in ci[x] and ci[x]['selectable'],ci.keys()))) > 0 or view in ('form','list','m2mlist','form.modal') or view == 'tree' and info['names']['parent_id'] and  info['names']['childs_id'] or view in ('calendar','graph','mdx') and info['names']['date'] or view == 'schedule' and (info['names']['from_date'] and info['names']['to_date'] or info['names']['start_date'] and info['names']['end_date']) or view == 'kanban' and info['names']['state'] or view == 'geo' and (info['names']['from_latitude'] and info['names']['from_longitude'] or info['names']['to_latitude'] and info['names']['to_longitude'] or info['names']['latitude'] and info['names']['longitude']) or view == 'flow' and  info['names']['prev_name'] and info['names']['next_name']):
		return res
	
	for col in columns:
		if len(EXCLUDE['models'][view]) == 0 or ci[col]['type'] not in EXCLUDE['models'][view] and ci[col]['type'] not in ('iProperty',):
				res.append(col)
	
	return res

def isAllowIModels(view,info,columns):
	res = []
	ci = info['columns']
		
	for col in columns:
		if len(EXCLUDE['models'][view]) == 0 or ci[col]['type'] not in EXCLUDE['models'][view] and ci[col]['type'] not in ('iProperty',):
			res.append(col)
	
	return res


def isAllowViews(view,info,columns):
	r = False
	return r

def isAllowReports(view,info,columns):
	r = False
	return r

def isAllowWizards(view,info,columns):
	r = False
	return r

ISALLOW_OBJS = {'dashboards':isAllowDashboards,'models': isAllowModels,'imodels': isAllowIModels,'views':isAllowViews,'reports':isAllowReports,'wizards':isAllowWizards}

def isAllow(view,cat,info,columns):
	r = False
	if cat in ISALLOW_OBJS:
		r = ISALLOW_OBJS[cat](view,info,columns)
	
	return r

def isAllowInherit(view,cat,columnsinfo):
	r = False
	if cat in ISALLOW_OBJS:
		r = ISALLOW_OBJS[cat](view,columnsinfo)
	
	return r



EXCLUDE = {}
EXCLUDE['models'] = {'calendar':['one2many','one2related','many2many','text','binary','xml','json'],'form':[],'form.modal':[],'schedule':['one2many','one2related','many2many','text','binary','xml','json'],'gantt':['one2many','one2related','many2many','text','binary','xml','json'],'graph':['one2many','one2related','many2many','text','binary','xml','json'],'kanban':['one2many','one2related','many2many','xml','json'],'list':['many2many','text','binary','xml','json'],'m2mlist':['one2many','one2related','many2many','text','binary','xml','json'],'mdx':['one2many','one2related','many2many','text','binary','xml','json'],'matrix':['one2many','one2related','many2many','text','binary','xml','json'],'search':['one2many','one2related','many2many','text','binary','xml','json'],'find':['one2many','one2related','many2many','text','binary','xml','json'],'tree':['one2many','one2related','many2many','text','binary','xml','json'],'geo':['one2many','one2related','many2many','text','binary','xml','json'],'flow':['integer','float','real','decimal','numeric','date','time','datetime','one2related','many2many','text','binary','xml','json']}


