# --*-- coding: utf-8 --*--

import os
import sys
import time
import logging
from functools import reduce
from .metaobjects import MetaObjects
from tools.translations import trlocal as _
from . import mm
from .mm import orm_exception
from .mm import Access

_logger = logging.getLogger(__name__)

import web_pdb

class BaseModelInherit(object, metaclass = MetaObjects):
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
		return list(filter(lambda x: self._columns[x]._type in ('many2one','related','referenced'),self._columns.keys())) 

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
		return list(filter(lambda x: hasattr(self._columns[x],'compute') and self._columns[x].compute,self._columns.keys())) 

	@property
	def _on_change_fields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'on_change') and self._columns[x].on_change and type(self._columns[x].on_change) == str,self._columns.keys())) 

	@property
	def _on_check_fields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'on_check') and self._columns[x].on_change and type(self._columns[x].on_change) == str,self._columns.keys())) 

	@property
	def _computefields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'compute') and self._columns[x].compute and type(self._columns[x].compute) == str or self._columns[x]._type == 'i18n' and hasattr(self._columns[x].column,'compute') and self._columns[x].column.compute and type(self._columns[x].column.compute) == str,self._columns.keys())) 

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
		return list(filter(lambda x: hasattr(self._columns[x],'store') and not self._columns[x].store or hasattr(self._columns[x],'compute') and type(self._columns[x].compute) in (list,tuple),self._columns.keys())) 

	@property
	def _requiredfields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'required') and self._columns[x].required,self._columns.keys())) 

	@property
	def _storefields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'store') and self._columns[x].store,self._columns.keys())) 

	@property
	def _selectablefields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'store') and self._columns[x].store or self._columns[x]._type in ('one2many','many2many','text','xml','binary'),self._columns.keys())) 

	def imodelInfo(self, args = [], kwargs = {}):
		return mm.imodelInfo(self, args, kwargs)

	def icolumnsInfo(self, columns = None, attributes = None):
		return mm.columnsInfo(self, columns, attributes)

	def ifamilyInfo(self,columns):
		return mm.ifamilyInfo(self,columns)

#class BaseModel(object, metaclass = MetaModel):
class BaseModel(object, metaclass = MetaObjects):
	_name = None
	_table = None
	_tr_table = None
	_class_model = 'A'
	_class_category = None
	_schema = None
	_names = None
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
	_i18n_constraints = []
	_sql_constraints = []
	_i18n_sql_constraints = []
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
	_family = {}
	_i18n_family ={}
	_i18n_columns = {}
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
		nostorecomputefields = list(filter(lambda x: x in fields,self._nostorecomputefields))
		m = self
		fields = list(item.keys())
		if len(nostorecomputefields) > 0:
			ci = m.columnsInfo(columns=m._computefields,attributes=['compute','priority'])
			priority = {}
			for compute_field in nostorecomputefields:
				priority.setdefault(ci[compute_field]['priority'],set()).add(ci[compute_field]['compute'])
			
			pkeys = list(priority.keys())
			pkeys.sort()
			for pkey in pkeys:
				for compute_method in priority[pkey]:			
					method = getattr(m,compute_method,None)
					if method and callable(method):
						r = method(item,context)
						if r is not None: 
							res.update(r)
	
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

	def readforupdate(self,ids,fields=None,context={}):
		if hasattr(self,'_session'):
			uid = self._getCacheID('readforupdate',context)
			return getattr(self._session._cache[uid],'_readforupdate')(self,ids,fields,context)

	def write(self,records,context={}):
		if hasattr(self,'_session'):
			if 'cache' in context:
				return records
			else:
				uid = self._getCacheID('write',context)
				return getattr(self._session._cache[uid],'_write')(self,records,context)

	def modify(self,records,context={}):
		if hasattr(self,'_session'):
			if 'cache' in context:
				return records
			else:
				uid = self._getCacheID('modify',context)
				return getattr(self._session._cache[uid],'_modify')(self,records,context)

	def create(self,records,context={}):
		if hasattr(self,'_session'):
			if 'cache' in context:
				return records
			else:
				uid = self._getCacheID('create',context)
				return getattr(self._session._cache[uid],'_create')(self,records,context)

	def unlink(self,ids,context={}):
		if hasattr(self,'_session'):
			if 'cache' in context:
				return ids
			else:
				uid = self._getCacheID('unlink',context)
				return getattr(self._session._cache[uid],'_unlink')(self,ids,context)

	def select(self,fields = None ,cond = None, context = {}, limit = None, offset = None):
		if hasattr(self,'_session'):
			uid = self._getCacheID('select',context)
			return getattr(self._session._cache[uid],'_select')(self,fields, cond, context, limit, offset)

	def selectforupdate(self,fields = None ,cond = None, context = {}, limit = None, offset = None):
		if hasattr(self,'_session'):
			uid = self._getCacheID('selectforupdate',context)
			return getattr(self._session._cache[uid],'_selectforupdate')(self,fields, cond, context, limit, offset)

	def update(self,record, cond = None,context = {}):
		if hasattr(self,'_session'):
			if 'cache' in context:
				return record
			else:
				uid = self._getCacheID('update',context)
				return getattr(self._session._cache[uid],'_update')(self,record,cond,context)

	def upsert(self,fields, values,context = {}):
		if hasattr(self,'_session'):
			if 'cache' in context:
				return values
			else:
				uid = self._getCacheID('upsert',context)
				return getattr(self._session._cache[uid],'_upsert')(self,fields, values,context )

	def insert(self,fields, values,context = {}):
		if hasattr(self,'_session'):
			if 'cache' in context:
				return values
			else:
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

	def treeforupdate(self,fields = None ,parent = None, context = {}):
		if hasattr(self,'_session'):
			uid = self._getCacheID('treeforupdate',context)
			return getattr(self._session._cache[uid],'_treeforupdate')(self,fields,parent, context)

	def browse(self,ids,fields=None,context={}):
		if hasattr(self,'_session'):
			uid = self._getCacheID('browse',context)
			return getattr(self._session._cache[uid],'_browse')(self,ids,fields,context)

	def selectbrowse(self, fields = None ,cond = None, context = {}, limit = None, offset = None):
		if hasattr(self,'_session'):
			uid = self._getCacheID('selectbrowse',context)
			return getattr(self._session._cache[uid],'_selectbrowse')(self, fields ,cond, context , limit, offset )

	def o2mread(self, oid, field,fields, context):
		if hasattr(self,'_session'):
			uid = self._getCacheID('_02mread',context)
			return getattr(self._session._cache[uid],'o2mread')(self, oid, field,fields, context)
	
		def m2mread(self, oid, field, fields, context):
			if hasattr(self,'_session'):
				uid = self._getCacheID('m2mread',context)
				return getattr(self._session._cache[uid],'_m2mread')(self, oid, field, fields, context)
		
		def m2mcreate(self,rel,id1,id2,oid,rels,context):
			if hasattr(self,'_session'):
				uid = self._getCacheID('m2mcreate',context)
				return getattr(self._session._cache[uid],'_m2mcreate')(self,rel,id1,id2,oid,rels,context)
		
		def m2mwrite(self,rel,id1,id2,oid,rels,context):
			if hasattr(self,'_session'):
				uid = self._getCacheID('m2mwrite',context)
				return  getattr(self._session._cache[uid],'_m2mwrite')(self,rel,id1,id2,oid,rels,context)
		
		def m2mmodify(self,rel,id1,id2,oid,rels,context):
			if hasattr(self,'_session'):
				uid = self._getCacheID('m2mmodify',context)
				return getattr(self._session._cache[uid],'_m2mmodify')(self,rel,id1,id2,oid,rels,context)
		
		def _m2munlink(self,rel,id1,id2,oid,rels,context):
			if hasattr(self,'_session'):
				uid = self._getCacheID('m2munlink',context)
				return getattr(self._session._cache[uid],'_m2munlink')(self,rel,id1,id2,oid,rels,context)


	@property
	def _columnsmeta(self):
		r = {}

		for k in self._columns.keys():
			r[k] = self._columns[k]._type

		return r 

	@property
	def _rowfields(self):
		return list(filter(lambda x: self._columns[x]._type not in ('one2many','many2many','one2related'),self._columns.keys())) 

	@property
	def _i18nfields(self):
		return list(filter(lambda x: self._columns[x]._type == 'i18n',self._columns.keys())) 


	@property
	def _m2ofields(self):
		return list(filter(lambda x: self._columns[x]._type == 'many2one',self._columns.keys())) 

	@property
	def _m2orelatedfields(self):
		return list(filter(lambda x: self._columns[x]._type in ('many2one','referenced','related'),self._columns.keys())) 

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
	def _jsonfields(self):
		return list(filter(lambda x: self._columns[x]._type == 'json',self._columns.keys())) 


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
		return list(filter(lambda x: hasattr(self._columns[x],'readonly') and self._columns[x].readonly or hasattr(self._columns[x],'compute') and self._columns[x].compute and hasattr(self._columns[x],'store') and self._columns[x].store,self._columns.keys())) 

	@property
	def _on_change_fields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'on_change') and self._columns[x].on_change and type(self._columns[x].on_change) == str,self._columns.keys())) 

	@property
	def _on_check_fields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'on_check') and self._columns[x].on_check and type(self._columns[x].on_check) == str,self._columns.keys())) 
	
	@property
	def _computefields(self):
		return list(filter(lambda x: self._columns[x]._type == 'i18n' and hasattr(self._columns[x].column,'compute') and self._columns[x].column.compute and type(self._columns[x].column.compute) == str or  hasattr(self._columns[x],'compute') and self._columns[x].compute and type(self._columns[x].compute) == str,self._columns.keys())) 

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
		return list(filter(lambda x: hasattr(self._columns[x],'store') and not self._columns[x].store or hasattr(self._columns[x],'compute') and type(self._columns[x].compute) in (list,tuple),self._columns.keys())) 

	@property
	def _requiredfields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'required') and self._columns[x].required,self._columns.keys())) 

	@property
	def _storefields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'store') and self._columns[x].store,self._columns.keys())) 

	@property
	def _selectablefields(self):
		return list(filter(lambda x: hasattr(self._columns[x],'store') and self._columns[x].store or self._columns[x]._type in ('one2many','many2many','text','xml','binary'),self._columns.keys())) 

	def _getMessage(self ,area,code,context={}):
		r = self._pool.get('bc.messages').select(['area','code','descr'],[('area','=',area),('code','=',code)],context,limit=1)
		if len(r) > 0:
			return r[0]
	
	def _getUid(self,cr):
		rowcount = self._.execute('select uuid_v4()::UUID as id')
		if rowcount > 0:
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

	def checkAccess(self,mode = None):
		return mm.checkAccess(self,mode = None)

	def _getParentIdName(self):
		return mm. _getParentIdName(self)
	
	def _getChildsIdName(self):
		return mm._getChildsIdName(self)

	def _getRecNameName(self):
		return mm._getRecNameName(self)

	def _getRowNameName(self):
		return mm._getRowNameName(self)

	def _getCompleteNameName(self):
		return mm._getCompleteNameName(self)


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

	def _getMatrixNames(self):
		return mm._getMatrixNames(self)

	def _getSpecName(self,name):
		return mm._getSpecName(self,name)

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

	def _compute_composite(self ,field,item,context):
		return mm._compute_composite(self ,field,item,context)

	def _compute_complete_composite(self ,item,context):
		return mm._compute_complete_composite(self ,item,context)

	def _compute_composite_tree(self ,field,item,context):
		return mm._compute_composite_tree(self ,field,item,context)

	def _compute_decomposite(self ,field,item,context):
		return mm._compute_decomposite(self ,field,item,context)


	# def _getAccess(self):
		# return mm._getAccess(self)

	# def _getAuth(self):
		# return mm._getAuth(self)

	# def _buildXMLForDynamicModel(self):
		# return mm._buildXMLForDynamicModel(self)

	def modelInfo(self, args = [],kwargs = {}):
		return mm.modelInfo(self, args, kwargs)

	def columnsInfo(self, columns = None, attributes = None):
		#return mm.columnsInfo(self, columns, attributes)
		v = mm.modelInfo(self, [],{'columns':{'columns':columns,'attributes':attributes}})
		if 'columns' in v:
			return v['columns']
		
		return v

	def familyInfo(self,columns):
		return mm.familyInfo(self,columns)

	def do_upload_csv(self, fields, values,context = {}):
		return mm.do_upload_csv(self, fields, values,context)

	def do_action(self, action, column, record, context = {}):
		return mm.do_action(self, action, column, record, context)
	def _mcache(self ,key,value,idx=-1,context={}):
		return mm._mcache(self ,key,value,idx,context)
	
	def compute_columns_values(self ,columns,item,context):
		return mm._compute_columns_values(self ,columns,item,context)

	@property 
	def _ParentIdName(self):
		return mm. _getParentIdName(self)

	@property 
	def _ChildsIdName(self):
		return mm._getChildsIdName(self)

	@property 
	def _RecNameName(self):
		return mm._getRecNameName(self)

	@property 
	def _RowNameName(self):
		return mm._getRowNameName(self)

	@property 
	def _CompleteNameName(self):
		return mm._getCompleteNameName(self)


	@property 
	def _FullNameName(self):
		return mm._getFullNameName(self)

	@property 
	def _SequenceName(self):
		return mm._getSequenceName(self)

	@property 
	def _DateName(self):
		return mm._getDateName(self)

	@property 
	def _StartDateName(self):
		return mm._getStartDateName(self)

	@property 
	def _EndDateName(self):
		return mm._getEndDateName(self)

	@property 
	def _FromDateName(self):
		return mm._getFromDateName(self)

	@property 
	def _ToDateName(self):
		return mm._getToDateName(self)

	@property 
	def _FromTimeName(self):
		return mm._getFromTimeName(self)

	@property 
	def _ToTimeName(self):
		return mm._getToTimeName(self)

	@property 
	def _ProgressName(self):
		return mm._getProgressName(self)

	@property 
	def _ProjectTypeName(self):
		return mm._getProjectTypeName(self)

	@property 
	def _StateName(self):
		return mm._getStateName(self)

	@property 
	def _InactiveName(self):
		return mm._getInactiveName(self)

	@property 
	def _LatitudeName(self):
		return mm._getLatitudeName(self)

	@property 
	def _LongitudeName(self):
		return mm._getLongitudeName(self)

	@property 
	def _FromLatitudeName(self):
		return mm._getFromLatitudeName(self)

	@property 
	def _FromLongitudeName(self):
		return mm._getFromLongitudeName(self)

	@property 
	def _ToLatitudeName(self):
		return mm._getToLatitudeName(self)

	@property 
	def _ToLongitudeName(self):
		return mm._getToLongitudeName(self)

	@property 
	def _MatrixNames(self):
		return mm._getMatrixNamesName(self)


	@property 
	def _Names(self):
		return mm._getNames(self,names=None)

class Model(BaseModel):
	_transient = None

class TransientModel(BaseModel):
	_transient = True

class ModelInherit(BaseModelInherit):
	_transient = True
