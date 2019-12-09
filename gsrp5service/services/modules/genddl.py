from functools import reduce
from orm.common import *

def getName(name):
	if name.islower() and name.upper() not in SQL_RESERVED_KEYWORDS:
		l = ''
	else:
		l = '"'
	return l+name+l

def getColumnName(name):
	if name in MAGIC_COLUMNS:
		raise (ColumnNameError, name)
	return getName(name)

def getColumnType(column):
	return column['db_type']

def getColumnSize(column):
	if 'size' in column and column['size'] and column['type'] in ('char','varchar','selection','float','decimal','numeric'):
		if type(column['size']) == tuple:
			return '%s' % (column['size'],)
		else:
			return '(%s)' % (column['size'],)
	else:
		return ''

def getColumnConstraints(pool,column,name,rec_name):
	_c = ''
	if 'required' in column and type(column['required']) == bool and column['required']:
		_c += ' NOT NULL'
	# if 'type' in column and column['type'] in ('many2one','related'):
		# _c += ' REFERENCES ' + pool.get(column['obj'])._table + ' (id)'
		# if 'on_delete' in column  and column['on_delete'] != None:
			# _c += ' ON DELETE'+ RESTRCT_TYPE_DB.get(column['on_delete'].lower(), ' NO ACTION')
		# if 'on_update' in column and column['on_update'] != None:
			# _c += ' ON UPDATE'+ RESTRCT_TYPE_DB.get(column['on_update'].lower(), ' NO ACTION')
	if rec_name and name == rec_name or 'unique' in column and column['unique']:
		_c += ' UNIQUE'
	if 'check' in column and column['check'] != None:
		_c += ' CHECK ('+ column['check'] +')'
	#print('getColumnConstraints',column,_c)
	return _c

def getReferencedConstraints(pool,model):
	_sqls = []
	self = pool.get(model)
	columns_info = pool.get(model).modelInfo()['columns']
	for key in self._m2orelatedfields:
		cn = 'fk_' + key + '_ref_' + columns_info[key]['obj'].replace('.','_')
		ref = columns_info[key]['obj'].replace('.','_')
		c = columns_info[key]
		_sqls.append(getReferencedColumnConstraints(self._table,cn,key,ref,c))
	
	return _sqls
def getColumnComputed(column):
	_c = ''
	if type(column['compute']) in (list,tuple):
		_c = ' AS '+ column['compute'][0]
		if len(column['compute']) > 1:
			if type(column['compute'][1]) == str:
				_c += ' ' + column['compute'][1]
			elif type(column['compute'][1]) == bool and column['compute'][1]:
				_c += ' STORED'
	return _c


def getReferencedColumnConstraints(tablename,constraintname,columnname,ref,column):
	_c = ''
	"""
	CONSTRAINT fk_demand_item_id_ref_srm_demand_items FOREIGN KEY (demand_item_id) REFERENCES srm_demand_items (id) ON DELETE CASCADE ON UPDATE CASCADE
	
	"""
	_c = "ALTER TABLE IF EXISTS %s ADD CONSTRAINT %s FOREIGN KEY (%s) REFERENCES %s (id)" % (tablename,constraintname,columnname,ref)
	if 'on_delete' in column  and column['on_delete'] != None:
		_c += ' ON DELETE'+ RESTRCT_TYPE_DB.get(column['on_delete'].lower(), ' NO ACTION')
	if 'on_update' in column and column['on_update'] != None:
		_c += ' ON UPDATE'+ RESTRCT_TYPE_DB.get(column['on_update'].lower(), ' NO ACTION')
	#print('getReferencedColumnConstraints',column,_c)
	return _c


def constraintModel(pool,info):
	res =[]
	sql_constaraints = info['sql_constraints']
	for sql_constaraint in sql_constaraints:
		res.append("CONSTRAINT "+ sql_constaraint[0] + ' ' + sql_constaraint[1])
	return res

def columnsModel(pool,info):
	res = []
	columns = info['columns']
	rec_name = info['names']['rec_name']
	for key in columns.keys():
		column = columns[key]
		#print('column:',column)
		if 'db_type' in column and column['db_type']:
			#print('column:',column)
			res.append(getColumnName(key) + ' ' + getColumnType(column) + getColumnSize(column) + getColumnConstraints(pool,column,key,rec_name)+getColumnComputed(column))
	return res



def columnsFamily(pool,info):
	res = []
	families = info['family']
	table = info['table']
	for key in families.keys():
		res.append('FAMILY '+ getName(table + '_' + key) + ' (' + reduce(lambda x, y: x + ',' + y, families[key]) + ')')
	return res

def columnsMagic(pool,info):
	res = []
	res.append("id UUID PRIMARY KEY DEFAULT uuid_v4()::UUID")
	if 'log_access' in info and info['log_access']:
		for key in ('create_uid','create_timestamp','write_uid','write_timestamp'):
			res.append(key + LOG_ACCESS_COLUMNS[key])
	#print('log_access:',res,info['log_access'])
	return res

def columnsIndex(pool,info):
	res = []
	columns = info['columns']
	rec_name = info['names']['rec_name']
	if info['log_access']:
		res.append('INDEX create_uid_idx (create_uid)')
		res.append('INDEX write_uid_idx (write_uid)')
	for key in columns.keys():
		if ('selectable' in columns[key] and columns[key]['selectable'] or columns[key]['type'] in ('many2one','related','state','inactive')) and  key != rec_name:
			res.append('INDEX '+ key + '_idx (' + key +')' )
		if columns[key]['type'] == 'json':
			res.append('INVERTED INDEX '+ key + '_inverted_idx (' + key +')' )
	return res

def relationTable(pool,info):
	res = []
	columns = info['columns']
	for key in columns.keys():
		if columns[key]['type'] == 'many2many':
			rel = getName(columns[key]['rel'])
			id1 = getName(columns[key]['id1'])
			id1_constaraint_name = 'fk_' + id1
			id1_references = getName(info['table'])
	
			res.append("ALTER TABLE IF EXISTS %s ADD CONSTRAINT %s FOREIGN KEY (%s) REFERENCES %s (id) ON DELETE CASCADE ON UPDATE CASCADE" % (rel,id1_constaraint_name,id1, id1_references))

			rel = getName(columns[key]['rel'])
			id1 = getName(columns[key]['id1'])
			id1_index_name = 'idx_' + id1
			id1_index = id1
			id1_references = getName(info['table'])
			id2 = getName(columns[key]['id2'])
			id2_index_name = 'idx_' + id2
			id2_index = id2
			name_unique = 'unique_' + id1 + '_' + id2
			index_unique = id1 + ',' + id2
			
			res.append("CREATE TABLE IF NOT EXISTS %s (id UUID PRIMARY KEY DEFAULT uuid_v4()::UUID, %s UUID REFERENCES %s (id) ON DELETE CASCADE ON UPDATE CASCADE, %s UUID, INDEX %s (%s),INDEX %s (%s), CONSTRAINT %s UNIQUE (%s))" % (rel, id1, id1_references,id2,id1_index_name,id1_index,id2_index_name,id2_index,name_unique,index_unique))
	return res

def createTable(pool,info):
	res =[]
	#print('table:',info['name'])
	res.extend(columnsMagic(pool,info))
	res.extend(columnsModel(pool,info))
	res.extend(constraintModel(pool,info))
	res.extend(columnsFamily(pool,info))
	res.extend(columnsIndex(pool,info))
	sql = "CREATE TABLE IF NOT EXISTS "+info['table'] + ' ('+ reduce(lambda x,y: x + ',' + y,res) + ")"
	res = []
	res.extend(relationTable(pool,info))
	if len(res) > 0:
		m2m = reduce(lambda x,y: x + ';' + y,res)
		if len(m2m) > 0:
			sql += ';' + m2m
	#print('sql:',sql)
	return sql

def AlterTable(pool,info):
	res = []
	for key in info['inherit'].keys():
		for column in info['inherit'][key]['_columns']:
			modelinfo = pool.get(key).modelInfo() 
			if info['columns'][column]['db_type']:
				col = getColumnName(column) + ' ' + getColumnType(info['columns'][column]) + getColumnSize(info['columns'][column]) + getColumnConstraints(pool,info['columns'][column],column,None)
				sql = "ALTER TABLE %s ADD COLUMN IF NOT EXISTS %s"  % (modelinfo['table'],col)
				res.append(sql)
	
	sqls = ''
	
	if len(res) > 0:
		if len(res) == 1:
			sqls = res[0]
		else:
			sqls = reduce(lambda x,y: x + ';' + y,res)
	
	return sqls
