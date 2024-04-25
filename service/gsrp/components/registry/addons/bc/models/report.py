from gsrp5service.orm import fields
from gsrp5service.orm.model import Model



class bc_type_objs(Model):
	_name = 'bc.type.objs'
	_description = 'Type Objects'
	_class_object = 'K'
	_rec_name = 'code'
	_columns = {
	'code': fields.varchar(label='Code', size = 32,readonly=True),
	'descr': fields.varchar(label='Description', size = 64,readonly=True),
	'note': fields.text(label='Note',readonly=True),
	'objs': fields.one2many(label='Objects',obj='bc.objs', rel='type_obj',readonly = True),
	'class_category_objs': fields.one2many(label='Objects',obj='bc.objs', rel='type_obj',readonly = True),
	'class_objs': fields.one2many(label='Objects',obj='bc.objs', rel='type_obj',readonly = True),

	}

class bc_class_obj_categories(Model):
	_name = 'bc.class.obj.categories'
	_description = 'Category Class Objs'
	_class_object = 'K'
	_rec_name = 'code'
	_columns = {
	'type_obj': fields.many2one(label = 'Type Object', obj = 'bc.type.objs',rel='class_category_objs',readonly=True, on_delete = 'c'),
	'code': fields.varchar(label='Code', size = 32,readonly=True),
	'descr': fields.varchar(label='Description', size = 64,readonly=True),
	'note': fields.text(label='Note',readonly=True),
	}

class bc_class_objs(Model):
	_name = 'bc.class.objs'
	_description = 'Class Objs'
	_class_object = 'K'
	_rec_name = 'code'
	_columns = {
	'type_obj': fields.many2one(label = 'Type Object', obj = 'bc.type.objs',rel='class_objs',readonly=True, on_delete = 'c'),
	'code': fields.varchar(label='Code', size = 8,readonly=True),
	'descr': fields.varchar(label='Description', size = 64,readonly=True),
	'note': fields.text(label='Note',readonly=True)
	}

class bc_objs(Model):
	_name = 'bc.objs'
	_description = 'Objects'
	_class_object = 'K'
	_order_by="module_id,code"
	_rec_name = 'code'
	_columns = {
	'module_id': fields.many2one(label = 'Module', obj = 'bc.modules',rel='objs',readonly=True, on_delete = 'c'),
	'type_obj': fields.many2one(label = 'Type Object', obj = 'bc.type.objs',rel='objs',readonly=True, on_delete = 'c'),
	'code': fields.varchar(label = 'Name', size = 64,readonly=True),
	'descr': fields.varchar(label = 'Description', size = 256,readonly=True),
	'class_obj': fields.related(label = 'Class Model', obj = 'bc.class.objs', readonly=True),
	'class_obj_category': fields.related(label = 'Class Model Category', obj = 'bc.class.obj.categories', readonly=True),
	'oom': fields.json(label='Meta Of Object', readonly = True),
	'columns': fields.one2many(label='Columns',obj='bc.obj.columns', rel='obj_id',readonly = True),
	'inherits':fields.one2many(label = 'Inherits', obj = 'bc.obj.inherit.inherits', rel = 'obj_id',readonly=True)
	}

class bc_obj_columns(Model):
	_name = 'bc.obj.columns'
	_description = 'Columns Of Model'
	_class_obj = 'K'
	#_rec_name = 'name'
	_order_by="seq"
	_columns = {
	'obj_id': fields.many2one(label = 'Object', obj = 'bc.objs',rel='columns',readonly=True, on_delete = 'c'),
	'obj_type_name': fields.varchar(label='Type Name',size=64,required = True,readonly=True),
	'obj_name': fields.varchar(label='Object Name',size=64,required = True,readonly=True),
	'name': fields.composite(label='Name Column', cols = ['obj_type_name','obj_name','col'], required = True),
	'seq': fields.integer(label='Sequence', readonly = True),
	'col': fields.varchar(label='Column', readonly=True),
	'moc': fields.json(label='Meta Of Column', readonly = True),
	}

class bc_obj_inherits(Model):
	_name = 'bc.obj.inherits'
	_description = 'Object Inherits'
	_class_object = 'K'
	_order_by="code"
	_rec_name = 'code'
	_columns = {
	'module_id': fields.many2one(label = 'Module', obj = 'bc.modules',rel='inherits',readonly=True, on_delete = 'c'),
	'type_obj': fields.referenced(label = 'Type Object', obj = 'bc.type.objs',readonly=True, on_delete = 'c'),
	'code': fields.varchar(label = 'Name', size = 64,readonly=True),
	'descr': fields.varchar(label = 'Description', size = 256,readonly=True),
	'momi': fields.json(label='Meta Of Model Inherit', readonly = True),
	'columns': fields.one2many(label='Columns', obj = 'bc.obj.inherit.columns', rel = 'inherit_id'),
	'objs': fields.one2many(label='Objects', obj = 'bc.obj.inherit.inherits', rel = 'inherit_id'),
	}

class bc_obj_inherit_columns(Model):
	_name = 'bc.obj.inherit.columns'
	_description = 'Objects Columns Inherits'
	_class_object = 'K'
	_order_by="col"
	_columns = {
	'inherit_id': fields.many2one(label = 'Object Inherit', obj = 'bc.obj.inherits', rel='columns',readonly=True, on_delete = 'c'),
	'type_obj': fields.referenced(label = 'Type Object', obj = 'bc.type.objs',readonly=True, on_delete = 'c'),
	'name': fields.composite(label='Name Column', cols = ['type_obj','inherit_id','col'], required = True),
	'seq': fields.integer(label='Sequence', readonly = True),
	'col': fields.varchar(label='Column', size = 64, readonly=True),
	'moc': fields.json(label='Meta Of Column', readonly = True),
	}

class bc_obj_inherit_inherits(Model):
	_name = 'bc.obj.inherit.inherits'
	_description = 'Inherit Columns To Objects'
	_class_object = 'K'
	_order_by="col"
	_columns = {
	'inherit_id': fields.many2one(label = 'Inherit', obj = 'bc.obj.inherits', rel='objs',readonly=True, on_delete = 'c'),
	'type_obj': fields.referenced(label = 'Type Object', obj = 'bc.type.objs',readonly=True, on_delete = 'c'),
	'obj_id': fields.referenced(label = 'Object', obj = 'bc.objs',readonly=True, on_delete = 'c'),
	'col': fields.referenced(label='Column', obj = 'bc.obj.inherit.columns', on_delete = 'c', readonly=True),
	'name': fields.composite(label='Name Column', cols = ['obj_id','col'], required = True)
	}

class bc_group_obj_access(Model):
	_name = 'bc.group.obj.access'
	_description = 'Group Object Access'
	_class_object = 'K'
	_columns = {
	'type_obj': fields.referenced(label = 'Type Object', obj = 'bc.type.objs',readonly=True, on_delete = 'c'),
	'name': fields.varchar(label="Group Access",readonly=True),
	'parent_id': fields.many2one(label='Parent',obj='bc.group.access',rel='childs_id',readonly=True),
	'childs_id': fields.one2many(label='Childs',obj='bc.group.access',rel='parent_id',readonly=True),
	'roles': fields.one2many(label='Roles',obj='bc.access',rel='group_id',readonly=True),
	'active': fields.boolean('Active',readonly=True),
	'note': fields.text(label='Note',readonly=True)
	}

class bc_obj_access(Model):
	_name = 'bc.obj.access'
	_description = 'Obj Access'
	_class_object = 'K'
	_columns = {
	'type_obj': fields.referenced(label = 'Type Object', obj = 'bc.type.objs',readonly=True, on_delete = 'c'),
	'group_id': fields.many2one(label='Group',obj='bc.group.obj.access',rel = 'bc.group.obj.access',readonly=True, on_delete = 'c'),
	'name': fields.varchar(label="Access",readonly=True),
	'objs': fields.one2many(label='Objects',obj='bc.obj.object.access',rel='obj_access_id',readonly=True),
	'inactive': fields.boolean('Inactive',readonly=True),
	'note': fields.text(label='Note',readonly=True)
	}

class bc_obj_object_access(Model):
	_name = 'bc.obj.object.access'
	_description = 'Object Access'
	_class_object = 'K'
	_order_by=['type_obj','obj']
	_columns = {
	'obj_access_id': fields.many2one(label='Access',obj='bc.access',rel='objs',readonly=True, on_delete = 'c'),
	'type_obj': fields.referenced(label = 'Type Object', obj = 'bc.type.objs',readonly=True, on_delete = 'c'),
	'obj': fields.referenced(label='Object',obj='bc.objs',readonly=True, on_delete = 'c'),
	'access': fields.json(label="Object Access"),
	'note': fields.text(label='Note',readonly=True)
	}
	
	_sql_constraints = [('obj_unique','unique (type_obj, obj)', 'Obj to be  unique in access')]

class bc_obj_data(Model):
	_name = 'bc.obj.data'
	_description = 'Loading Object Relation Data'
	_class_object = 'K'
	_table = 'bc_obj_data'
	_columns = {
	'module': fields.varchar(label = 'Module',size = 64,selectable=True,readonly=True),
	'type_obj': fields.referenced(label = 'Type Object', obj = 'bc.type.objs',readonly=True, on_delete = 'c'),
	'obj': fields.varchar(label = 'Object',size = 64,selectable=True,readonly=True),
	'name': fields.varchar(label = 'Name',size = 256,readonly=True),
	'fullname': fields.composite(label = 'Full Name',cols=['type_obj','name'],readonly=True),
	'rec_id': fields.uuid(label = 'ID record',readonly=True),
	'file_id': fields.related(label='File',obj='bc.module.files',relatedy = ['module'],readonly=True),
	'timestamp_init': fields.datetime(label = 'Timestamp init', timezone = False,readonly=True),
	'timestamp_update': fields.datetime(label = 'Timestamp update', timezone = False,readonly=True)
	}

class bc_ui_view_obj_types(Model):
	_name = 'bc.ui.view.obj.types'
	_description = 'UI Type Of View'
	_class_object = 'K'
	_columns = {
	'type_obj': fields.referenced(label = 'Type Object', obj = 'bc.type.objs',readonly=True, on_delete = 'c'),
	'framework': fields.referenced(label='Web Framework',obj='bc.web.frameworks',required=True),
	'code': fields.varchar(label='Code', size = 64,required=True),
	'fullname': fields.composite(label='Full Name', cols = ['type_obj','framework','code'], translate = True,required = True),
	'exclude': fields.json(label='Exclude'),
	'note': fields.text(label='Note')
	}

class bc_ui_obj_views(Model):
	_name = 'bc.ui.obj.views'
	_description = 'UI Views'
	_rec_name='fullname'
	_class_object = 'K'
	_columns = {
	'type_obj': fields.referenced(label = 'Type Object', obj = 'bc.type.objs',readonly=True, on_delete = 'c'),
	'obj': fields.related(label='Object',obj='bc.objs',relatedy=[()], on_delete = 'c'),
	'vtype': fields.referenced(label='View Type',obj='bc.ui.view.obj.types', on_delete = 'c'),
	'fullname': fields.composite(label='Full Name', cols = ['type_obj','obj','vtype'], translate = True,required = True),
	'created': fields.datetime('Created', readonly = True),
	'modified': fields.datetime('Modified', readonly = True),
	'standalone': fields.boolean(label='Standalone View'),
	'template_xlst': fields.text(label='Template XSLT'),
	'template': fields.text(label='Template'),
	'render': fields.text(label='Render'),
	'script': fields.text(label='Script'),
	'script_setup': fields.text(label='Script  Setup'),
	'scoped': fields.boolean(label='Scoped'),
	'style': fields.text(label='Style'),
	'i18n': fields.text(label='I18N'),
	'sfc': fields.text(label='Single File Component'),
	'cols': fields.one2many(label='Columns', obj = 'bc.ui.obj.view.columns',rel = 'view_id'),
	'inherit_cols': fields.one2many(label='Columns Inherit', obj = 'bc.ui.obj.view.column.inherits',rel = 'view_id'),
	'note': fields.text(label='Note')
	}
	
	# def _generateTemplateColumns(self,record,context):
		# #web_pdb.set_trace()
		# if record['vtype']['name'] in _GENERATEVIEW: #and (record['template'] is  None or len(record['template']) == 0):
			# return _GENERATEVIEW[record['vtype']['name']].view._generateTemplateColumns(META,record['obj']['name'],self._proxy.pool,context)


	# def _generateTemplate(self,record,context):
		# #web_pdb.set_trace()
		# if record['vtype']['name'] in _GENERATEVIEW: #and (record['template'] is  None or len(record['template']) == 0):
			# record['template'] = _GENERATEVIEW[record['vtype']['name']].view._generateTemplate(META,record['obj']['name'],self._proxy.pool,context)

	# def _generateRender(self,record,context):
		# if record['vtype']['name'] in _GENERATEVIEW: #and (record['render'] is  None or len(record['render']) == 0):
			# record['render'] = _GENERATEVIEW[record['vtype']['name']].view._generateRender(META,record['obj']['name'],self._proxy.pool,context)


	# def _generateScript(self,record,context):	
		# if record['vtype']['name'] in _GENERATEVIEW: #and (record['script'] is  None or len(record['script']) == 0):
			# record['script'] = _GENERATEVIEW[record['vtype']['name']].view._generateScript(META,record['obj']['name'],self._proxy.pool,context)

	# def _generateScriptSetup(self,record,context):	
		# if record['vtype']['name'] in _GENERATEVIEW: #and (record['script'] is  None or len(record['script']) == 0):
			# record['script_setup'] = _GENERATEVIEW[record['vtype']['name']].view._generateScriptSetup(META,record['obj']['name'],self._proxy.pool,context)


	# def _generateStyle(self,record,context):
		# if record['vtype']['name'] in _GENERATEVIEW: #and (record['style'] is  None or len(record['style']) == 0):
			# record['style'] = _GENERATEVIEW[record['vtype']['name']].view._generateStyle(META,record['obj']['name'],self._proxy.pool,context)

	# def _generateI18N(self,record,context):
		# if record['vtype']['name'] in _GENERATEVIEW: # and (record['i18n'] is  None or len(record['i18n']) == 0):
			# record['i18n'] = _GENERATEVIEW[record['vtype']['name']].view._generateI18N(META,record['obj']['name'],self._proxy.pool,context)


	# def _generateSFC(self,record,context):
		# self._generateI18N(record,context)
		# #cs = self._generateTemplateColumns(record,context)
		# # for col in record['__o2m_comtainers__']['cols']:
			# # col['template'] = cs[col['col']['name']]
		# self._generateTemplate(record,context)
		# #self._generateRender(record,context)
		# self._generateScript(record,context)
		# self._generateScriptSetup(record,context)
		# self._generateStyle(record,context)
		# #record['sfc'] = record[record['render']] if len(record['render']) > 0 else record['template'] + record['script'] + '\n' + record['style'] 
		# if 'template' in record and record['template']:
			# record['sfc'] = record['template']
		# if 'script' in record and record['script']:
			# record['sfc'] += record['script']
		# if 'script_setup' in record and record['script_setup']:
			# record['sfc'] += record['script_setup']	
		# if 'style' in record and record['style']:
			# record['sfc'] += record['style']


		# if 'i18n' in record and record['i18n']:
			# record['sfc'] += record['i18n']

		# #record['sfc'] = record['template'] if record['template'] else '' + '\n'+ record['script'] if record['script'] else ''  + '\n' + record['style'] if record['style'] else '' 
		# #print('RECORD:',self._name,record)
	# def create(self,records,context):
		# pass
		# #return self._generateSFC(record,context)

	
	# def getSFC(self, obj, vtype,context):
		# records = super(Model,self).select(fields=["fullname", "obj", "vtype", "standalone",'template','script', 'style', 'i18n','sfc',{'cols':['seq','col','template','render'],'inherit_cols':[]}], cond=[('obj','=',obj),('vtype','=', vtype)], context=context)

		# if len(records) > 0:
			# if type(records) in (list,tuple):
				# for record in records:
					# self._generateSFC(record,context)
					# for k in ('template','script','script_setup', 'style','i18n'):
						# del record[k]
			# elif type(records) == dict:
				# self._generateSFC(records,context)
				# for k in ('template','script','script_setup', 'style','i18n'):
					# del records[k]
			
			# #web_pdb.set_trace()
			# #print('RECORDS:',self._name,records[0]['__data__'])
		# return records


	# def readforupdate(self, ids, fields = None, context = {}):
		# records = super(Model,self).readforupdate(ids,fields, context)
		# # if len(records) > 0:
			# # if type(records) in (list,tuple):
				# # for record in records:
					# # self._generateSFC(record,context)
			# # elif type(records) == dict:
				# # self._generateSFC(records,context)
			
			# #web_pdb.set_trace()
			# #print('RECORDS:',self._name,records[0]['__data__'])
		# return records

	# _default = {
		# 'framework':'element-plus'
	# }

class bc_ui_obj_view_columns(Model):
	_name = 'bc.ui.obj.view.columns'
	_description = 'UI Model View Columns'
	_class_object = 'K'
	_order_by="seq"
	_columns = {
	'view_id': fields.many2one(label='Object View',obj='bc.ui.obj.views',rel='cols', on_delete = 'c',required=True),
	'seq': fields.integer(label='Sequence', readonly = True),
	'col': fields.referenced(label='Column',obj='bc.obj.columns', on_delete = 'c'),
	'template_xlst': fields.text(label='Template XSLT'),
	'template': fields.text(label='Template'),
	'render': fields.text(label='Render')
	}

class bc_ui_obj_view_column_inherits(Model):
	_name = 'bc.ui.obj.view.column.inherits'
	_description = 'UI Model View Columns Inherit'
	_class_object = 'K'
	_columns = {
	'view_id': fields.many2one(label='Object View',obj='bc.ui.obj.views',rel='inherit_cols', on_delete = 'c',required=True),
	'col': fields.referenced(label='Column',obj='bc.obj.inherit.inherits', on_delete = 'c'),
	'i18n': fields.text(label='I18N'),
	'template_xlst': fields.text(label='Template XSLT'),
	'template': fields.text(label='Template'),
	'render': fields.text(label='Render'),
	'script': fields.text(label='Script')
	}

class bc_obj_translations(Model):
	_name = 'bc.obj.translations'
	_description = 'Object Translations'
	_class_object = 'K'
	_columns = {
	'lang': fields.referenced(label='Language',obj='bc.langs',readonly=True, on_delete = 'c'),
	'type_obj': fields.referenced(label = 'Type Object', obj = 'bc.type.objs',readonly=True, on_delete = 'c'),
	'obj': fields.referenced(label='Object',obj='bc.objs',readonly=True, on_delete = 'c'),
	'tr': fields.json(label='Translations',readonly=True),
	'inherits': fields.one2many(label='Inherits',obj='bc.obj.translation.inherits',rel='inherit_id')
	}

class bc_obj_translation_inherits(Model):
	_name = 'bc.obj.translation.inherits'
	_description = 'Object Translations Inherit'
	_class_object = 'K'
	_columns = {
	'inherit_id': fields.many2one(label='Translation Object',obj='bc.obj.translations',rel='inherits',readonly=True, on_delete = 'c'),
	'tr': fields.json(label='Translations',readonly=True),
	}

class bc_tuning_ui_obj_views(Model):
	_name = 'bc.tuning.ui.obj.views'
	_description = 'Tunning Objects Views'
	_class_object = 'K'
	_columns = {
	'fullname': fields.i18n(fields.composite(label='Full Name', cols = ['tuser','view','name'], required = True)),
	'name':fields.varchar(label='Name',size=128,readonly=True),
	'view':fields.referenced(label = 'View', obj='bc.ui.obj.views',readonly=True, on_delete = 'c'),
	'tuser': fields.referenced(label = 'User', obj='bc.users',readonly=True, on_delete = 'c'),
	'values': fields.json(label='Values',readonly=True)
	}

	_sql_constraints = [('view_id_seq_unique','unique (tuser,view, name)', 'Sequence unique of views')]

class bc_global_tuning_ui_obj_views(Model):
	_name = 'bc.global.tuning.ui.obj.views'
	_description = 'Global Tunning Objct Views'
	_class_object = 'K'
	_columns = {
	'name':fields.varchar(label='Name',size=128,readonly=True),
	'view':fields.referenced(label = 'View', obj='bc.ui.obj.views',readonly=True, on_delete = 'c'),
	'fullname': fields.i18n(fields.composite(label='Full Name', cols = ['view','name'], required = True)),
	'values': fields.json(label='Values',readonly=True)
	}

	_sql_constraints = [('view_id_seq_unique','unique (view, name)', 'Sequence unique of views')]

class bc_ui_obj_actions(Model):
	_name = 'bc.ui.obj.actions'
	_description = 'Object UI Actions'
	_class_object = 'K'
	_columns = {
	'type_obj': fields.referenced(label = 'Type Object', obj = 'bc.type.objs',readonly=True, on_delete = 'c'),
	'name': fields.varchar(label = 'Object Action',readonly=True),
	'fullname': fields.composite(label='Fullname',cols=['type_obj','name'],readonly=True),
	'obj': fields.referenced(label='Object',obj = 'bc.objs')
	}

class bc_ui_framework_obj_actions(Model):
	_name = 'bc.ui.framework.obj.actions'
	_description = 'Object UI Framework Actions'
	_class_object = 'K'
	_columns = {
	'type_obj': fields.referenced(label = 'Type Object', obj = 'bc.type.objs',readonly=True, on_delete = 'c'),
	'framework_id': fields.referenced(label='Framework',obj = 'bc.web.frameworks'),
	'action_id': fields.referenced(label='Action',obj = 'bc.ui.obj.actions'),
	'fullname': fields.composite(label='Full Name', cols = ['type_obj','framework_id','action_id'], required = True),
	'view_id': fields.related(label='View',obj='bc.ui.obj.views',relatedy=['type_obj',('framework_id','code')],readonly=True, on_delete = 'c')
	}

class bc_ui_obj_menus(Model):
	_name ='bc.ui.obj.menus'
	_description = 'Object UI Menus'
	_class_object = 'K'
	_order_by = 'sequence,label'
	_columns = {
	'type_obj': fields.referenced(label = 'Type Object', obj = 'bc.type.objs',readonly=True, on_delete = 'c'),
	'name': fields.varchar(label = 'Name',readonly=True),
	'fullname': fields.composite(label='Fullname',cols=['type_obj','name'],readonly=True),
	'label': fields.varchar(label = 'Label',readonly=True),
	'parent_id': fields.many2one(label='Parent',obj='bc.ui.obj.menus',rel='childs_id',readonly=True,on_delete='c'),
	'childs_id': fields.one2many(label='Childs',obj='bc.ui.obj.menus',rel='parent_id',readonly=True),
	'sequence': fields.integer(label='Sequence'),
	'action_id': fields.referenced(label='Action', obj='bc.ui.obj.actions',readonly=True, on_delete = 'c')
	}

class bc_access_objs(Model):
	_name = 'bc.access.objs'
	_description = 'Access Objects'
	_class_object = 'K'
	_columns = {
	'type_obj': fields.referenced(label = 'Type Object', obj = 'bc.type.objs',readonly=True, on_delete = 'c'),
	'name': fields.varchar(label = 'Name',readonly=True),
	'fullname': fields.composite(label='Fullname',cols=['type_obj','name']),
	'obj': fields.related(label = 'Object',obj='bc.objs',relatedy=['type_obj'],readonly=True,on_delete='c'),
	'note': fields.text(label='Note',readonly=True)
	}

class bc_auth_objs(Model):
	_name = 'bc.auth.objs'
	_description = 'Auth Objects'
	_class_object = 'K'
	_columns = {
	'type_obj': fields.referenced(label = 'Type Object', obj = 'bc.type.objs',readonly=True, on_delete = 'c'),
	'name': fields.varchar(label = 'Name',readonly=True),
	'fullname': fields.composite(label='Fullname',cols=['type_obj','name']),
	'obj': fields.related(label = 'Object',obj='bc.objs',relatedy=['type_obj'],readonly=True,on_delete='c'),
	'note': fields.text(label='Note',readonly=True)
	}

class bc_user_obj_access(Model):
	_name = 'bc.user.obj.access'
	_description = 'User Access Objects'
	_class_object = 'K'
	_columns = {
	'user_id': fields.many2one(label = 'User',obj = 'bc.users',rel = 'access',readonly=True),
	'type_obj': fields.referenced(label = 'Type Object', obj = 'bc.type.objs',readonly=True, on_delete = 'c'),
	'obj': fields.related(label = 'Object',obj='bc.objs',relatedy=['type_obj'],readonly=True,on_delete='c'),
	'note': fields.text(label='Note',readonly=True)
	}

class bc_user_obj_auths(Model):
	_name = 'bc.user.obj.auths'
	_description = 'User Auth Objects'
	_class_object = 'K'
	_columns = {
	'user_id': fields.many2one(label = 'User',obj = 'bc.users',rel = 'auth', on_delete = 'c',readonly=True),
	'type_obj': fields.referenced(label = 'Type Object', obj = 'bc.type.objs',readonly=True, on_delete = 'c'),
	'obj': fields.related(label = 'Object',obj='bc.objs',relatedy=['type_obj'],readonly=True,on_delete='c'),
	'note': fields.text(label='Note',readonly=True)
	}
