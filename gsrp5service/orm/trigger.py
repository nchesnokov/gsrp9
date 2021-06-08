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
	
class TriggerInherit(object, metaclass = MetaObjects):
	_name = None
