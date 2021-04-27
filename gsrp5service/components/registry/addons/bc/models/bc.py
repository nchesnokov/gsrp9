from gsrp5service.orm import fields
from gsrp5service.orm.model import Model

from passlib.hash import pbkdf2_sha256

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
	'preferences':fields.one2many(label='Preferences',obj='bc.user.preferences',rel='user_id')
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
	'code': fields.varchar(label='Language',size = 3,readonly=True),
	'description': fields.varchar(label='Description', size = 64,readonly=True)
	}

bc_langs()

class bc_user_preferences(Model):
	_name = 'bc.user.preferences'
	_description = 'User Preferncess'
	_class_object = 'K'
	_columns = {
	'user_id':fields.many2one(label='User',obj='bc.users',readonly=True),
	'lang':fields.many2one(label='Language',obj='bc.langs'),
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
	'bc_modules': fields.one2many(label = 'Modules',obj = 'bc.modules', rel = 'bc_group_module_id',readonly=True),
	'note': fields.text(label='Note',readonly=True)
	}

bc_group_modules()

class bc_modules(Model):
	_name = 'bc.modules'
	_description = 'Modules'
	_rec_name = 'code'
	_class_object = 'K'
	_columns = {
	'bc_group_module_id': fields.many2one(label = 'Group', obj = 'bc.group.modules', required = False, on_delete = 'n',readonly=True),
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
	'model_inherits': fields.one2many(label ='Inherit Objects', obj = 'bc.model.inherits', rel = 'module_id',readonly=True),
	'files': fields.one2many(label ='Files', obj = 'bc.module.files', rel = 'module_id',readonly=True)}

bc_modules()

class bc_module_files(Model):
	_name = 'bc.module.files'
	_description = 'Module File'
	_rec_name = 'filename'
	_class_object = 'K'
	_order_by="module_id,id"
	_columns = {
	'module_id': fields.many2one(label = 'Module', obj = 'bc.modules', required = False, on_delete = 'n',readonly=True),
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
	rec_name = 'code'
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
	rec_name = 'code'
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
	_extra = {'env-fields':['class_model','class_model_category']}
	rec_name = 'code'
	_columns = {
	'module_id': fields.many2one(label = 'Module', obj = 'bc.modules',readonly=True, on_delete = 'c'),
	'code': fields.varchar(label = 'Name', size = 64,readonly=True),
	'descr': fields.varchar(label = 'Description', size = 256,readonly=True),
	'class_model': fields.many2one(label = 'Class Model', obj = 'bc.class.models', readonly=True),
	'class_model_category': fields.many2one(label = 'Class Model Category', obj = 'bc.class.model.categories', readonly=True),
	'oom': fields.json(label='Meta Of Object', readonly = True),
	'columns': fields.one2many(label='Columns',obj='bc.model.columns', readonly = True),
	'inherits':fields.one2many(label = 'Inherits', obj = 'bc.model.inherits', rel = 'object_id',readonly=True)
	}

bc_models()

class bc_model_columns(Model):
	_name = 'bc.model.columns'
	_description = 'Models'
	_class_object = 'K'
	_order_by="col"
	_columns = {
	'model_id': fields.many2one(label = 'Model', obj = 'bc.models', readonly=True, on_delete = 'c'),
	'col': fields.varchar(label='Column', readonly=True),
	'moc': fields.json(label='Meta Of Column', readonly = True),
	}

bc_model_columns()



class bc_model_inherits(Model):
	_name = 'bc.model.inherits'
	_description = 'Object Inherits'
	_class_object = 'K'
	_order_by="module_id,model_id"
	_columns = {
	'fullname': fields.composite(label='Full Name', cols = ['module_id','model_id','code'], required = True, compute = '_compute_composite'),
	'model_id': fields.many2one(label = 'Object', obj = 'bc.models',readonly=True, on_delete = 'c'),
	'module_id': fields.many2one(label = 'Module', obj = 'bc.modules',readonly=True, on_delete = 'c'),
	'code': fields.varchar(label = 'Name', size = 64,readonly=True),
	'descr': fields.varchar(label = 'Description', size = 256,readonly=True),
	'momi': fields.json(label='Meta Of Model Inherit', readonly = True),
	}

bc_model_inherits()

class bc_model_inherit_columns(Model):
	_name = 'bc.model.inherit.columns'
	_description = 'Models Inherits'
	_class_object = 'K'
	_order_by="col"
	_columns = {
	'inherit_id': fields.many2one(label = 'Inherit', obj = 'bc.model.inherits', readonly=True, on_delete = 'c'),
	'col': fields.varchar(label='Column', readonly=True),
	'moc': fields.json(label='Meta Of Column', readonly = True),
	}

bc_model_inherit_columns()


class bc_group_access(Model):
	_name = 'bc.group.access'
	_description = 'Group Access'
	_class_object = 'K'
	_columns = {
	'name': fields.varchar(label="Group Access",readonly=True),
	'parent_id': fields.many2one(label='Parent',obj='bc.group.access',readonly=True),
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
	'name': fields.varchar(label="Access",readonly=True),
	'group_id': fields.many2one(label='Group',obj='bc.group.access',readonly=True, on_delete = 'c'),
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
	'access_id': fields.many2one(label='Access',obj='bc.access',readonly=True, on_delete = 'c'),
	'model_id': fields.many2one(label='Object',obj='bc.models',readonly=True, on_delete = 'c'),
	'acreate': fields.boolean('Create',readonly=True),
	'awrite': fields.boolean('Write',readonly=True),
	'aread': fields.boolean('Read',readonly=True),
	'aunlink': fields.boolean('Unlink',readonly=True),
	'aexecute': fields.boolean('Execute',readonly=True),
	'inactive': fields.boolean('Inactive',readonly=True),
	'auth': fields.json(label='Auth',readonly=True),
	'note': fields.text(label='Note',readonly=True)
	}
	
	_sql_constraints = [('model_unique','unique (access_id, model_id)', 'Model to be  unique in access')]

bc_model_access()

class bc_model_data(Model):
	_name = 'bc.model.data'
	_description = 'Loading Object XML Data'
	_class_object = 'K'
	_table = 'bc_object_data'
	_columns = {
	'name': fields.varchar(label = 'Name',size = 256,readonly=True),
	'module': fields.varchar(label = 'Module',size = 64,selectable=True,readonly=True),
	'model': fields.varchar(label = 'Object',size = 64,selectable=True,readonly=True),
	'rec_id': fields.uuid(label = 'ID record',readonly=True),
	'file_id': fields.many2one(label='File',obj='bc.module.files',readonly=True),
	'date_init': fields.datetime(label = 'Timestamp init', timezone = False,readonly=True),
	'date_update': fields.datetime(label = 'Timestamp update', timezone = False,readonly=True)
	}

bc_model_data()

