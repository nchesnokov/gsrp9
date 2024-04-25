import os
import sys
import copy
import logging
from configparser import ConfigParser
import importlib
import uuid

_logger= logging.getLogger(__name__)

class Service(object): pass

class Component(object): pass

class configManager(dict):
	def __init__(self, cf,default_value,sections='fixed',bkey=[],ikey=[],fkey=[],lkey=[],tkey=[],dkey=[]):
		self._bkey=bkey
		self._ikey = ikey
		self._fkey = fkey
		self._lkey = lkey
		self._tkey = tkey
		self._dkey = dkey

		if sections == 'fixed':
			self.update(default_value)

		for s in cf.sections():
			if sections == 'dynamic':
				self[s] = copy.deepcopy(default_value)
			for (n,v) in  cf.items(s):
				if n in self[s] and n in self._bkey:
					v = cf.getboolean(s,n)
					if self[s][n] != v:
						self[s][n] = v
				elif n in self[s] and n in self._ikey:
					v = cf.getint(s,n)
					if self[s][n] != v:
						self[s][n] = v
				elif n in self[s] and n in self._fkey:
					v = cf.getfloat(s,n)
					if self[s][n] != v:
						self[s][n] = v
				elif n in self[s] and n in self._lkey:
					v = cf.get(s,n).split(',')
					if self[s][n] != v:
						self[s][n] = v
				elif n in self[s] and n in self._tkey:
					v = tuple(cf.get(s,n).split(','))
					if self[s][n] != v:
						self[s][n] = v
				elif n in self[s] and n in self._dkey:
					v = dict(map(lambda x: x.split(':'),cf.get(s,n).split(',')))
					if self[s][n] != v:
						self[s][n] = v
				elif n in self[s]:
					if len(v) > 0 and self[s][n] != v:
						self[s][n] = cf.get(s,n)
				else:
					_logger.info( 'Invalid parameter: - %s section: - %s - Ignored' % (n,s))
				
class configManagerFixed(configManager):
	def __init__(self, cf,default_value,bkey=[],ikey=[],fkey=[],lkey=[],tkey=[],dkey=[]):
		super(configManagerFixed,self).__init__(cf,default_value,sections='fixed',bkey=bkey,ikey=ikey,fkey=fkey,lkey=lkey,tkey=tkey,dkey=dkey)

class configManagerDynamic(configManager):
	def __init__(self, cf,default_value,bkey=[],ikey=[],fkey=[],lkey=[],tkey=[],dkey=[]):
		super(configManagerDynamic,self).__init__(cf,default_value,sections='dynamic',bkey=bkey,ikey=ikey,fkey=fkey,lkey=lkey,tkey=tkey,dkey=dkey)

class configManagerService(configManagerDynamic):
	def __init__(self, cf,bkey=[],ikey=[],fkey=[],lkey=[],tkey=[],dkey=[]):
		return super(configManagerService,self).__init__(cf,{'preload':False,'package':None,'service':None,'module':'serviceloader.tools.common','loader':'Loader','config_file':None,'type':'service','name':None,'path':None,'parent':None,'components_config_file':None,'services_config_file':None},bkey=bkey,ikey=ikey,fkey=fkey,lkey=lkey,tkey=tkey,dkey=dkey)

class Tree(dict):
	def __getitem__(self,key):
		k = key.find('.')
		if k == -1:
			return dict.__getitem__(self,key)
		else:
			return dict.__getitem__(self,key[:k])[key[k+1:]]

	def __setitem__(self,key,value):
		k = key.find('.')
		if k == -1:
			dict.__setitem__(self,key,value)
		else:
			if dict.__contains__(self,key[:k]) and type(dict.__getitem__(self,key[:k])) != Tree:
				raise TypeError
			self.setdefault(key[:k],Tree())[key[k+1:]] = value

class ServiceLoader(dict):

	def __init__(self,cf):
		self._services = Tree()
		self._components = Tree()
		self._tree = Tree()
		self._configs = cf
		self._load_services()

	def _open(self,args):
		name = args[0]
		kwargs = {}
		if len(args) == 2:
			kwargs = args[1] 
		o = self._tree[name].open(**kwargs)
		if o and type(o) not in (list,tuple,dict):
			i = uuid.uuid1(uuid.getnode()).hex
			self[i] = o
			return i
		
		return o

	def _close(self,args):
		oid = args[0]
		kwargs = args[1] 
		r = self[oid].close(**kwargs)
		del self[oid]		
		return r

	def _shutdown(self,args):
		name = args[0]
		kwargs = {}
		if len(args) == 2:
			kwargs = args[1] 

		oids = list(map(lambda x: x,filter(lambda y:y._name == name,self.keys())))
		for oid in oids:
			self[oid].shutdown(**kwargs)
			del self[oid]

		del self._tree[name]
		
		r = self._tree[name].shutdown(**kwargs)
		return r

	def _control(self):
		pass
		
	def _dispatch(self,args):
		rmsg = []	
		args0 = args[0]
		#print('DISPATCH-ARGS:',args)
		if args0 in self:
			if args[1][1] != '_':
				if len(args) >= 2:
					rmsg.extend(self[args0]._call(args[1:]))
			elif args[1] == '_close':
				rmsg.append(self._close(args[2:]))
			elif args[1] == '_shutdown':
				rmsg.extend(self._shutdown(args[2:]))
			else:
				rmsg.extend([Exception("Can`t call private method: %s " % (args[1],))]) 

		elif args0 == '0' * 32:
			if args[1] == '_open':
				o = self._open(args[2:])
				if type(o) == str:
					rmsg.append(o)
				else:
					rmsg.extend(o)

			elif args[1] in ('_services_list','_slots'):
				#rmsg.extend(self._slots(args[2:]))
				rmsg.extend(['test001','test002'])
			else:
				rmsg.extend([Exception("Not opened. Can`t call method: %s " % (args[0],))]) 
		else:		
			rmsg.extend([Exception("Not opened. Can`t call method: %s " % (args[0],))]) 

		#print('DISPATCH-RMSG:', rmsg)
		return rmsg

	@property
	def tree(self):
		return self._tree

	@property
	def service(self):
		return self._tree[list(self._tree.keys())[0]]

	def _services_list(self,args):
		return list(self._tree.keys())

	def _open_service(self,name,kwargs):
		if name in self._tree:
			srv = self._tree[name].open(**kwargs)
		else:
			if name in self._configs:
				self._load_module(name)
				srv = self._tree[name].open(**kwargs)
		if srv:
			_uuid=uuid.uuid1(uuid.getnode()).hex
			self[_uuid] = srv
			self._instancies.setdefault(name,set()).add(_uuid)
			return _uuid

	def _close_service(self,_uuid):
		if _uuid in self:
			name =  self[_uuid]._name
			r = self[_uuid].close()
			self._instancies[name].remove(_uuid)
			del self[_uuid]
			del self._tree[name]
			_logger.info('Instanse: %s of service: %s closed' % (name,_uuid))
			
			return r
		else:
			return [Exception("Close: Can`t exists object: %s" % (_uuid,))]
	
	def _shutdown_service(self,sid):
		if sid in self:
			name =  self[sid]
			r = self[sid].shutdown()
			del self[sid]
			_logger.info('Instanse: %s of service: %s shutdowned' % (name,sid))
			
			return r
		else:
			return [Exception("Shutdown:Can`t exists object: %s" % (sid,))]

	def _close_all_services(self):
		srvs = list(self.keys())
		_logger.info('All instanse of service closing')
		for srv in srvs:
			self[srv].close()
		
		_logger.info('All instanse of service closeded')

	def _shutdown_all_services(self):
		srvs = list(self.keys())
		_logger.info('All instanse of service shutdowning')
		for srv in srvs:
			self[srv].shutdown()
		
		_logger.info('All instanse of service shutdowned')

	def _load_services(self,services=None):
		res = []

		tree = Tree()

		if services is None:
			srvs = list(filter(lambda x: x != 'DEFAULT' and x not in self._tree,self._configs.keys()))
		else:
			srvs = list(filter(lambda x: x != 'DEFAULT' and x in self._configs and x not in self._tree,services))

		for srv in srvs:
			preload = self._configs[srv]['preload']
			if preload:
				self._load_service(srv)
				res.append(srv)
		
		_logger.info('Loaded objects: %s ' % (res,))
	
	def _reload_services(self,services=None):	
		res = []

		tree = Tree()

		if services is None:
			srvs = list(filter(lambda x: x != 'DEFAULT' and x not in self._tree,self._configs.keys()))
		else:
			srvs = list(filter(lambda x: x != 'DEFAULT' and x in self._configs and x not in self._tree,services))

		for srv in srvs:
			preload = self._configs[srv]['preload']
			if preload:
				self._reload_service(srv)
				res.append(srv)
		
		_logger.info('Reloaded servicies: %s ' % (res,))

	def _load_service(self,key):
		tp = self._configs[key]['type']
		package = self._configs[key]['package']
		service = self._configs[key]['service']
		name = self._configs[key]['name']
		path = self._configs[key]['path']
		parent = self._configs[key]['parent']
		preload = self._configs[key]['preload']
		config_file = self._configs[key]['config_file']
		services_config_file = self._configs[key]['services_config_file']
		components_config_file = self._configs[key]['components_config_file']
				
		module = self._configs[key]['module']
		loader = self._configs[key]['loader']
		g = globals()
		g[module] = __import__(module,globals=globals(),locals=locals(),fromlist=[loader],level=0)
		service_loader = getattr(g[module],loader,None)

		if service_loader:
			ldr = service_loader()		
			srv = ldr.load(package,service,config_file)
			self._tree[key] = srv

			if components_config_file:
				if not hasattr(srv,'_components'):
					srv._components = Tree()
				srv._components.update(_service_loader(components_config_file).tree)

			if services_config_file:
				if not hasattr(srv,'_services'):
					srv._services = Tree()

				srv._services.update(_service_loader(services_config_file).tree)
		else:
			raise Exception('Loader: <%s> of Module: <%s> not exists>' % (loader,module))
	
	def _reload_service(self,key):
		tp = self._configs[key]['type']
		package = self._configs[key]['package']
		service = self._configs[key]['service']
		name = self._configs[key]['name']
		path = self._configs[key]['path']
		parent = self._configs[key]['parent']
		preload = self._configs[key]['preload']
		config_file = self._configs[key]['config_file']
		services_config_file = self._configs[key]['services_config_file']
		components_config_file = self._configs[key]['components_config_file']
				
		module = self._configs[key]['module']
		loader = self._configs[key]['loader']
		g = globals()
		g[module] = __import__(module,globals=globals(),locals=locals(),fromlist=[loader],level=0)
		service_loader = getattr(g[module],loader,None)

		if service_loader:
			ldr = service_loader()		
			srv = ldr.load(package,service,config_file)
			self._tree[key] = srv

			if components_config_file:
				self._services[key] = _service_loader(components_config_file)

			if services_config_file:
				self._services[key] = _service_loader(services_config_file)
		else:
			raise Exception('Loader: <%s> of Module: <%s> not exists>' % (loader,module))


def _service_loader(config_file):
	cf = ConfigParser()
	cf.read(config_file)
	return ServiceLoader(configManagerService(cf))

def default_tree_service_loader(config_file):
	return _service_loader(config_file).tree

def default_service_loader(config_file):
	return _service_loader(config_file).service

class Loader(object):
	
	def load(self,package,service,config_file):
		g = globals()
		g[package] = __import__(package,fromlist=[service])
		srv = getattr(g[package],service,None)
		if srv:
			if config_file:
				obj = srv(config_file)
			else:
				obj = srv() 				
		else:
			raise Exception('Service: <%s> of module <%s> is not avalaible' % (service,package))
		
		if isinstance(obj,Service):
			to = 'service'
		elif isinstance(obj,Component):
			to = 'component'
		else:
			to = 'undefined'

		_logger.info('Loaded %s: %s from package: %s' % (to,service,package))

		return obj

class Dummy(Service):
	def __init__(self,config_file=None):
		if config_file:
			self.configure(config_file)
	
	def configure(self,config_file):
		cf = ConfigParser()
		cf.read(config_file)
		self._config = cf
