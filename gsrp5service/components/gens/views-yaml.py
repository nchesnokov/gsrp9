import os
import logging
from os.path import join as opj
from io import BytesIO
from .common import concat
from gsrp5service.orm.model import Model,ModelInherit

import web_pdb

import yaml

from gsrp5service.orm.common import DEFAULT_MODEL_NAMES as DMN

_logger = logging.getLogger('listener.' + __name__)

def ModelsColumns( view, columns):

	exclude = EXCLUDE['models'][view]
	return list(filter(lambda x: not (columns[x]['type'] in exclude or columns[x]['type'] == 'iProperty',columns.keys())))

def Views(framework,model,info):
	res = []
	columnsinfo = info['columns']
	for view in VIEWSGEN['models'].keys():
		if isAllow(view,obj,info) and len(list(filter(lambda x: not columnsinfo[x]['type'] in EXCLUDE[obj][view] and columnsinfo[x]['type'] != 'iProperty',columns))) > 0:
			res.append({'framework':framework,'model':info['name'],'vtype':view,'cols':ModelsColumns(modelinfo['columns'])})

	return res

def Records(framework,models):
	res = []
	for model in models:
		res.append(Views(framework,model._name,model.modelInfo()))

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
			f=open(opj(path,module,'views','views.yaml'),'wb')
			f.write(yaml.dumps(Records('element-plus',objs['models'])))
			f.close()
			logmodules.append(module)
	_logger.info('Gen views of modules %s' % (logmodules,))
	return ['Gen views of modules %s' % (logmodules,)]

def isAllowDashboards(view,info):
	r = False
	return r

def isAllowModels(view,info):

	r = False

	if view in ('form','list','m2mlist'):
		r = True

	if view in ('search','find','report','custom') and len(list(filter(lambda x: 'selectable' in info['columns'][x] and info['columns'][x]['selectable'],info['columns'].keys()))) > 0 and ('full_name' in info['names'] and info['names']['full_name'] or 'rec_name' in info['names'] and info['names']['rec_name']):
		r = True

	if view == 'tree' and info['names']['parent_id'] and  info['names']['childs_id']:
		r = True

	if view == 'calendar' and info['names']['date']:
			r = True

	if view == 'schedule' and (info['names']['from_date'] and info['names']['to_date'] or info['names']['start_date'] and info['names']['end_date']):
		r = True

	if view == 'gantt' and info['names']['parent_id'] and info['names']['childs_id'] and info['names']['start_date'] and info['names']['end_date']:
		r = True

	if view == 'kanban' and info['names']['state']:
		r = True

	if view == 'graph' and info['names']['date']:
		r = True

	if view == 'mdx' and info['names']['date']:
		r = True

	if view == 'matrix' and ('matrix_names' in info['names'] and info['names']['matrix_names'] and 'matrix_col_name' in info['names']['matrix_names'] and info['names']['matrix_names']['matrix_col_name']  and 'matrix_val_name' in info['names']['matrix_names'] and info['names']['matrix_names']['matrix_val_name'] or ('matrix_col_name' in info['names'] and info['names']['matrix_col_name']  and 'matrix_val_name' in info['names'] and info['names']['matrix_val_name'])):
		r = True


	if view == 'geo' and (info['names']['from_latitude'] and info['names']['from_longitude'] or info['names']['to_latitude'] and info['names']['to_longitude'] or info['names']['latitude'] and info['names']['longitude']):
		r = True

	if view == 'flow' and  info['names']['prev_name'] and info['names']['next_name']:
		# and info['names']['transitions'] :
		r = True

	return r

def isAllowViews(view,info):
	r = False
	return r

def isAllowReports(view,info):
	r = False
	return r

def isAllowWizards(view,info):
	r = False
	return r

ISALLOW_OBJS = {'dashboards':isAllowDashboards,'models': isAllowModels,'views':isAllowViews,'reports':isAllowReports,'wizards':isAllowWizards}

def isAllow(view,cat,info):
	r = False
	if cat in ISALLOW_OBJS:
		r = ISALLOW_OBJS[cat](view,info)
	
	return r


VIEWSGEN = {}			
VIEWSGEN['models']  = {'calendar':ViewCalendar,'schedule':ViewSchedule,'form': ViewForm, 'gantt':ViewGantt, 'graph':ViewGraph, 'kanban':ViewKanban,'list':ViewList,'m2mlist':ViewM2MList,'mdx':ViewMdx,'matrix':ViewMatrix,'search':ViewSearch,'find':ViewFind,'tree':ViewTree,'geo':ViewGeo,'flow':ViewFlow}		

IVIEWSGEN = {}
IVIEWSGEN['models']  = {'calendar':iViewCalendar,'schedule':iViewSchedule,'form': iViewForm, 'gantt':iViewGantt, 'graph':iViewGraph, 'kanban':iViewKanban,'list':iViewList,'m2mlist':iViewM2MList,'mdx':iViewMdx,'matrix':iViewMatrix,'search':iViewSearch,'find':iViewFind,'tree':iViewTree,'geo':iViewGeo,'flow':iViewFlow}		

EXCLUDE = {}
EXCLUDE['models'] = {'calendar':['one2many','one2related','many2many','text','binary','xml','json'],'form':[],'schedule':['one2many','one2related','many2many','text','binary','xml','json'],'gantt':['one2many','one2related','many2many','text','binary','xml','json'],'graph':['one2many','one2related','many2many','text','binary','xml','json'],'kanban':['one2many','one2related','many2many','xml','json'],'list':['many2many','text','binary','xml','json'],'m2mlist':['one2many','one2related','many2many','text','binary','xml','json'],'mdx':['one2many','one2related','many2many','text','binary','xml','json'],'matrix':['one2many','one2related','many2many','text','binary','xml','json'],'search':['one2many','one2related','many2many','text','binary','xml','json'],'find':['one2many','one2related','many2many','text','binary','xml','json'],'tree':['one2many','one2related','many2many','text','binary','xml','json'],'geo':['one2many','one2related','many2many','text','binary','xml','json'],'flow':['integer','float','real','decimal','numeric','date','time','datetime','one2related','many2many','text','binary','xml','json']}


