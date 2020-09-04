import os
import copy
from functools import reduce
import uuid
from decimal import Decimal
import datetime
import psycopg2
import ctypes
import json
from deepdiff.diff import DeepDiff
from gsrp5service.orm import gensql
from gsrp5service.orm.mm import browse_record, browse_record_list,browse_null
from gsrp5service.orm.common import MAGIC_COLUMNS
#from datetime import datetime,date,time
import time as tm
import web_pdb

from gsrp5service.orm.mm import _m2mfieldid2

MAX_CHUNK_READ = 5000
MAX_CHUNK_DELETE = 5000

class orm_exception(Exception):
	def __init__(self, *args, **kwargs):
		self.args = args
		self.kwargs = kwargs

def _join_diffs(d1,d2):
	keys1 = list(d1.keys())
	for k1 in filter(lambda x: x in keys1,('__o2m_append__',)):
		for r1 in d1[k1]:
			if '__update__' in d2 and r1['__path__'] in d2['__update__']:
				r1['__data__'].update(d2['__update__'][r1['__path__']])
				del d2['__update__'][r1['__path__']]

			if '__insert__' in d2 and r1['__path__'] in d2['__insert__']:
				r1['__data__'].update(d2['__insert__'][r1['__path__']])
				del d2['__insert__'][r1['__path__']]

			if '__delete__' in d2 and r1['__path__'] in d2['__delete__']:
				for k2d in d2['__delete__'][r1['__path__']].keys():
					del r1['__data__'][k2d]

	keys2 = list(d2.keys())
	for k2 in filter(lambda x: x in keys2,('__o2m_append__','__o2m_remove__','__m2m_append__','__m2m_remove__','__update__','__insert__','__delete__')):
		if k2 in ('__o2m_append__','__m2m_append__'):
			for r2 in d2[k2]:
				if '__update__' in d2 and r2['__path__'] in d2['__update__']:
					r2['__data__'].update(d2['__update__'][r2['__path__']])
					del d2['__update__'][r2['__path__']]

				if '__insert__' in d2 and r2['__path__'] in d2['__insert__']:
					r2['__data__'].update(d2['__insert__'][r2['__path__']])
					del d2['__insert__'][r2['__path__']]

				if '__delete__' in d2 and r2['__path__'] in d2['__delete__']:
					for k2d in d2['__delete__'][r2['__path__']].keys():
						del r2['__data__'][k2d]
			d1[k2].extend(d2[k2])
		elif k2 in ('__o2m_remove__','__m2m_remove__'):
			d1[k2].extend(d2[k2])
		elif k2 in ('__update__','__insert__','__delete__'):
			for k21 in d2[k2].keys():
				d1.setdefault(k2,{})[k21].update(d2[k2][k21])

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

def _do_checks(self, record, context = {}):
	results = []
	if type(record) == dict:
		res = {} 			
		for check in self._checks:
			method = getattr(self,check,None)
			if method and callable(method):
				res[check] = method(record,context)
				results.append(res)
	elif type(record) in (list,tuple):
		result = []
		for r in record:
			res = {}
			for check in self._checks:
				method = getattr(self,check,None)
				if method and callable(method):
					res[check] = method(r,context)
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
			#print('CONV-FIELDS:',field,fields,record)
			if type(field) == str:
				row.append(record[field])
			elif  type(field) == dict:
				for key in field.keys():
					if key in record:
						#print('_conv_dict_to_list_records:',field,fields,key,record)
						if type(record[key]) == dict:
							row.append(_conv_dict_to_list_records(self,field[key],record[key]))
						elif type(record[key]) in (list,tuple):
							row.append(record[key])
		
		#print('CONV-RECORD:',row,record)
		#if 'cache' in context:
			#row.append({'path':uuid.uuid4().hex,'model':self._name})
		rows.append(row)
		
	return rows

def _conv_dict_to_raw_records(self,fields,records,context):
	for record in records:
		for field in filter(lambda x: x != 'id',fields):
			#print('CONV-FIELDS:',field,fields,record)
			if type(field) == str:
				if type(record[field]) == dict and 'id' in record[field]:
					record[field] = record[field]['id']
			elif  type(field) == dict:
				for key in field.keys():
					if key in record:
						#print('_conv_dict_to_list_records:',field,fields,key,record)
						if type(record[key]) == dict:
							record[key] = _conv_dict_to_raw_records(self,field[key],record[key])
						elif type(record[key]) in (list,tuple):
							record[key] = _conv_dict_to_raw_records(self,field[key],record[key])
		
	print('RECORDS:',records)	
		
	return records

def _fetch_results(self,fields,context):
	
	res = []
	
	if 'FETCH' not in context:
		context['FETCH'] = 'DICT'

	fetch = context['FETCH']

	selectablefields = list(filter(lambda x: x in fields,self._selectablefields))
	nostorecomputefields = list(filter(lambda x: x in fields,self._nostorecomputefields))

	records = self._cr.dictfetchall(selectablefields, self._columnsmeta)
	for record in records:
		for field in fields:
			if type(field) == dict:
				recname = self._getRecNameName()
				if recname in record:
					oid = record[recname]
				else:
					if context['FETCH'] == 'LIST':
						oid = self.read(record['id'],[recname],context)[0][0]
					elif context['FETCH'] == 'DICT':
						oid = self.read(record['id'],[recname],context)[0]['id']
					elif context['FETCH'] == 'RAW':
						oid = self.read(record['id'],[recname],context)[0]['id']
				for key in filter(lambda x: x in self._o2mfields,field.keys()):
					columninfo = self.columnsInfo(columns=[key],attributes=['obj','rel','limit','offset'])
					obj = columninfo[key]['obj']
					rel = columninfo[key]['rel']
					record[key] = _o2mread(self = self._pool.get(obj),oid = oid, field = rel, fields = field[key], context = context,limit = columninfo[key]['limit'],offset = columninfo[key]['offset'])

		for field in fields:
			if type(field) == dict:
				for key in filter(lambda x: x in self._m2mfields,field.keys()):
					record[key] = _m2mread(self = self,oid = record['id'], field = key, fields = field[key], context = context)

		_computes = self._compute(record,context)
		if _computes is not None:
			record.update(_computes)
	if fetch == 'DICT':		
		res.extend(records)
	elif fetch == 'LIST':
		res.extend(_conv_dict_to_list_records(self,fields,records,context))
	elif fetch == 'RAW':
		res.extend(_conv_dict_to_raw_records(self,fields,records,context))

	return res

def _createRecords(self, records, context):
	res = []

	trg1 = self._getTriger('bi')
	for trg11 in trg1:
		kwargs = {'r1':records,'context':context}
		trg11(**kwargs)

	for record in records:
		oid = _createRecord(self, record, context)		
		res.append(oid)

	trg2 = self._getTriger('ai')
	for trg22 in trg2:
		kwargs = {'r1':records,'context':context}
		trg22(**kwargs)

	return res

def _createRecord(self, record, context):
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

	for nonefield in list(filter(lambda x: x in record and record[x] is None,fields)):
		if nonefield in record:
			del record[nonefield]
	
	emptyfields = list(filter(lambda x: not x in record and not x in MAGIC_COLUMNS,self._requiredfields))		
	if len(emptyfields) > 0:
		raise orm_exception("Fields: %s of model: %s is required and not found in record: %s" % (emptyfields, self.modelInfo()['name'], record))

	trg1 = self._getTriger('bir')
	for trg11 in trg1:
		kwargs = {'r1':record,'context':context}
		trg11(**kwargs)

	sql,vals = gensql.Create(self, record, context)
	rowcount = self._execute(sql,vals)
	if rowcount > 0:
		oid = self._cr.fetchone()[0]

	trg2 = self._getTriger('air')
	for trg22 in trg2:
		kwargs = {'r1':record,'context':context}
		trg22(**kwargs)

	return oid

def _writeRecords(self, records, context):
	res = []

	trg1 = self._getTriger('bu')
	for trg11 in trg1:
		kwargs = {'r1':records,'r2':records,'context':context}
		trg11(**kwargs)

	for record in records:
		res.append(_writeRecord(self, record, context))		

	trg2 = self._getTriger('au')
	for trg22 in trg2:
		kwargs = {'r1':records,'r2':records,'context':context}
		trg22(**kwargs)

	return res

def _writeRecord(self, record, context):
	oid = None
	fields = list(record.keys())
	modelfields = list(self._columns.keys())
	nomodelfields = list(filter(lambda x: not x in modelfields and not x in MAGIC_COLUMNS,fields))
	if len(nomodelfields) > 0:
		raise orm_exception("Fields: %s not found in model: %s" % (nomodelfields, self._name))

	for nosavedfield in self._nosavedfields:
		if nosavedfield in record:
			del record[nosavedfield]
	columnsinfo = self.columnsInfo(columns = fields)
	
	emptyfields = list(filter(lambda x: x in fields and record[x] is None,self._requiredfields))		

	if len(emptyfields) > 0:
		raise orm_exception("Fields: %s of model: %s is required and not found in record: %s" % (emptyfields, self._name, record))

	trg1 = self._getTriger('bur')
	record2 =None
	upd_cols = set()
	if trg1 and len(trg1) > 0:
		ctx = context.copy()
		ctx['FETCH'] = 'RAW'
		record21 = self.read(record['id'], self._selectablefields, ctx)

		if len(record21) > 0:
			record2 = record21[0]
		
		if record2:
			k1 = set(list(record.keys()))
			k2 = set(list(record2.keys()))
			uk = list(set(k1).intersection(set(k2)))
			ik = list(set(k1)- set(k2))
			dk = list(set(k2)- set(k1))
			
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
		
			if len(upd_cols) > 0:
		
				for trg11 in trg1:
					kwargs = {'r1':record,'r2':record,'context':context}
					trg11(**kwargs)

	sql,vals = gensql.Write(self, record, context)
	rowcount = self._execute(sql,vals)
	if rowcount > 0:
		oid = self._cr.fetchone()[0]

	if len(upd_cols) > 0:
		trg2 = self._getTriger('aur')
		if trg2 and len(trg2) > 0:
			for trg22 in trg2:
				kwargs = {'r1':record,'r2':record,'context':context}
				trg22(**kwargs)

	return oid

def _modifyRecords(self, records, context):
	res = []

	trg1 = self._getTriger('bu')
	for trg11 in trg1:
		kwargs = {'r1':records,'r2':records,'context':context}
		trg11(**kwargs)

	for record in records:
		oid = _modifyRecord(self, record, context)
		res.append(oid)

	trg2 = self._getTriger('au')
	for trg22 in trg2:
		kwargs = {'r1':records,'r2':records,'context':context}
		trg22(**kwargs)

	return res

def _modifyRecord(self, record, context):
	oid = None
	fields = list(record.keys())
	modelfields = list(self._columns.keys())
	nomodelfields = list(filter(lambda x: not x in modelfields and not x in MAGIC_COLUMNS, fields))
	if len(nomodelfields) > 0:
		raise orm_exception("Fields: %s not found in model: %s" % (nomodelfields, self.modelInfo()['name']))
	
	for nosavedfield in self._nosavedfields:
		if nosavedfield in record:
			del record[nosavedfield]
	columnsinfo = self.columnsInfo(columns = fields)
	o2mfields = list(filter(lambda x: x in fields, self._o2mfields))
	o2rfields = list(filter(lambda x: x in fields, self._o2rfields)) # o2related
	m2mfields = list(filter(lambda x: x in fields, self._m2mfields))

	emptyfields = list(filter(lambda x: x in fields and record[x] is None,self._requiredfields))		
	if len(emptyfields) > 0:
		raise orm_exception("Fields: %s of model: %s is required and not found in record: %s" % (emptyfields, self.modelInfo()['name'], record))

	o2mfieldsrecords = {}
	o2rfieldsrecords = {} # o2related
	m2mfieldsrecords = {}

	trg1 = self._getTriger('bur')
	record2 =None
	upd_cols = set()
	if trg1 and len(trg1) > 0:
		if 'id' in record and record['id']:
			ctx = context.copy()
			ctx['FETCH'] = 'RAW'
			record21 = self.read(record['id'], self._selectablefields, ctx)

			if len(record21) > 0:
				record2 = record21[0]

		if record2:
			k1 = set(list(record.keys()))
			k2 = set(list(record2.keys()))
			uk = list(set(k1).intersection(set(k2)))
			ik = list(set(k1)- set(k2))
			dk = list(set(k2)- set(k1))
			
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
				kwargs = {'r1':record,'r2':record2,'context':context}
				trg11(**kwargs)
		
	sql,vals = gensql.Modify(self, record, context)
	rowcount = self._execute(sql,vals)
	if rowcount > 0:
		oid = self._cr.fetchone()[0]

	if record2 is None or len(upd_cols) > 0:
		trg2 = self._getTriger('aur')
		for trg22 in trg2:
			kwargs = {'r1':record,'r2':record2,'context':context}
			trg22(**kwargs)

	return oid

def _unlinkRecord(self, record, context = {}):
	oid = None
	if not self._access._checkUnlink():
		orm_exception("Unlink:access dennied of model % s" % (self._name,))

	model_info = self.modelInfo(attributes=['type','rel','obj','id1','id2'])
	columns_info = model_info['columns']
	m2mfields = list(filter(lambda x: columns_info[x]['type'] == 'many2many',self._columns.keys()))
	for m2mfield in m2mfields:
		rel = columns_info[m2mfield]['rel']
		obj = columns_info[m2mfield]['obj']
		id1 = columns_info[m2mfield]['id1']
		id2 = columns_info[m2mfield]['id2']

		if not id2:
			id2 = _m2mfieldid2(self._pool,obj,rel)

		rels = []

	trg1 = self._getTriger('bdr')
	for trg11 in trg1:
		kwargs = {'r2':record,'context':context}
		trg11(**kwargs)

	sql,vals = gensql.Unlink(self,[record['id']],context)
	rowcount = self._execute(sql,vals)
	if rowcount > 0:
		oid = self._cr.fetchone()[0]

	trg2 = self._getTriger('adr')
	for trg22 in trg2:
		kwargs = {'r2':record,'context':context}
		trg22(**kwargs)

	return oid

def count(self, cond = None, context = {}):
	if not self._access._checkRead():
		orm_exception("Read:access dennied of model % s" % (self._name,))

	res = []
	if 'LANG' not in context:
		context['LANG'] = os.environ['LANG']
	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]
	if cond is None:
		cond = []

	if 'FETCH' not in context:
		context['FETCH'] = 'DICT'

	fetch = context['FETCH']

	if not fetch in ('LIST','DICT'):
		orm_exception('Invalid fetch mode: %s' % (fetch,))

	sql,vals = gensql.Count(self, cond, context)
	rowcount = self._execute(sql,vals)
	if rowcount > 0:
		if fetch == "LIST":
			res.extend(self._cr.fetchone(['count'], {'count':'integer'})) 
		elif fetch == "DICT":
			res.extend(self._cr.dictfetchone(['count'], {'count':'integer'})) 
	return res
	
#tested
def search(self, cond = None, context = {}, limit = None, offset = None):
	if not self._access._checkRead():
		orm_exception("Read:access dennied of model % s" % (self._name,))

	res = []

	if 'LANG' not in context:
		context['LANG'] = os.environ['LANG']

	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]

	if cond is None:
		cond = []

	if 'FETCH' not in context:
		context['FETCH'] = 'DICT'

	fetch = context['FETCH']

	if not fetch in ('LIST','DICT'):
		orm_exception('Invalid fetch mode: %s' % (fetch,))

	sql,vals = gensql.Search(self,cond, context, limit, offset)
	rowcount = self._execute(sql,vals)
	if rowcount > 0:
		if fetch == "LIST":
			res.extend(list(map(lambda x: x[0],self._cr.fetchall()))) 
		elif fetch == "DICT":
			res.extend(list(map(lambda x: x['id'],self._cr.dictfetchall()))) 
	return res

def _read(self, ids, fields = None, context = {}):

	res = []

	if 'LANG' not in context:
		context['LANG'] = os.environ['LANG']

	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]

	if 'FETCH' not in context:
		context['FETCH'] = 'DICT'

	fetch = context['FETCH']

	if not fetch.upper() in ('LIST','DICT','RAW'):
		orm_exception('Invalid fetch mode: %s' % (fetch.upper(),))

	if fields is None:
		fields = self._selectablefields

	rowfields = list(filter(lambda x: x in fields,self._rowfields)) 
	length = 1
	if type(ids) in (list,tuple):
		length = len(ids)		
	count = int(length/MAX_CHUNK_READ)
	chunk = int(length % MAX_CHUNK_READ)
	for i in range(count):
		j = i * MAX_CHUNK_READ
		chunk_ids = ids[j:j + MAX_CHUNK_READ]
		sql,vals = gensql.Read(self,chunk_ids,rowfields,context)
		rowcount = self._execute(sql,vals)
		if rowcount > 0:
			selectablefields = list(filter(lambda x: x in fields,self._selectablefields))
			nostorecomputefields = list(filter(lambda x: x in fields,self._nostorecomputefields))		
			records = self._cr.dictfetchall(selectablefields,self._columnsmeta)
			for record in records:
				o2mfields = {}
				m2mfields = {}
				fds = list(filter(lambda x: type(x) == dict,fields))
				dictfields = {}
				for fd in fds:
					dictfields.update(fd)

				recname = self._getRecNameName()
				if recname and recname in record:
					oid = record[recname]
				else:
					oid = record['id']

				for o2mfield in self._o2mfields:
					if o2mfield in dictfields:
						o2mfields[o2mfield] = dictfields[o2mfield]

				for m2mfield in self._m2mfields:
					if m2mfield in dictfields:
						m2mfields[m2mfield] = dictfields[m2mfield]

				for o2mfield in o2mfields:
					record[o2mfield] = _o2mread(self._pool[self._columns[o2mfield].obj],oid,self._columns[o2mfield].rel,o2mfields[o2mfield],context)
	
				for m2mfield in m2mfields:
					record[m2mfield] = _m2mread(self,record['id'],m2mfields[m2mfield],context)
			
			res.extend(records)

	if chunk > 0:
		if length == 1:
			chunk_ids = ids
		else:
			j = count * MAX_CHUNK_READ			
			chunk_ids = ids[j:]
		sql,vals = gensql.Read(self,chunk_ids,fields,context)
		rowcount = self._execute(sql,vals)
		if rowcount > 0:
			selectablefields = list(filter(lambda x: x in fields,self._selectablefields))
			nostorecomputefields = list(filter(lambda x: x in fields,self._nostorecomputefields))		
			records = self._cr.dictfetchall(selectablefields,self._columnsmeta)
			for record in records:
				o2mfields = {}
				m2mfields = {}
				fds = list(filter(lambda x: type(x) == dict,fields))
				dictfields = {}
				for fd in fds:
					dictfields.update(fd)

				recname = self._getRecNameName()
				if recname and recname in record:
					oid = record[recname]
				else:
					oid = record['id']

				for o2mfield in self._o2mfields:
					if o2mfield in dictfields:
						o2mfields[o2mfield] = dictfields[o2mfield]

				for m2mfield in self._m2mfields:
					if m2mfield in dictfields:
						m2mfields[m2mfield] = dictfields[m2mfield]

				for o2mfield in o2mfields:
					record[o2mfield] = _o2mread(self._pool[self._columns[o2mfield].obj],oid,self._columns[o2mfield].rel,o2mfields[o2mfield],context)
	
				for m2mfield in m2mfields:
					record[m2mfield] = _m2mread(self,record['id'],m2mfield,m2mfields[m2mfield],context)
			
			res.extend(records)
	
	return res
	
def read(self, ids, fields = None, context = {}):
	if not self._access._checkRead():
		orm_exception("Read:access dennied of model % s" % (self._name,))
	return _read(self, ids, fields, context)

def _select(self, fields = None ,cond = None, context = {}, limit = None, offset = None):

	res = []

	if 'LANG' not in context:
		context['LANG'] = os.environ['LANG']

	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]

	if 'FETCH' not in context:
		context['FETCH'] = 'DICT'

	fetch = context['FETCH']

	if not fetch.upper() in ('LIST','DICT','RAW'):
		orm_exception('Invalid fetch mode: %s' % (fetch.upper(),))

	if fields is None:
		fields = self._selectablefields

	rowfields = list(filter(lambda x: x in fields,self._rowfields)) 
	if cond is None:
		cond = []

	sql,vals = gensql.Select(self, rowfields, cond, context, limit, offset)

	rowcount = self._execute(sql,vals)
	if rowcount > 0:
		selectablefields = list(filter(lambda x: x in fields,self._selectablefields))
		nostorecomputefields = list(filter(lambda x: x in fields,self._nostorecomputefields))
		records = self._cr.dictfetchall(selectablefields,self._columnsmeta)
		for record in records:
			o2mfields = {}
			m2mfields = {}
			fds = list(filter(lambda x: type(x) == dict,fields))
			dictfields = {}
			for fd in fds:
				dictfields.update(fd)

			recname = self._getRecNameName()
			if recname and recname in record:
				oid = record[recname]
			else:
				oid = record['id']

			for o2mfield in self._o2mfields:
				if o2mfield in dictfields:
					o2mfields[o2mfield] = dictfields[o2mfield]

			for m2mfield in self._m2mfields:
				if m2mfield in dictfields:
					m2mfields[m2mfield] = dictfields[m2mfield]

			for o2mfield in o2mfields:
				record[o2mfield] = _o2mread(self._pool[self._columns[o2mfield].obj],oid,self._columns[o2mfield].rel,o2mfields[o2mfield],context)

			for m2mfield in m2mfields:
				record[m2mfield] = _m2mread(self._pool[self._columns[o2mfield].obj],oid,m2mfield,m2mfields[m2mfield],context)
		
		res.extend(records)

	return res

def select(self,fields = None ,cond = None, context = {}, limit = None, offset = None):
	if not self._access._checkSelect():
		orm_exception("Select:access dennied of model % s" % (self._name,))
	
	return _select(self,  fields, cond, context, limit, offset)

# Other start
def unlink(self, ids, context = {}):
	if not self._access._checkUnlink():
		orm_exception("Unlink:access dennied of model % s" % (self._name,))

	res = []
	if 'LANG' not in context:
		context['LANG'] = os.environ['LANG']
	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]
	if type(ids)  == str:
		ids = [ids]

	model_info = self.modelInfo(attributes=['type','rel','obj','id1','id2'])
	columns_info = model_info['columns']
	m2mfields = list(filter(lambda x: columns_info[x]['type'] == 'many2many',self._columns.keys()))
	for m2mfield in m2mfields:
		rel = columns_info[m2mfield]['rel']
		obj = columns_info[m2mfield]['obj']
		id1 = columns_info[m2mfield]['id1']
		id2 = columns_info[m2mfield]['id2']

		if not id2:
			id2 = _m2mfieldid2(self._pool,obj,rel)

		rels = []
		#for oid in ids:
			#_m2munlink(self,rel,id1,id2,oid,rels,context)

	trg1 = self._getTriger('bdr')
	for trg11 in trg1:
		kwargs = {'oid':ids,'context':context}
		trg11(**kwargs)

	trg2 = self._getTriger('bd')
	for trg22 in trg2:
		kwargs = {'oid':ids,'context':context}
		trg22(**kwargs)

	length = len(ids)
	count = int(length/MAX_CHUNK_DELETE)
	chunk = length % MAX_CHUNK_DELETE
	for i in range(count):
		j = i * MAX_CHUNK_DELETE
		chunk_ids = ids[j:j + MAX_CHUNK_DELETE]
		sql,vals = gensql.Unlink(self,chunk_ids,context)
		rowcount = self._execute(sql,vals)
		if rowcount > 0:
			res.extend(list(map(lambda x: x[0],self._cr.fetchall()))) 
	if chunk > 0:
		j = count * MAX_CHUNK_DELETE
		chunk_ids = ids[j:]
		sql,vals = gensql.Unlink(self,chunk_ids,context)
		rowcount = self._execute(sql,vals)
		if rowcount > 0:
			res.extend(list(map(lambda x: x[0],self._cr.fetchall()))) 


	trg3 = self._getTriger('adr')
	for trg33 in trg3:
		kwargs = {'oid':ids,'context':context}
		trg33(**kwargs)

	trg4 = self._getTriger('ad')
	for trg44 in trg4:
		kwargs = {'oid':ids,'context':context}
		trg44(**kwargs)

	return res

def delete(self, cond, context = {}):
	if not self._access._checkDelete():
		orm_exception("Delete:access dennied of model % s" % (self._name,))

	res = []
	oids = search(self, cond, context)
	if len(oids) > 0:
		res = unlink(self, oids, context)
	
	return res

def create(self, records, context = {}):
	if not self._access._checkCreate():
		orm_exception("Create:access dennied of model % s" % (self._name,))

	checks = _do_checks(self,  records, context)
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

	if 'LANG' not in context:
		context['LANG'] = os.environ['LANG']
	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]

	if type(records) in (list,tuple):
		return _createRecords(self, records, context)

	elif type(records) == dict:
		return [_createRecord(self, records, context)]

def write(self, records, context = {}):
	if not self._access._checkWrite():
		orm_exception("Write:access dennied of model % s" % (self._name,))

	checks = _do_checks(self, records, context)
	for ch in checks:
		for check in ch:
			for key in check.keys():
				if check[key] and type(check[key]) in (list,tuple) and len(check[key]) and check[key][0] in ('A','E','C'):  
					orm_exception("Create:Check errors of model %s\nChecks:%s" % (self._name,checks))

	if 'LANG' not in context:
		context['LANG'] = os.environ['LANG']
	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]

	if type(records) in (list,tuple):
		return _writeRecords(self, records,context)

	elif type(records) == dict:
		return [_writeRecord(self, records, context)]

def modify(self, records, context = {}):
	if not self._access._checkModify():
		orm_exception("Modify:access dennied of model % s" % (self._name,))

	checks = _do_checks(self, records, context)
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

	if 'LANG' not in context:
		context['LANG'] = os.environ['LANG']
	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]

	if type(records) in (list,tuple):
		return _modifyRecords(self, records, context)

	elif type(records) == dict:
		return [_modifyRecord(self, records, context)]
	
def update(self, record, cond = None,context = {}):
	if not self._access._checkUpdate():
		orm_exception("Update:access dennied of model % s" % (self._name,))

	res = []
	fields = list(record.keys())
	if 'LANG' not in context:
		context['LANG'] = os.environ['LANG']
	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]
	if cond is None:
		cond = []
	
	fields = list(record.keys())
	recs = search(self, cond, context)
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
		
	res = upsert(self,  _fields, values,context)
	return res

#testing
def insert(self, fields, values,context = {}):
	if not self._access._checkInsert():
		orm_exception("Insert:access dennied of model % s" % (self._name,))

	checks = _do_checks(self, _gen_records(fields,values), context)
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
			_computes = self._compute(storecomputefields,_gen_record(fields,value))
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
	if 'LANG' not in context:
		context['LANG'] = os.environ['LANG']
	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]

	trg1 = self._getTriger('bir')
	for trg11 in trg1:
		for value in values:
			kwargs = {'r1':_gen_record(fields,value),'context':context}
			trg11(**kwargs)


	trg2 = self._getTriger('bi')
	for trg22 in trg2:
		kwargs = {'r1':_gen_records(fields,values),'context':context}
		trg22(**kwargs)

	sql,vals = gensql.Insert(self, _fields, values, context)
	rowcount = self._execute(sql,vals)
	if rowcount > 0:
		res.extend(self._cr.fetchall()) 
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
							self._pool.get(obj).insert(_o2mfields, _o2mvalues,context)

			for m2mfield in m2mfields:
				columninfo = columnsinfo[m2mfield]
				obj = columninfo['obj']
				rel = self._getName(columninfo['rel'])
				rels = values[fm[key]]
				id1 = self._getName(columninfo['id1'])
				if columninfo['id2']:
					id2 = self._getName(columninfo['id2'])
				else:
					id2 = _m2mfieldid2(self._pool,obj,rel)
		
				oid = r[0]
				if len(rels) > 0:
					_m2mcreate(self,rel,id1,id2,oid,rels,context)


	trg3 = self._getTriger('air')
	for trg33 in trg3:
		for value in values:
			kwargs = {'r1':_gen_records(fields,values),'context':context}
			trg33(**kwargs)


	trg4 = self._getTriger('ai')
	for trg44 in trg4:
		kwargs = {'r1':_gen_records(fields,values),'context':context}
		trg44(**kwargs)

	return res

#testing
def upsert(self, fields, values,context = {}):
	if not self._access._checkUpsert():
		orm_exception("Upsert:access dennied of model % s" % (self._name,))

	checks = _do_checks(self, _gen_records(fields,values), context)
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
			_computes = self._compute(storecomputefields,_gen_record(fields,value))
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
	if 'LANG' not in context:
		context['LANG'] = os.environ['LANG']
	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]


	trg1 = self._getTriger('bir')
	for trg11 in trg1:
		for value in values:
			kwargs = {'r1':_gen_record(fields,value),'context':context}
			trg11(**kwargs)


	trg2 = self._getTriger('bi')
	for trg22 in trg2:
		kwargs = {'r1':_gen_records(fields,values),'context':context}
		trg22(**kwargs)

	sql,vals = gensql.Upsert(self, fields, values, context)
	rowcount = self._.execute(sql,vals)
	if rowcount > 0:
		res.extend(self._cr.fetchall()) 
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
							self._pool.get(obj).upsert(_o2mfields, _o2mvalues,context)

			for m2mfield in m2mfields:
				columninfo = columnsinfo[m2mfield]
				obj = columninfo['obj']
				rel = self._getName(columninfo['rel'])
				rels = values[fm[key]]
				id1 = self._getName(columninfo['id1'])
				if columninfo['id2']:
					id2 = self._getName(columninfo['id2'])
				else:
					id2 = _m2mfieldid2(self._pool,obj,rel)
		
				oid = r[0]
				_m2mmodify(self,rel,id1,id2,oid,rels,context)

	trg3 = self._getTriger('air')
	for trg33 in trg3:
		for value in values:
			kwargs = {'r1':_gen_record(fields,value),'context':context}
			trg33(**kwargs)


	trg4 = self._getTriger('ai')
	for trg44 in trg4:
		kwargs = {'r1':_gen_records(fields,values),'context':context}
		trg44(**kwargs)

	return res

def browse(self, ids, fields = None, context = {}):
	if not self._access._checkBrowse():
		orm_exception("Browse:access dennied of model % s" % (self._name,))

	brl = browse_record_list()
	
	for r in _read(self, ids, fields, context):
		brl.append(browse_record(self._uid,r))

	if len(brl) == 0:
		return browse_null()

	return brl

def selectbrowse(self, fields = None ,cond = None, context = {}, limit = None, offset = None):
	if not self._access._checkSelectBrowse():
		orm_exception("SelectBrowse:access dennied of model % s" % (self._name,))

	brl = browse_record_list()

	for r in _select(self, fields, cond, context, limit, offset):
		brl.append(browse_record(self._uid,r))

	if len(brl) == 0:
		return browse_null()

	return brl

# Other end

def _o2mread(self, oid, field,fields, context):
	res = []
	modelinfo = self.modelInfo()
	columnsinfo = self.columnsInfo()
	
	sql,vals = gensql.Select(self,fields, [(field,'=',oid)], context)
	rowcount = self._execute(sql,vals)
	if rowcount > 0:
		selectablefields = list(filter(lambda x: x in fields,self._selectablefields))
		nostorecomputefields = list(filter(lambda x: x in fields,self._nostorecomputefields))
		records = self._cr.dictfetchall(selectablefields,self._columnsmeta)
		for record in records:
			o2mfields = {}
			m2mfields = {}
			fds = list(filter(lambda x: type(x) == dict,fields))
			dictfields = {}
			for fd in fds:
				dictfields.update(fd)

			recname = self._getRecNameName()
			if recname and recname in record:
				oid = record[recname]
			else:
				oid = record['id']

			for o2mfield in self._o2mfields:
				if o2mfield in dictfields:
					o2mfields[o2mfield] = dictfields[o2mfield]

			for m2mfield in self._m2mfields:
				if m2mfield in dictfields:
					m2mfields[m2mfield] = dictfields[m2mfield]

			for o2mfield in o2mfields:
				record[o2mfield] = _o2mread(self._pool[self._columns[o2mfield].obj],oid,self._columns[o2mfield].rel,dictfields[o2mfield],context)

			for m2mfield in m2mfields:
				record[m2mfield] = _m2mread(self._pool[self._columns[o2mfield].obj],oid,m2mfield,dictfields[m2mfield],context)

		res.extend(records)
	
	return res

def _m2mread(self, oid, field, fields, context):
	res = []
	ids = []

	columnsinfo = self.columnsInfo()
	columninfo = columnsinfo[field]
	rel = columninfo['rel']
	obj = columninfo['obj']

	id1 = columninfo['id1']
	id2 = columninfo['id2']
	if not id2:
		id2 = self._m2mfieldid2(self._pool,obj,rel)
	rowcount = self._execute("SELECT id,%s,%s FROM %s WHERE %s = '%s'" % (id1,id2,rel,id1,oid))
	if rowcount > 0:
		if len(fields) > 0:
			ids.extend(list(map(lambda x: x[2],self._cr.fetchall([id1,id2], {id1:'uuid',id2:'uuid'})))) 
			if len(ids) > 0:
				res.extend(self._pool.get(obj).read(ids ,fields , context))
		else:
			res.extend(self._cr.fetchall([id1,id2], {id1:'uuid',id2:'uuid'})) 

	return res

def _m2mcreate(self,rel,id1,id2,oid,rels,context):
	res = []
	values = []

	if 'FETCH' not in context:
		context['FETCH'] = 'DICT'

	for r in rels:
		values.append((oid,r))
	sql = "insert into %s (%s,%s) values " % (rel,id1,id2)
	if len(values) == 1:
		sql += str(values[0])
	else:
		sql += reduce(lambda x,y: str(x) + ',' + str(y),values)
		
	sql += ' returning id'
	cr.execute(sql)
	if cr.cr.rowcount > 0:
		if context['FETCH'] == 'LIST':
			res.extend(list(map(lambda x: x[0],self._cr.fetchall()))) 
		elif context['FETCH'] == 'DICT':
			res.extend(list(map(lambda x: x['id'],self._cr.dictfetchall()))) 
	
	return res

def _m2mwrite(self,rel,id1,id2,oid,rels,context):
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

def _m2mmodify(self,rel,id1,id2,oid,rels,context):
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

def _m2munlink(self,rel,id1,id2,oid,rels,context):
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

def _tree(self, fields = None ,parent = None, context = {}):

	res = []

	if 'LANG' not in context:
		context['LANG'] = os.environ['LANG']

	if 'TZ' not in context:
		context['TZ'] = tm.tzname[1]

	if 'FETCH' not in context:
		context['FETCH'] = 'DICT'

	fetch = context['FETCH']

	if not fetch.upper() in ('LIST','DICT','RAW'):
		orm_exception('Invalid fetch mode: %s' % (fetch.upper(),))

	if parent is None:
		cond = [(self._getName('parent_id'),'?')]
	else:
		cond = [(self._getName('parent_id'),'=', parent)]

	sql,vals = gensql.Select(self,fields, cond, context,None,None)
	rowcount = self._execute(sql,vals)

	if rowcount > 0:
		res.extend(_fetch_results(self,fields,context))
		for r in res:
			r[self._getName('childs_id')].extend(_tree(self, fields, r[self._getName('rec_name')], context))

	return res

def tree(self, fields = None ,parent = None, context = {}):
	if not self._access._checkSelect():
		orm_exception("Tree:access dennied of model % s" % (self._name,))
	
	return _tree(self, fields, parent, context)


class DCacheList(list): pass

class DCacheDict(object):
	
	__doc__ ="""
	X c - current, o - old, p - primary values
		
	_Xdata dict(str(id(row|container)),row|container)
	_Xpaths dict(str(id(row)),str(id(<parent row>)))
	_Xr2c dict(str(id(row)), str(id(container)))
	_Xcontainers dict(str(id(container)),<container name>)
	_Xnames dict(<container name>,str(id(container)))
	_Xmetas dict(<model name>,meta)
	_Xmodels dict(str(id(row|<container name>)),<name model>)
	"""
	
	def __init__(self,data,model,cr,pool,uid,context,primary=True):
		self._value = data 
		self._model = model
		self._cr = cr
		self._pool = pool
		self._uid = uid
		self._context = context
		self._primary = primary

		for v in ('data','paths','r2c','containers','names','metas','models','rels','attrs'):
			for a in ('p','w','o','c'):
				if not primary and a == 'p':
					continue
				setattr(self,'_%s%s' % (a,v),{})

		self._buildTree(data,model)
		self._copyBuild()
		
	@property
	def _data(self):
		return self._value

	def _getCData(self,path):
		return ctypes.cast(int(self._cdata[path]), ctypes.py_object).value

	def _getAData(self,path):
		return ctypes.cast(int(path), ctypes.py_object).value

	def _clearTree(self,level='c'):
		for v in ('data','paths','r2c','containers','names','metas','models','rels','attrs'):
			getattr(self,'_%s%s' % (level,v)).clear()


	def _updateTree(self,data,model,level='c'):
		self._clearTree(level)
		self._buildTree(data,model,parent=None,name=None, mode = 'N',level=level)
	
	def _buildTree(self,data,model,parent=None,name=None, mode = 'N',level='c'):
		if type(data) != dict:
			raise TypeError

		oid = str(id(data))

		cmetas = getattr(self,'_%smetas' % (level,))
		cdata = getattr(self,'_%sdata' % (level,))
		cmodels = getattr(self,'_%smodels' % (level,))
		cpaths = getattr(self,'_%spaths' % (level,))
		cr2c = getattr(self,'_%sr2c' % (level,))
		ccontainers = getattr(self,'_%scontainers' % (level,))
		cnames = getattr(self,'_%snames' % (level,))

		if model not in cmetas:
			cmetas[model] = self._pool.get(model).columnsInfo(attributes=['type','obj','rel','id1','id2'])
		
		ci = cmetas[model]

		if mode == 'N' and not hasattr(self,'_root'):
			self._root = oid

		cdata[oid] = oid
		cmodels[oid] = model
		self._set_meta(oid)
		if parent and name:
			cpaths.setdefault(oid,{})[name] = parent
			cr2c[oid] = self._cnames[name + '.' + str(parent)]
			cdata[self._cnames[name + '.' + str(parent)]].append(oid)
		else:
			cpaths[oid] = None

		for m2mfield in filter(lambda x: x in data,self._pool.get(model)._m2mfields):
			if m2mfield in data: 
				self._m2m_buildTree(data[m2mfield],ci[m2mfield]['rel'],oid,m2mfield,model,level)
	
		for o2mfield in filter(lambda x: x in data ,self._pool.get(model)._o2mfields):
			cn = o2mfield + '.' + oid
			coid = str(id(data[o2mfield]))
			ccontainers[coid] = cn
			cnames[cn] = coid
			cdata[coid] = []
			cmodels[coid] = ci[o2mfield]['obj']

			if mode != 'I':
				for r1 in data[o2mfield]:
					self._buildTree(r1,ci[o2mfield]['obj'],oid,o2mfield,mode,level)

	def _m2m_buildTree(self,data,rel,parent,name,model,level):

		cmetas = getattr(self,'_%smetas' % (level,))
		cdata = getattr(self,'_%sdata' % (level,))
		cmodels = getattr(self,'_%smodels' % (level,))
		cpaths = getattr(self,'_%spaths' % (level,))
		cr2c = getattr(self,'_%sr2c' % (level,))
		ccontainers = getattr(self,'_%scontainers' % (level,))
		cnames = getattr(self,'_%snames' % (level,))
		crels = getattr(self,'_%srels' % (level,))

		if type(data) == dict:
			cn = name + '.' + parent
			coid = cnames[cn]
			
			m2moid = str(id(data))
			cdata[m2moid] = m2moid
			cdata.setdefault(coid,[]).append(m2moid)
			cmodels[m2moid] = model
			crels[m2moid] = rel
			cpaths.setdefault(m2moid,{})[name] = parent
			cr2c[m2moid] = cnames[cn]

		elif type(data) in (list,tuple):

			cn = name + '.' + parent
			coid = str(id(data))
			if coid not in cdata: 
				cdata[coid] = []
			ccontainers[coid] = cn
			cnames[cn] = coid
			crels[coid] = rel

			for r in data:
				m2moid = str(id(r))
				cdata[m2moid] = m2moid
				cdata[coid].append(m2moid)
				cmodels[m2moid] = model
				crels[m2moid] = rel
				cpaths.setdefault(m2moid,{})[name] = parent
				cr2c[m2moid] = cnames[cn]

	def _copyData(self,o,c):
		odata = getattr(self,'_%sdata' % (o,))
		cdata = getattr(self,'_%sdata' % (c,))
	
		for k in cdata.keys():
			if type(cdata[k]) == str:
				odata[k] = copy.deepcopy(self._getCData(cdata[k]))
			elif type(cdata[k]) == list:
				ka = cdata[k]
				odata[k] = []
				for k2 in ka:
					odata.setdefault(k,[]).append(copy.deepcopy(self._getCData(k2)))

	def _copyBuildLevel(self,o,c):
		opaths = getattr(self,'_%spaths' % (o,))
		or2c = getattr(self,'_%sr2c' % (o,))
		ocontainers = getattr(self,'_%scontainers' % (o,))
		onames = getattr(self,'_%snames' % (o,))
		ometas = getattr(self,'_%smetas' % (o,))
		omodels = getattr(self,'_%smodels' % (o,))
		orels = getattr(self,'_%srels' % (o,))
		oattrs = getattr(self,'_%sattrs' % (o,))

		cpaths = getattr(self,'_%spaths' % (c,))
		cr2c = getattr(self,'_%sr2c' % (c,))
		ccontainers = getattr(self,'_%scontainers' % (c,))
		cnames = getattr(self,'_%snames' % (c,))
		cmetas = getattr(self,'_%smetas' % (c,))
		cmodels = getattr(self,'_%smodels' % (c,))
		crels = getattr(self,'_%srels' % (c,))
		cattrs = getattr(self,'_%sattrs' % (c,))

		self._copyData(o,c)
		opaths.update(copy.deepcopy(cpaths))
		or2c.update(copy.deepcopy(cr2c))
		ocontainers.update(copy.deepcopy(ccontainers))
		onames.update(copy.deepcopy(cnames))
		ometas.update(copy.deepcopy(cmetas))
		omodels.update(copy.deepcopy(cmodels))
		orels.update(copy.deepcopy(crels))
		oattrs.update(copy.deepcopy(cattrs))

		
	def _copyBuild(self):
		self._copyBuildLevel('o','c')
		if self._primary:
			self._copyBuildLevel('p','c')

	def _diffs(self,o,c,commit):
		res = {}
		
		path = self._root
		self._updateTree(self._data,self._model)
		res.update(self._cmpDict(o,c,path))

		if commit:
			self._apply_from_diffs(o,c,res)

		return res

	def _apply_from_diffs(self,o,c,diffs):
		def _update(self,o,c,diffs):
			if ('__update__' in diffs ):
				for k in diffs['__update__'].keys():
					getattr(self,'_%sdata' % (o,))[k].update(copy.deepcopy(diffs['__update__'][k]))

		def _insert(self,o,c,diffs):
			if ('__insert__' in diffs ):
				for k in diffs['__insert__'].keys():
					getattr(self,'_%sdata' % (o,))[k].update(copy.deepcopy(diffs['__insert__'][k]))
	
		def _delete(self,o,c,diffs):
			if ('__delete__' in diffs ):
				for k in diffs['__delete__'].keys():
					for d in diffs['__delete__'][k].keys():
						del getattr(self,'_%sdata' % (c,))[k][d]

		def _meta_update(self,o,c,diffs):
			if ('__meta_update__' in diffs ):
				for k in diffs['__meta_update__'].keys():
					for k1 in diffs['__meta_update__'][k]:
						getattr(self,'_%sattrs' % (o,))[k][k1].update(copy.deepcopy(diffs['__meta_update__'][k][k1]))

		def _meta_insert(self,o,c,diffs):
			if ('__meta_insert__' in diffs ):
				for k in diffs['__meta_insert__'].keys():
					getattr(self,'_%sattrs' % (o,))[k].update(copy.deepcopy(diffs['__meta_insert__'][k]))

		def _meta_delete(self,o,c,diffs):
			if ('__meta_delete__' in diffs ):
				for k in diffs['__meta_delete__'].keys():
					del getattr(self,'_%sattrs' % (c,))[k]

		def _m2m_append(self,o,c,diffs):
			if ('__m2m_append__' in diffs ):
				for r in diffs['__m2m_append__']:
					container = r['__container__']
					path = r['__path__']
					model = r['__model__']
					cdata = getattr(self,'_%sdata' % (c,))
					odata = getattr(self,'_%sdata' % (o,))
					cnames = getattr(self,'_%snames' % (c,))
					onames = getattr(self,'_%snames' % (o,))
					ccontainers = getattr(self,'_%scontainers' % (c,))
					ocontainers = getattr(self,'_%scontainers' % (o,))
					
					cmetas = getattr(self,'_%smetas' % (c,))
					ometas = getattr(self,'_%smetas' % (o,))
					cmodels = getattr(self,'_%smodels' % (c,))
					omodels = getattr(self,'_%smodels' % (o,))
	
					crels = getattr(self,'_%srels' % (c,))
					orels = getattr(self,'_%srels' % (o,))
	
					cpaths = getattr(self,'_%spaths' % (c,))
					opaths = getattr(self,'_%spaths' % (o,))
					cr2c = getattr(self,'_%sr2c' % (c,))
					or2c = getattr(self,'_%sr2c' % (o,))
	
					cattrs = getattr(self,'_%sattrs' % (c,))
					oattrs = getattr(self,'_%sattrs' % (o,))
	
	
					r1 = copy.deepcopy(r['__data__'])
					odata.setdefault(cnames[container],[]).append(r1)
					odata[path] = r1
					if '__meta__' in r:
						oattrs[path] = r['__meta__']
					onames[container] = cnames[container]
					ocontainers[cnames[container]] = ccontainers[cnames[container]]
					orels[path] = crels[path]
					omodels[path] = cmodels[path] 
					opaths[path] = cpaths[path]
					or2c[path] = cr2c[path]
					
					if '__o2m_containers__' in r:
						for ck in r['__o2m_containers__'].keys():
							onames[ck + '.' + path] = cnames[ck + '.' + path]
							ocontainers[onames[ck + '.' + path]] = ccontainers[cnames[ck + '.' + path]]
							omodels[path] = cmodels[path]
							ometas[omodels[path]] = cmetas[cmodels[path]]
							or2c[path] = cr2c[path]
							opaths[path] = cpaths[path]
	
					if '__m2m_containers__' in r:
						for ck in r['__m2m_containers__'].keys():
							onames[ck + '.' + path] = cnames[ck + '.' + path]
							ocontainers[cnames[ck + '.' + path]] = ccontainers[cnames[ck + '.' + path]]
							omodels[path] = cmodels[path]
							orels[path] = crels[path]
							or2c[path] = cr2c[path]
							opaths[path] = cpaths[path]

		def _m2m_remove(self,o,c,diffs):
			if ('__m2m_remove__' in diffs ):
				for r in diffs['__m2m_remove__']:
					container = r['__container__']
					path = r['__path__']
					model = r['__model__']
					cdata = getattr(self,'_%sdata' % (c,))
					odata = getattr(self,'_%sdata' % (o,))
					cnames = getattr(self,'_%snames' % (c,))
					onames = getattr(self,'_%snames' % (o,))
					ccontainers = getattr(self,'_%scontainers' % (c,))
					ocontainers = getattr(self,'_%scontainers' % (o,))
					
					cmetas = getattr(self,'_%smetas' % (c,))
					ometas = getattr(self,'_%smetas' % (o,))
					cmodels = getattr(self,'_%smodels' % (c,))
					omodels = getattr(self,'_%smodels' % (o,))
	
					crels = getattr(self,'_%srels' % (c,))
					orels = getattr(self,'_%srels' % (o,))
	
					cpaths = getattr(self,'_%spaths' % (c,))
					opaths = getattr(self,'_%spaths' % (o,))
					cr2c = getattr(self,'_%sr2c' % (c,))
					or2c = getattr(self,'_%sr2c' % (o,))
	
					cattrs = getattr(self,'_%sattrs' % (c,))
					oattrs = getattr(self,'_%sattrs' % (o,))
				
	
					odata[onames[container]].remove(odata[path])
					del odata[path]
	
					if len(odata[onames[container]]) == 0:
						del odata[onames[container]]
						del ocontainers[onames[container]]
						del onames[container]
					
					del omodels[path] 				
					del opaths[path]					
					del or2c[path]

		def _o2m_append(self,o,c,diffs):
			if ('__o2m_append__' in diffs ):
				for r in diffs['__o2m_append__']:
					container = r['__container__']
					path = r['__path__']
					model = r['__model__']
					cdata = getattr(self,'_%sdata' % (c,))
					odata = getattr(self,'_%sdata' % (o,))
					cnames = getattr(self,'_%snames' % (c,))
					onames = getattr(self,'_%snames' % (o,))
					ccontainers = getattr(self,'_%scontainers' % (c,))
					ocontainers = getattr(self,'_%scontainers' % (o,))
					
					cmetas = getattr(self,'_%smetas' % (c,))
					ometas = getattr(self,'_%smetas' % (o,))
					cmodels = getattr(self,'_%smodels' % (c,))
					omodels = getattr(self,'_%smodels' % (o,))
	
					crels = getattr(self,'_%srels' % (c,))
					orels = getattr(self,'_%srels' % (o,))
	
					cpaths = getattr(self,'_%spaths' % (c,))
					opaths = getattr(self,'_%spaths' % (o,))
					cr2c = getattr(self,'_%sr2c' % (c,))
					or2c = getattr(self,'_%sr2c' % (o,))
	
					cattrs = getattr(self,'_%sattrs' % (c,))
					oattrs = getattr(self,'_%sattrs' % (o,))
	
	
					r1 = copy.deepcopy(r['__data__'])
					odata.setdefault(cnames[container],[]).append(r1)
					odata[path] = r1
					if '__meta__' in r:
						oattrs[path] = r['__meta__']
					onames[container] = cnames[container]
					ocontainers[cnames[container]] = ccontainers[cnames[container]]
					ometas[model] = cmetas[model]
					omodels[path] = cmodels[path] 
					opaths[path] = cpaths[path]
					or2c[path] = cr2c[path]

					if '__m2m_containers__' in r:
						for ck in r['__m2m_containers__'].keys():
							_apply_diffs(self,o,c,r['__m2m_containers__'][ck])
					
					if '__o2m_containers__' in r:
						for ck in r['__o2m_containers__'].keys():
							_apply_diffs(self,o,c,r['__o2m_containers__'][ck])
	
		def _o2m_remove(self,o,c,diffs):
			if ('__o2m_remove__' in diffs ):
				for r in diffs['__o2m_remove__']:
					container = r['__container__']
					path = r['__path__']
					model = r['__model__']
					cdata = getattr(self,'_%sdata' % (c,))
					odata = getattr(self,'_%sdata' % (o,))
					cnames = getattr(self,'_%snames' % (c,))
					onames = getattr(self,'_%snames' % (o,))
					ccontainers = getattr(self,'_%scontainers' % (c,))
					ocontainers = getattr(self,'_%scontainers' % (o,))
					
					cmetas = getattr(self,'_%smetas' % (c,))
					ometas = getattr(self,'_%smetas' % (o,))
					cmodels = getattr(self,'_%smodels' % (c,))
					omodels = getattr(self,'_%smodels' % (o,))
	
					crels = getattr(self,'_%srels' % (c,))
					orels = getattr(self,'_%srels' % (o,))
	
					cpaths = getattr(self,'_%spaths' % (c,))
					opaths = getattr(self,'_%spaths' % (o,))
					cr2c = getattr(self,'_%sr2c' % (c,))
					or2c = getattr(self,'_%sr2c' % (o,))
	
					cattrs = getattr(self,'_%sattrs' % (c,))
					oattrs = getattr(self,'_%sattrs' % (o,))
				
					if '__m2m_containers__' in r:
						for ck in r['__m2m_containers__'].keys():
							_apply_diffs(self,o,c,r['__m2m_containers__'][ck])
					
					if '__o2m_containers__' in r:
						for ck in r['__o2m_containers__'].keys():
							_apply_diffs(self,o,c,r['__o2m_containers__'][ck])
	
					odata[onames[container]].remove(odata[path])
					del odata[path]
	
					if len(odata[onames[container]]) == 0:
						del odata[onames[container]]
						del ocontainers[onames[container]]
						del onames[container]
					
					del omodels[path] 				
					del opaths[path]					
					del or2c[path]
					del oattrs[path]

		def _apply_diffs(self,o,c,diffs):
	
			_m2m_remove(self,o,c,diffs)
			_o2m_remove(self,o,c,diffs)
	
			_m2m_append(self,o,c,diffs)
			_o2m_append(self,o,c,diffs)

			_update(self,o,c,diffs)
			_insert(self,o,c,diffs)
			_delete(self,o,c,diffs)
	
			_meta_update(self,o,c,diffs)
			_meta_insert(self,o,c,diffs)
			_meta_delete(self,o,c,diffs)


		_apply_diffs(self,o,c,diffs)
			
		return True

	def _cmp_meta(self,o,c,path):
		diff = {}
		cattrs = getattr(self,'_%sattrs' % (c,))[path]
		oattrs = None
		if path in getattr(self,'_%sattrs' % (o,)):
			oattrs = getattr(self,'_%sattrs' % (o,))[path]
		for a in ('ro','rq','iv'):
			for k in cattrs[a].keys():
				if oattrs is None or cattrs[a][k] != oattrs[a][k]:
					diff.setdefault(a,{})[k] = cattrs[a][k]

		return diff

	def _cmpDict(self,o,c,path):
		res = {}
		odata = getattr(self,'_%sdata' % (o,))
		cdata = getattr(self,'_%sdata' % (c,))
		d1 = self._getCData(path)
		
		ci = self._cmetas[self._cmodels[path]]

		ck = list(filter(lambda x: x != 'id' and ci[x]['type'] not in ('many2many','one2many'),d1.keys()))
		ok = list(filter(lambda x: x != 'id' and ci[x]['type'] not in ('many2many','one2many'),odata[path].keys()))
		uk = list(set(ok).intersection(set(ck)))
		ik = list(set(ck)- set(ok))
		dk = list(set(ok)- set(ck))

		for k in filter(lambda x: x != 'id',d1.keys()):
			if ci[k]['type'] == 'one2many':
				v = self._o2m_cmpList(o,c,k + '.' + path)
				if '__o2m_append__' in v:			
					res.setdefault('__o2m_append__',[]).extend(v['__o2m_append__'])
				if '__o2m_remove__' in v:
					res.setdefault('__o2m_remove__',[]).extend(v['__o2m_remove__'])

				if '__o2m_meta_append__' in v:			
					res.setdefault('__o2m_meta_append__',[]).extend(v['__o2m_meta_append__'])
				if '__o2m_meta_remove__' in v:
					res.setdefault('__o2m_meta_remove__',[]).extend(v['__o2m_meta_remove__'])

				if '__update__' in v:
					res.setdefault('__update__',{}).update(v['__update__'])
				if '__insert__' in v:
					res.setdefault('__insert__',{}).update(v['__insert__'])
				if '__delete__' in v:
					res.setdefault('__delete__',{}).update(v['__delete__'])

			elif ci[k]['type'] == 'many2many':
				v = self._m2m_cmpList(o,c,k + '.' + path)
				if '__m2m_append__' in v:			
					res.setdefault('__m2m_append__',[]).extend(v['__m2m_append__'])
				if '__m2m_remove__' in v:
					res.setdefault('__m2m_remove__',[]).extend(v['__m2m_remove__'])
				if '__update__' in v:
					res.setdefault('__update__',{}).update(v['__update__'])
				if '__insert__' in v:
					res.setdefault('__insert__',{}).update(v['__insert__'])
				if '__delete__' in v:
					res.setdefault('__delete__',{}).update(v['__delete__'])

			else:
				if k in uk and d1[k] != getattr(self,'_%sdata' % (o,))[path][k]:
					if type(d1[k]) == memoryview:
						res.setdefault('__update__',{}).setdefault(path,{})[k] = d1[k].tobytes()
					else:
						res.setdefault('__update__',{}).setdefault(path,{})[k] = d1[k]
				elif k in ik:
					if type(self._getCData(getattr(self,'_%sdata' % (c,))[path])[k]) == memoryview:
						res.setdefault('__insert__',{}).setdefault(path,{})[k] = d1[k].tobytes()
					else:
						res.setdefault('__insert__',{}).setdefault(path,{})[k] = d1[k]
				elif k in dk:
					res.setdefault('__delete__',{}).setdefault(path,[]).append(k)

		diff = self._cmp_meta(o,c,path)
				 
		if len(diff) > 0:
			res.setdefault('__meta_update__',{}).setdefault(path,{}).update(diff)
	
		return res

	def _o2m_cmpList(self,o,c,container):
		res = {}

		cdata = getattr(self,'_%sdata' % (c,))
		odata = getattr(self,'_%sdata' % (o,))
		
		cnames = getattr(self,'_%snames' % (c,))
		onames = getattr(self,'_%snames' % (o,))

		cr2c = getattr(self,'_%sr2c' % (c,))
		or2c = getattr(self,'_%sr2c' % (o,))

		cmodels = getattr(self,'_%smodels' % (c,))
		omodels = getattr(self,'_%smodels' % (o,))
		
		ck = []
		ok = []
		
		if container in onames:
			ooid = onames[container]
			ok = list(filter(lambda x:or2c[x] == ooid,or2c.keys()))
		
		if container in cnames:
			coid = cnames[container]
			ck = list(filter(lambda x:cr2c[x] == coid,cr2c.keys()))

		uk = list(set(ok).intersection(set(ck)))
		ik = list(set(ck)- set(ok))
		dk = list(set(ok)- set(ck))
					
		for path in uk:
			v = self._cmpDict(o,c,path)
			if '__update__' in v:
				res.setdefault('__update__',{}).update(v['__update__'])
			if '__insert__' in v:
				res.setdefault('__insert__',{}).update(v['__insert__'])
			if '__delete__' in v:
				res.setdefault('__delete__',{}).update(v['__delete__'])
			if '__o2m_append__' in v:
				res.setdefault('__o2m_append__',[]).extend(v['__o2m_append__'])
			if '__o2m_remove__' in v:
				res.setdefault('__o2m_remove__',[]).extend(v['__o2m_remove__'])
			if '__o2m_meta_append__' in v:
				res.setdefault('__o2m_meta_append__',[]).extend(v['__o2m_meta_append__'])
			if '__o2m_meta_remove__' in v:
				res.setdefault('__o2m_meta_remove__',[]).extend(v['__o2m_meta_remove__'])
		for i in ik:
			p=container.split('.')
			model = cmodels[cnames[container]]
			
			coid = getattr(self,'_%sr2c' % (c,))[i]
			ci = getattr(self,'_%smetas' % (c,))[model]
			
			cattrs = getattr(self,'_%sattrs' % (c,))[i]
			
			m2m_containers = {}
			d1 = self._getCData(i)
			for k in filter(lambda x: x != 'id' and ci[x]['type'] == 'many2many',d1.keys()):
				r1 = self._m2m_cmpList(o,c,k + '.' + i)
				m2m_containers.setdefault(k,[]).extend(r1['__m2m_append__'] if '__m2m_append__' in r1 else [])

			data = {}

			for v in filter(lambda x: x != 'id' and ci[x]['type'] not in ('one2many','many2many'),d1.keys()):
				data[v] = d1[v]

			o2m_containers = {}
			for k in filter(lambda x: x != 'id' and ci[x]['type'] == 'one2many',d1.keys()):
				r1 = self._o2m_cmpList(o,c,k + '.' + i)
				o2m_containers.setdefault(k,[]).extend(r1['__o2m_append__'] if '__o2m_append__' in r1 else [])

				
			ir = {'__path__':i,'__container__':container,'__model__':model,'__data__':data,'__meta__':self._get_meta(i)}

			if len(m2m_containers) > 0:
				ir['__m2m_containers__'] = m2m_containers

			if len(o2m_containers) > 0:
				ir['__o2m_containers__'] = o2m_containers
			
			res.setdefault('__o2m_append__',[]).append(ir)
	
		for d in dk:
			model = omodels[onames[container]]
			remove_data = copy.deepcopy(odata[d])			

			ci = getattr(self,'_%smetas' % (o,))[model]

			m2m_containers = {}
			for k in filter(lambda x: x != 'id' and ci[x]['type'] == 'many2many',remove_data.keys()):
				r1 = self._m2m_cmpList(o,c,k + '.' + d)
				m2m_containers.setdefault(k,[]).extend(r1['__m2m_remove__'] if '__m2m_remove__' in r1 else [])
				
			o2m_containers = {}
			for k in filter(lambda x: x != 'id' and ci[x]['type'] == 'one2many',remove_data.keys()):
				r1 = self._o2m_cmpList(o,c,k + '.' + d)
				o2m_containers.setdefault(k,[]).extend(r1['__o2m_remove__'] if '__o2m_remove__' in r1 else [])
			
			dr = {'__path__':d,'__container__':container,'__model__':model,'__data__':remove_data}

			if len(m2m_containers) > 0:
				dr['__m2m_containers__'] = m2m_containers

			if len(o2m_containers) > 0:
				dr['__o2m_containers__'] = o2m_containers

			res.setdefault('__o2m_remove__',[]).append(dr)

		return res

	def _m2m_cmpList(self,o,c,container):
		res = {}

		cdata = getattr(self,'_%sdata' % (c,))
		odata = getattr(self,'_%sdata' % (o,))
		
		cnames = getattr(self,'_%snames' % (c,))
		onames = getattr(self,'_%snames' % (o,))

		cr2c = getattr(self,'_%sr2c' % (c,))
		or2c = getattr(self,'_%sr2c' % (o,))

		cmodels = getattr(self,'_%smodels' % (c,))
		omodels = getattr(self,'_%smodels' % (o,))
		
		crels = getattr(self,'_%srels' % (c,))
		orels = getattr(self,'_%srels' % (o,))

		ck = []
		ok = []
		
		if container in onames:
			ooid = onames[container]
			ok = list(filter(lambda x:or2c[x] == ooid,or2c.keys()))
		
		if container in cnames:
			coid = cnames[container]
			ck = list(filter(lambda x:cr2c[x] == coid,cr2c.keys()))

		ik = list(set(ck)- set(ok))
		dk = list(set(ok)- set(ck))
			
		for i in ik:
			d1 = self._getCData(i)

			model = cmodels[i]
			rel = crels[i]
				
			res.setdefault('__m2m_append__',[]).append({'__path__':i,'__container__':container,'__model__':model,'__rel__':rel,'__data__':d1})
	
		for d in dk:
			d1 = getattr(self,'_%sdata' % (o,))[d]
			model = omodels[d]
			rel = orels[d]			
			res.setdefault('__m2m_remove__',[]).append({'__path__':d,'__container__':container,'__model__':model,'__rel__':rel,'__data__':d1})
				
		return res

	def _removeRecursive(self,o,c,path):
		res = []

		cdata = getattr(self,'_%sdata' % (c,))
		cnames = getattr(self,'_%snames' % (c,))
		ccontainers = getattr(self,'_%scontainers' % (c,))	
		cmetas = getattr(self,'_%smetas' % (c,))
		cmodels = getattr(self,'_%smodels' % (c,))
		crels = getattr(self,'_%srels' % (c,))
		cpaths = getattr(self,'_%spaths' % (c,))
		cr2c = getattr(self,'_%sr2c' % (c,))
		cattrs = getattr(self,'_%sattrs' % (c,))

		model = cmodels[path]
		for o2mfield in self._pool.get(model)._o2mfields:
			container1 = o2mfield + '.' + str(path)
			coid = cnames[container1]
			paths1 = list(filter(lambda x: cr2c[x] == coid,cr2c.keys()))
			for path1 in paths1:
				res.extend(self._removeRecursive(o,c,path1))

		container = ccontainers[cr2c[path]]

		cdata[cnames[container]].remove(path)
		del cdata[path]
		del cattrs[path]

		if container in cnames and cnames[container] in cdata and len(cdata[cnames[container]]) == 0:
			del cdata[cnames[container]]
			del ccontainers[cnames[container]]
			del cnames[container]

		del cmodels[path] 
		del cpaths[path]
		del cr2c[path] 
		
		return res

	def _wdiffs(self,commit=True):
		return self._diffs('w','c',commit)
			
	def _odiffs(self,commit=True):
		return self._diffs('o','c',commit)

	def _pdiffs(self,commit=True):
		if self._primary:
			return self._diffs('p','c',commit)
		else:
			res = {'__create__':self._getData(self._root)}
			if commit:
				self._papply()
			
			return res

	def _wapply(self):
		return self._diffs('w','c',True)

	def _oapply(self):
		return self._diffs('o','c',True)

	def _papply(self):
		if self._primary:
			return self._diffs('p','c',True)
		else:
			return self._diffs('o','c',True)

	def _getData(self,path):
		model = self._cmodels[path]
		data = {}
		container = None
		m2m_container = None
		o2m_containers = {}
		m2m_containers = {}
		ci = self._cmetas[model]
		oid = None
		cdata = self._getCData(path)
		if 'id' in cdata:
			oid = cdata['id']
		for k in cdata.keys():
			if k != 'id' and ci[k]['type'] == 'one2many':
				o2m_containers[k] = self._get_o2mDataContainers(k + '.' + path)
			elif k != 'id' and ci[k]['type'] == 'many2many':	
				m2m_containers[k] = self._get_m2mDataContainers(model,k + '.' + path,oid)
			else:
				data[k] = cdata[k]

		if path in self._cr2c:
			container = self._ccontainers[self._cr2c[path]]
		
		res = {'__path__':path,'__data__':data,'__model__':model,'__meta__':self._get_meta(path)}
		if container:
			res['__container__'] = container
		
		if len(o2m_containers) > 0:
			res['__o2m_containers__'] = o2m_containers

		if len(m2m_containers) > 0:
			res['__m2m_containers__'] = m2m_containers


		return res

	def _get_o2mDataContainers(self,container):
		res = []

		if container in self._cnames:
			for r in self._cdata[self._cnames[container]]:
				res.append(self._getData(r))
			
		return res

	def _get_m2mDataContainers(self,model,container,oid):
		res = []
		
		for r in self._cdata[self._cnames[container]]:
			res.append({'__container__':container,'__path__':r,'__parent__':container.split('.')[1],'__model__':model,'__data__':self._getCData(r)})
			
		return res

	def _set_meta(self,path):
		ca = {'readonly':'ro','invisible':'iv','required':'rq','state':'st'}

		m = self._pool.get(self._cmodels[path])

		keys = list(m._columns.keys())
		for a in ('ro','rq','iv'):
			for k in keys:
				self._cattrs.setdefault(path,{}).setdefault(a,{})[k] = False

		if type(m._attrs) == dict:
			if len(m._attrs) > 0:
				self._cattrs.setdefault(path,{}).update(m._attrs)
		elif type(m._attrs) == str:
			method = getattr(m,m._attrs,None)
			if method and callable(method):
				rc = method(self._getCData(path),self._context)
				if rc and len(rc) > 0:
					self._cattrs.setdefault(path,{}).update(rc)

		cm = {}
		for a in ('readonly','invisible','required','state'):
			for c in m._columns.keys():
				if m._columns[c]._type =='referenced':
					continue
				
				if a in ('readonly',) and hasattr(m._columns[c],'compute') and m._columns[c].compute:
					self._cattrs.setdefault(path,{}).setdefault(ca[a],{})[c] = True
					continue
				
				aa = getattr(m._columns[c],a,None)
				if type(aa) == bool:
					self._cattrs.setdefault(path,{}).setdefault(ca[a],{})[c] = aa
				elif type(aa) == str:
					cm.setdefault(a,{}).setdefault(aa,set()).add(c)
				elif type(aa) == dict:
					if a == 'state':
						for s in aa.keys():
							sn = m._getStateName()
							if sn and s == self._getCData(path)[sn]:
								if type(aa[s]) == dict:
									for s1 in aa[s].keys():
										if aa[s][s1]:
											if type(aa[s][s1]) == bool:
												self._cattrs.setdefault(path,{}).setdefault(ca[a],{}).setdefault(s1,{})[c] = aa[s][s1]
											else:
												self._cattrs.setdefault(s,set()).add(aa[s][s1])
								elif type(aa[s]) == str:
									cm.setdefault(a,{}).setdefault(aa,set()).add(c)

		for k in cm.keys():
			for k1 in cm[k].keys():
				method = getattr(m,k1,None)
				if method and callable(method):
					rc = method(cm[k][k1],self._getCData(path),self._context)
					if type(rc) == dict and len(rc)> 0:
						self._cattrs.setdefault(path,{}).setdefault(ca[k],{}).update(rc)
					elif type(rc) == bool:
						for f in cm[k][k1]:
							self._cattrs.setdefault(path,{}).setdefault(ca[k],{})[f] = rc 

		if 'st' in self._cattrs[path]:
			st = self._cattrs[path]['st']
			for k1a in st.keys():
				for k1c in st[k1a].keys():
					self._cattrs.setdefault(path,{}).setdefault(k1a,{})[k1c] = st[k1a][k1c]
			
			del self._cattrs[path]['st']
			
	def _get_meta(self,path):
		return self._cattrs[path]
	
class MCache(object):
	
	def __init__(self,cr,pool,uid,mode,context):
		self._cr = cr
		self._pool = pool
		self._uid = uid
		self._context = context
		self._mode = mode
		self._m = {}
		self._checks = {}

		self._meta = {}
		self._cache_attrs = {}
		self._diffs = {}
		self._commit_diffs = {}

	def _getMode(self):
		return [self._mode]

	def _setMode(self,mode):
		self._mode = mode
		return [self._mode == mode]

	def _getContext(self):
		return [self._context]

	def _setContext(self,context):
		self._context = context
		return [self._context == context]

	def _initialize(self,model,view='form',context={}):
		self._clear()
		self._model = model
		row = self._pool.get(model)._buildEmptyItem()
		self._data = DCacheDict(row,model,self._cr,self._pool,self._uid,self._context,False)
		
		self._setDefault(model,row)
		self._post_diffs(context)
		#self._do_calculate(self._data._root,context=context)
		self._getMeta()	
		m = self._data._getData(self._data._root)
		m['__checks__'] = []
		return m

	def _readNodes(self,model,row):
		schema = self._pool.get(model)._schema1
		q = []
		for k in schema[0].keys():
			parent = schema[0][k]
			m = self._pool.get(parent)
			oid = row[k]['id']
			if oid:
				d = m.select([m._m2ofields],[('id','=',oid)],self._context,limit=1)
				if len(d) > 0:
					q.extend(self._readNodes(parent,d[0]))
			else:
				q.append((row['id'],model))
		
		return q

	def _readSchema(self,model,row):
		res = {}
		nodes = self._readNodes(model,row)
		for oid,model in nodes:
			m = self._pool.get(model)
			cols = m._buildSchemaColumns(self._pool)
			d = m.read(oid,cols,self._context)
			res[model] = d
		
		return res

#model method
	def _read(self,model,ids,fields=None,context={}):
		row = read(model,ids,fields,context)
		if len(row) > 0:
			if  'read' in context and context['read'] == 'raw' or 'cache' not in context:
				return row
			else:
				self._data = DCacheDict(row[0],model._name,model._cr,model._pool,model._uid,self._context)
				self._getMeta()
				m = self._data._getData(self._data._root)
				m['__checks__'] = []
				return [m]
		else:
			return row

	def _write(self,model,records,context={}):
		res = []
		if type(records) == dict:
			self._data = DCacheDict(records,model._name,model._cr,model._pool,model._uid,self._context,False)
			self._do_calculate_all(context)
			res.append(self._save()[1])
		elif  type(records) in (list,tuple):
			res = []
			for record in records:
				self._data = DCacheDict(record,model._name,model._cr,model._pool,model._uid,self._context,False)
				self._do_calculate_all(context)
				res.append(self._save()[1])
		
		return res

	def _modify(self,model,records,context={}):
		res = []
		if type(records) == dict:
			self._data = DCacheDict(records,model._name,model._cr,model._pool,model._uid,self._context,False)
			self._do_calculate_all(context)
			res.append(self._save()[1])
		elif  type(records) in (list,tuple):
			res = []
			for record in records:
				self._data = DCacheDict(record,model._name,model._cr,model._pool,model._uid,self._context,False)
				self._do_calculate_all(context)
				res.append(self._save()[1])
		
		return res

	def _create(self,model,records,context={}):
		res = []
		if type(records) == dict:
			self._data = DCacheDict(records,model._name,model._cr,model._pool,model._uid,self._context,False)
			self._do_calculate_all(context)
			res.append(self._save()[1])
		elif  type(records) in (list,tuple):
			res = []
			for record in records:
				self._data = DCacheDict(record,model._name,model._cr,model._pool,model._uid,self._context,False)
				self._do_calculate_all(context)
				res.append(self._save()[1])
		
		#self._commit()
		return res

	def _unlink(self,model,ids,context={}):
		return unlink(model,ids,context)

	def _select(self,model,fields = None ,cond = None, context = {}, limit = None, offset = None):
		return select(model,fields, cond, context, limit, offset)

	def _update(self,model,record, cond = None,context = {}):
		return update(model,record,cond,context)

	def _upsert(self,model,fields, values,context = {}):
		return upsert(model,fields, values,context )

	def _insert(self,model,fields, values,context = {}):
		return insert(model,fields, values,context )

	def _delete(self,model,cond,context = {}):
		return delete(model,cond,context )

	def _count(self,model,cond = None, context = {}):
			return count(model,cond, context)

	def _search(self,model, cond = None, context = {}, limit = None, offset = None):
		return search(model,cond, context, limit, offset)

	def _tree(self,model,fields = None ,parent = None, context = {}):
		return tree(model,fields,parent, context)

	def _browse(self,model,ids,fields=None,context={}):
			return browse(model,ids,fields,context)

	def _selectbrowse(self,model, fields = None ,cond = None, context = {}, limit = None, offset = None):
			return selectbrowse(model,fields,cond,context,limit,offset)

	def _o2mread(self, oid, field,fields, context):
		return _o2mread(self, oid, field,fields, context)

	def _m2mread(self, oid, field, fields, context):
		return _m2mread(self, oid, field, fields, context)
	
	def _m2mcreate(self,rel,id1,id2,oid,rels,context):
		return _m2mcreate(self,rel,id1,id2,oid,rels,context)
	
	def _m2mwrite(self,rel,id1,id2,oid,rels,context):
		return  _m2mwrite(self,rel,id1,id2,oid,rels,context)
	
	def _m2mmodify(self,rel,id1,id2,oid,rels,context):
		return _m2mmodify(self,rel,id1,id2,oid,rels,context)
	
	def _m2munlink(self,rel,id1,id2,oid,rels,context):
		return _m2munlink(self,rel,id1,id2,oid,rels,context)

# model method

	def _getMeta(self,models = None):
		if models is None:
			models = list(self._data._cmodels.values())
		elif type(models) == str:
			models = [models]
		for model in models:
			if not model in self._meta:
				self._meta[model] = self._pool.get(model).columnsInfo(attributes=['type','obj','rel','readonly','invisible','required','state','on_change','on_check'])

			if not model in self._cache_attrs:
				self._cache_attrs[model] = {'iscaching': len(self._pool.get(model)._computefields) > 0,'computefields': self._pool.get(model)._computefields,'changefields': self._pool.get(model)._on_change_fields,'checkfields': self._pool.get(model)._on_check_fields}

	def _clear(self):
		self._m.clear()
		return True

	def _on_change(self,path,model,key,context):
		if model not in self._meta:
			self._getMeta(model)
		k1 = key
		if type(key) in (list,tuple):
			k1 = key[-1]
		name = self._meta[model][k1]['on_change']
		if name:
			method = getattr(self._pool.get(model),name,None)
			if method:
				r1 = copy.deepcopy(self._data._getCData(path))
				_on_change = method(self._data._getCData(path),context)
				if _on_change:
					self._data._getCData(path).update(_on_change)
				r2 = self._data._getCData(path)
				for k in filter(lambda x: x != k1 and x not in key,self._pool.get(model)._on_change_fields):
					if r2[k] != r1[k]:
						if  type(key) in (list,tuple):
							key.append(k)
						else:
							key = [key,k]
						self._on_change(path,model,key,context)

	def _on_check(self,path,model,key,context):
		name = self._meta[model][key]['on_check']
		if name:
			method = getattr(self._pool.get(model),name,None)
			if method:
				self._checks.setdefault(path,{})[key] = method(key,self._data._getCData(path),context)
	
	def _do_diff(self,path,key,value,context):
		res = {}

		cdata = self._data._getCData(path)
		if key not in cdata or cdata[key] != value:
			cdata[key] = value
			model = self._data._cmodels[path]

			if model not in self._meta:
				self._getMeta(model)

			if key in self._cache_attrs[model]['checkfields'] and self._cache_attrs[model]['checkfields'][key]:
				self._on_check(path,model,key,context)

			if key not in self._checks or key in self._checks and self._checks[key]:
				self._on_change(path,model,key,context)
		
			if key not in self._checks or key in self._checks and self._checks[key]:
				self._do_calculate(path,context)

			self._data._set_meta(path)
		return res

	def _do_meta(self,path):
		res = {}
		res[path] = self._data._get_meta(path)
		while True:
			if self._data._cpaths[path]:
				parents = self._data._cpaths[path]
				for key in parents.keys():
					path = parents[key]
					res[path] = self._data._get_meta(path)
			else:
				break

		return res

	def _do_compute(self, path, model):
		res = {}
		m = self._pool.get(model)
		record = self._data._getCData(path)
		fields = list(record.keys())
		ci = m.columnsInfo(columns=m._computefields,attributes=['compute','priority'])
		priority = {}
		#for compute_field in filter(lambda x: x in fields,m._computefields):
		for compute_field in m._computefields:
			priority.setdefault(ci[compute_field]['priority'],set()).add(ci[compute_field]['compute'])
		
		pkeys = list(priority.keys())
		pkeys.sort()
		for pkey in pkeys:
			for compute_method in priority[pkey]:			
				method = getattr(m,compute_method,None)
				if method and callable(method):
					r = method(record,self._context)
					if r is not None: 
						res.update(r)
	
		return res

	def _do_calculate(self,path,context):
		model = self._data._cmodels[path]
		_computes = self._do_compute(path,model)
		
		if len(_computes) > 0:
			self._data._getCData(path).update(_computes)
		
		parents = self._data._cpaths[path]
		if parents:
			for key in parents.keys():
				parent = parents[key]
				self._do_calculate(parent,context)

	def _do_calculate_all(self,context):
		def _calculate_from_array(vpaths,context):
			for vpath in vpaths:
				if type(vpath) in (list,tuple):
					_calculate_from_array(vpath,context)
				else:
					self._do_compute(vpath,self._data._cmodels[vpath])
		vpaths = []
		for k in filter(lambda x: self._data._cpaths[x] is None,self._data._cpaths.keys()):
			vpaths.append(k)
			childs = self._calculate_paths(k,context)
			if len(childs) > 0:
				vpaths.append(childs)

		for vpath in reversed(vpaths):
			if type(vpath) in (list,tuple):
				_calculate_from_array(vpath,context)
			else:
				self._do_compute(vpath,self._data._cmodels[vpath])
				
			
	def _calculate_paths(self,parent,context):
		vpaths = []
		for k in list(filter(lambda x: not self._data._cpaths[x] is None , self._data._cpaths.keys())):
			for k1 in self._data._cpaths[k].keys():
				if self._data._cpaths[k][k1] == parent:
					vpaths.append(k)
					childs = self._calculate_paths(k,context)
					if len(childs) > 0:
						vpaths.append(childs)

		return vpaths


	def _setDefault(self,model,item):
		m = self._pool.get(model)
		_default = m._default
		if model not in self._meta:
			self._getMeta([model])
		m1 = self._meta[model]
		for k in _default.keys():
			if k in item:
				if m1[k]['type'] in ('numeric','decimal'):
					item[k] = Decimal(_default[k])
				elif m1[k]['type'] in ('many2one','related'):
					item[k]['name'] = _default[k]
					oids = self._pool.get(m1[k]['obj']).search([(self._pool.get(m1[k]['obj'])._getRecNameName(),'=',_default[k])],self._context)
					if len(oids) > 0:
						item[k]['id'] = oids[0] 
				else:
					item[k] = _default[k]	
	
	def _o2m_add(self,model,container,context,view='form'):
		row = self._pool.get(model)._buildEmptyItem()
		self._setDefault(model,row)
		
		hook = self._pool.get(model)._getHook('Before_o2m_Add')
		if hook:
			hook(row,context)
		p = container.split('.')
		path = p[1]
		self._data._getAData(self._data._cnames[container]).append(row)
		self._data._buildTree(row,model,p[1],p[0],'A')
		
		self._do_calculate(str(id(row)),context)

		hook = self._pool.get(model)._getHook('After_o2m_Add')
		if hook:
			hook(row,context)
		
		res = {}

		data_diffs = self._data._odiffs(True)
		
		if len(data_diffs) > 0:
			res['__data__'] = data_diffs
		
		if len(self._checks) > 0:
			res['__checks__'] = copy.deepcopy(self._checks)
			self._checks.clear()

		if len(res) > 0:
			return [res]
		
		return []
			
	def _o2m_remove(self,path,container,context):
		c = container.split('.')
		model = self._data._cmodels[path]
		row = self._data._getCData(path)
		hook = self._pool.get(model)._getHook('Before_o2m_Remove')
		if hook:
			hook(row,context)
		
		self._data._getAData(self._data._cnames[container]).remove(row)
		self._data._removeRecursive('o','c',path)
		
		self._do_calculate(c[1],context)
		
		hook = self._pool.get(model)._getHook('Afftre_o2m_Remove')
		if hook:
			hook(row,context)
		
		res = {}

		data_diffs = self._data._odiffs(True)

		if len(data_diffs) > 0:
			res['__data__'] = data_diffs

		if len(self._checks) > 0:
			res['__checks__'] = copy.deepcopy(self._checks)
			self._checks.clear()
		
		if len(res) > 0:
			return [res]
		
		return []

	def _o2m_removes(self,rows,context):
		for row in rows:
			path = row['path']
			container = row['container']
			c = container.split('.')
			self._data._getAData(self._data._cnames[container]).remove(self._data._getCData(path))		
			self._data._removeRecursive('o','c',path)
			self._do_calculate(c[1],context)

		res = {}

		data_diffs = self._data._odiffs(True)

		if len(data_diffs) > 0:
			res['__data__'] = data_diffs
		
		if len(self._checks) > 0:
			res['__checks__'] = copy.deepcopy(self._checks)
			self._checks.clear()

		if len(res) > 0:
			return [res]
		
		return []

	def _m2m_add(self,model,container,fields,obj,rel,id2,context={}):
		
		rows = self._pool.get(obj).read(id2,fields,self._context)
		
		cn,parent = container.split('.')
		if len(rows) > 0:
			for row in rows:
				self._data._getAData(parent)[cn].append(row)
				self._data._m2m_buildTree(row,rel,parent,cn,model,'c')
				
		res = {}

		data_diffs = self._data._odiffs(True)
		
		if len(data_diffs) > 0:
			res['__data__'] = data_diffs
		
		if len(self._checks) > 0:
			res['__checks__'] = copy.deepcopy(self._checks)
			self._checks.clear()

		if len(res) > 0:
			return [res]
		
		return []

	def _m2m_remove(self,path,container,context):
		cn,parent = container.split('.')
		self._data._getAData(self._data._cnames[container]).remove(self._data._getCData(path))

		res = {}

		data_diffs = self._data._odiffs(True)

		if len(data_diffs) > 0:
			res['__data__'] = data_diffs

		if len(res) > 0:
			return [res]
		
		return []

	def _m2m_removes(self,rows,context):
		for row in rows:
			path = row['path']
			container = row['container']
			c = container.split('.')
			self._data._getAData(self._data._cnames[container]).remove(self._data._getCData(path))		

		res = {}

		data_diffs = self._data._odiffs(True)

		if len(data_diffs) > 0:
			res['__data__'] = data_diffs
		
		if len(self._checks) > 0:
			res['__checks__'] = copy.deepcopy(self._checks)
			self._checks.clear()

		if len(res) > 0:
			return [res]
		
		return []
	
	def _m2o_find(self,path,model,key,value,context):
		rec_name = self._pool.get(self._meta[model][key]['obj'])._getRecNameName()
		if rec_name:
			fields = [rec_name]
			cond = [(rec_name,'like',value['name'] if type(value) == dict else value)]
		else:
			fields = [key]
			cond = []

			if value['id']:
				cond.append((key,'like',value['id']))

		r = self._pool.get(self._meta[model][key]['obj']).select(fields,cond=cond,context=context)
		
		if len(r) > 1:
			res = {'path':path,'key':key,'v':list(map(lambda x: x['id'],r))}
		elif len(r) == 1:
			res = {'path':path,'key':key,'v':r}
		elif len(r) == 0:
			res = {'path':path,'key':key,'v':[]}
		
		return [{'__m2o_find__':{'__data__':res}}]

	def _related_find(self,path,model,key,value,relatedy,context):
		rec_name = self._pool.get(self._meta[model][key]['obj'])._getRecNameName()
		if rec_name:
			fields = [rec_name]
			cond = [(rec_name,'like',value['name'] if type(value) == dict else value)]
		else:
			fields = [key]
			cond = []
			if value['id']:
				cond.append((key,'like',value['id']))

		for rel in relatedy:
			d = self._data._getCData(path)[rel]
			if type(d) == dict:
				r1 = d['name']
			else:
				r1 = d
			cond.append((rel,'=',r1))

		r = self._pool.get(self._meta[model][key]['obj']).select(fields,cond=cond,context=context)
		if len(r) > 1:
			res = {'path':path,'key':key,'v':list(map(lambda x: x['id'],r))}
		elif len(r) == 1:
			res = {'path':path,'key':key,'v':r}
		elif len(r) == 0:
			res = {'path':path,'key':key,'v':[]}
		
		return [{'__related_find__':{'__data__':res}}]

	def _action(self,path,name,column = None,context={}):
		res = {}
		act = self._pool.get(self._data._cmodels[path]).do_action(self._cr,self._pool,self._uid,name,column,self._data._getCData(path),context)
		if act and len(act) > 0:
			res['__do_action__'] = act
		else:
			res['__do_action__'] = []

		self._diffs = self._post_diffs(context)
		
		if len(self._diffs) > 0:
			res['__data__'] = copy.deepcopy(self._diffs)
			self._diffs.clear()

		if len(self._checks) > 0:
			res['__checks__'] = copy.deepcopy(self._checks)
			self._checks.clear()
		
		if len(res) > 0:
			return [res]
		
		return []

	def _is_change(self,autocommit = False):
		return len(self._data._pdiffs(False)) > 0

	def _do_copy(self,autocommit = False):
		data = self._data._getData(self._data._root)
		self._copyItem(data)
		return ['commit',data['__data__']['id']]

	def _save_one(self,data):
		diffs = data._pdiffs(False)
		if len(diffs) == 0:
			return 'no chache'
		
		if '__create__' in diffs:
			self._createItem(diffs['__create__'])
			if 'id' in diffs['__create__']['__data__'] and diffs['__create__']['__data__']['id']:
				return diffs['__create__']['__data__']['id']

		else:
			for k in diffs.keys():
				if k == '__update__':
					self._updateItems(diffs['__update__'])
				elif k == '__insert__':
					self._updateItems(diffs['__insert__'])
				elif k == '__delete__':
					self._updateItems(diffs['__delete__'])
				elif k == '__o2m_append__':
					self._o2m_appendItems(diffs['__o2m_append__'])
				elif k == '__o2m_remove__':
					self._o2m_removeItems(diffs['__o2m_remove__'])
				elif k == '__m2m_append__':
					self._m2m_appendRows(diffs['__m2m_append__'])
				elif k == '__m2m_remove__':
					self._m2m_removeRows(diffs['__m2m_remove__'])
		
			if type(self._commit_diffs) == dict:
				self._commit_diffs = diffs
			elif type(self._commit_diffs) == list:	
				self._commit_diffs.append(diffs)

	def _save_many(self,data,autocommit):
		pass

	def _save_all(self,datas):
		res = []

		for data in datas:
			res.append(self._save_one(data))
		
		return res

	def _save_commit_one(self,data,diffs):
		return data._apply_from_diffs('p','c',diffs)

	def _save_commit_many(self,data,diffs):
		pass

	def _save_commit_all(self,datas,diffs):
		for data,diff in zip(datas,diffs):
			self._save_commit_one(data,diff)

		return ['commited']

	def _save_commit(self,datas,diffs):
		if type(self._commit_diffs) == dict:
			rc = self._save_commit_one(datas,diffs)
			self._commit_diffs = {}
		elif type(self._commit_diffs) == list:	
			self._save_commit_all(datas,diffs)
			self._commit_diffs = []

		return ['commited']

	def _save(self,autocommit = False):
		res = []
		if type(self._data) == DCacheDict:
			self._commit_diffs = {}
			v = self._save_one(self._data)
			if v == 'no chache':
				res.append(v)
			else:
				res.extend(['commit',v])
			if autocommit:
				self._commit()

		elif type(self._data) == DCacheList:
			self._commit_diffs = []
			res.extend(self._save_all(self._data))
			if autocommit:
				self._commit()
		
		return res

	def _copyItems(self,items,rel=None,oid = None):
		if len(items) > 0:
			m = self._pool.get(items[0]['__model__'])
			trg1 = m._getTriger('bi')
			for trg11 in trg1:
				kwargs = {'r1':items,'context':self._context}
				trg11(**kwargs)
	
			for item in items:
				self._copyItem(item,rel,oid)
	
			trg2 = m._getTriger('ai')
			for trg22 in trg2:
				kwargs = {'r1':items,'context':self._context}
				trg22(**kwargs)

	def _copyItem(self,item,rel = None, oid = None):
		if rel and oid:
			item['__data__'][rel]['id'] = oid
		data = {}
		model = item ['__model__']
		m = self._pool.get(model)
		excl_fields = m._o2mfields + m._m2mfields + ['id']
		for k in filter(lambda x: x not in excl_fields,item['__data__'].keys()):
			if k in m._columns and m._columns[k]._type in ('many2one','related'):
				#if rel and k != rel or not rel:
				data[k] = item['__data__'][k]['id']
			elif k in m._columns and m._columns[k]._type == 'json':
				data[k] = json.dumps(item['__data__'][k])
			else:
				data[k] = item['__data__'][k]

		if 'id' in data:
			r = _modifyRecord(m,data,self._context)
		else:
			r = _createRecord(m,data,self._context)

		if r:
			item['__data__']['id'] = r
			path = item['__path__']
			self._data._getCData(path)['id'] = r
			self._data._odata[path]['id'] = copy.deepcopy(r)
			if self._data._primary and path in self._data._pdata:
				self._data._pdata[path]['id'] = copy.deepcopy(r)

			if '__m2m_containers__' in item:
				m2m_containers = item['__m2m_containers__']
				for key in m2m_containers.keys():
					self._m2m_appendRows(m2m_containers[key])
	
			if '__o2m_containers__' in item and not (m._ParentIdName and m._ChildsIdName):
				o2m_containers = item['__o2m_containers__']
				for key in o2m_containers.keys():
					self._copyItems(o2m_containers[key],self._pool.get(model)._columns[key].rel,item['__data__']['id'])

	def _createItems(self,items,rel=None,oid = None):
		if len(items) > 0:
			m = self._pool.get(items[0]['__model__'])
			trg1 = m._getTriger('bi')
			for trg11 in trg1:
				kwargs = {'cr':self._cr,'pool':self._pool,'uid':self._uid,'r1':items,'context':self._context}
				trg11(**kwargs)
	
			for item in items:
				self._createItem(item,rel,oid)
	
			trg2 = m._getTriger('ai')
			for trg22 in trg2:
				kwargs = {'cr':self._cr,'pool':self._pool,'uid':self._uid,'r1':items,'context':self._context}
				trg22(**kwargs)

	def _createItem(self,item,rel = None, oid = None):
		if rel and oid:
			if rel in item['__data__'] and type(item['__data__'][rel]) == dict:
				item['__data__'][rel]['id'] = oid
			else:
				item['__data__'][rel] = oid
		data = {}
		model = item ['__model__']
		m = self._pool.get(model)
		excl_fields = m._o2mfields + m._m2mfields
		for k in filter(lambda x: x not in excl_fields,item['__data__'].keys()):
			if k in m._columns and m._columns[k]._type in ('many2one','related'):
				if rel and k != rel or not rel:
					if type(item['__data__'][k]) == dict:
						data[k] = item['__data__'][k]['id']
					else:
						data[k] = item['__data__'][k]
			elif k in m._columns and m._columns[k]._type == 'json':
				data[k] = json.dumps(item['__data__'][k])
			else:
				data[k] = item['__data__'][k]

		if 'id' in data:
			r = _writeRecord(m,data,self._context)
		else:
			r = _createRecord(m,data,self._context)

		if r:
			item['__data__']['id'] = r
			path = item['__path__']
			self._data._getCData(path)['id'] = r
			self._data._odata[path]['id'] = copy.deepcopy(r)
			if self._data._primary and path in self._data._pdata:
				self._data._pdata[path]['id'] = copy.deepcopy(r)

			if '__m2m_containers__' in item:
				m2m_containers = item['__m2m_containers__']
				for key in m2m_containers.keys():
					self._m2m_appendRows(m2m_containers[key])
	
			if '__o2m_containers__' in item:
				o2m_containers = item['__o2m_containers__']
				for key in o2m_containers.keys():
					self._createItems(o2m_containers[key],self._pool.get(model)._columns[key].rel,item['__data__']['id'])

	def _o2m_appendItems(self,items):
		if len(items) > 0:
			parents = {}
			for item in items:
				parents.setdefault(item['__container__'].split('.')[1],{}).setdefault(item['__model__'],[]).append(item)
				
			for pkey in parents.keys():
				for mkey in parents[pkey].keys():
					m = self._pool.get(mkey)
					rows = list(map(lambda x:x['__data__'],parents[pkey][mkey]))
					trg1 = m._getTriger('bi')
					for trg11 in trg1:
						kwargs = {'r1':rows,'context':self._context}
						trg11(**kwargs)

					for item in parents[pkey][mkey]:
						self._o2m_appendItem(item)

					trg2 = m._getTriger('ai')
					for trg22 in trg2:
						kwargs = {'r1':rows,'context':self._context}
						trg22(**kwargs)

	def _o2m_appendItem(self,item):
		data = {}
		path = item['__path__']
		model = item['__model__']
		container = item['__container__']
		cn,parent = container.split('.')
		oid = self._data._getCData(parent)['id']
		rel = self._pool.get(self._data._cmodels[parent])._columns[cn].rel
		recname = self._pool.get(self._data._cmodels[parent])._getRecNameName()
		data[rel] = oid
		m = self._pool.get(model)
		excl_fields = m._o2mfields + m._m2mfields
		for k in filter(lambda x: x not in excl_fields,item['__data__'].keys()):
			if m._columns[k]._type in ('many2one','related'):
				if k != rel:
					data[k] = item['__data__'][k]['id']
			elif k in m._columns and m._columns[k]._type == 'json':
				data[k] = json.dumps(item['__data__'][k])
			else:
				data[k] = item['__data__'][k]

		r = _createRecord(m,data,self._context)
		if r:
			item['__data__']['id'] = r
			self._data._getCData(path)['id'] = r
			self._data._odata[path]['id'] = copy.deepcopy(r)
			if self._data._primary and path in self._data._pdata:
				self._data._pdata[path]['id'] = copy.deepcopy(r)

		if '__o2m_containers__' in item:
			o2m_containers = item['__o2m_containers__']
			for key in o2m_containers.keys():
				if '__o2m_remove__' in o2m_containers[key]:
					self._o2m_removeItems(o2m_containers[key]['__o2m_removr__'])

				if '__o2m_append__' in o2m_containers[key]:
					self._o2m_appendItems(o2m_containers[key]['__o2m_append__'])

	def _o2m_removeItems(self,items):
		if len(items) > 0:
			parents = {}
			for item in items:
				parents.setdefault(item['__container__'].split('.')[1],{}).setdefault(item['__model__'],[]).append(item)
				
			for pkey in parents.keys():
				for mkey in parents[pkey].keys():
					m = self._pool.get(mkey)
					rows = list(map(lambda x:x['__data__'],parents[pkey][mkey]))
					trg1 = m._getTriger('bd')
					for trg11 in trg1:
						kwargs = {'cr':self._cr,'pool':self._pool,'uid':self._uid,'r2':rows,'context':self._context}
						trg11(**kwargs)

					for item in parents[pkey][mkey]:
						self._o2m_removeItem(item)

					trg2 = m._getTriger('ad')
					for trg22 in trg2:
						kwargs = {'cr':self._cr,'pool':self._pool,'uid':self._uid,'r2':rows,'context':self._context}
						trg22(**kwargs)

	def _o2m_removeItem(self,item):
		if 'id' in item['__data__']:
			if '__o2m_containers__' in item:
				for k in item['__o2m_containers__'].keys():
					for r in item['__o2m_containers__'][k]:
						self._o2m_removeItem(r)
			data = item['__data__']
			m = self._pool.get(item['__model__'])
			r = _unlinkRecord(m,data,self._context)

	def _m2m_appendRows(self,rows):
		rels = {}
		for row in rows:
			m = self._pool.get(row['__model__'])
			cn,parent = row['__container__'].split('.')
			oid = self._data._getCData(parent)['id']
			rel = m._columns[cn].rel
			id1 = m._columns[cn].id1
			id2 = m._columns[cn].id2
			rels.setdefault(oid,[]).append(row['__data__']['id'])

		for oid in rels.keys():
			_m2mcreate(m,rel,id1,id2,oid,rels[oid],self._context)

	def _m2m_removeRows(self,rows):
		rels = {}
		for row in rows:
			m = self._pool.get(row['__model__'])
			c = row['__container__'].split('.')
			oid = self._data._getCData(c[1])['id']
			rel = m._columns[c[0]].rel
			id1 = m._columns[c[0]].id1
			id2 = m._columns[c[0]].id2
			rels.setdefault(oid,[]).append(row['__data__']['id'])

		for oid in rels.keys():
			_m2munlink(m,rel,id1,id2,oid,rels[oid],self._context)

	def _updateItems(self,items):
		models = {}
		for key in items.keys():
			model = self._data._cmodels[key]
			models.setdefault(model,{})[key]  = items[key]
		for model in models.keys():
			m = self._pool.get(model)
			for mkey in models[model].keys():
				data = {}
				for k in models[model][mkey].keys():
					if m._columns[k]._type in ('many2one','related'):
						data[k] = models[model][mkey][k]['id']
					elif k in m._columns and m._columns[k]._type == 'json':
						data[k] = json.dumps(models[model][mkey][k])
					else:
						data[k] = models[model][mkey][k]
			
				cdata = self._data._getCData(self._data._cdata[mkey])
				if 'id' in cdata:
					data['id'] = cdata['id']
					r = _writeRecord(m, data, self._context)
				else:
					r = _createRecord(m,data,self._context)
					if r:
						models[model][mkey]['id'] = r

	def _reset(self):	
		self._commit_diffs = {}
		self._roolback()

		return ['reseted']

	def _commit(self,action='commit work'):
		
		try:
			self._cr.commit()
			
			if hasattr(self,'_data'):
				res = self._save_commit(self._data,self._commit_diffs)
				if self._mode in ('new',):
					self._clear()
	
				return res
			
			return ['commited']			
		except:
			raise


	def _rollback(self):
		if self._mode in ('new',):
			self._clear()
		
		self._cr.rollback()
		
		return ['rollbacked']
			
	def _post_diff_A(self,data,diffs,context):
		if  '__o2m_append__' in diffs:
			apnds1 = diffs['__o2m_append__']
			for apnd1 in apnds1:
				if '__o2m_containers__' in apnd1:
					for k1 in apnd1['__o2m_containers__'].keys():
						if len(apnd1['__o2m_containers__'][k1]) > 0:
							self._post_diff_recursive(data,apnd1['__o2m_containers__'][k1],context)
	
				m = self._pool.get(apnd1['__model__'])
				on_change_fields = list(filter(lambda x: x in m._on_change_fields and x is not None,apnd1['__data__'].keys()))
				if len(on_change_fields) > 0:
					ci = m.columnsInfo(columns=on_change_fields,attributes=['on_change','priority'])
					priority = {}
					for on_change_field in on_change_fields:
						priority.setdefault(ci[on_change_field]['on_change'],set()).add(on_change_field)
					
					pkeys = list(priority.keys())
					pkeys.sort()
		
					for pkey in pkeys:
						for on_change_field in priority[pkey]:
							self._on_change(apnd1['__path__'],apnd1['__model__'],on_change_field,context)
							self._do_calculate(apnd1['__path__'],context)
							diffs2 = data._wdiffs()
							if len(diffs2) > 0 and '__o2m_append__' in diffs2:
								self._post_diff_A(data,diffs2,context)
	
							diffs4 = {}
							for k in filter(lambda x: x in ('__update__','__insert__','__delete__'),diffs2.keys()):
								diffs4[k] = diffs2[k]
								
							if len(diffs4) > 0:
								self._post_diff_U(data,diffs4,context)
	
#
	def _post_diff_U(self,data,diffs,context):
			if '__insert__' in diffs:
				insts = diffs['__insert__']
				for inst in insts.keys():
					model = self._data._cmodels[inst]
					m = self._pool.get(model)
					on_change_fields = list(filter(lambda x: x in m._on_change_fields and x is not None,insts[inst].keys()))
					if len(on_change_fields) > 0:
						ci = m.columnsInfo(columns=on_change_fields,attributes=['on_change','priority'])
						priority = {}
						for on_change_field in on_change_fields:
							priority.setdefault(ci[on_change_field]['on_change'],set()).add(on_change_field)
						
						pkeys = list(priority.keys())
						pkeys.sort()
		
						for pkey in pkeys:
							for on_change_field in priority[pkey]:
								self._on_change(inst,model,on_change_field,context)
								self._do_calculate(inst,context)
								diffs1 = data._wdiffs()
								if len(diffs1) > 0 and '__o2m_append__' in diffs1:
									self._post_diff_A(data,diffs1,context)
		
			if '__update__' in diffs:
				upds = diffs['__update__']
				for upd in upds.keys():
					model = self._data._cmodels[upd]
					m = self._pool.get(model)
					on_change_fields = list(filter(lambda x: x in m._on_change_fields and x is not None,upds[upd].keys()))
					if len(on_change_fields) > 0:
						ci = m.columnsInfo(columns=on_change_fields,attributes=['on_change','priority'])
						priority = {}
						for on_change_field in on_change_fields:
							priority.setdefault(ci[on_change_field]['on_change'],set()).add(on_change_field)
						
						pkeys = list(priority.keys())
						pkeys.sort()
		
						for pkey in pkeys:
							for on_change_field in priority[pkey]:
								self._on_change(upd,model,on_change_field,context)
								self._do_calculate(upd,context)
								diffs1 = data._wdiffs()
								if len(diffs1) > 0 and '__o2m_append__' in diffs1:
									self._post_diff_A(data,diffs1,context)
	
	
				if '__delete__' in diffs:
					unlks = diffs['__delete__']
					for unlk in unlks.keys():
						model = self._data._cmodels[unlk]
						m = self._pool.get(model)
						on_change_fields = list(filter(lambda x: x in m._on_change_fields and x is not None,unlks[unlk].keys()))
						if len(on_change_fields) > 0:
							ci = m.columnsInfo(columns=on_change_fields,attributes=['on_change','priority'])
							priority = {}
							for on_change_field in on_change_fields:
								priority.setdefault(ci[on_change_field]['on_change'],set()).add(on_change_field)
							
							pkeys = list(priority.keys())
							pkeys.sort()
			
							for pkey in pkeys:
								for on_change_field in priority[pkey]:
									self._on_change(unlk,model,on_change_field,context)
									self._do_calculate(unlk,context)
									diffs1 = data._wdiffs()
									if len(diffs1) > 0 and '__o2m_append__' in diffs1:
										self._post_diff_A(data,diffs1,context)

#
	def _post_diff_recursive(self,data,apnds1,context):
		for apnd1 in apnds1:
			if '__o2m_containers__' in apnd1:
				for k1 in apnd1['__o2m_containers__'].keys():
					self._post_diff_recursive(data,apnd1['__o2m_containers__'][k1],context)

			m = self._pool.get(apnd1['__model__'])
			on_change_fields = list(filter(lambda x: x in m._on_change_fields and x is not None,apnd1['__data__'].keys()))
			if len(on_change_fields) > 0:
				ci = m.columnsInfo(columns=on_change_fields,attributes=['on_change','priority'])
				priority = {}
				for on_change_field in on_change_fields:
					priority.setdefault(ci[on_change_field]['on_change'],set()).add(on_change_field)
				
				pkeys = list(priority.keys())
				pkeys.sort()
	
				for pkey in pkeys:
					for on_change_field in priority[pkey]:
						self._on_change(apnd1['__path__'],apnd1['__model__'],on_change_field,context)
						self._do_calculate(apnd1['__path__'],context)
						diffs2 = data._wdiffs()
						if len(diffs2) > 0 and '__o2m_append__' in diffs2:
							self._post_diff(data,diffs2['__o2m_append__'],context)

#
	def _post_diffs(self,context):
		diffs1 = self._data._odiffs(False)
		if len(diffs1) > 0:
			self._data._clearTree('w')
			self._data._copyBuildLevel('w','c')
			#ch1 = DCacheDict(self._data._getCData(self._data._root),self._data._model,self._cr,self._pool,self._uid,self._context)
			ch1 = self._data
	
			if  '__o2m_append__' in diffs1:
				self._post_diff_A(ch1,diffs1,context)
			
			diffs2 = ch1._odiffs()
	
			self._data._apply_from_diffs('o','c',diffs2)
			return eval(str(diffs2))

		return eval(str(diffs1))

	def _mcache(self,path,key=None,value=None,context={}):
		res = {}

		if 'debug' in context and context['debug']:
			web_pdb.set_trace()

		self._do_diff(path,key,value,context)
		self._diffs = self._post_diffs(context)

		if len(self._diffs) > 0:
			res['__data__'] = copy.deepcopy(self._diffs)
			self._diffs.clear()

		if len(self._checks) > 0:
			res['__checks__'] = copy.deepcopy(self._checks)
			self._checks.clear()

		if len(res) > 0:
			return [res]
		
		return []

