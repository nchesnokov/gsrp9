import os
import logging
from os.path import join as opj
from os import unlink
from functools import reduce
from configparser import ConfigParser
from serviceloader.tools.common import Component

_logger = logging.getLogger('listener.' + __name__)

class serviceslots_exception(Exception): pass

class Slots(Component):

	def __init__(self,config_file=None):
		if config_file:
			self.configure(config_file)
	
	def configure(self,config_file):
		cf = ConfigParser()
		cf.read(config_file)
		self._config = cf
	
	def _setup(self,session):
		self._session = session
	
	def _call(self, args):
		print('ServiceSids-execute:',args)
		if args[0][0] == '_':
			raise serviceslots_exception("The method <%s> of service <%s> is private. You can not call it remotely." % (args[1],self._name))

		rmsg = []
		method = getattr(self,args[0],None)
		if method and callable(method):
			kwargs = {'session':self._session}
			if len(args) > 1 and type(args[1]) == dict:
				for key in args[1].keys():
					print('args1-key:',args[1][key])
					kwargs[key] = args[1][key]
			rmsg.extend(method(**kwargs))
		return rmsg 

	def create(self,session,name,db_user):
		rmsg = []
		if name !='system':
			session._cursor.cr.execute("select count(*) from pg_catalog.pg_database where datname=%s" ,(name,))
			if session._cursor.cr.fetchone()[0] == 0:
				session._cursor.execute("CREATE DATABASE IF NOT EXISTS %s ENCODING='UTF-8'; SET DATABASE=%s;GRANT ALL ON DATABASE %s TO %s" % (name,name,name,db_user))
				_logger.info("Creating Slot: %s" % (name,))
				rmsg.append(session._components['modules']._call(['sysinstall']))
				_logger.info("Created Slot: %s" % (name,))
			else:
				_logger.info("Slot: %s are created" % (name,))
				rmsg.append("Slot: %s are created" % (name,))
		else:
			rmsg.append(Exception("Can`t create system sid. Name <system> is reserved."))

		#print('RMSG:',rmsg)
		return rmsg
	
	def drop(self, session,sid):
		res = []
		if sid != 'system':
			session.commit()
			session._cursor.conn.autocommit=True
			session._cursor.execute("DROP DATABASE IF EXISTS %s CASCADE" % (sid,))
			res.append(session._cursor.cr.statusmessage)
			#session._models.get('root.sids').delete(session._cursor,session._models,0,cond=[('name','=',sid)])
			session._cursor.conn.autocommit=False
			_logger.info("Drop Slot: %s" % (sid,))
			res.append(session._cursor.cr.statusmessage)
			return res
		else:
			_logger.info("Can`t drop Slot: %s" % (sid,))
			return [Exception("Can`t drop Slot: %s" % (sid,))]

	def initialize(self,session):
		session._cursor.execute("select count(*) as count from pg_catalog.pg_database where datname = 'root'")
		if session._cursor.rowcount > 0:
			#print('initialize',session._cursor.fetchone(['count'],{'count':'uuid'}))
			if session._cursor.fetchone(['count'],{'count':'integer'})[0] > 10:
				return ["System sids are initialize"]
		sqls = []
		sql = "create database if not exists root encoding='utf-8'"
		sqls.append(sql)
		sql = "set database = 'root'"
		sqls.append(sql)
		sql = 'create table if not exists sids (id serial primary key, name string unique, db_name string,db_host string,db_port int,db_user string,db_password string,dsn string,sslmode string,preload bool)'
		sqls.append(sql)
		
		session._cursor.commit()
		session._cursor.conn.autocommit=True
		session._cursor.execute(reduce(lambda x,y: x + ';' +y,sqls))
		session._cursor.conn.autocommit=True
		
		_logger.info("Slots initialize")		
		return [session._cursor.cr.statusmessage]
		
