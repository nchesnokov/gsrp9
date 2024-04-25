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
	return [{'seq':idx * 10,'col': '/'.join([vmodel,col])} for idx,col in enumerate(columns)]

def ModelViews(model,views):
	return [ {'model':vmodel,'vtype':view,'controller':'%s:%s' % (view,vmodel),'standalone':True,'cols':ModelsColumns(view,vmodel,columns)} for view,vmodel,columns,cat in views]


def iViews(views):
	res = []

	for view,model,cols,cat in views:
		for col in cols:
			res.append({'view_id':model + '/' + view,'col': '/'.join([cat,model,col])})

	return res

_gen_type_view_class = {'form':'ModelForm','form.modal':'ModelFormModal','search':'ModelSearch','find':'ModelFind','list':'ModelList','o2m-list':'ModelO2MList','m2mlist':'ModelM2MList','o2m-form':'ModelO2MForm','gantt':'ModelGantt','o2m-gantt':'ModelO2MGantt','schedule':'ModelSchedule','o2m-schedule':'ModelO2MSchedule','calendar':'ModelCalendar','o2m-calendar':'ModelO2MCalendar','graph':'ModelGraph','o2m-graph':'ModelO2MGraph','kanban':'ModelKanban','o2m-kanban':'ModelO2MKanban','mdx':'ModelMdx','o2m-mdx':'ModelO2MMdx','matrix':'ModelMatrix','o2m-matrix':'ModelO2MMatrix','geo':'ModelGeo','o2m-geo':'ModelO2MGeo','flow':'ModelFlow','o2m-flow':'ModelO2MFlow','tree':'ModelTree','o2m-tree':'ModelO2MTree'}
_get_type_view_prefix_name = {'form':'model.form','form.modal':'model.form.modal','search':'model.search','find':'model.find','list':'model.list','o2m-list':'model.o2mlist','m2mlist':'model.m2mlist','o2m-form':'model.o2mform','gantt':'model.gantt','o2m-gantt':'model.o2mgantt','schedule':'model.schedule','o2m-schedule':'model.o2mschedule','calendar':'model.calendar','o2m-calendar':'vodel.o2mcalendar','graph':'model.graph','o2m-graph':'model.o2mgraph','kanban':'model.kanban','o2m-kanban':'model.o2mkanban','mdx':'model.mdx','o2m-mdx':'model.o2mmdx','matrix':'model.matrix','o2m-matrix':'model.o2mmatrix','geo':'model.geo','o2m-geo':'model.o2mgeo','flow':'model.flow','o2m-flow':'model.o2mflow','tree':'model.tree','o2m-tree':'model.o2mtree'}

def gen_model_views(description, views):
	v = []
	#web_pdb.set_trace()
	for view,vobj,columns,type_obj in views:
		v.append('from gsrp5service.obj.controller.controller import View%sController' % (_gen_type_view_class[view],))
	v.append('')
	for view,vobj,columns,type_obj in views:
#		if view in ('form','form.modal','search','find'):
		v.append('class View%s%s(View%sController):' %( _gen_type_view_class[view],''.join([n.title() for n in vobj.split('.')]),_gen_type_view_class[view]))
		v.append('\t_name = "%s:%s"' % (view,vobj))
		v.append('\t_view_name = "%s"' % ('/'.join([vobj,view]),))
		v.append('\t_description = "%s"' % ( 	description,))
		v.append('')

	return '\n'.join(v)

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
		if module in registry._metas:
			for cat in filter(lambda x: x in ('models','reports','dashboards'),registry._metas[module].keys()):
				objs = {}
				iobjs = {}
				for key in registry._metas[module][cat]:
					obj = registry._create_module_object(cat,key,module)
					if isinstance(obj,Model):
						objs.setdefault(cat,[]).append(obj)
					elif isinstance(obj,ModelInherit):
						if hasattr(obj,'_inherit') and getattr(obj,'_inherit',None):
							iobjs.setdefault(cat,[]).append(obj)

				if len(objs) + len(iobjs) > 0:
					if not os.path.exists(opj(path,module,cat,'views')):
						os.mkdir(opj(path,module,cat,'views'))

					if not os.path.exists(opj(path,module,cat,'controllers')):
						os.mkdir(opj(path,module,cat,'controllers'))

					if not os.path.exists(opj(path,module,cat,'webcomponents')):
						os.mkdir(opj(path,module,cat,'webcomponents'))

					if len(objs) > 0:
						_remove_dirs(opj(path,module,cat,'views'))
						_remove_dirs(opj(path,module,cat,'controllers'))
						_remove_dirs(opj(path,module,cat,'webcompponents'))
						fmode = 'w'
						a = open(opj(path,module,cat,'views.csv'),fmode)
						if fmode == 'w':
							aw = csv.DictWriter(a,['model', 'file'])
							aw.writeheader()
							if os.path.exists(opj(path,module,cat,'views')):
								_remove_dirs(opj(path,module,cat,'views'))

						if not os.path.exists(opj(path,module,cat,'views')):
							os.mkdir(opj(path,module,cat,'views'))

						with open(opj(path,module,cat,'views','views.yaml'),'w') as outfile:
							yaml.dump([record for model in objs[cat] for record in ModelViews(model._name,isAllow(registry,model))], outfile, Dumper, default_flow_style=False)

						aw.writerow({'model': 'bc.ui.model.views','file':opj(cat,'views','views.yaml' )})

						_i_ = []
						for model in objs[cat]:
							record = gen_model_views(model._description,isAllow(registry,model))
							_i_.append('from . import ' + model._name.replace('.','_'))
							with open(opj(path,module,cat,'controllers',model._name.replace('.','_')+'.py'),'w') as outfile:
								outfile.write(record)

						with open(opj(path,module,cat,'controllers','__init__.py'),'w') as outfile:
							outfile.write('\n'.join(_i_))


					if len(iobjs) > 0:
						if len(objs) == 0:
							a = open(opj(path,module,cat,'views','views.csv'),'w')
							aw = csv.DictWriter(a,['model','file'])
							aw.writeheader()
						for framework in FRAMEWORKS_1:
							_remove_dirs(opj(path,module,cat,'views','inherits'))

						if not os.path.exists(opj(path,module,cat,'views','inherits')):
							os.mkdir(opj(path,module,cat,'views','inherits'))

						if not os.path.exists(opj(path,module,cat,'views','inherits')):
							os.mkdir(opj(path,module,cat,'views','inherits'))
						for imodel in iobjs[cat]:
							inherit = getattr(imodel,'_inherit')
							for m in inherit.keys():
								if '_columns' in inherit[m]:
									nm = m + '.' +imodel._name
									views = []
									m2mviews = []
									vv = isAllowView(registry,m,imodel)
									if len(vv) > 0:
										views.extend(list(filter(lambda x:x[0] != 'm2mlist',vv)))
										m2mviews.extend(list(filter(lambda x:x[0] == 'm2mlist',vv)))
										if len(views) > 0:
											with open(opj(path,module,cat,'views','inherits',nm.replace('.','_') + '.yaml'),'w') as outfile:
												yaml.dump(iViews(views), outfile, Dumper, default_flow_style=False)

											aw.writerow({'model': 'bc.ui.model.view.column.inherits','file':opj(cat,'views','inherits',nm.replace('.','_') + '.yaml' )})

										if len(m2mviews) > 0:
											with open(opj(path,module,cat,'views','inherits','m2m_' + nm.replace('.','_') + '.yaml'),'w') as outfile:
												yaml.dump( ModelViews(m,m2mviews), outfile, Dumper, default_flow_style=False)

											aw.writerow({'model': 'bc.ui.model.views','file':opj(cat,'views','inherits','m2m_' + nm.replace('.','_') + '.yaml' )})

			logmodules.append(module)
	_logger.info('Gen views of modules %s' % (logmodules,))
	return ['Gen views of modules %s' % (logmodules,)]


def isAllow(registry,obj):
	allows = []
	for view in VIEWS['models']:
		cols = list(filter(lambda x:obj._columns[x]._type not in EXCLUDE['models'][view] and obj._columns[x]._type != 'iProperty', obj._columns.keys()))
		if view == 'search' and (obj._RowNameName or obj._RecNameName or obj._FullNameName):
			allows.append((view,obj._name,cols,'models'))
		elif view in ('form','form.modal','list') and (obj._RowNameName or obj._RecNameName or obj._FullNameName):
			allows.append((view,obj._name,cols,'models'))
		elif view == 'tree' and obj._ParentIdName and obj._ChildsIdName and (obj._RowNameName or obj._RecNameName or obj._FullNameName):
			allows.append((view,obj._name,cols,'models'))
		elif view == 'find' and (len(obj._findfields) > 0 or obj._RowNameName or obj._RecNameName or obj._FullNameName):
			allows.append((view,obj._name,cols,'models'))
		elif view == 'm2mlist' and len(obj._m2mfields) > 0:
			for m2mfield in obj._m2mfields:
				mobj = registry._create_module_object('models',obj._columns[m2mfield].obj,registry._getLastModuleObject('models',obj._columns[m2mfield].obj))
				allows.append((view,obj._columns[m2mfield].obj,list(filter(lambda x: mobj._columns[x]._type not in EXCLUDE['models']['m2mlist'],mobj._columns.keys())),'models'))
		elif view in ('calendar','graph','mdx') and obj._DateName and (obj._RowNameName or obj._RecNameName or obj._FullNameName):
			allows.append((view,obj._name,cols,'models'))
		elif view in ('schedule','gantt') and (obj._FromDateName and obj._ToDateName or obj._StartDateName and obj._EndDateName)  and (obj._RowNameName or obj._RecNameName or obj._FullNameName):
			allows.append((view,obj._name,cols,'models'))
		elif view == 'kanban' and obj._StateName and (obj._RowNameName or obj._RecNameName or obj._FullNameName):
			allows.append((view,obj._name,cols,'models'))
		elif view == 'geo' and (obj._FromLatitudeName and obj._FromLongitudeName or obj._ToLatitudeName and obj._ToLongitudeName or obj._LatitudeName and obj._LongitudeName )  and (obj._RowNameName or obj._RecNameName or obj._FullNameName):
			allows.append((view,obj._name,cols,'models'))
		elif view == 'flow' and obj._PrevNameName and obj._NextNameName and (obj._RowNameName or obj._RecNameName or obj._FullNameName):
			allows.append((view,obj._name,cols,'models'))
		elif view in ('o2m-form','o2m-list') and len(obj._m2ofields) > 0 and not (obj._RowNameName or obj._RecNameName or obj._FullNameName):
			allows.append((view,obj._name,cols,'models'))
		elif view == 'o2m-tree' and len(obj._m2ofields) > 0 and obj._ParentIdName and obj._ChildsIdName and not (obj._RowNameName or obj._RecNameName or obj._FullNameName):
			allows.append((view,obj._name,cols,'models'))
		elif view in ('o2m-calendar','o2m-graph','o2m-mdx') and len(obj._m2ofields) > 0 and obj._DateName and not (obj._RowNameName or obj._RecNameName or obj._FullNameName):
			allows.append((view,obj._name,cols,'models'))
		elif view in ('o2m-schedule','o2m-gantt') and len(obj._m2ofields) > 0 and (obj._FromDateName and obj._ToDateName or obj._StartDateName and obj._EndDateName) and not (obj._RowNameName or obj._RecNameName or obj._FullNameName):
			allows.append((view,obj._name,cols,'models'))
		elif view == 'o2m-kanban' and len(obj._m2ofields) > 0 and obj._StateName and not (obj._RowNameName or obj._RecNameName or obj._FullNameName):
			allows.append((view,obj._name,cols,'models'))
		elif view == 'o2m-geo' and len(obj._m2ofields) > 0 and (obj._FromLatitudeName and obj._FromLongitudeName or obj._ToLatitudeName and obj._ToLongitudeName or obj._LatitudeName and obj._LongitudeName ) and not (obj._RowNameName or obj._RecNameName or obj._FullNameName):
			allows.append((view,obj._name,cols,'models'))
		elif view == 'o2m-flow' and len(obj._m2ofields) > 0 and  obj._PrevNameName and obj._NextNameName and not (obj._RowNameName or obj._RecNameName or obj._FullNameName):
			allows.append((view,obj._name,cols,'models'))

	return allows

def isAllowView(registry,model,imodel):
	allows = []

	obj = registry._create_module_object('models',model,registry._getLastModuleObject('models',model))
	m2mcols = list(filter(lambda x:imodel._columns[x]._type == 'many2many', imodel._columns.keys()))
	icols = imodel._inherit[model]['_columns']

	for view in EXCLUDE['models'].keys():
		cols = list(filter(lambda x:x in icols and imodel._columns[x]._type not in EXCLUDE['models'][view] and imodel._columns[x]._type != 'iProperty', imodel._columns.keys()))
		if len(cols) == 0 and view != 'm2mlist':
			continue
		if view == 'search' and (obj._RowNameName or obj._RecNameName or obj._FullNameName):
			allows.append((view,obj._name,cols,'models'))
		elif view in ('form','form.modal','list'):
			allows.append((view,obj._name,cols,'models'))
		elif view == 'tree' and obj._ParentIdName and obj._ChildsIdName:
			allows.append((view,obj._name,cols,'models'))
		elif view == 'find' and (len(obj._findfields) > 0 or obj._RowNameName or obj._RecNameName or obj._FullNameName):
			allows.append((view,obj._name,cols,'models'))
		elif view == 'm2mlist':
			if len(m2mcols) > 0:
				for m2mcol in m2mcols:
					mobj = registry._create_module_object('models',imodel._columns[m2mcol].obj,registry._getLastModuleObject('models',imodel._columns[m2mcol].obj))
					#allows.append((view,imodel._columns[m2mcol].obj,list(filter(lambda x: mobj._columns[x]._type not in EXCLUDE['models']['m2mlist'],mobj._columns.keys()))))
					allows.append((view,mobj._name,list(filter(lambda x: mobj._columns[x]._type not in EXCLUDE['models']['m2mlist'],mobj._columns.keys())),'models'))
		elif view in ('calendar','graph','mdx') and hasattr(obj,'_DateName') and obj._DateName:
			allows.append((view,obj._name,cols,'models'))
		elif view in ('schedule','gantt') and (obj._FromDateName and obj._ToDateName or obj._StartDateName and obj._EndDateName):
			allows.append((view,obj._name,cols,'models'))
		elif view == 'kanban' and obj._StateName:
			allows.append((view,obj._name,cols,'models'))
		elif view == 'geo' and (obj._FromLatitudeName and obj._FromLongitudeName or obj._ToLatitudeName and obj._ToLongitudeName or obj._LatitudeName and obj._LongitudeName ):
			allows.append((view,obj._name,cols,'models'))
		elif view == 'flow' and  obj._PrevNameName and obj._NextNameName:
			allows.append((view,obj._name,cols,'models'))
		elif view in ('o2m-form','o2m-list') and len(obj._m2ofields) > 0:
			allows.append((view,obj._name,cols,'models'))
		elif view == 'o2m-tree' and len(obj._m2ofields) > 0 and obj._ParentIdName and obj._ChildsIdName:
			allows.append((view,obj._name,cols,'models'))
		elif view in ('o2m-calendar','o2m-graph','o2m-mdx') and len(obj._m2ofields) > 0 and obj._DateName:
			allows.append((view,obj._name,cols,'models'))
		elif view in ('o2m-schedule','o2m-gantt') and len(obj._m2ofields) > 0 and (obj._FromDateName and obj._ToDateName or obj._StartDateName and obj._EndDateName):
			allows.append((view,obj._name,cols,'models'))
		elif view == 'o2m-kanban' and len(obj._m2ofields) > 0 and obj._StateName:
			allows.append((view,obj._name,cols,'models'))
		elif view == 'o2m-geo' and len(obj._m2ofields) > 0 and (obj._FromLatitudeName and obj._FromLongitudeName or obj._ToLatitudeName and obj._ToLongitudeName or obj._LatitudeName and obj._LongitudeName ):
			allows.append((view,obj._name,cols,'models'))
		elif view == 'o2m-flow' and len(obj._m2ofields) > 0 and  obj._PrevNameName and obj._NextNameName:
			allows.append((view,obj._name,cols,'models'))

	return allows


def isAllowInherit(iobj):
	iallows = []
	for view in VIEWS['models']:
		icols = list(filter(lambda x: iobj._columns[x]._type != 'iProperty' and obj._columns[x]._type not in EXCLUDE['models'][view],iobj._columns.keys()))
		if len(icols) > 0:
			iallows.append((view,[]))


	return iallows

VIEWS = {}
VIEWS['models'] = ['search','find','list','m2mlist','form.modal','form','o2m-form','gantt','o2m-gantt','schedule', 'o2m-schedule','calendar', 'o2m-calendar','graph','o2m-graph','kanban','o2m-kanban','mdx','o2m-mdx','matrix','o2m-matrix','geo','o2m-geo','flow','o2m-flow','tree','o2m-tree','o2m-list']

EXCLUDE = {}
EXCLUDE['models'] = {'calendar':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'form':[],'form.modal':[],'schedule':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'gantt':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'graph':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'kanban':['one2many','one2related','many2many','xml','json','jsonb'],'list':['many2many','text','binary','xml','json','jsonb'],'o2m-list':['many2many','text','binary','xml','json','jsonb'],'m2mlist':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'mdx':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'matrix':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'search':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'find':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'tree':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'geo':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'flow':['integer','float','real','decimal','numeric','date','time','datetime','one2related','many2many','text','binary','xml','json','jsonb'],'o2m-calendar':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'o2m-form':[],'o2m-schedule':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'o2m-gantt':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'o2m-graph':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'o2m-kanban':['one2many','one2related','many2many','xml','json','jsonb'],'o2m-mdx':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'o2m-matrix':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'o2m-tree':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'o2m-geo':['one2many','one2related','many2many','text','binary','xml','json','jsonb'],'o2m-flow':['integer','float','real','decimal','numeric','date','time','datetime','one2related','many2many','text','binary','xml','json','jsonb']
}


