from gsrp5service.orm import fields
from gsrp5service.orm.model import Model

import web_pdb

class devel_area_messages(Model):
	_name = 'devel.area.messages'
	_description = 'Area Messages'
	_columns = {
	'name': fields.varchar(label='Area', size = 64),
	'note': fields.text(label='Note')
	}

devel_area_messages()

class devel_messages(Model):
	_name = 'devel.messages'
	_description = 'Messages'
	_rec_name='code'
	_columns = {
	'area': fields.many2one(label='Area', obj='devel.area.messages', required=True),
	'code': fields.varchar(label='Message', size = 64),
	'descr': fields.varchar(label='Description', required=True),
	'note': fields.text(label='Note')
	}

devel_messages()

class devel_ui_view_types(Model):
	_name = 'devel.ui.view.types'
	_description = 'UI Type Of View'
	_class_model = 'C'
	_columns = {
	'framework': fields.many2one(label='Web Framework',obj='bc.frameworks',required=True),
	'name': fields.varchar(label='Name', size = 64),
	'fullname': fields.composite(label='Full Name', cols = ['framework','name'], translate = True,required = True, compute = '_compute_composite'),
	'code': fields.varchar(label='Code', size = 32,required=True),
	'note': fields.text(label='Note')
	}

devel_ui_view_types()

class devel_ui_views(Model):
	_name = 'devel.ui.models'
	_description = 'UI Models'
	_rec_name='fullname'
	_columns = {
	'fullname': fields.composite(label='Full Name', cols = ['framework','model','vtype'], translate = True,required = True, compute = '_compute_composite'),
	'framework': fields.many2one(label='Web Framework',obj='bc.frameworks',required=True),
	'model': fields.many2one(label='Model',obj='bc.models'),
	'vtype': fields.related(label='View Type',obj='devel.ui.view.types',relatedy=['framework']),
	'template': fields.text(label='Template'),
	'script': fields.text(label='Script'),
	'style': fields.text(label='Style'),
	'scoped': fields.boolean(label='Scoped'),
	'note': fields.text(label='Note')
	}

	_default = {
		'framework':'Prime'
	}


devel_ui_views()


