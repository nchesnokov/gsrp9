# -*- coding: utf-8 -*-

import base64
import decimal
from psycopg2 import Binary
import datetime as DT
import pytz
import logging

_logger = logging.getLogger(__name__)

def _set_symbol(self, symb):
	if symb is None or symb == False:
		return None
	return str(symb)

class _column(object):

	__slots__ = ('__dict__','accept','actions','label', 'column', 'readonly','invisible', 'priority', 'domain', 'context', 'pattern','required', 'size', 'on_delete', 'on_update','on_change','on_check', 'translate', 'selections', 'selectable', 'manual', 'help', 'unique','check','family','timezone','relatedy','obj','rel','id1','id2','ref','offset','limit','compute','store','state','icon','cols','delimiter','model')

	def __init__(self, **kwargs):

		if len(kwargs) == 0:
			raise AttributeError

		for key in kwargs.keys():
			if key in self.__slots__ and key != "__dict__":			
				if 'store' in kwargs and not kwargs['store']:
					if 'required' in kwargs:
						kwargs['required'] = False
					if 'selectable' in kwargs:
						kwargs['selectable'] = False
						
		for key in kwargs.keys():
			if key in self.__slots__ and key != "__dict__":
				setattr(self,key,kwargs[key])
			else:
				self.__dict__[key] = kwargs[key]

	def __contains__(self, name):
		if name != "__dict__" and name in self.__slots__:
			return True
		else:
			if name == "__dict__":
				return True
			else:
				return False

	def _get_symbol_c(self):
		if hasattr(self, '_symbol_c'):
			return self._symbol_set[0]
		else:
			raise AttributeError

	def _get_symbol_f(self, value):
		if hasattr(self, '_symbol_f'):
			return self._symbol_set[1](value)
		else:
			raise AttributeError

	def _get_attrs(self, attrs = None):
		result = {}

		if not attrs:
			attrs = list(self.__slots__[1:]) + list(self.__dict__.keys())

		for attr in attrs:
			if attr in self.__dict__:
				if attr == 'column':
					result[attr] = self._get_attrs(attrs)
				else:
					result[attr] = self.__dict__[attr]
			else:
				prefix = ''
				if attr in ('type','db_type','symbol_c','symbol_f','symbol_set','symbol_get'):
					prefix = '_'
				if hasattr(self,prefix + attr):
					result[attr] = getattr(self,prefix + attr,None)

		if hasattr(self,'_type') and not 'type' in result:
			result['type'] = self._type
		if hasattr(self,'_db_type') and not 'db_type' in result:
			result['db_type'] = self._db_type
		if 'symbol_c' in attrs and hasattr(self,'_symbol_c') and not 'symbol_c' in result:
			result['symbol_c'] = self._symbol_c
		if 'symbol_f' in attrs and hasattr(self,'_symbol_f') and not 'symbol_f' in result:
			result['symbol_f'] = self._symbol_f
		if 'symbol_set' in attrs and hasattr(self,'_symbol_set') and not 'symbol_set' in result:
			result['symbol_set'] = self._symbol_set
		if 'symbol_get' in attrs and hasattr(self,'_symbol_get') and not 'symbol.get' in result:
			result['symbol_get'] = self._symbol_get

		if 'readonly' in result:
			result['readonly'] = result['readonly'] or 'compute' in self.__dict__ and self.__dict__['compute'] and type(self.__dict__['compute']) in (list,tuple) 
		
		return result

class char(_column):
	_type = 'char'
	_db_type = 'STRING'
	_symbol_c = "%s"
	_symbol_f = _set_symbol
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = None

	def __init__(self, label = 'unknown', readonly = None, invisible = None, pattern = None, priority = 0, context = {}, required = None, size = 32, on_change = None, on_check=None, translate = False, selectable = False, domain=None, manual = None, help = None, unique = False, check = None,family = 'Primary',compute = None, store = True,state=None, actions=None, icon = None):
		super(char, self).__init__(label=label, readonly=readonly, invisible=invisible, pattern = pattern, priority=priority, context=context, required = required, size = size, on_change = on_change, on_check = on_check, translate = translate, selectable = selectable, domain=domain, manual = manual, help=help, unique = unique, check = check,family = family,compute = compute, store = store, state = state, actions = actions,icon = icon)

class varchar(_column):
	_type = 'varchar'
	_db_type = 'STRING'
	_symbol_c = "%s"
	_symbol_f = _set_symbol
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = None

	def __init__(self, label = 'unknown', readonly = None, invisible = None, pattern = None,priority = 0, context = {}, required = None, size = None, on_change = None, on_check = None, translate = False, selectable = False, domain=None, manual = None, help = None, unique = None, check = None,family = 'Primary',compute = None, store = True,state=None, actions=None, icon = None):
		super(varchar, self).__init__(label=label, readonly=readonly, invisible=invisible, pattern=pattern, priority=priority, context=context, required = required, size = size, on_change = on_change, translate = translate, selectable = selectable, domain=domain, manual = manual, help=help, unique = unique, check = check,family = family,compute = compute, store = store, state = state, actions = actions,icon = icon)

class composite(_column):
	_type = 'composite'
	_db_type = 'STRING'
	_symbol_c = "%s"
	_symbol_f = _set_symbol
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = None

	def __init__(self, label = 'unknown', cols = [], delimiter = '/',readonly = None, invisible = None, pattern = None,priority = 0, context = {}, required = None, size = None, on_change = None, on_check = None, translate = False, selectable = False, domain=None, manual = None, help = None, unique = None, check = None,family = 'Primary', store = True,state=None, actions=None, icon = None):
		super(composite, self).__init__(label=label, cols = cols, delimiter = delimiter, readonly=readonly, invisible=invisible, pattern=pattern, priority=priority, context=context, required = required, size = size, on_change = on_change, translate = translate, selectable = selectable, domain=domain, manual = manual, help=help, unique = unique, check = check,family = family,compute = '_compute_composite', store = store, state = state, actions = actions, icon = icon)

class tree(_column):
	_type = 'tree'
	_db_type = 'STRING'
	_symbol_c = "%s"
	_symbol_f = _set_symbol
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = None

	def __init__(self, label = 'unknown', parent = None, delimiter = '/',readonly = None, invisible = None, pattern = None,priority = 0, context = {}, required = None, size = None, on_change = None, on_check = None, translate = False, selectable = False, domain=None, manual = None, help = None, unique = None, check = None,family = 'Primary', store = True,state=None, actions=None, icon = None):
		super(tree, self).__init__(label=label, parent = parent, delimiter = delimiter, readonly=readonly, invisible=invisible, pattern=pattern, priority=priority, context=context, required = required, size = size, on_change = on_change, translate = translate, selectable = selectable, domain=domain, manual = manual, help=help, unique = unique, check = check,family = family,compute = '_compute_composite_tree', store = store, state = state, actions = actions, icon = icon)



class decomposite(_column):
	_type = 'decomposite'
	_db_type = 'STRING'
	_symbol_c = "%s"
	_symbol_f = _set_symbol
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = None

	def __init__(self, label = 'unknown', col = None, delimiter = '/', part=None, readonly = None, invisible = None, pattern = None,priority = 0, context = {}, required = None, size = None, on_change = None, on_check = None, translate = False, selectable = False, domain=None, manual = None, help = None, unique = None, check = None,family = 'Primary', store = False, state=None, actions=None, icon = None):
		super(decomposite, self).__init__(label=label, part = part, delimiter = delimiter, readonly=readonly, invisible=invisible, pattern=pattern, priority=priority, context=context, required = required, size = size, on_change = on_change, translate = translate, selectable = selectable, domain=domain, manual = manual, help=help, unique = unique, check = check,family = family,compute = '_compute_decomposite', store = store, state = state, actions = actions, icon = icon)



class text(_column):
	_type = 'text'
	_db_type = 'STRING'
	_symbol_c = "%s"
	_symbol_f = _set_symbol
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = None

	def __init__(self, label = 'unknown', readonly = None, invisible = None, priority = 0, context = {}, required = None, on_change = None, on_check = None, translate = False, manual = None, help = None,family = 'Secondary',compute = None, store = True,state=None, actions=None, icon = None):
		super(text,self).__init__(label = label, readonly = readonly, invisible=invisible, priority = priority, context = context, required = required, on_change = on_change, on_check = on_check, translate = translate, manual = manual, help = help, family = family,compute = compute, store = store, state = state, actions = actions,icon = icon)

class xml(_column):
	_type = 'xml'
	_db_type = 'STRING'
	_symbol_c = "%s"
	_symbol_f = _set_symbol
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = None

	def __init__(self, label = 'unknown', readonly = None, invisible = None, priority = 0, context = {}, required = None, on_change = None, on_check = None,translate = False, manual = None, help = None,family = 'Secondary',compute = None, store = True,state=None, actions=None, icon = None):
		super(xml,self).__init__(label = label, readonly = readonly, invisible = invisible,priority = priority, context = context, required = required, on_change = on_change, on_check = on_check, translate = translate, manual = manual, help= help,family = family,compute = compute, store = store, state = state, actions = actions,icon = icon)

class i18n(_column):
	_type = 'i18n'

	def __init__(self, column, store = True):
		super(i18n, self).__init__(column=column, store = store)
	

class boolean(_column):
	_type = 'boolean'
	_db_type = 'BOOL'
	_symbol_c = "%s"
	_symbol_f = lambda x: x and 'True' or 'False'
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = None

	def __init__(self, label = 'unknown', readonly = None, invisible = None, priority = 0, context = {}, required = None, on_change = None, on_check = None, manual = None, help = None, selectable = None,family = 'Primary',compute = None, store = True,state=None, actions=None, icon = None):
		super(boolean,self).__init__(label = label, readonly = readonly, invisible=invisible,priority = priority, context = context, required = required, on_change = on_change, on_check = on_check, manual = manual, help = help, selectable=selectable, family = family, compute = compute, store = store, state = state, actions = actions, icon = icon)

class uuid(_column):
	_type = 'uuid'
	_db_type = 'UUID'
	_symbol_c = "%s"
	_symbol_f = _set_symbol
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = None

	def __init__(self, label = 'unknown', readonly = None, invisible = None, pattern = None,priority = 0, context = {}, required = None, size = None, on_change = None, translate = False, manual = None, help = None, unique = None, check = None,family = 'Primary', compute = None, store = True,state=None, actions=None, icon = None):
		super(uuid, self).__init__(label=label, readonly=readonly, invisible = invisible, pattern=pattern, priority=priority, context=context, required = required, size = size, on_change = on_change, translate = translate, manual = manual, help=help, unique = unique, check = check,family = family, compute = compute, store = store, state = state, actions = actions, icon = icon)

class integer(_column):
	_type = 'integer'
	_db_type = 'INT'
	_symbol_c = "%s"
	_symbol_f = lambda x: int(x or 0)
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = lambda self, x: x or 0

	def __init__(self, label = 'unknown', readonly = None, invisible = None, priority = 0, context = {}, required = None, on_change = None, on_check = None, manual = None, help = None, check = None,family = 'Primary', compute = None, store = True,state=None, actions=None, icon = None):
		super(integer,self).__init__(label = label, readonly = readonly, invisible = invisible, priority = priority, context = context, required = required, on_change = on_change, on_check = on_check, manual = manual, help = help, check = check,family = family, compute = compute, store = store, state = state, actions = actions, icon = icon)

class float(_column):
	_type = 'float'
	_db_type = 'FLOAT'
	_symbol_c = "%s"
	_symbol_f = lambda x: float(x) or 0.0
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = lambda self, x: x or 0.0

	def __init__(self, label = 'unknown', readonly = None, invisible = None, priority = 0, context = {}, required = None, size = (15), on_change = None, on_check = None, manual = None, help = None, check = None,family = 'Primary', compute = None, store = True,state=None, actions=None, icon = None):
		super(float,self).__init__(label = label, readonly = readonly, invisible = invisible, priority = priority, context = context, required = required, size = size, on_change = on_change, on_check = on_check, manual = manual, help = help, check = check,family = family, compute = compute, store = store, state = state, actions = actions, icon = icon)

class real(_column):
	_type = 'real'
	_db_type = 'REAL'
	_symbol_c = "%s"
	_symbol_f = lambda x: float(x) or 0.0
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = lambda self, x: x or 0.0

	def __init__(self, label = 'unknown', readonly = None, invisible = None, priority = 0, context = {}, required = None, on_change = None, on_check = None, manual = None, help = None, check = None,family = 'Primary', compute = None, store = True,state=None, actions=None, icon = None):
		super(real,self).__init__(label = label, readonly = readonly, invisible = invisible, priority = priority, context = context, required = required, on_change = on_change, on_check = on_check, manual = manual, help = help, check = check,family = family, compute = compute, store = store, state = state, actions = actions, icon = icon)


class double(_column):
	_type = 'double'
	_db_type = 'DOUBLE PRECISION'
	_symbol_c = "%s"
	_symbol_f = lambda x: float(x) or 0.0
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = lambda self, x: x or 0.0

	def __init__(self, label = 'unknown', readonly = None, invisible = None, priority = 0, context = {}, required = None, on_change = None, on_check = None, manual = None, help = None, check = None,family = 'Primary', compute = None, store = True,state=None, actions=None, icon = None):
		super(double,self).__init__(label = label, readonly = readonly, invisible = invisible, priority = priority, context = context, required = required, on_change = on_change, on_check = on_check, manual = manual, help = help, check = check,family = family, compute = compute, store = store, state = state, actions = actions, icon = icon)

class decimal(_column):
	_type = 'decimal'
	_db_type = 'DECIMAL'
	_symbol_c = "%s"
	_symbol_f = lambda x: decimal.Decimal(x) or decimal.Decimal('0.0')
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = lambda self, x: decimal.Decimal(x) or decimal.Decimal('0.0')

	def __init__(self, label = 'unknown', readonly = None, invisible = None, priority = 0, context = {}, required = None, size = (15,3), on_change = None, on_check = None, manual = None, help = None, check = None,family = 'Primary', compute = None, store = True,state=None, actions=None, icon = None):
		super(decimal,self).__init__(label = label, readonly = readonly, invisible = invisible, priority = priority, context = context, required = required, size = size, on_change = on_change, on_check = on_check, manual = manual, help = help, check = check,family = family, compute = compute, store = store, state = state, actions = actions, icon = icon)

class numeric(_column):
	_type = 'numeric'
	_db_type = 'DECIMAL'
	_symbol_c = "%s"
	_symbol_f = lambda x: decimal.Decimal(x) or decimal.Decimal('0.0')
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = lambda self, x: decimal.Decimal(x) or decimal.Decimal('0.0')

	def __init__(self, label = 'unknown', readonly = None, invisible = None, priority = 0, context = {}, required = None, size = (15,3), on_change = None, on_check = None, manual = None, help = None, check=None,family = 'Primary', compute = None, store = True,state=None, actions=None, icon = None):
		super(numeric,self).__init__(label = label, readonly = readonly, invisible = invisible, priority = priority, context = context, required = required, size =size, on_change = on_change, on_check = on_check, manual = manual, help = help,check = check,family = family, compute = compute, store = store, state = state, actions = actions, icon = icon)

class selection(_column):
	_type = 'selection'
	_db_type = 'STRING'
	_symbol_c = "%s"
	_symbol_f = _set_symbol
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = None

	def __init__(self, label = 'unknown', selections = [],readonly = None, invisible = None, priority = 0, context = {}, required = None, size = 32, on_change = None, on_check = None, translate = False, selectable = False, manual = None, help = None, unique = None,family = 'Primary', compute = None, store = True,state=None, actions=None, icon = None):
		super(selection,self).__init__(label = label, selections = selections,readonly = readonly, invisible = invisible, priority = priority, context = context, required = required, size = size, on_change = on_change, on_check = on_check, translate = translate, selectable = selectable, manual = manual, help = help, unique = unique,family = family, compute = compute, store = store, state = state, actions = actions, icon = icon)

# class iSelection(_column):
	# _type = 'iSelection'
	# _db_type = None
	# _symbol_c = "%s"
	# _symbol_f = _set_symbol
	# _symbol_set = (_symbol_c, _symbol_f)
	# _symbol_get = None

	# def __init__(self, selections = []):
		# super(iSelection,self).__init__(selections = selections)

class binary(_column):
	_type = 'binary'
	_db_type = 'BYTES'
	_symbol_c = "%s"
	_symbol_f = lambda symb: symb and Binary(str(symb)) or None
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = lambda self, x: x and str(x)

	def __init__(self, label = 'unknown', readonly = None, invisible = None, priority = 0, context = {}, required = None, on_change = None, on_check = None, accept = None,manual = None, help = None,family = 'Secondary', compute = None, store = True,state=None, actions=None):
		super(binary,self).__init__(label = label, readonly = readonly, invisible = invisible, priority = priority, context = context, required = required, on_change = on_change, on_check = on_check, accept=accept, manual = manual, help = help,family = family, compute = compute, store = store, state = state, actions = actions)

class icon(_column):
	_type = 'icon'
	_db_type = 'string'
	_symbol_c = "%s"
	_symbol_f = lambda symb: symb and Binary(str(symb)) or None
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = lambda self, x: x and str(x)

	def __init__(self, label = 'unknown', readonly = None, invisible = None, priority = 0, context = {}, required = None, on_change = None, on_check = None, accept = None,manual = None, help = None,family = 'Primary', compute = None, store = True,state=None, actions=None):
		super(icon,self).__init__(label = label, readonly = readonly, invisible = invisible, priority = priority, context = context, required = required, on_change = on_change, on_check = on_check, accept=accept, manual = manual, help = help,family = family, compute = compute, store = store, state = state, actions = actions)


class json(_column):
	_type = 'json'
	_db_type = 'JSONB'
	_symbol_c = "%s"
	_symbol_f = lambda symb: symb and str(symb) or None
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = lambda self, x: x and str(x)

	def __init__(self, label = 'unknown', readonly = None, invisible = None, priority = 0, context = {}, required = None, on_change = None, on_check = None, manual = None, help = None,family = 'Secondary', compute = None, store = True,state={'attrs':{'readonly':True}}, actions=None, icon = None):
		super(json,self).__init__(label = label, readonly = readonly, invisible = invisible, priority = priority, context = context, required = required, on_change = on_change, on_check = on_check, manual = manual, help = help,family = family, compute = compute, store = store, state = state, actions = actions, icon = icon)

class geometry(_column):
	_type = 'geometry'
	_db_type = 'GEOMETRY'
	_symbol_c = "%s"
	_symbol_f = lambda symb: symb and str(symb) or None
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = lambda self, x: x and str(x)

	def __init__(self, label = 'unknown', readonly = None, invisible = None, priority = 0, context = {}, required = None, on_change = None, on_check = None, manual = None, help = None,family = 'Secondary', compute = None, store = True,state={'attrs':{'readonly':True}}, actions=None, icon = None):
		super(geometry,self).__init__(label = label, readonly = readonly, invisible = invisible, priority = priority, context = context, required = required, on_change = on_change, on_check = on_check, manual = manual, help = help,family = family, compute = compute, store = store, state = state, actions = actions, icon = icon)

class geography(_column):
	_type = 'geography'
	_db_type = 'GEOGRAPHY'
	_symbol_c = "%s"
	_symbol_f = lambda symb: symb and str(symb) or None
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = lambda self, x: x and str(x)

	def __init__(self, label = 'unknown', readonly = None, invisible = None, priority = 0, context = {}, required = None, on_change = None, on_check = None, manual = None, help = None,family = 'Secondary', compute = None, store = True,state={'attrs':{'readonly':True}}, actions=None, icon = None):
		super(geography,self).__init__(label = label, readonly = readonly, invisible = invisible, priority = priority, context = context, required = required, on_change = on_change, on_check = on_check, manual = manual, help = help,family = family, compute = compute, store = store, state = state, actions = actions, icon = icon)


class date(_column):
	_type = 'date'
	_db_type = 'DATE'
	_symbol_c = "%s"
	_symbol_f = lambda symb: symb or None
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = lambda self, x: x and str(x)

	def __init__(self, label = 'unknown', readonly = None, invisible = None, priority = 0, context = {}, required = None, on_change = None, on_check = None, manual = None, help = None,check =  None,family = 'Primary', compute = None, store = True,state=None, actions=None, icon = None):
		super(date,self).__init__(label = label, readonly = readonly, invisible = invisible, priority = priority, context = context, required = required, on_change = on_change, on_check = on_check, manual = manual, help = help,check = check,family = family, compute = compute, store = store, state = state, actions = actions, icon = icon)

	def today(self):
		return DT.datetime.today().strftime("YYYY-MM-DD")

	def context_today(self, timestamp = None, context = None):
		assert isinstance(timestamp, DT.datetime), 'Datetime instance expected'

		today = timestamp or DT.datetime.now()
		context_today = None

		if context and context.get('tz'):
			tz_name = context['tz']
		if tz_name:
			try:
				utc = pytz.timezone('UTC')
				context_tz = pytz.timezone(tz_name)
				utc_today = utc.localize(today, is_dst=False) # UTC = no DS
				context_today = utc_today.astimezone(context_tz)
			except Exception:
				_logger.debug("failed to compute context/client-specific today date, "
							  "using the UTC value for `today`",
							  exc_info=True)
		return (context_today or today).strftime("YYYY-MM-DD")


class datetime(_column):
	_type = 'datetime'
	_db_type = 'TIMESTAMP'
	_symbol_c = "%s"
	_symbol_f = None
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = None

	def __init__(self, label = 'unknown', readonly = None, invisible = None, timezone = True, priority = 0, context = {}, required = None, on_change = None, on_check = None, manual = None, help = None,check = None,family = 'Primary', compute = None, store = True,state=None, actions=None, icon = None):
		if timezone:
			self._db_type = 'TIMESTAMP WITH TIME ZONE'
		else:
			self._db_type = 'TIMESTAMP WITHOUT TIME ZONE'
		super(datetime,self).__init__(label = label, readonly = readonly, invisible = invisible, timezone = timezone, priority = priority, context = context, required = required, on_change = on_change, on_check = on_check, manual = manual, help = help,check = check,family = family, compute = compute, store = store, state = state, actions = actions, icon = icon)

	def now(self):
		if self.tz:
			return DT.datetime.now().strftime("YYYY-MM-DD HH:MM:SS%z")
		else:
			return DT.datetime.now().strftime("YYYY-MM-DD HH:MM:SS")

	def context_timestamp(self, timestamp, context):
		assert isinstance(timestamp, DT.datetime), 'Datetime instance expected'
		if context and context.get('tz'):
			tz_name = context['tz']
		if tz_name:
			try:
				utc = pytz.timezone('UTC')
				context_tz = pytz.timezone(tz_name)
				utc_timestamp = utc.localize(timestamp, is_dst=False) # UTC = no DS
				return utc_timestamp.astimezone(context_tz)
			except Exception:
				_logger.debug("failed to compute context/client-specific timestamp, "
							  "using the UTC value",
							  exc_info=True)
		return timestamp

class time(_column):
	_type = 'time'
	_db_type = 'TIME'
	_symbol_c = "%s"
	_symbol_f = lambda symb: symb and Binary(str(symb)) or None
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = lambda self, x: x and str(x)

	def __init__(self, label = 'unknown', readonly = None, invisible = None, timezone = True, priority = 0, context = {}, required = None, on_change = None, on_check = None, manual = None, help = None,family = 'Primary', compute = None, store = True,state=None, actions=None, icon = None):
		if timezone:
			self._db_type = 'TIME WITH TIME ZONE'
		else:
			self._db_type = 'TIME WITHOUT TIME ZONE'
		super(time,self).__init__(label = label, readonly = readonly, invisible = invisible, timezone = timezone, context = context, required = required, on_change = on_change, on_check = on_check, manual = manual, help = help,family = family, compute = compute, store = store, state = state, actions = actions, icon = icon)

	def time(self):
		return DT.datetime.now().strftime("YYYY-MM-DD")

	def context_time(self, timestamp = None, context = None):
		assert isinstance(timestamp, DT.datetime), 'Datetime instance expected'

		today = timestamp or DT.datetime.now()
		context_today = None

		if context and context.get('tz'):
			tz_name = context['tz']
		if tz_name:
			try:
				utc = pytz.timezone('UTC')
				context_tz = pytz.timezone(tz_name)
				utc_today = utc.localize(today, is_dst=False) # UTC = no DS
				context_today = utc_today.astimezone(context_tz)
			except Exception:
				_logger.debug("failed to compute context/client-specific today date, "
							  "using the UTC value for `today`",
							  exc_info=True)
		return (context_today or today).strftime("YYYY-MM-DD")

class timedelta(_column):
	_type = 'timedelta'
	_db_type = 'INTERVAL'
	_symbol_c = "%s"
	_symbol_f = lambda symb: symb and Binary(str(symb)) or None
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = lambda self, x: x and str(x)

	def __init__(self, label = 'unknown', readonly = None, invisible = None, priority = 0, context = {}, required = None, on_change = None, manual = None, on_check = None, help = None,family = 'Primary', compute = None, store = True,state=None, actions=None, icon = None):
		super(timedelta,self).__init__(label = label, readonly = readonly, invisible = invisible, context = context, required = required, on_change = on_change, on_check = on_check, manual = manual, help = help,family = family, compute = compute, store = store, state = state, actions = actions, icon = icon)

	def timedelta(self):
		return DT.datetime.timedelta().strftime("YYYY-MM-DD HH:MM:SS")

	def context_timedelta(self, timestamp = None, context = None):
		assert isinstance(timestamp, DT.datetime), 'Datetime instance expected'

		today = timestamp or DT.datetime.now()
		context_today = None

		if context and context.get('tz'):
			tz_name = context['tz']
		if tz_name:
			try:
				utc = pytz.timezone('UTC')
				context_tz = pytz.timezone(tz_name)
				utc_today = utc.localize(today, is_dst=False) # UTC = no DS
				context_today = utc_today.astimezone(context_tz)
			except Exception:
				_logger.debug("failed to compute context/client-specific today date, "
							  "using the UTC value for `today`",
							  exc_info=True)
		return (context_today or today).strftime("YYYY-MM-DD")

class one2many(_column):
	_type = 'one2many'
	_db_type = None
	def __init__(self, label='unknown', obj = None, rel = None, readonly = None, invisible = None, required = None, on_change = None, on_check = None, context = {}, offset = None, limit=None, manual = None, help = None,state=None, icon = None):
		super(one2many,self).__init__(label = label, obj = obj, rel = rel, readonly = readonly, invisible = invisible, required = required, on_change = on_change, on_check = on_check, context = context, offset = offset,limit = limit, manual = manual,help = help, state = state, icon = icon)

class one2related(_column):
	_type = 'one2related'
	_db_type = None
	def __init__(self, label='unknown', obj = None, relatedy=None, rel = None, readonly = None, invisible = None, required = None, on_change = None, on_check = None, context = {}, offset = None, limit=None, manual = None, help = None,state=None, icon = None):
		super(one2many,self).__init__(label = label, obj = obj, relatedy=relatedy, rel = rel, readonly = readonly, invisible = invisible, required = required, on_change = on_change, on_check = on_check, context = context, offset = offset,limit = limit, manual = manual,help = help, state = state, icon = icon)


class many2one(_column):
	_type = 'many2one'
	_db_type = 'UUID'
	_symbol_c = '%s'
	_symbol_f = lambda x: x or None
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = None
	def __init__(self,label='unknown', obj = None, rel = None, readonly = None, invisible = None, required = None,priority = 0, ext_fields = None, domain = None, context = {}, on_change = None, on_check = None, selectable = True, on_delete = None, on_update = None, manual = None, help = None,family = 'Primary', compute = None, store = True,state=None, icon = None):
		super(many2one,self).__init__(label = label, obj = obj, rel = rel, readonly = readonly, invisible = invisible, required = required,priority = priority, ext_fields = ext_fields, domain = domain, context = context, on_change = on_change, on_check = on_check, selectable = selectable, on_delete = on_delete, on_update = on_update, manual = manual, help = help,family = family, compute = compute, store = store, state = state, icon = icon)

class one2one(_column):
	_type = 'one2one'
	_db_type = 'UUID'
	_symbol_c = '%s'
	_symbol_f = lambda x: x or None
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = None
	def __init__(self,label='unknown', obj = None, readonly = None, invisible = None, required = None, ext_fields = None, domain = None, context = {}, on_change = None, on_check = None, selectable = True, on_delete = None, on_update = None, manual = None, help = None,family = 'Primary', compute = None, store = True,state=None, icon = None):
		super(one2one,self).__init__(label = label, obj = obj, readonly = readonly, invisible = invisible, required = required, ext_fields = ext_fields, domain = domain, context = context, on_change = on_change, on_check = on_check, selectable = selectable, on_delete = on_delete, on_update = on_update, manual = manual, help = help,family = family, compute = compute, store = store, state = state, icon = icon)

class many2many(_column):
	_type = 'many2many'
	_db_type = None
	def __init__(self, label='unknown', obj = None, rel = None, id1 = None, id2 = None, readonly = None, invisible = None, required = None, on_change = None, on_check = None, manual = None, help = None,offset = None,limit=None, domain = None,state=None):
		super(many2many,self).__init__(label = label, obj = obj, rel = rel, id1 = id1, id2 = id2, readonly = readonly, invisible = invisible, required = required, on_change = on_change, on_check = on_check, manual=manual, help = help, domain = domain, state = state)

class related(_column):
	_type = 'related'
	_db_type = 'UUID'
	_symbol_c = '%s'
	_symbol_f = lambda x: x or None
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = None
	def __init__(self,label='unknown', obj = None, relatedy=None, readonly = None, invisible = None, required = None,priority = 0, domain = None, context = {}, on_change = None, on_check = None, selectable = True, on_delete = None, on_update = None, manual = None, help = None,family = 'Primary', compute = None, store = True,state=None, icon = None):
		super(related,self).__init__(label = label, obj = obj, relatedy=relatedy, readonly = readonly, invisible = invisible, required = required,priority = priority, domain = domain, context = context,on_change = on_change, on_check = on_check,selectable = selectable, on_delete = on_delete, on_update = on_update, manual = manual, help = help,family = family, compute = compute, store = store, state = state, icon = icon)

class referenced(_column):
	_type = 'referenced'
	_db_type = 'UUID'
	_symbol_c = '%s'
	_symbol_f = lambda x: x or None
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = None
	def __init__(self,label='unknown', obj = None, readonly = None, invisible = None, required = None,priority = 0, ext_fields = None, domain = None, context = {}, on_change = None, on_check = None, selectable = True, on_delete = None, on_update = None, manual = None, help = None,family = 'Primary', compute = None, store = True,state=None, icon = None):
		super(referenced,self).__init__(label = label, obj = obj , readonly = readonly, invisible = invisible, required = required,priority = priority, ext_fields = ext_fields, domain = domain, context = context, on_change = on_change, on_check = on_check, selectable = selectable, on_delete = on_delete, on_update = on_update, manual = manual, help = help,family = family, compute = compute, store = store, state = state, icon = icon)



class link(_column):
	_type = 'link'
	_db_type = None
	_symbol_c = '%s'
	_symbol_f = lambda x: x or None
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = None
	def __init__(self,label=None,ref = None, state = None, invisible = None):
		super(link,self).__init__(label=label,ref = ref,readonly=True,state=state, invisible = invisible, store = False)

class columnRef(_column):
	_type = 'columnRef'
	def __init__(self,model, column,label=None):
		super(columnRef,self).__init__(model=model,column=column,label=label)

class iProperty(_column):
	_type = 'iProperty'
	_db_type = None
	_symbol_c = "%s"
	_symbol_f = _set_symbol
	_symbol_set = (_symbol_c, _symbol_f)
	_symbol_get = None

	def __init__(self, *args,**kwargs):
		super(iProperty,self).__init__(*args,**kwargs)

