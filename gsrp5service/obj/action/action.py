import os
import sys
import time
import logging
from functools import reduce
from gsrp5service.obj.metaobjects import MetaObjects
from tools.translations import trlocal as _

_logger = logging.getLogger(__name__)

class Action(object, metaclass = MetaObjects):
	_name = None

class ActionInherit(object, metaclass = MetaObjects):
	_name = None
