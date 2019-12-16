import logging
import traceback
import uuid
import copy
import pdb
from passlib.hash import pbkdf2_sha256
from decimal import Decimal
from configparser import ConfigParser
from serviceloader.tools.common import configManagerDynamic
from gsrp5service.connection import Cursor
from gsrp5service.orm.model import Access
from gsrp5service.services.models.cache import MCache

_logger = logging.getLogger('listener.' + __name__)

class interface_exception(Exception): pass

class User(object):

	_closed = False
	_shutdown = False
	_cursor = None
	_logged = False
	_uuid = None
	_connected = None
	_sid = None
	_uid = 0
	_srvs = {}
	_models = {}
	_cache = {}
	_cache_attrs = {}

	def __init__(self,config_file):
		cf = ConfigParser()
		cf.read(config_file)
		self._conf = configManagerDynamic(cf,{'dsn':None,'database':None,'host':'localhost','port':26257,'user':None,'password':None,'sslmode':None,'sslrootcert':None,'sslcert':None,'sslkey':None},ikey=['port'])

	def _call(self,args):
		res = []
		args0 = args[0]
		if args0 == 'modules':
			rc = self._components['modules']._call(args[1:])
		elif args0 == 'models':
			rc = self._components['models']._call(args[1:])
		elif args0 == 'gens':
			rc = self._components['gens']._call(args[1:])
		elif args0 == 'slots':
			rc = self._components['slots']._call(args[1:])
		else:
			rc = ['NOT CALLED']
		
		if type(rc) in (list,tuple):
			res.extend(rc)
		else:
			res.append(rc)
		
		return res

	def open(self,profile):

		if profile not in self._conf:
			return [False,'Profile not found']
		
		self._profile = profile
		conf = self._conf[profile]

		if conf['sslmode']:
			self._cursor  = Cursor(dsn=conf['dsn'],database=conf['database'],host=conf['host'],port=conf['port'],user=conf['user'],password=conf['password'],sslmode=conf['sslmode'],sslrootcert=conf['sslrootcert'],sslcert=conf['sslcert'],sslkey=conf['sslkey'])
		else:
			self._cursor  = Cursor(dsn=conf['dsn'],database=conf['database'],host=conf['host'],port=conf['port'],user=conf['user'],password=conf['password'])

		if self._cursor.open():
			self._models = self._components['registry']._createAllModels()
			self._uid = self._getUid()
			self._components['models']._setup(self._cursor,self._models,self._uid,self)
			self._components['uis']._setup(self._cursor,self._models,self._uid)
			return self

		self._cursor = None

	def login(self,user,password):
		return self._login(user,password)

	def _login(self,user,password):
		if not self._connected:
			self._cursor.execute('select id,password,issuperuser from bc_users where login = %s limit 1', (user,))
			if self._cursor.rowcount > 0:			
				res = self._cursor.fetchone(['id','password','issuperuser'],{'id':'UUID','password':'varchar','issuperuser':'boolean'})
				if pbkdf2_sha256.verify(password, res[1]):
					self._connected =True
					self._uid = res[0]
					for key in self._sid._models.keys():
						self._models[key] = self._sid._models[key]
						if res[2]:
							self._models[key]._access = Access(read=True,write=True,create=True,unlink=True,modify=True,insert=True,select=True,update=True,delete=True,upsert=True,browse=True,selectbrowse=True)
						else:
							self._models[key]._access = Access(read=True,write=False,create=False,unlink=False,modify=False,insert=False,select=True,update=False,delete=False,upsert=False,browse=True,selectbrowse=True)
							
					db_infos = self._srvs['models']._execute(self,['bc.modules','select',{'fields':['code','state'],'cond':[]}])
					for db_info in db_infos:
						self._sid._registry._modules[db_info['code']]['db_id'] = db_info['id']
						self._sid._registry._modules[db_info['code']]['state'] = db_info['state']
	
					models = self._sid._registry._load_inherits()
					for key in models:
						self._sid._models[key] = models[key]
						self._models[key] = models[key]  

						if res[2]:
							self._models[key]._access = Access(read=True,write=True,create=True,unlink=True,modify=True,insert=True,select=True,update=True,delete=True,upsert=True,browse=True,selectbrowse=True)
						else:
							self._models[key]._access = Access(read=True,write=False,create=False,unlink=False,modify=False,insert=False,select=True,update=False,delete=False,upsert=False,browse=True,selectbrowse=True)
	
					return [self._connected,self._uid]
				else:
					return [False,'Invalid username or password']
		
		return [False,'Not connected']

	def logout(self):
		return self._logout()
	
	def _logout(self):
		if self._connected:
			self._connected =False
			self._uid = None
		return [not self._connected]

	def close(self):
		self._logout()
		if self._cursor:
			self._cursor.close()
		self._cursor = None
		self._closed = True
		return ['Closed']
	
	def shutdown(self):
		self.rollback()
		self.close()
		self._shutdown = True
		self._cache.clear()
		return ['Shutdown']

# new cache
	def _mcache(self,args):
		if args[0] == 'cache':
			return self._cache[args[1]]._mcache(**(args[2]))
		elif args[0] == 'm2ofind':			
			return self._cache[args[1]]._m2o_find(**(args[2]))
		elif args[0] == 'relatedfind':			
			return self._cache[args[1]]._related_find(**(args[2]))
		elif args[0] == 'action':			
			return self._cache[args[1]]._action(**(args[2]))
		elif args[0] == 'add':			
			return self._cache[args[1]]._add(**(args[2]))
		elif args[0] == 'remove':
			return self._cache[args[1]]._remove(**(args[2]))
		elif args[0] == 'initialize':
			return self._cache[args[1]]._initialize(**(args[2]))
		elif args[0] == 'open':
			oid = uuid.uuid4().hex
			kwargs = {'cr':self._cursor,'pool':self._models,'uid':self._uid}
			for k in args[1].keys():
				kwargs[k] = args[1][k]
			self._cache[oid] = MCache(**kwargs)
			return [oid]
		elif args[0] == 'getmode':
			return self._cache[args[1]]._getMode()
		elif args[0] == 'setmode':
			return self._cache[args[1]]._setMode(**(args[2]))
		elif args[0] == 'close':
			del self._cache[args[1]]
			return [True]
		
		return

# new cache
		
	def commit(self):
		if self._cursor:
			self._cursor.commit()

			for key in self._cache.keys():
				self._cache[key]._commit()

		return [0 , 'Commit Work']

	def rollback(self):
		if self._cursor:
			self._cursor.rollback()

			for key in self._cache.keys():
				self._cache[key]._rollback()

		return [0 , 'Rollback Work']

class System(object):

	_closed = False
	_shutdown = False
	_cursor = None
	_logged = False
	_uuid = None
	_connected = None
	_sid = None
	_uid = None
	_srvs = {}
	_models = {}
	
	def __init__(self,config_file):
		cf = ConfigParser()
		cf.read(config_file)
		self._conf = configManagerDynamic(cf,{'dsn':None,'database':None,'host':'localhost','port':26257,'user':'system','password':None,'sslmode':None,'sslrootcert':None,'sslcert':None,'sslkey':None},ikey=['port'])

	def _call(self,args):
		res = []
		args0 = args[0]
		if args0 == 'modules':
			rc = self._components['modules']._call(args[1:])
		elif args0 == 'models':
			rc = self._components['models']._call(args[1:])
		elif args0 == 'gens':
			rc = self._components['gens']._call(args[1:])
		elif args0 == 'slots':
			rc = self._components['slots']._call(args[1:])
		else:
			rc = ['NOT CALLED']
		
		if type(rc) in (list,tuple):
			res.extend(rc)
		else:
			res.append(rc)
		
		return res

	def open(self,profile):

		if profile not in self._conf:
			return [False,'Profile not found']

		self._profile = profile
		conf = self._conf[profile]
		
		if conf['sslmode']:
			self._cursor  = Cursor(dsn=conf['dsn'],database=conf['database'],host=conf['host'],port=conf['port'],user=conf['user'],password=conf['password'],sslmode=conf['sslmode'],sslcert=conf['sslcert'],sslkey=conf['sslkey'])
		else:
			self._cursor  = Cursor(dsn=conf['dsn'],database=conf['database'],host=conf['host'],port=conf['port'],user=conf['user'],password=conf['password'])

		if self._cursor.open():
			self._models = self._components['registry']._createAllModels()
			for key in self._models.keys():
				self._models[key]._access = Access(read=True,write=True,create=True,unlink=True,modify=True,insert=True,select=True,update=True,delete=True,upsert=True,browse=True,selectbrowse=True)
			
			self._uid = self._getUid()
			self._components['modules']._setup(cr=self._cursor,pool=self._models,uid=self._uid,registry=self._components['registry'])
			self._components['models']._setup(self._cursor,self._models,self._uid,self)
			self._components['gens']._setup(self._cursor,self._models,self._uid,self._components['registry'])
			self._components['slots']._setup(self)		
			return self

		#self._cursor = None

	
	def login(self,user,password,slot=None):
		return self._login(user,password,slot)

	def _getUid(self):
		self._cursor.execute('select uuid_v4()::UUID as id')
		if self._cursor.rowcount > 0:
			res = self._cursor.fetchone(['id'],{'id':'UUID'})
			self._uid = res[0]

	def _login(self,user,password,slot):
		if not self._connected:
			if slot:
				self._cursor.execute('SET DATABASE=%s' % (slot,))
			self._cursor.execute('select id,password from bc_users where login = %s limit 1', (user,))
			if self._cursor.rowcount > 0:
				res = self._cursor.fetchone(['id','password'],{'id':'UUID','password':'varchar'})
				if pbkdf2_sha256.verify(password, res[1]):
					self._connected =True
					self._uid = res[0]
					for key in self._sid._models.keys():
						self._models[key] = self._sid._models[key]
						self._models[key]._access = Access(read=True,write=True,create=True,unlink=True,modify=True,insert=True,select=True,update=True,delete=True,upsert=True,browse=True,selectbrowse=True)
					db_infos = self._srvs['models']._execute(self,['bc.modules','select',{'fields':['code','state'],'cond':[]}])
					for db_info in db_infos:
						self._sid._registry._modules[db_info['code']]['db_id'] = db_info['id']
						self._sid._registry._modules[db_info['code']]['state'] = db_info['state']

				self._sid._models = self._sid._registry._load_inherits()

				for key in self._sid._models.keys():
					self._models[key] = self._sid._models[key]
					self._models[key]._access = Access(read=True,write=True,create=True,unlink=True,modify=True,insert=True,select=True,update=True,delete=True,upsert=True,browse=True,selectbrowse=True)
		
		return [self._connected,self._uid]

	def logout(self):
		return self._logout()
	
	def _logout(self):
		if self._connected:
			self._connected =False
			self._uid = None
		return [not self._connected]

	def close(self):
		if hasattr(self,'_uuid') and self._uuid and '_uuid' in self._sid._sessions:
			del self._sid._sessions[self._uuid]
		self._logout()
		if self._cursor:
			self._cursor.close()
		self._cursor = None
		self._closed = True
		return [self._uuid,'Closed']
	
	def shutdown(self):
		self.rollback()
		self.close()
		self._uuid = None
		self._sid = None
		self._shutdown = True
		return ['Shutdown']

	def _service(self,args):
		if args[0] in self._srvs:
			return self._srvs[args[0]]._execute(args[1:])
		elif len(args) == 2 and args[1] in ('close','shutdown'):
			if args[1] == 'close':
				return self.close()
			elif args[1] == 'shutdown':
				return self.shutdown()
		raise interface_exception("In session: %s service: %s not found" % (self._uuid,args[1]))

	def commit(self):
		if self._cursor:
			self._cursor.commit()
		return [0 , 'Commit Work']

	def rollback(self):
		if self._cursor:
			self._cursor.rollback()
		return [0 , 'Rollback Work']
