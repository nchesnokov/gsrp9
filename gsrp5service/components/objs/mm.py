import os
import copy
from functools import reduce
import uuid
from decimal import Decimal
import datetime
import psycopg2
import ctypes
import json
import toposort
#from deepdiff.diff import DeepDiff
from gsrp5service.orm import gensql
from gsrp5service.orm.mm import browse_record, browse_record_list,browse_null
from gsrp5service.orm.common import MAGIC_COLUMNS
#from datetime import datetime,date,time
import time as tm
import web_pdb

from gsrp5service.orm.mm import _m2mfieldid2

__all__ = ['count','search','select','read','write','modify','create','insert','upsert','update','unlink','delete','browse','selectbrowse','tree','browse_record','browse_record_list','browse_null']

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

def _conv_record_to_ext(self,record,context):
	for key in filter(lambda x: x != 'id',record.keys()):
		if self._columns[key]._type in ('many2one','related'):
			if type(record[key]) == str:
				try:
					uuid.UUID(record[key])
					m = self._pool.get(self._columns[key].obj)
					recname = m._RecNameName
					ctx = context.copy()
					ctx['read'] = 'raw'
					v = m.read(record[key],[recname],ctx)
					if len(v) > 0:
						if type(v[0]) == dict:
							try:
								record[key] = {'id':record[key],'name': v[0][recname]}
							except:
								pass
								#web_pdb.set_trace()
							
				except ValueError:
					m = self._pool.get(self._columns[key].obj)
					recname = m._RecNameName
					ctx = context.copy()
					ctx['read'] = 'raw'
					v = m.search([(recname,'=',record[key])])
					if len(v) > 0:
						if type(v[0]) == dict:
							record[key] = {'id':v[0],'name':record[key]}
	
	return record

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
		
	#print('RECORDS:',records)	
		
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
	
	i18nfields = self._i18nfields
	fields = list(filter(lambda x: x != 'id',record.keys()))
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
		raise orm_exception("Fields: %s of model: %s is required and not found in record: %s" % (emptyfields, self.modelInfo(['name'])['name'], record))

	trg1 = self._getTriger('bir')
	for trg11 in trg1:
		kwargs = {'r1':record,'context':context}
		trg11(**kwargs)



	if 'id' in record:
		record_m = {'id':record['id']}
		record_t = {'id':record['id']}
	else:
		record_m = {}
		record_t = {}
			
	for k in filter(lambda x: x != 'id',record.keys()):
		if k in i18nfields:
			record_t[k] = record[k]
		else:
			record_m[k] = record[k]
	sql,vals = gensql.Create(self, record_m, context)
	rowcount = self._execute(sql,vals)
	if rowcount > 0:
		oid = self._cr.fetchone()[0]
		if 'id' in record_t and len(record_t) > 1 or 'id' not in record_t and len(record_t) > 0:
			if 'id' not in record_t:
				record_t['id'] = oid
			if 'lang' not in record_t:
				#web_pdb.set_trace()
				lang = self._pool.get('bc.users').read(self._session._uid,[{'preferences':['user_id','lang']}],{})
				if len(lang[0]['preferences']) > 0:
					record_t['lang'] = lang[0]['preferences'][0]['lang']['id']
				else:
					if 'lang' in context:
						record_t['lang'] = self._session._lang2id[context['lang']]
					else:
						record_t['lang'] = self._session._lang2id['EN']
			sql,vals = gensql.CreateI18N(self, record_t, context)
			rowcount = self._execute(sql,vals)



	# sql,vals = gensql.Create(self, record, context)
	# rowcount = self._execute(sql,vals)
	# if rowcount > 0:
		# oid = self._cr.fetchone()[0]

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
	i18nfields = self._i18nfields
	fields = list(filter(lambda x: x != 'id',record.keys()))
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

	if 'id' in record:
		record_m = {'id':record['id']}
		record_t = {'id':record['id']}
	else:
		record_m = {}
		record_t = {}
			
	for k in filter(lambda x: x != 'id',record.keys()):
		if k in i18nfields:
			record_t[k] = record[k]
		else:
			record_m[k] = record[k]

	sql,vals = gensql.Write(self, record_m, context)
	rowcount = self._execute(sql,vals)
	if rowcount > 0:
		oid = self._cr.fetchone()[0]
		if 'id' in record_t and len(record_t) > 1 or 'id' not in record_t and len(record_t) > 0:
			if 'id' not in record_t:
				record_t['id'] = oid
			if 'lang' not in record_t:
				#web_pdb.set_trace()
				lang = self._pool.get('bc.users').read(self._session._uid,[{'preferences':['user_id','lang']}],{})
				if len(lang[0]['preferences']) > 0:
					record_t['lang'] = lang[0]['preferences'][0]['lang']['id']
				else:
					if 'lang' in context:
						record_t['lang'] = self._session._lang2id[context['lang']]
					else:
						record_t['lang'] = self._session._lang2id['EN']
			sql,vals = gensql.WriteI18N(self, record_t, context)
			rowcount = self._execute(sql,vals)

	# if rowcount > 0:
		# oid = self._cr.fetchone()[0]

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
	i18nfields = self._i18nfields
	fields = list(set(list(filter(lambda x: x != 'id',record.keys()))) - set(i18nfields))
	modelfields = list(set(self._columns.keys()) - set(i18nfields))
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

	emptyfields = list(filter(lambda x: x in fields and record[x] is None,list(set(self._requiredfields) - set(i18nfields))))		
	if len(emptyfields) > 0:
		raise orm_exception("Fields: %s of model: %s is required and not found in record: %s" % (emptyfields, self.modelInfo(['name'])['name'], record))

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
	if 'id' in record:
		record_m = {'id':record['id']}
		record_t = {'id':record['id']}
	else:
		record_m = {}
		record_t = {}
			
	for k in filter(lambda x: x != 'id',record.keys()):
		if k in i18nfields:
			record_t[k] = record[k]
		else:
			record_m[k] = record[k]
	sql,vals = gensql.Modify(self, record_m, context)
	rowcount = self._execute(sql,vals)
	if rowcount > 0:
		oid = self._cr.fetchone()[0]
		if 'id' in record_t and len(record_t) > 1 or 'id' not in record_t and len(record_t) > 0:
			if 'id' not in record_t:
				record_t['id'] = oid
			if 'lang' not in record_t:
				#web_pdb.set_trace()
				lang = self._pool.get('bc.users').read(self._session._uid,[{'preferences':['user_id','lang']}],{})
				if len(lang[0]['preferences']) > 0:
					record_t['lang'] = lang[0]['preferences'][0]['lang']['id']
				else:
					if 'lang' in context:
						record_t['lang'] = self._session._lang2id[context['lang']]
					else:
						record_t['lang'] = self._session._lang2id['EN']
			sql,vals = gensql.ModifyI18N(self, record_t, context)
			rowcount = self._execute(sql,vals)
			

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

	model_info = self.modelInfo() #attributes=['type','rel','obj','id1','id2'])
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
	if 'lang' not in context:
		context['lang'] = os.environ['LANG']
	if 'tz' not in context:
		context['tz'] = tm.tzname[1]
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

	if 'lang' not in context:
		context['lang'] = os.environ['LANG']

	if 'tz' not in context:
		context['tz'] = tm.tzname[1]

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

	if 'lang' not in context:
		context['lang'] = os.environ['LANG']

	if 'tz' not in context:
		context['tz'] = tm.tzname[1]

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

				for jk in self._jsonfields:
					if jk in record:
						if type(record[jk]) == str:
							record[jk] = json.loads(record[jk])

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

				for jk in self._jsonfields:
					if jk in record:
						if type(record[jk]) == str:
							record[jk] = json.loads(record[jk])

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

	if 'lang' not in context:
		context['lang'] = os.environ['LANG']

	if 'tz' not in context:
		context['tz'] = tm.tzname[1]

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

			for jk in self._jsonfields:
				if jk in record:
					if type(record[jk]) == str:
						record[jk] = json.loads(record[jk])
				
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
	if not self._access._checkRead():
		orm_exception("Select:access dennied of model % s" % (self._name,))
	
	return _select(self,  fields, cond, context, limit, offset)

# Other start
def unlink(self, ids, context = {}):
	if not self._access._checkUnlink():
		orm_exception("Unlink:access dennied of model % s" % (self._name,))

	res = []
	if 'lang' not in context:
		context['lang'] = os.environ['LANG']
	if 'tz' not in context:
		context['tz'] = tm.tzname[1]
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
	if not self._access._checkUnlink():
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

	if 'lang' not in context:
		context['lang'] = os.environ['LANG']
	if 'tz' not in context:
		context['tz'] = tm.tzname[1]

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

	if 'lang' not in context:
		context['lang'] = os.environ['LANG']
	if 'tz' not in context:
		context['tz'] = tm.tzname[1]

	if type(records) in (list,tuple):
		return _writeRecords(self, records,context)

	elif type(records) == dict:
		return [_writeRecord(self, records, context)]

def modify(self, records, context = {}):
	if not self._access._checkWrite():
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

	if 'lang' not in context:
		context['lang'] = os.environ['LANG']
	if 'tz' not in context:
		context['tz'] = tm.tzname[1]

	if type(records) in (list,tuple):
		return _modifyRecords(self, records, context)

	elif type(records) == dict:
		return [_modifyRecord(self, records, context)]
	
def update(self, record, cond = None,context = {}):
	if not self._access._checkWrite():
		orm_exception("Update:access dennied of model % s" % (self._name,))

	res = []
	fields = list(record.keys())
	if 'lang' not in context:
		context['lang'] = os.environ['LANG']
	if 'tz' not in context:
		context['tz'] = tm.tzname[1]
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
	if not self._access._checkCreate():
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
	if 'lang' not in context:
		context['lang'] = os.environ['LANG']
	if 'tz' not in context:
		context['tz'] = tm.tzname[1]

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
				rel = self._getSpecName(columninfo['rel'])
				rels = values[fm[key]]
				id1 = self._getSpecName(columninfo['id1'])
				if columninfo['id2']:
					id2 = self._getSpecName(columninfo['id2'])
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
	if not self._access._checkCreate():
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
	if 'lang' not in context:
		context['lang'] = os.environ['LANG']
	if 'tz' not in context:
		context['tz'] = tm.tzname[1]


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
				rel = self._getSpecName(columninfo['rel'])
				rels = values[fm[key]]
				id1 = self._getSpecName(columninfo['id1'])
				if columninfo['id2']:
					id2 = self._getSpecName(columninfo['id2'])
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
	if not self._access._checkRead():
		orm_exception("Browse:access dennied of model % s" % (self._name,))

	brl = browse_record_list()
	
	for r in _read(self, ids, fields, context):
		brl.append(browse_record(self._uid,r))

	if len(brl) == 0:
		return browse_null()

	return brl

def selectbrowse(self, fields = None ,cond = None, context = {}, limit = None, offset = None):
	if not self._access._checkRead():
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
	self._execute(sql)
	if self._cr.rowcount > 0:
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
	self._execute("SELECT id,%s,%s FROM %s WHERE %s = '%s'" % (id1,id2,rel,id1,oid))
	if self._cr.rowcount > 0:
		ids2 = list(map(lambda x: x[2],self._cr.fetchall(fields = ['id',id1,id2], columnsmeta = {'id':'uuid',id1:'uuid',id2:'uuid'})))
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
		self._execute(sql)
	if self._cr.rowcount > 0:
		res.extend(list(map(lambda x: x[0],self._cr.fetchall()))) 
	
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
	self._execute("SELECT id,%s,%s FROM %s WHERE %s = '%s'" % (id1,id2,rel,id1,oid))
	if self._cr.rowcount > 0:
		ids2 = list(map(lambda x: x[2],self._cr.fetchall(fields = ['id',id1,id2], columnsmeta = {'id':'uuid',id1:'uuid',id2:'uuid'})))
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
		self._execute(sql)
	if self._cr.rowcount > 0:
		res.extend(list(map(lambda x: x[0],self._cr.fetchall()))) 
	
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
	self._execute(sql)
	if self._cr.rowcount > 0:
		res.extend(list(map(lambda x: x[0],self._cr.fetchall()))) 
	
	return res

def _tree(self, fields = None ,parent = None, context = {}):

	res = []

	if 'lang' not in context:
		context['lang'] = os.environ['LANG']

	if 'tz' not in context:
		context['tz'] = tm.tzname[1]

	if 'FETCH' not in context:
		context['FETCH'] = 'DICT'

	fetch = context['FETCH']

	if not fetch.upper() in ('LIST','DICT','RAW'):
		orm_exception('Invalid fetch mode: %s' % (fetch.upper(),))

	if parent is None:
		cond = [(self._getSpecName('parent_id'),'?')]
	else:
		cond = [(self._getSpecName('parent_id'),'=', parent)]

	sql,vals = gensql.Select(self,fields, cond, context,None,None)
	rowcount = self._execute(sql,vals)

	if rowcount > 0:
		res.extend(_fetch_results(self,fields,context))
		for r in res:
			r[self._getSpecName('childs_id')].extend(_tree(self, fields, r[self._getSpecName('rec_name')], context))

	return res

def tree(self, fields = None ,parent = None, context = {}):
	if not self._access._checkRead():
		orm_exception("Tree:access dennied of model % s" % (self._name,))
	
	return _tree(self, fields, parent, context)


