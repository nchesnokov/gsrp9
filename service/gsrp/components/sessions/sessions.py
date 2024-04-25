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
from serviceloader.tools.common import Component
from gsrp5service.connection import Cursor
from gsrp5service.orm.model import Access
from gsrp5service.components.objs.mm import Model
from gsrp5service.components.objs.cache4 import MCache

_logger = logging.getLogger('listener.' + __name__)

class interface_exception(Exception): pass

class ModelProxy(object):
	def __init__(self,session):
		self._session = session

	def _call(self,args):
		return self._session._call(args)

	@property
	def _getCursor(self):
		return self._session._cursor
	
	@property
	def _getUid(self):
		return self._session._uid

	@property
	def _getPool(self):
		return	self._session._objects.get('models')
	
	@property
	def _getMCache(self):
		return self._session._mcache

	def _getInterface(self,key,name,*args, **kwargs):
		if key and key in self._session._cache and hasattr(self._session._cache[key],name):
			return getattr(self._session._cache[key],name)(*args,**kwargs)
		
	def _getModel(self,name):
		return	self._session._objects.get('models').get(name)

	def _getAction(self,name):
		return	self._session._objects.get('actions').get(name)

	def _getContext(self,name):
		return	self._session._context

	def _getLib(self,name):
		return	self._session._objects.get('libs').get(name)

	def _getNavigate(self,name):
		return	self._getMCache()['111']._navigate(name)

	def _getLangID(self,lang):
		return self._session._lang2id.get(lang)

class ReportProxy(object):
	def __init__(self,session):
		self._session = session

	def _call(self,args):
		return self._session._call(args)

	@property
	def _getCursor(self):
		return self._session._cursor
	
	@property
	def _getUid(self):
		return self._session._uid

	@property
	def _getPool(self):
		return	self._session._objects.get('models')
	
	@property
	def _getMCache(self):
		return self._session._mcache

	def _getInterface(self,key,name,*args, **kwargs):
		if key and key in self._session._cache and hasattr(self._session._cache[key],name):
			return getattr(self._session._cache[key],name)(*args,**kwargs)
		
	def _getReport(self,name):
		return	self._session._objects.get('reports').get(name)
	
	def _getLangID(self,lang):
		return self._session._lang2id.get(lang)

class DashboarfProxy(object):
	def __init__(self,session):
		self._session = session

	def _call(self,args):
		return self._session._call(args)

	@property
	def _getCursor(self):
		return self._session._cursor
	
	@property
	def _getUid(self):
		return self._session._uid

	@property
	def _getPool(self):
		return	self._session._objects.get('models')
	
	@property
	def _getMCache(self):
		return self._session._mcache

	def _getInterface(self,key,name,*args, **kwargs):
		if key and key in self._session._cache and hasattr(self._session._cache[key],name):
			return getattr(self._session._cache[key],name)(*args,**kwargs)
		
	def _getDashboard(self,name):
		return	self._session._objects.get('dashboards').get(name)
	
	def _getLangID(self,lang):
		return self._session._lang2id.get(lang)


class TrigerProxy(object):

	def __init__(self,session):
		self._session = session
	
	def _getModel(self,name):
		return	self._session._objects.get('models').get(name)
		
	def _getTriger(self,name):
		return	self._session._objects.get('triggers').get(name)

class ActionProxy(object):

	def __init__(self,session):
		self._session = session
		
	def _getAction(self,name):
		return	self._session._objects.get('actions').get(name)

class AccessProxy(object):
	_models = {}
	def __init__(self,session):
		self._session = session
		
	def get(self,name):
		return	self._session._access.get('models').get(name)

class Session(Component):
	_lang2id = {}
	def _mcache(self,args):
		if args[0] == 'cache':
			return self._cache[args[1]]._mcache(**(args[2]))
		elif args[0] == 'on_selected':
			return self._cache[args[1]]._on_selected(**(args[2]))
		elif args[0] == 'm2ofind':			
			return self._cache[args[1]]._m2o_find(**(args[2]))
		elif args[0] == 'relatedfind':			
			return self._cache[args[1]]._related_find(**(args[2]))
		elif args[0] == 'action':			
			return self._cache[args[1]]._action(**(args[2]))
		elif args[0] == 'add':			
			return self._cache[args[1]]._call('_o2m_add',args[2])
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
			return self._cache[args[1]]._do_modify(**(args[2]))
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
			kwargs = {'cr':self._cursor,'pool':self._models,'uid':self._uid,'session':self}
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
	_objects = {}
	_auths = {}
	_access = {}
	_cache = {}
	_cache_attrs = {}

	def __init__(self,config_file):
		cf = ConfigParser()
		cf.read(config_file)
		self._conf = configManagerDynamic(cf,{'dsn':None,'database':None,'host':'localhost','port':26257,'user':None,'password':None,'sslmode':None,'sslrootcert':None,'sslrootkey':None,'sslcert':None,'sslkey':None},ikey=['port'])
	
		self._proxy_models = ModelProxy(self)
		self._proxy_triggers = TrigerProxy(self)
		self._proxy_actions = ActionProxy(self)
		self._proxy_access = AccessProxy(self)
	
	def _call(self,args):
		rmsg = []
		args0 = args[0]
		if args0 in ('_cache',):
			rc = self._mcache(args[1:])
		elif args0 in ('dashboards','models','reports','queries','dialogs','wizards'):
			rc = self._components['objs']._call(args[1:])
		elif args0 == 'uis':
			rc = self._components['uis']._call(args[1:])
		elif args0 == 'modules':
			if self._connected:
				self._components['modules']._setup(self)
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
			rmsg.extend(rc)
		else:
			rmsg.append(rc)
		
		return rmsg

	@property
	def _dashboards(self):
		if 'dashboards' in self._objects:
			return	self._objects['dashboards']
		return {}

	@property
	def _models(self):
		if 'models' in self._objects:
			return	self._objects['models']
		return {}

	@property
	def _reports(self):
		if 'reports' in self._objects:
			return	self._objects['reports']
		return {}

	@property
	def _dialogs(self):
		if 'dialogs' in self._objects:
			return	self._objects['dialog']
		return {}

	@property
	def _wizards(self):
		if 'wizards' in self._objects:
			return	self._objects['wizards']
		return {}

	@property
	def _queries(self):
		if 'queries' in self._objects:
			return	self._objects['queries']
		return {}

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
			self._registry._setup(self)
			self._registry._load_module('bc')
			self._objects = self._components['registry']._create_loaded_objects(self)
			for key in self._components.keys():
				if hasattr(self._components[key],'_setup'):
					self._components[key]._setup(self)

			self._components['uis']._setup(self)
			return self

		self._cursor = None

	def _setLangs(self):
		for lang in self._models.get('bc.langs').select(['code','description']):
			self._lang2id[lang['code']] = lang['id']
	
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
					for key in self._models.keys():
						if res[2]:
							self._access.setdefault('models',{})[key] = Access(read=True,write=True,create=True,unlink=True,modify=True,insert=True,select=True,update=True,delete=True,upsert=True,browse=True,selectbrowse=True)
						else:
							self._access.setdefault('models',{})[key] = Access(read=True,write=False,create=False,unlink=False,modify=False,insert=False,select=True,update=False,delete=False,upsert=False,browse=True,selectbrowse=True)
							

					db_infos = self._models.get('bc.modules').select(fields=['code','state'],cond=[],context={})
					for db_info in db_infos:
						self._components['registry']._modules[db_info['code']]['db_id'] = db_info['id']
						self._components['registry']._modules[db_info['code']]['state'] = db_info['state']
	
					#web_pdb.set_trace()
					self._components['registry']._load_installed_modules()
					self._objects = self._components['registry']._create_loaded_objects(self)
					self._components['registry']._load_inheritables()					  
					for key in self._models.keys():
						if res[2]:
							self._access.setdefault('models',{})[key] = Access(read=True,write=True,create=True,unlink=True,modify=True,insert=True,select=True,update=True,delete=True,upsert=True,browse=True,selectbrowse=True)
						else:
							self._access.setdefault('models',{})[key] = Access(read=True,write=False,create=False,unlink=False,modify=False,insert=False,select=True,update=False,delete=False,upsert=False,browse=True,selectbrowse=True)
	
					self._setLangs()
					return [self._connected,self._uid,{'country_timezones':dict(pytz.country_timezones),'country_names':dict(pytz.country_names),'langs':self._models.get('bc.langs').select(['code','description']),'preferences':self._models.get('bc.user.preferences').select(['user_id','lang','country','framework','timezone']),'frameworks':self._models.get('bc.web.frameworks').select(['code','descr'])}]
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
	_objects = {}
	_access = {}
	_auths = {}
	_cache = {}
	_cache_attrs = {}
	
	def __init__(self,config_file):
		cf = ConfigParser()
		cf.read(config_file)
		self._conf = configManagerDynamic(cf,{'dsn':None,'database':None,'host':'localhost','port':26257,'user':'system','password':None,'sslmode':None,'sslrootcert':None,'sslrootkey':None,'sslcert':None,'sslkey':None},ikey=['port'])
		#print('CONG:',self._conf)
		self._proxy_models = ModelProxy(self)
		self._proxy_triggers = TrigerProxy(self)
		self._proxy_actions = ActionProxy(self)
		self._proxy_access = AccessProxy(self)


	def _call(self,args):
		res = []
		args0 = args[0]
		if args0 == 'modules':
			if self._connected:
				self._components['modules']._setup(self)
				rc = self._components['modules']._call(args[1:])
			else:
				rc = [False,'Not logged']
			#rc = self._components['modules']._call(args[1:])
		elif args0 in ('dashboards','models','reports','queries','dialogs','wizards'):
			rc = self._components['objs']._call(args[1:])
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

	@property
	def _dashboards(self):
		if 'dashboards' in self._objects:
			return	self._objects['dashboards']
		return {}

	@property
	def _models(self):
		if 'models' in self._objects:
			return	self._objects['models']
		return {}

	@property
	def _reports(self):
		if 'reports' in self._objects:
			return	self._objects['reports']
		return {}

	@property
	def _dialogs(self):
		if 'dialogs' in self._objects:
			return	self._objects['dialog']
		return {}

	@property
	def _wizards(self):
		if 'wizards' in self._objects:
			return	self._objects['wizards']
		return {}

	@property
	def _queries(self):
		if 'queries' in self._objects:
			return	self._objects['queries']
		return {}

	def _setLangs(self):
		for lang in self._models.get('bc.langs').select(['code','description']):
			self._lang2id[lang['code']] = lang['id']

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
			self._getUid()
			for key in self._components.keys():
				if hasattr(self._components[key],'_setup'):
					self._components[key]._setup(self)

			self._registry = self._components['registry']
			self._components['registry']._load_modules()
			self._objects = self._components['registry']._create_loaded_objects(self)
			

			for key in self._models.keys():
				self._models[key]._access = Access(read=True,write=True,create=True,unlink=True,modify=True,insert=True,select=True,update=True,delete=True,upsert=True,browse=True,selectbrowse=True)
			
			# self._getUid()
			# for key in self._components.keys():
				# if hasattr(self._components[key],'_setup'):
					# self._components[key]._setup(self)
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
				self._cursor.execute("CREATE DATABASE IF NOT EXISTS %s ENCODING='UTF-8'" % (name,))
				self._cursor.execute("SET DATABASE=%s" % (name,))
				
				self._cursor.conn.autocommit = autocommit

				rmsg.append(self._cursor.cr.statusmessage)
				rmsg.extend(self._components['modules']._call(['sysinstall']))
				self._cursor.execute("GRANT ALL ON TABLE %s.* TO %s WITH GRANT OPTION" % (name,db_user))
				self._cursor.commit()
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
			self._cursor.commit()
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

					self._components['registry']._load_installed_modules()
					self._objects = self._components['registry']._create_loaded_objects(self)

					for key in self._components.keys():
						if hasattr(self._components[key],'_setup'):
							self._components[key]._setup(self)

					for key in self._models.keys():
						self._access.setdefault('models',{})[key] = Access(read=True,write=True,create=True,unlink=True,modify=True,insert=True,select=True,update=True,delete=True,upsert=True,browse=True,selectbrowse=True)

					db_infos = self._models.get('bc.modules').select(fields=['code','state'],cond=[])
					for db_info in db_infos:
						self._components['registry']._modules[db_info['code']]['db_id'] = db_info['id']
						self._components['registry']._modules[db_info['code']]['state'] = db_info['state']

				#self._components['registry']._load_inheritables()
				#models = self._components['registry']._create_loaded_models()

				for key in self._models.keys():
					self._access.setdefault('models',{})[key] = Access(read=True,write=True,create=True,unlink=True,modify=True,insert=True,select=True,update=True,delete=True,upsert=True,browse=True,selectbrowse=True)
		
		self._setLangs()
		
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
