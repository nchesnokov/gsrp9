import os
import logging
from functools import reduce
from os.path import join as opj
from io import BytesIO
from .views import isAllow,VIEWSGEN
from gsrp5service.orm.model import Model

import html

b = BytesIO()
TAB = '  '

_logger = logging.getLogger('listener.' + __name__)

def RecordActions(level,module,model,modinfo,key,cat):

	indent = TAB * level
	if isAllow(key,modinfo):
		b.write((indent + '<record id="%s">\n' % ('action.' + model + '.' + key,)).encode('utf-8'))
		b.write((indent + TAB + '<column name="name">%s</column>\n' % ('action.' + model + '.' + key,)).encode('utf-8'))
		b.write((indent + TAB + '<column name="ta">%s</column>\n' % (cat,)).encode('utf-8'))		
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


def RecordMenuItems(level,pool,models,key,menu):

	indent = TAB * level

	b.write((indent + '<records model="%s">\n' % ('bc.ui.menus',)).encode('utf-8'))
	for idx,model in enumerate(models):
		label = model._description
		# d = model._description.split(' ')
		# if len(d) == 1:
			# label = d[0]
		# elif len(d) == 2:
			# label = d[0] + ' ' + d[1]
		# else:
			# label = reduce(lambda x,y:x + ' ' + y,d[2:])

		if isAllow(key,model.modelInfo()):
			RecordMenuItem(level + 1,idx,model._name,key,label,menu)
	b.write((indent + '</records>\n').encode('utf-8'))

def RecordMenuItem(level,idx,model,key,label,menu):

	indent = TAB * level

	b.write((indent + TAB + '<record id="%s">\n' % ('ui.menu.' + model + '.' + key,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="sequence">%s</column>\n' % (idx,)).encode('utf-8'))
	b.write((indent + TAB * 2 + '<column name="name">%s</column>\n' % ('ui.menu.' + model + '.' + key,)).encode('utf-8'))
	b.write((indent + TAB * 2 + '<column name="label">%s</column>\n' % (label,)).encode('utf-8'))
	if menu:
		b.write((indent + TAB + '<column name="parent_id">%s</column>\n' % (menu,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="sequence">%s</column>\n' % (idx * 10,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="action_id">%s</column>\n' % ('action.' + model + '.' + key,)).encode('utf-8'))

	b.write((indent + TAB + '</record>\n').encode('utf-8'))

def RecordReport(level,idx,module,model,label):

	indent = TAB * level

	b.write((indent + '<record id="%s">\n' % ('bc.ui.report.docx.' + model,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="name">%s</column>\n' % ('bc.ui.report.docx.' + model,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="label">%s</column>\n' % (label,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="report">%s</column>\n' % ('report.' + model,)).replace('.','_').encode('utf-8'))
	b.write((indent + TAB + '<column name="infile">%s</column>\n' % (('infile.' + model).replace('.','_') + '.docx',)).encode('utf-8'))
	b.write((indent + TAB + '<column name="outfile">%s</column>\n' % (('outfile.' + model).replace('.','_') + '.docx',)).encode('utf-8'))
	b.write((indent + '</record>\n').encode('utf-8'))

def RecordsReport(level,pool,module,models):

	indent = TAB * level

	b.write((indent + '<records model="%s">\n' % ('bc.ui.reports',)).encode('utf-8'))
	for idx,model in enumerate(models):
		description = model._description
		# d = model._description.split(' ')
		# if len(d) == 1:
			# description = d[0]
		# elif len(d) == 2:
			# description = d[0] + ' ' + d[1]
		# else:
			# description = reduce(lambda x,y:x + ' ' + y,d[2:])

		if isAllow('report',model.modelInfo()):
			RecordReport(level + 1,idx,module,model._name,description)
	b.write((indent + '</records>\n').encode('utf-8'))


def View(level,idx,module,model,label,key):

	indent = TAB * level

	#key = 'search'
	b.write((indent + '<record id="%s">\n' % ('view.action.' + model + '.' + key,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="action_id">%s</column>\n' % ('action.' + model + '.' + key,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="view_id">%s</column>\n' % ('view.' + model + '.' + key,)).encode('utf-8'))
	b.write((indent + '</record>\n').encode('utf-8'))

def Views(level,pool,module,models,key):

	indent = TAB * level

	b.write((indent + '<records model="%s">\n' % ('bc.view.actions',)).encode('utf-8'))
	for idx,model in enumerate(models):
		description = model._description
		# d = model._description.split(' ')
		# if len(d) == 1:
			# description = d[0]
		# elif len(d) == 2:
			# description = d[0] + ' ' + d[1]
		# else:
			# description = reduce(lambda x,y:x + ' ' + y,d[2:])

		if isAllow(key,model.modelInfo()):
			View(level + 1,idx,module,model._name,description,key)
	b.write((indent + '</records>\n').encode('utf-8'))

def Report(level,idx,module,model,label):

	indent = TAB * level

	key = 'report'
	b.write((indent + '<record id="%s">\n' % ('report.action.' + model + '.' + key,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="action_id">%s</column>\n' % ('action.' + model + '.' + key,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="report_id">%s</column>\n' % ('bc.ui.report.docx.' + model,)).encode('utf-8'))
	b.write((indent + '</record>\n').encode('utf-8'))

def Reports(level,pool,module,models):

	indent = TAB * level

	b.write((indent + '<records model="%s">\n' % ('bc.report.actions',)).encode('utf-8'))
	for idx,model in enumerate(models):
		description = model._description
		# d = model._description.split(' ')
		# if len(d) == 1:
			# description = d[0]
		# elif len(d) == 2:
			# description = d[0] + ' ' + d[1]
		# else:
			# description = reduce(lambda x,y:x + ' ' + y,d[2:])

		if isAllow('report',model.modelInfo()):
			Report(level + 1,idx,module,model._name,description)
	b.write((indent + '</records>\n').encode('utf-8'))

#
def Custom(level,idx,module,model,label,key):

	indent = TAB * level

	#key = 'search'
	b.write((indent + '<record id="%s">\n' % ('view.action.' + model + '.' + key,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="action_id">%s</column>\n' % ('action.' + model + '.' + key,)).encode('utf-8'))
	b.write((indent + TAB + '<column name="view_id">%s</column>\n' % ('view.' + model + '.' + 'search',)).encode('utf-8'))
	b.write((indent + '</record>\n').encode('utf-8'))

def Customs(level,pool,module,models,key):

	indent = TAB * level

	b.write((indent + '<records model="%s">\n' % ('bc.view.actions',)).encode('utf-8'))
	for idx,model in enumerate(models):
		description = model._description
		# d = model._description.split(' ')
		# if len(d) == 1:
			# description = d[0]
		# elif len(d) == 2:
			# description = d[0] + ' ' + d[1]
		# else:
			# description = reduce(lambda x,y:x + ' ' + y,d[2:])

		if isAllow(key,model.modelInfo()):
			Custom(level + 1,idx,module,model._name,description,key)
	b.write((indent + '</records>\n').encode('utf-8'))

#
def ViewActions(level,pool,module,models,key,cat):
	
	indent = TAB * level
	
	b.write((indent + '<records model="%s">\n' % ('bc.actions',)).encode('utf-8'))
	for model in models:
		RecordActions(level+1,module,model._name,model.modelInfo(),key,cat)

	b.write((indent + '</records>\n').encode('utf-8'))

def Area(cr, pool, uid, registry, modules = None, context={}):
	pwd = os.getcwd()
	log = []
	if 	not modules:
		modules = registry._depends
	else:
		modules = list(filter(lambda x: x in modules,registry._depends))
	logmodules = []
	for module in modules:
		path = registry._modules[module]['path']
		label = registry._modules[module]['meta']['name']
		models = []
		cust_models = []
		module_models = registry._create_module_models(module)
		for model in module_models.keys():
			mm = module_models[model]
			if isinstance(mm,Model):
				info = mm.modelInfo()	
				if len(list(filter(lambda x: 'selectable' in info['columns'][x] and info['columns'][x]['selectable'] and 'rec_name' in info['names'] and info['names']['rec_name'],info['columns'].keys()))) > 0:
					if 'class_model' in info and info['class_model'] == 'A':
						models.append(mm)
					elif 'class_model' in info and info['class_model'] == 'C':
						cust_models.append(mm)
		if len(models) > 0 or len(cust_models) > 0:
			b.write('<?xml version="1.0" encoding="utf-8" standalone="yes" ?>\n'.encode('utf-8'))
			b.write((TAB+'<gsrp>\n').encode('utf-8'))
			b.write((TAB * 2 + '<data>\n').encode('utf-8'))
			RecordMenu(3,'ui.menu.'+module,label)
			if len(models) > 0:
				ViewActions(3, pool,module,models,'search','View')
				ViewActions(3, pool,module,models,'report','Report')
				Views(3,pool,module,models,'search')
				RecordsReport(3,pool,module,models)
				Reports(3,pool,module,models)
				RecordMenuItems(3,pool,models,'search','ui.menu.'+module)			
				RecordMenu(3,'ui.menu.'+module+'.report','Reports','ui.menu.'+module)
				RecordMenuItems(3,pool,models,'report','ui.menu.'+module+'.report')
			if len(cust_models) > 0:
				#print('CUST_MODELS:',cust_models)
				ViewActions(3, pool,module,cust_models,'custom','View')
				Customs(3,pool,module,cust_models,'custom')
				RecordMenu(3,'ui.menu.'+module+'.custom','Customs','ui.menu.'+module)
				RecordMenuItems(3,pool,cust_models,'custom','ui.menu.'+module+'.custom')		

				ViewActions(3, pool,module,cust_models,'report','Report')
				RecordsReport(3,pool,module,cust_models)
				Reports(3,pool,module,cust_models)
				RecordMenu(3,'ui.menu.'+module+'.report.custom','Customs','ui.menu.'+module+'.report')
				RecordMenuItems(3,pool,cust_models,'report','ui.menu.'+module+'.report.custom')

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

