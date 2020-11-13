# class ModelMeta(object):
	# def __init__(self, m):
		# self._name = m._name
		# self._columnsmeta = m._columnsmeta
		# self._parent_models = m._shema[0]
		# for k in ('row','m2ofields','m2orelated','o2m','o2r','referenced','readonly','on_change_','on_check_','compute','domaincompute','selectioncompute','storecompute','nostorecompute','nosaved','required','selectable'):
			# setattr(self, '_' + k + 'fields', getattr(m, '_' + k + 'fields'))

# class ModelRecord(object):
	# def __init__(self, meta):
		# self._meta = meta

	# def build(self, r,oid = None):
		# for k in ('row','m2ofields','m2orelated','o2m','o2r','referenced','readonly','on_change_','on_check_','compute','domaincompute','selectioncompute','storecompute','nostorecompute','nosaved','required','selectable'):
			# rkeys = set(r.keys())
			# setattr(self, '_' + k + 'cols', list(filter(lambda x: x in rkeys, getattr(self._meta, '_' + k + 'fields').keys )))

		# if oid:
			# self._oid = oid
		# else:
			# self._oid = str(id(r))	
			# self._values = {}
			# for col in self._rowcols:
				# self._values[col] = r[col]

	# def _diffs(self,r):
		# res = {}
		# if hasattr(self,'_values'):
			# vals = self._values
		# else:
			# vals = ctypes.cast(int(self._oid), ctypes.py_object).value
		
		# ok = set(vals.keys())
		# ck = set(r.keys())
		# uk = list(ok.intersection(ck))
		# ik = list(ck- ok)
		# dk = list(ok- ck)

		# for k in uk:
			# if type(r[k]) == memoryview:
				# res.setdefault('__update__',{}).setdefault(self._oid,{})[k] = r[k].tobytes()
			# else:
				# res.setdefault('__update__',{}).setdefault(self._oid,{})[k] = r[k]

		# for k in ik:
			# if type(r[k]) == memoryview:
				# res.setdefault('__insert__',{}).setdefault(self._oid,{})[k] = r[k].tobytes()
			# else:
				# res.setdefault('__insert__',{}).setdefault(self._oid,{})[k] = r[k]

		# for k in dk:
			# res.setdefault('__delete__',{}).setdefault(self._oid,[]).append(k)

		# return res

	# def _apply_from_diffs(self,diffs):
		# if not hasattr(self,'_values'):
			# return False
		# if  ['__insert__'] in diffs:
			# iv = diffs['__insert__'][self._oid]
			# self._values.update(iv.copy())

		# if  ['__update__'] in diffs:
			# uv = diffs['__update__'][self._oid]
			# self._values.update(uv.copy())

		# if  ['__delete__'] in diffs:
			# dv = diffs['__delete__'][self._oid]
			# for k in dv:
				# del self._values[k]
		
		# return True


# class ModelRecords(list):
	# def  _add(self,record,oid=None):
		# if oid:
			# self.append(oid)
			# if not hasattr(self,'_values'):
				# self._values = {}
			
			# self._values[oid] = record.copy()
		# else:
			# self.append(str(id(record)))
	
	# def _diffs(self, records):
		# res = {}
		# if hasattr(self,'_values'):
			# ok = set(self._values.keys())
		# else:
			# ok = set(self)
		# ck = set(map(lambda x: str(id(x)),records))
		# ik = list(ck- ok)
		# dk = list(ok- ck)
		
		# for k in ik:
			# res.setdefault('__append__', {})[k] =  ctypes.cast(int(k), ctypes.py_object).value

		# for k in dk:
			# res.setdefault('__remove__', {})[k] =  self._values[k]

		# return res

	# def _apply_from_diffs(self,diffs):
		# if '__remove__' in diffs:
			# rv = diffs['__remove__']
			# for k in rv.keys():
				# self.remove(k)
			# if hasattr(self,'_values'):
				# for k in rv.keys():
					# del self._values[k]

		# if '__append__' in diffs:
			# av = diffs['__append__']
			# for k in av.keys():
				# self.add(av[k],k)

		# return True

# class DCache(object):
	# __doc__ = """
	# {__path__:{__model__,__m2o_containers__,__o2m_containers__,__m2m__containers__,__data__}}'
	# __path__ - id(записи)
	# __model__  - имя модели
	# __m2o_containers__ = {имя поля: __path__ вышестояшей записи}
	# __o2m_containers__ = {имя поля: [__path__:{__model__,__m2o_containers__,__o2m_containers__,__m2m__containers__}]}
	# __m2m_containers__ = {имя поля:[__path__]}
	# """
	# _entry=None
	
	# def __init__(self,pool,primary=True):
		# self._pool = pool

		# for v in ('entries','items','containers','ids'):
			# for a in ('p','w','o','c'):
				# if not primary and a == 'p':
					# continue
				# setattr(self,'_%s%s' % (a,v),{})

	# def _buildEntries(self,model,data):
		# oid = id(data)

		# if not self._entry: 
			# self._entry = oid

		# if 'id' in data:
			# self._cids[data['id']] = oid

		# self._citems.setdefault(id(data),{})['__model__'] = model._name
		# for m2ofield in model._m2ofields:
			# if  m2ofield in data:
				# if data[m2ofield] is not None:
					# if  data[m2ofield] not in self._cids:
						# self._citems.setdefault(id(data),{}).setdefault('__m2o_containers__',{})[o2mfield] = self._build_m2o_entry(self._pool.get(model._columns[m2ofield].obj),data[m2ofield])

		# for o2mfield in model._o2mfields:
			# if  o2mfield in data:
				# if data[o2mfield] is not None:
					# self._citems.setdefault(id(data),{}).setdefault('__o2m_containers__',{}).setdefault(o2mfield,[]).extend(self._build_o2m_entry(self._pool.get(model._columns[o2mfield].obj),data[o2mfield]))

		# for m2mfield in model._m2mfields:
			# if  m2mfield in data:
				# if data[m2mfield] is not None:
					# self._citems.setdefault(id(data),{}).setdefault('__m2m_containers__',{}).setdefault(m2mfield,[]).extend(self._build_m2m_entry(self._pool.get(model._columns[m2mfield].obj),data[m2mfield]))

		# return oid

	# def _build_m2o_entry(self,model,data):
		# rows = model.read(data['id'],[model._rowfields])
		# if len(rows) > 0:
			# self._cids[data['id']] = id(rows[0])
			# self._buildEntries(model,rows[0])

	# def _build_o2m_entry(self,model,datas):
		# res = []
		
		# for data in datas:
			# oid = id(data)
			# if 'id' in data and data['id'] not in self._cids:
				# self._cids[data['id']] = oid
				# res.append(oid)
				# self._buildEntries(model,data)
		
		# return res

	# def _build_m2m_entry(self,model,datas):
		# res = []
		
		# for data in datas:
			# oid = id(data)
			# if 'id' in data and data['id'] not in self._cids:
				# self._cids[data['id']] = oid
				# res.append(oid)
				# self._buildEntries(model,data)
		
		# return res


	# def add(self, model, data, primary=True):
		# if type(data) == dict:
			# self._entry[model._name] = DCacheList(self._pool.get(model),[data],context,primary=True)
		# elif type(data) in (list,tuple):
			# self._entry[model._name] = DCacheList(self._pool.get(model),data,context,primary=True)
			
	# def _diffs(self):
		# for d in self._data:
			# d._diffs()
	
	# def clear(self):
		# self._data.clear()
		# self._diffs.clear()
