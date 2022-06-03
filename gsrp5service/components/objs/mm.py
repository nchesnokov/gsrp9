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
from gsrp5service.components.objs.cache4 import MCache, DCacheDict, DCacheList
from gsrp5service.orm.utils.models import *
#from datetime import datetime,date,time
import time as tm
import web_pdb


	
class Model(object):
	def __init__(self,session):
		self._cr = session._cursor
		self._uid = session._uid
		self._pool = session._models
		self._session = session
	
	def count(self, model, cond = None, context = {}):
		return count(self, self._cr, self._uid, self._pool, model, cond, context)
	
	def countFor(self, name, cond = None, context = {}):
		return count(self, self._cr, self._uid, self._pool, self._pool.get(name), cond, context)
		
	def search(self, model, cond = None, context = {}, limit = None, offset = None):
		return search(self, self._cr, self._uid, self._pool, model, cond, context, limit, offset)

	def searchFor(self, name,  cond = None, context = {}, limit = None, offset = None):
		return search(self, self._cr, self._uid, self._pool, self._pool.get(name), cond, context, limit, offset)

	def read(self, model, ids, fields = None, context = {}):
		return  read(self, self._cr, self._uid, self._pool, model, ids, fields, context)
	
	def readFor(self, name, ids, fields = None, context = {}):
		return  read(self, self._cr, self._uid, self._pool.get(name), ids, fields, context)

	def readForUpdate(self, model, ids, fields = None, context = {}):
		return  readForUpdate(self, self._cr, self._uid, self._pool, model, ids, fields, context)
	
	def readForUpdateFor(self, name, ids, fields = None, context = {}):
		return  readForUpdate(self, self._cr, self._uid, self._pool.get(name), ids, fields, context)
	
	def select(self, model, fields = None ,cond = None, context = {}, limit = None, offset = None):
		return select(self, self._cr, self._uid, self._pool, model, fields, cond, context, limit, offset)

	def selectFor(self, name, fields = None ,cond = None, context = {}, limit = None, offset = None):
		return select(self, self._cr, self._uid, self._pool, self._pool.get(name),fields, cond, context, limit, offset)

	def selectForUpdate(self, model, fields = None ,cond = None, context = {}, limit = None, offset = None):
		return selectForUpdate(self, self._cr, self._uid, self._pool, fields, model, cond, context, limit, offset)

	def selectForUpdateFor(self, name, fields = None ,cond = None, context = {}, limit = None, offset = None):
		return selectForUpdate(self, self._cr, self._uid, self._pool, self._pool.get(name),fields, cond, context, limit, offset)
	
	def tree(self, model,fields = None ,parent = None, context = {}):
		return tree(self, self._cr, self._uid, self._pool, model, fields ,parent, context)

	def treeFor(self, name,fields = None ,parent = None, context = {}):
		return tree(self, self._cr, self._uid, self._pool, self._pool.get(name), fields ,parent, context)
	
	def treeForUpdate(self, model,fields = None ,parent = None, context = {}):
		return treeForUpdate(self, self._cr, self._uid, self._pool, model, fields ,parent, context)

	def treeForUpdateFor(self, name,fields = None ,parent = None, context = {}):
		return treeForUpdate(self, self._cr, self._uid, self._pool, self._pool.get(name), fields ,parent, context)

	def browse(self, model, ids, fields = None, context = {}):
		return browse(self, self._cr, self._uid, self._pool, model, ids, fields, context)

	def browseFor(self, name, ids, fields = None, context = {}):
		return browse(self, self._cr, self._uid, self._pool, self._pool.get(name), ids, fields, context)

	def browseForUpdate(self, model, ids, fields = None, context = {}):
		return browseForUpdate(self, self._cr, self._uid, self._pool, model, ids, fields, context)

	def browseForUpdateFor(self, name, ids, fields = None, context = {}):
		return browseForUpdate(self, self._cr, self._uid, self._pool, self._pool.get(name), ids, fields, context)
	
	def selectBrowse(self, model, fields = None ,cond = None, context = {}, limit = None, offset = None):
		return selectBrowse(self, self._cr, self._uid, self._pool, model, fields ,cond, context, limit, offset)

	def selectBrowseFor(self, name, fields = None ,cond = None, context = {}, limit = None, offset = None):
		return selectBrowse(self, self._cr, self._uid, self._pool, self._pool.get(name), fields ,cond, context, limit, offset)

	def selectBrowseForUpdate(self, model, fields = None ,cond = None, context = {}, limit = None, offset = None):
		return selectBrowse(self, self._cr, self._uid, self._pool, model, fields ,cond, context, limit, offset)

	def selectBrowseForUpdateFor(self, name, fields = None ,cond = None, context = {}, limit = None, offset = None):
		return selectBrowse(self, self._cr, self._uid, self._pool, self._pool.get(name), fields ,cond, context, limit, offset)
	
	def unlink(self, model, ids, context = {}):
		return unlink(self, self._cr, self._uid, self._pool, model, ids, context)

	def unlinkFor(self, name, ids, context = {}):
		return unlink(self, self._cr, self._uid, self._pool, self._pool.get(name), ids, context)
	
	def delete(self, model, cond, context = {}):
		return delete(self, self._cr, self._uid, self._pool, model, cond, context)

	def deleteFor(self, name, cond, context = {}):
		return delete(self, self._cr, self._uid, self._pool, self._pool.get(name), cond, context)
	
	def create(self, model, records, context = {}):
		res = []
		mcache = MCache(model._model._cr,model._model._pool,model._model._uid,'create',context)
		if type(records) == dict:
			mcache._data = DCacheDict(_conv_record_to_ext(model,records,context),model._name,model._model._cr,model._model._pool,model._model._uid,context,False)
			mcache._do_calculate_all(context)
			res.append(mcache._save()[1])
		elif  type(records) in (list,tuple):
			res = []
			for record in records:
				mcache._data = DCacheDict(_conv_record_to_ext(model,record,context),model._name,model._model._cr,model._model._pool,model._model._uid,context,False)
				mcache._do_calculate_all(context)
				res.append(mcache._save()[1])
		
		#self._commit()
		return res

		# if hasattr(self,'_session'):
			# if 'cache' in context:
				# return records
			# else:
				# uid = model._getCacheID('create',context)
				# return getattr(self._session._cache[uid],'_create')(model,records,context)
		# #return create(self, self._cr, self._uid, self._pool, model, records, context)

	def createFor(self, name, records, context = {}):
		return create(self, self._cr, self._uid, self._pool, self._pool.get(name), records, context)
	
	def write(self, model, records, context = {}):
		res = []
		mcache = MCache(model._model._cr,model._model._pool,model._model._uid,'write',context)
		if type(records) == dict:
			mcache._data = DCacheDict(_conv_record_to_ext(model,records,context),model._name,model._model._cr,model._model._pool,model._model._uid,context,False)
			mcache._do_calculate_all(context)
			res.append(mcache._save()[1])
		elif  type(records) in (list,tuple):
			res = []
			for record in records:
				mcache._data = DCacheDict(_conv_record_to_ext(model,record,context),model._name,model._model._cr,model._model._pool,model._model._uid,context,False)
				mcache._do_calculate_all(context)
				res.append(mcache._save()[1])
		
		#self._commit()
		return res
		
		#return write(self, self._cr, self._uid, self._pool, model, records, context)

	def writeFor(self, name, records, context = {}):
		return write(self, self._cr, self._uid, self._pool, self._pool.get(name), records, context)
	
	def modify(self, model, records, context = {}):
		res = []
		mcache = MCache(model._model._cr,model._model._pool,model._model._uid,'write',context)
		if type(records) == dict:
			mcache._data = DCacheDict(_conv_record_to_ext(model,records,context),model._name,model._model._cr,model._model._pool,model._model._uid,context,False)
			mcache._do_calculate_all(context)
			res.append(mcache._save()[1])
		elif  type(records) in (list,tuple):
			res = []
			for record in records:
				mcache._data = DCacheDict(_conv_record_to_ext(model,record,context),model._name,model._model._cr,model._model._pool,model._model._uid,context,False)
				mcache._do_calculate_all(context)
				res.append(mcache._save()[1])
		
		#self._commit()
		return res
		
		#return modify(self, self._cr, self._uid, self._pool, model, records, context)

	def modifyFor(self, name, records, context = {}):
		return modify(self, self._cr, self._uid, self._pool, self._pool.get(name), records, context)

	def update(self, model, record, cond = None,context = {}):
		return update(self, self._cr, self._uid, self._pool, model, record, cond,context)

	def updateFor(self, name, record, cond = None,context = {}):
		return update(self, self._cr, self._uid, self._pool, self._pool.get(name), record, cond,context)
	
	def insert(self, model, fields, values,context = {}):
		return insert(self, self._cr, self._uid, self._pool, model, fields, values,context)

	def insertFor(self, name, fields, values,context = {}):
		return insert(self, self._cr, self._uid, self._pool, self._pool.get(name), fields, values,context)

	def upsert(self, model, fields, values,context = {}):
		return upsert(self, self._cr, self._uid, self._pool, model, fields, values,context)

	def upsertFor(self, name, fields, values,context = {}):
		return upsert(self, self._cr, self._uid, self._pool, self._pool.get(name), fields, values,context)

	def model(self,name):
		return self._pool.get(name)
	
	def navigate(self,name,onlyRowData=True):
		pass
