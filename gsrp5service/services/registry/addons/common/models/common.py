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

class common_application(Model):
	_name = 'common.application'
	_description = 'Genaral Model Sequence Access'
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
	_class_model = 'C'
	_columns = {
	'app_id': fields.many2one(label='Application',obj='common.application'),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname'),
	'name': fields.varchar(label='Name',translate = True,required = True),
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
	_class_model = 'C'
	_columns = {
	'access_sequence_id': fields.many2one(label='Access Sequence',obj='common.access.sequences'),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname'),
	'name': fields.varchar(label='Name',translate = True,required = True),
	'model': fields.many2one(label='Model', obj = 'bc.models', domain = '_compute_domain_model')
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
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname'),
	'ctype': fields.selection(label='Type',selections=[('pr','Price'),('md','Margins & Discounts'),('tax','Tax')]),
	'name': fields.varchar(label='Name',translate = True,required = True),
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
