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
	'area': fields.referenced(label='Area', obj='devel.area.messages', required=True),
	'code': fields.varchar(label='Message', size = 64),
	'descr': fields.varchar(label='Description', required=True),
	'note': fields.text(label='Note')
	}

devel_messages()

class devel_web_frameworks(Model):
	_name = 'devel.web.frameworks'
	_description = 'Web Frameworks'
	_rec_name = 'code'
	_class_object = 'D'
	_columns = {
	'code': fields.varchar(label='Web Framework',size = 64,readonly=True),
	'descr': fields.varchar(label='Description', size = 256,readonly=True)
	}

devel_web_frameworks()


class devel_ui_view_model_types(Model):
	_name = 'devel.ui.view.model.types'
	_description = 'UI Type Of View'
	_class_object = 'K'
	_columns = {
	'fullname': fields.composite(label='Full Name', cols = ['framework','code'], translate = True,required = True),
	'framework': fields.referenced(label='Web Framework',obj='devel.web.frameworks',required=True),
	'code': fields.varchar(label='Code', size = 64,required=True),
	'exclude': fields.json(label='Exclude'),
	'note': fields.text(label='Note')
	}

devel_ui_view_model_types()

class devel_ui_model_views(Model):
	_name = 'devel.ui.model.views'
	_description = 'UI Views'
	_rec_name='fullname'
	_class_object = 'K'
	_columns = {
	'fullname': fields.composite(label='Full Name', cols = ['obj','vtype'], translate = True,required = True),
	'type_obj': fields.referenced(label='ObjectType',obj='bc.type.objs'),
	'obj': fields.related(label='Object',obj='bc.objs',relatedy = ['type_obj']),
	'vtype': fields.referenced(label='View Type',obj='devel.ui.view.model.types'),
	'standalone': fields.boolean(label='Standalone View'),
	'template': fields.text(label='Template'),
	'script': fields.text(label='Script'),
	'style': fields.text(label='Style'),
	'scoped': fields.boolean(label='Scoped'),
	'sfc': fields.text(label='Single File Component'),
	'cols': fields.one2many(label='Columns', obj = 'devel.ui.model.view.columns',rel = 'view_id'),
	'inherit_cols': fields.one2many(label='Columns Inherit', obj = 'devel.ui.model.view.column.inherits',rel = 'view_id'),
	'note': fields.text(label='Note')
	}

	_default = {
		'framework':'element-plus'
	}


devel_ui_model_views()

class devel_ui_model_view_columns(Model):
	_name = 'devel.ui.model.view.columns'
	_description = 'UI Model View Columns'
	_class_object = 'K'
	_order_by="seq"
	_columns = {
	'view_id': fields.many2one(label='Model View',obj='devel.ui.model.views',rel='cols',required=True),
	'seq': fields.integer(label='Sequence', readonly = True),
	#'col': fields.many2one(label='Column',obj='bc.model.columns')
	'col': fields.varchar(label='Column', readonly = True)
	}

devel_ui_model_view_columns()

class devel_ui_model_view_column_inherits(Model):
	_name = 'devel.ui.model.view.column.inherits'
	_description = 'UI Model View Columns Inherit'
	_class_object = 'K'
	_columns = {
	'view_id': fields.many2one(label='Model View',obj='devel.ui.model.views',rel='inherit_cols',required=True),
	#'col': fields.many2one(label='Column',obj='bc.model.columns')
	'col': fields.varchar(label='Column', readonly = True)
	}

devel_ui_model_view_column_inherits()
