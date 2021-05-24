from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

from decimal import Decimal

class common_schema_access_method(ModelInherit):
	_name = 'common.schema.access.method'
	_description = 'Access Schema Method'
	_columns = {
	}

	def get_schema(self,area,segment,name,context={}):
		r = self._pool.get('seq.access.schemas').select(fields=['seq','condition','required',{'items':['seq','condition','required']}],cond=[('area','=',area),('segment','=',segment),('name','=','name')],context=context)
		if len(r) > 0:
			return r[0]['items']
		
		return []

	def get_schema_items_values(self,area,segment,name,items,context={}):
		res = []
		for item in items:
			citem = item.copy()
			citem['value'] = self._get_condition_value(area,segment,name,context)
		
		return res

	def _get_condition_value(self,area,segment,name,context={}):
		pass
		

class model_common(ModelInherit):
	_name = 'common.model'
	_description = 'Common'
	def _calculate_amount_costs(self ,record,context={}):
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

	def _calculate_items(self ,item,context={}):		
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
				r = self._pool.get('md.vat.code').read(ids,['value','subtype_vat'],context)[0]
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

	def _calculate_items_amount_costs(self ,record,context={}):
		if 'amount' in record and record['amount']:
			record['total_amount'] = record['amount']
			if 'vat_amount' in record:
				if record['vat_amount']:
					record['total_amount'] += record['vat_amount'] 
				
		return None

	def _calculate_vat_amount_costs(self ,record,context={}):
		if 'amount' in record and record['amount'] and 'vat_code' in record and record['vat_code']:
			if type(record['vat_code']) == dict:
				ids = record['vat_code']['id']
			else:
				ids = record['vat_code']
			if ids:
				r = self._pool.get('md.vat.code').read(ids,['value'],context)[0]['value']
				record['vat_amount'] = record['amount'] * Decimal('0.%s' % (r,)) 
				
		return None

	_columns = {
	}

model_common()

class inherit_common(ModelInherit):
	_name = 'common.inherit'
	_description = 'Inherit'

	_columns = {
	}
	
inherit_common()

# sequence access start

# sequence access end

class seq_access_schemas(Model):
	_name = 'seq.access.schemas'
	_description = 'Sequence Access Schema'
	_rec_name = 'fullname'
	_columns = {
	'area': fields.many2one(label='Area',obj='seq.areas',required = True),
	'segment': fields.many2one(label='Segment',obj='seq.segments',required = True),
	'name': fields.varchar(label='Name',translate = True,required = True),
	'fullname': fields.composite(label='Full Name',cols=['area','segment','name'],translate = True,required = True),
	'usage': fields.selection(label='Usage',selections=[('a','All')]),
	'items': fields.one2many(label='Items',obj='seq.access.schema.items',rel='schema_id')
	}
	
	_default = {
		'usage':'a'
	}


seq_access_schemas()

class seq_access_schema_items(Model):
	_name = 'seq.access.schema.items'
	_description = 'Sequence Access Items Of Schema'
	_order_by = 'seq'
	_columns = {
	'schema_id': fields.many2one(label='Schema',obj='seq.access.schemas',required = True),
	'seq': fields.integer(label='Sequence',required=True),
	'condition': fields.many2one(label='Condition',obj='seq.conditions',required = True),
	'required': fields.boolean(label='Required')
	}

seq_access_schema_items()
