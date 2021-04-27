import os
import logging
from os.path import join as opj
import csv
import yaml
from yaml import Dumper
from .common import concat
from gsrp5service.orm.model import Model
import web_pdb

GRANTS = ('readonly','nodrop','full','crw')
ACCESS = {'readonly':['aread'],'nodrop':['aread','acreate','awrite',],'full':['aread','acreate','awrite','aunlink','aexecute'],'crw':['aread','acreate','awrite','aexecute']}

_logger = logging.getLogger('listener.' + __name__)

def RecordGroup(module,grant,cat):
	return {'name': concat([module,cat,grant]),'note':"Module %s Type Object %s grant %s" % (module,cat,grant)}

def RecordRole(module,model,grant,cat):
	return {'name':concat(['role',module,cat,model,grant]),'note':"Module: %s Type: %s Object: %s grant: %s" % (module,cat,model,grant),'group_id':concat([module,cat,grant])}

def RecordsRole(module,models,cat):
	res = []
	for model in models:
		for grant in GRANTS:
			res.append({model._name:RecordRole(module,model._name,grant,cat)})
	
	return res
	
def RecordAccess(module,model,grant, cat):
	cols = {'access_id':concat(['role',module,cat,model,grant]),'object_id': model}
	for column in ACCESS[grant]:
		cols[column] = True
	
	return cols
	

def RecordsAccess(module,models,cat):
	res = []
	for model in models:
		for grant in GRANTS:
			res.append(RecordAccess(module,model._name,grant,cat))
	
	return res

def Group(module,cat):
	res = []
	for grant in GRANTS:
		res.append(RecordGroup(module,grant,cat))

	return res

def Role(module,models,cat):
	return RecordsRole(module,models,cat)

def Access(module,models,cat):
	return RecordsAccess(module,models,cat)

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
		models = []
		if module in registry._metas:
				for key in registry._metas[module]['models']:
					model = registry._create_module_object('models',key,module)
					if isinstance(model,Model):
						if hasattr(model,'_inherit') and not getattr(model,'_inherit',None):
							models.append(model)

		if len(models) > 0:
			res_group = Group(module,'models')
			#web_pdb.set_trace()
			res_roles = Role(module,models,'models')
			res_access = Access(module,models,'models')
			if len(res_group) + len(res_roles) + len(res_access) > 0:
				if not os.path.exists(opj(path,module,'views','roles')):
					os.mkdir(opj(path,module,'views','roles'))
				a = open(opj(path,module,'views','roles.csv'),'w')
				aw = csv.DictWriter(a,['model','file'])
				aw.writeheader()

				if len(res_group) > 0:
					with open(opj(path,module,'views','roles','bc.group.access'.replace('.','_') + '.yaml'),'w') as outfile:
						yaml.dump(res_group, outfile, Dumper, default_flow_style=False)
					aw.writerow({'model': 'bc.group.access','file':opj('views','menus','bc.group.access'.replace('.','_') + '.yaml' )})

				if len(res_roles) > 0:
					with open(opj(path,module,'views','roles','bc.access'.replace('.','_') + '.yaml'),'w') as outfile:
						yaml.dump(res_roles, outfile, Dumper, default_flow_style=False)
					aw.writerow({'model': 'bc.access','file':opj('views','menus','bc.access'.replace('.','_') + '.yaml' )})

				if len(res_access) > 0:
					with open(opj(path,module,'views','roles','bc.model.access'.replace('.','_') + '.yaml'),'w') as outfile:
						yaml.dump(res_access, outfile, Dumper, default_flow_style=False)
					aw.writerow({'model': 'bc.model.access','file':opj('views','menus','bc.model.access'.replace('.','_') + '.yaml' )})

			logmodules.append(module)
	log.append('Gen roles of modules %s' % (logmodules,))
	_logger.info('Gen roles of modules %s' % (logmodules,))
	return log

