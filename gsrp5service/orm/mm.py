import os
#import uuid
import logging
import web_pdb
from copy import deepcopy
from functools import reduce
from .common import *
from .common import DEFAULT_MODEL_NAMES as DMN
from . import gensql
from gsrp5service.components.modules.genddl import getName
from io import StringIO
from datetime import datetime,date,time
import time as tm
from decimal import Decimal
from gsrp5service.orm.orm import Model


MAX_CHUNK_READ = 5000
MAX_CHUNK_DELETE = 5000

_logger = logging.getLogger(__name__)

_TRIGGERS_KEYS_ = ('bir',	'bur', 'bdr', 'air', 'aur', 'adr', 'bi', 'bu', 'bd', 'ai', 'au', 'ad')
_HOOKS_KEYS_ = ('bai',	'aai', 'bri', 'ari','bui','aui')


class orm_exception(Exception):
	def __init__(self, *args, **kwargs):
		self.args = args
		self.kwargs = kwargs

class Access(object):

	_create = None
	_read = None
	_write = None
	_unlink = None
	_modify = None
	_insert = None
	_select = None
	_update = None
	_delete = None
	_upsert = None
	_browse = None
	_selectbrowse = None
	
	_readonly = None
	
	def __init__(self, **kwargs):
		if self._readonly:
			return
		for key in kwargs.keys():
			if not key in ('readonly','_setattr__') and hasattr(self,'_' + key):
				setattr(self, '_' + key,kwargs[key])
		
		self._readonly = True

	def __setattr__(self,name,value):
		if self._readonly:
			return
		
		if name in ('__setattr__',):
			return
		super(Access,self).__setattr__(name,value)
			
	def _checkCreate(self):
		if self._create:
			return True
		return False

	def _checkRead(self):
		if self._read:
			return True
		return False

	def _checkWrite(self):
		if self._write:
			return True
		return False

	def _checkUnlink(self):
		if self._unlink:
			return True
		return False

	def _checkModify(self):
		if self._modify:
			return True
		return False

	def _checkInsert(self):
		if self._insert:
			return True
		return False

	def _checkSelect(self):
		if self._select:
			return True
		return False

	def _checkUpdate(self):
		if self._update:
			return True
		return False

	def _checkDelete(self):
		if self._delete:
			return True
		return False

	def _checkUpsert(self):
		if self._upsert:
			return True
		return False

	def _checkBrowse(self):
		if self._browse:
			return True
		return False

	def _checkSelectBrowse(self):
		if self._selectbrowse:
			return True
		return False

class browse_null(object):

	def __init__(self):
		self.id = False

	def __getitem__(self,name):
		return None

	def __getattr__(self,name):
		return None

	def __int__(self):
		return False

	def __str__(self):
		return ''

	def __nonzero__(self):
		return False

	def __unicode__(self):
		return u''

class browse_record_list(list): pass

class browse_record(object):

	def __init__(self, uid, vals):
		setattr(self,'uid',uid)

		for k in vals.keys():
			setattr(self,k,vals[k])

	def __str__(self,name):
		return str(self)

	def __repr__(self):
		return str(self)


def model__init__(self,access = None):
	
	self._schema = []
	self._levels = {}
		
	if not self._name and not hasattr(self, '_inherit'):
		name = type(self).__name__.split('.')[0]
		msg = "The class %s has to have a _name attribute" % (name,)

		_logger.error(msg)
		raise except_orm('ValueError', msg)

	if hasattr(self, '_list_columns'):
		for name,field in self._list_columns:
			self._columns[name] = field
		self._list_columns.clear()			
	
	if not self._description:
		self._description = self._name
	if self._transient:
		self._table = None
	else:
		if hasattr(self,'_table') and not self._table:
			self._table = self._name.replace('.', '_')

		if len(self._i18nfields) > 0 and hasattr(self,'_tr_table') and not self._tr_table:
			self._tr_table = self._name.replace('.', '_') + '_tr'


	if self._table and self._table[:3].lower() == 'pg_':
		raise orm_exception([_('Invalid table name'), self._table, self._name])

	if self._transient:
		self._log_access = False
	else:
		if not hasattr(self, '_log_access'):
		## If _log_access is not specified, it is the same value as _auto.
			self._log_access = getattr(self, "_auto", True)

	fullname = _getFullNameName(self)
	rec_name = _getRecNameName(self)
	row_name = _getRowNameName(self)
	complete_name = _getCompleteNameName(self)
	if not hasattr(self,'_rec_name'):
		self._rec_name = rec_name
	if not hasattr(self,'_full_name'):
		self._full_name = fullname
	if not hasattr(self,'_row_name'):
		self._row_name = row_name

	if rec_name and rec_name in self._nostorecomputefields:
		raise orm_exception(_('Recname: <%s> in model: %s must be store in database') % (rec_name, self._name))

	try:
		if rec_name  and hasattr(self._columns[rec_name],'selectable'):
			self._columns[rec_name].selectable = True
		elif rec_name  and self._columns[rec_name]._type == 'i18n' and hasattr(self._columns[rec_name].column,'selectable'):
			self._columns[rec_name].column.selectable = True
			
	except:
		print('EXCEPT:',self._name,self._row_name,self._rec_name,self._full_name,self._columns)

	if rec_name  and hasattr(self._columns[rec_name],'unique'):
		self._columns[rec_name].unique = True

	if rec_name and hasattr(self._columns[rec_name],'required'):
		self._columns[rec_name].required = True

	if fullname and fullname != rec_name and hasattr(self._columns[fullname],'selectable'):
		self._columns[fullname].selectable = True

	if rec_name and rec_name != fullname and hasattr(self._columns[rec_name],'selectable'):
		self._columns[rec_name].selectable = True

	state = _getStateName(self)
	if state and hasattr(self._columns[state],'selectable') and self._columns[state].selectable:
		self._columns[state]._selectable = True

	inactive = _getInactiveName(self)
	if inactive and hasattr(self._columns[inactive],'selectable') and self._columns[inactive].selectable:
		self._columns[inactive]._selectable = True
	
	if access:
		self._access = Access(access)
	
	if self._actions is None:
		self._actions = {}

	if self._checks is None:
		self._checks = []

	for sf in dir(self):
		if sf[:7] == '_action':
			if callable(getattr(self,sf,None)):
				if not sf in self._actions:
					self._actions[sf[7:]] = sf
		if sf[:6] == '_check':
			if callable(getattr(self,sf,None)):
				if not sf in self._checks:
					self._checks.append(sf)

def checkAccess(self,mode = None):
	if self._access and hasattr(self._access,'_' + mode):
		return getattr(self._access,'_' + mode,None)

def _getParentIdName(self):
	n = _getSpecName(self,'parent_id')
	if n:
		if self._columns[n]._type != 'many2one':
			n = None
	
	return n

def _getChildsIdName(self):
	n = _getSpecName(self,'childs_id')
	if n:
		if self._columns[n]._type != 'one2many':
			n = None

	return n

def _getRowNameName(self):
	n = _getSpecName(self,'row_name')
	if n:
		if not self._columns[n]._type in ('char','varchar','selection','composite','decomposite','tree','i18n'):
			n = None

	return n

def _getCompleteNameName(self):
	n = _getSpecName(self,'complete_name')
	if n:
		if not self._columns[n]._type in ('char','varchar','selection','composite','decomposite','tree','i18n'):
			n = None

	return n


def _getFullNameName(self):
	n = _getSpecName(self,'full_name')
	if n:
		if not self._columns[n]._type in ('char','varchar','composite','decomposite','tree','i18n'):
			n = None

	return n

def _getRecNameName(self):
	if hasattr(self,'_rec_name') and self._rec_name:
		return self._rec_name
	else:
		return _getCompleteNameName(self) or _getFullNameName(self) or _getRowNameName(self)

def _getSequenceName(self):
	n = _getSpecName(self,'sequence')
	if n:
		if self._columns[n]._type != 'integer':
			n = None

	return n

def _getDateName(self):
	n = _getSpecName(self,'date')
	if n:
		if not self._columns[n]._type in ('date','datetime'):
			n = None

	return n

def _getStartDateName(self):
	n = _getSpecName(self,'start_date')
	if n:
		if not self._columns[n]._type in ('date','datetime'):
			n = None

	return n

def _getEndDateName(self):
	n =  _getSpecName(self,'end_date')
	if n:
		if not self._columns[n]._type in ('date','datetime'):
			n = None

	return n
#
def _getFromDateName(self):
	n = _getSpecName(self,'from_date')
	if n:
		if not self._columns[n]._type in ('date','datetime'):
			n = None

	return n

def _getToDateName(self):
	n =  _getSpecName(self,'to_date')
	if n:
		if not self._columns[n]._type in ('date','datetime'):
			n = None

	return n

def _getFromTimeName(self):
	n = _getSpecName(self,'from_time')
	if n:
		if not self._columns[n]._type in ('time','datetime'):
			n = None

	return n

def _getToTimeName(self):
	n =  _getSpecName(self,'to_time')
	if n:
		if not self._columns[n]._type in ('time','datetime'):
			n = None

	return n

def _getProgressName(self):
	n = _getSpecName(self,'progress')
	if n:
		if not self._columns[n]._type in ('integer','flot','double','real','decimal','numeric'):
			n = None

	return n

def _getProjectTypeName(self):
	n = _getSpecName(self,'project_type')
	if n:
		if self._columns[n]._type != 'selection':
			n = None

	return n

#
def _getStateName(self):
	n = _getSpecName(self,'state')
	if n:
		if self._columns[n]._type != 'selection':
			n = None

	return n

def _getInactiveName(self):
	n = _getSpecName(self,'inactive')
	if n:
		if self._columns[n]._type != 'boolean':
			n = None

	return n

# geo start
def _getLatitudeName(self):
	n = _getSpecName(self,'latitude')
	if n:
		if not self._columns[n]._type in ('float','double','real','decimal','numeric'):
			n = None

	return n

def _getLongitudeName(self):
	n = _getSpecName(self,'longitude')
	if n:
		if not self._columns[n]._type in ('float','double','real','decimal','numeric'):
			n = None

	return n
# from
def _getFromLatitudeName(self):
	n = _getSpecName(self,'from_latitude')
	if n:
		if not self._columns[n]._type in ('float','double','real','decimal','numeric'):
			n = None

	return n

def _getFromLongitudeName(self):
	n = _getSpecName(self,'from_longitude')
	if n:
		if not self._columns[n]._type in ('float','double','real','decimal','numeric'):
			n = None

	return n

# to
def _getToLatitudeName(self):
	n = _getSpecName(self,'to_latitude')
	if n:
		if not self._columns[n]._type in ('float','double','real','decimal','numeric'):
			n = None

	return n

def _getToLongitudeName(self):
	n = _getSpecName(self,'to_longitude')
	if n:
		if not self._columns[n]._type in ('float','double','real','decimal','numeric'):
			n = None

	return n

# geo end

def _getPrevNameName(self):
	n = _getSpecName(self,'prev_name')
	if n:
		if not self._columns[n]._type in ('many2one','related'):
			n = None

	return n

def _getNextNameName(self):
	n = _getSpecName(self,'next_name')
	if n:
		if not self._columns[n]._type in ('many2one','related'):
			n = None

	return n

def _getTransitionsName(self):
	n = _getSpecName(self,'transitions')
	if n:
		if not self._columns[n]._type in ('one2many','one2related'):
			n = None

	return n

def _getMatrixNamesName(self):
	n = _getSpecName(self,'matrix_names')
	col_name = None
	val_name = None
	if n:
		col_name,val_name = n[0],n[1]
	else:
		col_name = _getMatrixColNameName(self)
		val_name = _getMatrixValNameName(self)
	
	return {'matrix_col_name':col_name,'matrix_val_name':val_name}

def _getMatrixColNameName(self):
	n = _getSpecName(self,'matrix_col_name')
	if n:
		if not self._columns[n]._type in ('one2many','one2related,','many2many','integer','float','double','real','decimal','numeric'):
			n = None

	return n

def _getMatrixValNameName(self):
	n = _getSpecName(self,'matrix_val_name')
	if n:
		if self._columns[n]._type in ('integer','float','double','real','decimal','numeric'):
			n = None

	return n


#wkf end
def _getSpecName(self,name):
	n = None
	fname = '_' + name
	if hasattr(self,fname):
		n = getattr(self,fname,None)
		if n and type(n) == str:
			if not n in self._columns:
				n=None
	else:
		if DMN[name] in self._columns:
			n = DMN[name]

	return n

def _getNames(self,names=None):
	n = {}
	if not names:
		names = ('parent_id','childs_id','row_name','full_name','rec_name','complete_name','date','date','start_date','end_date','from_date','to_date','from_time','to_time','progress','project_type','sequence','state','inactive','prev_name','next_name','transitions','latitude','longitude','from_latitude','from_longitude','to_latitude','to_longitude','matrix_names','matrix_col_name','matrix_val_name')
	for name in names:
		n[name] = _getSpecName(self,name)
		# #if self._name == 'purchase.order.item.delivery.schedules' and name in ('matrix_names','matrix_col_name','matrix_val_name'):
			# #pass
			# #web_pdb.set_trace()
		# ns = name.split('_')
		# if len(ns) == 1:
			# nf = ns[0].title()
		# else:
			# nf = ''
			# for ns0 in ns:
				# nf += ns0.title()
			# #nf = reduce(lambda x,y: x.title()+y.title(),ns)
		# _f = '_get' + nf + 'Name'
		# #f = getattr(self,_f,None)
		# f = None
		# if _f in __locals__:
			# f = __locals__[_f]
		# #print('get-names:',name,_f,f)
		# if f:
			# n[name] = f(self)

	return n

def _getTriger(self,name):
	if name not in _TRIGGERS_KEYS_:
		raise orm_exception('Invalid triger key: <%s>' % (name,))

	res = []

	if self._trigers and name in self._trigers and self._trigers[name]:
		trg = self._trigers[name]
		if type(trg) == str:
			t = getattr(self,trg,None)
			if t is None:
				raise orm_exception('Invalid triger method: <%s>' % (trg,))
			res.append(t)
		elif type(trg) in (tuple,list):
			for t1 in trg:
				if type(t1) == str:
					t2 = getattr(self,t1,None)
					if t2 is None:
						raise orm_exception('Triger method: <%s> not found' % (t2,))
					res.append(t2)
				else:
					if not callable(t1):
						raise orm_exception('Triger: <%s> not callable' % (t1,))
					res.append(t1)
	
	return res

def _getHook(self,name):
	if self._hooks and name in self._hooks and self._hooks[name]:
		hook = self._hooks[name]
		if callable(hook):
			return hook
		
		return getattr(self,hook,None)

def _compute_composite(self , field, item, context):
	v=''
	if self._columns[field]._type == 'composite':
		cols = self._columns[field].cols
		delimiter = self._columns[field].delimiter
		for col in cols:
			if self._columns[col]._type in ('many2one','referenced','related'):
				if col in item and item[col] and item[col]['name']:
					if len(v) == 0:
						if item[col]['name']:
							v += item[col]['name']
					else:
						if item[col]['name']:
							v += delimiter + item[col]['name']
			else:
				if len(v) == 0:
					if item[col]:
						v += str(item[col])
				else:
					if item[col]:
						v += delimiter + str(item[col])

		if len(v) > 0:
			item[field] = v
	elif self._columns[field]._type == 'i18n' and self._columns[field].column._type == 'composite':
		cols = self._columns[field].column.cols
		delimiter = self._columns[field].column.delimiter
		for col in cols:
			if self._columns[col]._type in ('many2one','referenced','related'):
				if col in item and item[col] and item[col]['name']:
					if len(v) == 0:
						if item[col]['name']:
							v += item[col]['name']
					else:
						if item[col]['name']:
							v += delimiter + item[col]['name']
			else:
				if len(v) == 0:
					if item[col]:
						v += str(item[col])
				else:
					if item[col]:
						v += delimiter + str(item[col])

		if len(v) > 0:
			item[field] = v


def _compute_complete_composite(self ,item,context):
	v=''
	completename = self._getCompleteNameName()
	if completename and self._columns[completename]._type == 'composite':
		cols = self._columns[completename].cols
		delimiter = self._columns[completename].delimiter
		for col in cols:
			if self._columns[col]._type in ('many2one','referenced','related'):
				if col in item and item[col] and item[col]['name']:
					if len(v) == 0:
						if item[col]['name']:
							v += item[col]['name']
					else:
						if item[col]['name']:
							v += delimiter + item[col]['name']
			else:
				if len(v) == 0:
					if item[col]:
						v += str(item[col])
				else:
					if item[col]:
						v += delimiter + str(item[col])

		if len(v) > 0:
			item[completename] = v
	elif completename and self._columns[completename]._type == 'i18n' and self._columns[completename].column._type == 'composite':
		cols = self._columns[completename].column.cols
		delimiter = self._columns[completename].column.delimiter
		for col in cols:
			if self._columns[col].column._type in ('many2one','referenced','related'):
				if col in item and item[col] and item[col]['name']:
					if len(v) == 0:
						if item[col]['name']:
							v += item[col]['name']
					else:
						if item[col]['name']:
							v += delimiter + item[col]['name']
			else:
				if len(v) == 0:
					if item[col]:
						v += str(item[col])
				else:
					if item[col]:
						v += delimiter + str(item[col])

		if len(v) > 0:
			item[completename] = v


def _compute_decomposite(self ,field, item,context):
	v=''
	if self._columns[field]._type == 'decomposite' and self._columns[self._columns[field].column]._type == 'composite':
		col = self._columns[field].column
		part = self._columns[field].part
		delimiter = self._columns[col].delimiter
		parts = item[col].split(delimiter)
		item[field] = parts[part] 

	elif self._columns[field]._type == 'i18n' and self._columns[field].column._type == 'decomposite' and self._columns[self._columns[field].column].column._type == 'composite':
		col = self._columns[field].column
		part = self._columns[field].part
		delimiter = self._columns[col].delimiter
		parts = item[col].split(delimiter)
		item[field] = parts[part] 



def _compute_composite_tree(self ,field ,item, context):
	v=''
	recname = self._getRecNameName()
	rowname = self._getRowNameName()
	fullname = self._getFullNameName()
	parent_id = self._getParentIdName()
	childs_id = self._getChildsIdName() 

	if self._columns[field]._type == 'tree' and parent_id and childs_id:
		delimiter = self._columns[field].delimiter
		if item[parent_id] and item[parent_id]['name']:
			if type(item[parent_id]) == dict and item[parent_id]['id']:
				v += self.read(item[parent_id]['id'],[recname],context)[0][recname]
			elif type(item[parent_id]) == str:
				v += self.read(item[parent_id],[recname],context)[0][recname]
			if item[rowname]:
				v += delimiter + item[rowname]

		else:
			if item[rowname]:
				v += item[rowname]

		if len(v) > 0:
			item[recname] = v
	elif fullname and self._columns[field]._type == 'i18n' and self._columns[field].column._type == 'tree':
		delimiter = self._columns[field].column.delimiter
		if item[parent_id] and item[parent_id]['name']:
			if type(item[parent_id]) == dict and item[parent_id]['id']:
				v += self.read(item[parent_id]['id'],[recname],context)[0][recname]
			elif type(item[parent_id]) == str:
				v += self.read(item[parent_id],[recname],context)[0][recname]
			if item[rowname]:
				v += delimiter + item[rowname]

		else:
			if item[rowname]:
				v += item[rowname]

		if len(v) > 0:
			item[recname] = v


# modelinfo
def _setDefault(self,item):
	_default = self._default
	m1 = self.columnsInfo(attributes=['type','obj'])
	for k in _default.keys():
		if k in item:
			if m1[k]['type'] in ('numeric','decimal'):
				item[k] = Decimal(_default[k])
			elif m1[k]['type'] in ('many2one','related'):
				item.setdefault(k,{})['name'] = _default[k]
			else:
				item[k] = _default[k]	


def _buildEmptyItem(self):
	r = dict.fromkeys(list(self._columns.keys()))
	for o2mfiled in self._o2mfields:
		r[o2mfiled] = []

	for m2mfiled in self._m2mfields:
		r[m2mfiled] = []
	
	for m2orelatedfield in self._m2orelatedfields:
		r[m2orelatedfield] = {'id':None,'name':None}
	
	
	_setDefault(self,r)
	return r

def _buildSchemaColumns(self,pool):
	r = []
	o2mfields = self._o2mfields
	for k in self._columns.keys():
		if k in o2mfields:
			ci = self.columnsInfo([k],['obj'])
			obj = ci[k]['obj']
			m = pool.get(obj)
			r.append({k:_buildSchemaColumns(m,pool)})
		else:
			r.append(k)
	
	return r


def _get__Doc__(self):
	return self.__doc__

def _getAccess(self):
	if not self._access is None:
		return {'create':self._access._create,'read':self._access._read,'write':self._access._write,'unlink':self._access._unlink,'modify':self._access._modify,'insert':self._access._insert,'select':self._access._select,'update':self._access._update,'delete':self._access._delete,'upsert':self._access._upsert,'browse':self._access._browse,'selectbrowse':self._access._selectbrowse}
	else:
		return {'create':True,'read':True,'write':True,'unlink':True,'modify':True,'insert':True,'select':True,'update':True,'delete':True,'upsert':True,'browse':True,'selectbrowse':True}

def _getTrigers(self):
	return str(self._trigers)

def _getColumns(self,columns=None,attributes=None):
	
	return columnsInfo(self,columns,attributes)

def _getI18NColumns(self,columns=None,attributes=None):
	
	return columnsI18NInfo(self,columns,attributes)

	
def _getFamily(self,columns = None):
	return familyInfo(self,columns)

def _getI18N_Family(self,columns = None):
	return familyI18NInfo(self,columns)


def _getDefault(self):
	res = {}
	if self._default:
		for k in self._default.keys():
			v = self._default[k]
			if callable(v):
				res[k] = self._default[k]()
			else:
				res[k] = v
			
	return res


def _info(self,whitelist,args=[],kwargs={}):

	mi = {}

	worklist = []
	lk = False
	lka = False
	
	if len(args) > 0:
		lka = True
		worklist.extend(args)
	
	if len(kwargs) > 0:
		lk = True
		worklist.extend(list(kwargs.keys()))
	
	if len(worklist) == 0:
		worklist.extend(whitelist)
	
	for k in filter(lambda x: x in worklist, whitelist):
		kk = k
		fname = '_get'+kk.title()
		if fname in __locals__:
			if lk and k in kwargs:
				mi[k] = __locals__[fname](self,**(kwargs[k]))
			else:
				mi[k] = __locals__[fname](self)
		else:
			if hasattr(self,'_' + k):
				mi[k] = getattr(self,'_' + k)
			else:
				mi[k]=None
	
	return mi
				


def modelInfo(self,args=[],kwargs={}):
	whitelist = ['__doc__','access','auth','transient','name','names','table','tr_table','schema','class_model','class_model_category','inherit','inherits','description','checks','trgupdcols','trigers','columns_attrs','columns','family','i18n_family','default','register','constraints','i18n_constraints','sql_constraints','i18n_sql_constraints','order_by','group_by','auto','actions','states','attrs','no_copy','groups','pages','indicies','log_access','extra','i18nfields']
	return _info(self,whitelist,args,kwargs)
				

def imodelInfo(self,args=[],kwargs={}):
	whitelist = ['__doc__','name','inherit','inherits','description','checks','columns','family','i18n_family','default','register','constraints','i18n_constraints','sql_constraints','i18n_sql_constraints''i18nfields']
	return _info(self,whitelist,args,kwargs)
				


def columnsInfo(self, columns = None, attributes = None):
	res = {}
	if not columns:
		columns = list(self._columns.keys())
	
	for column in columns:
		if isinstance(self, Model) and column in MAGIC_COLUMNS:
			res[column] = MAGIC_COLUMNS_INFO[column]
		else:
			if self._columns[column]._type == 'i18n':
				res[column] = self._columns[column].column._get_attrs(attributes)
			else:
				res[column] = self._columns[column]._get_attrs(attributes)

	for s in self._selectioncomputefields:
		if s in res and 'selections' in res[s]:
			method = getattr(self,res[s]['selections'],None)
			if method:
				v = method()
				if v is not None:
					res[s]['selections'] = v

	for d in self._domaincomputefields:
		if d in res and 'domain' in res[d]:
			method = getattr(self,res[d]['domain'],None)
			if method:
				v = method()
				if v is not None:
					res[d]['selections'] = v

	return res

# def icolumnsInfo(self, columns = None, attributes = None):
	# res = {}
	# if not columns:
		# columns = list(self._columns.keys())
	
	# for column in columns:
		# res[column] = self._columns[column]._get_attrs(attributes)

	# for s in self._selectionfields:
		# if s in res and type(res[s]['selections']) == str:
			# method = getattr(self,res[s]['selections'],None)
			# if method:
				# v = method()
				# if v is not None:
					# res[s]['selections'] = v


	# return res

# def ifamilyInfo(self,columns):
	# ifamily = {}

	# for key in columns.keys():
		# column = columns[key]
		# if 'family' in column:
			# f = column['family']
			# ifamily.setdefault(f,[]).append(key)
	# return ifamily

def familyInfo(self,columns):
	family = {'Primary': ['id']}
	if columns is None:
		columns = columnsInfo(self,list(self._columns.keys()))
	if isinstance(self,Model) and self._log_access and not self._transient:
		family['Primary'].extend(['create_uid','create_timestamp','write_uid','write_timestamp'])

	for key in filter(lambda x: self._columns[x]._type != 'i18n',columns.keys()):
		column = columns[key]
		if 'family' in column:
			f = column['family']
			family.setdefault(f,[]).append(key)
	return family


def familyI18NInfo(self,columns):
	family = {}
	if columns is None:
		columns = columnsInfo(self,list(self._columns.keys()))

	for key in filter(lambda x: self._columns[x]._type == 'i18n',columns.keys()):
		column = columns[key]
		if 'family' in column:
			f = column['family']
			family.setdefault(f,[]).append(key)
	return family

# Testing
def _m2mfieldid2(pool,obj,rel):
	id2 = None
	columnsinfo = pool.get(obj).columnsInfo()
	for key in columnsinfo.keys():
		columninfo = columnsinfo[key]
		if columninfo['type'] == 'many2many' and columninfo['rel'] == rel:
			id2 = columninfo['id1'] 
	return id2
		

# Testing
def _o2mread(self , oid, field, fields, context,limit,offset):
	res = []
	modelinfo = self.modelInfo()
	columnsinfo = self.columnsInfo()
	#columninfo = columnsinfo[field]
	
	sql,vals = gensql.Select(self = self,pool = pool,uid = uid, info = self.modelInfo(), fields = fields, cond = [(field,'=',oid)], context = context, limit = limit, offset=offset)
	cr.execute(sql,vals)
	if cr.cr.rowcount > 0:
		if context['FETCH'] == 'DICT':
			res.extend(_fetch_results(self ,fields,context))
			#res.extend(cr.fetchall(fields,self._columnsmeta))
		elif context['FETCH'] == 'LIST':
			records = cr.dictfetchall(fields,self._columnsmeta)
			res.extend(_conv_dict_to_list_records(self,fields,records,context))
			#res.extend(cr.dictfetchall(fields,self._columnsmeta))

	for o2mfield in filter(lambda x:self._columnsmeta[x] == 'one2many',self._columnsmeta.keys()):
		for r in res:
			obj = columnsinfo[o2mfield]['obj']
			rel = columnsinfo[o2mfield]['rel']
			if modelinfo['names']['rec_name']:
				rec_name = modelinfo['names']['rec_name']
			else:
				rec_name = 'id'
			for f in fields:
				if type(f) == dict and o2mfield in f:
					r[o2mfield] = _select(pool.get(obj) , f[o2mfield] ,[(rel,'=',r[rec_name])], context, limit, offset)

	return res

# Testing
def _funcread(self , oid, field, record, context):
	columnsinfo = self.columnsInfo(columns = [field], attributes = ['compute','store'])
	store = columnsinfo[field]['store']
	if store == False:
		compute = columnsinfo[field]['compute']
		method = getattr(self,compute,None)
		if method and callable(method):
			return method(self ,record,context)
	return None

# Testing
def _referencedread(self , oid, field, record, context):
	columnsinfo = self.columnsInfo(columns = [field], attributes = ['compute','store'])
	store = columnsinfo[field]['store']
	if store == False:
		compute = columnsinfo[field]['compute']
		method = getattr(self,compute,None)
		if method and callable(method):
			return method(self ,record,context)
	return None

# Testing
def _m2mread(self , oid, field, fields, context):
	res = []
	ids = []

	columnsinfo = self.columnsInfo()
	columninfo = columnsinfo[field]
	rel = getName(columninfo['rel'])
	obj = columninfo['obj']

	id1 = columninfo['id1']
	id2 = columninfo['id2']
	if not id2:
		id2 = _m2mfieldid2(pool,obj,rel)
	cr.execute("SELECT id,%s,%s FROM %s WHERE %s = '%s'" % (id1,id2,rel,id1,oid))
	if cr.cr.rowcount > 0:
		if len(fields) > 0:
			ids.extend(list(map(lambda x: x[2],cr.fetchall([id1,id2], {id1:'uuid',id2:'uuid'})))) 
			if len(ids) > 0:
				res.extend(pool.get(obj).read(cr=cr,pool=pool,uid=uid, ids = ids,fields = fields, context=context))
		else:
			res.extend(cr.fetchall([id1,id2], {id1:'uuid',id2:'uuid'})) 

	return res
		
#testing
def _m2mcreate(self ,rel,id1,id2,oid,rels,context):
	res = []
	values = []
	for r in rels:
		values.append((oid,r))
	print('VALUES:',values)
	sql = "insert into %s (%s,%s) values " % (rel,id1,id2)
	if len(values) == 1:
		sql += str(values[0])
	else:
		sql += reduce(lambda x,y: str(x) + ',' + str(y),values)
		
	sql += ' returning id'
	cr.execute(sql)
	if cr.cr.rowcount > 0:
		if context['FETCH'] == 'LIST':
			res.extend(list(map(lambda x: x[0],cr.fetchall()))) 
		elif context['FETCH'] == 'DICT':
			res.extend(list(map(lambda x: x['id'],cr.dictfetchall()))) 
	
	return res

#testing
def _m2mwrite(self ,rel,id1,id2,oid,rels,context):
	res = []
	iValues = []
	toInsert = rels
	toUnlink = []
	sqls = []
	ids2 = []
	cr.execute("SELECT id,%s,%s FROM %s WHERE %s = '%s'" % (id1,id2,rel,id1,oid))
	if cr.cr.rowcount > 0:
		ids2 = list(map(lambda x: x[2],cr.fetchall(fields = ['id',id1,id2], columnsmeta = {'id':'uuid',id1:'uuid',id2:'uuid'})))
		toInsert = list(filter(lambda x: not x in ids2,rels))
		toUnlink = list(filter(lambda x: not x in rels,ids2))
	
	for i in toInsert:
		iValues.append((oid,i))
	if len(iValues) > 0:
		sql = "insert into %s (%s,%s) values " % (rel,id1,id2)
		if len(iValues) > 1:
			sql += '(' + reduce(lambda x,y: str(x)+','+str(y),iValues) + ')'
		else:
			sql += str(iValues[0])
		
		sql += " returning id"
		sqls.append(sql)

	if len(toUnlink) > 0:
		t = []
		for u in toUnlink:
			t.append("'%s'" % (u,))
		sql = "delete from %s where %s = '%s' and %s in %s" % (rel,id1,oid,id2,tuple(list(map(lambda x: "'%s'" % (x,),toUnlink))))
		sql += " returning id"
		sqls.append(sql)

	if len(sqls) > 0:
		sql = sqls[0]
		if len(sqls) == 2:
			sql += ';' + sqls[1]
		cr.execute(sql)
	if cr.cr.rowcount > 0:
		res.extend(list(map(lambda x: x[0],cr.fetchall()))) 
	
	res.extend(filter(lambda x: not x in toUnlink,ids2))
	res.extend(toInsert)

	return res

#testing
def _m2mmodify(self ,rel,id1,id2,oid,rels,context):
	res = []
	iValues = []
	toInsert = rels
	toUnlink = []
	sqls = []
	ids2 = []
	cr.execute("SELECT id,%s,%s FROM %s WHERE %s = '%s'" % (id1,id2,rel,id1,oid))
	if cr.cr.rowcount > 0:
		ids2 = list(map(lambda x: x[2],cr.fetchall(fields = ['id',id1,id2], columnsmeta = {'id':'uuid',id1:'uuid',id2:'uuid'})))
		toInsert = list(filter(lambda x: not x in ids2,rels))
		toUnlink = list(filter(lambda x: not x in rels,ids2))
	
	for i in toInsert:
		iValues.append((oid,i))
	if len(iValues) > 0:
		sql = "insert into %s (%s,%s) values " % (rel,id1,id2)
		if len(iValues) > 1:
			sql += '(' + reduce(lambda x,y: str(x)+','+str(y),iValues) + ')'
		else:
			sql += str(iValues[0])
		
		sql += " returning id"
		sqls.append(sql)

	if len(toUnlink) > 0:
		if len(toUnlink) == 1:
			sql = "delete from %s where %s = '%s' and %s = '%s'" % (rel,id1,oid,id2,toUnlink[0])
		else:
			sql = "delete from %s where %s = '%s' and %s in (%s)" % (rel,id1,oid,id2,reduce(lambda x,y: x+','+"'"+y+"'",toUnlink))
		sql += " returning id"
		sqls.append(sql)

	if len(sqls) > 0:
		sql = sqls[0]
		if len(sqls) == 2:
			sql += ';' + sqls[1]
		cr.execute(sql)
	if cr.cr.rowcount > 0:
		res.extend(list(map(lambda x: x[0],cr.fetchall()))) 
	
	res.extend(filter(lambda x: not x in toUnlink,ids2))
	res.extend(toInsert)

	return res

#testing
def _m2munlink(self ,rel,id1,id2,oid,rels,context):
	res = []
	if rels and len(rels) > 0:
		if len(rels) == 1:
			sql = "delete from %s where %s = '%s' and %s = '%s'" % (rel,id1,oid,id2,rels[0])
		else:
			sql = "delete from %s where %s = '%s' and %s in (%s)" % (rel,id1,oid,id2,reduce(lambda x,y:x+','+y,rels))
	else:
		sql = "delete from %s where %s = '%s'" % (rel,id1,oid)
	sql += ' returning id'
	cr.execute(sql)
	if cr.cr.rowcount > 0:
		res.extend(list(map(lambda x: x[0],cr.fetchall()))) 
	
	return res

def _do_upload_csv_tree(self , fields, values,context,buf,recname_idx,parent_id_idx,parent_id_value):
	res = []
	if parent_id_value is None:
		_values = list(filter(lambda x: x[parent_id_idx] is None, values))
	else:
		_values = list(filter(lambda x: x[parent_id_idx] == parent_id_value, values))
	 
	if len(_values) > 0:
		for _value in _values:
			_parent_id_value = _value[parent_id_idx]
			if not parent_id_value is None:
				if _parent_id_value in buf:
					_value[parent_id_idx] = buf[_parent_id_value]
				else:
					recname = _getRecNameName(self)
					oid = self.select(cr,pool,uid,[],[(recname,'=',_value[parent_id_idx])],context)[0][0]
					buf[_parent_id_value] = oid
					_value[parent_id_idx] = oid

		res.extend(self.insert(cr,pool,uid,fields,_values,context))

		for _value in _values:
			_parent_id_value = _value[recname_idx]
			res.extend(_do_upload_csv_tree(self , fields, values,context,buf,recname_idx,parent_id_idx,_parent_id_value))
	
	return res

	
def do_upload_csv(self , fields, values,context = {}):
	ir = []

	if len(values) > 0:
		ifields = []
		ufields = []
		ivalues = []
		uvalues = []
		selectionTofields = {}
		selectionFromfields = {}
		columns_info = self.columnsInfo()
		selectionfields = list(filter(lambda x: x in fields,self._selectionfields))
		parent_id = self._getParentIdName()
		for key in selectionfields:
			for k,v in columns_info[key]['selections']:
				selectionTofields.setdefault(key,{})[k] = v
				selectionFromfields.setdefault(key,{})[v] = k 
			
		for value in values:
			for idx,field in enumerate(fields):
				v = value[idx]
				if field == 'id':
					ct = 'uuid'
				else:
					ct = columns_info[field]['type']

				if v is None or len(v) == 0:
					value[idx] = None
					continue

				if ct in ('char','varchar','text','xml'):
					if 'size' in columns_info[field] and columns_info[field]['size']:
						if len(value[idx]) > columns_info[field]['size']:
							value[idx] = value[idx][:columns_info[field]['size']]
					else:
						ml = 2**16
						if len(value[idx]) > ml:
							value[idx] = value[idx][:ml]
				elif ct == 'integer':
					value[idx] = int(v)
				elif ct == 'boolean':
					if v == 'True':
						value[idx] = True
					else:
						value[idx] = None
				elif ct == 'selection':
					value[idx] = selectionFromfields[field][value[idx]]
				elif ct in ('many2one','related'):
					if parent_id and parent_id in fields:
						if field != parent_id:
							obj = pool.get(columns_info[field]['obj'])
							r = obj.search(cr,pool,uid,[(_getRecNameName(obj),'=',value[idx])],context)
							if len(r) > 0:
								value[idx] = r[0]
							else:
								value[idx]=None
					else:
						if len(value[idx]) > 0:
							obj = pool.get(columns_info[field]['obj'])
							r = obj.search(cr,pool,uid,[(_getRecNameName(obj),'=',value[idx])],context)
							if len(r) > 0:
								value[idx] = r[0]
							else:
								value[idx]=None
						else:
							value[idx]=None							
				elif ct in ('float','double'):
					value[idx] = float(value[idx])
				elif ct in ('numeric','decimal'):
					value[idx] = Decimal(value[idx])
				elif ct == 'datetime':
					if columns_info[field]['timezone']:
						value[idx] = datetime.strptime(v+' 00:00:00+0000'[len(v)-10:14],'%Y-%m-%d %H:%M:%S%z')
					else:
						value[idx] = datetime.strptime(v+' 00:00:00'[len(v)-10:9],'%Y-%m-%d %H:%M:%S')
				elif ct == 'date':
					value[idx] = datetime.strptime(value[idx],'%Y-%m-%d').date()
				elif ct == 'time':
					if columns_info[field]['timezone']:
						value[idx] = datetime.strptime(v+'+0000'[len(v)-8:5],'%H:%M:%S%z').time()
					else:
						value[idx] = datetime.strptime(v,'%H:%M:%S').time()
				elif ct == 'one2many':
					value[idx] = None
				elif ct == 'many2many':
					value[idx] = None
				elif ct == 'binary':
					value[idx] = None
				
		fm = {}
		buf = {}
		if parent_id and parent_id in fields:
			for idx,field in enumerate(fields):
				fm[field] = idx
			rec_name = _getRecNameName(self)
			recname_idx = -1
			if rec_name in fm:
				recname_idx = fm[rec_name]
			parent_id_idx = fm[self._getParentIdName()]
			ir.extend(_do_upload_csv_tree(self , fields, values,context,buf,recname_idx,parent_id_idx,None))
		else:
			ichunk = len(ivalues)
			uchunk = len(uvalues)
			if 'id' in fields:
				
				ifields.extend(list(filter(lambda x: x != 'id',fields)))
				ufields = fields
				for value in values:
					v = []
					for field in enumerate(fields):
						if field == 'id' and len(value[idx]) == 0:
							ivalues.append(value[0:idx]+value[idx+1:])
				
				ichunk = len(ivalues)
	
				for value in values:
					v = []
					for idx,field in enumerate(fields):
						if field == 'id' and len(value[idx]) == 36:
							uvalues.append(value)
					
				uchunk = len(uvalues)
			else:
				ifields = fields
				ivalues = values
				ichunk = len(ivalues)
	
			if len(ivalues) > 1000:
				ichunk = len(ivalues) % 1000
				for i in range(int(len(ivalues)/1000)):
					ir.extend(self.insert(cr,pool,uid,ifields,ivalues[1000*i:1000*(i+1)],{'FETCH':'LIST'}))
			if ichunk > 0:
				ir.extend(self.insert(cr,pool,uid,ifields,ivalues[int(len(ivalues)/1000) * 1000:],{'FETCH':'LIST'}))
	
			if len(uvalues) > 1000:
				uchunk = len(uvalues) % 1000
				for i in range(int(len(uvalues)/1000)):
					ir.extend(self.upsert(cr,pool,uid,ufields,uvalues[1000*i:1000*(i+1)],{'FETCH':'LIST'}))
			if uchunk > 0:
				ir.extend(self.upsert(cr,pool,uid,ufields,uvalues[int(len(uvalues)/1000) * 1000:],{'FETCH':'LIST'}))
		
	return ir

def _compute_columns_values(self ,columns,item,context):
	res = {}
	for col in columns.keys():
		columnsinfo = self.columnsInfo(columns=[col],attributes=columns[col])
		col_attrs = columninfo[key]
		for attr in col_attrs.keys():
			if type(col_attrs[attr]) == str:
				method = getattr(self,col_attrs[attr],NOne)
				if method:
					res.setdefault(col,{})[attr] = method(cr,pool,uid,columns,item,context)
	
	return res
			
def do_action(self , action, column, record, context = {}):
	return getattr(self,self._actions[action]['method'],None)(cr,pool,uid,column,record,context)

def do_compute(self , fields, record, context = {}):
	res = {}
	# ci = self.columnsInfo(columns=fields,attributes=['compute','priority'])
	# priority = {}
	# for compute_field in filter(lambda x: x in fields,self._computefields):
		# priority.setdefault(ci[compute_field]['compute'],set()).add(compute_field)
	
	# pkeys = list(priority.keys())
	# pkeys.sort()
	# for pkey in pkeys:
		# for compute_field in priority[pkey]:
			# method = getattr(self,ci[compute_field]['compute'],None)
			# if method and callable(method):
				# r = method(cr,pool,uid,record,context)
				# if r is not None: 
					# res.update(r)

	return res

def _do_checks(self , record, context = {}):
	results = []
	if type(record) == dict:
		res = {} 			
		for check in self._checks:
			method = getattr(self,check,None)
			if method and callable(method):
				res[check] = method(cr,pool,uid,record,context)
				results.append(res)
	elif type(record) in (list,tuple):
		result = []
		for r in record:
			res = {}
			for check in self._checks:
				method = getattr(self,check,None)
				if method and callable(method):
					res[check] = method(cr,pool,uid,r,context)
					result.append(res)
			results.append(result)
	return results

def _conv_dict_to_list_records(self,fields,records,context):
	rows = []
	for record in records:
		row = []
		if 'id' in record:
			row.append(record['id'])
		for field in filter(lambda x: x != 'id',fields):
			if type(field) == str:
				row.append(record[field])
			elif  type(field) == dict:
				for key in field.keys():
					if key in record:
						if type(record[key]) == dict:
							row.append(_conv_dict_to_list_records(self,field[key],record[key]))
						elif type(record[key]) in (list,tuple):
							row.append(record[key])
		
		rows.append(row)
		
	return rows

def _conv_dict_to_raw_records(self,fields,records,context):
	for record in records:
		for field in filter(lambda x: x != 'id',fields):
			if type(field) == str:
				if type(record[field]) == dict and 'id' in record[field]:
					record[field] = record[field]['id']
			elif  type(field) == dict:
				for key in field.keys():
					if key in record:
						if type(record[key]) == dict:
							record[key] = _conv_dict_to_raw_records(self,field[key],record[key])
						elif type(record[key]) in (list,tuple):
							record[key] = _conv_dict_to_raw_records(self,field[key],record[key])
		
	return records

def _fetch_results(self,fields,context):
	
	res = []
	#print('FETCH-FIELDS:',fields)
	if 'FETCH' not in context:
		context['FETCH'] = 'DICT'

	fetch = context['FETCH']

	selectablefields = list(filter(lambda x: x in fields,self._selectablefields))
	nostorecomputefields = list(filter(lambda x: x in fields,self._nostorecomputefields))
	
	records = cr.dictfetchall(selectablefields, self._columnsmeta)
	#print('RECORDs-FETCH:',records)
	for record in records:
		#print('RECORD-FETCH:',record)
		#record = dict(list(record.items())+list(self._compute(cr,pool,uid,nostorecomputefields,record).items()))
		#o2mfields = []
		#if 'cache' in context:
			#record[' '] = {'path':uuid.uuid4().hex,'model':self._name}
		for field in fields:
			if type(field) == dict:
				recname = _getRecNameName(self)
				if recname in record:
					oid = record[recname]
				else:
					if context['FETCH'] == 'LIST':
						oid = self.read(cr,pool,uid,record['id'],[recname],context)[0][0]
					elif context['FETCH'] == 'DICT':
						oid = self.read(cr,pool,uid,record['id'],[recname],context)[0]['id']
				for key in filter(lambda x: x in self._o2mfields,field.keys()):
					#o2mfields.append(f)
					columninfo = self.columnsInfo(columns=[key],attributes=['obj','rel','limit','offset'])
					#print('COLUMNINFO:',columninfo,fields)
					obj = columninfo[key]['obj']
					rel = columninfo[key]['rel']
					record[key] = _o2mread(self = pool.get(obj),cr = cr, pool = pool, uid = uid, oid = oid, field = rel, fields = field[key], context = context,limit = columninfo[key]['limit'],offset = columninfo[key]['offset'])

		for field in fields:
			if type(field) == dict:
				for key in filter(lambda x: x in self._m2mfields,field.keys()):
					record[key] = _m2mread(self = self,cr = cr, pool = pool, uid = uid, oid = record['id'], field = key, fields = field[key], context = context)

		_computes = self._compute(cr,pool,uid,nostorecomputefields,record)
		if not _computes is None:
			#record = dict(list(record.items())+list(_computes.items()))
			record.update(_computes)
	if fetch == 'DICT':		
		res.extend(records)
	elif fetch == 'LIST':
		res.extend(_conv_dict_to_list_records(self,fields,records,context))

	return res

def _gen_record(fields,value):
	record = {}
	for idx,field in enumerate(fields):
		record[field] = value[idx]

	return record

def _gen_records(fields,values):
	records = []
	for value in values:
		records.append(_gen_record(fields,value))

	return records

#tested
def count(self , cond = None, context = {}):
	if not self._access._checkRead():
		orm_exception("Read:access dennied of model % s" % (self._name,))

	res = []
	if 'lang' not in context:
		context['lang'] = os.environ['LANG']
	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]
	if cond is None:
		cond = []

	if 'FETCH' not in context:
		context['FETCH'] = 'DICT'

	fetch = context['FETCH']

	if not fetch in ('LIST','DICT'):
		orm_exception('Invalid fetch mode: %s' % (fetch,))

	sql,vals = gensql.Count(self,pool,uid, self.modelInfo(), cond, context)
	cr.execute(sql,vals)
	if cr.cr.rowcount > 0:
		if fetch == "LIST":
			res.extend(cr.fetchone(['count'], {'count':'integer'})) 
		elif fetch == "DICT":
			res.extend(cr.dictfetchone(['count'], {'count':'integer'})) 
	return res
	
#tested
def search(self , cond = None, context = {}, limit = None, offset = None):
	if not self._access._checkRead():
		orm_exception("Read:access dennied of model % s" % (self._name,))

	res = []

	if 'lang' not in context:
		context['lang'] = os.environ['LANG']

	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]

	if cond is None:
		cond = []

	if 'FETCH' not in context:
		context['FETCH'] = 'DICT'

	fetch = context['FETCH']

	if not fetch in ('LIST','DICT'):
		orm_exception('Invalid fetch mode: %s' % (fetch,))

	sql,vals = gensql.Search(self,pool,uid, self.modelInfo(), cond, context, limit, offset)
	cr.execute(sql,vals)
	if cr.cr.rowcount > 0:
		if fetch == "LIST":
			res.extend(list(map(lambda x: x[0],cr.fetchall()))) 
		elif fetch == "DICT":
			res.extend(list(map(lambda x: x['id'],cr.dictfetchall()))) 
	return res
	
# tested
def _read(self , ids, fields = None, context = {}):

	res = []

	if 'lang' not in context:
		context['lang'] = os.environ['LANG']

	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]

	if 'FETCH' not in context:
		context['FETCH'] = 'DICT'

	fetch = context['FETCH']

	if not fetch.upper() in ('LIST','DICT','RAW'):
		orm_exception('Invalid fetch mode: %s' % (fetch.upper(),))

	length = 1
	if type(ids) in (list,tuple):
		length = len(ids)		
	count = int(length/MAX_CHUNK_READ)
	chunk = int(length % MAX_CHUNK_READ)
	if fields is None:
		fields = self._selectablefields
	for i in range(count):
		j = i * MAX_CHUNK_READ
		chunk_ids = ids[j:j + MAX_CHUNK_READ]
		#sql,vals = gensql.Read(self,pool,uid,self.modelInfo(),chunk_ids,self._selectablefields,context)
		sql,vals = gensql.Read(self,pool,uid,self.modelInfo(),chunk_ids,fields,context)
		cr.execute(sql,vals)
		if cr.cr.rowcount > 0:
			if context['FETCH'] == 'DICT':
				res.extend(_fetch_results(self ,fields,context))
			elif context['FETCH'] == 'LIST':
				records = cr.dictfetchall(fields,self._columnsmeta)
				res.extend(_conv_dict_to_list_records(self,fields,records,context))
			elif context['FETCH'] == 'RAW':
				records = cr.dictfetchall(fields,self._columnsmeta)
				res.extend(_conv_dict_to_raw_records(self,fields,records,context))


	if chunk > 0:
		if length == 1:
			chunk_ids = ids
		else:
			j = count * MAX_CHUNK_READ			
			chunk_ids = ids[j:]
		sql,vals = gensql.Read(self,pool,uid,self.modelInfo(),chunk_ids,fields,context)
		cr.execute(sql,vals)
		if cr.cr.rowcount > 0:
			if context['FETCH'] == 'DICT':
				res.extend(_fetch_results(self ,fields,context))
			elif context['FETCH'] == 'LIST':
				res.extend(_conv_dict_to_list_records(self,fields,records,context))
			elif context['FETCH'] == 'RAW':
				records = cr.dictfetchall(fields,self._columnsmeta)
				res.extend(_conv_dict_to_raw_records(self,fields,records,context))
	
	return res
	
def read(self , ids, fields = None, context = {}):
	if not self._access._checkRead():
		orm_exception("Read:access dennied of model % s" % (self._name,))
	return _read(self , ids, fields, context)

# to be tested
def browse(self , ids, fields = None, context = {}):
	if not self._access._checkBrowse():
		orm_exception("Browse:access dennied of model % s" % (self._name,))

	brl = browse_record_list()
	
	for r in _read(self , ids, fields, context):
		brl.append(browse_record(uid,r))

	if len(brl) == 0:
		return browse_null()

	return brl

#tested
def _tree(self , fields = None ,parent = None, context = {}):

	res = []

	if 'lang' not in context:
		context['lang'] = os.environ['LANG']

	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]

	if 'FETCH' not in context:
		context['FETCH'] = 'DICT'

	fetch = context['FETCH']

	if not fetch.upper() in ('LIST','DICT','RAW'):
		orm_exception('Invalid fetch mode: %s' % (fetch.upper(),))

	if parent is None:
		cond = [(self._getSpecName('parent_id'),'?')]
	else:
		cond = [(self._getSpecName('parent_id'),'=', parent)]

	sql,vals = gensql.Select(self,pool,uid,self.modelInfo(), fields, cond, context,None,None)
	cr.execute(sql,vals)

	if cr.cr.rowcount > 0:
		res.extend(_fetch_results(self ,fields,context))
		for r in res:
			r[self._getSpecName('childs_id')].extend(_tree(self , fields, r[self._getSpecName('rec_name')], context))

	return res

def tree(self , fields = None ,parent = None, context = {}):
	if not self._access._checkSelect():
		orm_exception("Tree:access dennied of model % s" % (self._name,))
	
	return _tree(self , fields, parent, context)


#tested
def _select(self , fields = None ,cond = None, context = {}, limit = None, offset = None):

	res = []

	if 'lang' not in context:
		context['lang'] = os.environ['LANG']

	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]

	if 'FETCH' not in context:
		context['FETCH'] = 'DICT'

	fetch = context['FETCH']

	if not fetch.upper() in ('LIST','DICT','RAW'):
		orm_exception('Invalid fetch mode: %s' % (fetch.upper(),))

	if cond is None:
		cond = []

	sql,vals = gensql.Select(self,pool,uid,self.modelInfo(), fields, cond, context, limit, offset)
	cr.execute(sql,vals)

	if cr.cr.rowcount > 0:
		if context['FETCH'] == 'DICT':
			res.extend(_fetch_results(self ,fields,context))
		elif context['FETCH'] == 'LIST':
			records = cr.dictfetchall(fields,self._columnsmeta)
			res.extend(_conv_dict_to_list_records(self,fields,records,context))
		elif context['FETCH'] == 'RAW':
			records = cr.dictfetchall(fields,self._columnsmeta)
			res.extend(_conv_dict_to_raw_records(self,fields,records,context))
	
	return res

def select(self , fields = None ,cond = None, context = {}, limit = None, offset = None):
	if not self._access._checkSelect():
		orm_exception("Select:access dennied of model % s" % (self._name,))
	
	return _select(self , fields, cond, context, limit, offset)

#testing
def selectbrowse(self , fields = None ,cond = None, context = {}, limit = None, offset = None):
	if not self._access._checkSelectBrowse():
		orm_exception("SelectBrowse:access dennied of model % s" % (self._name,))

	brl = browse_record_list()

	for r in _select(self , fields, cond, context, limit, offset):
		brl.append(browse_record(uid,r))

	if len(brl) == 0:
		return browse_null()

	return brl

#tested
def unlink(self , ids, context = {}):
	if not self._access._checkUnlink():
		orm_exception("Unlink:access dennied of model % s" % (self._name,))

	res = []
	if 'lang' not in context:
		context['lang'] = os.environ['LANG']
	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]
	if type(ids)  == str:
		ids = [ids]

	model_info = self.modelInfo() #attributes=['type','rel','obj','id1','id2'])
	columns_info = model_info['columns']
	m2mfields = list(filter(lambda x: columns_info[x]['type'] == 'many2many',self._columns.keys()))
	for m2mfield in m2mfields:
		rel = columns_info[m2mfield]['rel']
		obj = columns_info[m2mfield]['obj']
		id1 = columns_info[m2mfield]['id1']
		id2 = columns_info[m2mfield]['id2']

		if not id2:
			id2 = _m2mfieldid2(pool,obj,rel)

		rels = []
		#for oid in ids:
			#_m2munlink(self ,rel,id1,id2,oid,rels,context)

	trg1 = self._getTriger('bdr')
	for trg11 in trg1:
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'oid':oid,'context':context}
		trg11(**kwargs)

	trg2 = self._getTriger('bd')
	for trg22 in trg2:
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'oid':oid,'context':context}
		trg22(**kwargs)

	length = len(ids)
	count = int(length/MAX_CHUNK_DELETE)
	chunk = length % MAX_CHUNK_DELETE
	for i in range(count):
		j = i * MAX_CHUNK_DELETE
		chunk_ids = ids[j:j + MAX_CHUNK_DELETE]
		sql,vals = gensql.Unlink(self,pool,uid,self.modelInfo(),chunk_ids,context)
		cr.execute(sql,vals)
		if cr.cr.rowcount > 0:
			res.extend(list(map(lambda x: x[0],cr.fetchall()))) 
	if chunk > 0:
		j = count * MAX_CHUNK_DELETE
		chunk_ids = ids[j:]
		sql,vals = gensql.Unlink(self,pool,uid,self.modelInfo(),chunk_ids,context)
		cr.execute(sql,vals)
		if cr.cr.rowcount > 0:
			res.extend(list(map(lambda x: x[0],cr.fetchall()))) 


	trg3 = self._getTriger('adr')
	for trg33 in trg3:
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'oid':oid,'context':context}
		trg33(**kwargs)

	trg4 = self._getTriger('ad')
	for trg44 in trg4:
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'oid':oid,'context':context}
		trg44(**kwargs)

	return res

#tested
def delete(self , cond, context = {}):
	if not self._access._checkDelete():
		orm_exception("Delete:access dennied of model % s" % (self._name,))

	res = []
	oids = search(self , cond, context)
	if len(oids) > 0:
		res = unlink(self , oids, context)
	
	return res

def _createRecords(self , records, context):
	res = []

	trg1 = self._getTriger('bi')
	for trg11 in trg1:
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':records,'context':context}
		trg11(**kwargs)

	for record in records:
		oid = self._createRecord(cr=cr, pool=pool, uid=uid, record=record, context=context)		
		res.append(oid)

	trg2 = self._getTriger('ai')
	for trg22 in trg2:
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':records,'context':context}
		trg22(**kwargs)

	return res

def _createRecord(self , record, context):
	oid = None

	fields = list(record.keys())
	modelfields = list(self._columns.keys())
	nomodelfields = list(filter(lambda x: not x in modelfields,fields))
	if len(nomodelfields) > 0:
		raise orm_exception("Fields: %s not found in model: %s" % (nomodelfields, self._name))

	for nosavedfield in self._nosavedfields:
		if nosavedfield in record:
			del record[nosavedfield]
	columnsinfo = self.columnsInfo(columns = fields)
	o2mfields = list(filter(lambda x: x in fields, self._o2mfields))
	o2rfields = list(filter(lambda x: x in fields, self._o2rfields)) # o2related
	m2mfields = list(filter(lambda x: x in fields, self._m2mfields))

	for nonefield in list(filter(lambda x: record[x] is None,fields)):
		if nonefield in record:
			del record[nonefield]
	
	emptyfields = list(filter(lambda x: not x in record and not x in MAGIC_COLUMNS,self._requiredfields))		
	if len(emptyfields) > 0:
		raise orm_exception("Fields: %s of model: %s is required and not found in record: %s" % (emptyfields, self.modelInfo(['name'])['name'], record))

	o2mfieldsrecords = {}
	o2rfieldsrecords = {} # o2related
	m2mfieldsrecords = {}

	for o2mfield in o2mfields:
		if o2mfield in record:
			for r in record[o2mfield]:
				obj = pool.get(columnsinfo[o2mfield]['obj'])
				_computes = obj._compute(cr,pool,uid,obj._storecomputefields,r)
				if not _computes is None:
					for key in _computes.keys():
						r[key] = _computes[key]
# o2related
	for o2rfield in o2rfields:
		if o2rfield in record:
			for r in record[o2rfield]:
				obj = pool.get(columnsinfo[o2rfield]['obj'])
				_computes = obj._compute(cr,pool,uid,obj._storecomputefields,r)
				if not _computes is None:
					for key in _computes.keys():
						r[key] = _computes[key]

	_computes = self._compute(cr,pool,uid,self._storecomputefields,record)
	
	#print('RECORD-BERORE-CREATE:',record)
	if not _computes is None:
		for key in _computes.keys():
			record[key] = _computes[key]

	for o2mfield in o2mfields:
		if o2mfield in record:
			o2mfieldsrecords[o2mfield] = record[o2mfield]
			del record[o2mfield]
# o2related
	for o2rfield in o2rfields:
		if o2rfield in record:
			o2rfieldsrecords[o2rfield] = record[o2rfield]
			del record[o2rfield]

	for m2mfield in m2mfields:
		if m2mfield in record:
			m2mfieldsrecords[m2mfield] = record[m2mfield]
			del record[m2mfield]


	trg1 = self._getTriger('bir')
	for trg11 in trg1:
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':record,'context':context}
		trg11(**kwargs)

	sql,vals = gensql.Create(self,pool,uid,self.modelInfo(), record, context)
	cr.execute(sql,vals)
	if cr.cr.rowcount > 0:
		oid = cr.fetchone()[0]
		for key in o2mfieldsrecords.keys():
			columninfo = columnsinfo[key]
			o2mfieldrecords = o2mfieldsrecords[key]
			if o2mfieldrecords is None or len(o2mfieldrecords) == 0:
				continue
			obj = columninfo['obj']
			rel = columninfo['rel']
			for o2mfieldrecord in o2mfieldrecords:
				o2mfieldrecord[rel] = oid
			pool.get(obj).create(cr=cr,pool=pool,uid=uid,records=o2mfieldrecords,context=context)
# o2related
		for key in o2rfieldsrecords.keys():
			columninfo = columnsinfo[key]
			o2rfieldrecords = o2rfieldsrecords[key]
			if o2rfieldrecords is None or len(o2rfieldrecords) == 0:
				continue
			obj = columninfo['obj']
			rel = columninfo['rel']
			relatedy = columninfo['relatedy']
			for o2rfieldrecord in o2rfieldrecords:
				o2rfieldrecord[rel] = oid
				for r1 in relatedy:
					o2rfieldrecord[r1] = record[r1]
			pool.get(obj).create(cr=cr,pool=pool,uid=uid,records=o2rfieldrecords,context=context)

		for key in m2mfieldsrecords.keys():
			columninfo = columnsinfo[key]
			obj = columninfo['obj']
			rels = m2mfieldsrecords[key]
			if rels is None or len(rels) == 0:
				continue
				
			rel = getName(columninfo['rel'])
			
			id1 = getName(columninfo['id1'])
			if columninfo['id2']:
				id2 = getName(columninfo['id2'])
			else:
				id2 = _m2mfieldid2(pool,obj,rel)
	
			_m2mcreate(self ,rel,id1,id2,oid,rels,context)

	trg2 = self._getTriger('air')
	for trg22 in trg2:
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':record,'context':context}
		trg22(**kwargs)

	return oid

#tested
def create(self , records, context = {}):
	if not self._access._checkCreate():
		orm_exception("Create:access dennied of model % s" % (self._name,))

	checks = _do_checks(self , records, context)
	if type(records) == dict:
		for check in checks:
			for key in check.keys():
				if check[key] and type(check[key]) in (list,tuple) and len(check[key]) and check[key][0] in ('A','E','C'):  
					orm_exception("Create:Check errors of model %s\nChecks:%s" % (self._name,checks))
	elif type(records) in (list,tuple):
		for ch in checks:
			for check in ch:
				for key in check.keys():
					if check[key] and type(check[key]) in (list,tuple) and len(check[key]) and check[key][0] in ('A','E','C'):  
						orm_exception("Create:Check errors of model %s\nChecks:%s" % (self._name,checks))

	if 'lang' not in context:
		context['lang'] = os.environ['LANG']
	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]

	if type(records) in (list,tuple):
		return self._createRecords(cr=cr, pool=pool, uid=uid, records=records, context = context)

	elif type(records) == dict:
		return [self._createRecord(cr=cr, pool=pool, uid=uid, record=records, context = context)]

def _writeRecords(self , records, context):
	res = []

	trg1 = self._getTriger('bu')
	for trg11 in trg1:
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':records,'r2':records,'context':context}
		trg11(**kwargs)

	for record in records:
		res.append(self._writeRecord(cr=cr, pool=pool, uid=uid, record=record, context=context))		

	trg2 = self._getTriger('au')
	for trg22 in trg2:
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':records,'r2':records,'context':context}
		trg22(**kwargs)

	return res

def _writeRecord(self , record, context):
	oid = None
	#print('WRITE RECORD:',record)
	fields = list(record.keys())
	modelfields = list(self._columns.keys())
	nomodelfields = list(filter(lambda x: not x in modelfields and not x in MAGIC_COLUMNS,fields))
	if len(nomodelfields) > 0:
		raise orm_exception("Fields: %s not found in model: %s" % (nomodelfields, self._name))

	for nosavedfield in self._nosavedfields:
		if nosavedfield in record:
			del record[nosavedfield]
	columnsinfo = self.columnsInfo(columns = fields)
	o2mfields = list(filter(lambda x: x in fields, self._o2mfields))
	o2rfields = list(filter(lambda x: x in fields, self._o2rfields)) # o2related
	m2mfields = list(filter(lambda x: x in fields, self._m2mfields))
	
	emptyfields = list(filter(lambda x: x in fields and record[x] is None,self._requiredfields))		
	if len(emptyfields) > 0:
		raise orm_exception("Fields: %s of model: %s is required and not found in record: %s" % (emptyfields, self._name, record))

	o2mfieldsrecords = {}
	o2rfieldsrecords = {} # o2related
	m2mfieldsrecords = {}

	for o2mfield in o2mfields:
		if o2mfield in record:
			for r in record[o2mfield]:
				obj = pool.get(columnsinfo[o2mfield]['obj'])
				_computes = obj._compute(cr,pool,uid,obj._storecomputefields,r)
				if not _computes is None:
					for key in _computes.keys():
						r[key] = _computes[key]
# o2related
	for o2rfield in o2rfields:
		if o2rfield in record:
			for r in record[o2rfield]:
				obj = pool.get(columnsinfo[o2rfield]['obj'])
				_computes = obj._compute(cr,pool,uid,obj._storecomputefields,r)
				if not _computes is None:
					for key in _computes.keys():
						r[key] = _computes[key]

	_computes = self._compute(cr,pool,uid,self._storecomputefields,record)

	#print('RECORD-BERORE-WRITE:',record)
	if not _computes is None:
		for key in _computes.keys():
			record[key] = _computes[key]

	for o2mfield in o2mfields:
		if o2mfield in record:
			o2mfieldsrecords[o2mfield] = record[o2mfield]
			del record[o2mfield]
# o2related
	for o2rfield in o2rfields:
		if o2rfield in record:
			o2rfieldsrecords[o2rfield] = record[o2rfield]
			del record[o2rfield]

	for m2mfield in m2mfields:
		if m2mfield in record:
			m2mfieldsrecords[m2mfield] = record[m2mfield]
			del record[m2mfield]

	trg1 = self._getTriger('bur')
	#print('TRG1:',trg1)
	for trg11 in trg1:
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':record,'r2':record,'context':context}
		trg11(**kwargs)

	sql,vals = gensql.Write(self,pool,uid,self.modelInfo(), record, context)
	cr.execute(sql,vals)
	if cr.cr.rowcount > 0:
		oid = cr.fetchone()[0]
		for key in o2mfieldsrecords.keys():
			columninfo = columnsinfo[key]
			o2mfieldrecords = o2mfieldsrecords[key]
			for o2mfieldrecord in o2mfieldrecords:
				o2mfieldrecord[columninfo['rel']] = oid
			pool.get(columninfo['obj']).write(cr=cr,pool=pool,uid=uid,records=o2mfieldrecords,context=context)
# o2related
		for key in o2rfieldsrecords.keys():
			columninfo = columnsinfo[key]
			o2rfieldrecords = o2rfieldsrecords[key]
			if o2rfieldrecords is None or len(o2rfieldrecords) == 0:
				continue
			obj = columninfo['obj']
			rel = columninfo['rel']
			relatedy = columninfo['relatedy']
			for o2rfieldrecord in o2rfieldrecords:
				o2rfieldrecord[rel] = oid
				for r1 in relatedy:
					o2rfieldrecord[r1] = record[r1]
			pool.get(obj).write(cr=cr,pool=pool,uid=uid,records=o2rfieldrecords,context=context)

			for key in m2mfieldsrecords.keys():
				columninfo = columnsinfo[key]
				obj = columninfo['obj']
				rels = m2mfieldsrecords[key]
				rel = getName(columninfo['rel'])
				
				id1 = getName(columninfo['id1'])
				if columninfo['id2']:
					id2 = getName(columninfo['id2'])
				else:
					id2 = _m2mfieldid2(pool,obj,rel)

				_m2mwrite(self ,rel,id1,id2,oid,rels,context)

	trg2 = self._getTriger('aur')
	#print('TRG2:',trg2)
	for trg22 in trg2:
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':record,'r2':record,'context':context}
		trg22(**kwargs)

	return oid

#tested
def write(self , records, context = {}):
	if not self._access._checkWrite():
		orm_exception("Write:access dennied of model % s" % (self._name,))

	checks = _do_checks(self , records, context)
	for ch in checks:
		for check in ch:
			for key in check.keys():
				if check[key] and type(check[key]) in (list,tuple) and len(check[key]) and check[key][0] in ('A','E','C'):  
					orm_exception("Create:Check errors of model %s\nChecks:%s" % (self._name,checks))

	if 'lang' not in context:
		context['lang'] = os.environ['LANG']
	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]

	if type(records) in (list,tuple):
		return self._writeRecords(cr=cr, pool=pool, uid=uid, records=records,context = context)

	elif type(records) == dict:
		return [self._writeRecord(cr=cr, pool=pool, uid=uid, record=records, context = context)]

#testing
def update(self , record, cond = None,context = {}):
	if not self._access._checkUpdate():
		orm_exception("Update:access dennied of model % s" % (self._name,))

	res = []
	fields = list(record.keys())
	if 'lang' not in context:
		context['lang'] = os.environ['LANG']
	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]
	if cond is None:
		cond = []
	
	fields = list(record.keys())
	#recs = _select(self , fields, cond, context)
	recs = search(self , cond, context)
	_fields =[]
	_fields.extend(fields)
	_fields.append('id')
	
	values = []
	_value = []
	for idx,field in enumerate(fields):
		_value.append(record[field])

	for rec in recs:
		value = []
		value.extend(_value)
		#value.append(rec['id'])
		value.append(rec)
		values.append(value)
		
	res = upsert(self , _fields, values,context)
	return res

#testing
def insert(self , fields, values,context = {}):
	if not self._access._checkInsert():
		orm_exception("Insert:access dennied of model % s" % (self._name,))

	checks = _do_checks(self , _gen_records(fields,values), context)
	if type(checks) == dict:
		for check in checks:
			for key in check.keys():
				if check[key] and type(check[key]) in (list,tuple) and len(check[key]) and check[key][0] in ('A','E','C'):  
					orm_exception("Create:Check errors of model %s\nChecks:%s" % (self._name,checks))
	elif type(checks) in (list,tuple):
		for ch in checks:
			for check in ch:
				for key in check.keys():
					if check[key] and type(check[key]) in (list,tuple) and len(check[key]) and check[key][0] in ('A','E','C'):  
						orm_exception("Create:Check errors of model %s\nChecks:%s" % (self._name,checks))


	storecomputefields = list(filter(lambda x: x in fields, self._storecomputefields))
	if len(storecomputefields) > 0:
		for value in values:
			_computes = self._compute(cr,pool,uid,storecomputefields,_gen_record(fields,value))
			for f in enumerate(fields):
				if f[1] in _computes:
					value[f[0]] = _computes[f[1]]
	
	nosavedfields = list(filter(lambda x: x in fields, self._nosavedfields))
	if len(nosavedfields) > 0:	
		for v in values:
			_v = []
			for idx,f in enumerate(fields):
				if f in nosavedfields:
					continue
				_v.append(v[1][idx])
			v[1] = []
			v[1].extend(_v)
			
	_fields = list(filter(lambda x: not x in nosavedfields,fields))

	res = []
	if 'lang' not in context:
		context['lang'] = os.environ['LANG']
	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]

	trg1 = self._getTriger('bir')
	for trg11 in trg1:
		for value in values:
			kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':_gen_record(fields,value),'context':context}
			trg11(**kwargs)


	trg2 = self._getTriger('bi')
	for trg22 in trg2:
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':_gen_records(fields,values),'context':context}
		trg22(**kwargs)

	sql,vals = gensql.Insert(self,pool,uid, self.modelInfo(), _fields, values, context)
	cr.execute(sql,vals)
	if cr.cr.rowcount > 0:
		res.extend(cr.fetchall()) 
		info = self.modelInfo()
		columnsinfo = info['columns']
		fm = {}
		o2mfields = list(filter(lambda x: x in fields,self._o2mfields))
		m2mfields = list(filter(lambda x: x in fields,self._m2mfields))
		computefields = self._computefields
		for idx,field in enumerate(fields):
			if not field in MAGIC_COLUMNS and columnsinfo[field]['type'] in ('one2many','one2related','many2many'):
				fm[field] = idx
		for r in res:
			for o2mfield in o2mfields:
				columninfo = columnsinfo[o2mfield]
				_o2mfields = values[fm[o2mfield]]['fields'] 
				_o2mvalues = values[fm[o2mfield]]['values'] 
				obj = columninfo['obj']
				rel = columninfo['rel']
				
				for _idx,_o2mfield in enumerate(_o2mfields):
					if _o2mfield == rel:
						for _o2mvalue in _o2mvalues:
							_o2mvalue[_idx] = r[0]
						if len(_o2mvalues) > 0:
							pool.get(obj).insert(cr, pool, uid, _o2mfields, _o2mvalues,context)

			for m2mfield in m2mfields:
				columninfo = columnsinfo[m2mfield]
				obj = columninfo['obj']
				rel = getName(columninfo['rel'])
				rels = values[fm[key]]
				id1 = getName(columninfo['id1'])
				if columninfo['id2']:
					id2 = getName(columninfo['id2'])
				else:
					id2 = _m2mfieldid2(pool,obj,rel)
		
				oid = r[0]
				if len(rels) > 0:
					_m2mcreate(self ,rel,id1,id2,oid,rels,context)


	trg3 = self._getTriger('air')
	for trg33 in trg3:
		for value in values:
			kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':_gen_records(fields,values),'context':context}
			trg33(**kwargs)


	trg4 = self._getTriger('ai')
	for trg44 in trg4:
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':_gen_records(fields,values),'context':context}
		trg44(**kwargs)

	return res

#testing
def upsert(self , fields, values,context = {}):
	if not self._access._checkUpsert():
		orm_exception("Upsert:access dennied of model % s" % (self._name,))

	checks = _do_checks(self , _gen_records(fields,values), context)
	if type(checks) == dict:
		for check in checks:
			for key in check.keys():
				if check[key] and type(check[key]) in (list,tuple) and len(check[key]) and check[key][0] in ('A','E','C'):  
					orm_exception("Create:Check errors of model %s\nChecks:%s" % (self._name,checks))
	elif type(checks) in (list,tuple):
		for ch in checks:
			for check in ch:
				for key in check.keys():
					if check[key] and type(check[key]) in (list,tuple) and len(check[key]) and check[key][0] in ('A','E','C'):  
						orm_exception("Create:Check errors of model %s\nChecks:%s" % (self._name,checks))

	storecomputefields = list(filter(lambda x: x in fields, self._storecomputefields))
	if len(storecomputefields) > 0:
		for value in values:
			_computes = self._compute(cr,pool,uid,storecomputefields,_gen_record(fields,value))
			for f in enumerate(fields):
				if f[1] in _computes:
					value[f[0]] = _computes[f[1]]
	
	nosavedfields = list(filter(lambda x: x in fields, self._nosavedfields))
	if len(nosavedfields) > 0:	
		for v in values:
			_v = []
			for idx,f in enumerate(fields):
				if f in nosavedfields:
					continue
				_v.append(v[1][idx])
			v[1] = []
			v[1].extend(_v)
			
		fields = list(filter(lambda x: not x in nosavedfields,fields))

	res = []
	if 'lang' not in context:
		context['lang'] = os.environ['LANG']
	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]


	trg1 = self._getTriger('bir')
	for trg11 in trg1:
		for value in values:
			kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':_gen_record(fields,value),'context':context}
			trg11(**kwargs)


	trg2 = self._getTriger('bi')
	for trg22 in trg2:
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':_gen_records(fields,values),'context':context}
		trg22(**kwargs)

	sql,vals = gensql.Upsert(self,pool,uid, self.modelInfo(), fields, values, context)
	cr.execute(sql,vals)
	if cr.cr.rowcount > 0:
		res.extend(cr.fetchall()) 
		info = self.modelInfo()
		columnsinfo = info['columns']
		fm = {}
		o2mfields = list(filter(lambda x: x in fields,self._o2mfields))
		m2mfields = list(filter(lambda x: x in fields,self._m2mfields))
		computefields = self._computefields
		for idx,field in enumerate(fields):
			if not field in MAGIC_COLUMNS and columnsinfo[field]['type'] in ('one2many','one2related','many2many'):
				fm[field] = idx
		for r in res:
			for o2mfield in o2mfields:
				columninfo = columnsinfo[o2mfield]
				_o2mfields = values[fm[o2mfield]]['fields'] 
				_o2mvalues = values[fm[o2mfield]]['values'] 
				obj = columninfo['obj']
				rel = columninfo['rel']
				
				for _idx,_o2mfield in enumerate(_o2mfields):
					if _o2mfield == rel:
						for _o2mvalue in _o2mvalues:
							_o2mvalue[_o2mfield] = r[0]
						if len(_o2mvalues) > 0:
							pool.get(obj).upsert(cr, pool, uid, _o2mfields, _o2mvalues,context)

			for m2mfield in m2mfields:
				columninfo = columnsinfo[m2mfield]
				obj = columninfo['obj']
				rel = getName(columninfo['rel'])
				rels = values[fm[key]]
				id1 = getName(columninfo['id1'])
				if columninfo['id2']:
					id2 = getName(columninfo['id2'])
				else:
					id2 = _m2mfieldid2(pool,obj,rel)
		
				oid = r[0]
				_m2mmodify(self ,rel,id1,id2,oid,rels,context)

	trg3 = self._getTriger('air')
	for trg33 in trg3:
		for value in values:
			kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':_gen_record(fields,value),'context':context}
			trg33(**kwargs)


	trg4 = self._getTriger('ai')
	for trg44 in trg4:
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':_gen_records(fields,values),'context':context}
		trg44(**kwargs)

	return res


def _modifyRecords(self , records, context):
	res = []

	trg1 = self._getTriger('bu')
	for trg11 in trg1:
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':records,'r2':records,'context':context}
		trg11(**kwargs)

	for record in records:
		oid = self._modifyRecord(cr=cr, pool=pool, uid=uid, record=record, context = context)
		res.append(oid)

	trg2 = self._getTriger('au')
	for trg22 in trg2:
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':records,'r2':records,'context':context}
		trg22(**kwargs)

	return res

def _modifyRecord(self , record, context):
	oid = None
	#print('MODIFY-RECORD:',record)
	fields = list(record.keys())
	modelfields = list(self._columns.keys())
	nomodelfields = list(filter(lambda x: not x in modelfields and not x in MAGIC_COLUMNS, fields))
	if len(nomodelfields) > 0:
		raise orm_exception("Fields: %s not found in model: %s" % (nomodelfields, self.modelInfo(['name'])['name']))
	
	for nosavedfield in self._nosavedfields:
		if nosavedfield in record:
			del record[nosavedfield]
	columnsinfo = self.columnsInfo(columns = fields)
	o2mfields = list(filter(lambda x: x in fields, self._o2mfields))
	o2rfields = list(filter(lambda x: x in fields, self._o2rfields)) # o2related
	m2mfields = list(filter(lambda x: x in fields, self._m2mfields))

	emptyfields = list(filter(lambda x: x in fields and record[x] is None,self._requiredfields))		
	if len(emptyfields) > 0:
		raise orm_exception("Fields: %s of model: %s is required and not found in record: %s" % (emptyfields, self.modelInfo(['name'])['name'], record))

	o2mfieldsrecords = {}
	o2rfieldsrecords = {} # o2related
	m2mfieldsrecords = {}

	for o2mfield in o2mfields:
		if o2mfield in record:
			for r in record[o2mfield]:
				obj = pool.get(columnsinfo[o2mfield]['obj'])
				_computes = obj._compute(cr,pool,uid,obj._storecomputefields,r)
				if not _computes is None:
					for key in _computes.keys():
						r[key] = _computes[key]
# o2related
	for o2rfield in o2rfields:
		if o2rfield in record:
			for r in record[o2rfield]:
				obj = pool.get(columnsinfo[o2rfield]['obj'])
				_computes = obj._compute(cr,pool,uid,obj._storecomputefields,r)
				if not _computes is None:
					for key in _computes.keys():
						r[key] = _computes[key]

	_computes = self._compute(cr,pool,uid,self._storecomputefields,record)

	#print('RECORD-BERORE-MODIFY:',record)
	if not _computes is None:
		for key in _computes.keys():
			record[key] = _computes[key]

	for o2mfield in o2mfields:
		if o2mfield in record:
			o2mfieldsrecords[o2mfield] = record[o2mfield]
			del record[o2mfield]
# o2related
	for o2rfield in o2rfields:
		if o2rfield in record:
			o2rfieldsrecords[o2rfield] = record[o2rfield]
			del record[o2rfield]

	for m2mfield in m2mfields:
		if m2mfield in record:
			m2mfieldsrecords[m2mfield] = record[m2mfield]
			del record[m2mfield]

	trg1 = self._getTriger('bur')
	record2 =None
	upd_cols = set()
	if trg1 and len(trg1) > 0:
		
		if 'id' in record and record['id']:
			ctx = context.copy()
			ctx['FETCH'] = 'RAW'
			record2 = None
			record21 = read(self , record['id'], self._selectablefields, ctx)
			if len(record21) > 0:
				record2 = record21[0]
	
		if record2:
			k1 = set(list(record.keys()))
			k2 = set(list(record2.keys()))
			uk = list(set(k1).intersection(set(k2)))
			ik = list(set(k1)- set(k2))
			dk = list(set(k2)- set(k1))
		else:
			k1 = set()
			k2 = set()
			uk = list()
			ik = list()
			dk = list()
			
		for k in uk:
			if record[k] != record2[k]:
				if self._trg_upd_cols and len(self._trg_upd_cols) == 0 or self._trg_upd_cols and k in self._trg_upd_cols:
					upd_cols.add(k)
		for k in ik:
			if self._trg_upd_cols and len(self._trg_upd_cols) == 0 or self._trg_upd_cols and k in self._trg_upd_cols:
				upd_cols.add(k)

		for k in dk:
			if self._trg_upd_cols and len(self._trg_upd_cols) == 0 or self._trg_upd_cols and k in self._trg_upd_cols:
				upd_cols.add(k)

		if record2 is None or len(upd_cols) > 0:
			for trg11 in trg1:
				kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':record,'r2':record2,'context':context}
				trg11(**kwargs)
		
	#print('RECORD-0:',record)
	sql,vals = gensql.Modify(self,pool,uid,self.modelInfo(), record, context)
	cr.execute(sql,vals)
	if cr.cr.rowcount > 0:
		oid = cr.fetchone()[0]
		for key in o2mfieldsrecords.keys():
			columninfo = columnsinfo[key]
			o2mfieldrecords = o2mfieldsrecords[key]
			for o2mfieldrecord in o2mfieldrecords:
				o2mfieldrecord[columninfo['rel']] = oid
			pool.get(columninfo['obj']).modify(cr=cr,pool=pool,uid=uid,records=o2mfieldrecords,context=context)
# o2related
		for key in o2rfieldsrecords.keys():
			columninfo = columnsinfo[key]
			o2rfieldrecords = o2rfieldsrecords[key]
			if o2rfieldrecords is None or len(o2rfieldrecords) == 0:
				continue
			obj = columninfo['obj']
			rel = columninfo['rel']
			relatedy = columninfo['relatedy']
			for o2rfieldrecord in o2rfieldrecords:
				o2rfieldrecord[rel] = oid
				for r1 in relatedy:
					o2rfieldrecord[r1] = record[r1]
			pool.get(obj).modify(cr=cr,pool=pool,uid=uid,records=o2rfieldrecords,context=context)

		for key in m2mfieldsrecords.keys():
			columninfo = columnsinfo[key]
			obj = columninfo['obj']
			rels = m2mfieldsrecords[key]
			rel = getName(columninfo['rel'])
				
			id1 = getName(columninfo['id1'])
			if columninfo['id2']:
				id2 = getName(columninfo['id2'])
			else:
				id2 = _m2mfieldid2(pool,obj,rel)

			_m2mmodify(self ,rel,id1,id2,oid,rels,context)

	
	if record2 is None or len(upd_cols) > 0:
		trg2 = self._getTriger('aur')
		for trg22 in trg2:
			kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':record,'r2':record2,'context':context}
			trg22(**kwargs)

	return oid

#tested
def modify(self , records, context = {}):
	if not self._access._checkModify():
		orm_exception("Modify:access dennied of model % s" % (self._name,))

	checks = _do_checks(self , records, context)
	if type(records) == dict:
		for check in checks:
			for key in check.keys():
				if check[key] and type(check[key]) in (list,tuple) and len(check[key]) and check[key][0] in ('A','E','C'):  
					orm_exception("Create:Check errors of model %s\nChecks:%s" % (self._name,checks))
	elif type(records) in (list,tuple):
		for ch in checks:
			for check in ch:
				for key in check.keys():
					if check[key] and type(check[key]) in (list,tuple) and len(check[key]) and check[key][0] in ('A','E','C'):  
						orm_exception("Create:Check errors of model %s\nChecks:%s" % (self._name,checks))

	if 'lang' not in context:
		context['lang'] = os.environ['LANG']
	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]

	if type(records) in (list,tuple):
		return self._modifyRecords(cr=cr, pool=pool, uid=uid, records=records, context = context)

	elif type(records) == dict:
		return [self._modifyRecord(cr=cr, pool=pool, uid=uid, record=records, context = context)]

__locals__= locals()
