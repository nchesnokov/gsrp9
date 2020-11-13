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

