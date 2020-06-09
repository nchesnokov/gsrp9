from gsrp5service.orm import fields
from gsrp5service.orm.model import Model,ModelInherit

import web_pdb


class model_common(ModelInherit):
	_name = 'mm.common.model'
	_description = 'Manufsctured management Common'
	def _calculate_amount_costs(self,cr,pool,uid,record,context={}):
		fields = ['amount']
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

	def _calculate_parts(self,cr,pool,uid,item,context={}):		
		if 'schedules' in item and item['schedules']:
			item['parts'] = None
			for r in item['schedules']:
				if item['parts'] is None:
					item['parts'] = r['part']
				else:
					item['parts'] += r['part']

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.mm.product').select(cr,pool,uid,['uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
			if len(p) > 0:
				for f in ('uom','price','currency','unit','uop'):
					if f not in item or item[f] != p[0][f]:
						item[f] = p[0][f]
			else:
				for f in ('uom','price','currency','unit','uop'):
					if f in ('price','unit'):
						if f in self._default:
							item[f] = self._default[f]
						else:
							item[f] = None
					else:
						item[f] = {'id':None,'name':None}

	def _calculate_item(self,cr,pool,uid,item,context={}):
		if 'quantity' in item and item['quantity'] and 'uom' in item and item['uom'] and 'price' in item and item['price'] and 'currency' in item and item['currency'] and 'unit' in item and item['unit'] and 'uop' in item and item['uop']:
			item['amount'] = item['price'] / item['unit'] * item['quantity']



#production
class mm_production_orders(Model):
	_name = 'mm.production.orders'
	_description = 'Production Order'
	_inherits = {'mm.common.model':{'_methods':['_calculate_amount_costs','_calculate_parts']}}
	_date = 'dopo'
	_columns = {
	'otype': fields.many2one(label='Type',obj='mm.production.order.types',on_change='_on_change_otype', required = True),
	'name': fields.varchar(label = 'Name'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'fullname': fields.composite(label='Full Name', cols = ['company','otype','name'], translate = True,required = True, compute = '_compute_composite'),
	 'map': fields.many2one(label='Map',obj= 'mm.production.maps',on_change='_on_change_map'),
	'bom': fields.many2one(label='BoM',obj='md.boms',on_change='_on_change_bom'),
	'product': fields.many2one(label='Production Product',obj='md.product',readonly=True),
	'part': fields.numeric(label='Production Part',size=(11,3), readonly=True),
	'category_id': fields.many2one(label='Category',obj='mm.production.order.category'),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'origin': fields.varchar(label = 'Origin'),
	'dopo': fields.date(label='Date Of Production Order',required=True),
	'from_date': fields.date(label='Start Date Of Production Order',required=True),
	'to_date': fields.date(label='End Date Of Production Order',required=True),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'parts': fields.numeric(label='Parts',size=(11,3),compute='_calculate_parts'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'schedules': fields.one2many(label='Schedule',obj='mm.production.order.schedules',rel='order_id'),
	'ops': fields.one2many(label='Ops',obj='mm.production.order.ops',rel='order_id'),
	'items': fields.one2many(label='Items',obj='mm.production.order.items',rel='order_id'),
	'roles': fields.one2many(label='Roles',obj='mm.production.order.roles',rel='order_id'),
	'pricing': fields.one2many(label='Pricing',obj='mm.production.order.pricing',rel='order_id'),
	'texts': fields.one2many(label='Texts',obj='mm.production.order.texts',rel='order_id'),
	'note': fields.text(label='Note')}

	_default = {
		'state':'draft'
	}

	def _on_change_otype(self,cr,pool,uid,item,context={}):		
		roles = pool.get('mm.production.order.type.roles').select(cr,pool,uid,['role_id'],[('type_id','=',item['otype']['name'])],context)
		for role in roles:
			item_role = pool.get('mm.production.order.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)
		
		types = pool.get('mm.production.order.types').select(cr,pool,uid,['htschema'],[('name','=',item['otype']['name'])],context)	
		texts1 = pool.get('mm.schema.texts').select(cr,pool,uid,['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = pool.get('mm.production.order.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

	def _on_change_map(self,cr,pool,uid,item,context={}):
		if  item['map'] and 'name' in item['map'] and item['map']['name']:
			m = pool.get('mm.production.maps').select(cr,pool,uid,['fullname','bom',{'ops':['prev','op','next','workcenter','duration','uod','per_cicle','note']}],[('fullname','=',item['map']['name'])],context)		
			if len(m) > 0:
				if m[0]['bom']:
					item['bom'] = m[0]['bom']
				if len(m[0]['ops']) > 0:
					for op in m[0]['ops']:
						ei_op = pool.get('mm.production.order.ops')._buildEmptyItem()
						for k in filter(lambda x: x != 'id',op.keys()):
							ei_op[k] = op[k]
							
						item['ops'].append(ei_op)

		if item['bom'] and 'name' in item['bom'] and item['bom']['name']:
			b = pool.get('md.boms').select(cr,pool,uid,['fullname','product','partition',{'items':['product','quantity','uom']}],[('fullname','=',item['bom']['name'])],context)
			if len(b) > 0:
				item['product'] = b[0]['product']
				item['part'] = b[0]['partition']
				p = b[0]['items']
				for i in p:
					ei = pool.get('mm.production.order.items')._buildEmptyItem()
					ei['product'] = i['product']
					ei['quantity'] = i['quantity']
					ei['uom'] = i['uom']
					item['items'].append(ei)


	def _on_change_bom(self,cr,pool,uid,item,context={}):		
		if item['bom'] and 'name' in item['bom'] and item['bom']['name']:
			b = pool.get('md.boms').select(cr,pool,uid,['fullname','product','partition',{'items':['product','quantity','uom']}],[('fullname','=',item['bom']['name'])],context)
			if len(b) > 0:
				item['product'] = b[0]['product']
				item['part'] = b[0]['partition']
				p = b[0]['items']
				for i in p:
					ei = pool.get('mm.production.order.items')._buildEmptyItem()
					ei['product'] = i['product']
					ei['quantity'] = i['quantity']
					ei['uom'] = i['uom']
					item['items'].append(ei)

mm_production_orders()

class mm_production_order_texts(Model):
	_name = 'mm.production.order.texts'
	_description = 'Production Order Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'order_id': fields.many2one(label='Order',obj='mm.production.orders'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='mm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

mm_production_order_texts()

class mm_production_order_roles(Model):
	_name = 'mm.production.order.roles'
	_description = 'Production Order Roles'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='mm.production.orders'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

mm_production_order_roles()

class mm_production_order_pricing(Model):
	_name = 'mm.production.order.pricing'
	_description = 'Production Order Pricing'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='mm.production.orders'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','mm')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='mm.pricing.group.levels'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

mm_production_order_pricing()

class mm_production_order_items(Model):
	_name = 'mm.production.order.items'
	_description = 'Production Order Items'
	_inherits = {'mm.common.model':{'_methods':['_on_change_product','_calculate_item']}}
	_columns = {
	'order_id': fields.many2one(obj = 'mm.production.orders',label = 'Production Order'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product',readonly=True),
	'quantity': fields.numeric(label='Quantity',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),priority=1,compute='_calculate_item'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000,
		'price': '0.00',
		'amount': '0.00',
	}

mm_production_order_items()

class mm_production_order_delivery_schedules(Model):
	_name = 'mm.production.order.schedules'
	_description = 'Production Order Schedule'
	_columns = {
	'order_id': fields.many2one(obj = 'mm.production.orders',label = 'Order'),
	'part': fields.numeric(label='Part',size=(11,3),required=True,check='part > 0.000'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'part': 1.000
	}

mm_production_order_delivery_schedules()

class mm_production_order_ops(Model):
	_name = 'mm.production.order.ops'
	_description = 'Operations of production order'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'order_id': fields.many2one(label='Order',obj='mm.production.orders'),
	'prev':  fields.many2one(label='Prev',obj='mm.map.ops',domain=[('usage','in',('d','a'))]),
	'op':  fields.many2one(label='Operation',obj='mm.map.ops',domain=[('usage','in',('d','a'))],required=True),
	'next': fields.many2one(label='Next',obj='mm.map.ops',domain=[('usage','in',('d','a'))]),
	'workcenter': fields.many2one(label='Workcenter',obj='mm.workcenters',required=True),
	'duration': fields.numeric(label='Duration',size=(11,3),required=True),
	'uod': fields.many2one(label='Unit of duration',obj='md.uom',domain=[('quantity_id','=','Time')],required=True),
	'per_cicle': fields.boolean(label='Per Cicle'),
	'note': fields.text(label = 'Note')
	}

mm_production_order_ops()

# Technologic
class mm_technologic_orders(Model):
	_name = 'mm.technologic.orders'
	_description = 'Technologic Order'
	_inherits = {'mm.common.model':{'_methods':['_calculate_amount_costs','_calculate_parts']}}
	_date = 'doto'
	_columns = {
	'otype': fields.many2one(label='Type',obj='mm.technologic.order.types',on_change='_on_change_otype', required = True),
	'name': fields.varchar(label = 'Name'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'fullname': fields.composite(label='Full Name', cols = ['company','otype','name'], translate = True,required = True, compute = '_compute_composite'),
	'map': fields.many2one(label='Map',obj= 'mm.technologic.maps',on_change='_on_change_map'),
	'bob': fields.many2one(label='BoB',obj='md.bobs',on_change='_on_change_bob'),
	'part': fields.numeric(label='Production Part',size=(11,3), readonly=True),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'category_id': fields.many2one(label='Category',obj='mm.technologic.order.category'),
	'origin': fields.varchar(label = 'Origin'),
	'doto': fields.date(label='Date Of Technologic Order',required=True),
	'from_date': fields.date(label='Start Date Of Technologic Order',required=True),
	'to_date': fields.date(label='End Date Of Technologic Order',required=True),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'parts': fields.numeric(label='Parts',size=(11,3),compute='_calculate_parts'),
	'oamount': fields.numeric(label='Output Amount',size=(15,2),compute='_calculate_oamount_costs'),
	'iamount': fields.numeric(label='Input Amount',size=(15,2),compute='_calculate_iamount_costs'),
	'schedules': fields.one2many(label='Schedule',obj='mm.technologic.order.schedules',rel='order_id'),
	'ops': fields.one2many(label='Ops',obj='mm.technologic.order.ops',rel='order_id'),
	'ibobs': fields.one2many(label='InBoB',obj='mm.technologic.order.item.ibob',rel='order_id'),
	'obobs': fields.one2many(label='OutBoB',obj='mm.technologic.order.item.obob',rel='order_id'),
	'roles': fields.one2many(label='Roles',obj='mm.technologic.order.roles',rel='order_id'),
	'pricing': fields.one2many(label='Pricing',obj='mm.technologic.order.pricing',rel='order_id'),
	'texts': fields.one2many(label='Texts',obj='mm.technologic.order.texts',rel='order_id'),
	'note': fields.text(label='Note')}

	def _on_change_otype(self,cr,pool,uid,item,context={}):		
		roles = pool.get('mm.technologic.order.type.roles').select(cr,pool,uid,['role_id'],[('type_id','=',item['otype']['name'])],context)
		for role in roles:
			item_role = pool.get('mm.technologic.order.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)
		
		types = pool.get('mm.technologic.order.types').select(cr,pool,uid,['htschema'],[('name','=',item['otype']['name'])],context)	
		texts1 = pool.get('mm.schema.texts').select(cr,pool,uid,['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = pool.get('mm.technologic.order.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

	def _on_change_map(self,cr,pool,uid,item,context={}):
		if  item['map'] and 'name' in item['map'] and item['map']['name']:
			m = pool.get('mm.technologic.maps').select(cr,pool,uid,['fullname','bob',{'ops':['prev','op','next','workcenter','duration','uod','per_cicle','note']}],[('fullname','=',item['map']['name'])],context)		
			if len(m) > 0:
				if m[0]['bob']:
					item['bob'] = m[0]['bob']
				if len(m[0]['ops']) > 0:
					for op in m[0]['ops']:
						ei_op = pool.get('mm.technologic.order.ops')._buildEmptyItem()
						for k in filter(lambda x: x != 'id',op.keys()):
							ei_op[k] = op[k]
						
						item['ops'].append(ei_op)

		if item['bob'] and 'name' in item['bob'] and item['bob']['name']:
			b = pool.get('md.bobs').select(cr,pool,uid,['fullname','partition',{'input_items':['product','quantity','uom']},{'output_items':['product','quantity','uom']}],[('fullname','=',item['bob']['name'])],context)
			if len(b) > 0:
				item['part'] = b[0]['partition']
				p = b[0]['input_items']
				for i in p:
					ei = pool.get('mm.technologic.order.item.ibob')._buildEmptyItem()
					ei['product'] = i['product']
					ei['quantity'] = i['quantity']
					ei['uom'] = i['uom']
					item['ibobs'].append(ei)
					
				p = b[0]['output_items']
				for i in p:
					ei = pool.get('mm.technologic.order.item.obob')._buildEmptyItem()
					ei['product'] = i['product']
					ei['quantity'] = i['quantity']
					ei['uom'] = i['uom']
					item['obobs'].append(ei)



	def _on_change_bob(self,cr,pool,uid,item,context={}):		
		if item['bob'] and 'name' in item['bob'] and item['bob']['name']:
			b = pool.get('md.bobs').select(cr,pool,uid,['fullname','partition',{'input_items':['product','quantity','uom']},{'output_items':['product','quantity','uom']}],[('fullname','=',item['bob']['name'])],context)
			if len(b) > 0:
				item['part'] = b[0]['partition']
				p = b[0]['input_items']
				for i in p:
					ei = pool.get('mm.technologic.order.item.ibob')._buildEmptyItem()
					ei['product'] = i['product']
					ei['quantity'] = i['quantity']
					ei['uom'] = i['uom']
					item['ibobs'].append(ei)
					
				p = b[0]['output_items']
				for i in p:
					ei = pool.get('mm.technologic.order.item.obob')._buildEmptyItem()
					ei['product'] = i['product']
					ei['quantity'] = i['quantity']
					ei['uom'] = i['uom']
					item['obobs'].append(ei)

	def _calculate_oamount_costs(self,cr,pool,uid,item,context={}):		
		if 'obobs' in item and item['obobs']:
			item['oamount'] = None
			for r in item['obobs']:
				if item['oamount'] is None:
					item['oamount'] = r['amount']
				else:
					item['oamount'] += r['amount']

	def _calculate_iamount_costs(self,cr,pool,uid,item,context={}):		
		if 'ibobs' in item and item['ibobs']:
			item['iamount'] = None
			for r in item['ibobs']:
				if item['iamount'] is None:
					item['iamount'] = r['amount']
				else:
					item['iamount'] += r['amount']


	_default = {
		'state':'draft'
	}

mm_technologic_orders()

class mm_technologic_order_delivery_schedules(Model):
	_name = 'mm.technologic.order.schedules'
	_description = 'Technologic Order Delivery Schedule'
	_columns = {
	'order_id': fields.many2one(obj = 'mm.technologic.orders',label = 'Schedule'),
	'part': fields.numeric(label='Part',size=(11,3),required=True,check='part > 0.000'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'part': 1.000
	}

mm_technologic_order_delivery_schedules()

class mm_technologic_order_ops(Model):
	_name = 'mm.technologic.order.ops'
	_description = 'Operations of technologic order'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'order_id': fields.many2one(label='Order',obj='mm.technologic.orders'),
	'prev':  fields.many2one(label='Prev',obj='mm.map.ops',domain=[('usage','in',('d','a'))]),
	'op':  fields.many2one(label='Operation',obj='mm.map.ops',domain=[('usage','in',('d','a'))],required=True),
	'next': fields.many2one(label='Next',obj='mm.map.ops',domain=[('usage','in',('d','a'))]),
	'workcenter': fields.many2one(label='Workcenter',obj='mm.workcenters',required=True),
	'duration': fields.numeric(label='Duration',size=(11,3),required=True),
	'uod': fields.many2one(label='Unit of duration',obj='md.uom',domain=[('quantity_id','=','Time')],required=True),
	'per_cicle': fields.boolean(label='Per Cicle'),
	'note': fields.text(label = 'Note')
	}

mm_technologic_order_ops()

class mm_technologic_order_texts(Model):
	_name = 'mm.technologic.order.texts'
	_description = 'Technologic Order Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'order_id': fields.many2one(label='Order',obj='mm.technologic.orders'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='mm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

mm_technologic_order_texts()

class mm_technologic_order_roles(Model):
	_name = 'mm.technologic.order.roles'
	_description = 'Technologic Order Roles'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='mm.technologic.orders'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

mm_technologic_order_roles()

class mm_technologic_order_pricing(Model):
	_name = 'mm.technologic.order.pricing'
	_description = 'Technologic Order Pricing'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='mm.technologic.orders'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','mm')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='mm.pricing.group.levels'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

mm_technologic_order_pricing()

class mm_technologic_order_item_ibob(Model):
	_name = 'mm.technologic.order.item.ibob'
	_description = 'Technologic Order Items InBoB'
	_inherits = {'mm.common.model':{'_methods':['_on_change_product','_calculate_item']}}
	_columns = {
	'order_id': fields.many2one(obj = 'mm.technologic.orders',label = 'Item'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_item'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000,
		'price': '0.00',
		'amount': '0.00',

	}

mm_technologic_order_item_ibob()

class mm_technologic_order_item_obob(Model):
	_name = 'mm.technologic.order.item.obob'
	_description = 'Technologic Order Items OutBoB'
	_inherits = {'mm.common.model':{'_methods':['_on_change_product','_calculate_item']}}
	_columns = {
	'order_id': fields.many2one(obj = 'mm.technologic.orders',label = 'Item'),
	'product': fields.many2one(label='Product',obj='md.product',on_change = '_on_change_product'),
	'quantity': fields.numeric(label='Quantity',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_item'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000,
		'price': '0.00',
		'amount': '0.00',
	}

mm_technologic_order_item_obob()

# Disassebly
class mm_disassembly_orders(Model):
	_name = 'mm.disassembly.orders'
	_description = 'Disassembly Order'
	_inherits = {'mm.common.model':{'_methods':['_calculate_amount_costs','_calculate_parts']}}
	_date = 'dodo'
	_columns = {
	'otype': fields.many2one(label='Type',obj='mm.disassembly.order.types',on_change='_on_change_otype', required = True),
	'name': fields.varchar(label = 'Name'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'fullname': fields.composite(label='Full Name', cols = ['company','otype','name'], translate = True,required = True, compute = '_compute_composite'),
	'map': fields.many2one(label='Map',obj= 'mm.disassembly.maps',on_change='_on_change_map'),
	'mob': fields.many2one(label='MoB',obj='md.mobs',priority=1,on_change='_on_change_mob'),
	'product': fields.many2one(label='Disassembly Product',obj='md.product',readonly=True),
	'part': fields.numeric(label='Disassembly Part',size=(11,3), readonly=True),
	'category_id': fields.many2one(label='Category',obj='mm.disassembly.order.category'),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'origin': fields.varchar(label = 'Origin'),
	'dodo': fields.date(label='Date Of Disassembly Order',required=True),
	'from_date': fields.date(label='Start Date Of Disassembly Order',required=True),
	'to_date': fields.date(label='End Date Of Disassembly Order',required=True),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'parts': fields.numeric(label='Parts',size=(15,2),compute='_calculate_parts'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'schedules': fields.one2many(label='Schedule',obj='mm.disassembly.order.schedules',rel='order_id'),
	'ops': fields.one2many(label='Ops',obj='mm.disassembly.order.ops',rel='order_id'),
	'items': fields.one2many(label='Items',obj='mm.disassembly.order.items',rel='order_id'),
	'roles': fields.one2many(label='Roles',obj='mm.disassembly.order.roles',rel='order_id'),
	'pricing': fields.one2many(label='Pricing',obj='mm.disassembly.order.pricing',rel='order_id'),
	'texts': fields.one2many(label='Texts',obj='mm.disassembly.order.texts',rel='order_id'),
	'note': fields.text('Note')}

	def _on_change_otype(self,cr,pool,uid,item,context={}):		
		roles = pool.get('mm.disassembly.order.type.roles').select(cr,pool,uid,['role_id'],[('type_id','=',item['otype']['name'])],context)
		for role in roles:
			item_role = pool.get('mm.disassembly.order.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)
		
		types = pool.get('mm.disassembly.order.types').select(cr,pool,uid,['htschema'],[('name','=',item['otype']['name'])],context)	
		texts1 = pool.get('mm.schema.texts').select(cr,pool,uid,['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = pool.get('mm.disassembly.order.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

	def _on_change_map(self,cr,pool,uid,item,context={}):
		if  item['map'] and 'name' in item['map'] and item['map']['name']:
			m = pool.get('mm.disassembly.maps').select(cr,pool,uid,['fullname','mob',{'ops':['prev','op','next','workcenter','duration','uod','per_cicle','note']}],[('fullname','=',item['map']['name'])],context)		
			if len(m) > 0:
				if m[0]['mob']:
					item['mob'] = m[0]['mob']
				if len(m[0]['ops']) > 0:
					for op in m[0]['ops']:
						ei_op = pool.get('mm.disassembly.order.ops')._buildEmptyItem()
						for k in filter(lambda x: x != 'id',op.keys()):
							ei_op[k] = op[k]
						
						item['ops'].append(ei_op)
									
		# if item['mob'] and 'name' in item['mob'] and item['mob']['name']:
			# b = pool.get('md.mobs').select(cr,pool,uid,['fullname','product','partition',{'items':['product','quantity','uom']}],[('fullname','=',item['mob']['name'])],context)
			# if len(b) > 0:
				# item['product'] = b[0]['product']
				# item['part'] = b[0]['partition']
				# p = b[0]['items']

				# for i in p:
					# ei = pool.get('mm.disassembly.order.items')._buildEmptyItem()
					# ei['product'] = i['product']
					# ei['quantity'] = i['quantity']
					# ei['uom'] = i['uom']
					# item['items'].append(ei)


	def _on_change_mob(self,cr,pool,uid,item,context={}):		
		if item['mob'] and 'name' in item['mob'] and item['mob']['name']:
			b = pool.get('md.mobs').select(cr,pool,uid,['fullname','product','partition',{'items':['product','quantity','uom']}],[('fullname','=',item['mob']['name'])],context)
			if len(b) > 0:
				item['product'] = b[0]['product']
				item['part'] = b[0]['partition']
				p = b[0]['items']

				for i in p:
					ei = pool.get('mm.disassembly.order.items')._buildEmptyItem()
					ei['product'] = i['product']
					ei['quantity'] = i['quantity']
					ei['uom'] = i['uom']
					item['items'].append(ei)

	_default = {
		'state':'draft'
	}

mm_disassembly_orders()

class mm_disassembly_order_texts(Model):
	_name = 'mm.disassembly.order.texts'
	_description = 'Disassembly Order Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'order_id': fields.many2one(label='Order',obj='mm.disassembly.orders'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='mm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

mm_disassembly_order_texts()

class mm_disassembly_order_roles(Model):
	_name = 'mm.disassembly.order.roles'
	_description = 'Disassembly Order Roles'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='mm.disassembly.orders'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

mm_disassembly_order_roles()

class mm_disassembly_order_pricing(Model):
	_name = 'mm.disassembly.order.pricing'
	_description = 'Disassembly Order Pricing'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='mm.disassembly.orders'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','mm')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='mm.pricing.group.levels'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

mm_disassembly_order_pricing()

class mm_disassembly_order_items(Model):
	_name = 'mm.disassembly.order.items'
	_description = 'Disassembly Order Items'
	_inherits = {'mm.common.model':{'_methods':['_on_change_product','_calculate_item']}}
	_columns = {
	'order_id': fields.many2one(obj = 'mm.disassembly.orders',label = 'Order'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),priority=1,compute='_calculate_item'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000,
		'price': '0.00',
		'amount': '0.00',
	}


mm_disassembly_order_items()

class mm_disassembly_order_delivery_schedules(Model):
	_name = 'mm.disassembly.order.schedules'
	_description = 'Disassembly Order Delivery Schedule'
	_columns = {
	'order_id': fields.many2one(obj = 'mm.disassembly.orders',label = 'Order'),
	'part': fields.numeric(label='Part',size=(11,3),required=True,check='part > 0.000'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'part': 1.000
	}

mm_disassembly_order_delivery_schedules()

class mm_disassembly_order_ops(Model):
	_name = 'mm.disassembly.order.ops'
	_description = 'Operations of disassembly order'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'order_id': fields.many2one(label='Order',obj='mm.disassembly.orders'),
	'prev':  fields.many2one(label='Prev',obj='mm.map.ops',domain=[('usage','in',('d','a'))]),
	'op':  fields.many2one(label='Operation',obj='mm.map.ops',domain=[('usage','in',('d','a'))],required=True),
	'next': fields.many2one(label='Next',obj='mm.map.ops',domain=[('usage','in',('d','a'))]),
	'workcenter': fields.many2one(label='Workcenter',obj='mm.workcenters',required=True),
	'duration': fields.numeric(label='Duration',size=(11,3),required=True),
	'uod': fields.many2one(label='Unit of duration',obj='md.uom',domain=[('quantity_id','=','Time')],required=True),
	'per_cicle': fields.boolean(label='Per Cicle'),
	'note': fields.text(label = 'Note')
	}

mm_disassembly_order_ops()


class md_mm_product(Model):
	_name = 'md.mm.product'
	_description = 'Production Of Product'
	_columns = {
	'product_id': fields.many2one(label='Product',obj='md.product'),
	'uom': fields.many2one(label="Unit Of Measure",obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'note': fields.text(label = 'Note'),
	}

md_mm_product()

class md_mm_product_inherit(ModelInherit):
	_name = 'md.mm.product.inherit'
	_description = 'Inherit For Production Product'
	_inherit = {'md.product':{'_columns':['production']},'md.boms':{'_columns':['usage']},'md.boms':{'_columns':['usage']},'md.mobs':{'_columns':['usage']},'md.bobs':{'_columns':['usage']},'seq.conditions':{'_columns':['usage']},'seq.access.schemas':{'_columns':['usage']},'seq.access':{'_columns':['usage']}
	}
	_columns = {
		'production': fields.one2many(label='Production',obj='md.mm.product',rel='product_id'),
		'usage': fields.iProperty(selections=[('mm','Production')])
	}
	
md_mm_product_inherit()
