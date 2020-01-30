from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

from decimal import Decimal

class model_common(ModelInherit):
	_name = 'common.model'
	_description = 'Genaral Model Common'
	def _calculate_amount_costs(self,cr,pool,uid,record,context={}):
		fields = ['amount','vat_amount','total_amount']
		for field in fields:
			if field in record:
				record[field] = None
			for o2mfield in self._o2mfields:
				if o2mfield in record:
					for rec in record[o2mfield]:
						if field in rec and rec[field]:
							if field not in record or record[field] is None:
								record[field] = rec[field]
							else:
								record[field] += rec[field]

		return None

	def _calculate_items(self,cr,pool,uid,item,context={}):		
		if 'delivery_schedules' in item:
			item['quantity'] = None
			for d in item['delivery_schedules']:
				if item['quantity']:
					item['quantity'] += d['quantity']
				else:
					item['quantity'] = d['quantity']
			if 'quantity' in item and item['quantity'] and 'price' in item and item['price'] and 'unit' in item and item['unit']:
				item['amount'] = item['quantity'] * item['price'] / item['unit']

				if 'volume' in item and item['volume']:
					item['volume_total'] =  item['quantity'] * Decimal(item['volume'])

				if 'weight' in item and item['weight']:
					item['weight_total'] =  item['quantity'] * Decimal(item['weight'])

			elif item['quantity'] is None:
				item['amount'] = None
				item['vat_amount'] = None
				item['total_amount'] = None
		
		if 'amount' in item and item['amount'] and 'vat_code' in item and item['vat_code']:
			if type(item['vat_code']) == dict:
				ids = item['vat_code']['id']
			else:
				ids = item['vat_code']
			if ids:
				r = pool.get('md.vat.code').read(cr,pool,uid,ids,['value','subtype_vat'],context)[0]
				v = r['value']
				s = r['subtype_vat']
				if s == 'e':
					item['vat_amount'] = item['amount'] * Decimal('0.%s' % (v,)) 
				elif s == 'i':
					item['vat_amount'] = item['amount'] - item['amount'] * Decimal('0.%s' % (v,)) 

		if 'amount' in item and item['amount']:
			item['total_amount'] = item['amount']
			if 'vat_amount' in item:
				if item['vat_amount']:
					item['total_amount'] += item['vat_amount'] 
		elif item['amount'] is None:
			item['vat_amount'] = None
			item['total_amount'] = None


		return None

	def _calculate_items_amount_costs(self,cr,pool,uid,record,context={}):
		if 'amount' in record and record['amount']:
			record['total_amount'] = record['amount']
			if 'vat_amount' in record:
				if record['vat_amount']:
					record['total_amount'] += record['vat_amount'] 
				
		return None

	def _calculate_vat_amount_costs(self,cr,pool,uid,record,context={}):
		if 'amount' in record and record['amount'] and 'vat_code' in record and record['vat_code']:
			if type(record['vat_code']) == dict:
				ids = record['vat_code']['id']
			else:
				ids = record['vat_code']
			if ids:
				r = pool.get('md.vat.code').read(cr,pool,uid,ids,['value'],context)[0]['value']
				record['vat_amount'] = record['amount'] * Decimal('0.%s' % (r,)) 
				
		return None

	_columns = {
	}

model_common()

class inherit_common(ModelInherit):
	_name = 'common.inherit'
	_description = 'Genaral Model Inherit'

	_columns = {
	}
	
inherit_common()

# sequence access start

class seq_areas(Model):
	_name = 'seq.areas'
	_description = 'Genaral Model Sequense Area'
	_class_model = 'C'
	_rec_name = 'area'
	_columns = {
	'area': fields.varchar(label='Area',size=8),
	'descr':fields.text(label='Description')
	}

seq_areas()

class seq_segmens(Model):
	_name = 'seq.segments'
	_description = 'Genaral Model Sequense Area'
	_class_model = 'C'
	_rec_name = 'area'
	_columns = {
	'segment': fields.varchar(label='Segment',size=8),
	'descr':fields.text(label='Description')
	}

seq_segments()

class seq_access(Model):
	_name = 'seq.access'
	_description = 'Genaral Model Sequence Access'
	_class_model = 'C'
	_rec_name = 'fullname'
	_columns = {
	'area': fields.many2one(label='Area',obj='seq.areas',required = True),
	'segment': fields.many2one(label='Segment',obj='seq.segments',required = True),
	'name': fields.varchar(label='Name',translate = True,required = True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname'),
	'usage': fields.selection(label='Usage',selections=[('a','All')]),
	'models': fields.one2many(label='Models',obj='seq.models',rel='access_id')
	}

	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''
		if 'area' in item and 'name' in item['area'] and item['area']['name']:
			v += item['area']['name']

		if 'segment' in item and 'name' in item['segment'] and item['segment']['name']:
			v += '/' + item['segment']['name']

		if item['name']:
			v += '/' + item['name']
		
		if len(v) > 0:
			item['fullname'] = v
	
	_default = {
		'usage':'a'
	}


seq_accesss()

class seq_models(Model):
	_name = 'seq.models'
	_description = 'Genaral Model Sequence Models'
	_class_model = 'C'
	_columns = {
	'access_id': fields.many2one(label='Access Sequence',obj='seq.access'),
	'sequence': fields.integer(label='Sequence'),
	'model': fields.many2one(label='Model', obj = 'bc.models'),
	'columns': fields.one2many(label='Columns',obj='seq.model.columns',rel='model_id'),
	'values': fields.one2many(label='Values',obj='seq.model.column.values',rel='model_id'),
	
	}

seq_models()

class seq_model_columns(Model):
	_name = 'seq.model.columns'
	_description = 'Genaral Model Sequence Model Columns'
	_class_model = 'C'
	_columns = {
	'model_id': fields.many2one(label='Model',obj='seq.models'),
	'sequence': fields.integer(label='Sequence'),
	'column': fields.related(label='Column', obj = 'bc.columns',relatedy=['model_id'])
	}

seq_model_columns()

class seq_model_column_values(Model):
	_name = 'seq.model.column.values'
	_description = 'Genaral Model Sequence Model Columns'
	_class_model = 'C'
	_columns = {
	'model_id': fields.many2one(label='Model',obj='seq.models'),
	'sequence': fields.integer(label='Sequence'),
	'column': fields.related(label='Column', obj = 'bc.columns',relatedy=['model_id'])
	}

seq_model_column_values()


class seq_conditions(Model):
	_name = 'seq.conditions'
	_description = 'Genaral Model Sequence Condition'
	_class_model = 'C'
	_columns = {
	'area': fields.many2one(label='Area',obj='seq.areas',required = True),
	'segment': fields.many2one(label='Segment',obj='seq.segments',required = True),
	'name': fields.varchar(label='Name',translate = True,required = True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname'),
	'usage': fields.selection(label='Usage',selections=[('a','All')]),
	'seq_access': fields.related(label='Sequence Access',obj='seq.access',relatedy=['area','segment','usage']),
	}

	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''
		if 'usage' in item and 'name' in item['usage'] and item['usage']['name']:
			v += item['usage']['name']

		if 'area' in item and 'name' in item['area'] and item['area']['name']:
			v += '/' + item['area']['name']


		if item['name']:
			v += '/' + item['name']
		
		if len(v) > 0:
			item['fullname'] = v

	
	_default = {
		'usage':'b'
	}


seq_conditions()


# sequence access end



class common_application(Model):
	_name = 'common.application'
	_description = 'Genaral Model Application'
	_class_model = 'C'
	_rec_name = 'app'
	_columns = {
	'app': fields.selection(label='Application',selections=[('a','Price'),('b','Output Formular')]),
	'sequences': fields.one2many(label='Sequences',obj='common.access.sequences',rel='app_id'),
	'conditions': fields.one2many(label='Conditions',obj='common.conditions',rel='app_id'),
	}

	_default = {
		'app':'a'
	}

common_application()


class common_access_sequences(Model):
	_name = 'common.access.sequences'
	_description = 'Genaral Model Sequence Access'
	_rec_name = 'fullname'
	_class_model = 'C'
	_columns = {
	'app_id': fields.many2one(label='Application',obj='common.application'),
	'name': fields.varchar(label='Name',translate = True,required = True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname'),
	'models': fields.one2many(label='Models',obj = 'common.access.sequence.models',rel = 'access_sequence_id')
	}

	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''
		if 'app_id' in item and 'name' in item['app_id'] and item['app_id']['name']:
			v += item['app_id']['name']

		if item['name']:
			v += '/' + item['name']
		
		if len(v) > 0:
			item['fullname'] = v

	_default = {
		'app':'a'
	}

common_access_sequences()

class common_access_sequence_models(Model):
	_name = 'common.access.sequence.models'
	_description = 'Genaral Model Models Sequence Access'
	_rec_name = 'fullname'
	_class_model = 'C'
	_columns = {
	'access_sequence_id': fields.many2one(label='Access Sequence',obj='common.access.sequences'),
	'name': fields.varchar(label='Name',translate = True,required = True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname'),
	#'model': fields.many2one(label='Model', obj = 'bc.models', domain = '_compute_domain_model')
	'model': fields.many2one(label='Model', obj = 'bc.models', domain = [('name','between',('common.price.a0001','common.price.a9999'))])
	}

	def _compute_domain_model(self,cr,pool,uid,item,context):
		return [('name','between',('common.price.a0001','common.price.a9999'))]

	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''
		if 'access_sequence_id' in item and 'name' in item['access_sequence_id'] and item['access_sequence_id']['name']:
			v += item['access_sequence_id']['name']

		if item['name']:
			v += '/' + item['name']
		
		if len(v) > 0:
			item['fullname'] = v

common_access_sequence_models()

class common_conditions(Model):
	_name = 'common.conditions'
	_description = 'Genaral Model Conditions'
	_class_model = 'C'
	_columns = {
	'app_id': fields.many2one(label='Application',obj='common.application'),
	'name': fields.varchar(label='Name',translate = True,required = True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname'),
	'ctype': fields.selection(label='Class Of Type',selections=[('pr','Price'),('ma','Margins'),('di','Discounts'),('tax','Tax')]),
	#'ttype': fields.selection(label='Type Of Type',selections=[('pr','Price'),('ma','Margins'),('di','Discounts'),('tax','Tax')]),
	#'crule': fields.selection(label='Rule',selections=[('q','Quantity'),('%','Persent'),('a','Amount'),('w','Weigth')]),
	'access_sequense': fields.related(label='Sequence Access',obj = 'common.access.sequences',relatedy = ['app'])
	}

	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''
		if 'app_id' in item and 'name' in item['app_id'] and item['app_id']['name']:
			v += item['app_id']['name']

		if item['ctype']:
			v += '/' + item['ctype']


		if item['name']:
			v += '/' + item['name']
		
		if len(v) > 0:
			item['fullname'] = v

	
	_default = {
		'ctype':'pr'
	}


common_conditions()
