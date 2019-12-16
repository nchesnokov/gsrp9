# --*-- coding: utf-8 --*--

import psycopg2
import psycopg2.extras
import uuid
from functools import reduce
import logging

from psycopg2.extras import register_json
register_json(oid=3802, array_oid=0)

_logger = logging.getLogger(__name__)

class Connection(object):
	conn =None
	__cursors__ = {}
	def __init__(self, dsn = None, database = 'system', user = 'root', password = None, host = 'ec2-52-88-6-233.us-west-2.compute.amazonaws.com', port=26257):
		self.dsn = dsn
		self.database = database
		self.user = user
		self.password = password
		self.host = host
		self.port = port

	def __reduce__(self):
		return(self.dsn,self.database,self.user,self.passowrd,self.host,self.port)

	def connect(self):
		if not self.conn or self.conn and self.conn.closed:
			self.conn = psycopg2.connect(dsn = self.dsn, database = self.database, user = self.user, password = self.password, host = self.host, port = self.port, connection_factory = psycopg2.extensions.connection)
		return self.conn.closed == 0

	def cursor(self):
		guid = uuid.uuid4().hex
		self.__cursors__[guid] = self.conn.cursor()
		return guid

	def mogrify(self, guid, query, vars):
		return self.__cursors__[guid].mogrify(query,vars)

	def execute(self, guid, query, vars = None):
		try:
			#print('sql query:',query,vars)
			self.__cursors__[guid].execute(query = query, vars = vars)
		except:
			self._rollback()
			print('sql query:',query,vars)
			raise
	
	def executemany(self, guid, query, vars_list):
		try:
			self.__cursors__[guid].execute(query = query, vars_list = vars_list)
		except:
			self._rollback()
			raise

	def _commit(self):
		if self.conn and not self.conn.closed:
			self.conn.commit()
			return True
		else:
			return False

	def _rollback(self):
		if self.conn and not self.conn.closed:
			self.conn.rollback()
			return True
		else:
			return False

	def rollback(self):
		return self._rollback()

	def commit(self):
		return self._commit()

	def fetchone(self, guid):
		record = ()
		cr = self.__cursors__[guid]
		if cr.rowcount > 0:
			record = cr.fetchone()
		return record

	def dictfetchone(self, guid):
		record = {}
		cr = self.__cursors__[guid]
		if cr.rowcount > 0:
			row = cr.fetchone()
			for i in range(cr.description.__len__()):
				record[cr.description[i].name] = row[i]
		return record

	def fetchmany(self, guid, size = None):
		cr = self.__cursors__[guid]
		if not size:
			size = cr.arraysize
		return cr.fetchmany(size = size)

	def dictfetchmany(self, guid, size = None):
		cr = self.__cursors__[guid]
		if not size:
			size = cr.arraysize
		records = []
		if cr.rowcount > 0:
			for row in cr.fetchmany(size=size):
				record = {}
				for i in range(cr.description.__len__()):
					record[cr.description[i].name] = row[i]
				records.append(record)
		return records

	def fetchall(self, guid):
		return self.__cursors__[guid].fetchall()

	def dictfetchall(self, guid):
		records = []
		cr = self.__cursors__[guid]
		if cr.rowcount > 0:
			for row in cr.fetchall():
				record = {}
				for i in range(cr.description.__len__()):
					record[cr.description[i].name] = row[i]
				records.append(record)
		return records

	def cursor_close(self,cr):
		if cr in self.__cursors__:
			if self.__cursors__[cr].closed == 0:
				self.__cursors__[cr].close()
			del self.__cursors__[cr]
			return True
		else:
			return False

	def cursor_closeall(self):
		for key in self.__cursors__.keys():
			if self.__cursors__[key].closed == 0:
				self.__cursors__[key].close()
		self.__cursors__ = {}

	def disconnect(self):
		self.cursor_closeall()
		if self.conn.closed == 0:
			self.conn.close()
		self.conn = None

class Cursor(object):
	conn =None
	cr = None
	def __init__(self, dsn = None, database = 'system', user = 'root', password = None, host = 'localhost', port=26257, sslmode = None, sslcert = None,sslkey = None):
		self.dsn = dsn
		self.database = database
		self.user = user
		self.password = password
		self.host = host
		self.port = port
		self.sslmode = sslmode
		self.sslcert = sslcert
		self.sslkey=sslkey

	def __reduce__(self):
		return(self.dsn,self.database,self.user,self.passowrd,self.host,self.port,self.sslmode,self.sslcert,self.sslkey)

	def _connect(self):
		if not self.conn or self.conn and self.conn.closed:
			if self.sslmode:
				self.conn = psycopg2.connect(dsn = self.dsn, database = self.database, user = self.user, password = self.password, host = self.host, port = self.port, connection_factory = psycopg2.extensions.connection,sslmode=self.sslmode,sslcert= self.sslcert,sslkey=self.sslkey)
			else:
				self.conn = psycopg2.connect(dsn = self.dsn, database = self.database, user = self.user, password = self.password, host = self.host, port = self.port, connection_factory = psycopg2.extensions.connection)
			self.conn.autocommit=True

		return self.conn.closed == 0

	@property
	def rowcount(self):
		return self.cr.rowcount
	
	def _cursor(self):
		if self.conn and self.conn.closed == 0:
			self.cr = self.conn.cursor()
			return self.cr.closed == 0
		return self.conn

	def mogrify(self, query, vars):
		return self.cr.mogrify(query,vars)

	def execute(self, query, vals = None):
		try:
			#print('sql query:',query,vals)
			print('mogrify:',self.mogrify(query,vals))
			self.cr.execute(query = query, vars = vals)
		except psycopg2.Error as e:
			self._rollback()
			_logger.error('SQL Query: %s\n VALS: % s' % (query,vals))
			_logger.error('SQL Query mogrify: %s' % (self.mogrify(query,vals),))
			raise
	
	def executemany(self, query, vars_list):
		try:
			self.cr.execute(query = query, vars_list = vars_list)
		except:
			self._rollback()
			raise

	def _commit(self):
		if self.conn and not self.conn.closed:
			self.conn.commit()
			return True
		else:
			return False

	def _rollback(self):
		if self.conn and not self.conn.closed:
			self.conn.rollback()
			return True
		else:
			return False

	def open(self):
		return self._connect() and self._cursor()

	def rollback(self):
		return self._rollback()

	def commit(self):
		return self._commit()

	def _convertRecord(self,record,fields,columnsmeta,descfields):
		if self.cr.rowcount <= 0:
			return []

		if 'id' in descfields:
			if not 'id' in fields:
				fields.insert(0,'id')
			if not 'id' in columnsmeta:
				columnsmeta['id'] = 'uuid'
		
		dm = {}
		for i in range(self.cr.description.__len__()):
			dm[self.cr.description[i].name] = i

		fm = {}
		for i in range(fields.__len__()):
			if type(fields[i]) == str:
				fm[fields[i]] = i
			elif type(fields[i]) == dict:
				for k in fields[i]:
					fm[k] = i

		row = []
		for field in fields:
			if type(field) == str:
				if field in descfields:
					if columnsmeta[field] in ('many2one','related'):
						row.append({'id':record[dm[field]]})
					elif columnsmeta[field] in ('one2many','many2many'):
						row.append([])
					else:
						row.append(record[dm[field]])
				elif type(field) == dict:
					for k in field:
						if columnsmeta[k] in ('many2one','related'):
							row.append({'id':record[dm[k]]})
						elif columnsmeta[k] in ('one2many','many2many'):
							row.append([])
						elif columnsmeta[k] =='function':
							row.append(None)
						else:
							row.append(record[dm[k]])					
			else:
				if type(field) == str:
					if columnsmeta[field] in ('one2many','many2many'):
						row.append([])
					elif columnsmeta[field] =='function':
						row.append(None)
				elif type(field) == dict:
					for k in field:
						if columnsmeta[k] in ('one2many','many2many'):
							row.append([])
						elif columnsmeta[k] =='function':
							row.append(None)

		for j in range(len(descfields)):
			desc = descfields[j]
			if desc in fields:
				continue
			
			n = desc.split('-')
			if len(n) > 1 and n[0] in columnsmeta and columnsmeta[n[0]] in ('many2one','related'):
				if n[0] in fm:
					idx = fm[n[0]]
					row[idx]['name'] = record[j]

		return row

	def fetchone(self, fields = ['id'], columnsmeta = {'id':'uuid'}):
		if self.cr.rowcount > 0:
			descfields = list(map(lambda x: x.name,self.cr.description))
			return tuple(self._convertRecord(self.cr.fetchone(),fields,columnsmeta,descfields))
		return [tuple()]

	def dictfetchone(self, fields = ['id'], columnsmeta = {'id':'uuid'}):
		record = {}
		if self.cr.rowcount > 0:
			descfields = list(map(lambda x: x.name,self.cr.description))
			row =  self._convertRecord(self.cr.fetchone(),fields,columnsmeta,descfields)
			for i in range(fields.__len__()):
				#print('DICTFETCHONE:',i,fields,row)
				if type(fields[i]) == str:
					record[fields[i]] = row[i]
				elif type(fields[i]) == dict:
					for k in fields[i]:
						record[k] = row[i]
		#print('DICTFETCHONE:',record)
		return [record]

	def fetchmany(self, fields = ['id'], columnsmeta = {'id':'uuid'}, size = None):
		records = []
		if not size:
			size = self.cr.arraysize
		if self.cr.rowcount > 0:
			descfields = list(map(lambda x: x.name,self.cr.description))
			for record in self.cr.fetchmany(size = size):
				records.append(tuple(self._convertRecord(record,fields,columnsmeta,descfields)))
		#print('FETCHMANY:',record)
		return records

	def dictfetchmany(self, fields = ['id'], columnsmeta = {'id':'uuid'}, size = None):
		records = []
		if not size:
			size = self.cr.arraysize
		if self.cr.rowcount > 0:
			descfields = list(map(lambda x: x.name,self.cr.description))
			for row in self.cr.fetchmany(size = size):
				rec = self._convertRecord(row,fields,columnsmeta,descfields)
				record = {}
				for i in range(fields.__len__()):
					if type(fields[i]) == str:
						record[fields[i]] = rec[i]
					elif type(fields[i]) == dict:
						for k in fields[i]:
							record[k] = rec[i]
				records.append(record) 
		#print('DICTFETCHMANY:',record)
		return tuple(records)

	def fetchall(self, fields = ['id'], columnsmeta = {'id':'uuid'}):
		records = []
		if self.cr.rowcount > 0:
			descfields = list(map(lambda x: x.name,self.cr.description))
			for record in self.cr.fetchall():
				records.append(tuple(self._convertRecord(record,fields,columnsmeta,descfields)))
		#print('FETCHALL:',record)
		return tuple(records)

	def dictfetchall(self, fields = ['id'], columnsmeta = {'id':'uuid'}):
		records = []
		if self.cr.rowcount > 0:
			descfields = list(map(lambda x: x.name,self.cr.description))
			for row in self.cr.fetchall():
				rec = self._convertRecord(row,fields,columnsmeta,descfields)
				record = {}
				for i in range(fields.__len__()):
					if type(fields[i]) == str:
						record[fields[i]] = rec[i]
					elif type(fields[i]) == dict:
						for k in fields[i].keys():
							if columnsmeta[k] in ('many2one','related'):
								record[k] = rec[i]

				records.append(record) 
		
		#print('DICTFETCHALL:',records,tuple(records))
		return tuple(records)

	def close(self):
		if self.cr.closed == 0 and self.conn.closed == 0:
			self._rollback()
		if self.cr.closed == 0:
				self.cr.close()
		if self.cr.closed:
			if self.conn.closed == 0:
				self.conn.close()
		return self.cr.closed and self.conn.closed

	
if __name__ == "__main__":
	conn = Cursor(host="ec2-54-213-127-156.us-west-2.compute.amazonaws.com")
	conn.open()
	conn.execute("set database=pg_catalog")
	conn.execute("select schemaname,tablename from pg_tables")
	d=conn.dictfetchall()
	conn.close()
	print(d)
	
	conn=Connection(host="ec2-54-213-127-156.us-west-2.compute.amazonaws.com")
	conn.connect()
	cr=conn.cursor()
	conn.execute(cr,"set database=pg_catalog")
	conn.execute(cr,"select schemaname,tablename from pg_tables")
	d=conn.dictfetchall(cr)
	conn.disconnect()
	print(d)
