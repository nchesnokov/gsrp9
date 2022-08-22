import logging
import web_pdb
from passlib.hash import pbkdf2_sha256
from functools import reduce
from datetime import datetime
from lxml import etree
import os
import csv
import yaml
import json
import polib
from yaml import Loader
from os.path import join as opj
import toposort
import copy
from . import genddl
from gsrp5service.orm.model import Model,ModelInherit,Access

__all__ = ['install','uninstall','upgrade','sysinstall','sysupgrade','upgrademoduleslist','load']

_logger = logging.getLogger('listener.' + __name__)

class XMLValidator(Exception): pass

class KeyBuffer(dict):
	
	def add(self,key,obj,recordkey,value):
		self.setdefault(key,{}).setdefault(obj,{})[recordkey] = value

	def key(self,key,obj,recordkey):
		if key in self  and obj in self[key] and recordkey in self[key][obj]:
			return self[key][obj][recordkey]  
		return None

def loadModel(proxy,module,options,context):
	#['module','depends','env','view','example','data','demo','test','i18n']
	if 'meta' in options:
		loadModelMeta(proxy,module,options,context)
	if 'env' in options:
		loadModelEnv(proxy,module,options,context)
	if 'i18n' in options:
		loadModelI18N(proxy,module,options,context)
	if 'view' in options:
		loadModelView(proxy,module,options,context)
	if 'test' in options:
		loadModelTest(proxy,module,options,context)
	if 'data' in options:
		loadModelData(proxy,module,options,context)
	if 'demo' in options:
		loadModelDemo(proxy,module,options,context)
	if 'example' in options:
		if 'data' not in options:
			loadModelData(proxy,module,options,context)
		if 'demo' in options:
			loadModelDemo(proxy,module,options,context)

def createModel(proxy,model,module,options,context):
	createTables(proxy,model,module,options,context)

def createModels(proxy,module,options,context):
	for model in models:
		log.append([0,'model: <%s> creating' % (model,)])
		rc,errors = createModel(proxy, model, module, options[model] if model in options[model] else {}, context)
		if rc:
			log.append([0,'module: <%s> successfull installed' % (module,)])
		else:
			log.append([0,'module: <%s> installed errors: %s' % (module,errors)])
			return rc,errors
		
	return True
	

def installModule(proxy,modules=None, options=None, context={}):
	if 'models' in options['models']:
		createModels(proxy['models'],module,options['models'],context)

def installModules(proxy,modules=None, options=None, context={}):
	for module in modules:
		log.append([0,'module: <%s> installing' % (module,)])
		rc,errors = installModule(proxy, module, options, context)
		if rc:
			log.append([0,'module: <%s> successfull installed' % (module,)])
		else:
			log.append([0,'module: <%s> installed errors: %s' % (module,errors)])
			return rc,errors
		
	return True
