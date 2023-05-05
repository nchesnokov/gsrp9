from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

from decimal import Decimal


AREA_COMMON = [('A','Output Documentd'),('B','Pricing'),('C','Calculation Schema')]

class common_sequences(Model):
	_name = 'common.sequencies'
	_description = 'Common Sequencies'
	_class_model = 'C'
	_rec_name = 'fullname'
	_columns = {
	'area': fields.selection(label='Area',selections=AREA_COMMON),
	'usage': fields.selection(label='Usage',selections=[('all','All')]),
	'seq': fields.varchar(label='Sequence',size=16),
	'fullname': fields.composite(label='Full Name',cols=['area','usage','seq']),
	'descr':fields.varchar(label='Description',size=64),
	'seq_access': fields.one2many(label='Sequence Access',obj='common.sequence.access',rel='seq_id'),
	'comment':fields.text(label='Comment')
	}

class common_sequence_access(Model):
	_name = 'common.sequence.access'
	_description = 'Common Sequences'
	_class_model = 'C'
	_columns = {
	'seq_id': fields.many2one(label='Common Sequence',obj='common.sequencies',rel='seq_access'),
	'seq': fields.integer(label='Sequence'),
	'model': fields.varchar(label='Model',size=4),
	'descr':fields.varchar(label='Description',size=64,compute="_getTableName"),
	'comment':fields.text(label='Comment')
	}

	def _getTableName(self,row,context):
		if row['seq_id'] and row['model_code'] is not None:
			row['descr'] = ['common','a','a'].join('.') + row['model_code']

class common_sequence_conditions(Model):
	_name = 'common.sequence.conditions'
	_description = 'Common Sequence Condition'
	_class_model = 'C'
	_rec_name = 'fullname'
	_columns = {
	'area': fields.selection(label='Area',selections=AREA_COMMON),
	'usage': fields.selection(label='Usage',selections=[]),
	'condition': fields.varchar(label='Condition',size=16),
	'fullname': fields.composite(label='Full Name',cols=['area','usage','condition']),
	'seq': fields.related(label='Sequence',relatedy=['area','usage'],obj='common.sequencies'),
	'descr':fields.varchar(label='Description',size=64),
	'class_cond': fields.selection(label='Condition Class',selections=[]),
	'calc_rule': fields.selection(label='Calculation Rule',selections=[]),
	'type_cond': fields.selection(label='Type Condition',selections=[]),
	'rounding_rule': fields.selection(label='Rounding Rule',selections=[('c','Commercial'),('d','Down Side'),('b','Big Side')]),
	'sign_cond': fields.selection(label='Condition Sign',selections=[('b','Both'),('p','Positive'),('n','Negative')]),
	'group_cond': fields.boolean(label='Group Condition'),
	'equ_round_diff': fields.boolean(label='Equalize Rounding Differences'),
	'sub_group_cond': fields.referenced(label='Subroutine Group Condition',obj='common.sequence.schemas'),
	'comment':fields.text(label='Comment')
	}

class common_sequence_schemas(Model):
	_name = 'common.sequence.schemas'
	_description = 'Common Sequence Schemas'
	_class_model = 'C'
	_rec_name = 'fullname'
	_columns = {
	'area': fields.selection(label='Area',selections=AREA_COMMON),
	'usage': fields.selection(label='Usage',selections=[]),
	'schema': fields.varchar(label='Schema',size=16),
	'fullname': fields.composite(label='Full Name',cols=['area','usage','schema']),
	'seq': fields.related(label='Sequence',relatedy=['area','usage'],obj='common.sequencies'),
	'descr':fields.varchar(label='Description',size=64),
	'comment':fields.text(label='Comment')
	}


class seq_areas(Model):
	_name = 'seq.areas'
	_description = 'Sequense Area'
	_class_model = 'C'
	_rec_name = 'area'
	_columns = {
	'area': fields.varchar(label='Area',size=8),
	'descr':fields.text(label='Description')
	}

#seq_areas()

class seq_segments(Model):
	_name = 'seq.segments'
	_description = 'Sequense Segment'
	_class_model = 'C'
	_rec_name = 'segment'
	_columns = {
	'segment': fields.varchar(label='Segment',size=8),
	'descr':fields.text(label='Description')
	}

#seq_segments()

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


#seq_access()

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

#seq_models()

class seq_model_columns(Model):
	_name = 'seq.model.columns'
	_description = 'Sequence Model Columns'
	_class_model = 'C'
	_columns = {
	'model_id': fields.many2one(label='Model',obj='seq.models',rel='columns'),
	'sequence': fields.integer(label='Sequence'),
	'col': fields.referenced(label='Column', obj='bc.model.columns'),
	'inherit_col': fields.referenced(label='Inherit Column', obj='bc.model.inherit.inherits')
	}
	
#seq_model_columns()

class seq_model_column_values(Model):
	_name = 'seq.model.column.values'
	_description = 'Sequence Model Columns'
	_class_model = 'C'
	_columns = {
	'model_id': fields.many2one(label='Model',obj='seq.models',rel='values'),
	'sequence': fields.integer(label='Sequence'),
	'col': fields.referenced(label='Column', obj='bc.model.columns'),
	'inherit_col': fields.referenced(label='Inherit Column', obj='bc.model.inherit.inherits'),
	'values': fields.json(label='Values')
	}

#seq_model_column_values()


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


#seq_conditions()



