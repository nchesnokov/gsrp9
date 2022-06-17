from gsrp5service.orm import fields
from gsrp5service.orm.model import Model

from passlib.hash import pbkdf2_sha256

from gsrp5service.generate.loader import META

_GENERATEVIEW = META['_gens']

import pytz

import web_pdb

class bc_users(Model):
	_name = 'bc.users'
	_description = 'Users'
	_log_access = False
	_rec_name = 'login'
	_class_object = 'K'
	_columns = {
	'login': fields.varchar('Login', required = True, size = 64,readonly=True),
	'password': fields.varchar('Password', required = True,readonly=True),
	'firstname': fields.varchar('First Name', required = True, selectable = True,readonly=True),
	'lastname': fields.varchar('Last Name', required = True, selectable = True,readonly=True),
	'issuperuser': fields.boolean(label='Is Super User',readonly=True),
	'user_type': fields.selection(label='User Type',selections=[('s','Super User'),('u','User'),('d','Developer'),('t','Technical User'),('r','Remote User')]),
	'preferences':fields.one2many(label='Preferences',obj='bc.user.preferences',rel='user_id'),
	'access': fields.one2many(label='Access Models',obj='bc.user.model.access',rel='user_id'),
	'auth': fields.one2many(label='Auth Models',obj='bc.user.model.auths',rel='user_id'),
	}

	_sql_constraints = [('full_name_unique','unique (firstname, lastname)', 'Login unique fullname of user')]
	
	def create(self, records,context={}):
		if type(records) in (list,tuple):
			for record in records:
				if 'password' in record:
					record['password'] = pbkdf2_sha256.hash(record['password'])

		elif type(records) == dict:
			if 'password' in records:
				records['password'] = pbkdf2_sha256.hash(records['password'])

		return super(Model,self).create(records, context)

	def write(self, records, context = {}):
		if type(records) in (list,tuple):
			for record in records:
				if 'password' in record:
					record['password'] = pbkdf2_sha256.hash(record['password'])

		elif type(records) == dict:
			if 'password' in records:
				records['password'] = pbkdf2_sha256.hash(records['password'])

		return super(Model,self).write(records, context)

	def modify(self, records, context = {}):
		if type(records) in (list,tuple):
			for record in records:
				if 'password' in record:
					record['password'] = pbkdf2_sha256.hash(record['password'])

		elif type(records) == dict:
			if 'password' in records:
				records['password'] = pbkdf2_sha256.hash(records['password'])

		return super(Model,self).modify(records, context)

	def insert(self, fields, values,context = {}):
		for f in enumerate(fields):
			if f[1] == 'password':
				for value in values:
					value[f[0]] = pbkdf2_sha256.hash(value[f[0]])
		return super(Model,self).insert(fields, values,context)

	def upsert(self, fields, values,context = {}):
		for f in enumerate(fields):
			if f[1] == 'password':
				for value in values:
					value[f[0]] = pbkdf2_sha256.hash(value[f[0]])
		return super(Model,self).upsert(fields, values,context)


	def update(self, record, cond = None,context = {}):
		if 'password' in record:
			record['password'] = pbkdf2_sha256.hash(record['password'])

		return super(Model,self).update(record, cond,context)

	def read(self, ids, fields = None, context = {}):
		records = super(Model,self).read(ids,fields, context)
		if type(records) == dict:
			if 'password' in records:
				records['password'] = '******'
		elif type(records) in (list,tuple):
			for record in records:
				if 'password' in record:
					record['password'] = '******'
		
		return records
				
	def select(self, fields = None ,cond = None, context = {}, limit = None, offset = None):
		records = super(Model,self).select(fields, cond, context, limit, offset)
		if type(records) == dict:
			if 'password' in records:
				records['password'] = '******'
		elif type(records) in (list,tuple):
			for record in records:
				if 'password' in record:
					record['password'] = '******'

		return records

bc_users()

class bc_langs(Model):
	_name = 'bc.langs'
	_description = 'Langs'
	_rec_name = 'code'
	_class_object = 'K'
	_columns = {
	'code': fields.varchar(label='Language',size = 3,readonly=False),
	'description': fields.varchar(label='Description', size = 64,readonly=True)
	}

bc_langs()

class bc_web_frameworks(Model):
	_name = 'bc.web.frameworks'
	_description = 'Web Frameworks'
	_rec_name = 'code'
	_class_object = 'D'
	_columns = {
	'code': fields.varchar(label='Web Framework',size = 64,readonly=True),
	'descr': fields.varchar(label='Description', size = 256,readonly=True)
	}

bc_web_frameworks()

class bc_user_preferences(Model):
	_name = 'bc.user.preferences'
	_description = 'User Preferncess'
	_class_object = 'K'
	_columns = {
	'user_id':fields.many2one(label='User',obj='bc.users',rel='preferences',readonly=True),
	'framework': fields.referenced(label='Framework',obj='bc.web.frameworks'),
	'lang':fields.referenced(label='Language',obj='bc.langs'),
	'country': fields.selection(label='Country',selections='_get_countries'),
	'timezone': fields.selection(label='Timezone', selections='_get_timezones')
	}
	def _get_countries(self, item = {}, context = {}):
		return list(pytz.country_names.items())

	def _get_timezones(self, item = {}, context = {}):
		res = []
		for v in pytz.all_timezones:
			res.append((v,v))
		return res
		
bc_user_preferences()



class bc_group_modules(Model):
	_name = 'bc.group.modules'
	_description = 'Module Groups'
	_class_object = 'K'
	_columns = {
	'name': fields.varchar(label = 'Name',readonly=True),
	'name2': fields.varchar(label = 'Name 2', selectable = True, required = True,readonly=True),
	'parent_id': fields.many2one(label = 'Parent',obj='bc.group.modules',readonly=True),
	'childs_id': fields.one2many(label = 'Childs',obj='bc.group.modules',rel='parent_id',readonly=True),
	'modules': fields.one2many(label = 'Modules',obj = 'bc.modules', rel = 'group_module_id',readonly=True),
	'note': fields.text(label='Note',readonly=True)
	}

bc_group_modules()

class bc_modules(Model):
	_name = 'bc.modules'
	_description = 'Modules'
	_rec_name = 'code'
	_class_object = 'K'
	_columns = {
	'group_module_id': fields.many2one(label = 'Group', obj = 'bc.group.modules', rel='modules', required = False, on_delete = 'n',readonly=True),
	'code': fields.varchar(label = 'Code',readonly=True),
	'name': fields.varchar(label = 'Name',readonly=True),
	'version': fields.varchar(label = 'Version',readonly=True),
	'category': fields.varchar(label = 'Category',readonly=True),
	'shortdescription': fields.varchar(label = 'Short Description', size = 256,readonly=True),
	'author': fields.varchar(label = 'Author', size =128,readonly=True),
	'website': fields.varchar(label = 'Website', size =128,readonly=True),
	'maintainer': fields.varchar(label = 'Maintainer', size = 128,readonly=True),
	'able': fields.varchar(label = 'Able', size=32,readonly=True),
	'area': fields.selection(label = 'Area',selections = [('S','System'), ('A','Application'), ('E','Extra')],readonly=True),
	'icon': fields.varchar(label = 'Icon', size = 64,readonly=True),
	'image': fields.varchar(label = 'Image ', size = 64,readonly=True),
	'state': fields.selection(label = 'State', selections = [('N','Not installed'),('I','Installed'),('i','To be installed'),('u','To be upgrade'),('r','To be uninstalled')],readonly=True),
	'description': fields.text(label = 'Long Description',readonly=True),
	'models': fields.one2many(label ='Objects', obj = 'bc.models', rel = 'module_id',readonly=True),
	'inherits': fields.one2many(label ='Inherit Modelss', obj = 'bc.model.inherits', rel = 'module_id',readonly=True),
	'files': fields.one2many(label ='Files', obj = 'bc.module.files', rel = 'module_id',readonly=True)}

bc_modules()

class bc_module_files(Model):
	_name = 'bc.module.files'
	_description = 'Module File'
	_rec_name = 'filename'
	_class_object = 'K'
	_order_by="module_id,id"
	_columns = {
	'module_id': fields.many2one(label = 'Module', obj = 'bc.modules', rel='files', required = False, on_delete = 'n',readonly=True),
	'filename': fields.varchar(label = 'Name',size=255,readonly=True),
	'size': fields.integer(label='Size',readonly=True),
	'ctime': fields.datetime(label='Created',timezone = False,readonly=True),
	'mtime': fields.datetime(label='Modified',timezone = False,readonly=True),
	}

bc_module_files()

class bc_class_model_categories(Model):
	_name = 'bc.class.model.categories'
	_description = 'Category Class Models'
	_class_object = 'K'
	_rec_name = 'code'
	_columns = {
	'code': fields.varchar(label='Code', size = 8,readonly=True),
	'descr': fields.varchar(label='Description', size = 64,readonly=True),
	'note': fields.text(label='Note',readonly=True)
	}

bc_class_model_categories()


class bc_class_models(Model):
	_name = 'bc.class.models'
	_description = 'Class Models'
	_class_object = 'K'
	_rec_name = 'code'
	_columns = {
	'code': fields.varchar(label='Code', size = 8,readonly=True),
	'descr': fields.varchar(label='Description', size = 64,readonly=True),
	'note': fields.text(label='Note',readonly=True)
	}

bc_class_models()


class bc_models(Model):
	_name = 'bc.models'
	_description = 'Models'
	_class_object = 'K'
	_order_by="module_id,code"
	_rec_name = 'code'
	_columns = {
	'module_id': fields.many2one(label = 'Module', obj = 'bc.modules',rel='models',readonly=True, on_delete = 'c'),
	'code': fields.varchar(label = 'Name', size = 64,readonly=True),
	'descr': fields.varchar(label = 'Description', size = 256,readonly=True),
	'class_model': fields.related(label = 'Class Model', obj = 'bc.class.models', readonly=True),
	'class_model_category': fields.related(label = 'Class Model Category', obj = 'bc.class.model.categories', readonly=True),
	'oom': fields.json(label='Meta Of Object', readonly = True),
	'columns': fields.one2many(label='Columns',obj='bc.model.columns', rel='model_id',readonly = True),
	'inherits':fields.one2many(label = 'Inherits', obj = 'bc.model.inherit.inherits', rel = 'model_id',readonly=True)
	}

bc_models()

class bc_model_columns(Model):
	_name = 'bc.model.columns'
	_description = 'Columns Of Model'
	_class_model = 'K'
	#_rec_name = 'name'
	_order_by="seq"
	_columns = {
	'model_id': fields.many2one(label = 'Model', obj = 'bc.models', rel='columns',readonly=True, on_delete = 'c'),
	#'name': fields.composite(label='Name Column', cols = ['model_id','col'], required = True),
	'seq': fields.integer(label='Sequence', readonly = True),
	'col': fields.varchar(label='Column', readonly=True),
	'moc': fields.json(label='Meta Of Column', readonly = True),
	}

bc_model_columns()



class bc_model_inherits(Model):
	_name = 'bc.model.inherits'
	_description = 'Model Inherits'
	_class_object = 'K'
	_order_by="code"
	_rec_name = 'code'
	_columns = {
	'module_id': fields.many2one(label = 'Module', obj = 'bc.modules',rel='inherits',readonly=True, on_delete = 'c'),
	'code': fields.varchar(label = 'Name', size = 64,readonly=True),
	'descr': fields.varchar(label = 'Description', size = 256,readonly=True),
	'momi': fields.json(label='Meta Of Model Inherit', readonly = True),
	'columns': fields.one2many(label='Columns', obj = 'bc.model.inherit.columns', rel = 'inherit_id'),
	'models': fields.one2many(label='Models', obj = 'bc.model.inherit.inherits', rel = 'inherit_id'),
	}

bc_model_inherits()

class bc_model_inherit_columns(Model):
	_name = 'bc.model.inherit.columns'
	_description = 'Models Columns Inherits'
	_class_object = 'K'
	_order_by="col"
	_columns = {
	'inherit_id': fields.many2one(label = 'Model Inherit', obj = 'bc.model.inherits', rel='columns',readonly=True, on_delete = 'c'),
	'name': fields.composite(label='Name Column', cols = ['inherit_id','col'], required = True),
	'seq': fields.integer(label='Sequence', readonly = True),
	'col': fields.varchar(label='Column', size = 64, readonly=True),
	'moc': fields.json(label='Meta Of Column', readonly = True),
	}

bc_model_inherit_columns()

class bc_model_inherit_inherits(Model):
	_name = 'bc.model.inherit.inherits'
	_description = 'Inherit Columns To Models'
	_class_object = 'K'
	_order_by="col"
	_columns = {
	'inherit_id': fields.many2one(label = 'Inherit', obj = 'bc.model.inherits', rel='models',readonly=True, on_delete = 'c'),
	'model_id': fields.referenced(label = 'Model', obj = 'bc.models',readonly=True, on_delete = 'c'),
	#'name': fields.composite(label='Name Column', cols = ['inherit_id','model_id','col'], required = True),
	#'col': fields.many2one(label='Column', obj = 'bc.model.inherit.columns', readonly=True)
	'col': fields.varchar(label='Column', size = 64, readonly=True),
	}

bc_model_inherit_inherits()

class bc_group_access(Model):
	_name = 'bc.group.access'
	_description = 'Group Access'
	_class_object = 'K'
	_columns = {
	'name': fields.varchar(label="Group Access",readonly=True),
	'parent_id': fields.many2one(label='Parent',obj='bc.group.access',rel='childs_id',readonly=True),
	'childs_id': fields.one2many(label='Childs',obj='bc.group.access',rel='parent_id',readonly=True),
	'roles': fields.one2many(label='Roles',obj='bc.access',rel='group_id',readonly=True),
	'active': fields.boolean('Active',readonly=True),
	'note': fields.text(label='Note',readonly=True)
	}

bc_group_access()

class bc_access(Model):
	_name = 'bc.access'
	_description = 'Access'
	_class_object = 'K'
	_columns = {
	'group_id': fields.many2one(label='Group',obj='bc.group.access',rel = 'bc.group.access',readonly=True, on_delete = 'c'),
	'name': fields.varchar(label="Access",readonly=True),
	'models': fields.one2many(label='Objects',obj='bc.model.access',rel='access_id',readonly=True),
	'inactive': fields.boolean('Inactive',readonly=True),
	'note': fields.text(label='Note',readonly=True)
	}

bc_access()


class bc_model_access(Model):
	_name = 'bc.model.access'
	_description = 'Models Access'
	_class_object = 'K'
	_order_by='model_id,access_id'
	_columns = {
	'access_id': fields.many2one(label='Access',obj='bc.access',rel='models',readonly=True, on_delete = 'c'),
	'model': fields.referenced(label='Model',obj='bc.models',readonly=True, on_delete = 'c'),
	'acreate': fields.boolean('Create',readonly=True),
	'awrite': fields.boolean('Write',readonly=True),
	'aread': fields.boolean('Read',readonly=True),
	'aunlink': fields.boolean('Unlink',readonly=True),
	'aexecute': fields.boolean('Execute',readonly=True),
	'inactive': fields.boolean('Inactive',readonly=True),
	'auth': fields.json(label='Auth',readonly=True),
	'note': fields.text(label='Note',readonly=True)
	}
	
	_sql_constraints = [('model_unique','unique (access_id, model)', 'Model to be  unique in access')]

bc_model_access()

class bc_model_data(Model):
	_name = 'bc.model.data'
	_description = 'Loading Object XML Data'
	_class_object = 'K'
	_table = 'bc_object_data'
	_columns = {
	'name': fields.varchar(label = 'Name',size = 256,readonly=True),
	'module': fields.varchar(label = 'Module',size = 64,selectable=True,readonly=True),
	'model': fields.varchar(label = 'Model',size = 64,selectable=True,readonly=True),
	'rec_id': fields.uuid(label = 'ID record',readonly=True),
	'file_id': fields.related(label='File',obj='bc.module.files',relatedy = ['module'],readonly=True),
	'date_init': fields.datetime(label = 'Timestamp init', timezone = False,readonly=True),
	'date_update': fields.datetime(label = 'Timestamp update', timezone = False,readonly=True)
	}

bc_model_data()

class bc_ui_view_model_types(Model):
	_name = 'bc.ui.view.model.types'
	_description = 'UI Type Of View'
	_class_object = 'K'
	_columns = {
	'fullname': fields.composite(label='Full Name', cols = ['framework','code'], translate = True,required = True),
	'framework': fields.referenced(label='Web Framework',obj='bc.web.frameworks',required=True),
	'code': fields.varchar(label='Code', size = 64,required=True),
	'exclude': fields.json(label='Exclude'),
	'note': fields.text(label='Note')
	}

bc_ui_view_model_types()

class bc_ui_model_views(Model):
	_name = 'bc.ui.model.views'
	_description = 'UI Views'
	_rec_name='fullname'
	_class_object = 'K'
	_columns = {
	'fullname': fields.composite(label='Full Name', cols = ['model','vtype'], translate = True,required = True),
	'model': fields.referenced(label='Model',obj='bc.models'),
	'vtype': fields.referenced(label='View Type',obj='bc.ui.view.model.types'),
	'created': fields.datetime('Created', readonly = True),
	'modified': fields.datetime('Modified', readonly = True),
	'standalone': fields.boolean(label='Standalone View'),
	'template': fields.text(label='Template'),
	'render': fields.text(label='Render'),
	'script': fields.text(label='Script'),
	'script_setup': fields.text(label='Script  Setup'),
	'style': fields.text(label='Style'),
	'i18n': fields.text(label='I18N'),
	'scoped': fields.boolean(label='Scoped'),
	'sfc': fields.text(label='Single File Component'),
	'cols': fields.one2many(label='Columns', obj = 'bc.ui.model.view.columns',rel = 'view_id'),
	'inherit_cols': fields.one2many(label='Columns Inherit', obj = 'bc.ui.model.view.column.inherits',rel = 'view_id'),
	'note': fields.text(label='Note')
	}

	def _generateTemplate(self,record,context):
		#web_pdb.set_trace()
		if record['vtype']['name'] in _GENERATEVIEW: #and (record['template'] is  None or len(record['template']) == 0):
			record['template'] = _GENERATEVIEW[record['vtype']['name']].view._generateTemplate(META,record['model']['name'],self._model._pool,context)

	def _generateRender(self,record,context):
		if record['vtype']['name'] in _GENERATEVIEW: #and (record['render'] is  None or len(record['render']) == 0):
			record['render'] = _GENERATEVIEW[record['vtype']['name']].view._generateRender(META,record['model']['name'],self._model._pool,context)


	def _generateScript(self,record,context):	
		if record['vtype']['name'] in _GENERATEVIEW: #and (record['script'] is  None or len(record['script']) == 0):
			record['script'] = _GENERATEVIEW[record['vtype']['name']].view._generateScript(META,record['model']['name'],self._model._pool,context)

	def _generateStyle(self,record,context):
		if record['vtype']['name'] in _GENERATEVIEW: #and (record['style'] is  None or len(record['style']) == 0):
			record['style'] = _GENERATEVIEW[record['vtype']['name']].view._generateStyle(META,record['model']['name'],self._model._pool,context)

	def _generateI18N(self,record,context):
		if record['vtype']['name'] in _GENERATEVIEW: # and (record['i18n'] is  None or len(record['i18n']) == 0):
			record['i18n'] = _GENERATEVIEW[record['vtype']['name']].view._generateI18N(META,record['model']['name'],self._model._pool,context)


	def _generateSFC(self,record,context):
		self._generateI18N(record,context)
		self._generateTemplate(record,context)
		#self._generateRender(record,context)
		self._generateScript(record,context)
		self._generateStyle(record,context)
		#record['sfc'] = record[record['render']] if len(record['render']) > 0 else record['template'] + record['script'] + '\n' + record['style'] 
		if 'template' in record and record['template']:
			record['sfc'] = record['template']
		if 'script' in record and record['script']:
			record['sfc'] += record['script']
		
		if 'style' in record and record['style']:
			record['sfc'] += record['style']


		if 'i18n' in record and record['i18n']:
			record['sfc'] += record['i18n']

		#record['sfc'] = record['template'] if record['template'] else '' + '\n'+ record['script'] if record['script'] else ''  + '\n' + record['style'] if record['style'] else '' 
		#print('RECORD:',self._name,record)
	def create(self,records,context):
		pass
		#return self._generateSFC(record,context)

	
	def getSFC(self, model, vtype,context):
		records = super(Model,self).select(fields=["fullname", "model", "vtype", "standalone",'template','script', 'style', 'i18n',"sfc"], cond=[('model','=',model),('vtype','=', vtype)], context=context)

		if len(records) > 0:
			if type(records) in (list,tuple):
				for record in records:
					self._generateSFC(record,context)
					for k in ('template','script', 'style','i18n'):
						del record[k]
			elif type(records) == dict:
				self._generateSFC(records,context)
				for k in ('template','script', 'style','i18n'):
					del records[k]
			
			#web_pdb.set_trace()
			#print('RECORDS:',self._name,records[0]['__data__'])
		return records


	def readforupdate(self, ids, fields = None, context = {}):
		records = super(Model,self).readforupdate(ids,fields, context)
		if len(records) > 0:
			if type(records[0]['__data__']) in (list,tuple):
				for record in records[0]['__data__']:
					self._generateSFC(record,context)
			elif type(records[0]['__data__']) == dict:
				self._generateSFC(records[0]['__data__'],context)
			
			#web_pdb.set_trace()
			#print('RECORDS:',self._name,records[0]['__data__'])
		return records

	_default = {
		'framework':'element-plus'
	}


bc_ui_model_views()

class bc_ui_model_view_columns(Model):
	_name = 'bc.ui.model.view.columns'
	_description = 'UI Model View Columns'
	_class_object = 'K'
	_order_by="seq"
	_columns = {
	'view_id': fields.many2one(label='Model View',obj='bc.ui.model.views',rel='cols',required=True),
	'seq': fields.integer(label='Sequence', readonly = True),
	#'col': fields.referenced(label='Column',obj='bc.model.columns'),
	'col': fields.varchar(label='Column', readonly = True),
	'template': fields.text(label='Template'),
	'render': fields.text(label='Render')
	}

bc_ui_model_view_columns()

class bc_ui_model_view_column_inherits(Model):
	_name = 'bc.ui.model.view.column.inherits'
	_description = 'UI Model View Columns Inherit'
	_class_object = 'K'
	_columns = {
	'view_id': fields.many2one(label='Model View',obj='bc.ui.model.views',rel='inherit_cols',required=True),
	#'col': fields.referenced(label='Column',obj='bc.model.inherit.inherits'),
	'col': fields.varchar(label='Column', readonly = True),
	'template': fields.text(label='Template'),
	'render': fields.text(label='Render')
	#'script': fields.text(label='Script'),
	}

bc_ui_model_view_column_inherits()

class bc_model_translations(Model):
	_name = 'bc.model.translations'
	_description = 'Model Translations'
	_class_object = 'K'
	_columns = {
	'lang': fields.referenced(label='Language',obj='bc.langs',readonly=True, on_delete = 'c'),
	'model': fields.referenced(label='Object',obj='bc.models',readonly=True, on_delete = 'c'),
	'tr': fields.json(label='Translations',readonly=True),
	'inherits': fields.one2many(label='Inherits',obj='bc.model.translation.inherits',rel='inherit_id')
	}

bc_model_translations()

class bc_model_translation_inherits(Model):
	_name = 'bc.model.translation.inherits'
	_description = 'Model Translations Inherit'
	_class_object = 'K'
	_columns = {
	'inherit_id': fields.many2one(label='Translation Object',obj='bc.model.translations',rel='inherits',readonly=True, on_delete = 'c'),
	'tr': fields.json(label='Translations',readonly=True),
	}

bc_model_translation_inherits()

	


class bc_tuning_ui_model_views(Model):
	_name = 'bc.tuning.ui.model.views'
	_description = 'Tunning Models Views'
	_class_object = 'K'
	_columns = {
	'fullname': fields.i18n(fields.composite(label='Full Name', cols = ['tuser','view','name'], required = True)),
	'name':fields.varchar(label='Name',size=128,readonly=True),
	'view':fields.referenced(label = 'View', obj='bc.ui.model.views',readonly=True, on_delete = 'c'),
	'tuser': fields.referenced(label = 'User', obj='bc.users',readonly=True, on_delete = 'c'),
	'values': fields.json(label='Values',readonly=True)
	}

	_sql_constraints = [('view_id_seq_unique','unique (tuser,view, name)', 'Sequence unique of vies')]

bc_tuning_ui_model_views()



class bc_general_tuning_ui_model_views(Model):
	_name = 'bc.general.tuning.ui.model.views'
	_description = 'General Tunning Models Views'
	_class_object = 'K'
	_columns = {
	'fullname': fields.i18n(fields.composite(label='Full Name', cols = ['view','name'], required = True)),
	'name':fields.varchar(label='Name',size=128,readonly=True),
	'view':fields.referenced(label = 'View', obj='bc.ui.model.views',readonly=True, on_delete = 'c'),
	'values': fields.json(label='Values',readonly=True)
	}

	_sql_constraints = [('view_id_seq_unique','unique (view, name)', 'Sequence unique of vies')]

bc_general_tuning_ui_model_views()

class bc_ui_model_actions(Model):
	_name = 'bc.ui.model.actions'
	_description = 'Model UI Actions'
	_class_object = 'K'
	_columns = {
	'name': fields.varchar(label = 'Model Action',readonly=True),
	'model': fields.referenced(label='Model',obj = 'bc.models')
	}

class bc_ui_framework_model_actions(Model):
	_name = 'bc.ui.framework.model.actions'
	_description = 'Model UI Framework Actions'
	_class_object = 'K'
	_columns = {
	'fullname': fields.composite(label='Full Name', cols = ['action_id','framework_id'], required = True),
	'action_id': fields.referenced(label='Action',obj = 'bc.ui.model.actions'),
	'framework_id': fields.referenced(label='Framework',obj = 'bc.web.frameworks'),
	'view_id': fields.referenced(label='View',obj='bc.ui.model.views',readonly=True, on_delete = 'c')
	}

bc_ui_framework_model_actions()

class bc_ui_model_menus(Model):
	_name ='bc.ui.model.menus'
	_description = 'UI Menus'
	_class_object = 'K'
	_order_by = 'sequence,label'
	_columns = {
	'name': fields.varchar(label = 'Name',readonly=True),
	'label': fields.varchar(label = 'Label',readonly=True),
	'parent_id': fields.many2one(label='Parent',obj='bc.ui.model.menus',rel='childs_id',readonly=True,on_delete='c'),
	'childs_id': fields.one2many(label='Childs',obj='bc.ui.model.menus',rel='parent_id',readonly=True),
	'sequence': fields.integer(label='Sequence'),
	'action_id': fields.referenced(label='Action', obj='bc.ui.model.actions',readonly=True, on_delete = 'c')
	}

bc_ui_model_menus()

class bc_access_models(Model):
	_name = 'bc.access.models'
	_description = 'Access Models'
	_class_object = 'K'
	_columns = {
	'name': fields.varchar(label = 'Name',readonly=True),
	'model': fields.many2one(label = 'Model',obj='bc.models',readonly=True),
	#'access': fields.referenced(label = 'Columns',obj = 'bc.auth.model.columns', rel = 'model_module_id',readonly=True),
	'note': fields.text(label='Note',readonly=True)
	}

class bc_auth_models(Model):
	_name = 'bc.auth.models'
	_description = 'Auth Models'
	_class_object = 'K'
	_columns = {
	'name': fields.varchar(label = 'Name',readonly=True),
	'model': fields.many2one(label = 'Model',obj='bc.models',readonly=True),
	#'columns': fields.one2many(label = 'Columns',obj = 'bc.auth.model.columns', rel = 'model_module_id',readonly=True),
	'note': fields.text(label='Note',readonly=True)
	}

class bc_user_model_access(Model):
	_name = 'bc.user.model.access'
	_description = 'User Access Models'
	_class_object = 'K'
	_columns = {
	'user_id': fields.many2one(label = 'User',obj = 'bc.users',rel = 'access',readonly=True),
	#'columns': fields.one2many(label = 'Columns',obj = 'bc.auth.model.columns', rel = 'model_module_id',readonly=True),
	'note': fields.text(label='Note',readonly=True)
	}

class bc_user_model_auths(Model):
	_name = 'bc.user.model.auths'
	_description = 'User Auth Models'
	_class_object = 'K'
	_columns = {
	'user_id': fields.many2one(label = 'User',obj = 'bc.users',rel = 'auth',readonly=True),
	#'columns': fields.one2many(label = 'Columns',obj = 'bc.auth.model.columns', rel = 'model_module_id',readonly=True),
	'note': fields.text(label='Note',readonly=True)
	}
