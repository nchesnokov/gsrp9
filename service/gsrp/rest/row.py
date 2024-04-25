import copy
import web_pdb
class RowDict(dict):

	def __init__(self,row):
		if type(row) == dict:
			for key,value in row.items():
				if type(value) not in (list,tuple):
					self[key] = copy.copy(value)
				elif type(value) in (list,tuple):
					self[key] = RowsArray(value)

	def __getattr__(self,name):
		return self[name]


class RowsArray(list):
	def __init__(self,rows):
		if type(rows) in (list,tuple):
			for row in rows:
				self.append(RowDict(row))

class RecordDict(dict):
	def __init__(self,record):
		if type(record) == dict:
			for key,value in record.items():
				if type(value) in (list,tuple):
					self[key] = RowsArray(value)
				elif type(value) == dict:
					self[key] = RowDict(value)
				else:
					self[key] = copy.copy(value)

	def __getattr__(self,name):
		return self[name]

class RecordsArray(list):
	def __init__(self,records):
		if type(records) in (list,tuple):
			for record in records:
				self.append(RecordDict(record))

class Record(object):
	def __init__(self, data):
		#web_pdb.set_trace()
		if type(data) in (list,tuple):
			self.value = RecordsArray(data)
		elif type(data) == dict:
			self.value = RecordDict(data)

	def __getattr__(self,name):
		return self.value[name]

class Level(dict):
	def _setMeta(self,meta):
		self['meta'] = meta

	def _getattr__(self,name):
		return self['meta'][name]

v = Record({'a':'b','f':1,'c':[{'d':'e','f':[{'a':'b','f':1}]}]})

class Meta(dict):
	def __init__(self,root, meta, value):
		self ['root'] = root
		self['meta'] = {}
		self['value'] = value


class MetaRecord(object):
	pass

class TxnUpdate(object):
	_pv = Level()
	_ov = Level()
	_cv = Level()

	def __init__(self, meta):
		self._setCValue(meta)
		self._setOValue(meta)
		self._setP8Value(meta)


	def _setCValue(self, value):
		self._cv._setMeta(value)

	def _setOValue(self, value):
		self._ov._setMeta(value)

	def _setPValue(self, value):
		self._pv._setMeta(value)

	def _buildLevel(self):
		pass



print(v.c[0].f[0].f,type(v.value),getattr(v,'c'))
