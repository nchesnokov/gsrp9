import os
import logging
from os.path import join as opj
import csv
import yaml
import datetime
from datetime import date,time,datetime

from gsrp5service.orm.model import Model, ModelInherit

_logger = logging.getLogger('listener.' + __name__)

def _download_i18n(path,module,models):
	import polib

	po = polib.POFile()
	po.metadata = {
	    'Project-Id-Version': '1.0',
	    'Report-Msgid-Bugs-To': 'admin@gsrp5lab.com',
	    'POT-Creation-Date': '%s' % (datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S%z"),),
	    'PO-Revision-Date': '%s' % (datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S%z"),),
	    'Last-Translator': 'you <translater@yandex.ru>',
	    'Language-Team': 'English <translaterteam@yandex.ru>',
	    'MIME-Version': '1.0',
	    'Content-Type': 'text/plain; charset=utf-8',
	    'Content-Transfer-Encoding': '8bit',
	}
	mt = {}
	oc = []
	for model in models:
		msgid = model._description
		mt.setdefault(msgid,[]).append(('model@'+model._name + '|_description@', 1))
		if model.__doc__:
			msgid = model.__doc__
			mt.setdefault(msgid,[]).append(('model@'+model._name + '|__doc__@', 1))

		ci = model.columnsInfo(attributes=['label','selections','manual','help'])
		for k in ci.keys():
			if ci[k]['label'] is None:
				msgid = 'Unknown'
			else:
				msgid = ci[k]['label']
			
			mt.setdefault(msgid,[]).append(('model@'+model._name+'|_columns@'+k+'$label', 1))
			if 'selections' in ci[k] and ci[k]['selections']:
				for ks1,ks2 in ci[k]['selections']:
					msgid = ks2
					mt.setdefault(msgid,[]).append(('model@'+model._name+'|_columns@'+k+'$selections#'+ks1, 1))

			if 'manual' in ci[k] and ci[k]['manual']:
				msgid = ci[k]['manual']
				mt.setdefault(msgid,[]).append(('model@'+model._name+'|_columns@'+k+'$manual', 1))

			if 'help' in ci[k] and ci[k]['help']:
				msgid = ci[k]['help']
				mt.setdefault(msgid,[]).append(('model@'+model._name+'|_columns@'+k+'$help', 1))


	for k in mt.keys():
			
		entry = polib.POEntry(
		    msgid=k,
		    msgstr=u'',
		    occurrences=mt[k]
		)
		po.append(entry)
	

	_logger.info('Gen 18Ns write file: %s models: %s' % (opj(path,module,'i18n','po.pot'),len(models)));
	
	po.save(opj(path,module,'i18n','po.pot'))

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
			for cat in filter(lambda x: x in ('dashboards','models','views','reports','wizards'),registry._metas[module].keys()):
				for key in registry._metas[module][cat]:
					obj = registry._create_module_object(cat,key,module)
					if isinstance(obj,Model):
						objs.setdefault(cat,[]).append(obj)
					elif isinstance(obj,ModelInherit):
						if hasattr(obj,'_inherit') and getattr(obj,'_inherit',None):
							iobjs.setdefault(cat,[]).append(obj)

		if len(objs) + len(iobjs) > 0:
			for cat in objs.keys():
				if cat == 'models':
					if len(objs[cat]) > 0:
						_download_i18n(path,module,objs[cat])
			logmodules.append(module)



	# for module in modules:
		# path = registry._modules[module]['path']
		# models = []
		# imodels = []
		# module_models = registry._create_module_models(module)
		# for model in module_models.keys():
			# mm = module_models[model]
			# if isinstance(mm,Model):
				# models.append(mm)
			# elif isinstance(mm,ModelInherit):
				# if hasattr(mm,'_inherit') and getattr(mm,'_inherit',None):
					# imodels.append(mm)
		
		# if len(models) > 0:
			# # + len(imodels) > 0:
			# _download_i18n(path,module,models)
			# logmodules.append(module)

	_logger.info('Download i18ns of modules %s' % (logmodules,))
	
	return ['Download i18ns of modules %s' % (logmodules,)]


def Area2(registry, modules = None):
	pwd = os.getcwd()
	if not modules:
		modules = registry._depends
	else:
		modules = list(filter(lambda x: x in modules,registry._depends))
	logmodules = []
	for module in filter(lambda x:'state' in registry._modules[x] and registry._modules[x]['state'] == 'I',modules):
		path = registry._modules[module]['path']
		models = []
		for model in registry._momm[module].keys():
			if model in registry._models and registry._models[model]._inherit is None:
				models.append(model)


		if len(models) > 0:
			_download_i18n(path,module,models)
			logmodules.append(module)
	_logger.info('Download i18ns of modules %s' % (logmodules,))
	
	return ['Download i18ns of modules %s' % (logmodules,)]


