from gsrp5service.orm import fields
from gsrp5service.orm.model import Model

from passlib.hash import pbkdf2_sha256

class bc_users(Model):
	_name = 'bc.users'
	_description = 'General Model Users'
	_log_access = False
	_rec_name = 'login'
	_columns = {
	'login': fields.varchar('Login', required = True, size = 64,readonly=True),
	'password': fields.varchar('Password', required = True,readonly=True),
	'firstname': fields.varchar('First Name', required = True, selectable = True,readonly=True),
	'lastname': fields.varchar('Last Name', required = True, selectable = True,readonly=True),
	'issuperuser': fields.boolean(label='Is Super User',readonly=True)}

	_sql_constraints = [('full_name_unique','unique (firstname, lastname)', 'Login unique fullname of user')]
	
	def create(self,cr,pool,uid,records,context={}):
		if type(records) in (list,tuple):
			for record in records:
				if 'password' in record:
					record['password'] = pbkdf2_sha256.hash(record['password'])

		elif type(records) == dict:
			if 'password' in records:
				records['password'] = pbkdf2_sha256.hash(records['password'])

		return super(Model,self).create(cr, pool, uid, records, context)

	def write(self, cr, pool, uid, records, context = {}):
		if type(records) in (list,tuple):
			for record in records:
				if 'password' in record:
					record['password'] = pbkdf2_sha256.hash(record['password'])

		elif type(records) == dict:
			if 'password' in records:
				records['password'] = pbkdf2_sha256.hash(records['password'])

		return super(Model,self).write(cr, pool, uid, records, context)

	def modify(self, cr, pool, uid, records, context = {}):
		if type(records) in (list,tuple):
			for record in records:
				if 'password' in record:
					record['password'] = pbkdf2_sha256.hash(record['password'])

		elif type(records) == dict:
			if 'password' in records:
				records['password'] = pbkdf2_sha256.hash(records['password'])

		return super(Model,self).modify(cr, pool, uid, records, context)

	def insert(self, cr, pool, uid, fields, values,context = {}):
		for f in enumerate(fields):
			if f[1] == 'password':
				for value in values:
					value[f[0]] = pbkdf2_sha256.hash(value[f[0]])
		return super(Model,self).insert(cr, pool, uid, fields, values,context)

	def upsert(self, cr, pool, uid, fields, values,context = {}):
		for f in enumerate(fields):
			if f[1] == 'password':
				for value in values:
					value[f[0]] = pbkdf2_sha256.hash(value[f[0]])
		return super(Model,self).upsert(cr, pool, uid, fields, values,context)


	def update(self, cr, pool, uid, record, cond = None,context = {}):
		if 'password' in record:
			record['password'] = pbkdf2_sha256.hash(record['password'])

		return super(Model,self).update(cr, pool, uid, record, cond,context)

	def read(self, cr, pool, uid, ids, fields = None, context = {}):
		records = super(Model,self).read(cr, pool, uid, ids, fields, context)
		if type(records) == dict:
			if 'password' in records:
				records['password'] = '******'
		elif type(records) in (list,tuple):
			for record in records:
				if 'password' in record:
					record['password'] = '******'
		
		return records
				
	def select(self, cr, pool, uid, fields = None ,cond = None, context = {}, limit = None, offset = None):
		records = super(Model,self).select(cr, pool, uid, fields, cond, context, limit, offset)
		if type(records) == dict:
			if 'password' in records:
				records['password'] = '******'
		elif type(records) in (list,tuple):
			for record in records:
				if 'password' in record:
					record['password'] = '******'

		return records

bc_users()

class bc_area_messages(Model):
	_name = 'bc.area.messages'
	_description = 'General Model Area Messages'
	_columns = {
	'name': fields.varchar(label='Area', size = 64,readonly=True),
	'note': fields.text(label='Note',readonly=True)
	}

bc_area_messages()

class bc_messages(Model):
	_name = 'bc.messages'
	_description = 'General Model Messages'
	_rec_name='code'
	_columns = {
	'area': fields.many2one(label='Area', obj='bc.area.messages', readonly=True, required=True),
	'code': fields.varchar(label='Message', size = 64,readonly=True),
	'descr': fields.varchar(label='Description', readonly=True ,required=True),
	'note': fields.text(label='Note',readonly=True)
	}

bc_messages()

class bc_langs(Model):
	_name = 'bc.langs'
	_description = 'General Model Langs'
	_columns = {
	'name': fields.varchar(label='Language', size = 64,readonly=True),
	'description': fields.varchar(label='Description', size = 64,readonly=True)
	}

bc_langs()

class bc_group_modules(Model):
	_name = 'bc.group.modules'
	_description = 'General Model Module Groups'
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
	_description = 'General Model Modules'
	_rec_name = 'code'
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
	'models': fields.one2many(label ='Models', obj = 'bc.models', rel = 'module_id',readonly=True),
	'inherits': fields.one2many(label ='Inherit', obj = 'bc.inherits', rel = 'module_id',readonly=True),
	'files': fields.one2many(label ='Files', obj = 'bc.module.files', rel = 'module_id',readonly=True)}

bc_modules()

class bc_module_files(Model):
	_name = 'bc.module.files'
	_description = 'General Model Module File'
	_rec_name = 'filename'
	_order_by="module_id,id"
	_columns = {
	'module_id': fields.many2one(label = 'Module', obj = 'bc.modules', required = False, on_delete = 'n',readonly=True),
	'filename': fields.varchar(label = 'Name',size=255,readonly=True),
	'size': fields.integer(label='Size',readonly=True),
	'ctime': fields.datetime(label='Created',timezone = False,readonly=True),
	'mtime': fields.datetime(label='Modified',timezone = False,readonly=True),
	}

bc_module_files()

class bc_class_models(Model):
	_name = 'bc.class.models'
	_description = 'General Model Class Models'
	_columns = {
	'name': fields.varchar(label='Code', size = 64,readonly=True),
	'descr': fields.varchar(label='Description', size = 64,readonly=True),
	'note': fields.text(label='Note',readonly=True)
	}

bc_class_models()

class bc_class_categories(Model):
	_name = 'bc.class.categories'
	_description = 'General Model Class Categories'
	_columns = {
	'name': fields.varchar(label='Code', size = 64,readonly=True),
	'descr': fields.varchar(label='Description', size = 64,readonly=True),
	'note': fields.text(label='Note',readonly=True)
	}

bc_class_models()


class bc_models(Model):
	_name = 'bc.models'
	_description = 'General Model Models'
	_order_by="module_id"
	_extra = {'env-fields':['class_model','class_category']}
	_columns = {
	'name': fields.varchar(label = 'Name', size = 64,readonly=True),
	'db_table': fields.varchar(label = 'Database table', size = 64,readonly=True),
	'description': fields.varchar(label = 'Description', size = 256,readonly=True),
	'class_model': fields.many2one(label = 'Class Model', obj = 'bc.class.models', readonly=True),
	'class_category': fields.many2one(label = 'Class Categoty', obj = 'bc.class.categories', readonly=True),
	'module_id': fields.many2one(label = 'Module', obj = 'bc.modules',readonly=True, on_delete = 'c'),
	'columns':fields.one2many(label = 'Columns', obj = 'bc.model.columns', rel = 'model_id',readonly=True)
	}

bc_models()


class bc_inherits(Model):
	_name = 'bc.inherits'
	_description = 'General Model Inherits'
	_order_by="module_id"
	_columns = {
	'name': fields.varchar(label = 'Name', size = 64,readonly=True),
	'description': fields.varchar(label = 'Description', size = 256,readonly=True),
	'module_id': fields.many2one(label = 'Module', obj = 'bc.modules',readonly=True, on_delete = 'c'),
	'columns':fields.one2many(label = 'Columns', obj = 'bc.inherit.columns', rel = 'inherit_id',readonly=True)
	}

bc_inherits()

class bc_model_columns(Model):
	_name = 'bc.model.columns'
	_description = 'General Model Model Columns'
	_order_by='model_id,col_name'
	_columns = {
	'model_id': fields.many2one(label = 'Model', obj = 'bc.models',readonly=True, on_delete = 'c'),
	'col_name': fields.varchar(label = 'Name', size = 64,readonly=True),
	'col_type':  fields.varchar(label = 'Type', size = 64,readonly=True),
	'label': fields.varchar(label = 'label', size = 64,readonly=True),
	'readanly': fields.boolean(label = 'Readonly',readonly=True),
	'priority': fields.integer(label = 'Prority',readonly=True),
	'domain': fields.text(label = 'Domain',readonly=True),
	'required': fields.boolean(label = 'Required',readonly=True),
	'size': fields.integer(label = 'Size',readonly=True),
	'precision': fields.integer(label = 'Precesion',readonly=True),
	'on_delete': fields.selection(label = 'On Delete',selections = [('a','No action'),('r','Restrict'),('n','Set Null'),('c','Cascade'),('d','Set default')], size = 1,readonly=True),
	'on_update': fields.selection(label = 'On Update',selections = [('a','No action'),('r','Restrict'),('n','Set Null'),('c','Cascade'),('d','Set default')], size = 1,readonly=True),
	'change_default': fields.boolean(label = 'Change default',readonly=True),
	'translate': fields.boolean(label = 'Translate',readonly=True),
	'selections': fields.text(label = 'Selections',readonly=True),
	'selectable': fields.boolean(label = 'Selectable',readonly=True),
	'relatedy': fields.text(label = 'Relatedy',readonly=True),
	'manual': fields.text(label = 'Manual',readonly=True),
	'help': fields.text(label = 'Help',readonly=True),
	'col_unique': fields.boolean(label = 'Unique',readonly=True),
	'col_check': fields.text(label = 'Check',readonly=True),	
	'col_default': fields.text(label = 'Default',readonly=True),
	'col_family': fields.varchar(label = 'Family',size=64,readonly=True),		
	'timezone': fields.boolean(label = 'Timezone',readonly=True),
	'obj': fields.varchar(label = 'Obj', size = 64,readonly=True),
	'rel': fields.varchar(label = 'Relation', size = 64,readonly=True),
	'id1': fields.varchar(label = 'Id1', size = 64,readonly=True),
	'id2': fields.varchar(label = 'Id2', size = 64,readonly=True),
	}

bc_model_columns()

class bc_inherit_columns(Model):
	_name = 'bc.inherit.columns'
	_description = 'General Model Inherit Columns'
	_order_by='inherit_id,col_name'
	_columns = {
	'inherit_id': fields.many2one(label = 'Inherit', obj = 'bc.inherits',readonly=True, on_delete = 'c'),
	'col_name': fields.varchar(label = 'Name', size = 64,readonly=True),
	'col_type':  fields.varchar(label = 'Type', size = 64,readonly=True),
	'label': fields.varchar(label = 'label', size = 64,readonly=True),
	'readanly': fields.boolean(label = 'Readonly',readonly=True),
	'priority': fields.integer(label = 'Prority',readonly=True),
	'domain': fields.text(label = 'Domain',readonly=True),
	'required': fields.boolean(label = 'Required',readonly=True),
	'size': fields.integer(label = 'Size',readonly=True),
	'precision': fields.integer(label = 'Precesion',readonly=True),
	'on_delete': fields.selection(label = 'On Delete',selections = [('a','No action'),('r','Restrict'),('n','Set Null'),('c','Cascade'),('d','Set default')], size = 1,readonly=True),
	'on_update': fields.selection(label = 'On Update',selections = [('a','No action'),('r','Restrict'),('n','Set Null'),('c','Cascade'),('d','Set default')], size = 1,readonly=True),
	'change_default': fields.boolean(label = 'Change default',readonly=True),
	'translate': fields.boolean(label = 'Translate',readonly=True),
	'selections': fields.text(label = 'Selections',readonly=True),
	'selectable': fields.boolean(label = 'Selectable',readonly=True),
	'filtering': fields.text(label = 'Filtering',readonly=True),
	'manual': fields.text(label = 'Manual',readonly=True),
	'help': fields.text(label = 'Help',readonly=True),
	'col_unique': fields.boolean(label = 'Unique',readonly=True),
	'col_check': fields.text(label = 'Check',readonly=True),	
	'col_default': fields.text(label = 'Default',readonly=True),
	'col_family': fields.varchar(label = 'Family',size=64,readonly=True),		
	'timezone': fields.boolean(label = 'Timezone',readonly=True),
	'obj': fields.varchar(label = 'Obj', size = 64,readonly=True),
	'rel': fields.varchar(label = 'Relation', size = 64,readonly=True),
	'id1': fields.varchar(label = 'Id1', size = 64,readonly=True),
	'id2': fields.varchar(label = 'Id2', size = 64,readonly=True)
	}

bc_inherit_columns()


class bc_translations(Model):
	_name = 'bc.translations'
	_description = 'General Model Translations'
	_columns = {
	'module_id': fields.many2one(label='Module',obj='bc.modules',readonly=True, on_delete = 'c'),
	'lang_id': fields.many2one(label='Language',obj='bc.langs',readonly=True, on_delete = 'c'),
	'model_id': fields.many2one(label='Model',obj='bc.models',readonly=True, on_delete = 'c'),
	'record_id': fields.integer(label="Record ID",readonly=True),
	'column_id': fields.uuid(label="Column ID",readonly=True),
	'tr': fields.json(label='Translations',readonly=True)
	}

bc_translations()
	

class bc_group_access(Model):
	_name = 'bc.group.access'
	_description = 'General Model Group Access'
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
	_description = 'General Model Access'
	_columns = {
	'name': fields.varchar(label="Access",readonly=True),
	'group_id': fields.many2one(label='Group',obj='bc.group.access',readonly=True, on_delete = 'c'),
	'models': fields.one2many(label='Models',obj='bc.model.access',rel='access_id',readonly=True),
	'inactive': fields.boolean('Inactive',readonly=True),
	'note': fields.text(label='Note',readonly=True)
	}

bc_access()


class bc_model_access(Model):
	_name = 'bc.model.access'
	_description = 'General Model Model Access'
	_order_by='model_id,access_id'
	_columns = {
	'access_id': fields.many2one(label='Access',obj='bc.access',readonly=True, on_delete = 'c'),
	'model_id': fields.many2one(label='Model',obj='bc.models',readonly=True, on_delete = 'c'),
	'acreate': fields.boolean('Create',readonly=True),
	'awrite': fields.boolean('Write',readonly=True),
	'amodify': fields.boolean('Modify',readonly=True),
	'aread': fields.boolean('Read',readonly=True),
	'aunlink': fields.boolean('Unlink',readonly=True),
	'aselect': fields.boolean('Select',readonly=True),
	'aupdate': fields.boolean('Update',readonly=True),
	'adelete': fields.boolean('Delete',readonly=True),
	'ainsert': fields.boolean('Insert',readonly=True),
	'aupsert': fields.boolean('Upsert',readonly=True),
	'abrowse': fields.boolean('Browse',readonly=True),
	'aselectbrowse': fields.boolean('Browse Select',readonly=True),
	'inactive': fields.boolean('Inactive',readonly=True),
	'auth': fields.json(label='Auth'),
	'note': fields.text(label='Note',readonly=True)
	}
	
	_sql_constraints = [('model_unique','unique (access_id, model_id)', 'Model to be  unique in access')]

bc_model_access()

class bc_model_data(Model):
	_name = 'bc.model.data'
	_description = 'General Model Loading Model XML Data'
	_table = 'bc_model_data'
	_columns = {
	'name': fields.varchar(label = 'Name',size = 256,readonly=True),
	'module': fields.varchar(label = 'Module',size = 64,selectable=True,readonly=True),
	'model': fields.varchar(label = 'Model',size = 64,selectable=True,readonly=True),
	'rec_id': fields.uuid(label = 'ID record',readonly=True),
	'file_id': fields.many2one(label='File',obj='bc.module.files',readonly=True),
	'date_init': fields.datetime(label = 'Timestamp init', timezone = False,readonly=True),
	'date_update': fields.datetime(label = 'Timestamp update', timezone = False,readonly=True)
	}


class bc_ui_views(Model):
	_name = 'bc.ui.views'
	_description = 'General Model Models views'
	_columns = {
	'name':fields.varchar(label = 'View name', size = 64,readonly=True),
	'model': fields.varchar(label = 'Model Name', size = 64,selectable=True,readonly=True),
	'type': fields.selection(label = 'Arch Type', selections = [('xml','Xml'),('html','Html')],readonly=True),
	'arch': fields.xml(label = 'Arch Blob',readonly=True),
	'inherit_views': fields.one2many(label='Inherit Views',obj='bc.ui.views.inherit',rel='view_id',readonly=True)
	}

bc_ui_views()

class bc_ui_views_inherit(Model):
	_name = 'bc.ui.views.inherit'
	_description = 'General Model Models Views Inherit'
	_columns = {
	'view_id': fields.many2one(label='View',obj='bc.ui.views',readonly=True),
	'name':fields.varchar(label = 'Inherit', size = 128,readonly=True),
	'type': fields.selection(label = 'Arch Type', selections = [('xml','Xml'),('html','Html')],readonly=True),
	'arch':fields.xml(label = 'Arch Blob',readonly=True)
	}

bc_ui_views_inherit()

class bc_tuning_ui_views(Model):
	_name = 'bc.tuning.ui.views'
	_description = 'General Model Tunning Models Views'
	_columns = {
	'name':fields.varchar(label='Name',size=128,readonly=True),
	'view':fields.many2one(label = 'View', obj='bc.ui.views',readonly=True, on_delete = 'c'),
	'tuser': fields.many2one(label = 'User', obj='bc.users',readonly=True, on_delete = 'c'),
	'fullname': fields.composite(label='Full Name', cols = ['user','view','name'], translate = True,required = True, compute = '_compute_composite'),
	'cols': fields.one2many(label='Columns',obj='bc.tuning.ui.view.items',rel='tunning_id',readonly = True),
	}

	_sql_constraints = [('view_id_seq_unique','unique (tuser,view, name)', 'Sequence unique of vies')]

bc_tuning_ui_views()

class bc_tuning_ui_view_items(Model):
	_name = 'bc.tuning.ui.view.items'
	_description = 'General Model Tunning Models View Items'
	_columns = {
	'tunning_id': fields.many2one(label = 'Tunning', obj='bc.tuning.ui.views',readonly=True, on_delete = 'c'),
	'sequence': fields.integer(label = 'Sequence',readonly=True),
	'col_name': fields.varchar(label = 'Column', size=64,readonly=True),
	'readonly': fields.boolean(label='Readonly',readonly=True),
	'required': fields.boolean(label='Required',readonly=True),
	'invisible': fields.boolean(label='Invisible',readonly=True),
	'values': fields.json(label='Values',readonly=True)
	
	}

bc_tuning_ui_view_items()


class bc_general_tuning_ui_views(Model):
	_name = 'bc.general.tuning.ui.views'
	_description = 'General Model General Tunning Models Views'
	_columns = {
	'name':fields.varchar(label='Name',size=128,readonly=True),
	'view':fields.many2one(label = 'View', obj='bc.ui.views',readonly=True, on_delete = 'c'),
	'fullname': fields.composite(label='Full Name', cols = ['view','name'], translate = True,required = True, compute = '_compute_composite'),
	'cols': fields.one2many(label='Columns',obj='bc.general.tuning.ui.view.items',rel='tunning_id',readonly = True),
	}

	_sql_constraints = [('view_id_seq_unique','unique (view, name)', 'Sequence unique of vies')]

bc_general_tuning_ui_views()

class bc_general_tuning_ui_view_items(Model):
	_name = 'bc.general.tuning.ui.view.items'
	_description = 'General Model Tunning Models View Items'
	_columns = {
	'tunning_id': fields.many2one(label = 'Tunning', obj='bc.general.tuning.ui.views',readonly=True, on_delete = 'c'),
	'sequence': fields.integer(label = 'Sequence',readonly=True),
	'col_name': fields.varchar(label = 'Column', size=64,readonly=True),
	'readonly': fields.boolean(label='Readonly',readonly=True),
	'required': fields.boolean(label='Required',readonly=True),
	'invisible': fields.boolean(label='Invisible',readonly=True),
	'values': fields.json(label='Values',readonly=True)
	
	}

bc_general_tuning_ui_view_items()


class bc_ui_reports(Model):
	_name ='bc.ui.reports'
	_description = 'General Model Reports'
	_columns = {
	'name': fields.varchar(label = 'Name',readonly=True),
	'label': fields.varchar(label = 'Label',readonly=True),
	'report': fields.varchar(label = 'Report',readonly=True),
	'infile': fields.varchar(label = 'Report Input File',readonly=True),
	'outfile': fields.varchar(label = 'Report Output File',readonly=True),
	}

bc_ui_reports()

class bc_actions(Model):
	_name = 'bc.actions'
	_description = 'General Model Actions'
	_columns = {
	'name': fields.varchar(label = 'Action',readonly=True),
	'ta': fields.selection(label='Type Action',selections=[('view','View'),('report','Report'),('wkf','Worlflow'),('server','Server')],readonly=True),
	'va': fields.one2many(label='View action',obj='bc.view.actions',rel='action_id'),
	'ra': fields.one2many(label='Report action',obj='bc.report.actions',rel='action_id')
	}

bc_actions()

class bc_view_actions(Model):
	_name = 'bc.view.actions'
	_description = 'General Model View Actions'
	_columns = {
	'action_id': fields.many2one(label = 'Action',obj='bc.actions',readonly=True, on_delete = 'c'),
	'view_id': fields.many2one(label='View',obj='bc.ui.views',readonly=True, on_delete = 'c')
	}

bc_view_actions()

class bc_report_actions(Model):
	_name = 'bc.report.actions'
	_description = 'General Model Report Actions'
	_columns = {
	'action_id': fields.many2one(label = 'Action',obj='bc.actions',readonly=True, on_delete = 'c'),
	'report_id': fields.many2one(label='Report',obj='bc.ui.reports',readonly=True, on_delete = 'c')
	}

bc_report_actions()


class bc_ui_menus(Model):
	_name ='bc.ui.menus'
	_description = 'General Model Application Menus'
	_order_by = 'sequence,label'
	_columns = {
	'name': fields.varchar(label = 'Name',readonly=True),
	'label': fields.varchar(label = 'Label',readonly=True),
	'parent_id': fields.many2one(label='Parent',obj='bc.ui.menus',readonly=True,on_delete='c'),
	'childs_id': fields.one2many(label='Childs',obj='bc.ui.menus',rel='parent_id',readonly=True),
	'sequence': fields.integer(label='Sequence'),
	'action_id': fields.many2one(label='Action', obj='bc.actions',readonly=True, on_delete = 'c')
	}

bc_ui_menus()
