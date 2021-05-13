import os
import logging
from os.path import join as opj
import yaml
from yaml import Dumper
import csv
from .views import isAllow
from .common import concat
from gsrp5service.orm.model import Model
import web_pdb


_logger = logging.getLogger('listener.' + __name__)


#FRAMEWORKS = ('element-plus','vuetify','devextrme')
FRAMEWORKS = ('element-plus',)

def FrameworkRecordAction(framework,model,action):
	return {'framework_id':framework,'action_id': action,'view_id':concat([model,framework,'search'],'/')}


def RecordAction(model):
	return {'name': concat(['action',model,'search']),'model':model}


def RecordMenu(name,label,parent=None):
	record = {'name':name,'label':label}
	#if parent:
	record['parent_id'] = parent
	
	return record

def RecordMenuItem(idx,module,model,label,menu):
	record = {'sequence':idx,'name': concat(['ui.menu',model,'search']),'label':label,'action_id':concat(['action',model,'search'])}
	if menu:
		record['parent_id'] = menu
	
	return record

#

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
		models = []
		cust_models = []
		if module in registry._metas:
			for key in registry._metas[module]['models'].keys():
				obj = registry._create_module_object('models',key,module)
				if isinstance(obj,Model):
					info = obj.modelInfo()	
					if len(isAllow('search','models',info,list(info['columns'].keys()))) > 0:
						if 'class_model' in info and info['class_model'] in ('A','B','K'):
							models.append(obj)
						elif 'class_model' in info and info['class_model'] in ('C','E'):
							cust_models.append(obj)

		if len(models) > 0 or len(cust_models) > 0:
			res_menu =[]
			res_actions = []
			res_framework_actions = []

			if module == 'bc':
				res_menu.append(RecordMenu(concat(['ui','menu','customize']),'Customizing'))

			if len(models) > 0:
				res_menu.append(RecordMenu(concat(['ui','menu','module',module]),label))
				for idx,model in enumerate(models):
					action = RecordAction(model._name)
					res_actions.append(action)
					res_menu.append(RecordMenuItem(idx,module,model._name,model._description,concat(['ui','menu','module',module])))
					for framework in FRAMEWORKS:
						res_framework_actions.append(FrameworkRecordAction(framework,model._name,action['name']))

						
			if len(cust_models) > 0:
				res_menu.append(RecordMenu(concat(['ui','menu','customize',module]),label,concat(['ui','menu','customize'])))
				for idx,cust_model in enumerate(cust_models):
					action = RecordAction(cust_model._name)
					res_actions.append(action)
					res_menu.append(RecordMenuItem(idx,module,cust_model._name,cust_model._description,concat(['ui','menu','customize',module])))
					for framework in FRAMEWORKS:
						res_framework_actions.append(FrameworkRecordAction(framework,cust_model._name,action['name']))
			
			if len(res_menu) + len(res_actions) + len(res_framework_actions) > 0:
				if not os.path.exists(opj(path,module,'views','menus')):
					os.mkdir(opj(path,module,'views','menus'))
		
				a = open(opj(path,module,'views','menus.csv'),'w')
				aw = csv.DictWriter(a,['model','file'])
				aw.writeheader()
				if len(res_actions) > 0:
					with open(opj(path,module,'views','menus','ui.model.actions'.replace('.','_') + '.yaml'),'w') as outfile:
						yaml.dump(res_actions, outfile, Dumper, default_flow_style=False)
					aw.writerow({'model': 'bc.ui.model.actions','file':opj('views','menus','ui.model.actions'.replace('.','_') + '.yaml' )})

				if len(res_menu) > 0:
					with open(opj(path,module,'views','menus','ui.model.menus'.replace('.','_') + '.yaml'),'w') as outfile:
						yaml.dump(res_menu, outfile, Dumper, default_flow_style=False)
					aw.writerow({'model': 'bc.ui.model.menus','file':opj('views','menus','ui.model.menus'.replace('.','_') + '.yaml' )})

				if len(res_framework_actions) > 0:
					with open(opj(path,module,'views','menus','ui.framework.model.actions'.replace('.','_') + '.yaml'),'w') as outfile:
						yaml.dump(res_framework_actions, outfile, Dumper, default_flow_style=False)
					aw.writerow({'model': 'bc.ui.framework.model.actions','file':opj('views','menus','ui.framework.model.actions'.replace('.','_') + '.yaml' )})


			logmodules.append(module)
	log.append('Gen menus of modules %s' % (logmodules,))
	_logger.info('Gen menus of modules %s' % (logmodules,))
	return log

