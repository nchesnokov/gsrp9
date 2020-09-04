import logging
import traceback
import uuid
import copy
import pdb
import pytz
import web_pdb
from passlib.hash import pbkdf2_sha256
from decimal import Decimal
from configparser import ConfigParser
from serviceloader.tools.common import configManagerDynamic
from gsrp5service.connection import Cursor
from gsrp5service.orm.model import Access
from gsrp5service.services.models.cache4 import MCache

_logger = logging.getLogger('listener.' + __name__)

class interface_exception(Exception): pass

class Session(object):
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
			return self._cache[args[1]]._o2m_add(**(args[2]))
		elif args[0] == 'm2madd':			
			return self._cache[args[1]]._m2m_add(**(args[2]))
		elif args[0] == 'remove':
			return self._cache[args[1]]._o2m_remove(**(args[2]))
		elif args[0] == 'removes':
			return self._cache[args[1]]._o2m_removes(**(args[2]))
		elif args[0] == 'm2mremove':
			return self._cache[args[1]]._m2m_remove(**(args[2]))
		elif args[0] == 'm2mremoves':
			return self._cache[args[1]]._m2m_removes(**(args[2]))
		elif args[0] == 'initialize':
			return self._cache[args[1]]._initialize(**(args[2]))
		elif args[0] == 'copy':
			return self._cache[args[1]]._do_copy(**(args[2]))
		elif args[0] == 'read':
			return self._cache[args[1]]._do_read(**(args[2]))
		elif args[0] == 'create':
			return self._cache[args[1]]._do_create(**(args[2]))
		elif args[0] == 'write':
			return self._cache[args[1]]._do_write(**(args[2]))
		elif args[0] == 'modify':
			return self._cache[args[1]]._do_mmfify(**(args[2]))
		elif args[0] == 'unlink':
			return self._cache[args[1]]._do_unlink(**(args[2]))
		elif args[0] == 'select':
			return self._cache[args[1]]._do_select(**(args[2]))
		elif args[0] == 'insert':
			return self._cache[args[1]]._do_insert(**(args[2]))
		elif args[0] == 'update':
			return self._cache[args[1]]._do_update(**(args[2]))
		elif args[0] == 'upsert':
			return self._cache[args[1]]._do_upsert(**(args[2]))
		elif args[0] == 'delete':
			return self._cache[args[1]]._do_delete(**(args[2]))
		elif args[0] == 'call':
			return self._cache[args[1]]._do_call(**(args[2]))
		elif args[0] == 'save':
			return self._cache[args[1]]._save(**(args[2]))
		elif args[0] == 'reset':
			return self._cache[args[1]]._reset(**(args[2]))
		elif args[0] == 'commit':
			return self._cache[args[1]]._commit(**(args[2]))
		elif args[0] == 'rollback':
			return self._cache[args[1]]._rollback(**(args[2]))
		elif args[0] == 'open':
			oid = str(uuid.uuid4())
			kwargs = {'cr':self._cursor,'pool':self._models,'uid':self._uid}
			for k in args[1].keys():
				kwargs[k] = args[1][k]
			self._cache[oid] = MCache(**kwargs)
			return [oid]
		elif args[0] == 'getmode':
			return self._cache[args[1]]._getMode()
		elif args[0] == 'setmode':
			return self._cache[args[1]]._setMode(**(args[2]))
		elif args[0] == 'getcontext':
			return self._cache[args[1]]._getContext()
		elif args[0] == 'setcontext':
			return self._cache[args[1]]._setContext(**(args[2]))
		elif args[0] == 'ischange':
			return self._cache[args[1]]._is_change(**(args[2]))
		elif args[0] == 'close':
			del self._cache[args[1]]
			return [True]
		
		return Exception('No defined method of mcache: <%s>' % (args[0],))


class User(Session):

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
	_reports = {}
	_dialogs = {}
	_wizards = {}
	_queries = {}
	_cache = {}
	_cache_attrs = {}

	def __init__(self,config_file):
		cf = ConfigParser()
		cf.read(config_file)
		self._conf = configManagerDynamic(cf,{'dsn':None,'database':None,'host':'localhost','port':26257,'user':None,'password':None,'sslmode':None,'sslrootcert':None,'sslrootkey':None,'sslcert':None,'sslkey':None},ikey=['port'])

	def _call(self,args):
		res = []
		args0 = args[0]
		if args0 in ('_cache',):
			rc = self._mcache(args[1:])
		elif args0 == 'models':
			rc = self._components['models']._call(args[1:])
		elif args0 == 'reports':
			rc = self._components['reports']._call(args[1:])
		elif args0 == 'queries':
			rc = self._components['queries']._call(args[1:])
		elif args0 == 'dialogs':
			rc = self._components['dialogs']._call(args[1:])
		elif args0 == 'wizards':
			rc = self._components['wizards']._call(args[1:])
		elif args0 == 'uis':
			rc = self._components['uis']._call(args[1:])
		elif args0 == 'modules':
			if self._connected:
				self._components['modules']._setup(cr=self._cursor,pool=self._models,uid=self._uid,registry=self._components['registry'])
				rc = self._components['modules']._call(args[1:])
			else:
				rc = [False,'Not logged']
		elif args0 == 'gens':
			rc = self._components['gens']._call(args[1:])
		elif args0 == 'slots':
			rc = self._components['slots']._call(args[1:])
		elif args0 in ('login','logout','commit','rollback'):
			rc = getattr(self,args0)(**(args[1]))
		elif args0 == '_commit':
			rc = self.commit()
		elif args0 == '_rollback':
			rc = self.rollback()
		else:
			rc = [False,'NOT CALLED']
		
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
			self._registry = self._components['registry']
			self._registry._load_module('bc')
			self._models = self._components['registry']._create_loaded_models(self)
			self._reports = self._components['registry']._create_loaded_reports(self)
			self._queries = self._components['registry']._create_loaded_queries(self)
			self._dialogs = self._components['registry']._create_loaded_dialogs(self)
			self._wizards = self._components['registry']._create_loaded_wizards(self)
			self._components['models']._setup(self)
			self._components['reports']._setup(self)
			self._components['queries']._setup(self)
			self._components['dialogs']._setup(self)
			self._components['wizards']._setup(self)
			self._components['uis']._setup(self)
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
					#self._components['models']._setupUID(self._uid)
					#self._components['uis']._setupUID(self._uid)
					for key in self._models.keys():
						#self._models[key]._session = self
						if res[2]:
							self._models[key]._access = Access(read=True,write=True,create=True,unlink=True,modify=True,insert=True,select=True,update=True,delete=True,upsert=True,browse=True,selectbrowse=True)
						else:
							self._models[key]._access = Access(read=True,write=False,create=False,unlink=False,modify=False,insert=False,select=True,update=False,delete=False,upsert=False,browse=True,selectbrowse=True)

					db_infos = self._components['models']._call(['bc.modules','select',{'fields':['code','state'],'cond':[],'context':{}}])
					for db_info in db_infos:
						self._components['registry']._modules[db_info['code']]['db_id'] = db_info['id']
						self._components['registry']._modules[db_info['code']]['state'] = db_info['state']
	
					self._components['registry']._load_installed_modules()
					self._components['registry']._load_inheritables()
					models = self._components['registry']._create_loaded_models(self)
					for key in models:
						self._models[key] = models[key]
						self._models[key]._session = self
						  

						if res[2]:
							self._models[key]._access = Access(read=True,write=True,create=True,unlink=True,modify=True,insert=True,select=True,update=True,delete=True,upsert=True,browse=True,selectbrowse=True)
						else:
							self._models[key]._access = Access(read=True,write=False,create=False,unlink=False,modify=False,insert=False,select=True,update=False,delete=False,upsert=False,browse=True,selectbrowse=True)

					reports = self._components['registry']._create_loaded_reports(self)
					for key in reports:
						self._reports[key] = reports[key]
						self._reports[key]._session = self    

					queries = self._components['registry']._create_loaded_queries(self)
					for key in queries:
						self._queries[key] = queries[key]  
						self._queries[key]._session = self 

					dialogs = self._components['registry']._create_loaded_dialogs(self)
					for key in dialogs:
						self._dialogs[key] = dialogs[key]  
						self._dialogs[key]._session = self

					wizards = self._components['registry']._create_loaded_wizards(self)
					for key in wizards:
						self._wizards[key] = wizards[key]  
						self._wizards[key]._session = self  
	
					return [self._connected,self._uid,{'country_timezones':dict(pytz.country_timezones),'country_names':dict(pytz.country_names),'langs':self._models.get('bc.langs').select(['code','description']),'preferences':self._models.get('bc.user.preferences').select(['user_id','lang','country','timezone'])}]
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

class System(Session):

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
	_reports = {}
	_dialogs = {}
	_wizards = {}
	_queries = {}
	_cache = {}
	_cache_attrs = {}
	
	def __init__(self,config_file):
		cf = ConfigParser()
		cf.read(config_file)
		self._conf = configManagerDynamic(cf,{'dsn':None,'database':None,'host':'localhost','port':26257,'user':'system','password':None,'sslmode':None,'sslrootcert':None,'sslrootkey':None,'sslcert':None,'sslkey':None},ikey=['port'])
		#print('CONG:',self._conf)

	def _call(self,args):
		res = []
		args0 = args[0]
		if args0 == 'modules':
			rc = self._components['modules']._call(args[1:])
		elif args0 == 'models':
			rc = self._components['models']._call(args[1:])
		elif args0 == 'gens':
			rc = self._components['gens']._call(args[1:])
		#elif args0 == 'slots':
			#rc = self._components['slots']._call(args[1:])
		elif args0 in ('login','logout','commit','rollback','createSlot','dropSlot','initializeSlot'):
			rc = getattr(self,args0)(**(args[1]))
		elif args0 == '_commit':
			rc = self.commit()
		elif args0 == '_rollback':
			rc = self.rollback()
		else:
			rc = [False,'NOT CALLED']
		
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
		#print('CONF-1:',conf)
		
		if conf['sslmode']:
			self._cursor  = Cursor(dsn=conf['dsn'],database=conf['database'],host=conf['host'],port=conf['port'],user=conf['user'],password=conf['password'],sslmode=conf['sslmode'],sslrootcert=conf['sslrootcert'],sslrootkey=conf['sslrootkey'],sslcert=conf['sslcert'],sslkey=conf['sslkey'])
		else:
			self._cursor  = Cursor(dsn=conf['dsn'],database=conf['database'],host=conf['host'],port=conf['port'],user=conf['user'],password=conf['password'])

		if self._cursor.open():
			self._registry = self._components['registry']
			self._registry._load_modules()
			self._models = self._components['registry']._create_loaded_models(self)
			self._reports = self._components['registry']._create_loaded_reports(self)
			self._queries = self._components['registry']._create_loaded_queries(self)
			self._dialogs = self._components['registry']._create_loaded_dialogs(self)
			self._wizards = self._components['registry']._create_loaded_wizards(self)


			for key in self._models.keys():
				self._models[key]._access = Access(read=True,write=True,create=True,unlink=True,modify=True,insert=True,select=True,update=True,delete=True,upsert=True,browse=True,selectbrowse=True)
			
			self._getUid()
			self._components['modules']._setup(self)
			self._components['models']._setup(self)
			self._components['reports']._setup(self)
			self._components['queries']._setup(self)
			self._components['dialogs']._setup(self)
			self._components['wizards']._setup(self)
			self._components['gens']._setup(self._components['registry'])
			self._components['slots']._setup(self)		
			return self

		#self._cursor = None

	def createSlot(self,name,db_user):
		rmsg = []
		if name !='system':
			self._cursor.cr.execute("select count(*) from pg_catalog.pg_database where datname=%s" ,(name,))
			if self._cursor.cr.fetchone()[0] == 0:
				_logger.info("Creating Slot: %s" % (name,))
				self.commit()
				if self._cursor.conn.autocommit:
					autocommit = True
				else:
					autocommit = False
				
				self._cursor.conn.autocommit=True
				_logger.info("Create Slot: %s" % (name,))
				self._cursor.execute("CREATE DATABASE IF NOT EXISTS %s ENCODING='UTF-8';SET DATABASE=%s;GRANT ALL ON DATABASE %s TO %s" % (name,name,name,db_user))
				self._cursor.conn.autocommit = autocommit

				rmsg.append(self._cursor.cr.statusmessage)
				rmsg.extend(self._components['modules']._call(['sysinstall']))
				_logger.info("Slot: %s Created" % (name,))
			else:
				_logger.info("Slot: %s are created" % (name,))
				rmsg.append("Slot: %s are created" % (name,))
		else:
			rmsg.append(Exception("Can`t create system sid. Name <system> is reserved."))

		#print('RMSG:',rmsg)
		return rmsg
	
	def dropSlot(self,sid):
		res = []
		if sid != 'system':
			self.commit()
			if self._cursor.conn.autocommit:
				autocommit = True
			else:
				autocommit = False
				
			self._cursor.conn.autocommit=True
			_logger.info("Drop Slot: %s" % (sid,))
			self._cursor.execute("DROP DATABASE IF EXISTS %s CASCADE" % (sid,))
			self._cursor.conn.autocommit = autocommit
			_logger.info("Slot: %s Dropped" % (sid,))
			res.append(self._cursor.cr.statusmessage)
			return res
		else:
			_logger.info("Can`t drop Slot: %s" % (sid,))
			return [Exception("Can`t drop Slot: %s" % (sid,))]
	
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
			self._cursor.execute('select id,password from bc_users where login = %s and issuperuser = %s limit 1', (user,True))
			if self._cursor.rowcount > 0:
				res = self._cursor.fetchone(['id','password'],{'id':'UUID','password':'varchar'})
				if pbkdf2_sha256.verify(password, res[1]):
					self._connected =True
					self._uid = res[0]
					for key in self._models.keys():
						self._models[key]._session = self
						self._models[key]._access = Access(read=True,write=True,create=True,unlink=True,modify=True,insert=True,select=True,update=True,delete=True,upsert=True,browse=True,selectbrowse=True)

					db_infos = self._components['models']._call(['bc.modules','select',{'fields':['code','state'],'cond':[]}])
					for db_info in db_infos:
						self._components['registry']._modules[db_info['code']]['db_id'] = db_info['id']
						self._components['registry']._modules[db_info['code']]['state'] = db_info['state']

				#self._components['registry']._load_inheritables()
				#models = self._components['registry']._create_loaded_models()

				for key in self._models.keys():
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

	def commit(self):
		if self._cursor:
			self._cursor.commit()
		return [0 , 'Commit Work']

	def rollback(self):
		if self._cursor:
			self._cursor.rollback()
		return [0 , 'Rollback Work']
