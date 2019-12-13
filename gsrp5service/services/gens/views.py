import os
import logging
from os.path import join as opj
from io import BytesIO
from gsrp5service.services.models.orm.model import Model,ModelInherit

b = BytesIO()
TAB = '  '

from gsrp5service.services.models.orm.common import DEFAULT_MODEL_NAMES as DMN

_logger = logging.getLogger('listener.' + __name__)

def ColumnsView(level, info, columns, view):

	indent = TAB * level
	exclude = EXCLUDE[view]
	for column in columns:
		if info[column]['type'] in exclude or info[column]['type'] == 'iSelection':
			continue
		b.write((indent + '<field name="%s"/>\n' % (column, )).encode('utf-8'))

def ViewCalendar(level,modelinfo,columns):

	indent = TAB * level
	addparm = ''

	if modelinfo['names']['date'] != DMN['date']:
		addparm += ' date="%s"' % (modelinfo['names']['date'],)

	b.write((indent + '<calendar%s>\n' % (addparm,)).encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'calendar')
	b.write((indent + '</calendar>\n').encode('utf-8'))

def iViewCalendar(level,modelinfo,columns):

	indent = TAB * level
	b.write((indent + '<calendar>\n').encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'calendar')
	b.write((indent + '</calendar>\n').encode('utf-8'))

def ViewForm(level,modelinfo,columns):

	indent = TAB * level
	
	b.write((indent + '<form>\n').encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'form')
	b.write((indent + '</form>\n').encode('utf-8'))

def iViewForm(level,modelinfo,columns):

	indent = TAB * level
	
	b.write((indent + '<form>\n').encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'form')
	b.write((indent + '</form>\n').encode('utf-8'))

def ViewSchedule(level,modelinfo,columns):

	indent = TAB * level
	
	addparm = ''

	if modelinfo['names']['from_date'] != DMN['from_date']:
		addparm += ' from_date="%s"' % (modelinfo['names']['from_date'],)

	if modelinfo['names']['to_date'] != DMN['to_date']:
		addparm += ' to_date="%s"' % (modelinfo['names']['to_date'],)

	b.write((indent + '<schedule%s>\n' % (addparm,)).encode('utf-8'))

	ColumnsView(level+1,modelinfo['columns'],columns,'gantt')
	b.write((indent + '</schedule>\n').encode('utf-8'))

def iViewSchedule(level,modelinfo,columns):

	indent = TAB * level
	
	b.write((indent + '<schedule>\n').encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'gantt')
	b.write((indent + '</schedule>\n').encode('utf-8'))

def ViewGantt(level,modelinfo,columns):

	indent = TAB * level
	
	addparm = ''

	if modelinfo['names']['parent_id'] != DMN['parent_id']:
		addparm += ' parent_id="%s"' % (modelinfo['names']['parent_id'],)

	if modelinfo['names']['childs_id'] != DMN['childs_id']:
		addparm += ' childs_id="%s"' % (modelinfo['names']['childs_id'],)

	if modelinfo['names']['start_date'] != DMN['start_date']:
		addparm += ' start_date="%s"' % (modelinfo['names']['start_date'],)

	if modelinfo['names']['end_date'] != DMN['end_date']:
		addparm += ' end_date="%s"' % (modelinfo['names']['end_date'],)

	b.write((indent + '<gantt%s>\n' % (addparm,)).encode('utf-8'))

	ColumnsView(level+1,modelinfo['columns'],columns,'gantt')
	b.write((indent + '</gantt>\n').encode('utf-8'))

def iViewGantt(level,modelinfo,columns):

	indent = TAB * level
	
	b.write((indent + '<gantt>\n').encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'gantt')
	b.write((indent + '</gantt>\n').encode('utf-8'))

def ViewGraph(level,modelinfo,columns):

	indent = TAB * level
	
	addparm = ''

	if modelinfo['names']['date'] != DMN['date']:
		addparm += ' date="%s"' % (modelinfo['names']['date'],)

	b.write((indent + '<graph%s>\n' % (addparm,)).encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'graph')
	b.write((indent + '</graph>\n').encode('utf-8'))

def iViewGraph(level,modelinfo,columns):

	indent = TAB * level
	
	b.write((indent + '<graph>\n').encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'graph')
	b.write((indent + '</graph>\n').encode('utf-8'))

def ViewKanban(level,modelinfo,columns):

	indent = TAB * level

	addparm = ''

	if modelinfo['names']['state'] != DMN['state']:
		addparm += ' state="%s"' % (modelinfo['names']['state'],)

	b.write((indent + '<kanban%s>\n' % (addparm,)).encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'kanban')
	b.write((indent + '</kanban>\n').encode('utf-8'))

def iViewKanban(level,modelinfo,columns):

	indent = TAB * level

	b.write((indent + '<kanban>\n').encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'kanban')
	b.write((indent + '</kanban>\n').encode('utf-8'))

def ViewList(level,modelinfo,columns):

	indent = TAB * level
	
	b.write((indent + '<list>\n').encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'list')
	b.write((indent + '</list>\n').encode('utf-8'))

def iViewList(level,modelinfo,columns):

	indent = TAB * level
	
	b.write((indent + '<list>\n').encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'list')
	b.write((indent + '</list>\n').encode('utf-8'))

def ViewM2MList(level,modelinfo,columns):

	indent = TAB * level
	
	b.write((indent + '<m2mlist>\n').encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'m2mlist')
	b.write((indent + '</m2mlist>\n').encode('utf-8'))

def iViewM2MList(level,modelinfo,columns):

	indent = TAB * level
	
	b.write((indent + '<m2mlist>\n').encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'m2mlist')
	b.write((indent + '</m2mlist>\n').encode('utf-8'))


def ViewMdx(level,modelinfo,columns):

	indent = TAB * level
	
	addparm = ''

	if modelinfo['names']['date'] != DMN['date']:
		addparm += ' date="%s"' % (modelinfo['names']['date'],)

	b.write((indent + '<mdx%s>\n' % (addparm,)).encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'mdx')
	b.write((indent + '</mdx>\n').encode('utf-8'))

def iViewMdx(level,modelinfo,columns):

	indent = TAB * level
	
	b.write((indent + '<mdx>\n').encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'mdx')
	b.write((indent + '</mdx>\n').encode('utf-8'))

def ViewSearch(level,modelinfo,columns):

	indent = TAB * level
	
	b.write((indent + '<search>\n').encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'search')
	b.write((indent + '</search>\n').encode('utf-8'))

def iViewSearch(level,modelinfo,columns):

	indent = TAB * level
	
	b.write((indent + '<search>\n').encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'search')
	b.write((indent + '</search>\n').encode('utf-8'))

def ViewFind(level,modelinfo,columns):

	indent = TAB * level
	
	b.write((indent + '<find>\n').encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'find')
	b.write((indent + '</find>\n').encode('utf-8'))

def iViewFind(level,modelinfo,columns):

	indent = TAB * level
	
	b.write((indent + '<find>\n').encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'find')
	b.write((indent + '</find>\n').encode('utf-8'))


def ViewTree(level,modelinfo,columns):

	indent = TAB * level
	
	addparm = ''

	if modelinfo['names']['parent_id'] != DMN['parent_id']:
		addparm += ' parent_id="%s"' % (modelinfo['names']['parent_id'],)

	if modelinfo['names']['childs_id'] != DMN['childs_id']:
		addparm += ' childs_id="%s"' % (modelinfo['names']['childs_id'],)

	b.write((indent + '<tree%s>\n' % (addparm,)).encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'tree')
	b.write((indent + '</tree>\n').encode('utf-8'))

def iViewTree(level,modelinfo,columns):

	indent = TAB * level
	
	b.write((indent + '<tree>\n').encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'tree')
	b.write((indent + '</tree>\n').encode('utf-8'))
#Geo
def ViewGeo(level,modelinfo,columns):

	indent = TAB * level
	
	addparm = ''

	if modelinfo['names']['latitude'] != DMN['latitude']:
		addparm += ' latitude="%s"' % (modelinfo['names']['latitude'],)

	if modelinfo['names']['longitude'] != DMN['longitude']:
		addparm += ' longitude="%s"' % (modelinfo['names']['longitude'],)

	if modelinfo['names']['from_latitude'] != DMN['from_latitude']:
		addparm += ' from_latitude="%s"' % (modelinfo['names']['from_latitude'],)

	if modelinfo['names']['from_longitude'] != DMN['from_longitude']:
		addparm += ' from_longitude="%s"' % (modelinfo['names']['from_longitude'],)

	if modelinfo['names']['to_latitude'] != DMN['to_latitude']:
		addparm += ' to_latitude="%s"' % (modelinfo['names']['to_latitude'],)

	if modelinfo['names']['to_longitude'] != DMN['to_longitude']:
		addparm += ' to_longitude="%s"' % (modelinfo['names']['to_longitude'],)

	b.write((indent + '<geo%s>\n' % (addparm,)).encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'geo')
	b.write((indent + '</geo>\n').encode('utf-8'))

def iViewGeo(level,modelinfo,columns):

	indent = TAB * level
	
	b.write((indent + '<geo>\n').encode('utf-8'))
	ColumnsView(level+1,modelinfo['columns'],columns,'geo')
	b.write((indent + '</geo>\n').encode('utf-8'))


def RecordView(level,model,modelinfo,columns,view):

	indent = TAB * level
	b.write((indent + '<record id="%s">\n' % ('view.' + model + '.' + view,)).encode('utf-8'))

	b.write((indent + TAB + '<column name="name">%s</column>\n' % ('view.' + model+'.' + view,)).encode('utf-8'))

	b.write((indent + TAB + '<column name="model">%s</column>\n' % (model,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="arch" type="Xml">\n').encode('utf-8'))
	VIEWSGEN[view](level+2,modelinfo,columns)
	b.write((indent + TAB + '</column>\n').encode('utf-8'))
	b.write((indent + '</record>\n').encode('utf-8'))

def iRecordView(level,model,modelinfo,columns,view,registry):

	indent = TAB * level
	columnsinfo = modelinfo['columns']
	for key in modelinfo['inherit'].keys():
		ki = registry._create_model(key,registry._getLastModule(key)).modelInfo()
		if not isAllow(view,ki) or len(list(filter(lambda x: not columnsinfo[x]['type'] in EXCLUDE[view] and columnsinfo[x]['type'] != 'iSelection' ,modelinfo['inherit'][key]['_columns']))) == 0:
			continue
		b.write((indent + '<record id="%s">\n' % ('view.' + model + '.' + view + '.inherit.' + key,)).encode('utf-8'))
		b.write((indent + TAB + '<column name="view_id">%s</column>\n' % ('view.' + key + '.' + view,)).encode('utf-8'))
		b.write((indent + TAB + '<column name="name">%s</column>\n' % ('view.' + model + '.' + view + '.inherit.' + key ,)).encode('utf-8'))

		b.write((indent + TAB + '<column name="arch" type="Xml">\n').encode('utf-8'))

		IVIEWSGEN[view](level+2,modelinfo,modelinfo['inherit'][key]['_columns'])
		b.write((indent + TAB + '</column>\n').encode('utf-8'))
		b.write((indent + '</record>\n').encode('utf-8'))

def Views(level,model,modelinfo,columns):
	columnsinfo = modelinfo['columns']
	for view in VIEWSGEN.keys():
		if isAllow(view,modelinfo) and len(list(filter(lambda x: not columnsinfo[x]['type'] in EXCLUDE[view] and columnsinfo[x]['type'] != 'iSelection',columns))) > 0:
			RecordView(level,model,modelinfo,columns,view)

def iViews(level,model,modelinfo,columns,registry):
	for view in IVIEWSGEN.keys():
		if view in modelinfo['views']:
			iRecordView(level,model,modelinfo,columns,view,registry)


def Records(level,pool,registry,module,models):

	indent = TAB * level

	b.write((indent + '<records model="%s">\n' % ('bc.ui.views',)).encode('utf-8'))

	for model in models:
		modelinfo = model.modelInfo()
		columns = modelinfo['columns']
		Views(level+1,model._name,modelinfo,columns)

	b.write((indent + '</records>\n').encode('utf-8'))

def iRecords(level,pool,registry,module,models):

	indent = TAB * level

	b.write((indent + '<records model="%s">\n' % ('bc.ui.views.inherit',)).encode('utf-8'))

	for model in models:
		modelinfo = model.modelInfo()

		columns = modelinfo['columns']
		iViews(level+1,model._name,modelinfo,columns,registry)
	
	b.write((indent + '</records>\n').encode('utf-8'))



def Area(cr, pool, registry, modules = None):
	pwd = os.getcwd()
	if not modules:
		modules = registry._depends
	else:
		modules = list(filter(lambda x: x in modules,registry._depends))
	logmodules = []
	for module in modules:
		path = registry._modules[module]['path']
		models = []
		imodels = []
		for model in registry._momm[module].keys():
			mm = registry._create_model(model,registry._getFirstModule(model))
			#print('FIRST-MODULE:',model,registry._getFirstModule(model),mm)
			if isinstance(mm,Model):
				models.append(mm)
			elif isinstance(mm,ModelInherit):
				if hasattr(mm,'_inherit') and getattr(mm,'_inherit',None):
					imodels.append(mm)
		
		if len(models) + len(imodels) > 0:
			#print('models:',module,models)
			#print('imodels:',module,imodels)
			#return
			b.write('<?xml version="1.0" encoding="utf-8" standalone="yes" ?>\n'.encode('utf-8'))
			b.write((TAB+'<gsrp>\n').encode('utf-8'))
			b.write((TAB * 2 + '<data>\n').encode('utf-8'))
			if len(models) > 0:
				Records(3,pool, registry, module, models)
			if len(imodels) > 0:
				iRecords(3, pool, registry, module, imodels)
			b.write((TAB * 2 + '</data>\n').encode('utf-8'))
			b.write((TAB + '</gsrp>\n').encode('utf-8'))
			f=open(opj(path,module,'views','views.xml'),'wb')
			f.write(b.getvalue())
			f.close()
			b.seek(0,0)
			b.truncate(0)
			logmodules.append(module)
	_logger.info('Gen views of modules %s' % (logmodules,))
	return ['Gen views of modules %s' % (logmodules,)]


def isAllow(view,info):

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

	if view == 'geo' and (info['names']['from_latitude'] and info['names']['from_longitude'] or info['names']['to_latitude'] and info['names']['to_longitude'] or info['names']['latitude'] and info['names']['longitude']):
		r = True

	
	return r

			
VIEWSGEN  = {'calendar':ViewCalendar,'schedule':ViewSchedule,'form': ViewForm, 'gantt':ViewGantt, 'graph':ViewGraph, 'kanban':ViewKanban,'list':ViewList,'m2mlist':ViewM2MList,'mdx':ViewMdx,'search':ViewSearch,'find':ViewFind,'tree':ViewTree,'geo':ViewGeo}		

IVIEWSGEN  = {'calendar':iViewCalendar,'schedule':iViewSchedule,'form': iViewForm, 'gantt':iViewGantt, 'graph':iViewGraph, 'kanban':iViewKanban,'list':iViewList,'m2mlist':iViewM2MList,'mdx':iViewMdx,'search':iViewSearch,'find':iViewFind,'tree':iViewTree,'geo':iViewGeo}		

EXCLUDE = {'calendar':['one2many','one2related','many2many','text','binary','xml','json'],'form':[],'schedule':['one2many','one2related','many2many','text','binary','xml','json'],'gantt':['one2many','one2related','many2many','text','binary','xml','json'],'graph':['one2many','one2related','many2many','text','binary','xml','json'],'kanban':['one2many','one2related','many2many','xml','json'],'list':['many2many','text','binary','xml','json'],'m2mlist':['one2many','one2related','many2many','text','binary','xml','json'],'mdx':['one2many','one2related','many2many','text','binary','xml','json'],'search':['one2many','one2related','many2many','text','binary','xml','json'],'find':['one2many','one2related','many2many','text','binary','xml','json'],'tree':['one2many','one2related','many2many','text','binary','xml','json'],'geo':['one2many','one2related','many2many','text','binary','xml','json']}


