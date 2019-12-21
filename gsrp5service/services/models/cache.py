import copy
import uuid
from decimal import Decimal
import datetime
import psycopg2


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
		#self._root = str(id(self._data))
		self._model = model
		self._pool =pool
		self._primary = primary

		for v in ('data','paths','r2c','containers','names','metas','models'):
			for a in ('p','o','c'):
				if not primary and a == 'p':
					continue
				setattr(self,'_%s%s' % (a,v),{})

		self._buildTree(data,model)
		#print('CDATA:',self._cdata)
		self._copyBuild()
		
	@property
	def _data(self):
		return self._cdata[self._root]
	
	def _buildTree(self,data,model,parent=None,name=None, mode = 'N'):
		if model not in self._cmetas:
			self._cmetas[model] = self._pool.get(model).columnsInfo(attributes=['type','obj'])
		
		ci = self._cmetas[model]
		oid = str(id(data))

		if not hasattr(self,'_root'):
			self._root = oid

		self._cdata[oid] = data
		self._cmodels[oid] = model
		if parent and name:
			if mode == 'A':
				self._cdata[self._cnames[name + '.' + str(parent)]].append(data)

			self._cpaths[oid] = parent
			self._cr2c[oid] = self._cnames[name + '.' + str(parent)]
		else:
			self._cpaths[oid] = None
		
		for o2mfield in self._pool.get(model)._o2mfields:
			cn = o2mfield + '.' + oid
			coid = str(id(data[o2mfield]))
			self._ccontainers[coid] = cn
			self._cnames[cn] = coid
			self._cdata[coid] = data[o2mfield]
			self._cmodels[coid] = ci[o2mfield]['obj']
			if mode == 'A':
				print('O2MFILED:',o2mfield,oid,cn,coid) 

			for r1 in data[o2mfield]:
				self._buildTree(r1,ci[o2mfield]['obj'],oid,o2mfield,mode)

	def _copyBuild(self):
		self._odata.update(copy.deepcopy(self._cdata))
		self._opaths.update(copy.deepcopy(self._cpaths))
		self._or2c.update(copy.deepcopy(self._cr2c))
		self._ocontainers.update(copy.deepcopy(self._ccontainers))
		self._onames.update(copy.deepcopy(self._cnames))
		self._ometas.update(copy.deepcopy(self._cmetas))
		self._omodels.update(copy.deepcopy(self._cmodels))
		if self._primary:
			self._pdata.update(copy.deepcopy(self._cdata))
			self._ppaths.update(copy.deepcopy(self._cpaths))
			self._pr2c.update(copy.deepcopy(self._cr2c))
			self._pcontainers.update(copy.deepcopy(self._ccontainers))
			self._pnames.update(copy.deepcopy(self._cnames))
			self._pmetas.update(copy.deepcopy(self._cmetas))
			self._pmodels.update(copy.deepcopy(self._cmodels))		

	def _diffs(self,o,c,commit):
		res = {}

		path = self._root
		res.update(self._cmpDict(o,c,path))

		#print('RES:',res)

		if ('__update__' in res ):
			if commit:
				for k in res['__update__'].keys():
					getattr(self,'_%sdata' % (o,))[k].update(copy.deepcopy(res['__update__'][k]))

		if ('__insert__' in res ):
			if commit:
				for k in res['__insert__'].keys():
					getattr(self,'_%sdata' % (c,))[k].update(copy.deepcopy(res['__insert__'][k]))

		if ('__delete__' in res ):
			if commit:
				for k in res['__delete__'].keys():
					for d in res['__delete__'][k].keys():
						del getattr(self,'_%sdata' % (c,))[k][d]


		if ('__append__' in res ):
			if commit:
				for r in res['__append__']:
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
					cpaths = getattr(self,'_%spaths' % (c,))
					opaths = getattr(self,'_%spaths' % (o,))
					cr2c = getattr(self,'_%sr2c' % (c,))
					or2c = getattr(self,'_%sr2c' % (o,))

					r1 = copy.deepcopy(r['__data__'])
					odata.setdefault(cnames[container],[]).append(r1)
					odata[path] = r1
					onames[container] = cnames[container]
					ocontainers[cnames[container]] = ccontainers[cnames[container]]
					ometas[model] = cmetas[model]
					omodels[path] = cmodels[path] 
					opaths[path] = cpaths[path]
					or2c[path] = cr2c[path] 
					
					
					for c in r['__containers__'].keys():
						onames[c + '.' + path] = cnames[c + '.' + path]
						ocontainers[cnames[c + '.' + path]] = cnames[c + '.' + path]
						omodels[path] = cmodels[path]
						ometas[omodels[path]] = cmetas[cmodels[path]]
						or2c[path] = cr2c[path]
						opaths[path] = cpaths[path]
						
						

		if ('__remove__' in res ):
			res['__remove__'] = list(reversed(res['__remove__']))
			#print('__remove__:',res['__remove__'])
			if commit:
				for r in res['__remove__']:
					container = r['__container__']
					path = r['__path__']
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
					cpaths = getattr(self,'_%spaths' % (c,))
					opaths = getattr(self,'_%spaths' % (o,))
					cr2c = getattr(self,'_%sr2c' % (c,))
					or2c = getattr(self,'_%sr2c' % (o,))

					i = -1
					for idx,v in enumerate(odata[cnames[container]]):
						if str(id(v)) == path:
							i = idx
					if i >= 0:
						odata[cnames[container]].pop(i)
					del odata[path]
					
					if len(odata[cnames[container]]) == 0:
						del odata[cnames[container]]

					for c in r['__containers__'].keys():
						
						del ocontainers[onames[c + '.' + path]]
						del onames[c + '.' + path]
						del ometas[omodels[path]]
						del omodels[path]
						del or2c[path]
						del opaths[path]

						del ccontainers[cnames[c + '.' + path]]
						del cnames[c + '.' + path]
						del cmetas[cmodels[path]]
						del cmodels[path]
						del cr2c[path]
						del cpaths[path]


		return res

	def _cmpDict(self,o,c,path):
		res = {}
		ci = self._cmetas[self._cmodels[path]]
		
		ck = list(filter(lambda x: x != 'id' and ci[x]['type'] !='one2many',getattr(self,'_%sdata' % (c,))[path].keys()))
		#try:
		ok = []
		if path in getattr(self,'_%sdata' % (o,)):
			rr = getattr(self,'_%sdata' % (o,))[path]
			#print('RR:',rr)
			if type(rr) in (list,tuple):
				coid = str(id(rr))
				print('RR:',coid,self._ccontainers)
				print('RR-DATA:',coid,rr)
				container = self._ccontainers[coid]			
				v = self._cmpList(o,c,container)
				if '__append__' in v:			
					res.setdefault('__append__',[]).extend(v['__append__'])
				if '__remove__' in v:
					res.setdefault('__remove__',[]).extend(v['__remove__'])
				if '__update__' in v:
					res.setdefault('__update__',{}).update(v['__update__'])
				if '__insert__' in v:
					res.setdefault('__insert__',{}).update(v['__insert__'])
				if '__delete__' in v:
					res.setdefault('__delete__',{}).update(v['__delete__'])

			elif type(rr) == dict:
				ok = list(filter(lambda x: x != 'id' and ci[x]['type'] !='one2many',rr.keys()))
		#except:
			#print('EXCEPT:',path,getattr(self,'_%sdata' % (o,))[path])
		uk = list(set(ok).intersection(set(ck)))
		ik = list(set(ck)- set(ok))
		dk = list(set(ok)- set(ck))

		
		for k in filter(lambda x: x != 'id',getattr(self,'_%sdata' % (c,))[path].keys()):
			if ci[k]['type'] == 'one2many':
				#print('CMP-LIST:',self._cdata[path])
				v = self._cmpList(o,c,k + '.' + path)
				#print('CDIFFS:', k + '.' + path,v)
				if '__append__' in v:			
					res.setdefault('__append__',[]).extend(v['__append__'])
				if '__remove__' in v:
					res.setdefault('__remove__',[]).extend(v['__remove__'])
				if '__update__' in v:
					res.setdefault('__update__',{}).update(v['__update__'])
				if '__insert__' in v:
					res.setdefault('__insert__',{}).update(v['__insert__'])
				if '__delete__' in v:
					res.setdefault('__delete__',{}).update(v['__delete__'])

			else:
				if k in uk and getattr(self,'_%sdata' % (c,))[path][k] != getattr(self,'_%sdata' % (o,))[path][k]:
					res.setdefault('__update__',{}).setdefault(path,{})[k] = getattr(self,'_%sdata' % (c,))[path][k]
				elif k in ik:
					res.setdefault('__insert__',{}).setdefault(path,{})[k] = getattr(self,'_%sdata' % (c,))[path][k]
				elif k in dk:
					res.setdefault('__delete__',{}).setdefault(path,[]).append(k)
		
		#print('res-dict:',path,res)
		return res

	def _cmpList(self,o,c,container):
		res = {}

		coid = getattr(self,'_%snames' % (c,))[container]
		
		if len(self._cdata[coid]) > 0:					
			ok = list(map(lambda y:y[0],filter(lambda x: x[1] == coid,getattr(self,'_%sr2c' % (o,)).items())))
			ck = list(map(lambda x: str(id(x)),getattr(self,'_%sdata' % (c,))[coid]))
			uk = list(set(ok).intersection(set(ck)))
			ik = list(set(ck)- set(ok))
			dk = list(set(ok)- set(ck))
			#print('OK:',container,ok,ck,uk,ik,dk)
				
			for path in uk:
				if not path in getattr(self,'_%sdata' % (c,)):
					dk.append(path)
					continue
				#print('CMP-DICT:',self._cdata[path])
				v = self._cmpDict(o,c,path)
				if '__update__' in v:
					res.setdefault('__update__',{}).update(v['__update__'])
				if '__insert__' in v:
					res.setdefault('__insert__',{}).update(v['__insert__'])
				if '__delete__' in v:
					res.setdefault('__delete__',{}).update(v['__delete__'])
				if '__append__' in v:
					res.setdefault('__append__',[]).extend(v['__append__'])
				if '__remove__' in v:
					res.setdefault('__remove__',[]).extend(v['__remove__'])
			for i in ik:
				model = getattr(self,'_%smodels' % (c,))[i]
				ci = getattr(self,'_%smetas' % (c,))[model]

				data = {}
				for v in filter(lambda x: x != 'id' and ci[x]['type'] != 'one2many',getattr(self,'_%sdata' % (c,))[i].keys()):
					data[v] = getattr(self,'_%sdata' % (c,))[i][v]

				container = self._ccontainers[getattr(self,'_%sr2c' % (c,))[i]]
				containers = {}
				for k in filter(lambda x: x != 'id ' and ci[x]['type'] == 'one2many',getattr(self,'_%sdata' % (c,))[i].keys()):
					containers[k] = []
	
				res.setdefault('__append__',[]).append({'__path__':i,'__container__':container,'__model__':model,'__data__':data,'__containers__':containers})
		
			for d in dk:
				#print('DD:',d,dk)
				model = getattr(self,'_%smodels' % (c,))[d]
				ci = getattr(self,'_%smetas' % (c,))[model]

				container = self._ccontainers[getattr(self,'_%sr2c' % (o,))[d]]
				containers = {}
				for k in filter(lambda x: x != 'id' and ci[x]['type'] == 'one2many',getattr(self,'_%sdata' % (o,))[d].keys()):
					containers[k] = []
	
				res.setdefault('__remove__',[]).append({'__path__':d,'__container__':container,'__model__':model,'__containers__':containers})
		
		#print('res-container:',container,res)
		return res

	def _odiffs(self,commit=True):
		return self._diffs('o','c',commit)

	def _pdiffs(self,commit=True):
		return self._diffs('p','c',commit)

	def _oapply(self,commit=True):
		self._diffs('o','c',commit)

	def _papply(self,commit=True):
		self._diffs('p','c',commit)

	def _getData(self,d):
		path = str(id(d))

		model = self._cmodels[path]
		data = {}
		container = None
		containers = {}
		ci = self._cmetas[model]
		for k in self._cdata[path].keys():
			if k != 'id' and ci[k]['type'] == 'one2many':
				containers[k] = self._getDataContainers(k + '.' + path)
			else:
				data[k] = self._cdata[path][k]

		if path in self._cr2c:
			container = self._ccontainers[self._cr2c[path]]
		
		res = {'__path__':path,'__data__':data,'__model__':model}
		if container:
			res['__container__'] = container
		
		if len(containers) > 0:
			res['__containers__'] = containers
		
		return res

	def _getDataContainers(self,container):
		res = []

		for r in self._cdata[self._cnames[container]]:
			res.append(self._getData(r))
			
		return res
			
class MCache(object):
	
	def __init__(self,cr,pool,uid,mode,context):
		self._cr = cr
		self._pool = pool
		self._uid = uid
		self._context = context
		self._mode = mode

		#self._data = {}
		self._m = {}
		self._checks = {}

		self._meta = {}
		self._cache_attrs = {}
		self._diffs = {}

	def _getMode(self):
		return [self._mode]

	def _setMode(self,mode):
		self._mode = mode
		return [self._mode == mode]

	def _initialize(self,model,view='form'):
		self._clear()
		self._model = model
		row = self._buildItem(model,view)
		self._data = DCacheDict(row,model,self._pool)
		self._getMeta()	
		m = self._data._getData(self._data._data)
		m['__meta__'] = self._do_meta(str(self._data._root))
		m['__checks__'] = []
		return m

	def _do_read(self,model,row):
		#print('DO-READ:',model,row)
		self._clear()
		self._model = model
		self._data = DCacheDict(row,model,self._pool)
		#print('DATA:',self._data)
		self._getMeta()
		#print('GET-META')
		m = self._data._getData(self._data._data)
		#print('GET-DATA')
		m['__meta__'] = self._do_meta(str(self._data._root))
		#print('GET-DO-META')
		m['__checks__'] = []
		#print('M:',m)
		return m


	def _getMeta(self,models = None):
		if models is None:
			models = list(self._data._cmodels.values())
		for model in models:
			print('GET-META:',model)
			if not model in self._meta:
				self._meta[model] = self._pool.get(model).columnsInfo(attributes=['type','obj','rel','readonly','invisible','required','state','on_change','on_check'])

			if not model in self._cache_attrs:
				self._cache_attrs[model] = {'iscaching': len(self._pool.get(model)._computefields) > 0,'computefields': self._pool.get(model)._computefields,'changefields': self._pool.get(model)._on_change_fields,'checkfields': self._pool.get(model)._on_check_fields}


	def _clear(self):
		#self._data._data.clear()
		self._m.clear()
		return True

	def _buildItem(self,model,view='form'):
		ci = self._pool.get(model).columnsInfo(attributes = ['type'])
		
		if view == 'form':
			item = dict.fromkeys(list(self._pool.get(model)._columns.keys()))
		elif view == 'list':
			item = dict.fromkeys(list(filter(lambda x: ci[x]['type'] not in ('one2mamy','many2many','xml','text','binary','json'),self._pool.get(model)._columns.keys())))
		
		for key in item.keys():
			if ci[key]['type'] in ('many2one','related'):
				item[key] = {'id':None,'name':None}
			elif ci[key]['type'] in ('one2many','many2many'):
				item[key] = []

		return item

	def _on_change(self,path,model,key,context):
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
		
		#print('OIDS:',list(self._oids.keys()),list(self._containers.keys()))
		if key not in self._data._cdata[path] or self._data._cdata[path][key] != value:
			#print('path,key,value:',path,key,value)
			self._data._cdata.setdefault(path,{})[key] = value
			model = self._data._cmodels[path]
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
					res['m'] = m._attrs
			elif type(m._attrs) == str:
				method = getattr(m,m._attrs,None)
				if method:
					rc = method(self._cr,self._pool,self._uid,self._data[path],self._context)
					if rc and len(rc) > 0:
						res.setdefault('m',{}).update(rc)

			cols = self._meta[model]
			for a in ('readonly','invisible','required'):
				k = list(filter(lambda x:cols[x]['type'] != 'referenced' and type(cols[x][a]) == str,cols.keys()))
				v = list(map(lambda x: cols[x][a],k))
				for v1 in v:
					method = getattr(m,v1,None)
					if method:
						rc = method(self._cr,self._pool,self._uid,k,self._data[path],self._context)
						if rc and len(rc) > 0:
							for k1 in rc.keys():
								if a == 'readonly':
									res.setdefault('c',{}).setdefault(k1,{})['ro'] = rc[k1]
								elif a == 'required':
									res.setdefault('c',{}).setdefault(k1,{})['rq'] = rc[k1]
								elif a == 'invisible':
									res.setdefault('c',{}).setdefault(k1,{})['iv'] = rc[k1]
						
			for key in self._meta[model].keys():
				column = self._meta[model][key]
				if type(m._col_attrs) == dict:
					if len(m._col_attrs) > 0:
						res['c'] = m._col_attrs
				elif type(m._col_attrs) == str:
					res['c'] = getattr(m,m._col_attrs,None)(self._cr,self._pool,self._uid,self._data[path],self._context)
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
									res.setdefault('c',{}).setdefault(key,{})[k1] = attrs[k1]

					if 'readonly' in column and type(column['readonly']) == bool:
						res.setdefault('c',{}).setdefault('ro',{})[key] = column['readonly']

					if 'required' in column and type(column['required']) == bool:
						res.setdefault('c',{}).setdefault('rq',{})[key] = column['required']

					if 'invisible' in column and type(column['invisible']) == bool:
						res.setdefault('c',{}).setdefault('iv',{})[key] = column['invisible']
				
					if 'c' in res and len(res['c']) == 0:
						del res['c']

					if 'm' in res and len(res['m']) == 0:
						del res['m']

			if self._data._cpaths[path]:
				path = self._data._cpaths[path]
			else:
				break


		return res
	
	def _do_calculate(self,path,context):
		while True:
			model = self._data._cmodels[path]		
			_computes = self._pool.get(model)._compute(self._cr, self._pool, self._uid, self._cache_attrs[model]['computefields'], self._data._cdata[path], self._context)
			#print('CALCULATE:',path,model,self._data._cdata[path],self._data._cpaths[path])
			if len(_computes) > 0:
				self._data._cdata.setdefault(path,{}).update(_computes)

			if self._data._cpaths[path]:
				path = self._data._cpaths[path]
			else:
				break

	def _setDefault(self,model,item):
		_default = self._pool.get(model)._default
		m1 = self._meta[model]
		for k in _default.keys():
			if k not in item or item[k] is None:
				if m1[k]['type'] in ('numeric','decimal'):
					item[k] = Decimal(_default[k])
				else:
					item[k] = _default[k]
	
	def _add(self,model,container,context,view='form'):
		print('ADD:',model,container)
		row = self._buildItem(model,view)
		self._setDefault(model,row)
		
		print('ADD-ROW:',str(id(row)),row)
		#self._data._cdata[self._data._cnames[container]].append(row)
		c = container.split('.')
		self._data._buildTree(row,model,c[1],c[0],'A')
		
		self._do_calculate(str(id(row)),context)
		
		res = {}

		data_diffs = self._data._odiffs(True)
		
		#self._data._oapply()

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

			
	def _remove(self,path,container,context):
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
	
	def _m2o_find(self,path,model,key,value,context):
		rec_name = self._pool.get(self._meta[model][key]['obj'])._getRecNameName()
		fields = [rec_name]
		cond = [(rec_name,'like',value['name'] if type(value) == dict else value)]
		#print('R:',model,key,value,cond)
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
		fields = [rec_name]
		cond = [(rec_name,'like',value['name'] if type(value) == dict else value)]
		for rel in relatedy:
			cond.append((rel,'=',self._data[path][rel]))
		r = self._pool.get(self._meta[model][key]['obj']).select(self._cr,self._pool,self._uid,fields,cond=cond)
		#print('R:',r,key,value)
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

	
	def _commit(self):
		if self._mode in ('new',):
			self._clear()

	def _rollback(self):
		if self._mode in ('new',):
			self._clear()
			
	def _mcache(self,path,key=None,value=None,context={}):
		res = {}

		#print('MCACHE:',path,key,value)
		self._do_diff(path,key,value,context)
		meta = self._do_meta(path)
		
		self._diffs = eval(str(self._data._odiffs()))
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

