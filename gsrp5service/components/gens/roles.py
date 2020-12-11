import os
import logging
from os.path import join as opj
from io import BytesIO
from .common import concat
from gsrp5service.orm.model import Model
import web_pdb

b = BytesIO()
TAB = '  '

GRANTS = ('readonly','nodrop','full','crw')
ACCESS = {'readonly':['aread'],'nodrop':['aread','acreate','awrite',],'full':['aread','acreate','awrite','aunlink','aexecute'],'crw':['aread','acreate','awrite','aexecute']}

_logger = logging.getLogger('listener.' + __name__)

def RecordGroup(level,module,grant,cat):

	indent = TAB * level
	nm = concat([module,cat,grant])
	b.write((indent + '<record id="%s">\n' % (nm,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="name">%s</column>\n' % (nm,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="note">Module %s Type Object %s grant %s</column>\n' % (module,cat,grant)).encode('utf-8'))
	b.write((indent + '</record>\n').encode('utf-8'))

def RecordRole(level,module,obj,grant,cat):

	indent = TAB * level

	nm = concat(['role',module,cat,obj,grant])
	b.write((indent + '<record id="%s">\n' % (nm,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="name">%s</column>\n' % (nm,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="note">Module: %s Type: %s Object: %s grant: %s</column>\n' % (module,cat,obj,grant)).encode('utf-8'))
	b.write((indent + TAB + '<column name="group_id">%s</column>\n' % (concat([module,cat,grant]),)).encode('utf-8'))
	b.write((indent + '</record>\n').encode('utf-8'))

def RecordsRole(level,module,objs,cat):

	indent = TAB * level

	b.write((indent + '<records model="%s">\n' % ('bc.access',)).encode('utf-8'))
	for obj in objs:
		for grant in GRANTS:
			RecordRole(level+1,module,obj._name,grant,cat)
	b.write((indent + '</records>\n').encode('utf-8'))

def RecordAccess(level,module,obj,grant, cat):

	indent = TAB * level
	nm = concat(['access',module,cat,obj,grant])
	b.write((indent + '<record id="%s">\n' % (nm,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="access_id">%s</column>\n' % (nm,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="object_id">%s</column>\n' % (obj,)).encode('utf-8'))
	for column in ACCESS[grant]:
		b.write((indent + TAB + '<column name="%s">True</column>\n' % (column,)).encode('utf-8'))
		
	b.write((indent + '</record>\n').encode('utf-8'))


def RecordsAccess(level,module,objs,cat):

	indent = TAB * level

	b.write((indent + '<records model="%s">\n' % ('bc.obj.access',)).encode('utf-8'))
	for obj in objs:
		for grant in GRANTS:
			RecordAccess(level+1,module,obj._name,grant,cat)
	b.write((indent + '</records>\n').encode('utf-8'))


def Group(level,module,cat):
	
	indent = TAB * level
	
	b.write((indent + '<records model="%s">\n' % ('bc.group.access',)).encode('utf-8'))
	for grant in GRANTS:
		RecordGroup(level+1,module,grant,cat)

	b.write((indent + '</records>\n').encode('utf-8'))


def Role(level,module,objs,cat):
	RecordsRole(level,module,objs,cat)

def Access(level,module,objs,cat):
	RecordsAccess(level,module,objs,cat)

def Area(self, modules = None, context={}):
	pwd = os.getcwd()
	registry = self._registry
	log = []
	if not modules:
		modules = registry._depends
	else:
		modules = list(filter(lambda x: x in modules,registry._depends))
	logmodules = []
	for module in modules:
		path = registry._modules[module]['path']
		objs = {}
		if module in registry._metas:
			for cat in filter(lambda x: x in ('dashboards','models','views','reports','wizards'),registry._metas[module].keys()):
				for key in registry._metas[module][cat]:
					obj = registry._create_module_object(cat,key,module)
					if isinstance(obj,Model):
						if hasattr(obj,'_inherit') and not getattr(obj,'_inherit',None):
							objs.setdefault(cat,[]).append(obj)

		if len(objs) > 0:
			b.write('<?xml version="1.0" encoding="utf-8" standalone="yes" ?>\n'.encode('utf-8'))
			b.write((TAB+'<gsrp>\n').encode('utf-8'))
			b.write((TAB * 2 + '<data>\n').encode('utf-8'))
			Group(3, module,cat)
			for cat in objs.keys():
				Role(3,module,objs[cat],cat)
				Access(3,module,objs[cat],cat)
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

