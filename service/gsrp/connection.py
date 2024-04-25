# --*-- coding: utf-8 --*--
import json
import psycopg2
import psycopg2.extras
from psycopg2.errors import SerializationFailure
import uuid
from functools import reduce
import logging
import time
import random
import web_pdb

from psycopg2.extras import register_json
register_json(oid=3802, array_oid=0)

_logger = logging.getLogger(__name__)

class Cursor(object):
	conn =None
	cr = None
	query = None
	def __init__(self, dsn = None, database = 'system', user = 'root', password = None, host = 'localhost', port=26257, sslmode = None, sslrootcert = None, sslrootkey = None, sslcert = None,sslkey = None):
		self.dsn = dsn
		self.database = database
		self.user = user
		self.password = password
		self.host = host
		self.port = port
		self.sslmode = sslmode
		self.sslrootcert = sslrootcert
		self.sslrootkey = sslrootkey
		self.sslcert = sslcert
		self.sslkey=sslkey
		self.query = []
		#print('cursor',self.sslmode,self.sslrootcert,self.sslcert,self.sslkey)

	def __reduce__(self):
		return(self.dsn,self.database,self.user,self.passowrd,self.host,self.port,self.sslmode,self.sslcert,self.sslkey)

	def _connect(self):
		if not self.conn or self.conn and self.conn.closed:
			if self.sslmode:
				if self.user == 'root':
					if self.dsn:
						self.conn = psycopg2.connect(dsn = self.dsn)
					else:
						self.conn = psycopg2.connect(dsn = self.dsn, database = self.database, user = self.user, host = self.host, port = self.port, connection_factory = psycopg2.extensions.connection,sslmode=self.sslmode,sslrootcert=self.sslrootcert,sslcert=self.sslcert,sslkey=self.sslkey)
				else:
					#self.conn = psycopg2.connect(dsn = self.dsn, database = self.database, user = self.user, password = self.password, host = self.host, port = self.port, connection_factory = psycopg2.extensions.connection,sslmode=self.sslmode,sslrootcert=self.sslrootsert,sslcert=self.sslcert,sslkey=self.sslkey)
					if self.dsn:
						self.conn = psycopg2.connect(dsn = self.dsn)
					else:
						self.conn = psycopg2.connect(dsn = self.dsn, database = self.database, user = self.user, password = self.password, host = self.host, port = self.port, connection_factory = psycopg2.extensions.connection,sslmode=self.sslmode,sslrootcert=self.sslrootcert,sslcert=self.sslcert,sslkey=self.sslkey)
			else:
				if self.user == 'root':
					if self.dsn:
						self.conn = psycopg2.connect(dsn = self.dsn)
					else:
						self.conn = psycopg2.connect(dsn = self.dsn, database = self.database, user = self.user, host = self.host, port = self.port, connection_factory = psycopg2.extensions.connection)
				else:
					if self.dsn:
						self.conn = psycopg2.connect(dsn = self.dsn)
					else:
						self.conn = psycopg2.connect(dsn = self.dsn, database = self.database, user = self.user, password = self.password, host = self.host, port = self.port, connection_factory = psycopg2.extensions.connection)
			#self.conn.set_session(False)
			self.conn.autocommit = False

		return self.conn.closed == 0

	@property
	def rowcount(self):
		return self.cr.rowcount
	
	def _cursor(self):
		if self.conn and self.conn.closed == 0:
			self.cr = self.conn.cursor()
			return self.cr.closed == 0
		return self.conn

#	def run_commit(self, op, q, v, max_retries=3):
	def run_commit(self, max_retries=3):
		"""
		Execute the operation *op(conn)* retrying serialization failure.
	
		If the database returns an error asking to retry the transaction, retry it
		*max_retries* times before giving up (and propagate it).
		"""
		# leaving this block the transaction will commit or rollback
		# (if leaving with an exception)
		#with conn:
		for retry in range(1, max_retries + 1):
			try:
				self.conn.commit()
				self.query.clear()
				return True


			except SerializationFailure as e:
				# This is a retry error, so we roll back the current
				# transaction and sleep for a bit before retrying. The
				# sleep time increases for each failed transaction.
				logging.debug("got error: %s", e)
				self._rollback()
				logging.debug("EXECUTE SERIALIZATION_FAILURE BRANCH")
				sleep_ms = (2 ** retry) * 0.1 * (random.random() + 0.5)
				logging.debug("Sleeping %s seconds", sleep_ms)
				time.sleep(sleep_ms)
				for f,q,v in self.query:
					if f in ('execute','executemany'):
						fun = getattr(self,f,None)
						fun(q,v)

			except psycopg2.Error as e:
				self._rollback()
				self.query.clear()
				_logger.error('query:%s vars:%s' % (q,v))
				_logger.debug("got error: %s", e)
				_logger.debug("EXECUTE NON-SERIALIZATION_FAILURE BRANCH")
				self._rollback()
				self.query.clear()
				raise e

		self._rollback()
		self.query.clear()
		raise ValueError(f"Transaction did not succeed after {max_retries} retries")

	def mogrify(self, query, vars):
		if type(query) == str:
			return self.cr.mogrify(query,vars)
		elif  type(query) in (tuple,list):
			res = []
			for q1 in query:
				res.append(self.cr.mogrify(q1,vars))

			return res

	def execute(self, query, vals = None):
		try:
			if type(query) == str:
				self.cr.execute(query = query, vars = vals)
				self.query.append(('execute',query,vals))
				#print('EXECUTE:',self.mogrify(query,vals))
			elif type(query) in (tuple,list):
				for q1 in query:
					#print('EXECUTE:',self.mogrify(q1,vals))
					self.cr.execute(query = q1, vars = vals)
					self.query.append(('execute',q1,vals))
		except:
			self._rollback()
			self.query.clear()
			#print('query: %s %s' % (query,vals))
			_logger.error('query: %s %s' % (query,vals))
			raise

		return True
	
	def executemany(self, query, vars_list):
		try:
			self.cr.executemany(query = query, vars_list = vars_list)
			self.query.append(('executemany',query,vars_list))
		except:
			self._rollback()
			self.query.clear()
			raise

	def _commit(self):
		if self.conn and not self.conn.closed:
			return self.run_commit()
			#self.conn.commit()
			#return True
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
		for idx,descr in enumerate(self.cr.description):
			dm[descr.name] = idx

		fm = {}
		for i, field in enumerate(fields):
			if type(field) == str:
				fm[field] = i
			elif type(field) == dict:
				for k in field.keys():
					fm[k] = i

		#web_pdb.set_trace()
		row = []
		for field in fields:
			if type(field) == str:
				if field in descfields:
					if columnsmeta[field] in ('many2one','referenced','related'):
						row.append({'id':record[dm[field]]})
					elif columnsmeta[field] in ('one2many','many2many'):
						row.append([])
					elif columnsmeta[field] in ('json','jsonb') and type(record[dm[field]]) == str:
						row.append(json.loads(record[dm[field]]))
					else:
						row.append(record[dm[field]])
				elif type(field) == dict:
					for k in field:
						if columnsmeta[k] in ('many2one','referenced','related'):
							row.append({'id':record[dm[k]]})
						elif columnsmeta[k] in ('one2many','many2many'):
							row.append([])
						elif columnsmeta[field] in ('json','jsonb') and type(record[dm[field]]) == str:
							row.append(json.loads(record[dm[field]]))
						else:
							row.append(record[dm[k]])					
			else:
				if type(field) == str:
					if columnsmeta[field] in ('one2many','many2many'):
						row.append([])
				elif type(field) == dict:
					for k in field:
						if columnsmeta[k] in ('one2many','many2many'):
							row.append([])

		for j in range(len(descfields)):
			desc = descfields[j]
			if desc in fields:
				continue
			
			n = desc.split('-')
			if len(n) > 1 and n[0] in columnsmeta and columnsmeta[n[0]] in ('many2one','referenced','related'):
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
			record = {}
			for idx,field in enumerate(fields):
					record[field] = row[idx]

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
				for idx,field in enumerate(fields):
						record[field] = rec[idx]

				records.append(record) 

		return tuple(records)

	def fetchall(self, fields = ['id'], columnsmeta = {'id':'uuid'}):
		records = []
		if self.cr.rowcount > 0:
			descfields = list(map(lambda x: x.name,self.cr.description))
			for record in self.cr.fetchall():
				records.append(tuple(self._convertRecord(record,fields,columnsmeta,descfields)))
		return tuple(records)

	def dictfetchall(self, fields = ['id'], columnsmeta = {'id':'uuid'}):
		records = []
		if self.cr.rowcount > 0:
			descfields = list(map(lambda x: x.name,self.cr.description))
			for row in self.cr.fetchall():
				rec = self._convertRecord(row,fields,columnsmeta,descfields)
				record = {}
				for idx,field in enumerate(fields):
						record[field] = rec[idx]

				records.append(record) 

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
