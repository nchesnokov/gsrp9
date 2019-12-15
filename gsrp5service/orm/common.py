# -*- coding: utf-8 -*-


LOG_ACCESS_COLUMNS = {
    'create_uid':' UUID REFERENCES bc_users (id)',
    'create_timestamp':' TIMESTAMP WITHOUT TIME ZONE',
    'write_uid':' UUID REFERENCES bc_users (id)',
    'write_timestamp':' TIMESTAMP WITHOUT TIME ZONE'
    }

MAGIC_COLUMNS = ['id']
MAGIC_COLUMNS.extend(LOG_ACCESS_COLUMNS.keys())
MAGIC_COLUMNS_INFO={'id':{'required':True,'db_type':'UUID','type':'uuid','label':'ID Record'}}

MAP_TYPES_FIELDS_TO_DB = {'boolean':'bool','char':'string','varchar':'string','integer':'integer' ,
'many2one': 'integer','text':'string','float':'float','double':'float','numeric':'decimal', 'decimal':'decimal', 
'binary':'bytes','selection':'string'}

FIELDS_TYPE_NO_DB = ('one2many','function','many2many')

RESTRCT_TYPE_DB = {'a':' NO ACTION','r':' RESTRICT','n':' SET NULL','c':' CASCADE','d':' SET DEFAULT'}

RESERVED_KYEWORD_POSTGRESQL = ['ALL', 'ANALYSE', 'ANALYZE', 'AND', 'ANY', 'ARRAY', 'AS', 'ASYMETRIC', 'BOTH', 'CASE', 'CAST','CHECK', 'COLUMN', 'CONCURENTLY',
'CONSTRAINT','CREATE','CROSS','CURRENT_CATALOG','CURRENT_DATE','CURRENT_ROLE','CURRENT_SCHEMA','CURRENT_TIME','CURRENT_TIMESTAMP','CURRENT_USER','DEFAULT', 
'DEFERABLE','DESC','DISTINCT','DO','ELSE','END','EXCEPT','FALSE','FAMILY','FETCH','FOR','FOREIGN','FREZZE','FROM','FULL','GRANT','GROUP','HAVING','ILIKE','IN','INOTIALLY',
'INTERSECT','INTO', 'IS','ISNULL','JOIN', 'LEADING','LEFT','LIMIT','LOCALTIME','LOCALTIMESTAMP','NATURAL','NOT','NOTNULL','NULL','OFFSET','ON','ONLY','OR','ORDER',
'OUTER','OVER','OVERLAPS','PLACING','PRIMARY','REFERENCES','RIGTH','SELECT','SESSION_USER','SIMULAR','SOME','SYMMETRIC','TABLE','THEN','TRAILING','TRUE','INION',
'UNIQUE','USER','USING','VERBOSE','WHEN','WHERE']

SQL_RESERVED_KEYWORDS = RESERVED_KYEWORD_POSTGRESQL

DEFAULT_MODEL_NAMES = {'rec_name':'name','full_name':'fullname', 'parent_id':'parent_id','childs_id':'childs_id','date':'date','from_date':'from_date','to_date':'to_date','from_time':'from_time','to_time':'to_time','start_date':'start_date','end_date':'end_date','sequence':'sequence','progress':'progress','project_type':'project_type','state':'state','inactive':'inactive','latitude':'latitude','longitude':'longitude','from_latitude':'from_latitude','from_longitude':'from_longitude','to_latitude':'to_latitude','to_longitude':'to_longitude'}

class TPath:

	_t = None
	
	def __init__(self,t):
		self._t = {}
		if type(t) == str:
			self._t[t] = {'parent':None}
		elif type(t) in (list,tuple):
			if len(t) == 1:
				self._t[t[0]] = {'parent':None}
			elif len(t) > 1:
				prev = t[0]
				self._t[prev] = {'parent':None}
				for k in t[1:]:
					self._t[k] = {'parent':prev}
					prev = k
				self._t[t[-1]] = {'parent':t[-2]}
		elif type(t) == dict:
			for k in t.keys():
				self._t[k] = {'parent':None}
				if type(t[k]) == dict:
					self._b(t[k],k)

	@property
	def t(self):
		return self._t

	def _b(self,t,p):
		for k in t.keys():
			self._t[k] = {'parent':p}
			if type(t[k]) == dict:
				self._b(t[k],k)
			elif type(t[k]) == str:
				self._t[t[k]] = {'parent':k}
				
	
	def path(self,p):
		if p in self._t:
			r = []
			s = self._t[p]
			while s and s['parent']:
				r.append(s['parent'])
				s = self._t[s['parent']]
			return r
