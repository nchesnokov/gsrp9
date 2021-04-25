import os
import logging
from os.path import join as opj
from io import BytesIO
from .views import isAllow
from .common import concat
from gsrp5service.orm.model import Model
import web_pdb

import html

b = BytesIO()
TAB = '  '

_logger = logging.getLogger('listener.' + __name__)

_info_objs = {'dashbords':'dashboardInfo','models':'modelInfo','views':'viewInfo'}

_action_cat = {'dashboards':'Dashboard','models':'Model','views':'View','reports':'Report','izards':'Wizard','links':'Link'}

_view_cat = {'models':'search'}

def RecordActions(level,module,obj,key,cat):

	indent = TAB * level
	for view in VIEWSGEN[cat].keys():
		if isAllow(view,cat,getattr(obj,_info_objs[cat],None)()):
			nm = concat(['action',module,cat,key,view])
			b.write((indent + '<record id="%s">\n' % (nm,)).encode('utf-8'))
			b.write((indent + TAB + '<column name="name">%s</column>\n' % (nm,)).encode('utf-8'))
			b.write((indent + TAB + '<column name="ta">%s</column>\n' % (_action_cat[cat],)).encode('utf-8'))		
			b.write((indent + '</record>\n').encode('utf-8'))


def RecordMenu(level,name,label,parent=None):

	indent = TAB * level

	b.write((indent + '<records model="%s">\n' % ('bc.ui.menus',)).encode('utf-8'))
	b.write((indent + TAB + '<record id="%s">\n' % (name,)).encode('utf-8'))
	b.write((indent + TAB * 2 + '<column name="name">%s</column>\n' % (html.escape(name) ,)).encode('utf-8'))
	b.write((indent + TAB * 2 + '<column name="label">%s</column>\n' % (html.escape(label),)).encode('utf-8'))
	if parent:
		b.write((indent + TAB + '<column name="parent_id">%s</column>\n' % (html.escape(parent),)).encode('utf-8'))
	b.write((indent + TAB + '</record>\n').encode('utf-8'))
	b.write((indent + '</records>\n').encode('utf-8'))


def RecordMenuItems(level,module,objs,cat,menu):

	indent = TAB * level

	b.write((indent + '<records model="%s">\n' % ('bc.ui.menus',)).encode('utf-8'))
	for idx,obj in enumerate(objs):
		label = obj._description
		_view_cat = {'models':'search'}
		#for view in VIEWSGEN[cat].keys():
		if isAllow(_view_cat[cat],cat,getattr(obj,_info_objs[cat],None)()):
			RecordMenuItem(level + 1,idx,module,concat([obj._name,_view_cat[cat]]),cat,label,menu)
	b.write((indent + '</records>\n').encode('utf-8'))

def RecordMenuItem(level,idx,module,key,cat,label,menu):

	indent = TAB * level
	nm = concat(['ui.menu',cat,key])
	b.write((indent + TAB + '<record id="%s">\n' % (nm,)).encode('utf-8'))
	b.write((indent + TAB * 2 + '<column name="sequence">%s</column>\n' % (idx,)).encode('utf-8'))
	b.write((indent + TAB * 2 + '<column name="name">%s</column>\n' % (nm,)).encode('utf-8'))
	b.write((indent + TAB * 2 + '<column name="label">%s</column>\n' % (html.escape(label),)).encode('utf-8'))
	if menu:
		b.write((indent + TAB * 2 + '<column name="parent_id">%s</column>\n' % (menu,)).encode('utf-8'))
	nma = concat(['action',module,cat,key])
	b.write((indent + TAB * 2 + '<column name="action_id">%s</column>\n' % (nma,)).encode('utf-8'))

	b.write((indent + TAB + '</record>\n').encode('utf-8'))

#

def Actions(level,module,objs):
	
	indent = TAB * level
	
	b.write((indent + '<records model="%s">\n' % ('bc.actions',)).encode('utf-8'))
	for cat in objs.keys():
		for obj in objs[cat]:
			RecordActions(level+1,module,obj,obj._name,cat)

	b.write((indent + '</records>\n').encode('utf-8'))

def RecordObj(level,module,obj,cat,view):

	indent = TAB * level
	
	nm = concat(['action',module,cat,obj._name,view])
	nmv = concat(['view',module,cat,obj._name,view])
	b.write((indent + '<record id="%s">\n' % (concat(['view.action',module,cat,obj._name,view]),)).encode('utf-8'))
	b.write((indent + TAB + '<column name="action_id">%s</column>\n' % (nm,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="view_id">%s</column>\n' % (nmv,)).encode('utf-8'))
	b.write((indent + '</record>\n').encode('utf-8'))

def Objs(level,module,objs):
	indent = TAB * level

	b.write((indent + '<records model="%s">\n' % ('bc.view.actions',)).encode('utf-8'))
	for cat in objs.keys():
		for obj in objs[cat]:
			view = _view_cat[cat]
			if isAllow(view,cat,getattr(obj,_info_objs[cat],None)()):
				RecordObj(level + 1,module,obj,cat,view)
	b.write((indent + '</records>\n').encode('utf-8'))

def Area(self, modules = None, context={}):
	pwd = os.getcwd()
	pool = self._models
	registry = self._registry
	log = []
	if 	not modules:
		modules = registry._depends
	else:
		modules = list(filter(lambda x: x in modules,registry._depends))
	logmodules = []
	for module in modules:
		path = registry._modules[module]['path']
		label = registry._modules[module]['meta']['name']
		objs = {}
		cust_objs = {}
		if module in registry._metas:
			for cat in filter(lambda x: x in ('dashboards','models','views','reports','wizards','link','wkf'),registry._metas[module].keys()):
				for key in registry._metas[module][cat].keys():
					obj = registry._create_module_object(cat,key,module)
					if isinstance(obj,Model):
						info = obj.modelInfo()	
						if len(list(filter(lambda x: 'selectable' in info['columns'][x] and info['columns'][x]['selectable'] and 'rec_name' in info['names'] and info['names']['rec_name'],info['columns'].keys()))) > 0:
							if 'class_model' in info and info['class_model'] in ('A','B','K'):
								objs.setdefault(cat,[]).append(obj)
							elif 'class_model' in info and info['class_model'] in ('C','E'):
								cust_objs.setdefault(cat,[]).append(obj)

		if len(objs) > 0 or len(cust_objs) > 0:
			b.write('<?xml version="1.0" encoding="utf-8" standalone="yes" ?>\n'.encode('utf-8'))
			b.write((TAB+'<gsrp>\n').encode('utf-8'))
			b.write((TAB * 2 + '<data>\n').encode('utf-8'))
			if module == 'bc':
				RecordMenu(3,concat(['ui','menu','customize']),'Customizing')
			if len(objs) > 0:
				RecordMenu(3,concat(['ui','menu','module',module]),label)
				Actions(3, module,objs)
				Objs(3,module,objs)				
				for cat in objs.keys():
					RecordMenu(3,concat(['ui','menu','module',module,cat]),cat.title(),concat(['ui','menu','module',module]))
					RecordMenuItems(3,module,objs[cat],cat,concat(['ui','menu','module',module,cat]))
			if len(cust_objs) > 0:
				RecordMenu(3,concat(['ui','menu','customize',module]),label,concat(['ui','menu','customize']))
				Actions(3, module,cust_objs)				
				Objs(3,module,cust_objs)
				for cat in cust_objs.keys():
					RecordMenu(3,concat(['ui','menu','customize',module,cat]),cat.title(),concat(['ui','menu','customize',module]))
					RecordMenuItems(3,module,cust_objs[cat],cat,concat(['ui','menu','customize',module,cat]))

			b.write((TAB * 2 + '</data>\n').encode('utf-8'))
			b.write((TAB + '</gsrp>\n').encode('utf-8'))
			f=open(opj(path,module,'views','menus.xml'),'wb')
			f.write(b.getvalue())
			f.close()
			b.seek(0,0)
			b.truncate(0)
			logmodules.append(module)
	log.append('Gen menus of modules %s' % (logmodules,))
	_logger.info('Gen menus of modules %s' % (logmodules,))
	return log

