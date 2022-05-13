DMN = {"rec_name":"name",'row_name':'name','complete_name':'complete_name','full_name':'fullname', 'parent_id':'parent_id','childs_id':'childs_id','date':'date','from_date':'from_date','to_date':'to_date','from_time':'from_time','to_time':'to_time','start_date':'start_date','end_date':'end_date','sequence':'sequence','progress':'progress','project_type':'project_type','state':'state','inactive':'inactive','prev_name':'prev_name','next_name':'next_name','transitions':'transitions','latitude':'latitude','longitude':'longitude','from_latitude':'from_latitude','from_longitude':'from_longitude','to_latitude':'to_latitude','to_longitude':'to_longitude','matrix_names':'matrix_names','matrix_col_name':'matrix_col_name','matrix_val_name':'matrix_val_name'}


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

	return n

def _columnsmeta(self):
	r = {}

	for k in self._columns.keys():
		r[k] = self._columns[k]._type

	return r 

def _rowfields(self):
	return list(filter(lambda x: self._columns[x]._type not in ('one2many','many2many','one2related'),self._columns.keys())) 


def _i18nfields(self):
	return list(filter(lambda x: self._columns[x]._type == 'i18n',self._columns.keys())) 



def _m2ofields(self):
	return list(filter(lambda x: self._columns[x]._type == 'many2one',self._columns.keys())) 


def _m2orelatedfields(self):
	return list(filter(lambda x: self._columns[x]._type in ('many2one','referenced','related'),self._columns.keys())) 


def _joinfields(self):
	return list(filter(lambda x: self._columns[x]._type in ('many2one','related','referenced'),self._columns.keys())) 


def _o2mfields(self):
	return list(filter(lambda x: self._columns[x]._type == 'one2many',self._columns.keys())) 


def _o2rfields(self):
	return list(filter(lambda x: self._columns[x]._type == 'one2related',self._columns.keys())) 


def _m2mfields(self):
	return list(filter(lambda x: self._columns[x]._type == 'many2many',self._columns.keys())) 


def _jsonfields(self):
	return list(filter(lambda x: self._columns[x]._type == 'json',self._columns.keys())) 



def _relatedfields(self):
	return list(filter(lambda x: self._columns[x]._type == 'related',self._columns.keys())) 


def _referencedfields(self):
	return list(filter(lambda x: self._columns[x]._type == 'referenced',self._columns.keys())) 


def _selectionfields(self):
	return list(filter(lambda x: self._columns[x]._type == 'selection',self._columns.keys())) 


def _readonlyfields(self):
	return list(filter(lambda x: hasattr(self._columns[x],'readonly') and self._columns[x].readonly or hasattr(self._columns[x],'compute') and self._columns[x].compute and hasattr(self._columns[x],'store') and self._columns[x].store,self._columns.keys())) 


def _on_change_fields(self):
	return list(filter(lambda x: hasattr(self._columns[x],'on_change') and self._columns[x].on_change and type(self._columns[x].on_change) == str,self._columns.keys())) 


def _on_check_fields(self):
	return list(filter(lambda x: hasattr(self._columns[x],'on_check') and self._columns[x].on_check and type(self._columns[x].on_check) == str,self._columns.keys())) 


def _computefields(self):
	return list(filter(lambda x: self._columns[x]._type == 'i18n' and hasattr(self._columns[x].column,'compute') and self._columns[x].column.compute and type(self._columns[x].column.compute) == str or  hasattr(self._columns[x],'compute') and self._columns[x].compute and type(self._columns[x].compute) == str,self._columns.keys())) 


def _domaincomputefields(self):
	return list(filter(lambda x: hasattr(self._columns[x],'domain') and self._columns[x].domain and type(self._columns[x].domain) == str,self._columns.keys())) 


def _selectioncomputefields(self):
	return list(filter(lambda x: hasattr(self._columns[x],'selections') and self._columns[x].selections and type(self._columns[x].selections) == str,self._columns.keys())) 


def _storecomputefields(self):
	return list(filter(lambda x: hasattr(self._columns[x],'compute') and self._columns[x].compute and type(self._columns[x].compute) == str and hasattr(self._columns[x],'store') and self._columns[x].store,self._columns.keys())) 


def _nostorecomputefields(self):
	return list(filter(lambda x: hasattr(self._columns[x],'compute') and self._columns[x].compute and type(self._columns[x].compute) == str and hasattr(self._columns[x],'store') and not self._columns[x].store,self._columns.keys())) 


def _nosavedfields(self):
	return list(filter(lambda x: hasattr(self._columns[x],'store') and not self._columns[x].store or hasattr(self._columns[x],'compute') and type(self._columns[x].compute) in (list,tuple),self._columns.keys())) 


def _requiredfields(self):
	return list(filter(lambda x: hasattr(self._columns[x],'required') and self._columns[x].required,self._columns.keys())) 


def _storefields(self):
	return list(filter(lambda x: hasattr(self._columns[x],'store') and self._columns[x].store,self._columns.keys())) 


def _selectablefields(self):
	return list(filter(lambda x: hasattr(self._columns[x],'store') and self._columns[x].store or self._columns[x]._type in ('one2many','many2many','text','xml','binary'),self._columns.keys())) 


def _findfields(self):
	return list(filter(lambda x: hasattr(self._columns[x],'selectable') and self._columns[x].selectable,self._columns.keys())) 


ALL_ATTRS = ['_name','_table','_tr_table','_class_model','_description','_class_category','_schema','_names','_inherit','_inherits','_checks','_trg_upd_cols','_trigers','_triggers','_hooks','_columns_attrs','_columns','_default','_register','_constraints','_i18n_constraints','_sql_constraints','_i18n_sql_constraints','_order_by','_group_by','_access','_auth','_auto','_actions','_states','_attrs','_col_attrs','_no_copy','_groups','_pages','_family','_i18n_family','_i18n_columns','_indicies','_extra','_full_name','_rec_name','_row_name','_complete_name']

REQUIRED_ATTRS = ['_name','_table','_class_model', '_description','_columns','_order_by']

DEFAULT_ATTRS = {'_class_model':'A','_order_by':'id asc','_register':False,'_auto':True,'_names': _getNames}

DICT_DEFAULT_ATTRS = ['_columns_attrs','_columns','_default','_attrs','_col_attrs','_groups','_pages','_family','_i18n_family','_i18n_columns','_indicies','extra']

ARRAY_DEFAULT_ATTRS = ['_triggers','_constraints', '_sql_constraints','_i18n_sql_constraints','_group_by','_no_copy']

def build(o):
	for a in ALL_ATTRS:
		if hasattr(o,a):
			continue
		else:
			if a in REQUIRED_ATTRS:
				if a in DEFAULT_ATTRS:
					if callable(DEFAULT_ATTRS[a]):
						setattr(o,a,DEFAULT_ATTRS[a](o))
					else:
						setattr(o,a,DEFAULT_ATTRS[a])
				else:
					raise AttributeError("Property %s is required" % (a,))
			else:
				if a in DEFAULT_ATTRS:
					if callable(DEFAULT_ATTRS[a]):
						setattr(o,a,DEFAULT_ATTRS[a](o))
					else:
						setattr(o,a,DEFAULT_ATTRS[a])
				elif a in DICT_DEFAULT_ATTRS:
					setattr(o,a,{})
				elif a in ARRAY_DEFAULT_ATTRS: 
					setattr(o,a,[])
				else: 
					setattr(o,a,None)

class b(object):
	def __init__(self,t):
		self._type = t

class a(object):
	_name='a'
	_table = 'a'
	_description = 'Table a'
	_columns = {'parent_id':b('many2one')}
	_parent_id = 'parent_id'
	
	def n(self):
		return 'Property'
	
	def f(self):
		pass
o = a()
build(o)
for k in dir(o):
	if k.startswith('__'):
		continue
	print(k,'=',getattr(o,k))
print(dir(o))
