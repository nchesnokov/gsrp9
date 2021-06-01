from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

from decimal import Decimal

class seq_areas(Model):
	_name = 'seq.areas'
	_description = 'Sequense Area'
	_class_model = 'C'
	_rec_name = 'area'
	_columns = {
	'area': fields.varchar(label='Area',size=8),
	'descr':fields.text(label='Description')
	}

seq_areas()

class seq_segments(Model):
	_name = 'seq.segments'
	_description = 'Sequense Segment'
	_class_model = 'C'
	_rec_name = 'segment'
	_columns = {
	'segment': fields.varchar(label='Segment',size=8),
	'descr':fields.text(label='Description')
	}

seq_segments()

class seq_access(Model):
	_name = 'seq.access'
	_description = 'Sequence Access'
	_class_model = 'C'
	_rec_name = 'fullname'
	_columns = {
	'area': fields.referenced(label='Area',obj='seq.areas',required = True),
	'segment': fields.referenced(label='Segment',obj='seq.segments',required = True),
	'name': fields.varchar(label='Name',translate = True,required = True),
	'fullname': fields.composite(label='Full Name',cols=['area','segment','name'],translate = True,required = True),
	'usage': fields.selection(label='Usage',selections=[('a','All')]),
	'models': fields.one2many(label='Models',obj='seq.models',rel='access_id')
	}
	
	_default = {
		'usage':'a'
	}


seq_access()

class seq_models(Model):
	_name = 'seq.models'
	_description = 'Sequence Models'
	_class_model = 'C'
	_columns = {
	'access_id': fields.many2one(label='Access Sequence',obj='seq.access',rel='models'),
	'sequence': fields.integer(label='Sequence'),
	'model': fields.referenced(label='Model', obj = 'bc.models'),
	'columns': fields.one2many(label='Columns',obj='seq.model.columns',rel='model_id'),
	'values': fields.one2many(label='Values',obj='seq.model.column.values',rel='model_id'),
	
	}

seq_models()

class seq_model_columns(Model):
	_name = 'seq.model.columns'
	_description = 'Sequence Model Columns'
	_class_model = 'C'
	_columns = {
	'model_id': fields.many2one(label='Model',obj='seq.models',rel='columns'),
	'sequence': fields.integer(label='Sequence'),
	'col': fields.referenced(label='Column', obj='bc.model.columns')
	}
	
seq_model_columns()

class seq_model_column_values(Model):
	_name = 'seq.model.column.values'
	_description = 'Sequence Model Columns'
	_class_model = 'C'
	_columns = {
	'model_id': fields.many2one(label='Model',obj='seq.models',rel='values'),
	'sequence': fields.integer(label='Sequence'),
	'col': fields.referenced(label='Column', obj='bc.model.columns')
	}

seq_model_column_values()


class seq_conditions(Model):
	_name = 'seq.conditions'
	_description = 'Sequence Condition'
	_class_model = 'C'
	_rec_name = 'fullname'
	_columns = {
	'area': fields.referenced(label='Area',obj='seq.areas',required = True),
	'segment': fields.referenced(label='Segment',obj='seq.segments',required = True),
	'name': fields.i18n(fields.varchar(label='Name',required = True)),
	'fullname': fields.composite(label='Full Name',cols=['area','segment','name'],translate = True,required = True),
	'usage': fields.selection(label='Usage',selections=[('a','All')]),
	'seq_access': fields.related(label='Sequence Access',obj='seq.access',relatedy=['area','segment','usage']),
	}
	
	_default = {
		'usage':'a'
	}


seq_conditions()



