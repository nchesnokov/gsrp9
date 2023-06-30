import os
import sys
import time
import logging
from functools import reduce
from tools.translations import trlocal as _
#from . import mm
from .mm import orm_exception
from .mm import Access

_logger = logging.getLogger(__name__)

class MetaReport(type):
	__modules__ = {}

	def __new__(cls, name, bases, attrs):
		if '__module__' in attrs and not attrs['__module__'] in ('gsrp5service.orm.report.MetaReport','orm.report.MetaReport','report.MetaReport','gsrp5service.orm.report','gsrp5service.orm'):
			_m = attrs['__module__'].split('.')
			_module = attrs['__module__']

			if _m[0] == 'gsrp5service':
				_module = reduce(lambda x,y: x + '.' + y,attrs['__module__'].split('.')[3:5])	
			else:	
				_module = reduce(lambda x,y: x + '.' + y,attrs['__module__'].split('.')[:2])	

			MetaReport.__modules__.setdefault(_module,{})[attrs['_name']] = {'name':name,'bases':bases,'attrs':attrs}

		return super(MetaReport, cls).__new__(cls, name, bases, attrs)

	def __init__(self, name, bases, attrs):
		if not hasattr(self, '_register'):
			setattr(self,'_register',True)
		else:
			self._register = True
			super(MetaReport, self).__init__(name, bases, attrs)

class Report(object, metaclass = MetaReport):
	_name = None
	_colums = {}
	_action = []
	_join = {}
	
	def __init__(self,access = None, attrs = None, proxy = None):
		self. _access = access
		
		for key in filter(lambda x: x not in ('name','columns','action','join','access','proxy'),attrs.keys()):
			setattr(self,'_'+ key,attrs[key])
		
		self._proxy = proxy
		
	def execute(self,cond):
		pass

class ReportInherit(object, metaclass = MetaReport):
	_name = None

class ReportProxy(object):
	_methods = {}
	
	def __init__(self,session):
		self._methods['call'] = session._call
		self._methods['cr'] = session._cursor
		self._methods['uid'] = session._uid
		self._methods['get'] = session._getModel
		self._methods['lib'] = session._getLib
		self._methods['navigate'] = session._getNavigate
	
	def __getattr__(self,name):
		if name in self._methods:
			return self._methods[name]
