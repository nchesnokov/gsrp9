from gsrp5service.orm import fields
from gsrp5service.orm.model import Model,ModelInherit

import web_pdb

class devel_area_messages(Model):
	_name = 'devel.area.messages'
	_description = 'Area Messages'
	_class_object = 'D'
	_columns = {
	'name': fields.varchar(label='Area', size = 64),
	'note': fields.text(label='Note')
	}

devel_area_messages()

class devel_messages(Model):
	_name = 'devel.messages'
	_description = 'Messages'
	_rec_name='code'
	_class_object = 'D'
	_columns = {
	'area': fields.many2one(label='Area', obj='devel.area.messages', required=True),
	'code': fields.varchar(label='Message', size = 64),
	'descr': fields.varchar(label='Description', required=True),
	'note': fields.text(label='Note')
	}

devel_messages()

class devel_web_frameworks(Model):
	_name = 'devel.web.frameworks'
	_description = 'Web Frameworks'
	_rec_name = 'code'
	_class_object = 'd'
	_columns = {
	'code': fields.varchar(label='Web Framework',size = 16,readonly=True),
	'descr': fields.varchar(label='Description', size = 64,readonly=True)
	}

devel_web_frameworks()



class devel_ui_view_model_types(Model):
	_name = 'devel.ui.view.model.types'
	_description = 'UI Type Of View'
	_class_object = 'D'
	_columns = {
	'fullname': fields.composite(label='Full Name', cols = ['framework','otype','code'], translate = True,required = True, compute = '_compute_composite'),
	'framework': fields.many2one(label='Web Framework',obj='devel.web.frameworks',required=True),
	'code': fields.varchar(label='Code', size = 32,required=True),
	'note': fields.text(label='Note')
	}

devel_ui_view_model_types()

class devel_ui_model_views(Model):
	_name = 'devel.ui.model.views'
	_description = 'UI Views'
	_rec_name='fullname'
	_class_object = 'D'
	_columns = {
	'fullname': fields.composite(label='Full Name', cols = ['framework','model','vtype'], translate = True,required = True, compute = '_compute_composite'),
	'framework': fields.many2one(label='Web Framework',obj='devel.web.frameworks',required=True),
	'model': fields.many2one(label='Object',obj='bc.models'),
	'vtype': fields.related(label='View Type',obj='devel.ui.view.model.types', relatedy=['framework']),
	'template': fields.text(label='Template'),
	'script': fields.text(label='Script'),
	'style': fields.text(label='Style'),
	'scoped': fields.boolean(label='Scoped'),
	'sfc': fields.text(label='Single File Component'),
	'cols': fields.one2many(label='Columns', obj = 'devel.ui.model.view.columns',rel = 'view_id'),
	'note': fields.text(label='Note')
	}

	_default = {
		'framework':'element-plus'
	}


devel_ui_model_views()

class devel_ui_model_view_columns(Model):
	_name = 'devel.ui.model.view.columns'
	_description = 'UI View Columns'
	_class_object = 'D'
	_columns = {
	'view_id': fields.many2one(label='Model View',obj='devel.ui.model.views',required=True),
	'col': fields.many2one(label='Column',obj='bc.model.columns')
	}



devel_ui_model_view_columns()


class devel_model_translations(Model):
	_name = 'devel.model.translations'
	_description = 'Model Translations'
	_class_object = 'D'
	_columns = {
	'lang': fields.many2one(label='Language',obj='bc.langs',readonly=True, on_delete = 'c'),
	'otype': fields.selection(label='Object Type', selections = [('model','Model')]),
	'model': fields.many2one(label='Object',obj='bc.models',readonly=True, on_delete = 'c'),
	'tr': fields.json(label='Translations',readonly=True),
	'inherits': fields.one2many(label='Inherits',obj='devel.model.translation.inherits',rel='inherit_id')
	}

devel_model_translations()

class devel_model_translation_inherits(Model):
	_name = 'devel.model.translation.inherits'
	_description = 'Model Translations Inherit'
	_class_object = 'D'
	_columns = {
	'obj_tr_id': fields.many2one(label='Translation Object',obj='devel.model.translations',readonly=True, on_delete = 'c'),
	'tr': fields.json(label='Translations',readonly=True),
	}

devel_model_translation_inherits()

	


class devel_tuning_ui_model_views(Model):
	_name = 'devel.tuning.ui.model.views'
	_description = 'Tunning Models Views'
	_class_object = 'D'
	_columns = {
	'fullname': fields.i18n(fields.composite(label='Full Name', cols = ['tuser','view','name'], required = True, compute = '_compute_composite')),
	'name':fields.varchar(label='Name',size=128,readonly=True),
	'view':fields.many2one(label = 'View', obj='devel.ui.model.views',readonly=True, on_delete = 'c'),
	'tuser': fields.many2one(label = 'User', obj='bc.users',readonly=True, on_delete = 'c'),
	'values': fields.json(label='Values',readonly=True)
	}

	_sql_constraints = [('view_id_seq_unique','unique (tuser,view, name)', 'Sequence unique of vies')]

devel_tuning_ui_model_views()



class devel_general_tuning_ui_model_views(Model):
	_name = 'devel.general.tuning.ui.model.views'
	_description = 'General Tunning Models Views'
	_class_object = 'D'
	_columns = {
	'fullname': fields.i18n(fields.composite(label='Full Name', cols = ['view','name'], required = True, compute = '_compute_composite')),
	'name':fields.varchar(label='Name',size=128,readonly=True),
	'view':fields.many2one(label = 'View', obj='devel.ui.model.views',readonly=True, on_delete = 'c'),
	'values': fields.json(label='Values',readonly=True)
	}

	_sql_constraints = [('view_id_seq_unique','unique (view, name)', 'Sequence unique of vies')]

devel_general_tuning_ui_model_views()

class devel_ui_model_actions(Model):
	_name = 'devel.ui.model.actions'
	_description = 'Model UI Actions'
	_class_object = 'D'
	_columns = {
	'name': fields.varchar(label = 'Model Action',readonly=True),
	'view_id': fields.many2one(label='View',obj='devel.ui.model.views',readonly=True, on_delete = 'c')
	}

devel_ui_model_actions()

class devel_ui_model_menus(Model):
	_name ='devel.ui.model.menus'
	_description = 'UI Menus'
	_class_object = 'D'
	_order_by = 'sequence,label'
	_columns = {
	'name': fields.varchar(label = 'Name',readonly=True),
	'label': fields.varchar(label = 'Label',readonly=True),
	'parent_id': fields.many2one(label='Parent',obj='devel.ui.model.menus',readonly=True,on_delete='c'),
	'childs_id': fields.one2many(label='Childs',obj='devel.ui.model.menus',rel='parent_id',readonly=True),
	'sequence': fields.integer(label='Sequence'),
	'action_id': fields.many2one(label='Action', obj='devel.ui.model.actions',readonly=True, on_delete = 'c')
	}

devel_ui_model_menus()


class devel_bc_framework_inherit(ModelInherit):
	_name = 'devel.bc.framework.inherit'
	_description = 'BC module framework inherit'
	_inherit = {'bc.user.preferences':{'_columns':['framework']}}
	_columns = {
		'framework': fields.many2one(label='Framework',obj='devel.web.frameworks')
	}
