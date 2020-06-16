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
	
class ReportInherit(object, metaclass = MetaReport):
	_name = None
