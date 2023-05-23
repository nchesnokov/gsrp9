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

FRAMEWORKS_1 = ('element-plus','vuetify','devextrme')
FRAMEWORKS = ('element-plus',)

_logger = logging.getLogger('listener.' + __name__)


GENTEMPLATES = {'element-plus':gen_template_el,'vuetify':gen_template_vuetify,'devextrme':gen_template_devextrme}
GENSRCIPTS = {'element-plus':gen_script_el,'vuetify':gen_script_vuetify,'devextrme':gen_script_devextrme}
GENSTYLES = {'element-plus':gen_style_el,'vuetify':gen_style_vuetify,'devextrme':gen_style_devextrme}

def ModelsColumns( view, vmodel, columns):
	return [{'seq':idx * 10,'col':vmodel + '/' + col} for idx,col in enumerate(columns)]
	#return [{'seq':idx * 10,'col':col} for idx,col in enumerate(columns)]

def Views(framework,model,views):
	return [ {'model':vmodel,'vtype':framework + '/' + view,'cols':ModelsColumns(view,vmodel,columns)} for view,vmodel,columns in views]
	
def iViews(framework, imodel, info, model, icolumns,views):
	res = []
	icolumns_info = info['columns']
	for view in views:
		exclude = EXCLUDE['models'][view]
		for icolumn in filter(lambda x: icolumns_info[x]['type'] not in exclude and icolumns_info[x]['type'] != 'iProperty',icolumns):
			res.append({'view_id':model + '/' + framework + '/' + view,'col':model + '/' + icolumn})  

	return res

def checkIViews(objs,iobjs):
	ma = {}
	imа = {}
	for obj in objs:
		 ma[model] = isAllow(model,m2mobjs)
	
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
					columns = isAllow(mobj,m2mobjs)
					if len(columns) == 0:
						continue
					views.append(view)
					ima.setdefault(m,[]).append(view)
	
	for ikey in ima.keys():
		if  ikey in ima:
			pass
		 

m2mobjs = {}
# im2mobjs = {}
	
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
						for m2mfield in obj._m2mfields:
							m2mobjs.setdefault(obj._columns[m2mfield].obj,{})[m2mfield] = registry._create_module_object(cat,obj._columns[m2mfield].obj,registry._getLastModuleObject(cat,obj._columns[m2mfield].obj))
					elif isinstance(obj,ModelInherit):
						if hasattr(obj,'_inherit') and getattr(obj,'_inherit',None):
							iobjs.setdefault(cat,[]).append(obj)
							# for m2mkey in filter(lambda x: obj._columns[x]._type == 'many2many',obj._columns.keys()):
								# im2mobjs[obj._columns[m2mkey].obj] = ''
		
		if len(objs) + len(iobjs) > 0:
			if len(objs) > 0:
				_remove_dirs(opj(path,module,'views'))
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
						yaml.dump([record for model in objs['models'] for record in Views(framework,model._name,isAllow(model,m2mobjs))], outfile, Dumper, default_flow_style=False)
					
					aw.writerow({'model': 'bc.ui.model.views','file':opj('views',framework,'views.yaml' )})
			if len(iobjs) > 0:
				if len(objs) == 0:
					a = open(opj(path,module,'views','views.csv'),'w')
					aw = csv.DictWriter(a,['model','file'])
					aw.writeheader()
					for framework in FRAMEWORKS_1:
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
								cols =  list(filter(lambda x: imodel._columns[x]._type != 'iProperty',inherit[m]['_columns']))
								nm = m + '.' +imodel._name
								views = []
								mobj = registry._create_module_object('models',m,registry._getLastModuleObject('models',m))
								info = mobj.modelInfo()
								ci = info['columns']
								for view in EXCLUDE['models'].keys():
									#columns = isAllow(view,'models',info,list(ci.keys()))
									columns = isAllowView(view,mobj,m2mobjs)
									if len(columns) == 0:
										continue
									views.append(view)
								with open(opj(path,module,'views','inherits',framework,nm.replace('.','_') + '.yaml'),'w') as outfile:
									yaml.dump(iViews(framework,imodel._name,imodel.imodelInfo(),m,cols,views), outfile, Dumper, default_flow_style=False)
					
							aw.writerow({'model': 'bc.ui.model.view.column.inherits','file':opj('views','inherits',framework,nm.replace('.','_') + '.yaml' )})
				
			logmodules.append(module)
	_logger.info('Gen views of modules %s' % (logmodules,))
	return ['Gen views of modules %s' % (logmodules,)]


def isAllow(obj,m2mobjs):
	allows = []
	for view in VIEWS:
		cols = list(filter(lambda x:obj._columns[x]._type not in EXCLUDE['models'][view] and obj._columns[x]._type != 'iProperty', obj._columns.keys()))
		if view == 'search' and (obj._RowNameName or obj._RecNameName or obj._FullNameName):
			allows.append((view,obj._name,cols))
		elif view in ('form','form.modal','list'):
			allows.append((view,obj._name,cols))
		elif view == 'tree' and obj._ParentIdName and obj._ChildsIdName:
			allows.append((view,obj._name,cols))
		elif view == 'find' and (len(obj._findfields) > 0 or obj._RowNameName or obj._RecNameName or obj._FullNameName):
			allows.append((view,obj._name,cols))
		elif view == 'm2mlist' and len(obj._m2mfields) > 0:
			web_pdb.set_trace()
			for m2mfield in obj._m2mfields:
				if obj._columns[m2mfield].obj in m2mobjs:
					for m2mkey in m2mobjs[obj._columns[m2mfield].obj].keys():
						m2mcols = list(filter(lambda x:m2mobjs[obj._columns[m2mfield].obj][m2mkey]._columns[x]._type not in EXCLUDE['models'][view] , m2mobjs[obj._columns[m2mfield].obj][m2mkey]._columns.keys()))
						allows.append((view,obj._name,m2mcols))
		elif view in ('calendar','graph','mdx') and obj._DateName:
			allows.append((view,obj._name,cols))
		elif view in ('schedule','gantt') and (obj._FromDateName and obj._ToDateName or obj._StartDateName and obj._EndDateName):
			allows.append((view,obj._name,cols))
		elif view == 'kanban' and obj._StateName:
			allows.append((view,obj._name,cols))
		elif view == 'geo' and (obj._FromLatitudeName and obj._FromLongitudeName or obj._ToLatitudeName and obj._ToLongitudeName or obj._LatitudeName and obj._LongitudeName ):
			allows.append((view,obj._name,cols))
		elif view == 'flow' and  obj._PrevNameName and obj._NextNameName:
			allows.append((view,obj._name,cols))
		elif view in ('o2m-form','o2m-list') and len(obj._m2ofields) > 0:
			allows.append((view,obj._name,cols))
		elif view == 'o2m-tree' and len(obj._m2ofields) > 0 and obj._ParentIdName and obj._ChildsIdName:
			allows.append((view,obj._name,cols))
		elif view in ('o2m-calendar','o2m-graph','o2m-mdx') and len(obj._m2ofields) > 0 and obj._DateName:
			allows.append((view,obj._name,cols))
		elif view in ('o2m-schedule','o2m-gantt') and len(obj._m2ofields) > 0 and (obj._FromDateName and obj._ToDateName or obj._StartDateName and obj._EndDateName):
			allows.append((view,obj._name,cols))
		elif view == 'o2m-kanban' and len(obj._m2ofields) > 0 and obj._StateName:
			allows.append((view,obj._name,cols))
		elif view == 'o2m-geo' and len(obj._m2ofields) > 0 and (obj._FromLatitudeName and obj._FromLongitudeName or obj._ToLatitudeName and obj._ToLongitudeName or obj._LatitudeName and obj._LongitudeName ):
			allows.append((view,obj._name,cols))
		elif view == 'o2m-flow' and len(obj._m2ofields) > 0 and  obj._PrevNameName and obj._NextNameName:
			allows.append((view,obj._name,cols))
	
	#print('ALLOW:',allows)
	return allows

def isAllowView(view,obj,m2mobjs):
	allows = []
	cols = list(filter(lambda x:obj._columns[x]._type not in EXCLUDE['models'][view] and obj._columns[x]._type != 'iProperty', obj._columns.keys()))
	if view == 'search' and (obj._RowNameName or obj._RecNameName or obj._FullNameName):
		allows.append((view,obj._name,cols))
	elif view in ('form','form.modal','list'):
		allows.append((view,obj._name,cols))
	elif view == 'tree' and obj._ParentIdName and obj._ChildsIdName:
		allows.append((view,obj._name,cols))
	elif view == 'find' and (len(obj._findfields) > 0 or obj._RowNameName or obj._RecNameName or obj._FullNameName):
		allows.append((view,obj._name,cols))
	elif view == 'm2mlist' and len(obj._m2mfields) > 0:
		for m2mfield in obj._m2mfields:
			if obj._columns[m2mfield].obj in m2mobjs:
				m2mcols = list(filter(lambda x:m2mobjs[obj._columns[m2mfield].obj]._columns[x]._type not in EXCLUDE['models'][view] , m2mobjs[obj._columns[m2mfield].obj]._columns.keys()))
				allows.append((view,obj._columns[m2mfield].obj,m2mcols))
	elif view in ('calendar','graph','mdx') and obj._DateName:
		allows.append((view,obj._name,cols))
	elif view in ('schedule','gantt') and (obj._FromDateName and obj._ToDateName or obj._StartDateName and obj._EndDateName):
		allows.append((view,obj._name,cols))
	elif view == 'kanban' and obj._StateName:
		allows.append((view,obj._name,cols))
	elif view == 'geo' and (obj._FromLatitudeName and obj._FromLongitudeName or obj._ToLatitudeName and obj._ToLongitudeName or obj._LatitudeName and obj._LongitudeName ):
		allows.append((view,obj._name,cols))
	elif view == 'flow' and  obj._PrevNameName and obj._NextNameName:
		allows.append((view,obj._name,cols))
	elif view in ('o2m-form','o2m-list') and len(obj._m2ofields) > 0:
		allows.append((view,obj._name,cols))
	elif view == 'o2m-tree' and len(obj._m2ofields) > 0 and obj._ParentIdName and obj._ChildsIdName:
		allows.append((view,obj._name,cols))
	elif view in ('o2m-calendar','o2m-graph','o2m-mdx') and len(obj._m2ofields) > 0 and obj._DateName:
		allows.append((view,obj._name,cols))
	elif view in ('o2m-schedule','o2m-gantt') and len(obj._m2ofields) > 0 and (obj._FromDateName and obj._ToDateName or obj._StartDateName and obj._EndDateName):
		allows.append((view,obj._name,cols))
	elif view == 'o2m-kanban' and len(obj._m2ofields) > 0 and obj._StateName:
		allows.append((view,obj._name,cols))
	elif view == 'o2m-geo' and len(obj._m2ofields) > 0 and (obj._FromLatitudeName and obj._FromLongitudeName or obj._ToLatitudeName and obj._ToLongitudeName or obj._LatitudeName and obj._LongitudeName ):
		allows.append((view,obj._name,cols))
	elif view == 'o2m-flow' and len(obj._m2ofields) > 0 and  obj._PrevNameName and obj._NextNameName:
		allows.append((view,obj._name,cols))
	
	#print('ALLOW:',allows)
	return allows

	
def isAllowInherit(iobj):
	iallows = []
	for view in VIEWS:
		icols = list(filter(lambda x: iobj._columns[x]._type != 'iProperty' and obj._columns[x]._type not in EXCLUDE['models'][view],iobj._columns.keys()))
		if len(icols) > 0:
			iallows.append((view,[]))
		
	
	return iallows
	
	# r = False
	# if cat in ISALLOW_OBJS:
		# r = ISALLOW_OBJS[cat](view,columnsinfo)
	
	# return r






VIEWS = ['search','find','list','m2mlist','form.modal','form','o2m-form','gantt','o2m-gantt','schedule', 'o2m-schedule','calendar', 'o2m-calendar','graph','o2m-graph','kanban','o2m-kanban','mdx','o2m-mdx','matrix','o2m-matrix','geo','o2m-geo','flow','o2m-flow','tree','o2m-tree','o2m-list']
EXCLUDE = {}
EXCLUDE['models'] = {'calendar':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'form':[],'form.modal':[],'schedule':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'gantt':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'graph':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'kanban':['one2many','one2related','many2many','xml','json','jsonb'],'list':['many2many','text','binary','xml','json','jsonb'],'o2m-list':['many2many','text','binary','xml','json','jsonb'],'m2mlist':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'mdx':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'matrix':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'search':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'find':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'tree':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'geo':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'flow':['integer','float','real','decimal','numeric','date','time','datetime','one2related','many2many','text','binary','xml','json','jsonb'],'o2m-calendar':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'o2m-form':[],'o2m-schedule':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'o2m-gantt':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'o2m-graph':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'o2m-kanban':['one2many','one2related','many2many','xml','json','jsonb'],'o2m-mdx':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'o2m-matrix':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'o2m-tree':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'o2m-geo':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'o2m-flow':['integer','float','real','decimal','numeric','date','time','datetime','one2related','many2many','text','binary','xml','json','jsonb']
}


