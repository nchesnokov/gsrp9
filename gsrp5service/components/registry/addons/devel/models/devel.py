from gsrp5service.orm import fields
from gsrp5service.orm.model import Model

import web_pdb

class devel_area_messages(Model):
	_name = 'devel.area.messages'
	_description = 'Area Messages'
	_class_model = 'D'
	_columns = {
	'name': fields.varchar(label='Area', size = 64),
	'note': fields.text(label='Note')
	}

devel_area_messages()

class devel_messages(Model):
	_name = 'devel.messages'
	_description = 'Messages'
	_rec_name='code'
	_class_model = 'D'
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
	_class_model = 'd'
	_columns = {
	'code': fields.varchar(label='Web Framework',size = 16,readonly=True),
	'descr': fields.varchar(label='Description', size = 64,readonly=True)
	}

devel_web_frameworks()



class devel_ui_view_types(Model):
	_name = 'devel.ui.view.types'
	_description = 'UI Type Of View'
	_class_model = 'D'
	_columns = {
	'fullname': fields.composite(label='Full Name', cols = ['framework','code'], translate = True,required = True, compute = '_compute_composite'),
	'framework': fields.many2one(label='Web Framework',obj='devel.web.frameworks',required=True),
	'code': fields.varchar(label='Code', size = 32,required=True),
	'note': fields.text(label='Note')
	}

devel_ui_view_types()

class devel_meta_ui_views(Model):
	_name = 'devel.meta.ui.views'
	_description = 'Models views'
	_class_model = 'D'
	_columns = {
	'fullname': fields.composite(label='Full Name', cols = ['framework','model','vtype'], translate = True,required = True, compute = '_compute_composite'),
	'framework': fields.many2one(label='Framework',obj='bc.web.frameworks'),
	'model': fields.varchar(label = 'Model Name', size = 64,selectable=True,readonly=True),
	'vtype': fields.related(label='View Type',obj='devel.ui.view.types',relatedy=['framework']),
	'arch': fields.xml(label = 'Arch Blob',readonly=True),
	'inherit_views': fields.one2many(label='Inherit Views',obj='bc.ui.view.inherits',rel='view_id',readonly=True)
	}

devel_meta_ui_views()

class devel_meta_ui_view_inherits(Model):
	_name = 'devel.meta.ui.view.inherits'
	_description = 'Meta Views Inherits'
	_class_model = 'D'
	_columns = {
	'view_id': fields.many2one(label='View',obj='bc.ui.views',readonly=True),
	'inherit_name':fields.varchar(label = 'Inherit', size = 128,readonly=True),
	'arch':fields.xml(label = 'Arch Blob',readonly=True)
	}

devel_meta_ui_views_inherit()

class devel_ui_views(Model):
	_name = 'devel.ui.views'
	_description = 'UI Views'
	_rec_name='fullname'
	_class_model = 'D'
	_columns = {
	'fullname': fields.composite(label='Full Name', cols = ['framework','model','vtype'], translate = True,required = True, compute = '_compute_composite'),
	'framework': fields.many2one(label='Web Framework',obj='bc.web.frameworks',required=True),
	'model': fields.many2one(label='Model',obj='bc.models'),
	'vtype': fields.related(label='View Type',obj='devel.ui.view.types',relatedy=['framework']),
	'template': fields.text(label='Template'),
	'script': fields.text(label='Script'),
	'style': fields.text(label='Style'),
	'scoped': fields.boolean(label='Scoped'),
	'inherits': fields.one2many(label='Inherits',obj='devel.ui.view.inherits'),
	'note': fields.text(label='Note')
	}

	_default = {
		'framework':'EL'
	}


devel_ui_views()

class devel_tuning_ui_views(Model):
	_name = 'devel.tuning.ui.views'
	_description = 'Tunning Models Views'
	_class_model = 'D'
	_columns = {
	'name':fields.varchar(label='Name',size=128,readonly=True),
	'view':fields.many2one(label = 'View', obj='bc.ui.views',readonly=True, on_delete = 'c'),
	'tuser': fields.many2one(label = 'User', obj='bc.users',readonly=True, on_delete = 'c'),
	'fullname': fields.i18n(fields.composite(label='Full Name', cols = ['tuser','view','name'], required = True, compute = '_compute_composite')),
	'values': fields.json(label='Values',readonly=True)
	}

	_sql_constraints = [('view_id_seq_unique','unique (tuser,view, name)', 'Sequence unique of vies')]

devel_tuning_ui_views()



class devel_general_tuning_ui_views(Model):
	_name = 'devel.general.tuning.ui.views'
	_description = 'General Tunning Models Views'
	_class_model = 'D'
	_columns = {
	'name':fields.varchar(label='Name',size=128,readonly=True),
	'view':fields.many2one(label = 'View', obj='bc.ui.views',readonly=True, on_delete = 'c'),
	'fullname': fields.i18n(fields.composite(label='Full Name', cols = ['view','name'], required = True, compute = '_compute_composite')),
	'values': fields.json(label='Values',readonly=True)
	}

	_sql_constraints = [('view_id_seq_unique','unique (view, name)', 'Sequence unique of vies')]

devel_general_tuning_ui_views()

class devel_bc_framework_inherit(ModelInherit):
	_name = 'devel.bc.framework.inherit'
	_description = 'BC module framework inherit'
	_inherit = {'bc.user.preferences':{'_columns':['framework']}}
	_columns = {
	'framework': fields.many2one(label='Framework',obj='devel.web.frameworks')
	}
