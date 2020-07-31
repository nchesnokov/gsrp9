import os
import logging
from os.path import join as opj
from io import BytesIO
from gsrp5service.orm.model import Model

b = BytesIO()
TAB = '  '

GRANTS = ('readonly','nodrop','full','crw')
ACCESS = {'readonly':['aread','aselect'],'nodrop':['aread','aselect','acreate','ainsert','awrite','aupdate','amodify','aupsert','abrowse','aselectbrowse'],'full':['aread','aselect','acreate','ainsert','awrite','aupdate','amodify','aupsert','aunlink','adelete','abrowse','aselectbrowse'],'crw':['aread','aselect','acreate','ainsert','awrite','aupdate','amodify','aupsert','abrowse','aselectbrowse']}

_logger = logging.getLogger('listener.' + __name__)

def RecordGroup(level,module,grant):

	indent = TAB * level
	b.write((indent + '<record id="%s">\n' % (module + '.' + grant,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="name">%s</column>\n' % (module + '.' + grant,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="note">Module %s grant %s</column>\n' % (module,grant)).encode('utf-8'))
	b.write((indent + '</record>\n').encode('utf-8'))

def RecordRole(level,module,model,grant):

	indent = TAB * level

	b.write((indent + '<record id="%s">\n' % (model + '.' + grant,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="name">%s</column>\n' % (model + '.' + grant,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="note">Model %s grant %s</column>\n' % (model,grant)).encode('utf-8'))
	b.write((indent + TAB + '<column name="group_id">%s</column>\n' % (module + '.' + grant,)).encode('utf-8'))
	b.write((indent + '</record>\n').encode('utf-8'))

def RecordsRole(level,module,models):

	indent = TAB * level

	b.write((indent + '<records model="%s">\n' % ('bc.access',)).encode('utf-8'))
	for model in models:
		for grant in GRANTS:
			RecordRole(level+1,module,model._name,grant)
	b.write((indent + '</records>\n').encode('utf-8'))

def RecordAccess(level,module,model,grant):

	indent = TAB * level

	b.write((indent + '<record id="%s">\n' % (module + '.' + model + '.' + grant,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="access_id">%s</column>\n' % (model + '.' + grant,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="model_id">%s</column>\n' % (model,)).encode('utf-8'))
	for column in ACCESS[grant]:
		b.write((indent + TAB + '<column name="%s">True</column>\n' % (column,)).encode('utf-8'))
		
	b.write((indent + '</record>\n').encode('utf-8'))


def RecordsAccess(level,module,models):

	indent = TAB * level

	b.write((indent + '<records model="%s">\n' % ('bc.model.access',)).encode('utf-8'))
	for model in models:
		for grant in GRANTS:
			RecordAccess(level+1,module,model._name,grant)
	b.write((indent + '</records>\n').encode('utf-8'))


def Group(level,module):
	
	indent = TAB * level
	
	b.write((indent + '<records model="%s">\n' % ('bc.group.access',)).encode('utf-8'))
	for grant in GRANTS:
		RecordGroup(level+1,module,grant)

	b.write((indent + '</records>\n').encode('utf-8'))


def Role(level,module,models):
	RecordsRole(level,module,models)

def Access(level,module,models):
	RecordsAccess(level,module,models)

def Area(registry, modules = None, context={}):
	pwd = os.getcwd()
	pool = registry._models
	log = []
	if not modules:
		modules = registry._depends
	else:
		modules = list(filter(lambda x: x in modules,registry._depends))
	logmodules = []
	for module in modules:
		path = registry._modules[module]['path']
		models = []
		module_models = registry._create_module_models(module)
		for model in module_models.keys():
			mm = module_models[model]
			if isinstance(mm,Model):
				if hasattr(mm,'_inherit') and not getattr(mm,'_inherit',None):
					models.append(mm)

		if len(models) > 0:
			b.write('<?xml version="1.0" encoding="utf-8" standalone="yes" ?>\n'.encode('utf-8'))
			b.write((TAB+'<gsrp>\n').encode('utf-8'))
			b.write((TAB * 2 + '<data>\n').encode('utf-8'))
			Group(3, module)
			Role(3,module,models)
			Access(3,module,models)
			b.write((TAB * 2 + '</data>\n').encode('utf-8'))
			b.write((TAB + '</gsrp>\n').encode('utf-8'))
			f=open(opj(path,module,'views','roles.xml'),'wb')
			f.write(b.getvalue())
			f.close()
			b.seek(0,0)
			b.truncate(0)
			logmodules.append(module)
	log.append('Gen roles of modules %s' % (logmodules,))
	_logger.info('Gen roles of modules %s' % (logmodules,))
	return log

