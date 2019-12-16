# --*-- coding: utf-8 --*--

import os
import sys
import time
import logging
from functools import reduce
from tools.translations import trlocal as _
from . import mm
from .mm import orm_exception
from .mm import Access

_logger = logging.getLogger(__name__)

class MetaModel(type):
	__modules__ = {}

	def __new__(cls, name, bases, attrs):
		if '__module__' in attrs and not attrs['__module__'] in ('gsrp5service.orm.model','orm.model','model'):
			_m = attrs['__module__'].split('.')

			if _m[0] == 'gsrp5service':
				_module = reduce(lambda x,y: x + '.' + y,attrs['__module__'].split('.')[1:3])	
			else:	
				_module = reduce(lambda x,y: x + '.' + y,attrs['__module__'].split('.')[:2])	
			#MetaModel.__modules__.setdefault(_module,{})[attrs['_name']] = {'cls':cls,'name':name,'bases':bases,'attrs':attrs}
			MetaModel.__modules__.setdefault(_module,{})[attrs['_name']] = {'name':name,'bases':bases,'attrs':attrs}

		return super(MetaModel, cls).__new__(cls, name, bases, attrs)

	def __init__(self, name, bases, attrs):
		if not hasattr(self, '_register'):
			setattr(self,'_register',True)
		else:
			self._register = True
			super(MetaModel, self).__init__(name, bases, attrs)

class BaseModelInherit(object, metaclass = MetaModel):
	_name = None
	_description = None
	_register = False
	_inherit = None
	_inherits = None
	_views = ['search','form','tree','kanban','mdx','graph','gantt','list','calendar','geo']
	_trigers = {}
	_columns = {}
	_default = {}
	_constraints = []
	_sql_constraints = []
	_actions = {}
	_states ={}
	_extra = {}

	@property
	def _columnsmeta(self):
		r = {}
		c = self.columnsInfo(attributes=['type'])
		for k in c.keys():
			r[k] = c[k]['type']
		return r 

	@property
	def _m2ofields(self):
		c = self.columnsInfo(attributes=['type'])
		return list(filter(lambda x: c[x]['type'] == 'many2one',c.keys())) 

	@property
	def _m2orelatedfields(self):
		c = self.columnsInfo(attributes=['type'])
		return list(filter(lambda x: c[x]['type'] in ('many2one','related'),c.keys())) 

	@property
	def _joinfields(self):
		c = self.columnsInfo(attributes=['type'])
		return list(filter(lambda x: c[x]['type'] in ('many2one','related','referenced'),c.keys())) 

	@property
	def _o2mfields(self):
		c = self.columnsInfo(attributes=['type'])
		return list(filter(lambda x: c[x]['type'] == 'one2many',c.keys())) 

	@property
	def _o2rfields(self):
		c = self.columnsInfo(attributes=['type'])
		return list(filter(lambda x: c[x]['type'] == 'one2related',c.keys())) 


	@property
	def _m2mfields(self):
		c = self.columnsInfo(attributes=['type'])
		return list(filter(lambda x: c[x]['type'] == 'many2many',c.keys())) 

	@property
	def _relatedfields(self):
		c = self.columnsInfo(attributes=['type'])
		return list(filter(lambda x: c[x]['type'] == 'related',c.keys())) 

	@property
	def _referencedfields(self):
		c = self.columnsInfo(attributes=['type'])
		return list(filter(lambda x: c[x]['type'] == 'referenced',c.keys())) 

	@property
	def _selectionfields(self):
		c = self.columnsInfo(attributes=['type'])
		return list(filter(lambda x: c[x]['type'] == 'selection',c.keys())) 

	@property
	def _readonlyfields(self):
		c = self.columnsInfo(attributes=['compute','type'])
		return list(filter(lambda x: 'compute' in c[x] and c[x]['compute'] or c[x]['type'] == 'referenced',c.keys())) 

	@property
	def _on_change_fields(self):
		c = self.columnsInfo(attributes=['on_change'])
		return list(filter(lambda x: 'on_change' in c[x] and c[x]['on_change'] and type(c[x]['on_change']) == str,c.keys())) 

	@property
	def _on_check_fields(self):
		c = self.columnsInfo(attributes=['on_check'])
		return list(filter(lambda x: 'on_check' in c[x] and c[x]['on_check'] and type(c[x]['on_check']) == str,c.keys())) 

	@property
	def _computefields(self):
		c = self.columnsInfo(attributes=['compute'])
		return list(filter(lambda x: 'compute' in c[x] and c[x]['compute'] and type(c[x]['compute']) == str,c.keys())) 

	@property
	def _storecomputefields(self):
		c = self.columnsInfo(attributes=['compute','store'])
		return list(filter(lambda x: 'compute' in c[x] and c[x]['compute'] and type(c[x]['compute']) == str and 'store' in c[x] and c[x]['store'],c.keys())) 

	@property
	def _nostorecomputefields(self):
		c = self.columnsInfo(attributes=['compute','store'])
		return list(filter(lambda x: 'compute' in c[x] and c[x]['compute'] and type(c[x]['compute']) == str and 'store' in c[x] and not c[x]['store'],c.keys())) 

	@property
	def _nosavedfields(self):
		c = self.columnsInfo(attributes=['type','compute','store'])
		return list(filter(lambda x: 'compute' in c[x] and c[x]['compute'] and type(c[x]['compute']) == str and 'store' in c[x] and not c[x]['store'] or 'compute' in c[x] and c[x]['compute'] and type(c[x]['compute']) in (list,tuple) or c[x]['type'] == 'referenced',c.keys())) 


	@property
	def _requiredfields(self):
		c = self.columnsInfo(attributes=['required'])
		return list(filter(lambda x: 'required' in c[x] and c[x]['required'] and 'compute' in c[x] and c[x]['compute'] and type(c[x]['compute']) == str,c.keys())) 

	@property
	def _storefields(self):
		c = self.columnsInfo(attributes=['store'])
		return list(filter(lambda x: 'store' in c[x] and c[x]['store'],c.keys())) 

	@property
	def _selectablefields(self):
		c = self.columnsInfo(attributes=['store','type'])
		return list(filter(lambda x: 'store' in c[x] and c[x]['store'] or c[x]['type'] in ('one2many','many2many','text','xml','binary','referenced'),c.keys())) 

	def modelInfo(self, columns = None, attributes = None):
		return mm.imodelInfo(self, columns = None, attributes = None)

	def columnsInfo(self, columns = None, attributes = None):
		return mm.icolumnsInfo(self, columns, attributes)

	def familyInfo(self,columns):
		return mm.ifamilyInfo(self,columns)


class BaseModel(object, metaclass = MetaModel):
	_name = None
	_table = None
	_class_model = 'A'
	_class_category = None
	_schema = None
	_inherit = None
	_inherits = None
	_description = None
	_checks = None
	_trigers = None
	_columns_attrs = {}
	_columns = {}
	_default = {}
	_register = False
	_constraints = []
	_sql_constraints = []
	_order_by = "id asc"
	_group_by = []
	_access = None
	_auth = None
	_auto = True
	_actions = None
	_states = None
	_attrs = {}
	_col_attrs = {}
	_no_copy = []
	_groups = {}
	_indicies = {}
	_extra = {}

	def __init__(self,access = None):
		mm.model__init__(self,access)

	@property
	def _columnsmeta(self):
		r = {}
		c = self.columnsInfo(attributes=['type'])
		for k in c.keys():
			r[k] = c[k]['type']
		return r 

	@property
	def _m2ofields(self):
		c = self.columnsInfo(attributes=['type'])
		return list(filter(lambda x: c[x]['type'] == 'many2one',c.keys())) 

	@property
	def _m2orelatedfields(self):
		c = self.columnsInfo(attributes=['type'])
		return list(filter(lambda x: c[x]['type'] in ('many2one','related'),c.keys())) 

	@property
	def _joinfields(self):
		c = self.columnsInfo(attributes=['type'])
		return list(filter(lambda x: c[x]['type'] in ('many2one','related','referenced'),c.keys())) 

	@property
	def _o2mfields(self):
		c = self.columnsInfo(attributes=['type'])
		return list(filter(lambda x: c[x]['type'] == 'one2many',c.keys())) 

	@property
	def _o2rfields(self):
		c = self.columnsInfo(attributes=['type'])
		return list(filter(lambda x: c[x]['type'] == 'one2related',c.keys())) 

	@property
	def _m2mfields(self):
		c = self.columnsInfo(attributes=['type'])
		return list(filter(lambda x: c[x]['type'] == 'many2many',c.keys())) 

	@property
	def _relatedfields(self):
		c = self.columnsInfo(attributes=['type'])
		return list(filter(lambda x: c[x]['type'] == 'related',c.keys())) 

	@property
	def _referencedfields(self):
		c = self.columnsInfo(attributes=['type'])
		return list(filter(lambda x: c[x]['type'] == 'referenced',c.keys())) 

	@property
	def _selectionfields(self):
		c = self.columnsInfo(attributes=['type'])
		return list(filter(lambda x: c[x]['type'] == 'selection',c.keys())) 

	@property
	def _readonlyfields(self):
		c = self.columnsInfo(attributes=['compute','type'])
		return list(filter(lambda x: 'compute' in c[x] and c[x]['compute'] or c[x]['type'] == 'referenced',c.keys())) 

	@property
	def _on_change_fields(self):
		c = self.columnsInfo(attributes=['on_change'])
		return list(filter(lambda x: 'on_change' in c[x] and c[x]['on_change'] and type(c[x]['on_change']) == str,c.keys())) 

	@property
	def _on_check_fields(self):
		c = self.columnsInfo(attributes=['on_check'])
		return list(filter(lambda x: 'on_check' in c[x] and c[x]['on_check'] and type(c[x]['on_check']) == str,c.keys())) 

	@property
	def _computefields(self):
		c = self.columnsInfo(attributes=['compute'])
		return list(filter(lambda x: 'compute' in c[x] and c[x]['compute'] and type(c[x]['compute']) == str,c.keys())) 

	@property
	def _storecomputefields(self):
		c = self.columnsInfo(attributes=['compute','store'])
		return list(filter(lambda x: 'compute' in c[x] and c[x]['compute'] and type(c[x]['compute']) == str and 'store' in c[x] and c[x]['store'],c.keys())) 

	@property
	def _nostorecomputefields(self):
		c = self.columnsInfo(attributes=['compute','store'])
		return list(filter(lambda x: 'compute' in c[x] and c[x]['compute'] and type(c[x]['compute']) == str and 'store' in c[x] and not c[x]['store'],c.keys())) 

	@property
	def _nosavedfields(self):
		c = self.columnsInfo(attributes=['type','compute','store'])
		return list(filter(lambda x: 'compute' in c[x] and c[x]['compute'] and type(c[x]['compute']) == str and 'store' in c[x] and not c[x]['store'] or 'compute' in c[x] and c[x]['compute'] and type(c[x]['compute']) in (list,tuple) or c[x]['type'] == 'referenced',c.keys())) 


	@property
	def _requiredfields(self):
		c = self.columnsInfo(attributes=['required'])
		return list(filter(lambda x: 'required' in c[x] and c[x]['required'] and 'compute' in c[x] and c[x]['compute'] and type(c[x]['compute']) == str,c.keys())) 

	@property
	def _storefields(self):
		c = self.columnsInfo(attributes=['store'])
		return list(filter(lambda x: 'store' in c[x] and c[x]['store'],c.keys())) 

	@property
	def _selectablefields(self):
		c = self.columnsInfo(attributes=['store','type'])
		return list(filter(lambda x: 'store' in c[x] and c[x]['store'] or c[x]['type'] in ('one2many','many2many','text','xml','binary','referenced'),c.keys())) 

	def _is(self,n,t):
		return self.columnsInfo(columns=[n],attributes=['type'])[n]['type'] == t

	def _ism2ofield(self,n):
		return self._is(n,'many2one')

	def _iso2mfield(self,n):
		return self._is(n,'one2many')

	def _iso2related(self,n):
		return self._is(n,'one2related')


	def _ism2mfield(self,n):
		return self._is(n,'many2many')

	def _isrelatedfield(self,n):
		return self._is(n,'related')

	def _isreferencedfield(self,n):
		return self._is(n,'referenced')

	def _getParentIdName(self):
		return mm. _getParentIdName(self)

	def checkAccess(self,mode = None):
		return mm.checkAccess(self,mode = None)
	
	def _getChildsIdName(self):
		return mm._getChildsIdName(self)

	def _getRecNameName(self):
		return mm._getRecNameName(self)

	def _getSequenceName(self):
		return mm._getSequenceName(self)

	def _getDateName(self):
		return mm._getDateName(self)

	def _getStartDateName(self):
		return mm._getStartDateName(self)

	def _getEndDateName(self):
		return mm._getEndDateName(self)

	def _getFromDateName(self):
		return mm._getFromDateName(self)

	def _getToDateName(self):
		return mm._getToDateName(self)

	def _getFromTimeName(self):
		return mm._getFromTimeName(self)

	def _getToTimeName(self):
		return mm._getToTimeName(self)

	def _getProgressName(self):
		return mm._getProgressName(self)

	def _getProjectTypeName(self):
		return mm._getProjectTypeName(self)

	def _getStateName(self):
		return mm._getStateName(self)

	def _getInactiveName(self):
		return mm._getInactiveName(self)

	def _getLatitudeName(self):
		return mm._getLatitudeName(self)

	def _getLongitudeName(self):
		return mm._getLongitudeName(self)

	def _getFromLatitudeName(self):
		return mm._getFromLatitudeName(self)

	def _getFromLongitudeName(self):
		return mm._getFromLongitudeName(self)

	def _getToLatitudeName(self):
		return mm._getToLatitudeName(self)

	def _getToLongitudeName(self):
		return mm._getToLongitudeName(self)

	def _getName(self,name):
		return mm._getName(self,name)

	def _getNames(self,names = None):
		return mm._getNames(self,names)

	# def _getAccess(self):
		# return mm._getAccess(self)

	# def _getAuth(self):
		# return mm._getAuth(self)

	# def _buildXMLForDynamicModel(self):
		# return mm._buildXMLForDynamicModel(self)

	def modelInfo(self, header = None, names = None, columns = None, attributes = None):
		return mm.modelInfo(self, header = None, names = None, columns = None, attributes = None)

	def columnsInfo(self, columns = None, attributes = None):
		return mm.columnsInfo(self, columns, attributes)

	def familyInfo(self,columns):
		return mm.familyInfo(self,columns)

	def do_upload_csv(self, cr, pool, uid, fields, values,context = {}):
		return mm.do_upload_csv(self, cr, pool, uid, fields, values,context)

	def do_action(self, cr, pool, uid, action, column, record, context = {}):
		return mm.do_action(self, cr, pool, uid, action, column, record, context)
#tested
	def count(self, cr, pool, uid, cond = None, context = {}):
		return mm.count(self, cr, pool, uid, cond, context)
		
#tested
	def search(self, cr, pool, uid, cond = None, context = {}, limit = None, offset = None):
		return mm.search(self, cr, pool, uid, cond, context, limit, offset)
		
# tested	
	def read(self, cr, pool, uid, ids, fields = None, context = {}):
		return mm.read(self, cr, pool, uid, ids, fields, context)

# to be tested
	def browse(self, cr, pool, uid, ids, fields = None, context = {}):
		return mm.browse(self, cr, pool, uid, ids, fields, context)

#testing
	def tree(self, cr, pool, uid, fields = None ,parent = None, context = {}):
		return mm.tree(self, cr, pool, uid, fields, parent, context)

#tested
	def select(self, cr, pool, uid, fields = None ,cond = None, context = {}, limit = None, offset = None):
		return mm.select(self, cr, pool, uid, fields, cond, context, limit, offset)

#to be testing
	def selectbrowse(self, cr, pool, uid, fields = None ,cond = None, context = {}, limit = None, offset = None):
		return mm.selectbrowse(self, cr, pool, uid, fields, cond, context, limit, offset)

#tested
	def unlink(self, cr, pool, uid, ids, context = {}):
		return mm.unlink(self, cr, pool, uid, ids, context)

#tested
	def delete(self, cr, pool, uid, cond, context = {}):
		return mm.delete(self, cr, pool, uid, cond, context)

	def _createRecords(self, cr, pool, uid, records, context):
		return mm._createRecords(self, cr, pool, uid, records, context)

	def _createRecord(self, cr, pool, uid, record, context):
		return mm._createRecord(self, cr, pool, uid, record, context)

#tested
	def create(self, cr, pool, uid, records, context = {}):
		return mm.create(self, cr, pool, uid, records, context)

	def _writeRecords(self, cr, pool, uid, records, context):
		return mm._writeRecords(self, cr, pool, uid, records, context)

	def _writeRecord(self, cr, pool, uid, record, context):
		return mm._writeRecord(self, cr, pool, uid, record, context)

#tested
	def write(self, cr, pool, uid, records, context = {}):
		return mm.write(self, cr, pool, uid, records, context)

#testing
	def update(self, cr, pool, uid, record, cond = None,context = {}):
		return mm.update(self, cr, pool, uid, record, cond,context)

#testing
	def insert(self, cr, pool, uid, fields, values,context = {}):
		return mm.insert(self, cr, pool, uid, fields, values,context)

#testing
	def upsert(self, cr, pool, uid, fields, values,context = {}):
		return mm.upsert(self, cr, pool, uid, fields, values,context)

	def _modifyRecords(self, cr, pool, uid, records, context):
		return mm._modifyRecords(self, cr, pool, uid, records, context)

	def _modifyRecord(self, cr, pool, uid, record, context):
		return mm._modifyRecord(self, cr, pool, uid, record, context)

#tested
	def modify(self, cr, pool, uid, records, context = {}):
		return mm.modify(self, cr, pool, uid, records, context)

	def m2munlink(self,cr,pool,uid,rel,id1,id2,oid,rels,context={}):		
		return mm._m2munlink(self,cr,pool,uid,rel,id1,id2,oid,rels,context)

	def do_compute(self, cr, pool, uid, fields, record, context = {}):
		return [self._compute(cr, pool, uid, fields, record, context)]

	def _compute(self, cr, pool, uid, fields, record, context = {}):
		return mm.do_compute(self, cr, pool, uid, fields, record, context)

	def do_checks(self, cr, pool, uid, fields, record, context = {}):
		return [self._do_checks(cr, pool, uid, fields, record, context)]

	def _mcache(self,cr,pool,uid,key,value,idx=-1,context={}):
		return mm._mcache(self,cr,pool,uid,key,value,idx,context)
	
	def compute_columns_values(self,cr,pool,uid,columns,item,context):
		mm._compute_columns_values(self,cr,pool,uid,columns,item,context)

class Model(BaseModel):
	_transient = None

class TransientModel(BaseModel):
	_transient = True

class ModelInherit(BaseModelInherit):
	_transient = True
