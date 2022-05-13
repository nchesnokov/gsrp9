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
	return [{'seq':idx * 10,'col':col} for idx,col in enumerate(columns)]

def Views(framework,model,views):
	return [ {'model':model,'vtype':framework + '/' + view,'cols':ModelsColumns(view,columns)} for view,columns in views]
	
def iViews(framework, imodel, views):
	res = []
	icolumns_info = imodel.modelInfo()['columns']
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
					with open(opj(path,module,'views',framework,'views.yaml'),'w') as outfile:					
						yaml.dump([record for model in objs['models'] for record in Views(framework,model._name,isAllow(model))], outfile, Dumper, default_flow_style=False)
					
					aw.writerow({'model': 'bc.ui.model.views','file':opj('views',framework,'views.yaml' )})
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


def isAllow(obj):
	allows = []
	for view in VIEWS:
		if view == 'search' and len(obj._o2mfields) > 0 and len(obj._m2ofields) == 0 and obj._getRecNameName():
			allows.append((view,set(obj._columns.keys()-set(EXCLUDE['models'][view]))))
		elif view == 'find' and len(obj._findfields) > 0:
			allows.append((view,set(obj._columns.keys()-set(EXCLUDE['models'][view]))))
		elif view == 'm2m' and len(obj._m2mfields) > 0:
			allows.append((view,set(obj._columns.keys()-set(EXCLUDE['models'][view]))))

	
	return allows
	
def isAllowInherit(iobj):
	iallows = []
	for view in VIEWS:
		icols = list(filter(lambda x: iobj._columns[x]._type != 'iProperty' and obj._columns[x]._type not in EXCLUDE['models'][view],iobj._columns.keys()))
		if len(icols) > 0:
			iallows.append((view,[]))
		
	
	return iallows
	
	r = False
	if cat in ISALLOW_OBJS:
		r = ISALLOW_OBJS[cat](view,columnsinfo)
	
	return r






VIEWS = ['search','find','m2mlist','form.modal','form','o2mform','gantt','o2mgantt','schedule', 'o2mschedule','calendat', 'o2ncalendar','graph','o2mgraph','kanban','o2mkanban','mdx','o2mmdx','matrix','o2mmatrix','geo','o2mgeo','flow','o2mflow','tree','o2mtree']
EXCLUDE = {}
EXCLUDE['models'] = {'calendar':['one2many','one2related','many2many','text','binary','xml','json'],'form':[],'form.modal':[],'schedule':['one2many','one2related','many2many','text','binary','xml','json'],'gantt':['one2many','one2related','many2many','text','binary','xml','json'],'graph':['one2many','one2related','many2many','text','binary','xml','json'],'kanban':['one2many','one2related','many2many','xml','json'],'list':['many2many','text','binary','xml','json'],'m2mlist':['one2many','one2related','many2many','text','binary','xml','json'],'mdx':['one2many','one2related','many2many','text','binary','xml','json'],'matrix':['one2many','one2related','many2many','text','binary','xml','json'],'search':['one2many','one2related','many2many','text','binary','xml','json'],'find':['one2many','one2related','many2many','text','binary','xml','json'],'tree':['one2many','one2related','many2many','text','binary','xml','json'],'geo':['one2many','one2related','many2many','text','binary','xml','json'],'flow':['integer','float','real','decimal','numeric','date','time','datetime','one2related','many2many','text','binary','xml','json']
}


