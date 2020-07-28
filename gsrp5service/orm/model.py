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

import web_pdb

class MetaModel(type):
	__modules__ = {}

	def __new__(cls, name, bases, attrs):
		if '__module__' in attrs and not attrs['__module__'] in ('gsrp5service.orm.model.MetaModel','orm.model.MetaModel','model.MetaModel','gsrp5service.orm.model','orm.model'):
			_m = attrs['__module__'].split('.')
			_module = attrs['__module__']

			if _m[0] == 'gsrp5service':
				_module = reduce(lambda x,y: x + '.' + y,attrs['__module__'].split('.')[3:5])	
			else:	
				_module = reduce(lambda x,y: x + '.' + y,attrs['__module__'].split('.')[:2])	

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
	_views = ['search','form','tree','kanban','mdx','graph','gantt','list','calendar','geo','flow']
	_trg_upd_cols = []
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

		for k in self._columns.keys():
			r[k] = self._columns[k]._type

		return r 

	@property
	def _rowfields(self):
		return list(filter(lambda x: self._columns[x]._type not in ('one2many','many2many'),self._columns.keys())) 

	@property
	def _m2ofields(self):
		return list(filter(lambda x: self._columns[x]._type == 'many2one',self._columns.keys())) 

	@property
	def _m2orelatedfields(self):
		return list(filter(lambda x: self._columns[x]._type in ('many2one','related'),self._columns.keys())) 

	@property
	def _joinfields(self):
		return list(filter(lambda x: self._columns[x]._type in ('many2one','related','referenced'),self._columns.keys())) 

	@property
	def _o2mfields(self):
		return list(filter(lambda x: self._columns[x]._type == 'one2many',self._columns.keys())) 

	@property
	def _o2rfields(self):
		return list(filter(lambda x: self._columns[x]._type == 'one2related',self._columns.keys())) 

	@property
	def _m2mfields(self):
		return list(filter(lambda x: self._columns[x]._type == 'many2many',self._columns.keys())) 

	@property
	def _relatedfields(self):
		return list(filter(lambda x: self._columns[x]._type == 'related',self._columns.keys())) 

	@property
	def _referencedfields(self):
		return list(filter(lambda x: self._columns[x]._type == 'referenced',self._columns.keys())) 

	@property
	def _selectionfields(self):
		return list(filter(lambda x: self._columns[x]._type == 'selection',self._columns.keys())) 

	@property
	def _readonlyfields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'compute') and self._columns[x].compute or self._columns[x]._type == 'referenced',self._columns.keys())) 

	@property
	def _on_change_fields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'on_change') and self._columns[x].on_change and type(self._columns[x].on_change) == str,self._columns.keys())) 

	@property
	def _on_check_fields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'on_check') and self._columns[x].on_change and type(self._columns[x].on_change) == str,self._columns.keys())) 

	@property
	def _computefields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'compute') and self._columns[x].compute and type(self._columns[x].compute) == str,self._columns.keys())) 

	@property
	def _domaincomputefields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'domain') and self._columns[x].domain and type(self._columns[x].domain) == str,self._columns.keys())) 

	@property
	def _selectioncomputefields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'selections') and self._columns[x].selections and type(self._columns[x].selections) == str,self._columns.keys())) 

	@property
	def _storecomputefields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'compute') and self._columns[x].compute and type(self._columns[x].compute) == str and hasattr(self._columns[x],'store') and self._columns[x].store,self._columns.keys())) 

	@property
	def _nostorecomputefields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'compute') and self._columns[x].compute and type(self._columns[x].compute) == str and hasattr(self._columns[x],'store') and not self._columns[x].store,self._columns.keys())) 

	@property
	def _nosavedfields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'store') and not self._columns[x].store or self._columns[x]._type == 'referenced' or hasattr(self._columns[x],'compute') and type(self._columns[x].compute) in (list,tuple),self._columns.keys())) 

	@property
	def _requiredfields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'required') and self._columns[x].required,self._columns.keys())) 

	@property
	def _storefields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'store') and self._columns[x].store,self._columns.keys())) 

	@property
	def _selectablefields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'store') and self._columns[x].store or self._columns[x]._type in ('one2many','many2many','text','xml','binary','referenced'),self._columns.keys())) 

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
	_trg_upd_cols = None
	_trigers = None
	_hooks = None
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
	_pages = {}
	_indicies = {}
	_extra = {}

	def __init__(self,access = None):
		mm.model__init__(self,access)

	def _execute(self, sql,vals=None):
		self._session._cursor.cr.execute(sql,vals)
		return self._session._cursor.cr.rowcount

	@property
	def _cr(self):
		return self._session._cursor

	@property
	def _pool(self):
		return self._session._models

	@property
	def _reports(self):
		return self._session._reports

	@property
	def _dialogs(self):
		return self._session._dialogs

	@property
	def _wizards(self):
		return self._session._wizards

	@property
	def _pool(self):
		return self._session._models

	@property
	def _queries(self):
		return self._session._queries

	@property
	def _uid(self):
		return self._session._uid
		
	def _compute(self,item,context):
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

	def _getCacheID(self,mode,context):
				if 'cache' in context:
					return context['cache']
				else:
					return self._session._mcache(['open',{'mode':mode,'context':context}])[0]
		

	def read(self,ids,fields=None,context={}):
		if hasattr(self,'_session'):
			uid = self._getCacheID('read',context)
			return getattr(self._session._cache[uid],'_read')(self,ids,fields,context)

	def write(self,records,context={}):
		if hasattr(self,'_session'):
			uid = self._getCacheID('write',context)
			return getattr(self._session._cache[uid],'_write')(self,records,context)

	def modify(self,records,context={}):
		if hasattr(self,'_session'):
			uid = self._getCacheID('modify',context)
			return getattr(self._session._cache[uid],'_modify')(self,records,context)

	def create(self,records,context={}):
		if hasattr(self,'_session'):
			uid = self._getCacheID('create',context)
			return getattr(self._session._cache[uid],'_create')(self,records,context)

	def unlink(self,ids,context={}):
		if hasattr(self,'_session'):
			uid = self._getCacheID('unlink',context)
			return getattr(self._session._cache[uid],'_unlink')(self,ids,context)

	def select(self,fields = None ,cond = None, context = {}, limit = None, offset = None):
		if hasattr(self,'_session'):
			uid = self._getCacheID('select',context)
			return getattr(self._session._cache[uid],'_select')(self,fields, cond, context, limit, offset)

	def update(self,record, cond = None,context = {}):
		if hasattr(self,'_session'):
			uid = self._getCacheID('update',context)
			return getattr(self._session._cache[uid],'_update')(self,record,cond,context)

	def upsert(self,fields, values,context = {}):
		if hasattr(self,'_session'):
			uid = self._getCacheID('upsert',context)
			return getattr(self._session._cache[uid],'_upsert')(self,fields, values,context )

	def insert(self,fields, values,context = {}):
		if hasattr(self,'_session'):
			uid = self._getCacheID('insert',context)
			return getattr(self._session._cache[uid],'_insert')(self,fields, values,context )

	def delete(self,cond,context = {}):
		if hasattr(self,'_session'):
			uid = self._getCacheID('delete',context)
			return getattr(self._session._cache[uid],'_delete')(self,cond,context )

	def count(self,cond = None, context = {}):
		if hasattr(self,'_session'):
			uid = self._getCacheID('count',context)
			return getattr(self._session._cache[uid],'_count')(self,cond, context)

	def search(self,cond = None, context = {}, limit = None, offset = None):
		if hasattr(self,'_session'):
			uid = self._getCacheID('search',context)
			return getattr(self._session._cache[uid],'_search')(self,cond, context, limit, offset)

	def tree(self,fields = None ,parent = None, context = {}):
		if hasattr(self,'_session'):
			uid = self._getCacheID('tree',context)
			return getattr(self._session._cache[uid],'_tree')(self,fields,parent, context)

	def browse(self,ids,fields=None,context={}):
		if hasattr(self,'_session'):
			uid = self._getCacheID('browse',context)
			return getattr(self._session._cache[uid],'_browse')(self,ids,fields,context)

	@property
	def _columnsmeta(self):
		r = {}

		for k in self._columns.keys():
			r[k] = self._columns[k]._type

		return r 

	@property
	def _rowfields(self):
		return list(filter(lambda x: self._columns[x]._type not in ('one2many','many2many'),self._columns.keys())) 

	@property
	def _m2ofields(self):
		return list(filter(lambda x: self._columns[x]._type == 'many2one',self._columns.keys())) 

	@property
	def _m2orelatedfields(self):
		return list(filter(lambda x: self._columns[x]._type in ('many2one','related'),self._columns.keys())) 

	@property
	def _joinfields(self):
		return list(filter(lambda x: self._columns[x]._type in ('many2one','related','referenced'),self._columns.keys())) 

	@property
	def _o2mfields(self):
		return list(filter(lambda x: self._columns[x]._type == 'one2many',self._columns.keys())) 

	@property
	def _o2rfields(self):
		return list(filter(lambda x: self._columns[x]._type == 'one2related',self._columns.keys())) 

	@property
	def _m2mfields(self):
		return list(filter(lambda x: self._columns[x]._type == 'many2many',self._columns.keys())) 

	@property
	def _relatedfields(self):
		return list(filter(lambda x: self._columns[x]._type == 'related',self._columns.keys())) 

	@property
	def _referencedfields(self):
		return list(filter(lambda x: self._columns[x]._type == 'referenced',self._columns.keys())) 

	@property
	def _selectionfields(self):
		return list(filter(lambda x: self._columns[x]._type == 'selection',self._columns.keys())) 

	@property
	def _readonlyfields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'readonly') and self._columns[x].readonly or hasattr(self._columns[x],'compute') and self._columns[x].compute or self._columns[x]._type == 'referenced',self._columns.keys())) 

	@property
	def _on_change_fields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'on_change') and self._columns[x].on_change and type(self._columns[x].on_change) == str,self._columns.keys())) 

	@property
	def _on_check_fields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'on_check') and self._columns[x].on_check and type(self._columns[x].on_check) == str,self._columns.keys())) 

	@property
	def _computefields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'compute') and self._columns[x].compute and type(self._columns[x].compute) == str,self._columns.keys())) 

	@property
	def _domaincomputefields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'domain') and self._columns[x].domain and type(self._columns[x].domain) == str,self._columns.keys())) 

	@property
	def _selectioncomputefields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'selections') and self._columns[x].selections and type(self._columns[x].selections) == str,self._columns.keys())) 

	@property
	def _storecomputefields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'compute') and self._columns[x].compute and type(self._columns[x].compute) == str and hasattr(self._columns[x],'store') and self._columns[x].store,self._columns.keys())) 

	@property
	def _nostorecomputefields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'compute') and self._columns[x].compute and type(self._columns[x].compute) == str and hasattr(self._columns[x],'store') and not self._columns[x].store,self._columns.keys())) 

	@property
	def _nosavedfields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'store') and not self._columns[x].store or self._columns[x]._type == 'referenced' or hasattr(self._columns[x],'compute') and type(self._columns[x].compute) in (list,tuple),self._columns.keys())) 

	@property
	def _requiredfields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'required') and self._columns[x].required,self._columns.keys())) 

	@property
	def _storefields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'store') and self._columns[x].store,self._columns.keys())) 

	@property
	def _selectablefields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'store') and self._columns[x].store or self._columns[x]._type in ('one2many','many2many','text','xml','binary','referenced'),self._columns.keys())) 

	def _getMessage(self,cr,pool,uid,area,code,context={}):
		r = pool.get('bc.messages').select(cr,pool,uid,['area','code','descr'],[('area','=',area),('code','=',code)],context,limit=1)
		if len(r) > 0:
			return r[0]
	
	def _getUid(self,cr):
		cr.execute('select uuid_v4()::UUID as id')
		if cr.rowcount > 0:
			return cr.fetchone(['id'],{'id':'UUID'})[0]

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

	def _getRowNameName(self):
		return mm._getRowNameName(self)

	def _getFullNameName(self):
		return mm._getFullNameName(self)

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

	def _getTriger(self,name):
		return mm._getTriger(self,name)

	def _getHook(self,name):
		return mm._getHook(self,name)

	def _buildEmptyItem(self):
		return mm._buildEmptyItem(self)

	def _buildSchemaColumns(self,pool):
		return mm._buildSchemaColumns(self,pool)

	def _compute_composite(self,cr,pool,uid,item,context):
		return mm._compute_composite(self,cr,pool,uid,item,context)

	def _compute_composite_tree(self,cr,pool,uid,item,context):
		return mm._compute_composite_tree(self,cr,pool,uid,item,context)

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
	# def count(self, cr, pool, uid, cond = None, context = {}):
		# self._session[cr]
		# return mm.count(self, cr, pool, uid, cond, context)
		
# #tested
	# def search(self, cr, pool, uid, cond = None, context = {}, limit = None, offset = None):
		# return mm.search(self, cr, pool, uid, cond, context, limit, offset)
		
# # tested	
	# def read(self, cr, pool, uid, ids, fields = None, context = {}):
		# return mm.read(self, cr, pool, uid, ids, fields, context)

# # to be tested
	# def browse(self, cr, pool, uid, ids, fields = None, context = {}):
		# return mm.browse(self, cr, pool, uid, ids, fields, context)

# #testing
	# def tree(self, cr, pool, uid, fields = None ,parent = None, context = {}):
		# return mm.tree(self, cr, pool, uid, fields, parent, context)

# #tested
	# def select(self, cr, pool, uid, fields = None ,cond = None, context = {}, limit = None, offset = None):
		# return mm.select(self, cr, pool, uid, fields, cond, context, limit, offset)

# #to be testing
	# def selectbrowse(self, cr, pool, uid, fields = None ,cond = None, context = {}, limit = None, offset = None):
		# return mm.selectbrowse(self, cr, pool, uid, fields, cond, context, limit, offset)

# #tested
	# def unlink(self, cr, pool, uid, ids, context = {}):
		# return mm.unlink(self, cr, pool, uid, ids, context)

# #tested
	# def delete(self, cr, pool, uid, cond, context = {}):
		# return mm.delete(self, cr, pool, uid, cond, context)

	# def _createRecords(self, cr, pool, uid, records, context):
		# return mm._createRecords(self, cr, pool, uid, records, context)

	# def _createRecord(self, cr, pool, uid, record, context):
		# return mm._createRecord(self, cr, pool, uid, record, context)

# #tested
	# def create(self, cr, pool, uid, records, context = {}):
		# return mm.create(self, cr, pool, uid, records, context)

	# def _writeRecords(self, cr, pool, uid, records, context):
		# return mm._writeRecords(self, cr, pool, uid, records, context)

	# def _writeRecord(self, cr, pool, uid, record, context):
		# return mm._writeRecord(self, cr, pool, uid, record, context)

# #tested
	# def write(self, cr, pool, uid, records, context = {}):
		# return mm.write(self, cr, pool, uid, records, context)

# #testing
	# def update(self, cr, pool, uid, record, cond = None,context = {}):
		# return mm.update(self, cr, pool, uid, record, cond,context)

# #testing
	# def insert(self, cr, pool, uid, fields, values,context = {}):
		# return mm.insert(self, cr, pool, uid, fields, values,context)

# #testing
	# def upsert(self, cr, pool, uid, fields, values,context = {}):
		# return mm.upsert(self, cr, pool, uid, fields, values,context)

	# def _modifyRecords(self, cr, pool, uid, records, context):
		# return mm._modifyRecords(self, cr, pool, uid, records, context)

	# def _modifyRecord(self, cr, pool, uid, record, context):
		# return mm._modifyRecord(self, cr, pool, uid, record, context)

# #tested
	# def modify(self, cr, pool, uid, records, context = {}):
		# return mm.modify(self, cr, pool, uid, records, context)

	# def m2munlink(self,cr,pool,uid,rel,id1,id2,oid,rels,context={}):		
		# return mm._m2munlink(self,cr,pool,uid,rel,id1,id2,oid,rels,context)

	# def do_compute(self, cr, pool, uid, fields, record, context = {}):
		# return [self._compute(cr, pool, uid, fields, record, context)]

	# def _compute(self, cr, pool, uid, fields, record, context = {}):
		# return mm.do_compute(self, cr, pool, uid, fields, record, context)

	# def do_checks(self, cr, pool, uid, fields, record, context = {}):
		# return [self._do_checks(cr, pool, uid, fields, record, context)]

	def _mcache(self,cr,pool,uid,key,value,idx=-1,context={}):
		return mm._mcache(self,cr,pool,uid,key,value,idx,context)
	
	def compute_columns_values(self,cr,pool,uid,columns,item,context):
		return mm._compute_columns_values(self,cr,pool,uid,columns,item,context)

	def _m2mread(self, cr, pool, uid, oid, field, fields, context):
		return mm._m2mread(self, cr, pool, uid, oid, field, fields, context)

	def _m2mcreate(self,cr,pool,uid,rel,id1,id2,oid,rels,context):
		return mm._m2mcreate(self,cr,pool,uid,rel,id1,id2,oid,rels,context)

	def _m2mwrite(self,cr,pool,uid,rel,id1,id2,oid,rels,context):
		return mm._m2mwrite(self,cr,pool,uid,rel,id1,id2,oid,rels,context)

	def _m2mmodify(self,cr,pool,uid,rel,id1,id2,oid,rels,context):
		mm._m2mmodify(self,cr,pool,uid,rel,id1,id2,oid,rels,context)

	def _m2munlink(self,cr,pool,uid,rel,id1,id2,oid,rels,context):
		return mm._m2munlink(self,cr,pool,uid,rel,id1,id2,oid,rels,context)

class Model(BaseModel):
	_transient = None

class TransientModel(BaseModel):
	_transient = True

class ModelInherit(BaseModelInherit):
	_transient = True
