import os
import sys
import time
import logging
from functools import reduce
from .metaobjects import MetaObjects
from tools.translations import trlocal as _
#from . import mm
#from .mm import orm_exception
#from .mm import Access

_logger = logging.getLogger(__name__)


class Trigger(object, metaclass = MetaObjects):
	_name = None
	_actions = {}
	
	def __init__(self):
		for o in ('Read','Write','Create','Unlink'):
			for b in ('Before','After'):
				for a in ('ForEachRow','All'):
					n = '_on' + o + b + a
					if hasattr(self,n):
						method = getattr(self,n)
						if callable(method) and not (o in self._actions and b in self._actions[o] and a in self._actions[o][b] and n in self._actions[o][b][a] and callable(getattr(self,self._actions[o][b][a][n],None))):
							self._actions.setdefault(o,{}).setdefault(b,{}).setdefault(a,{})[n] = method
					else:
						self._actions.setdefault(o,{}).setdefault(b,{}).setdefault(a,{})[n] = None
		
class TriggerInherit(object, metaclass = MetaObjects):
	_name = None
