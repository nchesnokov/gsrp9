from functools import reduce
from datetime import datetime
from .common import MAGIC_COLUMNS

BOOLEAN_OPERATOR = {'|':' OR ','&': ' AND ','!':' NOT '}
IS_OPERATOR = {'?': ' IS NULL','!?':' IS NOT NULL'}
WHERE_OPERATOR = ['=','!=','>','>=','<','<=','like','ilike','~','~*','in','between']

class gensql_exception(Exception): pass

def convert(val):		
	if type(val) in (tuple,list):
		if len(val) == 1:
			return val[0]
		elif len(val) == 2:
			return val[0] + val[1]
		elif len(val) == 3:
			return val[0] + val[1] + convert(val[2])
		else:
			return reduce(lambda x,y: x + ',' + convert(y),val)
	elif type(val) == str:
		return "'%s'" % (val,)
	else:
		return "%s" % (val,)

def fields_clause(fields = None):
	if fields:
		return reduce(lambda x,y: x +',' + y,fields)
	return ""

def fields_clause_select(fields = None):
	if fields:
		return "id," + fields_clause(fields)
	return "id"

def fields_clause_insert(fields = None):
	if fields:
		return " (" + fields_clause(fields) + ")"
	return ""

def fields_clause_upsert(fields = None):
	if fields:
		return " (" + fields_clause(fields) + ")"
	return ""


def count_clause():
		return select_clause() + "count(*) as count"

def search_clause():
	return select_clause() + 'a.id '

def select_clause():
	return "SELECT "

def insert_clause():
		return "INSERT "

def upsert_clause():
	return "UPSERT "

def set_clause(fields):
	res = []
	for field in fields:
		res.append(field + ' = %s')
	return " SET " + reduce(lambda x,y:x + ',' + y, res)

def update_clause():
	return "UPDATE "

def delete_clause():
	return "DELETE "

def from_clause(tablename):
	return ' FROM ' + tablename

def on_conflict_clause(uf):
	if len(uf) > 0:
		#return ' ON CONFLICT (id) DO NOTHING'
		if len(uf) == 1:
			c = uf[0]
			e = 'id = excluded.id'
		else:
			c = reduce(lambda x,y: x + ',' + y,uf)
			#e1 = []
			#for u in uf:
				#e1.append(u + ' = excluded.' + u)
			#e = reduce(lambda x,y: x + ',' + y,e1)
			e = 'id = excluded.id'
		res = " ON CONFLICT (%s) DO UPDATE SET %s" % (c,e)
	else:
		res = ''
	
	return res
# Parses

def fields_from_order_by(self):
	s = []
	for s1 in self.modelInfo()['order_by'].split(','):
		s2 = s1.split(' ')[0]
		if s2 == 'id':
			recname = self._getRecNameName()
			if recname:
				s.append(recname)
			else:
				s.append(s2)
		else:
			s.append(s2)
	return s

def _convert_cond(self,cond):
	def _cond_convert(self,cond):
		conv = []
		for c in cond:
			if type(c) == dict and '__tuple__' in c:
				conv.append(tuple(c['__tuple__']))
			#elif type(c) == list:
				#conv.extend(_cond_convert(self,c))
			elif type(c) == str:
				conv.append(c)
			else:
				conv.append(c)
		return conv

	return _cond_convert(self,cond)

def _build_condfields(self,cond=None):
	def _condfields_parse(self,cond):
		if cond is None:
			cond = []
	
		condfields  = []
		for c in cond:
			if type(c) == tuple:
				if c[0] in self._nostorecomputefields:
					raise gensql_exception('Condition field: %s in model: %s must be store in database. Condition: %s' % (c[0],self._name,cond))
				if len(c) in (1,3):
					condfields.append(c[0])
				else:
					if c[1] in IS_OPERATOR: 
						condfields.append(IS_OPERATOR[c[1]])
					else:
						condfields.append(c[2])
			elif type(c) == list:
				condfields.extend(_condfields_parse(self,c))
			elif type(c) == str:
				if c in BOOLEAN_OPERATOR: 
					condfields.append(BOOLEAN_OPERATOR[c])
				else:
					raise gensql_exception('Is not logical operator: %s in model: %s. Condition: %s' % (c,self._name,cond))
		
		return condfields

	return _condfields_parse(self,cond)

def _build_joins(self,modinfo,fields,condfields):
	joins = {}
	for field in filter(lambda x: x in fields or x in condfields,self._joinfields):
		if 'obj' in modinfo['columns'][field]:
			joins.setdefault(modinfo['columns'][field]['obj'],[]).append(field)
		else:
			objref,fieldref = modinfo['columns'][field]['ref'].split('.')
			obj = modinfo['columns'][objref]['obj']
			joins.setdefault(obj,[]).append(field)
	
	return joins

def _build_aliases(self,joins=None):
	"""
	joins = {'model1':['field1'],'model2':['field1','field2']}
	"""
	aliases ={}
	curalias = 'c'
	if joins is None:
		joins = {}
	for key in joins.keys():
		l = len(joins[key])
		fields = joins[key]
		columnsinfo = self.columnsInfo(attributes=['type','ref'])
		fieldsref = list(filter(lambda x: columnsinfo[x]['type'] == 'referenced',self._columns.keys()))
		for i in range(l):
			if fields[i] in fieldsref:
				objref = columnsinfo[fields[i]]['ref'].split('.')[0]
				aliases.setdefault(key,{})[fields[i]] = aliases[key][objref]
			else:
				aliases.setdefault(key,{})[fields[i]] = curalias + '%s' % (i,)
		if curalias[-1] == 'z':
			curalias += 'a'
		else:
			curalias = curalias[:-1] + chr(ord(curalias[-1])+1)
			
	return aliases

def parse_joins(self,pool, model, aliases,joins = None):
	"""
	joins = {'model1':'field1','model2':'field2'}
	"""
	if joins is None:
		joins = {}

	join = pool.get(model)._table + ' AS a' 
	parent_id = pool.get(model)._getParentIdName()
	if parent_id and model in joins and parent_id in joins[model]:
		join += ' LEFT OUTER JOIN ' + pool.get(model)._table +' AS b ON (b.id = a.' + parent_id + ')'
	
	for key in joins.keys():
		for field in list(filter(lambda x: x in self._storefields,joins[key])):
			join += ' LEFT OUTER JOIN '+pool.get(key)._table + ' AS ' + aliases[key][field] + ' ON (' + aliases[key][field] + '.id = a.'  + field  + ')'
		
	return join

def _build_joinmodels(self,joins = None):
	"""
	joins = {'field1':'model1','field2':'model2'}
	"""
	joinmodels = {}
	if joins is None:
		joins = {}

	for key in joins.keys():
		for field in joins[key]:
			joinmodels[field] = key
	
	return joinmodels

def parse_cond(self,pool,aliases,models,cond = None):
	def _cond_parse(self,pool,aliases,models,cond):
		conds  = []
		for c in cond:
			if type(c) == tuple:
				if c[0] in models:
					m = models[c[0]]
					recname = pool.get(m)._getRecNameName()
					parent_id = pool.get(m)._getParentIdName()
					if recname:
						if  parent_id and c[0] == parent_id: 
							c0 = 'b.' + recname
						else:
							c0 = aliases[m][c[0]] + '.' + recname
					else:
						c0 = 'a.' +c[0]
				else:
					c0 = 'a.' + c[0]
				lc = len(c)
				if lc == 3:
					conds.append((c0,c[1],c[2]))
				elif lc == 1:
					conds.append((c0,))
				elif lc == 2:
					conds.append((c0,c[1]))
			elif type(c) == str:
				if c in BOOLEAN_OPERATOR:
					conds.append(BOOLEAN_OPERATOR[c])
				else:
					raise gensql_exception('Is not logical operator: %s in model: %s. Condition: %s' % (c,self._name,cond))
			elif type(c) == list:
				conds.append(_cond_parse(self,pool,aliases,models,c))
		
		return conds
	
	if cond is None:
		cond = []

	return _cond_parse(self,pool,aliases,models,cond)

def parse_fields(self,pool,aliases,models,fields = None, columnsmeta=None):
	"""

	models = {'field1':'model1','field2':'model2'}
	"""
	f = []
	
	if fields is None:
		fields = []

	if columnsmeta is None:
		columnsmeta = {'id':'uuid'}
	
	if not 'id' in columnsmeta:
		columnsmeta['id'] = 'uuid'
	for field in fields:
		if type(field) == str:
			if field in columnsmeta and columnsmeta[field] in ('one2many','many2many'):
				f.append('NULL AS ' + field)
			elif field in columnsmeta and columnsmeta[field] == 'referenced':
				colinfo = self.columnsInfo(columns=[field])[field]
				objref,fieldref = colinfo['ref'].split('.')
				obj = self.columnsInfo(columns=[objref])[objref]['obj']
				f.append(aliases[models[field]][field] + '.' + fieldref + ' as ' + field)
				
			else:
				f.append('a.' + field)
				if field in models:
					recname = pool.get(models[field])._getRecNameName()
					parent_id = pool.get(models[field])._getParentIdName()
					if recname and type(recname) == str:
						if field == parent_id:
							f.append('b.' + recname + ' as "' + field + '-name"')
						else:
							f.append(aliases[models[field]][field] + '.' + recname + ' as "' + field + '-name"')
		elif type(field) == dict:
			recname = pool.get(models[vf])._getRecNameName()
			if recname and type(recname) == str and recname not in field:
				field.append(recname)
			for vf in field.keys():
				if vf in columnsmeta and columnsmeta[vf] in ('one2many','many2many'):
					f.append('NULL AS ' + vf)
				if vf in models:
					recname = pool.get(models[vf])._getRecNameName()
					if recname and type(recname) == str:
						f.append(aliases[models[vf]] + '.' + recname + ' AS "' + vf + '-name"')
		else:
			Exception('Type fields: %s not avaliable' % (type(field),))

	return f

def parse_order_by(self,pool,aliases,models,order_by = None, columnsmeta=None):
	"""

	models = {'field1':'model1','field2':'model2'}
	"""
	o = []
	
	if order_by is None:
		return o

	if columnsmeta is None:
		columnsmeta = {'id':'uuid'}
	
	if not 'id' in columnsmeta:
		columnsmeta['id'] = 'uuid'

	s = []
	for s1 in order_by.split(','):
		s2 = s1.split(' ')
		if len(s2) == 1:
			s2.append('asc')
		s.append(s2)
	for field,sort in s:
		if field == 'id':
			recname = self._getRecNameName()
			if recname:
				o.append(('a.'+recname,sort))
			else:
				o.append(('a.'+field,sort))
		elif field in columnsmeta and columnsmeta[field] in ('many2one','related'):
			recname = pool.get(models[field])._getRecNameName()
			if recname:
				if type(recname) == str:
					o.append(('"' + field + '-name"',sort))
			else:
				o.append((recname,sort))
		else:
			o.append((field,sort))

	return o

# Parses

def into_clause(tablename):
	return ' INTO ' + tablename

def where_clause_unlink_ids(ids):
	_where = " WHERE id %s "
	_op = 'IN %s'
	if type(ids) == str:
		_op = '= %s'
	return _where % (_op,)


def where_clause_ids(ids):
	_where = " WHERE a.id %s "
	_op = 'IN %s'
	if type(ids) == str:
		_op = '= %s'
	return _where % (_op,)

def returning_clause(fields = None):
	if fields:
		return " RETURNING id," + reduce(lambda x,y: x +',' + y,fields) + " "
	else:
		return " RETURNING id"
	
def offset_clause(offset):
	if offset:
		return ' OFFSET %s'
	return ''

def limit_clause(limit):
	if limit:
		return ' LIMIT %s'
	return ''

def orderby_clause(order_by = None):
	res = ''
	if order_by and len(order_by) > 0:
		for field,sort in order_by:
			if len(res) > 0:
				res += ',' 
			res += field
			if sort:
				res += ' ' + sort				
	if len(res) > 0:
		res = ' ORDER BY ' + res 
	return res

def groupby_clause(group_by = None):
	if group_by:
		if type(group_by) in (str,bytes):
				return ' GROUP BY %s' % (group_by,)
		elif type(group_by) in (tuple,list):
			return ' GROUP BY %s' % reduce(lambda x,y: x+','+y, group_by)
		else:
			return ''
	return ''

def having_clause(having = None):
	if having:
		return ' HAVING %s' % (having,)
	return ''

def where_clause(cond):
	if len(cond) > 0:
		return ' WHERE ' + cond
	return ''

def values_clause(vl):
	return  ' VALUES (' + reduce(lambda x,y: x + ',' +  y,['%s']*vl) + ')'

def values_insert_clause1(vls):
	vals = []
	if len(vls) > 1:
		for vl in vls:
			if len(vl) > 1:
				vals.append('(' + reduce(lambda x,y: x + ',' +  convert(y),vl) + ')')
			else:
				vals.append('(' + convert(vl) + ')')
		return  ' VALUES ' + reduce(lambda x,y: x + ',' +  y,vals)

	return ' VALUES (' + convert(vls[0]) + ')'

def values_upsert_clause1(vls):
	vals = []
	if len(vls) > 1:
		for vl in vls:
			if len(vl) > 1:
				vals.append('(' + reduce(lambda x,y: x + ',' +  convert(y),vl) + ')')
			else:
				vals.append('(' + convert(vl) + ')')
		return  ' VALUES ' + reduce(lambda x,y: x + ',' +  y,vals)

	return ' VALUES (' + convert(vls[0]) + ')'

def values_insert_clause(vls):
	vals = []
	for vl in vls:
		vals.extend(vl)
	
	return vals

def array_insert_clause(lf,lv):
	if lv > 1:
		return ' VALUES ' + reduce(lambda x,y: x+','+y,['('+reduce(lambda x,y: x+','+y,['%s']*lf)+')']*lv)
	else:
		return ' VALUES ' + '('+reduce(lambda x,y: x+','+y,['%s']*lf)+')'


def values_upsert_clause(vls):
	vals = []
	for vl in vls:
		vals.extend(vl)
	
	return vals

def array_upsert_clause(lf,lv):
	if lv > 1:
		return ' VALUES ' + reduce(lambda x,y: x+','+y,['('+reduce(lambda x,y: x+','+y,['%s']*lf)+')']*lv)
	else:
		return ' VALUES ' + '('+reduce(lambda x,y: x+','+y,['%s']*lf)+')'



def domain_clause(info):
	columns = info['columns']
	va = list(filter(lambda x: 'domain' in x and x['domain'],columns))
	if len(va) > 0:
		return va
	return []
#tested
def Create(self,pool,uid,info,record,context):
	fields = list(record.keys())
	values = list(record.values())

	if info['log_access']:
		fields.extend(['create_uid','create_timestamp'])
		values.extend([uid,datetime.utcnow()])

	_sql = insert_clause() + into_clause(info['table']) + fields_clause_insert(fields) + values_clause(len(values))+returning_clause()

	return _sql, values

def Insert(self,pool,uid,info,fields,values,context):
	if id in fields:
		raise gensql_exception('Fields: id not be present to be insert into database')

	columnsinfo = info['columns']
	storefields = list(filter(lambda x: x in fields,self._storefields))

	columns = info['columns']
	requiredFields = self._requiredfields
	for field in storefields:
		if not field in columns:
			raise gensql_exception("Field: %s not found in model: %s" % (field, info['name']))

	for requiredField in requiredFields:		
		if requiredField not in storefields:
			raise gensql_exception("Field: %s model: %s is required not found in record: %s" % (requiredField, info['name'], fields))

	if info['log_access']:
		if not 'create_uid' in fields:
			fields.extend(['create_uid','create_timestamp'])
		utcnow = datetime.utcnow()
		for value in values:
			value.extend([uid,utcnow])
	
	_sql = insert_clause() + into_clause(info['table']) + fields_clause_insert(fields) + array_insert_clause(len(fields),len(values)) + returning_clause()

	return _sql, values_insert_clause(values)

def Upsert(self,pool,uid,info,fields,values,context):
	columns = info['columns']
	requiredFields = self._requiredfields
	for field in fields:
		if not field in MAGIC_COLUMNS and not field in columns:
			raise gensql_exception("Field: %s not found in model: %s" % (field, info['name']))

	for requiredField in requiredFields:		
		if requiredField not in fields:
			raise gensql_exception("Field: %s model: %s is required not found in record: %s" % (requiredField, info['name'], fields))


	if info['log_access']:
		if not 'write_uid' in fields:
			fields.extend(['write_uid','write_timestamp'])
		utcnow = datetime.utcnow()
		for value in values:
			value.extend([uid,utcnow])

	_sql = upsert_clause() + into_clause(info['table']) + fields_clause_upsert(fields) + array_upsert_clause(len(fields),len(values)) + returning_clause()

	return _sql, values_upsert_clause(values)


#tested
def Read(self,pool,uid,info,ids,fields,context):
	_fields = ['id']
	if fields is None:
		_fields.extend(list(info['columns'].keys()))
	else:
		_fields.extend(fields)

	_fields.extend(filter(lambda x: x != 'id' and x not in _fields,fields_from_order_by(self)))
 
# Parses
	cond = _convert_cond(self,[])
	condfields = _build_condfields(self=self,cond=cond)
	joins = _build_joins(self=self,modinfo = info,fields = _fields,condfields=condfields)
	aliases = _build_aliases(self=self,joins=joins)
	joinmodels = _build_joinmodels(self=self,joins = joins)
	_fields = parse_fields(self=self,pool = pool,aliases = aliases,models=joinmodels,fields = _fields, columnsmeta = self._columnsmeta)
	join = parse_joins(self=self,pool = pool, model = info['name'], aliases = aliases,joins = joins)
	cond = parse_cond(self=self,pool = pool,aliases = aliases,models = joinmodels,cond = cond)
	order_by = parse_order_by(self = self,pool = pool,aliases = aliases,models=joinmodels,order_by = info['order_by'], columnsmeta = self._columnsmeta)
# Parses

	_sql = select_clause() +fields_clause(_fields) + from_clause(join) + where_clause_ids(ids) + orderby_clause(order_by)
	if type(ids) == str:
		_values = [ids]
	else:
		_values = [tuple(ids)]
	return _sql,_values
#tested
def Select(self, pool, uid, info, fields, cond, context, limit, offset):
	_fields = ['id']
	if fields is None:
		_fields.extend(list(info['columns'].keys()))
	else:
		_fields.extend(fields)

	_fields.extend(filter(lambda x: x != 'id' and x not in _fields,fields_from_order_by(self)))

# Parses
	cond = _convert_cond(self,cond)
	condfields = _build_condfields(self=self,cond=cond)
	joins = _build_joins(self=self,modinfo = info,fields = _fields,condfields=condfields)
	aliases = _build_aliases(self=self,joins=joins)
	joinmodels = _build_joinmodels(self=self,joins = joins)
	_fields = parse_fields(self=self,pool = pool,aliases = aliases,models=joinmodels,fields = _fields, columnsmeta = self._columnsmeta)
	join = parse_joins(self=self,pool = pool, model = info['name'], aliases = aliases,joins = joins)	
	cond = parse_cond(self=self,pool = pool,aliases = aliases,models = joinmodels,cond = cond)
	order_by = parse_order_by(self = self,pool = pool,aliases = aliases,models=joinmodels,order_by = info['order_by'], columnsmeta = self._columnsmeta)
	
# Parses
	
	_where = WhereParse(cond)
	_cond = _where._cond
	_values = _where._values
	if limit:
		_values.append(limit)
	if offset:
		_values.append(offset)

	_sql = select_clause() + fields_clause(_fields) + from_clause(join) + where_clause(_cond) + orderby_clause(order_by) + limit_clause(limit) + offset_clause(offset) 
	return _sql,_values
#tested
def Search(self,pool, uid, info, cond, context, limit, offset):
	
	_f = fields_from_order_by(self)
	
	_fields = fields_clause_select(_f).split(',')
 
# Parses
	cond = _convert_cond(self,cond)
	condfields = _build_condfields(self=self,cond=cond)
	joins = _build_joins(self=self,modinfo = info,fields = _fields,condfields=condfields)
	aliases = _build_aliases(self=self,joins=joins)
	joinmodels = _build_joinmodels(self=self,joins = joins)
	_fields = parse_fields(self=self,pool = pool,aliases = aliases,models=joinmodels,fields = _fields, columnsmeta = self._columnsmeta)
	join = parse_joins(self=self,pool = pool, model = info['name'], aliases = aliases,joins = joins)
	cond = parse_cond(self=self,pool = pool,aliases = aliases,models = joinmodels,cond = cond)
	order_by = parse_order_by(self = self,pool = pool,aliases = aliases,models=joinmodels,order_by = info['order_by'], columnsmeta = self._columnsmeta)
# Parses

	_where = WhereParse(cond)
	_cond = _where._cond
	_values = _where._values
	if limit:
		_values.append(limit)
	if offset:
		_values.append(offset)
	_sql = select_clause() +fields_clause(_fields) + from_clause(join) + where_clause(_cond) + orderby_clause(order_by) + limit_clause(limit) + offset_clause(offset) 
	return _sql, tuple(_values)

#tested
def Count(self,pool,uid,info,cond,context):
	
	_fields = fields_clause_select().split(',')

# Parses
	cond = _convert_cond(self,cond)
	condfields = _build_condfields(self=self,cond=cond)
	joins = _build_joins(self=self,modinfo = info,fields = _fields,condfields=condfields)
	aliases = _build_aliases(self=self,joins=joins)
	joinmodels = _build_joinmodels(self=self,joins = joins)
	_fields = parse_fields(self=self,pool = pool,aliases = aliases,models=joinmodels,fields = _fields, columnsmeta = self._columnsmeta)
	join = parse_joins(self=self,pool = pool, model = info['name'], aliases = aliases,joins = joins)
	cond = parse_cond(self=self,pool = pool,aliases = aliases,models = joinmodels,cond = cond)
# Parses


	_where = WhereParse(cond)

	_cond = _where._cond
	_values = _where._values

	_sql = count_clause() + from_clause(join) + where_clause(_cond)
	return _sql,_values
#tested
def Delete(self,pool,uid, info, cond, context):
	
	_where = WhereParse(cond)
	_cond = _where._cond
	_values = _where._values

	_sql = delete_clause() + from_clause(info['table']) + where_clause(_cond) + returning_clause()
	return _sql,_values
#tested
def Unlink(self,pool,uid,info, ids, context):
	_sql = delete_clause() + from_clause(info['table']) + where_clause_unlink_ids(ids) + returning_clause()
	if type(ids) == int:
		_values = [ids]
	else:
		_values = [tuple(ids)]
	return _sql,_values
#tested
def Write(self,pool,uid,info,record,context):
	oid = record['id']
	del record['id']
	fields = list(record.keys())
	values = list(record.values())

	if info['log_access']:
		fields.extend(['create_uid','create_timestamp'])
		values.extend([uid,datetime.utcnow()])
		values.append(oid)
	
	_sql = update_clause() + info['table']+ set_clause(fields) + ' WHERE id = %s' + returning_clause(list(filter(lambda x: x != 'id',fields)))

	return _sql, values
#testing
def Update(sef,pool,uid,info,cond,record,context):
	fields = list(record.keys())
	values = list(record.values())
	columns = info['columns']
	requiredFields = list(filter(lambda x: 'required' in columns[x] and columns[x]['required'] ,columns.keys()))
	for field in fields:
		if field != 'id' and not field in columns:
			raise gensql_exception("Field: %s not found in model: %s" % (field, info['name']))

		if field in requiredFields and record[field] is None:		
				raise gensql_exception("Field: %s model: %s is required not set null: %s" % (requiredFields, info['name'], record))

	if info['log_access']:
		fields.extend(['write_uid','write_timestamp'])
		values.extend([uid,datetime.utcnow()])

	_where = WhereParse(cond)
	_cond = _where._cond
	values.extend(_where._values)

	_sql = update_clause() + info['table']+ set_clause(fields) + where_clause(_cond) + returning_clause(list(filter(lambda x: x != 'id',fields)))
	return _sql, values

def Modify(self,pool,uid,info,record,context):
	fields = list(record.keys())
	values = list(record.values())

	if info['log_access']:
		fields.extend(['create_uid','create_timestamp'])
		values.extend([uid,datetime.utcnow()])

	_sql = upsert_clause() + into_clause(info['table']) + fields_clause_insert(fields) + values_clause(len(values)) + returning_clause()
	return _sql, values

class WhereParse(list):
	_cond = ""
	_values = []
	def __init__(self, conds):
		for cond in conds:
			if type(cond) == dict:
				p = cond.popitem()
				if p[0] == 'tuple':
					cond = tuple(p[1])
			
			if type(cond) == tuple and len(cond) in (2,3):
				if self.isEmpty():
					self.append(cond)
				else:
					#if type(self.Last()) == tuple:
					if type(self.Last()) in (tuple,list):
						self.extend(['&',cond])
					elif type(self.Last()) == str:
						self.append(cond)
						
			elif type(cond) == tuple and len(cond) == 1:
				if self.isEmpty():
					self.append(cond)
				else:
					if type(self.Last()) == tuple:
						self.extend(['&',cond])
					elif type(self.Last()) == str:
						self.append(cond)
				
			elif type(cond) == str:
				if self.isEmpty():
					if cond[0] != '!':
						self.append(cond)
					else:
						raise Exception('Invalid logical operand: %s %s' % (self.Last(),cond))
				else:
					if type(self.Last()) == tuple:
						if type(cond) == type(self.Last()):
							self.extend(['&',cond])
						elif type(cond) == str:
							self.append(cond)
						else:
							self.extend(['(',WhereParse(cond),')'])
					elif type(self.Last()) == str:
						if cond in ('|','&','!','?','!?','(',')'):
							self.append(cond)
						else:
							if self.Last() in ('|','&','(',')'):
								self.append(cond)
							else:
								raise Exception('Invalid logical operand: %s %s' % (self.Last(),cond))
			elif type(cond) == list:
				self.extend(['&','(',WhereParse(cond),')'])
		self._optimize()

		self._cond = self._keys()
		self._values = self._vals()

	def First(self):
		if len(self) > 0:
			return self[0]
		else:
			return None
	
	def Last(self):
		if len(self) > 0:
			return self[-1]
		else:
			return None

	def isEmpty(self):
		return len(self) == 0

	def _optimize(self):
		while self.First() == '(' and self.Last() == ')' and self.count('(') == 1:
			self.pop()
			self.pop(0)

	def _keys(self,childs=None):
		_cond = ''
		if childs is None:
			childs = self
		for child in childs:
			if type(child) == tuple:
				if len(child) == 3:
					if child[1] in WHERE_OPERATOR:
						if type(child[2]) in (tuple,list,set):
							if child[1] == 'in':
								if type(child[2]) in (list,set):
									_cond += child[0] + ' ' + child[1] + ' ' + str(tuple(child[2]))
								else:
									_cond += child[0] + ' ' + child[1] + ' ' + str(child[2])
							elif child[1] == 'between':
								if type(child[2][0]) == str:
									arg1 = "'%s'" % (child[2][0],)
									arg2 = "'%s'" % (child[2][1],)
								else:
									arg1 = child[2][0]
									arg1 = child[2][1]
								_cond += child[0] + ' ' + child[1] + ' ' + arg1 + ' AND ' + arg2
						else:
							_cond += child[0] + ' ' + child[1] + ' %s'
					else:
						raise Exception("Invalid where operator: %s" % (child[1],))
				elif len(child) == 2:
					if child[1] in IS_OPERATOR:
						_cond += child[0] + IS_OPERATOR[child[1]]
					else:
						raise Exception("Invalid is operator: %s" % (child[1],))
				else:
					_cond += child[0]
			elif type(child) == str:
				if child in BOOLEAN_OPERATOR.keys():
					_cond += BOOLEAN_OPERATOR[child]
				else:
					_cond += child
			elif isinstance(child,WhereParse):
				_cond += child._keys()
		return _cond

	def _vals(self,childs = None):
		_values = []
		if childs is None:
			childs = self
		for child in childs:
			if type(child) == tuple:
				if len(child) == 3:
					if child[1] in ('in','between'):
						if not type(child[2]) in (tuple,list,set):
							raise Exception("invalid type operand: %s type: %s" % (child[1],type(child[2])))
					else:
						_values.append(child[2])
			elif isinstance(child,WhereParse):
				_values.extend(child._vals())
		return _values
