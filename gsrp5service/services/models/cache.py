import copy
import uuid
from decimal import Decimal
import datetime
import psycopg2
import ctypes
from gsrp5service.orm import gensql

def _join_levels(l1,l2):
	for k in l2.keys():
		l1.setdefault(k,set()).update(l2[k])

def _join_diffs(d1,d2):
	for k2 in d2.keys():
		if k2 in ('__update__','__insert__','__delete__'):
			d1[k2].update(d2[k2])
		elif k2 in ('__append__','__remove__'):
			d1[k2].extend(d2[k2])

class DictComp(dict):
	def __init__(self,data,primary=True):
		self.__shadow__ = {}
		if primary:
			self.__primary
		self.update(data)
		for key in data.keys():
			if type(data[key]) == dict:
				self.__shadow__[key] = DictComp(copy.deepcopy(data[key]))
			else:
				self.__shadow__[key] = copy.deepcopy(data[key])
	
	def _diff(self,commit = True):
		pass


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

	for nonefield in list(filter(lambda x: record[x] is None,fields)):
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
	
	def __init__(self,data,model,pool,primary=True):
		self._model = model
		self._pool =pool
		self._primary = primary

		for v in ('data','paths','r2c','containers','names','metas','models','rels'):
			for a in ('p','o','c'):
				if not primary and a == 'p':
					continue
				setattr(self,'_%s%s' % (a,v),{})

		self._buildTree(data,model)
		self._copyBuild()
		
	@property
	def _data(self):
		return self._cdata[self._root]
	
	def _buildTree(self,data,model,parent=None,name=None, mode = 'N'):
		if type(data) != dict:
			raise TypeError

		if model not in self._cmetas:
			self._cmetas[model] = self._pool.get(model).columnsInfo(attributes=['type','obj','rel','id1','id2'])
		
		ci = self._cmetas[model]
		oid = str(id(data))

		if mode == 'N' and not hasattr(self,'_root'):
			self._root = oid

		self._cdata[oid] = data
		self._cmodels[oid] = model
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
		#print('_m2m_buildTree:'.upper(),data,rel,parent,name)
		if type(data) == dict:
			cn = name + '.' + parent
			coid = self._cnames[cn]
			#self._ccontainers[coid] = cn
			#self._cnames[cn] = coid
			self._cdata[coid].append(data)
			self._crels[coid] = rel

			m2moid = str(id(data))
			self._cdata[m2moid] = data
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

#

	def _copyBuild(self):
		self._odata.update(copy.deepcopy(self._cdata))
		self._opaths.update(copy.deepcopy(self._cpaths))
		self._or2c.update(copy.deepcopy(self._cr2c))
		self._ocontainers.update(copy.deepcopy(self._ccontainers))
		self._onames.update(copy.deepcopy(self._cnames))
		self._ometas.update(copy.deepcopy(self._cmetas))
		self._omodels.update(copy.deepcopy(self._cmodels))
		self._orels.update(copy.deepcopy(self._crels))
		if self._primary:
			self._pdata.update(copy.deepcopy(self._cdata))
			self._ppaths.update(copy.deepcopy(self._cpaths))
			self._pr2c.update(copy.deepcopy(self._cr2c))
			self._pcontainers.update(copy.deepcopy(self._ccontainers))
			self._pnames.update(copy.deepcopy(self._cnames))
			self._pmetas.update(copy.deepcopy(self._cmetas))
			self._pmodels.update(copy.deepcopy(self._cmodels))		
			self._prels.update(copy.deepcopy(self._crels))

	def _diffs(self,o,c,commit):
		res = {}
		
		path = self._root
		res.update(self._cmpDict(o,c,path))

		if commit:
			self._apply_from_diffs(o,c,res)
		# if ('__update__' in res ):
			# if commit:
				# for k in res['__update__'].keys():
					# getattr(self,'_%sdata' % (o,))[k].update(copy.deepcopy(res['__update__'][k]))

		# if ('__insert__' in res ):
			# if commit:
				# for k in res['__insert__'].keys():
					# getattr(self,'_%sdata' % (c,))[k].update(copy.deepcopy(res['__insert__'][k]))

		# if ('__delete__' in res ):
			# if commit:
				# for k in res['__delete__'].keys():
					# for d in res['__delete__'][k].keys():
						# del getattr(self,'_%sdata' % (c,))[k][d]

		# if ('__o2m_append__' in res or '__m2m_append__' in res):
			# if commit:
				# for k in ('__o2m_append__','__m2m_append__'):
					# if k not in res:
						# continue
					# for r in res[k]:
						# container = r['__container__']
						# path = r['__path__']
						# model = r['__model__']
						# cdata = getattr(self,'_%sdata' % (c,))
						# odata = getattr(self,'_%sdata' % (o,))
						# cnames = getattr(self,'_%snames' % (c,))
						# onames = getattr(self,'_%snames' % (o,))
						# ccontainers = getattr(self,'_%scontainers' % (c,))
						# ocontainers = getattr(self,'_%scontainers' % (o,))
						
						# cmetas = getattr(self,'_%smetas' % (c,))
						# ometas = getattr(self,'_%smetas' % (o,))
						# cmodels = getattr(self,'_%smodels' % (c,))
						# omodels = getattr(self,'_%smodels' % (o,))
	
						# crels = getattr(self,'_%srels' % (c,))
						# orels = getattr(self,'_%srels' % (o,))
	
						# cpaths = getattr(self,'_%spaths' % (c,))
						# opaths = getattr(self,'_%spaths' % (o,))
						# cr2c = getattr(self,'_%sr2c' % (c,))
						# or2c = getattr(self,'_%sr2c' % (o,))
	
						# r1 = copy.deepcopy(r['__data__'])
						# odata.setdefault(cnames[container],[]).append(r1)
						# odata[path] = r1
						# onames[container] = cnames[container]
						# ocontainers[cnames[container]] = ccontainers[cnames[container]]
						# if k == '__o2m_append__':
							# ometas[model] = cmetas[model]
							# omodels[path] = cmodels[path] 
						# elif k == '__m2m_append__':
							# orels[path] = crels[path]
						# opaths[path] = cpaths[path]
						# or2c[path] = cr2c[path] 
						
						# if '__o2m_containers__' in r:
							# for ck in r['__o2m_containers__'].keys():
								# onames[ck + '.' + path] = cnames[ck + '.' + path]
								# ocontainers[cnames[ck + '.' + path]] = cnames[ck + '.' + path]
								# omodels[path] = cmodels[path]
								# ometas[omodels[path]] = cmetas[cmodels[path]]
								# or2c[path] = cr2c[path]
								# opaths[path] = cpaths[path]

						# if '__m2m_containers__' in r:
							# for ck in r['__m2m_containers__'].keys():
								# onames[ck + '.' + path] = cnames[ck + '.' + path]
								# ocontainers[cnames[ck + '.' + path]] = cnames[ck + '.' + path]
								# omodels[path] = cmodels[path]
								# orels[path] = crels[path]
								# or2c[path] = cr2c[path]
								# opaths[path] = cpaths[path]


		# if ('__o2m_remove__' in res or '__m2m_remove__' in res ):
			# if commit:
				# for k in ('__o2m_remove__','__m2m_remove__'):
					# if k not in res:
						# continue

					# for r in res[k]:
						# container = r['__container__']
						# path = r['__path__']
						# model = r['__model__']
						# cdata = getattr(self,'_%sdata' % (c,))
						# odata = getattr(self,'_%sdata' % (o,))
						# cnames = getattr(self,'_%snames' % (c,))
						# onames = getattr(self,'_%snames' % (o,))
						# ccontainers = getattr(self,'_%scontainers' % (c,))
						# ocontainers = getattr(self,'_%scontainers' % (o,))
						
						# cmetas = getattr(self,'_%smetas' % (c,))
						# ometas = getattr(self,'_%smetas' % (o,))
						# cmodels = getattr(self,'_%smodels' % (c,))
						# omodels = getattr(self,'_%smodels' % (o,))

						# crels = getattr(self,'_%srels' % (c,))
						# orels = getattr(self,'_%srels' % (o,))

						# cpaths = getattr(self,'_%spaths' % (c,))
						# opaths = getattr(self,'_%spaths' % (o,))
						# cr2c = getattr(self,'_%sr2c' % (c,))
						# or2c = getattr(self,'_%sr2c' % (o,))
	
						# odata[onames[container]].remove(odata[path])
						# del odata[path]
	
						# if container in cnames and cnames[container] in cdata and len(cdata[cnames[container]]) == 0:
							# del cdata[onames[container]]
							# del ccontainers[cnames[container]]
							# del cnames[container]
							
	
						# if len(odata[onames[container]]) == 0:
							# del odata[onames[container]]
							# del ocontainers[onames[container]]
							# del onames[container]
	
						
						# #del cmetas[model]
						# #del ometas[model]
						
						
						# if path in cmodels:
							# del cmodels[path] 
						# if path in omodels:
							# del omodels[path] 
						
						# if path in cpaths:
							# del cpaths[path]
						# if path in opaths:
							# del opaths[path]
						
						# if path in cr2c:
							# del cr2c[path] 
						# if path in cr2c:
							# del or2c[path]

		return res


	def _apply_from_diffs(self,o,c,diffs):
		if ('__update__' in diffs ):
			for k in diffs['__update__'].keys():
				getattr(self,'_%sdata' % (o,))[k].update(copy.deepcopy(diffs['__update__'][k]))

		if ('__insert__' in diffs ):
			for k in diffs['__insert__'].keys():
				getattr(self,'_%sdata' % (c,))[k].update(copy.deepcopy(diffs['__insert__'][k]))

		if ('__delete__' in diffs ):
			for k in diffs['__delete__'].keys():
				for d in diffs['__delete__'][k].keys():
					del getattr(self,'_%sdata' % (c,))[k][d]

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

					r1 = copy.deepcopy(r['__data__'])
					odata.setdefault(cnames[container],[]).append(r1)
					odata[path] = r1
					onames[container] = cnames[container]
					ocontainers[cnames[container]] = ccontainers[cnames[container]]
					if k == '__o2m_append__':
						ometas[model] = cmetas[model]
						omodels[path] = cmodels[path] 
					elif k == '__m2m_append__':
						orels[path] = crels[path]
					opaths[path] = cpaths[path]
					or2c[path] = cr2c[path] 
					
					if '__o2m_containers__' in r:
						for ck in r['__o2m_containers__'].keys():
							onames[ck + '.' + path] = cnames[ck + '.' + path]
							ocontainers[cnames[ck + '.' + path]] = cnames[ck + '.' + path]
							omodels[path] = cmodels[path]
							ometas[omodels[path]] = cmetas[cmodels[path]]
							or2c[path] = cr2c[path]
							opaths[path] = cpaths[path]

					if '__m2m_containers__' in r:
						for ck in r['__m2m_containers__'].keys():
							onames[ck + '.' + path] = cnames[ck + '.' + path]
							ocontainers[cnames[ck + '.' + path]] = cnames[ck + '.' + path]
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

					odata[onames[container]].remove(odata[path])
					del odata[path]

					if container in cnames and cnames[container] in cdata and len(cdata[cnames[container]]) == 0:
						del cdata[onames[container]]
						del ccontainers[cnames[container]]
						del cnames[container]
						

					if len(odata[onames[container]]) == 0:
						del odata[onames[container]]
						del ocontainers[onames[container]]
						del onames[container]

					
					#del cmetas[model]
					#del ometas[model]
					
					
					if path in cmodels:
						del cmodels[path] 
					if path in omodels:
						del omodels[path] 
					
					if path in cpaths:
						del cpaths[path]
					if path in opaths:
						del opaths[path]
					
					if path in cr2c:
						del cr2c[path] 
					if path in cr2c:
						del or2c[path]

		return True

	def _cmpDict(self,o,c,path):
		res = {}
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
	
		return res

	def _o2m_cmpList(self,o,c,container):
		res = {}

		cdata = getattr(self,'_%snames' % (c,))
		odata = getattr(self,'_%snames' % (o,))

		coid = None
		ooid = None
		ok = None
		ck = None
		ik = None
		uk = None
		dk = None

		if container in cdata:
			coid = cdata[container]

		if container in odata:
			ooid = odata[container]

		#if len(self._cdata[coid]) >= 0:					
		if ooid:
			ok = list(map(lambda y:y[0],filter(lambda x: x[1] == ooid,getattr(self,'_%sr2c' % (o,)).items())))
		else:
			ok = []

		if coid:
			ck = list(map(lambda x: str(id(x)),getattr(self,'_%sdata' % (c,))[coid]))
		else:
			ck = []

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
		for i in ik:
			d1 = ctypes.cast(int(i), ctypes.py_object).value
			p=container.split('.')
			model = getattr(self,'_%smodels' % (c,))[coid]
			self._buildTree(d1,model,p[1],p[0],'I')
			ci = getattr(self,'_%smetas' % (c,))[model]

			data = {}

			for v in filter(lambda x: x != 'id' and ci[x]['type'] != 'many2many',getattr(self,'_%sdata' % (c,))[i].keys()):
				data[v] = getattr(self,'_%sdata' % (c,))[i][v]

			container = self._ccontainers[getattr(self,'_%sr2c' % (c,))[i]]
			m2m_containers = {}
			for k in filter(lambda x: x != 'id ' and ci[x]['type'] == 'many2many',getattr(self,'_%sdata' % (c,))[i].keys()):
				r1 = self._m2m_cmpList(o,c,k + '.' + i)
				m2m_containers.setdefault(k,[]).extend(r1['__m2m_append__'] if '__m2m_append__' in r1 else [])
				
			res.setdefault('__m2m_append__',[]).append({'__path__':i,'__container__':container,'__model__':model,'__data__':data,'__containers__':m2m_containers})

			for v in filter(lambda x: x != 'id' and ci[x]['type'] != 'one2many',getattr(self,'_%sdata' % (c,))[i].keys()):
				data[v] = getattr(self,'_%sdata' % (c,))[i][v]

			container = self._ccontainers[getattr(self,'_%sr2c' % (c,))[i]]
			o2m_containers = {}
			for k in filter(lambda x: x != 'id ' and ci[x]['type'] == 'one2many',getattr(self,'_%sdata' % (c,))[i].keys()):
				r1 = self._o2m_cmpList(o,c,k + '.' + i)
				o2m_containers.setdefault(k,[]).extend(r1['__o2m_append__'] if '__o2m_append__' in r1 else [])
				
			res.setdefault('__o2m_append__',[]).append({'__path__':i,'__container__':container,'__model__':model,'__data__':data,'__containers__':o2m_containers})


	
		for d in dk:
			model = getattr(self,'_%smodels' % (o,))[d]
			ci = getattr(self,'_%smetas' % (o,))[model]

			container = getattr(self,'_%scontainers' % (o,))[getattr(self,'_%sr2c' % (o,))[d]]
			
			cr2c = getattr(self,'_%sr2c' % (o,))
			
			data = getattr(self,'_%sdata' % (o,))[d]
			
			names = getattr(self,'_%snames' % (o,))
				
			for o2mfield in self._pool.get(model)._o2mfields:
				container1 = o2mfield + '.' + str(d)
				
				for path in filter(lambda x:cr2c[x] == names[container1],cr2c.keys()):
					res.setdefault('__o2m_remove__',[]).extend(self._removeRecursive(o,c,path))
			
			res.setdefault('__o2m_remove__',[]).append({'__path__':d,'__container__':container,'__model__':model,'__data__':data})
				

		return res

# mamy2many
	def _m2m_cmpList(self,o,c,container):
		res = {}

		cdata = getattr(self,'_%snames' % (c,))
		odata = getattr(self,'_%snames' % (o,))

		coid = None
		ooid = None
		ok = None
		ck = None
		ik = None
		dk = None

		if container in cdata:
			coid = cdata[container]

		if container in odata:
			ooid = odata[container]
					
		if ooid:
			ok = list(map(lambda y:y[0],filter(lambda x: x[1] == ooid,getattr(self,'_%sr2c' % (o,)).items())))
		else:
			ok = []

		if coid:
			ck = list(map(lambda x: str(id(x)),getattr(self,'_%sdata' % (c,))[coid]))
		else:
			ck = []

		ik = list(set(ck)- set(ok))
		dk = list(set(ok)- set(ck))
		
		#print('M2M-CMPLIST:',container,ooid,coid,ok,ck,ik,dk)
			
		for i in ik:
			d1 = ctypes.cast(int(i), ctypes.py_object).value
			p=container.split('.')

			model = getattr(self,'_%smodels' % (c,))[i]
			rel = getattr(self,'_%srels' % (c,))[i]
			self._m2m_buildTree(d1,rel,p[1],p[0],model)
				
			res.setdefault('__m2m_append__',[]).append({'__path__':i,'__container__':container,'__model__':model,'__rel__':rel,'__data__':d1})
	
		for d in dk:
			d1 = getattr(self,'_%sdata' % (o,))[d]
			model = getattr(self,'_%smodels' % (o,))[d]
			rel = getattr(self,'_%srels' % (o,))[d]			
			res.setdefault('__m2m_remove__',[]).append({'__path__':d,'__container__':container,'__model__':model,'__rel__':rel,'__data__':d1})
				

		return res

# many 2 many

	def _removeRecursive(self,o,c,path):
		res = []
		model = getattr(self,'_%smodels' % (o,))[path]
		container = getattr(self,'_%scontainers' % (o,))[getattr(self,'_%sr2c' % (o,))[path]]

		for o2mfield in self._pool.get(model)._o2mfields:
			container1 = o2mfield + '.' + str(path)
			ooid = getattr(self,'_%snames' % (o,))[container1]
			obj = getattr(self,'_%smetas' % (o,))[model][o2mfield]['obj']
			odata = getattr(self,'_%sdata' % (o,))
			for r in odata[ooid]:
				path1 = str(id(r))
				res.extend(self._removeRecursive(o,c,path1))
				odata[ooid].remove(self._cdata[path1])
				data = copy.deepcopy(odata[path1])
				del odata[path1]
				res.append({'__path__':path1,'__container__':container1,'__model__':obj,'__data__':data})
			
		res.append({'__path__':path,'__container__':container,'__model__':model,'__data__':data})		
		
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
		
		res = {'__path__':path,'__data__':data,'__model__':model}
		if container:
			res['__container__'] = container
		
		if len(o2m_containers) > 0:
			res['__o2m_containers__'] = o2m_containers

		if len(m2m_containers) > 0:
			res['__m2m_containers__'] = m2m_containers


		return res

	def _get_o2mDataContainers(self,container):
		res = []

		for r in self._cdata[self._cnames[container]]:
			res.append(self._getData(r))
			
		return res

	def _get_m2mDataContainers(self,container,oid):
		res = []
		
		for r in self._cdata[self._cnames[container]]:
			res.append({'__container__':container,'__path__':str(id(r)),'__parent__':container.split('.')[1],'__data__':r})
			
		return res

			
class MCache(object):
	
	def __init__(self,cr,pool,uid,mode,context):
		self._cr = cr
		self._pool = pool
		self._uid = uid
		self._context = context
		self._mode = mode

		self._mdata = {}
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
		#row = self._buildItem(model,view)
		row = self._pool.get(model)._buildEmptyItem()
		self._setDefault(model,row)
		self._data = DCacheDict(row,model,self._pool,False)
		
		self._do_calculate(self._data._root,context=context)
		self._getMeta()	
		m = self._data._getData(self._data._data)
		m['__meta__'] = self._do_meta(str(self._data._root))
		m['__checks__'] = []
		return m

	def _readNodes(self,model,row):
		schema = self._pool.get(model)._schema1
		q = []
		print('SCHEMA:',model,schema)
		for k in schema[0].keys():
			parent = schema[0][k]
			print('PARENT:',parent)
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
		print('NODES:',nodes)
		for oid,model in nodes:
			print('OID:',oid,model)
			m = self._pool.get(model)
			cols = m._buildSchemaColumns(self._pool)
			d = m.read(self._cr,self._pool,self._uid,oid,cols,self._context)
			res[model] = d
		
		return res

	def _do_create(self,model,context={}):
		self._clear()
		self._model = model
		row = self._pool.get(model)._buildEmptyItem()
		self._setDefault(model,row)
		self._data = DCacheDict({},model,self._pool)
		self._data._buildTree(row,model,mode='A')
		self._do_calculate(self._data._root,context=self._context)
		self._getMeta()	
		m = self._data._getData(self._data._data)
		m['__meta__'] = self._do_meta(str(self._data._root))
		m['__checks__'] = []
		return m

	def _do_read(self,model,row):
		#v = self._readSchema(model,row)
		#print('READ-SCHEMA:',row)
		self._clear()
		self._model = model
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

		return res

	def _do_meta(self,path):
		res = {}

		while True:
			model = self._data._cmodels[path]
			m = self._pool.get(model)

			if type(m._attrs) == dict:
				if len(m._attrs) > 0:
					res.setdefault(model,{})['m'] = m._attrs
			elif type(m._attrs) == str:
				method = getattr(m,m._attrs,None)
				if method:
					rc = method(self._cr,self._pool,self._uid,self._data[path],self._context)
					if rc and len(rc) > 0:
						res.setdefault(model,{}).setdefault('m',{}).update(rc)

			if model not in self._meta:
				self._getMeta(model)

			cols = self._meta[model]
			for a in ('readonly','invisible','required'):
				k = list(filter(lambda x:cols[x]['type'] != 'referenced' and type(cols[x][a]) == str,cols.keys()))
				v = list(map(lambda x: cols[x][a],k))
				for v1 in v:
					method = getattr(m,v1,None)
					if method:
						rc = method(self._cr,self._pool,self._uid,k,self._data._cdata[path],self._context)
						if rc and len(rc) > 0:
							for k1 in rc.keys():
								if a == 'readonly':
									res.setdefault(model,{}).setdefault('c',{}).setdefault(k1,{})['ro'] = rc[k1]
								elif a == 'required':
									res.setdefault(model,{}).setdefault('c',{}).setdefault(k1,{})['rq'] = rc[k1]
								elif a == 'invisible':
									res.setdefault(model,{}).setdefault('c',{}).setdefault(k1,{})['iv'] = rc[k1]
						
			for key in self._meta[model].keys():
				column = self._meta[model][key]
				if type(m._col_attrs) == dict:
					if len(m._col_attrs) > 0:
						res.setdefault(model,{})['c'] = m._col_attrs
				elif type(m._col_attrs) == str:
					res.setdefault(model,{})['c'] = getattr(m,m._col_attrs,None)(self._cr,self._pool,self._uid,self._data._cdata[path],self._context)
					if len(res['c']) == 0:
						del res['c']

				if 'state' in column:
					state = column['state']
					state_name = m._getStateName()
					if state and state_name:
						for k in state.keys():
							if path in self._data._cdata and state_name in self._data._cdata[path]:
								if k != self._data._cdata[path][state_name]:
									continue
							else:
								continue
							attrs = state[k]['attrs']
							for k1 in attrs.keys():
								if k1 == 'ro' and type(cols[key]['readonly']) != bool or k1 == 're' and type(cols[key]['required']) != bool or k1 == 'iv' and type(cols[key]['invisible']) != bool:
									res.setdefault(model,{}).setdefault('c',{}).setdefault(key,{})[k1] = attrs[k1]

					if 'readonly' in column and type(column['readonly']) == bool:
						res.setdefault(model,{}).setdefault('c',{}).setdefault('ro',{})[key] = column['readonly']

					if 'required' in column and type(column['required']) == bool:
						res.setdefault(model,{}).setdefault('c',{}).setdefault('rq',{})[key] = column['required']

					if 'invisible' in column and type(column['invisible']) == bool:
						res.setdefault(model,{}).setdefault('c',{}).setdefault('iv',{})[key] = column['invisible']
				
					if model in res and 'c' in res[model] and len(res[model]['c']) == 0:
						del res[model]['c']

					if model in res and 'm' in res[model] and len(res[model]['m']) == 0:
						del res[model]['m']

			if self._data._cpaths[path]:
				parents = self._data._cpaths[path]
				for key in parents.keys():
					path = parents[key]
			else:
				break

		self._mdata = res
		
		return res

	def _do_compute(self, path, model):
		res = {}
		m = self._pool.get(model)
		record = self._data._cdata[path]
		fields = list(record.keys())
		ci = m.columnsInfo(columns=m._computefields,attributes=['compute','priority'])
		priority = {}
		for compute_field in filter(lambda x: x in fields,m._computefields):
			priority.setdefault(ci[compute_field]['compute'],set()).add(compute_field)
		
		pkeys = list(priority.keys())
		pkeys.sort()
		for pkey in pkeys:
			for compute_field in priority[pkey]:
				method = getattr(m,ci[compute_field]['compute'],None)
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
		#row = self._buildItem(model,view)
		row = self._pool.get(model)._buildEmptyItem()
		self._setDefault(model,row)
		
		p = container.split('.')
		self._data._cdata[self._data._cnames[container]].append(row)
		self._data._buildTree(row,model,p[1],p[0],'A')
		
		self._do_calculate(str(id(row)),context)
		
		res = {}

		data_diffs = self._data._odiffs(True)
		
		if len(data_diffs) > 0:
			res['__data__'] = data_diffs

		meta = self._do_meta(str(id(row)))
		if len(meta) > 0:
			res['__meta__'] = meta
		
		if len(self._checks) > 0:
			res['__checks__'] = copy.deepcopy(self._checks)
			self._checks.clear()

		if len(res) > 0:
			return [res]
		
		return []
			
	def _o2m_remove(self,path,container,context):
		print('O2M-CACHE-REMOVE:',path,container)
		c = container.split('.')
		self._data._cdata[self._data._cnames[container]].remove(self._data._cdata[path])
		del self._data._cdata[path]
		
		self._do_calculate(c[1],context)
		
		res = {}

		data_diffs = self._data._odiffs(True)

		if len(data_diffs) > 0:
			res['__data__'] = data_diffs
		
		meta = self._do_meta(c[1])
		if len(meta) > 0:
			res['__meta__'] = meta
		
		if len(self._checks) > 0:
			res['__checks__'] = copy.deepcopy(self._checks)
			self._checks.clear()

		if len(res) > 0:
			return [res]
		
		return []

	def _m2m_add(self,model,container,fields,obj,rel,id1,id2,context={}):
		
		rows = self._pool.get(obj).read(self._cr,self._pool,self._uid,id2,fields,self._context)
		#print('M2M-CACHE-ADD:',model,container,fields,obj,rel,id1,id2,rows)
		
		p = container.split('.')
		if len(rows) > 0:
			for row in rows:
				if container not in self._data._cnames:
					cc = []
					coid = str(id(cc))
					self._data._ccontainers[coid] = container
					self._data._cnames[container] = coid
					self._data._cdata[coid] = cc

				self._data._cdata[self._data._cnames[container]].append(row)
				self._data._m2m_buildTree(row,rel,p[1],p[0],model)
				
		res = {}

		data_diffs = self._data._odiffs(True)
		
		if len(data_diffs) > 0:
			res['__data__'] = data_diffs

		if len(res) > 0:
			return [res]
		
		return []

	def _m2m_remove(self,path,container,context):
		c = container.split('.')
		self._data._cdata[self._data._cnames[container]].remove(self._data._cdata[path])
		del self._data._cdata[path]

		res = {}

		data_diffs = self._data._odiffs(True)

		print('M2M-CACHE-REMOVE:',path,container,data_diffs)
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
		act = self._pool.get(self._data[path]._model).do_action(self._cr,self._pool,self._uid,name,column,self._oids[path].__shadow__,context)
		if act and len(act) > 0:
			res['__do_action__'] = act
		else:
			res['__do_action__'] = []

		self._diff(path,context)

		meta = self._do_meta(path)
		
		if len(self._diffs) > 0:
			res['__data__'] = copy.deepcopy(self._diffs)
			self._diffs.clear()

		if len(self._checks) > 0:
			res['__checks__'] = copy.deepcopy(self._checks)
			self._checks.clear()

		
		if len(meta) > 0:
			res['__meta__'] = meta

		if len(res) > 0:
			return [res]
		
		return []

	def _save(self,autocommit = False):
		diffs = self._data._pdiffs(False)
		#print('DIFFS:',diffs)
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
			if m._columns[k]._type in ('many2one','related'):
				data[k] = item['__data__'][k]['id']
			elif k == rel:
				data[rel] = {'id':oid,'name':recname}

		r = _createRecord(m,self._cr,self._pool,self._uid,data,self._context)

		if len(r) > 0:
			item['__data__']['id'] = r[0]
		
		if '__m2m_containers__' in item:
			m2m_containers = item['__m2m_containers__']
			for key in m2m_containers.keys():
				self._m2m_appendRows(m2m_containers[key])

		if '__o2m_containers__' in item:
			containers = item['__o2m_containers__']
			for key in containers.keys():
				self._createItems(containers[key],self._pool.get(model)._columns[key].rel,item['__data__']['id'])

	def _o2m_appendItems(self,items):
		for item in items:
			self._o2m_appendItem(item)

	def _o2m_appendItem(self,item):
		print('ITEM:',item)
		data = {}
		model = item['__model__']
		container = item['__container__']
		cn,parent = container.split('.')
		oid = self._data._cdata[parent]['id']
		rel = self._pool.get(self._data._cmodels[parent])._columns[cn].rel
		recname = self._pool.get(self._data._cmodels[parent])._getRecNameName()
		data[rel] = {'id':oid,'name':recname}
		m = self._pool.get(model)
		excl_fields = m._o2mfields + m._m2mfields
		for k in filter(lambda x: x not in excl_fields,item['__data__'].keys()):
			if m._columns[k]._type in ('many2one','related'):
				data[k] = item['__data__'][k]['id']
		
		print('DATA:',data)
		r = _createRecord(m,self._cr,self._pool,self._uid,data,self._context)
		if len(r) > 0:
			item['__data__']['id'] = r[0]
		if '__o2m_containers__' in item:
			o2m_containers = item['__o2m_containers__']
			for key in o2m_containers.keys():
				self._o2m_appendItems(o2m_containers[key])

	def _o2m_removeItems(self,items):
		for item in items:
			self._o2m_removeItem(item)

	def _o2m_removeItem(self,item):
		container = item['__container__']
		path = item['__path__']
		model = item['__model__']
		data = item['__data__']
		if 'id' in data:
			oid = data['id']
			m = self._pool.get(model)
			r = m.unlink(self._cr,self._pool,self._uid,oid,self._context)

	def _m2m_appendRows(self,rows):
		rels = []
		cols = {}
		for row in rows:
			m = self._pool.get(row['__model__'])
			c = row['__container__'].split('.')
			oid = self._data._cdata[c[1]]['id']
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
			print('row:',row,oid)
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
				for k in models[model][mkey].keys():
					if m._columns[k]._type in ('many2one','related'):
						models[model][mkey][k] = data[k]['id']
			
				if 'id' in self._data._cdata[mkey]:
					models[model][mkey]['id'] = self._data._cdata[mkey]['id']
					r = m.write(self._cr,self._pool,self._uid,models[model][mkey],self._context)
				else:
					r = m.create(self._cr,self._pool,self._uid,models[model][mkey],self._context)

	def _reset(self):
		#diffs = self._data._pdiffs()
		
		self._roolback()


	def _commit(self,action='commit work'):
		if self._mode in ('new',):
			self._clear()
		
		self._cr.commit()
		
		if self._data._apply_from_diffs('p','c',self._commit_diffs):
			return ['commited']
		
		return ['not commited']
		

	def _rollback(self):
		if self._mode in ('new',):
			self._clear()
		
		self._cr.rollback()
		
		return ['rollbacked']
			
	def _post_diff(self,diffs,context):
		if '__append__' in diffs:
			apnds1 = diffs['__append__']
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
			for inst1 in insts1:
				m = self._pool.get(inst1['__model__'])
				on_change_fields = list(filter(lambda x: x in m._on_change_fields and x is not None,inst1['__data__'].keys()))
				ci = m.columnsInfo(columns=on_change_fields,attributes=['compute','priority'])
				priority = {}
				for on_change_field in on_change_fields:
					priority.setdefault(ci[on_change_field]['compute'],set()).add(on_change_field)
				
				pkeys = list(priority.keys())
				pkeys.sort()

				for pkey in pkeys:
					for on_change_field in priority[pkey]:
						self._on_change(inst1['__path__'],apnd1['__model__'],on_change_field,context)
						self._do_calculate(apnd1['__path__'],context)
						diffs2 = self._data._odiffs()
						if len(diffs2) > 0:
							self._post_diff(diffs2,context)

	def _post_diffs(self,context):
		levels = {}
		diffs1 = self._data._odiffs()
		ch1 = DCacheDict(self._data._cdata[self._data._root],self._data._model,self._data._pool)

		self._post_diff(diffs1,context)
		diffs2 = ch1._pdiffs()

		_join_diffs(diffs1,diffs2)

		return eval(str(diffs1))

	def _mcache(self,path,key=None,value=None,context={}):
		res = {}

		self._do_diff(path,key,value,context)
		self._diffs = self._post_diffs(context)
		meta = self._do_meta(path)

		if len(self._diffs) > 0:
			res['__data__'] = copy.deepcopy(self._diffs)
			self._diffs.clear()

		if len(self._checks) > 0:
			res['__checks__'] = copy.deepcopy(self._checks)
			self._checks.clear()

		
		if len(meta) > 0:
			res['__meta__'] = meta

		if len(res) > 0:
			return [res]
		
		return []

