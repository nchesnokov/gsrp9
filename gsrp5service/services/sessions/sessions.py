import logging
import traceback
import uuid
import copy
from passlib.hash import pbkdf2_sha256
from .modules.registry import Registry
from .connection import Connection, Cursor
from .modules.modules import ServiceModules
from .sysmodules import ServiceSysModules
from .gens.gen import ServiceGen
from .slots.slots import ServiceSlots
from .ui.ui import ServiceUI
from .models.models import ServiceModels
from orm.model import Access
from .tree import Tree
from decimal import Decimal
from .cache import MCache

import pdb

_logger = logging.getLogger('listener.' + __name__)

class interface_exception(Exception): pass

class Service(dict):

	def __init__(self,*args,**kwargs):
		pass

	def open(self,*args,**kwargs):
		pass

	def close(self):
		pass

	def ioctl(self,*args,**kwargs):
		pass

	def _call(self,*args,**kwargs):
		pass

class Session(object): pass
class Slot(object): pass
class GroupSlot(object): pass

class Gsrp5Base(Service):
	_name = 'gsrp5'
	_path = 'gsrp5'
	
	def __init__(self,config,groups):
		self._config = config
		self._cr = None
		self._registry = Registry(self._config['paths'])
		self._pool = self._registry._models
		self._uid = None
		for group in groups:
			self[group._name] = group(self._cr,self._pool,self._uid,self._registry)

	def open(self):
		pass
	
	def close(self):
		self._cr.close()
		self._conn.close()
		self._cr = None
		self._conn = None
	
	def ioctl(self,args):
		name = args[0]
		method = getattr(self,'_ioctl_'+name,None)
		if method and callable(method):
			kwargs = args[1]
			return method(**kwargs)
		
		return Exception("Can`t call ioctl method: <%s>" % (name,))

	def _ioctl_opendb(self, dsn = None, database = 'system', user = 'root', password = None, host = 'localhost', port=26257, sslmode = None, sslrootcert = None, sslcert = None,sslkey = None):
		self._cr = Cursor(dsn,database,user,password,host,port,sslmode,sslrootcert,sslcert,sslkey)
		if self._cr.conn and self._cr.cr:
			return True
		
		return Exception("Can`t connect to db: <%s>" % (database,))
		
	def _call(self,args):
		if args[1][0] == '_':
			return [Exception('Can`t call private method: <%s>' % (args[1],))]
		else:
			if args[0] in self:
				obj = getattr(self[args[0]],args[1],None)
				if callable(obj):
					kwargs = args[2]
					return obj(**kwargs)
			else:
				return [Exception('Can`t call group of method: <%s>' % (args[0],))]
		

class Gsrp5System(Gsrp5Base):
	_name = 'gsrp5.system'
	_path = 'gsrp5.system'

class Gsrp5User(Gsrp5Base): 
	_name = 'gsrp5.user'
	_path = 'gsrp5.user'


class Gsrp5(dict):
	_name = 'gsrp5'
	_path = 'gsrp5'


class UserSession(Session):

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
	
	def __init__(self,tree,path,_uuid = None):
			
		self._sid = tree._get('gsrp5.slots.user.'+path.split('.')[-1])
		
		if _uuid:
			self._uuid= _uuid
		else:
			self._uuid= uuid.uuid1(uuid.getnode()).hex

	def open(self):
		
		conf = self._sid._conf

		if conf['sslmode']:
			self._cursor  = Cursor(dsn=conf['dsn'],database=conf['database'],host=conf['host'],port=conf['port'],user=conf['user'],password=conf['password'],sslmode=conf['sslmode'],sslrootcert=conf['sslrootcert'],sslcert=conf['sslcert'],sslkey=conf['sslkey'])
		else:
			self._cursor  = Cursor(dsn=conf['dsn'],database=conf['database'],host=conf['host'],port=conf['port'],user=conf['user'],password=conf['password'])

		if self._cursor.open():
			self._sid._sessions[self._uuid] = self
			for key in self._sid._srvs.keys():
				self._srvs[key] = self._sid._srvs[key]()
			#return [self._uuid]
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
		self._cache.clear()
		return ['Shutdown']

	def _service(self,args):
		if args[0] in self._srvs:
			return self._srvs[args[0]]._execute(args[1:])
		elif len(args) == 2 and args[1] in ('commit','close','shutdown','rollback'):
			if args[1] == 'cache':
				return self._mcache(args[1:])
			elif args[1] == 'commit':
				return self.commit()
			elif args[1] == 'close':
				return self.close()
			elif args[1] == 'shutdown':
				return self.shutdown()
			elif args[1] == 'rollback':
				return self.rollback()
		
		raise interface_exception("In session: %s service: %s not found" % (self._uuid,args[1]))

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
			#print('open:',oid)
			self._cache[oid] = MCache(**kwargs)
			return [oid]
		elif args[0] == 'getmode':
			return self._cache[args[1]]._getMode()
		elif args[0] == 'setmode':
			return self._cache[args[1]]._setMode(**(args[2]))
		elif args[0] == 'close':
			#print('close:',args[1],self._cache)
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

class SystemSession(Session):

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
	
	def __init__(self,tree,path,_uuid = None):
			
		self._sid = tree._get('gsrp5.slots.'+path.split('.')[-1])
		
		if _uuid:
			self._uuid= _uuid
		else:
			self._uuid= uuid.uuid1(uuid.getnode()).hex

	def open(self):

		conf = self._sid._conf
		if conf['sslmode']:
			self._cursor  = Cursor(dsn=conf['dsn'],database=conf['database'],host=conf['host'],port=conf['port'],user=conf['user'],password=conf['password'],sslmode=conf['sslmode'],sslcert=conf['sslcert'],sslkey=conf['sslkey'])
		else:
			self._cursor  = Cursor(dsn=conf['dsn'],database=conf['database'],host=conf['host'],port=conf['port'],user=conf['user'],password=conf['password'])

		if self._cursor.open():
			self._sid._sessions[self._uuid] = self
			for key in self._sid._srvs.keys():
				self._srvs[key] = self._sid._srvs[key]()

			for key in self._sid._models.keys():
				self._models[key] = self._sid._models[key]
				self._models[key]._access = Access(read=True,write=True,create=True,unlink=True,modify=True,insert=True,select=True,update=True,delete=True,upsert=True,browse=True,selectbrowse=True)
			return self
			#return [self._uuid]

		self._cursor = None

	def _call(self, args):
		return self._srvs[args[0]]._execute(obj,args[1:])
	
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

###########
class SystemSlot(Slot):

	_name = None
	_preload = False
	_connected = False
	_conf = None
	_installedmodules = []
	_models = {}
	_mom = {}
	_registry = None
	_sessions = {}
	_depends = None
	_srvs = {}
	_modules = {}

	def __init__(self, name, conf, srvs, paths, able ,preload = False):
		self._name = name
		self._preload = preload
		self._registry = Registry(paths,able)
		self._models = self._registry._createAllModels()
		self._mom = self._registry._mom
		self._depends = self._registry._depends
		self._conf = conf
		
		for key in srvs.keys():
			self._srvs[key] = srvs[key]
		
		for module in self._registry._modules.keys():
			self._modules[module] = self._registry._modules[module]

		if self._preload:
			self.loadall()

	def commit(self,guid):
		return self._sessions[guid].commit()
	
	def rolback(self,guid):
		return self._sessions[guid].rollback()

	def _execute(self,guid):
		return self._sessions[guid]._execute()

	def shutdown(self,guid):
		for key in self._sessions.keys():
			self._sessions[guid].shutdown()
	
	def open(self):
		if not self._preload and not self._connected:
			self._loadsysmodules()
		session = SystemSession(self)
		if session.open():
			self._sessions[session._uuid] = session	
			
		return session._uuid

	def login(self,guid,user,password):
		if self._name != 'system':
			return True
		else:
			return self._sessions[guid].login(user,password)

	def close(self,guid):
		self._sessions[guid].close()
		del self._sessions[guid]
		return True

	def loadall(self):
		self._loadsysmodules()
		self._loadautoinstallmodules()
		self._loadinstallmodules()
		self._loadnoinstallmodules()

	def _able(self,able):
		if type(able) == str:
			able = [able]
		m = []
		for key in self._modules.keys():
			if self._modules[key]['meta']['able'] in able:
				m.append(key)
		return m

	def _loadsysmodules(self):
		sysmodules = self._able('system')
		self._sysmodules = list(filter(lambda x: x in sysmodules,self._registry._dependsinstall))
		self._loadmodules(self._sysmodules)

	def _loadautoinstallmodules(self):
		autoinstallmodules = self._able('autoinstall')
		self._autoinstallmodules = list(filter(lambda x: x in autoinstallmodules,self._registry._dependsinstall))
		self._loadmodules(self._autoinstallmodules)

	def _loadinstallmodules(self):
		installmodules = self._able('install')
		self._installmodules = list(filter(lambda x: x in installmodules,self._registry._dependsinstall))
		self._loadmodules(self._installmodules)

	def _loadnoinstallmodules(self):
		noinstallmodules = self._able('noinstall')
		self._noinstallmodules = list(filter(lambda x: x in noinstallmodules,self._registry._dependsinstall))
		self._loadmodules(self._noinstallmodules)

	def _loadmodule(self, module):
		self._registry._load_module(module)

		self._mom = self._registry._mom

	def _loadmodules(self, modules):
		for module in modules:
			self._loadmodule(module)

		self._registry._mom = self._mom

	def _getModelOfModules(self, model,module):
		for m,c in self._mom.get(model):
			if m == module:
				return c
		return None

	def _download_module(self,name):
		models = self._modules[name]['lom']
		for model in models:
			mom = []
			for m in self._mom[model]:
				if m[0] == 'name':
					continue
				mom.append(m)
			if len(mom) > 0:
				self._mom[model] = mom
			else:
				del self._mom[model]

#############
class UserSlot(Slot):

	_name = None
	_preload = False
	_connected = False
	_conf = None
	_installedmodules = []
	_models = {}
	_mom = {}
	_registry = None
	_sessions = {}
	_depends = None
	_srvs = {}
	_modules = {}

	def __init__(self, name, conf, srvs, paths, able ,preload = False):
		self._name = name
		self._preload = preload
		self._registry = Registry(paths,able)
		self._models = self._registry._createAllModels()
		#self._mom = self._registry._mom
		self._depends = self._registry._depends
		self._conf = conf
		
		for key in srvs.keys():
			self._srvs[key] = srvs[key]
		
		for module in self._registry._modules.keys():
			self._modules[module] = self._registry._modules[module]

		if self._preload:
			self.loadall()

	def commit(self,guid):
		return self._sessions[guid].commit()
	
	def rolback(self,guid):
		return self._sessions[guid].rollback()

	def _execute(self,guid):
		return self._sessions[guid]._execute()

	def shutdown(self,guid):
		for key in self._sessions.keys():
			self._sessions[guid].shutdown()
	
	def open(self):
		if not self._preload and not self._connected:
			self._loadsysmodules()
		session = UserSession(self)
		if session.open():
			self._sessions[session._uuid] = session	
			
		return session._uuid

	def login(self,guid,user,password):
		if self._name != 'system':
			return True
		else:
			return self._sessions[guid].login(user,password)

	def close(self,guid):
		self._sessions[guid].close()
		del self._sessions[guid]
		return True

	def loadall(self):
		self._loadsysmodules()
		self._loadautoinstallmodules()
		self._loadinstallmodules()
		self._loadnoinstallmodules()

	def _able(self,able):
		if type(able) == str:
			able = [able]
		m = []
		for key in self._modules.keys():
			if self._modules[key]['meta']['able'] in able:
				m.append(key)
		return m

	def _loadsysmodules(self):
		sysmodules = self._able('system')
		self._sysmodules = list(filter(lambda x: x in sysmodules,self._registry._dependsinstall))
		self._loadmodules(self._sysmodules)

	def _loadautoinstallmodules(self):
		autoinstallmodules = self._able('autoinstall')
		self._autoinstallmodules = list(filter(lambda x: x in autoinstallmodules,self._registry._dependsinstall))
		self._loadmodules(self._autoinstallmodules)

	def _loadinstallmodules(self):
		installmodules = self._able('install')
		self._installmodules = list(filter(lambda x: x in installmodules,self._registry._dependsinstall))
		self._loadmodules(self._installmodules)

	def _loadnoinstallmodules(self):
		noinstallmodules = self._able('noinstall')
		self._noinstallmodules = list(filter(lambda x: x in noinstallmodules,self._registry._dependsinstall))
		self._loadmodules(self._noinstallmodules)

	def _loadmodule(self, module):
		self._registry._load_module(module)

		self._mom = self._registry._mom

	def _loadmodules(self, modules):
		for module in modules:
			self._loadmodule(module)

		self._registry._mom = self._mom

	def _getModelOfModules(self, model,module):
		for m,c in self._mom.get(model):
			if m == module:
				return c
		return None

	def _download_module(self,name):
		models = self._modules[name]['lom']
		for model in models:
			mom = []
			for m in self._mom[model]:
				if m[0] == 'name':
					continue
				mom.append(m)
			if len(mom) > 0:
				self._mom[model] = mom
			else:
				del self._mom[model]

class Dispatcher(dict):

	_null_uuid = '0' * 32
	_sysconfs = {}
	_confs = {}
	_syssids = {}
	_sids = {}
	_sysuuid = None
	_tree = None

	def __init__(self,configs):
		self._configs = configs
		self._tree = Tree('gsrp5')
		srvs = {'gens':ServiceGen,'slots':ServiceSlots,'sysmodules':ServiceSysModules,'modules':ServiceModules,'models': ServiceModels}
		self._tree._add('gsrp5.slots.system',SystemSlot(name = 'system', conf = self._configs['system'], srvs = srvs, paths = {'root':None,'addons':None}, able = ('root','system','autoinstall','install','noinstall'),preload = self._configs['system']['preload']))
		self._tree._add('gsrp5.sessions.system',SystemSession)
		self._sysuuid = self._open([{'path':'gsrp5.sessions.system'}])[0]
		self._load()

	def _slots(self,args):
		return [args[0],True,list(self._configs.keys())]

	def _open(self,args):
		kwargs = {'tree':self._tree}
		if len(args) == 1 and type(args[0]) == dict:
			for key in args[0].keys():
				kwargs[key] = args[0][key]
		session = self._tree._open(**kwargs)
		if session:
			_uuid=uuid.uuid1(uuid.getnode()).hex
			self[_uuid] = session
			return _uuid

	def _close(self, suid):
		try:
			_logger.info('Session: %s close' % (suid,))
			return self[suid].close()
		except:
			return [Exception("Can`t close object: %s" % (suid,))]
	
	def _shutdown(self,suid):
		try:
			return self[suid].shutdown()
		except:
			return [Exception("Can`t shutdown object: %s" % (suid,))]

	def _load(self):
		models = self[self._sysuuid]._sid._models
		cursor = self[self._sysuuid]._cursor
		for key in filter(lambda x: x not in ('globals','system'),self._configs.keys()):
			srvs = {'modules':ServiceModules,'models': ServiceModels,'ui':ServiceUI}
			self._tree._add('gsrp5.slots.user.'+key,UserSlot(name = key, conf = self._configs[key], srvs = srvs,paths = None,able=None, preload = self._configs[key]['preload']))
			self._tree._add('gsrp5.sessions.'+key,UserSession)
	
	def _reload(self):	
		models = self[self._sysuuid]._sid._models
		cursor = self[self._sysuuid]._cursor
		old_config_keys = list(filter(lambda x: x not in ('globals','system'),self._configs.keys()))
		self._configs._reload()
		new_config_keys = list(filter(lambda x: x not in ('globals','system'),self._configs.keys()))
		count_add = 0
		slots_for_add = list(set(new_config_keys) - set(old_config_keys))
		
		for key in slots_for_add:
			srvs = {'modules':ServiceModules,'models': ServiceModels}
			self._tree._add('gsrp5.slots.user.'+key,UserSlot(name = key, conf = self._configs[key], srvs = srvs,paths = None,able=None, preload = self._configs[key]['preload']))
			count_add += 1

		count_del = 0
		slots_for_delete = list(set(old_config_keys) - set(new_config_keys))
		for key in slots_for_delete:
			self._tree._remove('gsrp5.sessions.'+key)
			self._tree._remove('gsrp5.slots.'+key)
			del self._confs[key]
			count_del += 1
		
		_logger.info('Dispatcher reload slots: adds-%s,removes-%s' % (count_add,count_del))
		return [count_add,count_del,'Dispatcher slost reloaded']

	def _call(self,args,obj):
		if isinstance(obj,Session):
			return obj._srvs[args[0]]._execute(obj,args[1:])
		else:
			return [Exception("Object: %s no found" % (obj,))]

	
	def _dispatch(self,args):
		rmsg = []	
		#print('dispath-args:',args)
		args0 = args[0]
		if args0 in self:
			rmsg.extend(args[:1])
			rmsg.extend(self[args0]._call(args[2:]))
		else:
			if args0 == '_slots':
				rmsg.extend(self._slots(args[0:]))
			elif args0 == '_open':
				rmsg.append(self._open(args[2:]))
			elif args0 == '_close':
				rmsg.append(self._close(args[0]))
			elif args0 == '_shutdown':
				rmsg.extend(self._shutdown(args[0]))
			else:
				rmsg.extend([Exception("Not opened. Can`t call method: %s " % (args[0],))]) 

		return rmsg
