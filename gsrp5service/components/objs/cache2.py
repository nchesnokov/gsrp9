import copy
import uuid
from decimal import Decimal
import datetime
import psycopg2
import ctypes
from deepdiff.diff import DeepDiff
from gsrp5service.orm import gensql
from gsrp5service.orm.common import MAGIC_COLUMNS
import web_pdb

from gsrp5service.orm.mm import _m2mfieldid2

class orm_exception(Exception):
	def __init__(self, *args, **kwargs):
		self.args = args
		self.kwargs = kwargs

def _join_diffs(d1,d2):
	for k2 in d2.keys():
		if k2 in ('__update__','__insert__','__delete__'):
			d1[k2].update(d2[k2])
		elif k2 in ('__append__','__remove__'):
			d1[k2].extend(d2[k2])

def _createRecord(self, cr, pool, uid, record, context):
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
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':record,'context':context}
		trg11(**kwargs)

	sql,vals = gensql.Create(self,pool,uid,self.modelInfo(), record, context)
	cr.execute(sql,vals)
	if cr.cr.rowcount > 0:
		oid = cr.fetchone()[0]

	trg2 = self._getTriger('air')
	for trg22 in trg2:
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':record,'context':context}
		trg22(**kwargs)

	return oid

def _writeRecord(self, cr, pool, uid, record, context):
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
		record21 = self.read(cr, pool, uid, record['id'], self._selectablefields, ctx)

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
					kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':record,'r2':record,'context':context}
					trg11(**kwargs)

	sql,vals = gensql.Write(self,pool,uid,self.modelInfo(), record, context)
	cr.execute(sql,vals)
	if cr.cr.rowcount > 0:
		oid = cr.fetchone()[0]

	if len(upd_cols) > 0:
		trg2 = self._getTriger('aur')
		if trg2 and len(trg2) > 0:
			for trg22 in trg2:
				kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':record,'r2':record,'context':context}
				trg22(**kwargs)

	return oid

def _modifyRecord(self, cr, pool, uid, record, context):
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
			record21 = self.read(cr, pool, uid, record['id'], self._selectablefields, ctx)

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
				kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':record,'r2':record2,'context':context}
				trg11(**kwargs)
		
	sql,vals = gensql.Modify(self,pool,uid,self.modelInfo(), record, context)
	cr.execute(sql,vals)
	if cr.cr.rowcount > 0:
		oid = cr.fetchone()[0]

	if record2 is None or len(upd_cols) > 0:
		trg2 = self._getTriger('aur')
		for trg22 in trg2:
			kwargs = {'cr':cr,'pool':pool,'uid':uid,'r1':record,'r2':record2,'context':context}
			trg22(**kwargs)

	return oid

def _unlinkRecord(self, cr, pool, uid, record, context = {}):
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
			id2 = _m2mfieldid2(pool,obj,rel)

		rels = []

	trg1 = self._getTriger('bdr')
	for trg11 in trg1:
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'r2':record,'context':context}
		trg11(**kwargs)

	sql,vals = gensql.Unlink(self,pool,uid,self.modelInfo(),[record['id']],context)
	cr.execute(sql,vals)
	if cr.cr.rowcount > 0:
		oid = cr.fetchone()[0]

	trg2 = self._getTriger('adr')
	for trg22 in trg2:
		kwargs = {'cr':cr,'pool':pool,'uid':uid,'r2':record,'context':context}
		trg22(**kwargs)

	return oid

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
		self._model = model
		self._cr = cr
		self._pool = pool
		self._uid = uid
		self._context = context
		self._primary = primary

		for v in ('data','paths','r2c','containers','names','metas','models','rels','attrs'):
			for a in ('p','o','c'):
				if not primary and a == 'p':
					continue
				setattr(self,'_%s%s' % (a,v),{})

		self._buildTree(data,model)
		self._copyBuild()
		
	@property
	def _data(self):
		return self._cdata[self._root]

	def _updateTree(self,data,model):
		for v in ('data','paths','r2c','containers','names','metas','models','rels','attrs'):
			getattr(self,'_c' + v).clear()

		self._buildTree(data,model,parent=None,name=None, mode = 'N')
	
	def _buildTree(self,data,model,parent=None,name=None, mode = 'N'):
		if type(data) != dict:
			raise TypeError

		oid = str(id(data))
		if mode == 'N1':
			web_pdb.set_trace()

		if oid not in self._cdata:
			if model not in self._cmetas:
				self._cmetas[model] = self._pool.get(model).columnsInfo(attributes=['type','obj','rel','id1','id2'])
			
			ci = self._cmetas[model]
	
			if mode == 'N' and not hasattr(self,'_root'):
				self._root = oid

			self._cdata[oid] = data
			self._cmodels[oid] = model
			self._set_meta(oid)
			if parent and name:
				self._cpaths.setdefault(oid,{})[name] = parent
				self._cr2c[oid] = self._cnames[name + '.' + str(parent)]
			else:
				self._cpaths[oid] = None
	
			for m2mfield in self._pool.get(model)._m2mfields:
				if m2mfield in data: 
					self._m2m_buildTree(data[m2mfield],ci[m2mfield]['rel'],oid,m2mfield,model)
		
			for o2mfield in self._pool.get(model)._o2mfields:
				cn = o2mfield + '.' + oid
				coid = str(id(data[o2mfield]))
				self._ccontainers[coid] = cn
				self._cnames[cn] = coid
				self._cdata[coid] = data[o2mfield]
				self._cmodels[coid] = ci[o2mfield]['obj']
	
				if mode != 'I':
					for r1 in data[o2mfield]:
						self._buildTree(r1,ci[o2mfield]['obj'],oid,o2mfield,mode)

	def _m2m_buildTree(self,data,rel,parent,name,model):
		if type(data) == dict:
			cn = name + '.' + parent
			coid = self._cnames[cn]
			
			m2moid = str(id(data))
			self._cdata[m2moid] = data
			self._cdata[coid].append(data)
			self._cmodels[m2moid] = model
			self._crels[m2moid] = rel
			self._cpaths.setdefault(m2moid,{})[name] = parent
			self._cr2c[m2moid] = self._cnames[cn]

		elif type(data) in (list,tuple):

			cn = name + '.' + parent
			coid = str(id(data))
			self._ccontainers[coid] = cn
			self._cnames[cn] = coid
			self._cdata[coid] = data
			self._crels[coid] = rel

			for r in data:
				m2moid = str(id(r))
				self._cdata[m2moid] = r
				self._cmodels[m2moid] = model
				self._crels[m2moid] = rel
				self._cpaths.setdefault(m2moid,{})[name] = parent
				self._cr2c[m2moid] = self._cnames[cn]

	def _copyBuild(self):
		self._odata.update(copy.deepcopy(self._cdata))
		self._opaths.update(copy.deepcopy(self._cpaths))
		self._or2c.update(copy.deepcopy(self._cr2c))
		self._ocontainers.update(copy.deepcopy(self._ccontainers))
		self._onames.update(copy.deepcopy(self._cnames))
		self._ometas.update(copy.deepcopy(self._cmetas))
		self._omodels.update(copy.deepcopy(self._cmodels))
		self._orels.update(copy.deepcopy(self._crels))
		self._oattrs.update(copy.deepcopy(self._cattrs))
		if self._primary:
			self._pdata.update(copy.deepcopy(self._cdata))
			self._ppaths.update(copy.deepcopy(self._cpaths))
			self._pr2c.update(copy.deepcopy(self._cr2c))
			self._pcontainers.update(copy.deepcopy(self._ccontainers))
			self._pnames.update(copy.deepcopy(self._cnames))
			self._pmetas.update(copy.deepcopy(self._cmetas))
			self._pmodels.update(copy.deepcopy(self._cmodels))		
			self._prels.update(copy.deepcopy(self._crels))
			self._pattrs.update(copy.deepcopy(self._cattrs))
			
	def _diffs(self,o,c,commit):
		res = {}
		
		path = self._root
		self._updateTree(self._data,self._model)
		res.update(self._cmpDict(o,c,path))

		if commit:
			self._apply_from_diffs(o,c,res)

		return res

	def _apply_from_diffs(self,o,c,diffs):
		if ('__update__' in diffs ):
			for k in diffs['__update__'].keys():
				getattr(self,'_%sdata' % (o,))[k].update(copy.deepcopy(diffs['__update__'][k]))

		if ('__insert__' in diffs ):
			for k in diffs['__insert__'].keys():
				getattr(self,'_%sdata' % (o,))[k].update(copy.deepcopy(diffs['__insert__'][k]))

		if ('__delete__' in diffs ):
			for k in diffs['__delete__'].keys():
				for d in diffs['__delete__'][k].keys():
					del getattr(self,'_%sdata' % (c,))[k][d]

		if ('__meta_update__' in diffs ):
			#web_pdb.set_trace()
			for k in diffs['__meta_update__'].keys():
				for k1 in diffs['__meta_update__'][k]:
					getattr(self,'_%sattrs' % (o,))[k][k1].update(copy.deepcopy(diffs['__meta_update__'][k][k1]))

		if ('__meta_insert__' in diffs ):
			for k in diffs['__meta_insert__'].keys():
				getattr(self,'_%sattrs' % (o,))[k].update(copy.deepcopy(diffs['__meta_insert__'][k]))

		if ('__meta_delete__' in diffs ):
			for k in diffs['__meta_delete__'].keys():
				del getattr(self,'_%sattrs' % (c,))[k][d]

		if ('__o2m_append__' in diffs or '__m2m_append__' in diffs):
			for k in ('__o2m_append__','__m2m_append__'):
				if k not in diffs:
					continue
				for r in diffs[k]:
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
					oattrs[path] = r['__meta__']
					onames[container] = cnames[container]
					ocontainers[cnames[container]] = ccontainers[cnames[container]]
					if k == '__o2m_append__':
						ometas[model] = cmetas[model]
						omodels[path] = cmodels[path] 
					elif k == '__m2m_append__':
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

		if ('__o2m_remove__' in diffs or '__m2m_remove__' in diffs ):
			for k in ('__o2m_remove__','__m2m_remove__'):
				if k not in diffs:
					continue

				for r in diffs[k]:
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
					del oattrs[path]
			
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
		
		ci = self._cmetas[self._cmodels[path]]
		
		ck = list(filter(lambda x: x != 'id' and ci[x]['type'] not in ('many2many','one2many'),getattr(self,'_%sdata' % (c,))[path].keys()))
		ok = list(filter(lambda x: x != 'id' and ci[x]['type'] not in ('many2many','one2many'),getattr(self,'_%sdata' % (o,))[path].keys()))
		uk = list(set(ok).intersection(set(ck)))
		ik = list(set(ck)- set(ok))
		dk = list(set(ok)- set(ck))

		for k in filter(lambda x: x != 'id',getattr(self,'_%sdata' % (c,))[path].keys()):
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
				if k in uk and getattr(self,'_%sdata' % (c,))[path][k] != getattr(self,'_%sdata' % (o,))[path][k]:
					if type(getattr(self,'_%sdata' % (c,))[path][k]) == memoryview:
						res.setdefault('__update__',{}).setdefault(path,{})[k] = (getattr(self,'_%sdata' % (c,))[path][k]).tobytes()
					else:
						res.setdefault('__update__',{}).setdefault(path,{})[k] = getattr(self,'_%sdata' % (c,))[path][k]
				elif k in ik:
					if type(getattr(self,'_%sdata' % (c,))[path][k]) == memoryview:
						res.setdefault('__insert__',{}).setdefault(path,{})[k] = getattr(self,'_%sdata' % (c,))[path][k].tobytes()
					else:
						res.setdefault('__insert__',{}).setdefault(path,{})[k] = getattr(self,'_%sdata' % (c,))[path][k]
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
			ck = list(map(lambda x:str(id(x)),cdata[cnames[container]]))	

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
			for k in filter(lambda x: x != 'id' and ci[x]['type'] == 'many2many',getattr(self,'_%sdata' % (c,))[i].keys()):
				r1 = self._m2m_cmpList(o,c,k + '.' + i)
				m2m_containers.setdefault(k,[]).extend(r1['__m2m_append__'] if '__m2m_append__' in r1 else [])
				
			res.setdefault('__m2m_append__',[]).append({'__path__':i,'__container__':container,'__model__':model,'__m2m_containers__':m2m_containers})

			data = {}

			for v in filter(lambda x: x != 'id' and ci[x]['type'] not in ('one2many','many2many'),getattr(self,'_%sdata' % (c,))[i].keys()):
				data[v] = getattr(self,'_%sdata' % (c,))[i][v]

			o2m_containers = {}
			for k in filter(lambda x: x != 'id' and ci[x]['type'] == 'one2many',getattr(self,'_%sdata' % (c,))[i].keys()):
				r1 = self._o2m_cmpList(o,c,k + '.' + i)
				o2m_containers.setdefault(k,[]).extend(r1['__o2m_append__'] if '__o2m_append__' in r1 else [])

				
			
			res.setdefault('__o2m_append__',[]).append({'__path__':i,'__container__':container,'__model__':model,'__data__':data,'__meta__':self._get_meta(i),'__o2m_containers__':o2m_containers})
	
		for d in dk:
			model = omodels[onames[container]]
			remove_data = copy.deepcopy(odata[d])			
			
			res.setdefault('__o2m_remove__',[]).append({'__path__':d,'__container__':container,'__model__':model,'__data__':remove_data})
			#res.setdefault('__o2m_meta_remove__',[]).append({'__path__':d})

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
			ck = list(map(lambda x:str(id(x)),cdata[cnames[container]]))	

		ik = list(set(ck)- set(ok))
		dk = list(set(ok)- set(ck))
			
		for i in ik:
			d1 = ctypes.cast(int(i), ctypes.py_object).value
			p=container.split('.')

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


		model = omodels[path]
		for o2mfield in self._pool.get(model)._o2mfields:
			container1 = o2mfield + '.' + str(path)
			coid = onames[container1]
			for path1 in filter(lambda x: or2c[x] == coid,or2c.keys()):
				res.extend(self._removeRecursive(o,c,path1))

		container = ocontainers[cr2c[path]]

		cdata[cnames[container]].remove(cdata[path])
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
			
	def _odiffs(self,commit=True):
		return self._diffs('o','c',commit)

	def _pdiffs(self,commit=True):
		if self._primary:
			return self._diffs('p','c',commit)
		else:
			res = {'__create__':self._getData(self._data)}
			if commit:
				self._papply()
			
			return res

	def _oapply(self):
		return self._diffs('o','c',True)

	def _papply(self):
		if self._primary:
			return self._diffs('p','c',True)
		else:
			return self._diffs('o','c',True)

	def _getData(self,d):
		path = str(id(d))

		model = self._cmodels[path]
		data = {}
		container = None
		m2m_container = None
		o2m_containers = {}
		m2m_containers = {}
		ci = self._cmetas[model]
		oid = None
		if 'id' in self._cdata[path]:
			oid = self._cdata[path]['id']
		for k in self._cdata[path].keys():
			if k != 'id' and ci[k]['type'] == 'one2many':
				o2m_containers[k] = self._get_o2mDataContainers(k + '.' + path)
			elif k != 'id' and ci[k]['type'] == 'many2many':	
				m2m_containers[k] = self._get_m2mDataContainers(k + '.' + path,oid)
			else:
				data[k] = self._cdata[path][k]

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

	def _get_m2mDataContainers(self,container,oid):
		res = []
		
		for r in self._cdata[self._cnames[container]]:
			res.append({'__container__':container,'__path__':str(id(r)),'__parent__':container.split('.')[1],'__data__':r})
			
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
				rc = method(self._cr,self._pool,self._uid,self._cdata[path],self._context)
				if rc and len(rc) > 0:
					self._cattrs.setdefault(path,{}).update(rc)

		cm = {}
		for a in ('readonly','invisible','required','state'):
			for c in m._columns.keys():
				if m._columns[c]._type =='referenced':
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
							if s == self._cdata[path][sn]:
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
					rc = method(self._cr,self._pool,self._uid,cm[k][k1],self._cdata[path],self._context)
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
		self._setDefault(model,row)
		self._data = DCacheDict(row,model,self._cr,self._pool,self._uid,self._context,False)
		
		self._do_calculate(self._data._root,context=context)
		self._getMeta()	
		m = self._data._getData(self._data._data)
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
				d = m.select(self._cr,self._pool,self._uid,[m._m2ofields],[('id','=',oid)],self._context,limit=1)
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
			d = m.read(self._cr,self._pool,self._uid,oid,cols,self._context)
			res[model] = d
		
		return res

	def _do_create(self,model,kwargs):
		row = self._pool.get(model).create(**kwargs)
		return row

	def _do_read(self,model,kwargs):
		self._clear()
		self._model = model
		row = self._pool.get(model).read(**kwargs)
		if len(row) > 0:
			self._data = DCacheDict(row[0],model,self._cr,self._pool,self._uid,self._context)
			self._getMeta()
			m = self._data._getData(self._data._data)
			m['__checks__'] = []
			return m
		else:
			return []

	def _do_write(self,model,kwargs):
		row = self._pool.get(model).write(**kwargs)
		return row

	def _do_modify(self,model,kwargs):
		records = kwargs['records']
		if type(records) in (list,tuple):
			for record in records:
				self._data = DCacheDict(record,model,self._cr,self._pool,self._uid,self._context,False)
				self._save(True)
		elif type(records) == dict:
			self._data = DCacheDict(records,model,self._cr,self._pool,self._uid,self._context,False)
			self._save(True)

	def _do_unlink(self,model,kwargs):
		row = self._pool.get(model).unlink(**kwargs)
		return row

	def _do_insert(self,model,kwargs):
		row = self._pool.get(model).insert(**kwargs)
		return row

	def _do_select(self,model,kwargs):
		row = self._pool.get(model).select(**kwargs)
		return row

	def _do_upsert(self,model,kwargs):
		self._clear()
		self._model = model
		row = self._pool.get(model).upsert(**kwargs)
		self._data = DCacheDict(row,model,self._pool)
		self._getMeta()
		m = self._data._getData(self._data._data)
		m['__meta__'] = self._do_meta(str(self._data._root))
		m['__checks__'] = []
		return m

	def _do_update(self,model,kwargs):
		self._clear()
		self._model = model
		row = self._pool.get(model).update(**kwargs)
		self._data = DCacheDict(row,model,self._pool)
		self._getMeta()
		m = self._data._getData(self._data._data)
		m['__meta__'] = self._do_meta(str(self._data._root))
		m['__checks__'] = []
		return m

	def _do_delete(self,model,kwargs):
		self._clear()
		self._model = model
		row = self._pool.get(model).delete(**kwargs)
		self._data = DCacheDict(row,model,self._pool)
		self._getMeta()
		m = self._data._getData(self._data._data)
		m['__meta__'] = self._do_meta(str(self._data._root))
		m['__checks__'] = []
		return m

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
		name = self._meta[model][key]['on_change']
		if name:
			method = getattr(self._pool.get(model),name,None)
			if method:
				_on_change = method(self._cr,self._pool,self._uid,self._data._cdata[path],context)
				if _on_change:
					self._data._cdata[path].update(_on_change)

	def _on_check(self,path,model,key,context):
		name = self._meta[model][key]['on_check']
		if name:
			method = getattr(self._pool.get(model),name,None)
			if method:
				self._checks.setdefault(path,{})[key] = method(self._cr,self._pool,self._uid,key,self._data._cdata[path],context)
	
	def _do_diff(self,path,key,value,context):
		res = {}

		if key not in self._data._cdata[path] or self._data._cdata[path][key] != value:
			self._data._cdata.setdefault(path,{})[key] = value
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
		record = self._data._cdata[path]
		fields = list(record.keys())
		ci = m.columnsInfo(columns=m._computefields,attributes=['compute','priority'])
		priority = {}
		for compute_field in filter(lambda x: x in fields,m._computefields):
			priority.setdefault(ci[compute_field]['priority'],set()).add(ci[compute_field]['compute'])
		
		pkeys = list(priority.keys())
		pkeys.sort()
		for pkey in pkeys:
			for compute_method in priority[pkey]:			
				method = getattr(m,compute_method,None)
				if method and callable(method):
					r = method(self._cr,self._pool,self._uid,record,self._context)
					if r is not None: 
						res.update(r)
	
		return res

	def _do_calculate(self,path,context):
		model = self._data._cmodels[path]
		_computes = self._do_compute(path,model)
		
		if len(_computes) > 0:
			self._data._cdata.setdefault(path,{}).update(_computes)
		
		parents = self._data._cpaths[path]
		if parents:
			for key in parents.keys():
				parent = parents[key]
				self._do_calculate(parent,context)

	def _setDefault(self,model,item):
		_default = self._pool.get(model)._default
		if model not in self._meta:
			self._getMeta([model])
		m1 = self._meta[model]
		for k in _default.keys():
			if k not in item or item[k] is None:
				if m1[k]['type'] in ('numeric','decimal'):
					item[k] = Decimal(_default[k])
				else:
					item[k] = _default[k]	
	
	def _o2m_add(self,model,container,context,view='form'):
		row = self._pool.get(model)._buildEmptyItem()
		self._setDefault(model,row)
		
		p = container.split('.')
		path = p[1]
		self._data._cdata[self._data._cnames[container]].append(row)
		self._data._buildTree(row,model,p[1],p[0],'A')
		
		self._do_calculate(str(id(row)),context)
		
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

	def _o2m_removes(self,rows,context):
		for row in rows:
			path = row['path']
			container = row['container']
			c = container.split('.')
			self._data._cdata[self._data._cnames[container]].remove(self._data._cdata[path])		
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

	def _m2m_add(self,model,container,fields,obj,rel,id1,id2,context={}):
		
		rows = self._pool.get(obj).read(self._cr,self._pool,self._uid,id2,fields,self._context)
		
		p = container.split('.')
		if len(rows) > 0:
			for row in rows:
				self._data._m2m_buildTree(row,rel,p[1],p[0],model)
				
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
		c = container.split('.')
		self._data._cdata[self._data._cnames[container]].remove(self._data._cdata[path])
		del self._data._cdata[path]

		res = {}

		data_diffs = self._data._odiffs(True)


		if len(data_diffs) > 0:
			res['__data__'] = data_diffs

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

		r = self._pool.get(self._meta[model][key]['obj']).select(self._cr,self._pool,self._uid,fields,cond=cond)
		
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
			d = self._data._cdata[path][rel]
			if type(d) == dict:
				r1 = d['name']
			else:
				r1 = d
			cond.append((rel,'=',r1))

		r = self._pool.get(self._meta[model][key]['obj']).select(self._cr,self._pool,self._uid,fields,cond=cond)
		if len(r) > 1:
			res = {'path':path,'key':key,'v':list(map(lambda x: x['id'],r))}
		elif len(r) == 1:
			res = {'path':path,'key':key,'v':r}
		elif len(r) == 0:
			res = {'path':path,'key':key,'v':[]}
		
		return [{'__related_find__':{'__data__':res}}]

	def _action(self,path,name,column = None,context={}):
		res = {}
		act = self._pool.get(self._data._cmodels[path]).do_action(self._cr,self._pool,self._uid,name,column,self._data._cdata[path],context)
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

	def _save(self,autocommit = False):
		diffs = self._data._pdiffs(False)
		print('SAVE-DIFFS:',diffs)
		if len(diffs) == 0:
			return ['no chache']
		
		if '__create__' in diffs:
			self._createItem(diffs['__create__'])
			if 'id' in diffs['__create__']['__data__'] and diffs['__create__']['__data__']['id']:
				return ['commit',diffs['__create__']['__data__']['id']]

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
		
			self._commit_diffs = diffs
		
			if autocommit:
				if self._data._apply_from_diffs('p','c',diffs):
					self._commit_diffs = {}
					return self._commit()
			
			return ['commit']

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
			item['__data__'][rel]['id'] = oid
		data = {}
		model = item ['__model__']
		m = self._pool.get(model)
		excl_fields = m._o2mfields + m._m2mfields
		for k in filter(lambda x: x not in excl_fields,item['__data__'].keys()):
			if k in m._columns and m._columns[k]._type in ('many2one','related'):
				if rel and k != rel or not rel:
					data[k] = item['__data__'][k]['id']
			else:
				data[k] = item['__data__'][k]

		if 'id' in data:
			r = _modifyRecord(m,self._cr,self._pool,self._uid,data,self._context)
		else:
			r = _createRecord(m,self._cr,self._pool,self._uid,data,self._context)

		if r:
			item['__data__']['id'] = r
			path = item['__path__']
			self._data._cdata[path]['id'] = r
			self._data._odata[path]['id'] = copy.deepcopy(r)
			if self._data._primary and path in self._data._pdata:
				self._data._pdata[path]['id'] = copy.deepcopy(r)
		
			if '__m2m_containers__' in item:
				m2m_containers = item['__m2m_containers__']
				for key in m2m_containers.keys():
					self._m2m_appendRows(m2m_containers[key],item['__data__']['id'])
	
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
						kwargs = {'cr':self._cr,'pool':self._pool,'uid':self._uid,'r1':rows,'context':self._context}
						trg11(**kwargs)

					for item in parents[pkey][mkey]:
						self._o2m_appendItem(item)

					trg2 = m._getTriger('ai')
					for trg22 in trg2:
						kwargs = {'cr':self._cr,'pool':self._pool,'uid':self._uid,'r1':rows,'context':self._context}
						trg22(**kwargs)

	def _o2m_appendItem(self,item):
		data = {}
		path = item['__path__']
		model = item['__model__']
		container = item['__container__']
		cn,parent = container.split('.')
		oid = self._data._cdata[parent]['id']
		rel = self._pool.get(self._data._cmodels[parent])._columns[cn].rel
		recname = self._pool.get(self._data._cmodels[parent])._getRecNameName()
		data[rel] = oid
		m = self._pool.get(model)
		excl_fields = m._o2mfields + m._m2mfields
		for k in filter(lambda x: x not in excl_fields,item['__data__'].keys()):
			if m._columns[k]._type in ('many2one','related'):
				if k != rel:
					data[k] = item['__data__'][k]['id']
			else:
				data[k] = item['__data__'][k]

		r = _createRecord(m,self._cr,self._pool,self._uid,data,self._context)
		if r:
			item['__data__']['id'] = r
			self._data._cdata[path]['id'] = r
			self._data._odata[path]['id'] = copy.deepcopy(r)
			if self._data._primary and path in self._data._pdata:
				self._data._pdata[path]['id'] = copy.deepcopy(r)

		if '__o2m_containers__' in item:
			o2m_containers = item['__o2m_containers__']
			for key in o2m_containers.keys():
				self._o2m_appendItems(o2m_containers[key])

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
			data = item['__data__']
			m = self._pool.get(item['__model__'])
			r = _unlinkRecord(m,self._cr,self._pool,self._uid,data,self._context)

	def _m2m_appendRows(self,rows,oid):
		rels = []
		cols = {}
		for row in rows:
			m = self._pool.get(row['__model__'])
			c = row['__container__'].split('.')
			#oid = self._data._cdata[c[1]]['id']
			rel = m._columns[c[0]].rel
			id1 = m._columns[c[0]].id1
			id2 = m._columns[c[0]].id2
			rels.append(row['__data__']['id'])

			m._m2mmodify(self._cr,self._pool,self._uid,rel,id1,id2,oid,rels,self._context)

	def _m2m_removeRows(self,rows):
		rels = []
		for row in rows:
			m = self._pool.get(row['__model__'])
			c = row['__container__'].split('.')
			oid = self._data._cdata[c[1]]['id']
			rel = m._columns[c[0]].rel
			id1 = m._columns[c[0]].id1
			id2 = m._columns[c[0]].id2
			rels.append(row['__data__']['id'])

			m._m2munlink(self._cr,self._pool,self._uid,rel,id1,id2,oid,rels,self._context)

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
					else:
						data[k] = models[model][mkey][k]
			
				if 'id' in self._data._cdata[mkey]:
					data['id'] = self._data._cdata[mkey]['id']
					r = _writeRecord(m,self._cr,self._pool,self._uid,data,self._context)
				else:
					r = _createRecord(m,self._cr,self._pool,self._uid,data,self._context)
					if r:
						models[model][mkey]['id'] = r

	def _reset(self):	
		self._commit_diffs = {}
		self._roolback()

		return ['reseted']

	def _commit(self,action='commit work'):
		
		self._cr.commit()
		
		if self._data._apply_from_diffs('p','c',self._commit_diffs):
			self._commit_diffs = {}
			if self._mode in ('new',):
				self._clear()

			return ['commited']
		
		return ['not commited']

	def _rollback(self):
		if self._mode in ('new',):
			self._clear()
		
		self._cr.rollback()
		
		return ['rollbacked']
			
	def _post_diff(self,diffs,context):
		if '__o2m_append__' in diffs:
			apnds1 = diffs['__o2m_append__']
			for apnd1 in apnds1:
				m = self._pool.get(apnd1['__model__'])
				on_change_fields = list(filter(lambda x: x in m._on_change_fields and x is not None,apnd1['__data__'].keys()))
				ci = m.columnsInfo(columns=on_change_fields,attributes=['compute','priority'])
				priority = {}
				for on_change_field in on_change_fields:
					priority.setdefault(ci[on_change_field]['compute'],set()).add(on_change_field)
				
				pkeys = list(priority.keys())
				pkeys.sort()

				for pkey in pkeys:
					for on_change_field in priority[pkey]:
						self._on_change(apnd1['__path__'],apnd1['__model__'],on_change_field,context)
						self._do_calculate(apnd1['__path__'],context)
						diffs2 = self._data._odiffs()
						if len(diffs2) > 0:
							self._post_diff(diffs2,context)

		if '__insert__' in diffs:
			insts1 = diffs['__insert__']
			for inst1 in insts1.keys():
				model = self._data._cmodels[inst1]
				m = self._pool.get(model)
				on_change_fields = list(filter(lambda x: x in m._on_change_fields and x is not None,insts1[inst1].keys()))
				ci = m.columnsInfo(columns=on_change_fields,attributes=['compute','priority'])
				priority = {}
				for on_change_field in on_change_fields:
					priority.setdefault(ci[on_change_field]['compute'],set()).add(on_change_field)
				
				pkeys = list(priority.keys())
				pkeys.sort()

				for pkey in pkeys:
					for on_change_field in priority[pkey]:
						self._on_change(inst1,model,on_change_field,context)
						self._do_calculate(inst1,context)
						diffs2 = self._data._odiffs()
						if len(diffs2) > 0:
							self._post_diff(diffs2,context)

		if '__delete__' in diffs:
			insts1 = diffs['__delete__']
			for inst1 in insts1.keys():
				model = self._data._cmodels[inst1]
				m = self._pool.get(model)
				on_change_fields = list(filter(lambda x: x in m._on_change_fields and x is not None,insts1[inst1].keys()))
				ci = m.columnsInfo(columns=on_change_fields,attributes=['compute','priority'])
				priority = {}
				for on_change_field in on_change_fields:
					priority.setdefault(ci[on_change_field]['compute'],set()).add(on_change_field)
				
				pkeys = list(priority.keys())
				pkeys.sort()

				for pkey in pkeys:
					for on_change_field in priority[pkey]:
						self._on_change(inst1,model,on_change_field,context)
						self._do_calculate(inst1,context)
						diffs2 = self._data._odiffs()
						if len(diffs2) > 0:
							self._post_diff(diffs2,context)

	def _post_diffs(self,context):
		levels = {}
		diffs1 = self._data._odiffs(False)
		ch1 = DCacheDict(self._data._cdata[self._data._root],self._data._model,self._cr,self._pool,self._uid,self._context)

		self._post_diff(diffs1,context)
		diffs2 = ch1._pdiffs()
		
		_join_diffs(diffs1,diffs2)
		
		self._data._apply_from_diffs('o','c',diffs1)

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

