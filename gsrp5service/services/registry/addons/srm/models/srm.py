from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

from decimal import Decimal

from datetime import datetime
from datetime import timedelta

# Deadlines
class srm_deadlines(Model):
	_name = 'srm.deadlines'
	_description = 'General SRM Deadlines'
	_columns = {
	'name': fields.varchar(label = 'Name'),
	'note': fields.text('Note')}

srm_deadlines()

# SRM Demand
# Types & Roles
class srm_demand_types(Model):
	_name = 'srm.demand.types'
	_description = 'Types SRM Demand'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='srm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='srm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='srm.demand.type.roles',rel='type_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.demand.type.deadlines',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

srm_demand_types()

class srm_demand_type_roles(Model):
	_name = 'srm.demand.type.roles'
	_description = 'Role SRM Demand Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.demand.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_demand_type_roles()

class srm_demand_type_deadlines(Model):
	_name = 'srm.demand.type.deadlines'
	_description = 'Deadlines SRM Demand Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.demand.types'),
	'sequence': fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Deadline',obj='srm.deadlines'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_demand_type_deadlines()

class srm_demand_type_plates(Model):
	_name = 'srm.demand.type.plates'
	_description = 'SRM Demand Plates'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.demand.types'),
	'seq': fields.integer(label='Sequence',required=True),
	'plate': fields.many2one(label = 'Plate',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_demand_type_plates()


class srm_demand_type_items(Model):
	_name = 'srm.demand.type.items'
	_description = 'Type of SRM Deamnd Items'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.demand.types'),
	'gti_id': fields.many2one(label = 'GTI',obj='md.gtis'),
	'itype_id': fields.many2one(label = 'Type Of Items',obj='md.type.items',domain=[('usage','=','p'),'|',('usage','=','a')]),
	'note': fields.text(label = 'Note')
	}

srm_demand_type_items()



# Types & Roles
#
class srm_demands(Model):
	_name = 'srm.demands'
	_description = 'General SRM Demand'
	_inherits = {'srm.common':{'_methods':['copy_into','copy_from','_compute_fullname'],'_actions':['merge']},'common.model':{'_methods':['_calculate_amount_costs']}}
	_rec_name = 'fullname'
	_date = 'dod'
	_columns = {
	'dtype': fields.many2one(label='Type',obj='srm.demand.types',on_change='_on_change_dtype'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'name': fields.varchar(label = 'Name'),
	'fullname': fields.composite(label='Full Name',cols=['dtype','company','name'],translate = True,required = True, compute = '_compute_composite'),
	'market': fields.many2one(label='Market',obj='srm.markets'),
	'team': fields.many2one(label='Team',obj='srm.teams'),
	'category_id': fields.many2one(label='Category',obj='srm.demand.category'),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'origin': fields.varchar(label = 'Origin'),
	'dod': fields.date(label='Date Of Demand',required=True),
	'from_date': fields.date(label='From Date Of Demand',required=True),
	'to_date': fields.date(label='To Date Of Demand',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',on_delete='n',on_update='n',domain=[('issuplier',)]),
	'route_id': fields.many2one(label='Route',obj='srm.routes',on_delete='n',on_update='n'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'bom': fields.many2one(label='BoM',obj='md.boms',domain=[('usage','=','srm'),'|',('usage','=','all')],on_change='_on_change_bom'),
	'items': fields.one2many(label='Items',obj='srm.demand.items',rel='demand_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.demand.pricing',rel='demand_id'),
	'roles': fields.one2many(label='Roles',obj='srm.demand.roles',rel='demand_id'),
	'texts': fields.one2many(label='Texts',obj='srm.demand.texts',rel='demand_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.demand.deadlines',rel='demand_id'),
	'plates': fields.one2many(label='Plates',obj='srm.demand.output.plates',rel='demand_id'),
	'payments': fields.one2many(label='Payments',obj='srm.demand.payment.schedules',rel='demand_id'),
	'note': fields.text('Note')}
	
	def _on_change_dtype(self,cr,pool,uid,item,context={}):		
		#import web_pdb
		#web_pdb.set_trace()
		roles = pool.get('srm.demand.type.roles').select(cr,pool,uid,['role_id'],[('type_id','=',item['dtype']['name'])],context)
		for role in roles:
			item_role = pool.get('srm.demand.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)

		deadlines = pool.get('srm.demand.type.deadlines').select(cr,pool,uid,['sequence','deadline_id','required'],[('type_id','=',item['dtype']['name'])],context)
		for deadline in deadlines:
			item_deadline = pool.get('srm.demand.deadlines')._buildEmptyItem()
			item_deadline['sequence'] = deadline['sequence']
			item_deadline['deadline_id'] = deadline['deadline_id']
			item_deadline['required'] = deadline['required']
			item['deadlines'].append(item_deadline)
	
		types = pool.get('srm.demand.types').select(cr,pool,uid,['htschema'],[('name','=',item['dtype']['name'])],context)	
		texts1 = pool.get('srm.schema.texts').select(cr,pool,uid,['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = pool.get('srm.demand.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

	def _on_change_bom(self,cr,pool,uid,item,context={}):		
		if item['bom'] and 'name' in item['bom'] and item['bom']['name']:
			p = pool.get('md.bom.input.items').select(cr,pool,uid,['product','quantity','uom'],[('bom_id','=',item['bom']['name'])],context)
			for i in p:
				ei = pool.get('purchase.order.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.now().astimezone()+timedelta(3)
				item_items = pool.get('purchase.order.items')._buildEmptyItem()
				item_items['delivery_schedules'].append(ei)
				for f in ('product','uom'):
					item_items[f] = i[f]
				item_items['price'] = 0.00
				item['items'].append(item_items)

		return None

srm_demands()

class srm_demand_texts(Model):
	_name = 'srm.demand.texts'
	_description = 'SRM Demand Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'demand_id': fields.many2one(label='Demand',obj='srm.demands'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_demand_texts()


class srm_demand_roles(Model):
	_name = 'srm.demand.roles'
	_description = 'SRM Demand Roles'
	_columns = {
	'demand_id': fields.many2one(label = 'Demand',obj='srm.demands'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_demand_roles()

class srm_demand_output_plates(Model):
	_name = 'srm.demand.output.plates'
	_description = 'SRM Demand Output Plates'
	_columns = {
	'demand_id': fields.many2one(label = 'Demand',obj='srm.demands'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}


class srm_demand_deadlines(Model):
	_name = 'srm.demand.deadlines'
	_description = 'General SRM Demand Deadlines'
	_order_by = 'start_date asc'
	_columns = {
	'demand_id': fields.many2one(label = 'Demand',obj='srm.demands',on_delete='c',on_update='c'),
	'sequence':fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Type',obj='srm.deadlines',on_delete='n',on_update='n'),
	'start_date': fields.datetime(label='Start',required=True),
	'end_date': fields.datetime(label='End',required=True),
	'required': fields.boolean(label='Required'),
	'note': fields.text('Note')}

srm_demand_deadlines()

class srm_demand_pricing(Model):
	_name = 'srm.demand.pricing'
	_description = 'SRM Demand Pricing'
	_columns = {
	'demand_id': fields.many2one(label = 'Demand',obj='srm.demands'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','srm')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_demand_pricing()

class srm_demand_payment_schedules(Model):
	_name = 'srm.demand.payment.schedules'
	_description = 'SRM Demand Payment Schedules'
	_columns = {
	'demand_id': fields.many2one(label = 'Demand',obj='srm.demands'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_demand_payment_schedules()

class srm_demand_items(Model):
	_name = 'srm.demand.items'
	_description = 'General SRM Demant Item'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'demand_id': fields.many2one(obj = 'srm.demands',label = 'Demand',on_delete='c',on_update='c'),
	'product': fields.many2one(label='Product',obj='md.product',on_delete='n',on_update='n',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='VAT Code',obj='md.vat.code',on_delete='n',on_update='n',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'currency_id': fields.many2one(label='Currency',obj='md.currency',on_delete='n',on_update='n'),
	'delivery_schedules': fields.one2many(label='Delivery Schedules',obj='srm.demand.item.delivery.schedules',rel='item_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.demand.pricing.items',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='srm.demand.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='srm.demand.item.texts',rel='item_id'),
	'plates': fields.one2many(label='Plates',obj='srm.demand.item.output.plates',rel='item_id'),
	'payments': fields.one2many(label='Payments',obj='srm.demand.item.payment.schedules',rel='item_id'),
	'note': fields.text('Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.srm.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
			if len(p) > 0:
				if item['vat_code'] != p[0]['vat']:
					item['vat_code'] = p[0]['vat']				
				for f in ('uom','price','currency','unit','uop'):
					if item[f] != p[0][f]:
						item[f] = p[0][f]

		return None

	_default = {
		'quantity': 1,
		'unit': 1
	}

srm_demand_items()

class srm_demand_pricing_items(Model):
	_name = 'srm.demand.pricing.items'
	_description = 'Demand Item Pricing'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.demand.items'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','p')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'cop': fields.many2one(label='Currency Of Price',obj='md.currency',required=True),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_demand_pricing_items()


class srm_demand_item_texts(Model):
	_name = 'srm.demand.item.texts'
	_description = 'SRM Demand Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='srm.demand.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_demand_item_texts()

class srm_demand_item_roles(Model):
	_name = 'srm.demand.item.roles'
	_description = 'SRM Demand Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.demand.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_demand_item_roles()

class srm_demand_item_delivery_schedules(Model):
	_name = 'srm.demand.item.delivery.schedules'
	_description = 'General SRM Demand Delivery Schedules'
	_date = "schedule"
	_columns = {
	'item_id': fields.many2one(obj = 'srm.demand.items',label = 'Item',on_delete='c',on_update='c'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom',on_delete='n',on_update='n'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')}

srm_demand_item_delivery_schedules()

class srm_demand_item_output_plates(Model):
	_name = 'srm.demand.item.output.plates'
	_description = 'Demand Item Output Plates'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.demand.items'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

srm_demand_item_output_plates()

class srm_demand_item_payment_schedules(Model):
	_name = 'srm.demand.item.payment.schedules'
	_description = 'Demand Item Payment Schedules'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.demand.items'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_demand_item_payment_schedules()

# SRM Part
# Types & Roles
class srm_part_types(Model):
	_name = 'srm.part.types'
	_description = 'Types SRM Part'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='srm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='srm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='srm.part.type.roles',rel='type_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.part.type.deadlines',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

srm_part_types()

class srm_part_type_roles(Model):
	_name = 'srm.part.type.roles'
	_description = 'Role SRM Part Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.part.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_part_type_roles()

class srm_part_type_deadlines(Model):
	_name = 'srm.part.type.deadlines'
	_description = 'Deadlines SRM Part Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.part.types'),
	'sequence': fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Deadline',obj='srm.deadlines'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_part_type_deadlines()

class srm_part_type_plates(Model):
	_name = 'srm.part.type.plates'
	_description = 'SRM Part Plates'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.part.types'),
	'seq': fields.integer(label='Sequence',required=True),
	'plate': fields.many2one(label = 'Plate',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_part_type_plates()


class srm_part_type_items(Model):
	_name = 'srm.part.type.items'
	_description = 'Type of SRM Part Items'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.part.types'),
	'gti_id': fields.many2one(label = 'GTI',obj='md.gtis'),
	'itype_id': fields.many2one(label = 'Type Of Items',obj='md.type.items',domain=[('usage','=','p'),'|',('usage','=','a')]),
	'note': fields.text(label = 'Note')
	}

srm_part_type_items()



# Types & Roles
#
class srm_parts(Model):
	_name = 'srm.parts'
	_description = 'General SRM Part'
	_inherits = {'srm.common':{'_methods':['copy_into','copy_from','_compute_fullname'],'_actions':['merge']},'common.model':{'_methods':['_calculate_amount_costs']}}
	_rec_name = 'fullname'
	_date = 'dop'
	_columns = {
	'ptype': fields.many2one(label='Type',obj='srm.part.types',on_change='_on_change_ptype'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'name': fields.varchar(label = 'Name'),
	'fullname': fields.composite(label='Full Name',cols=['ptype','company','name'],translate = True,required = True, compute = '_compute_composite'),
	'market': fields.many2one(label='Market',obj='srm.markets'),
	'team': fields.many2one(label='Team',obj='srm.teams'),
	'category_id': fields.many2one(label='Category',obj='srm.part.category'),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'origin': fields.varchar(label = 'Origin'),
	'dop': fields.date(label='Date Of Part',required=True),
	'from_date': fields.date(label='From Date Of Part',required=True),
	'to_date': fields.date(label='To Date Of Part',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',on_delete='n',on_update='n',domain=[('issuplier',)]),
	'route_id': fields.many2one(label='Route',obj='srm.routes',on_delete='n',on_update='n'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'bom': fields.many2one(label='BoM',obj='md.boms',domain=[('usage','=','srm'),'|',('usage','=','all')],on_change='_on_change_bom'),
	'items': fields.one2many(label='Items',obj='srm.part.items',rel='part_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.part.pricing',rel='part_id'),
	'roles': fields.one2many(label='Roles',obj='srm.part.roles',rel='part_id'),
	'texts': fields.one2many(label='Texts',obj='srm.part.texts',rel='part_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.part.deadlines',rel='part_id'),
	'plates': fields.one2many(label='Plates',obj='srm.part.output.plates',rel='part_id'),
	'payments': fields.one2many(label='Payments',obj='srm.part.payment.schedules',rel='part_id'),
	'note': fields.text('Note')}
	
	def _on_change_ptype(self,cr,pool,uid,item,context={}):		
		roles = pool.get('srm.part.type.roles').select(cr,pool,uid,['role_id'],[('type_id','=',item['ptype']['name'])],context)
		for role in roles:
			item_role = pool.get('srm.part.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)

		deadlines = pool.get('srm.part.type.deadlines').select(cr,pool,uid,['sequence','deadline_id','required'],[('type_id','=',item['ptype']['name'])],context)
		for deadline in deadlines:
			item_deadline = pool.get('srm.part.deadlines')._buildEmptyItem()
			item_deadline['sequence'] = deadline['sequence']
			item_deadline['deadline_id'] = deadline['deadline_id']
			item_deadline['required'] = deadline['required']
			item['deadlines'].append(item_deadline)
		
		types = pool.get('srm.part.types').select(cr,pool,uid,['htschema'],[('name','=',item['dtype']['name'])],context)	
		texts1 = pool.get('srm.schema.texts').select(cr,pool,uid,['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = pool.get('srm.part.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

	def _on_change_bom(self,cr,pool,uid,item,context={}):		
		if item['bom'] and 'name' in item['bom'] and item['bom']['name']:
			p = pool.get('md.bom.input.items').select(cr,pool,uid,['product','quantity','uom'],[('bom_id','=',item['bom']['name'])],context)
			for i in p:
				ei = pool.get('purchase.order.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.now().astimezone()+timedelta(3)
				item_items = pool.get('purchase.order.items')._buildEmptyItem()
				item_items['delivery_schedules'].append(ei)
				for f in ('product','uom'):
					item_items[f] = i[f]
				item_items['price'] = 0.00
				item['items'].append(item_items)

		return None

srm_parts()

class srm_part_texts(Model):
	_name = 'srm.part.texts'
	_description = 'SRM Part Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'part_id': fields.many2one(label='Part',obj='srm.parts'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_part_texts()


class srm_part_roles(Model):
	_name = 'srm.part.roles'
	_description = 'SRM Part Roles'
	_columns = {
	'part_id': fields.many2one(label = 'Part',obj='srm.parts'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_part_roles()

class srm_part_output_plates(Model):
	_name = 'srm.part.output.plates'
	_description = 'SRM Part Output Plates'
	_columns = {
	'part_id': fields.many2one(label = 'Part',obj='srm.parts'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

class srm_part_deadlines(Model):
	_name = 'srm.part.deadlines'
	_description = 'General SRM Part Deadlines'
	_order_by = 'start_date asc'
	_columns = {
	'part_id': fields.many2one(label = 'Part',obj='srm.parts',on_delete='c',on_update='c'),
	'sequence':fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Type',obj='srm.deadlines',on_delete='n',on_update='n'),
	'start_date': fields.datetime(label='Start',required=True),
	'end_date': fields.datetime(label='End',required=True),
	'required': fields.boolean(label='Required'),
	'note': fields.text('Note')}

srm_part_deadlines()

class srm_part_pricing(Model):
	_name = 'srm.part.pricing'
	_description = 'SRM Part Pricing'
	_columns = {
	'part_id': fields.many2one(label = 'Part',obj='srm.parts'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','srm')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_part_pricing()

class srm_part_payment_schedules(Model):
	_name = 'srm.part.payment.schedules'
	_description = 'SRM Part Payment Schedules'
	_columns = {
	'part_id': fields.many2one(label = 'Part',obj='srm.parts'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_part_payment_schedules()

class srm_part_items(Model):
	_name = 'srm.part.items'
	_description = 'General SRM Part Item'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'part_id': fields.many2one(obj = 'srm.parts',label = 'Part',on_delete='c',on_update='c'),
	'product': fields.many2one(label='Product',obj='md.product',on_delete='n',on_update='n',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='VAT Code',obj='md.vat.code',on_delete='n',on_update='n',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'currency_id': fields.many2one(label='Currency',obj='md.currency',on_delete='n',on_update='n'),
	'delivery_schedules': fields.one2many(label='Delivery Schedules',obj='srm.part.item.delivery.schedules',rel='item_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.part.pricing.items',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='srm.part.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='srm.part.item.texts',rel='item_id'),
	'plates': fields.one2many(label='Plates',obj='srm.part.item.output.plates',rel='item_id'),
	'payments': fields.one2many(label='Payments',obj='srm.part.item.payment.schedules',rel='item_id'),
	'note': fields.text('Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.srm.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
			if len(p) > 0:
				if item['vat_code'] != p[0]['vat']:
					item['vat_code'] = p[0]['vat']				
				for f in ('uom','price','currency','unit','uop'):
					if item[f] != p[0][f]:
						item[f] = p[0][f]

		return None

	_default = {
		'quantity': 1,
		'unit': 1
	}

srm_part_items()

class srm_part_pricing_items(Model):
	_name = 'srm.part.pricing.items'
	_description = 'Part Item Pricing'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.part.items'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','p')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'cop': fields.many2one(label='Currency Of Price',obj='md.currency',required=True),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_part_pricing_items()


class srm_part_item_texts(Model):
	_name = 'srm.part.item.texts'
	_description = 'SRM Part Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='srm.part.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_part_item_texts()

class srm_part_item_roles(Model):
	_name = 'srm.part.item.roles'
	_description = 'SRM Part Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.part.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_part_item_roles()

class srm_part_item_delivery_schedules(Model):
	_name = 'srm.part.item.delivery.schedules'
	_description = 'General SRM Part Delivery Schedules'
	_date = "schedule"
	_columns = {
	'item_id': fields.many2one(obj = 'srm.part.items',label = 'Item',on_delete='c',on_update='c'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom',on_delete='n',on_update='n'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')}

srm_part_item_delivery_schedules()

class srm_part_item_output_plates(Model):
	_name = 'srm.part.item.output.plates'
	_description = 'Part Item Output Plates'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.part.items'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

srm_part_item_output_plates()

class srm_part_item_payment_schedules(Model):
	_name = 'srm.part.item.payment.schedules'
	_description = 'Part Item Payment Schedules'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.part.items'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_part_item_payment_schedules()

# SRM Plan
# Types & Roles
class srm_plan_types(Model):
	_name = 'srm.plan.types'
	_description = 'Types SRM Plan'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='srm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='srm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='srm.plan.type.roles',rel='type_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.plan.type.deadlines',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

srm_plan_types()

class srm_plan_type_roles(Model):
	_name = 'srm.plan.type.roles'
	_description = 'Role SRM Plan Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.plan.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_plan_type_roles()

class srm_plan_type_deadlines(Model):
	_name = 'srm.plan.type.deadlines'
	_description = 'Deadlines SRM Plan Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.plan.types'),
	'sequence': fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Deadline',obj='srm.deadlines'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_plan_type_deadlines()

class srm_plan_type_plates(Model):
	_name = 'srm.plan.type.plates'
	_description = 'SRM Plan Plates'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.plan.types'),
	'seq': fields.integer(label='Sequence',required=True),
	'plate': fields.many2one(label = 'Plate',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_plan_type_plates()


class srm_plan_type_items(Model):
	_name = 'srm.plan.type.items'
	_description = 'Type of SRM Plan Items'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.plan.types'),
	'gti_id': fields.many2one(label = 'GTI',obj='md.gtis'),
	'itype_id': fields.many2one(label = 'Type Of Items',obj='md.type.items',domain=[('usage','=','p'),'|',('usage','=','a')]),
	'note': fields.text(label = 'Note')
	}

srm_plan_type_items()



# Types & Roles
#
class srm_plans(Model):
	_name = 'srm.plans'
	_description = 'General SRM Plan'
	_inherits = {'srm.common':{'_methods':['copy_into','copy_from','_compute_fullname'],'_actions':['merge']},'common.model':{'_methods':['_calculate_amount_costs']}}
	_rec_name = 'fullname'
	_date = 'dop'
	_columns = {
	'ptype': fields.many2one(label='Type',obj='srm.plan.types',on_change='_on_change_ptype'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'name': fields.varchar(label = 'Name'),
	'fullname': fields.composite(label='Full Name',cols=['ptype','company','name'],translate = True,required = True, compute = '_compute_composite'),
	'market': fields.many2one(label='Market',obj='srm.markets'),
	'team': fields.many2one(label='Team',obj='srm.teams'),
	'category_id': fields.many2one(label='Category',obj='srm.plan.category'),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'origin': fields.varchar(label = 'Origin'),
	'dop': fields.date(label='Date Of Plan',required=True),
	'from_date': fields.date(label='From Date Of Plan',required=True),
	'to_date': fields.date(label='To Date Of Plan',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',on_delete='n',on_update='n',domain=[('issuplier',)]),
	'route_id': fields.many2one(label='Route',obj='srm.routes',on_delete='n',on_update='n'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'bom': fields.many2one(label='BoM',obj='md.boms',domain=[('usage','=','srm'),'|',('usage','=','all')],on_change='_on_change_bom'),
	'items': fields.one2many(label='Items',obj='srm.plan.items',rel='plan_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.plan.pricing',rel='plan_id'),
	'roles': fields.one2many(label='Roles',obj='srm.plan.roles',rel='plan_id'),
	'texts': fields.one2many(label='Texts',obj='srm.plan.texts',rel='plan_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.plan.deadlines',rel='plan_id'),
	'plates': fields.one2many(label='Plates',obj='srm.plan.output.plates',rel='plan_id'),
	'payments': fields.one2many(label='Payments',obj='srm.plan.payment.schedules',rel='plan_id'),
	'note': fields.text('Note')}
	
	def _on_change_ptype(self,cr,pool,uid,item,context={}):		
		roles = pool.get('srm.plan.type.roles').select(cr,pool,uid,['role_id'],[('type_id','=',item['ptype']['name'])],context)
		for role in roles:
			item_role = pool.get('srm.plan.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)

		deadlines = pool.get('srm.plan.type.deadlines').select(cr,pool,uid,['sequence','deadline_id','required'],[('type_id','=',item['ptype']['name'])],context)
		for deadline in deadlines:
			item_deadline = pool.get('srm.plan.deadlines')._buildEmptyItem()
			item_deadline['sequence'] = deadline['sequence']
			item_deadline['deadline_id'] = deadline['deadline_id']
			item_deadline['required'] = deadline['required']
			item['deadlines'].append(item_deadline)
		
		types = pool.get('srm.plan.types').select(cr,pool,uid,['htschema'],[('name','=',item['dtype']['name'])],context)	
		texts1 = pool.get('srm.schema.texts').select(cr,pool,uid,['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = pool.get('srm.plan.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

	def _on_change_bom(self,cr,pool,uid,item,context={}):		
		if item['bom'] and 'name' in item['bom'] and item['bom']['name']:
			p = pool.get('md.bom.input.items').select(cr,pool,uid,['product','quantity','uom'],[('bom_id','=',item['bom']['name'])],context)
			for i in p:
				ei = pool.get('purchase.order.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.now().astimezone()+timedelta(3)
				item_items = pool.get('purchase.order.items')._buildEmptyItem()
				item_items['delivery_schedules'].append(ei)
				for f in ('product','uom'):
					item_items[f] = i[f]
				item_items['price'] = 0.00
				item['items'].append(item_items)

		return None

srm_plans()

class srm_plan_texts(Model):
	_name = 'srm.plan.texts'
	_description = 'SRM Plan Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'plan_id': fields.many2one(label='Plan',obj='srm.plans'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_plan_texts()


class srm_plan_roles(Model):
	_name = 'srm.plan.roles'
	_description = 'SRM Plan Roles'
	_columns = {
	'plan_id': fields.many2one(label = 'Plan',obj='srm.plans'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_plan_roles()

class srm_plan_output_plates(Model):
	_name = 'srm.plan.output.plates'
	_description = 'SRM Plan Output Plates'
	_columns = {
	'plan_id': fields.many2one(label = 'Plan',obj='srm.plans'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

class srm_plan_deadlines(Model):
	_name = 'srm.plan.deadlines'
	_description = 'General SRM Plan Deadlines'
	_order_by = 'start_date asc'
	_columns = {
	'plan_id': fields.many2one(label = 'Plan',obj='srm.plans',on_delete='c',on_update='c'),
	'sequence':fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Type',obj='srm.deadlines',on_delete='n',on_update='n'),
	'start_date': fields.datetime(label='Start',required=True),
	'end_date': fields.datetime(label='End',required=True),
	'required': fields.boolean(label='Required'),
	'note': fields.text('Note')}

srm_plan_deadlines()

class srm_plan_pricing(Model):
	_name = 'srm.plan.pricing'
	_description = 'SRM Plan Pricing'
	_columns = {
	'plan_id': fields.many2one(label = 'Plan',obj='srm.plans'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','srm')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_plan_pricing()

class srm_plan_payment_schedules(Model):
	_name = 'srm.plan.payment.schedules'
	_description = 'SRM Plan Payment Schedules'
	_columns = {
	'plan_id': fields.many2one(label = 'Plan',obj='srm.plans'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_plan_payment_schedules()

class srm_plan_items(Model):
	_name = 'srm.plan.items'
	_description = 'General SRM Plan Item'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'plan_id': fields.many2one(obj = 'srm.plans',label = 'Plan',on_delete='c',on_update='c'),
	'product': fields.many2one(label='Product',obj='md.product',on_delete='n',on_update='n',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='VAT Code',obj='md.vat.code',on_delete='n',on_update='n',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'currency_id': fields.many2one(label='Currency',obj='md.currency',on_delete='n',on_update='n'),
	'delivery_schedules': fields.one2many(label='Delivery Schedules',obj='srm.plan.item.delivery.schedules',rel='item_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.plan.pricing.items',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='srm.plan.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='srm.plan.item.texts',rel='item_id'),
	'plates': fields.one2many(label='Plates',obj='srm.plan.item.output.plates',rel='item_id'),
	'payments': fields.one2many(label='Payments',obj='srm.plan.item.payment.schedules',rel='item_id'),
	'note': fields.text('Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.srm.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
			if len(p) > 0:
				if item['vat_code'] != p[0]['vat']:
					item['vat_code'] = p[0]['vat']				
				for f in ('uom','price','currency','unit','uop'):
					if item[f] != p[0][f]:
						item[f] = p[0][f]

		return None

	_default = {
		'quantity': 1,
		'unit': 1
	}

srm_plan_items()

class srm_plan_pricing_items(Model):
	_name = 'srm.plan.pricing.items'
	_description = 'Plan Item Pricing'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.plan.items'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','p')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'cop': fields.many2one(label='Currency Of Price',obj='md.currency',required=True),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_plan_pricing_items()


class srm_plan_item_texts(Model):
	_name = 'srm.plan.item.texts'
	_description = 'SRM Plan Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='srm.plan.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_plan_item_texts()

class srm_plan_item_roles(Model):
	_name = 'srm.plan.item.roles'
	_description = 'SRM Plan Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.plan.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_plan_item_roles()

class srm_plan_item_delivery_schedules(Model):
	_name = 'srm.plan.item.delivery.schedules'
	_description = 'General SRM Plan Delivery Schedules'
	_date = "schedule"
	_columns = {
	'item_id': fields.many2one(obj = 'srm.plan.items',label = 'Item',on_delete='c',on_update='c'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom',on_delete='n',on_update='n'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')}

srm_plan_item_delivery_schedules()

class srm_plan_item_output_plates(Model):
	_name = 'srm.plan.item.output.plates'
	_description = 'Plan Item Output Plates'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.plan.items'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

srm_plan_item_output_plates()

class srm_plan_item_payment_schedules(Model):
	_name = 'srm.plan.item.payment.schedules'
	_description = 'Plan Item Payment Schedules'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.plan.items'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_plan_item_payment_schedules()

# SRM Request
# Types & Roles
class srm_request_types(Model):
	_name = 'srm.request.types'
	_description = 'Types SRM Request'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='srm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='srm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='srm.request.type.roles',rel='type_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.request.type.deadlines',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

srm_request_types()

class srm_request_type_roles(Model):
	_name = 'srm.request.type.roles'
	_description = 'Role SRM Request Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.request.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_request_type_roles()

class srm_request_type_deadlines(Model):
	_name = 'srm.request.type.deadlines'
	_description = 'Deadlines SRM Request Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.request.types'),
	'sequence': fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Deadline',obj='srm.deadlines'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_request_type_deadlines()

class srm_request_type_plates(Model):
	_name = 'srm.request.type.plates'
	_description = 'SRM Request Plates'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.request.types'),
	'seq': fields.integer(label='Sequence',required=True),
	'plate': fields.many2one(label = 'Plate',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_request_type_plates()


class srm_request_type_items(Model):
	_name = 'srm.request.type.items'
	_description = 'Type of SRM Request Items'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.request.types'),
	'gti_id': fields.many2one(label = 'GTI',obj='md.gtis'),
	'itype_id': fields.many2one(label = 'Type Of Items',obj='md.type.items',domain=[('usage','=','p'),'|',('usage','=','a')]),
	'note': fields.text(label = 'Note')
	}

srm_request_type_items()



# Types & Roles
#
class srm_requests(Model):
	_name = 'srm.requests'
	_description = 'General SRM Request'
	_inherits = {'srm.common':{'_methods':['copy_into','copy_from','_compute_fullname'],'_actions':['merge']},'common.model':{'_methods':['_calculate_amount_costs']}}
	_rec_name = 'fullname'
	_date = 'dor'
	_columns = {
	'rtype': fields.many2one(label='Type',obj='srm.request.types',on_change='_on_change_rtype'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'name': fields.varchar(label = 'Name'),
	'fullname': fields.composite(label='Full Name',cols=['rtype','company','name'],translate = True,required = True, compute = '_compute_composite'),
	'market': fields.many2one(label='Market',obj='srm.markets'),
	'team': fields.many2one(label='Team',obj='srm.teams'),
	'category_id': fields.many2one(label='Category',obj='srm.request.category'),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'origin': fields.varchar(label = 'Origin'),
	'dor': fields.date(label='Date Of Request',required=True),
	'from_date': fields.date(label='From Date Of Request',required=True),
	'to_date': fields.date(label='To Date Of Request',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',on_delete='n',on_update='n',domain=[('issuplier',)]),
	'route_id': fields.many2one(label='Route',obj='srm.routes',on_delete='n',on_update='n'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'bom': fields.many2one(label='BoM',obj='md.boms',domain=[('usage','=','srm'),'|',('usage','=','all')],on_change='_on_change_bom'),
	'items': fields.one2many(label='Items',obj='srm.request.items',rel='request_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.request.pricing',rel='request_id'),
	'roles': fields.one2many(label='Roles',obj='srm.request.roles',rel='request_id'),
	'texts': fields.one2many(label='Texts',obj='srm.request.texts',rel='request_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.request.deadlines',rel='request_id'),
	'plates': fields.one2many(label='Plates',obj='srm.request.output.plates',rel='request_id'),
	'payments': fields.one2many(label='Payments',obj='srm.request.payment.schedules',rel='request_id'),
	'note': fields.text('Note')}
	
	def _on_change_rtype(self,cr,pool,uid,item,context={}):		
		roles = pool.get('srm.request.type.roles').select(cr,pool,uid,['role_id'],[('type_id','=',item['rtype']['name'])],context)
		for role in roles:
			item_role = pool.get('srm.request.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)

		deadlines = pool.get('srm.request.type.deadlines').select(cr,pool,uid,['sequence','deadline_id','required'],[('type_id','=',item['rtype']['name'])],context)
		for deadline in deadlines:
			item_deadline = pool.get('srm.request.deadlines')._buildEmptyItem()
			item_deadline['sequence'] = deadline['sequence']
			item_deadline['deadline_id'] = deadline['deadline_id']
			item_deadline['required'] = deadline['required']
			item['deadlines'].append(item_deadline)
		
		types = pool.get('srm.request.types').select(cr,pool,uid,['htschema'],[('name','=',item['dtype']['name'])],context)	
		texts1 = pool.get('srm.schema.texts').select(cr,pool,uid,['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = pool.get('srm.request.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

	def _on_change_bom(self,cr,pool,uid,item,context={}):		
		if item['bom'] and 'name' in item['bom'] and item['bom']['name']:
			p = pool.get('md.bom.input.items').select(cr,pool,uid,['product','quantity','uom'],[('bom_id','=',item['bom']['name'])],context)
			for i in p:
				ei = pool.get('purchase.order.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.now().astimezone()+timedelta(3)
				item_items = pool.get('purchase.order.items')._buildEmptyItem()
				item_items['delivery_schedules'].append(ei)
				for f in ('product','uom'):
					item_items[f] = i[f]
				item_items['price'] = 0.00
				item['items'].append(item_items)

		return None

srm_requests()

class srm_request_texts(Model):
	_name = 'srm.request.texts'
	_description = 'SRM Request Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'request_id': fields.many2one(label='Request',obj='srm.requests'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_request_texts()


class srm_request_roles(Model):
	_name = 'srm.request.roles'
	_description = 'SRM Request Roles'
	_columns = {
	'request_id': fields.many2one(label = 'Request',obj='srm.requests'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_request_roles()

class srm_request_output_plates(Model):
	_name = 'srm.request.output.plates'
	_description = 'SRM Request Output Plates'
	_columns = {
	'request_id': fields.many2one(label = 'Request',obj='srm.requests'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

class srm_request_deadlines(Model):
	_name = 'srm.request.deadlines'
	_description = 'General SRM Request Deadlines'
	_order_by = 'start_date asc'
	_columns = {
	'request_id': fields.many2one(label = 'Request',obj='srm.requests',on_delete='c',on_update='c'),
	'sequence':fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Type',obj='srm.deadlines',on_delete='n',on_update='n'),
	'start_date': fields.datetime(label='Start',required=True),
	'end_date': fields.datetime(label='End',required=True),
	'required': fields.boolean(label='Required'),
	'note': fields.text('Note')}

srm_request_deadlines()

class srm_request_pricing(Model):
	_name = 'srm.request.pricing'
	_description = 'SRM Request Pricing'
	_columns = {
	'request_id': fields.many2one(label = 'Request',obj='srm.requests'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','srm')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_request_pricing()

class srm_request_payment_schedules(Model):
	_name = 'srm.request.payment.schedules'
	_description = 'SRM Request Payment Schedules'
	_columns = {
	'request_id': fields.many2one(label = 'Request',obj='srm.requests'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_request_payment_schedules()

class srm_request_items(Model):
	_name = 'srm.request.items'
	_description = 'General SRM Request Item'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'request_id': fields.many2one(obj = 'srm.requests',label = 'Request',on_delete='c',on_update='c'),
	'product': fields.many2one(label='Product',obj='md.product',on_delete='n',on_update='n',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='VAT Code',obj='md.vat.code',on_delete='n',on_update='n',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'currency_id': fields.many2one(label='Currency',obj='md.currency',on_delete='n',on_update='n'),
	'delivery_schedules': fields.one2many(label='Delivery Schedules',obj='srm.request.item.delivery.schedules',rel='item_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.request.pricing.items',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='srm.request.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='srm.request.item.texts',rel='item_id'),
	'plates': fields.one2many(label='Plates',obj='srm.request.item.output.plates',rel='item_id'),
	'payments': fields.one2many(label='Payments',obj='srm.request.item.payment.schedules',rel='item_id'),
	'note': fields.text('Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.srm.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
			if len(p) > 0:
				if item['vat_code'] != p[0]['vat']:
					item['vat_code'] = p[0]['vat']				
				for f in ('uom','price','currency','unit','uop'):
					if item[f] != p[0][f]:
						item[f] = p[0][f]

		return None

	_default = {
		'quantity': 1,
		'unit': 1
	}

srm_request_items()

class srm_request_pricing_items(Model):
	_name = 'srm.request.pricing.items'
	_description = 'Request Item Pricing'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.request.items'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','p')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'cop': fields.many2one(label='Currency Of Price',obj='md.currency',required=True),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_request_pricing_items()


class srm_request_item_texts(Model):
	_name = 'srm.request.item.texts'
	_description = 'SRM Request Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='srm.request.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_request_item_texts()

class srm_request_item_roles(Model):
	_name = 'srm.request.item.roles'
	_description = 'SRM Request Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.request.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_request_item_roles()

class srm_request_item_delivery_schedules(Model):
	_name = 'srm.request.item.delivery.schedules'
	_description = 'General SRM Request Delivery Schedules'
	_date = "schedule"
	_columns = {
	'item_id': fields.many2one(obj = 'srm.request.items',label = 'Item',on_delete='c',on_update='c'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom',on_delete='n',on_update='n'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')}

srm_request_item_delivery_schedules()

class srm_request_item_output_plates(Model):
	_name = 'srm.request.item.output.plates'
	_description = 'Request Item Output Plates'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.request.items'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

srm_request_item_output_plates()

class srm_request_item_payment_schedules(Model):
	_name = 'srm.request.item.payment.schedules'
	_description = 'Request Item Payment Schedules'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.request.items'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_request_item_payment_schedules()

# SRM Response
# Types & Roles
class srm_response_types(Model):
	_name = 'srm.response.types'
	_description = 'Types SRM Response'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='srm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='srm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='srm.response.type.roles',rel='type_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.response.type.deadlines',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

srm_response_types()

class srm_response_type_roles(Model):
	_name = 'srm.response.type.roles'
	_description = 'Role SRM Response Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.response.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_response_type_roles()

class srm_response_type_deadlines(Model):
	_name = 'srm.response.type.deadlines'
	_description = 'Deadlines SRM Response Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.response.types'),
	'sequence': fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Deadline',obj='srm.deadlines'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_response_type_deadlines()

class srm_response_type_plates(Model):
	_name = 'srm.response.type.plates'
	_description = 'SRM Response Plates'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.response.types'),
	'seq': fields.integer(label='Sequence',required=True),
	'plate': fields.many2one(label = 'Plate',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_response_type_plates()


class srm_response_type_items(Model):
	_name = 'srm.response.type.items'
	_description = 'Type of SRM Response Items'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.response.types'),
	'gti_id': fields.many2one(label = 'GTI',obj='md.gtis'),
	'itype_id': fields.many2one(label = 'Type Of Items',obj='md.type.items',domain=[('usage','=','p'),'|',('usage','=','a')]),
	'note': fields.text(label = 'Note')
	}

srm_response_type_items()



# Types & Roles
#
class srm_responses(Model):
	_name = 'srm.responses'
	_description = 'General SRM Response'
	_inherits = {'srm.common':{'_methods':['copy_into','copy_from','_compute_fullname'],'_actions':['merge']},'common.model':{'_methods':['_calculate_amount_costs']}}
	_rec_name = 'fullname'
	_date = 'dor'
	_columns = {
	'rtype': fields.many2one(label='Type',obj='srm.response.types',on_change='_on_change_rtype'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'name': fields.varchar(label = 'Name'),
	'fullname': fields.composite(label='Full Name',cols=['rtype','company','name'],translate = True,required = True, compute = '_compute_composite'),
	'market': fields.many2one(label='Market',obj='srm.markets'),
	'team': fields.many2one(label='Team',obj='srm.teams'),
	'category_id': fields.many2one(label='Category',obj='srm.response.category'),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'origin': fields.varchar(label = 'Origin'),
	'dor': fields.date(label='Date Of Response',required=True),
	'from_date': fields.date(label='From Date Of Response',required=True),
	'to_date': fields.date(label='To Date Of Response',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',on_delete='n',on_update='n',domain=[('issuplier',)]),
	'route_id': fields.many2one(label='Route',obj='srm.routes',on_delete='n',on_update='n'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'bom': fields.many2one(label='BoM',obj='md.boms',domain=[('usage','=','srm'),'|',('usage','=','all')],on_change='_on_change_bom'),
	'items': fields.one2many(label='Items',obj='srm.response.items',rel='response_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.response.pricing',rel='response_id'),
	'roles': fields.one2many(label='Roles',obj='srm.response.roles',rel='response_id'),
	'texts': fields.one2many(label='Texts',obj='srm.response.texts',rel='response_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.response.deadlines',rel='response_id'),
	'plates': fields.one2many(label='Plates',obj='srm.response.output.plates',rel='response_id'),
	'payments': fields.one2many(label='Payments',obj='srm.response.payment.schedules',rel='response_id'),
	'note': fields.text('Note')}
	
	def _on_change_rtype(self,cr,pool,uid,item,context={}):		
		roles = pool.get('srm.response.type.roles').select(cr,pool,uid,['role_id'],[('type_id','=',item['rtype']['name'])],context)
		for role in roles:
			item_role = pool.get('srm.response.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)

		deadlines = pool.get('srm.response.type.deadlines').select(cr,pool,uid,['sequence','deadline_id','required'],[('type_id','=',item['rtype']['name'])],context)
		for deadline in deadlines:
			item_deadline = pool.get('srm.response.deadlines')._buildEmptyItem()
			item_deadline['sequence'] = deadline['sequence']
			item_deadline['deadline_id'] = deadline['deadline_id']
			item_deadline['required'] = deadline['required']
			item['deadlines'].append(item_deadline)
		
		types = pool.get('srm.response.types').select(cr,pool,uid,['htschema'],[('name','=',item['dtype']['name'])],context)	
		texts1 = pool.get('srm.schema.texts').select(cr,pool,uid,['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = pool.get('srm.response.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

	def _on_change_bom(self,cr,pool,uid,item,context={}):		
		if item['bom'] and 'name' in item['bom'] and item['bom']['name']:
			p = pool.get('md.bom.input.items').select(cr,pool,uid,['product','quantity','uom'],[('bom_id','=',item['bom']['name'])],context)
			for i in p:
				ei = pool.get('purchase.order.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.now().astimezone()+timedelta(3)
				item_items = pool.get('purchase.order.items')._buildEmptyItem()
				item_items['delivery_schedules'].append(ei)
				for f in ('product','uom'):
					item_items[f] = i[f]
				item_items['price'] = 0.00
				item['items'].append(item_items)

		return None

srm_responses()

class srm_response_texts(Model):
	_name = 'srm.response.texts'
	_description = 'SRM Response Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'response_id': fields.many2one(label='Response',obj='srm.responses'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_response_texts()


class srm_response_roles(Model):
	_name = 'srm.response.roles'
	_description = 'SRM Response Roles'
	_columns = {
	'response_id': fields.many2one(label = 'Response',obj='srm.responses'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_response_roles()

class srm_response_output_plates(Model):
	_name = 'srm.response.output.plates'
	_description = 'SRM Response Output Plates'
	_columns = {
	'response_id': fields.many2one(label = 'Response',obj='srm.responses'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

class srm_response_deadlines(Model):
	_name = 'srm.response.deadlines'
	_description = 'General SRM Response Deadlines'
	_order_by = 'start_date asc'
	_columns = {
	'response_id': fields.many2one(label = 'Response',obj='srm.responses',on_delete='c',on_update='c'),
	'sequence':fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Type',obj='srm.deadlines',on_delete='n',on_update='n'),
	'start_date': fields.datetime(label='Start',required=True),
	'end_date': fields.datetime(label='End',required=True),
	'required': fields.boolean(label='Required'),
	'note': fields.text('Note')}

srm_response_deadlines()

class srm_response_pricing(Model):
	_name = 'srm.response.pricing'
	_description = 'SRM Response Pricing'
	_columns = {
	'response_id': fields.many2one(label = 'Response',obj='srm.responses'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','srm')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_response_pricing()

class srm_response_payment_schedules(Model):
	_name = 'srm.response.payment.schedules'
	_description = 'SRM Response Payment Schedules'
	_columns = {
	'response_id': fields.many2one(label = 'Response',obj='srm.responses'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_response_payment_schedules()

class srm_response_items(Model):
	_name = 'srm.response.items'
	_description = 'General SRM Response Item'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'response_id': fields.many2one(obj = 'srm.responses',label = 'Response',on_delete='c',on_update='c'),
	'product': fields.many2one(label='Product',obj='md.product',on_delete='n',on_update='n',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='VAT Code',obj='md.vat.code',on_delete='n',on_update='n',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'currency_id': fields.many2one(label='Currency',obj='md.currency',on_delete='n',on_update='n'),
	'delivery_schedules': fields.one2many(label='Delivery Schedules',obj='srm.response.item.delivery.schedules',rel='item_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.response.pricing.items',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='srm.response.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='srm.response.item.texts',rel='item_id'),
	'plates': fields.one2many(label='Plates',obj='srm.response.item.output.plates',rel='item_id'),
	'payments': fields.one2many(label='Payments',obj='srm.response.item.payment.schedules',rel='item_id'),
	'note': fields.text('Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.srm.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
			if len(p) > 0:
				if item['vat_code'] != p[0]['vat']:
					item['vat_code'] = p[0]['vat']				
				for f in ('uom','price','currency','unit','uop'):
					if item[f] != p[0][f]:
						item[f] = p[0][f]

		return None

	_default = {
		'quantity': 1,
		'unit': 1
	}

srm_response_items()

class srm_response_pricing_items(Model):
	_name = 'srm.response.pricing.items'
	_description = 'Response Item Pricing'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.response.items'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','p')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'cop': fields.many2one(label='Currency Of Price',obj='md.currency',required=True),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_response_pricing_items()


class srm_response_item_texts(Model):
	_name = 'srm.response.item.texts'
	_description = 'SRM Response Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='srm.response.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_response_item_texts()

class srm_response_item_roles(Model):
	_name = 'srm.response.item.roles'
	_description = 'SRM Response Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.response.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_response_item_roles()

class srm_response_item_delivery_schedules(Model):
	_name = 'srm.response.item.delivery.schedules'
	_description = 'General SRM Response Delivery Schedules'
	_date = "schedule"
	_columns = {
	'item_id': fields.many2one(obj = 'srm.response.items',label = 'Item',on_delete='c',on_update='c'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom',on_delete='n',on_update='n'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')}

srm_response_item_delivery_schedules()

class srm_response_item_output_plates(Model):
	_name = 'srm.response.item.output.plates'
	_description = 'Response Item Output Plates'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.response.items'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

srm_response_item_output_plates()

class srm_response_item_payment_schedules(Model):
	_name = 'srm.response.item.payment.schedules'
	_description = 'Response Item Payment Schedules'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.response.items'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_response_item_payment_schedules()


# SRM RFX
# Types & Roles
class srm_rfx_types(Model):
	_name = 'srm.rfx.types'
	_description = 'Types SRM RFX'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='srm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='srm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='srm.rfx.type.roles',rel='type_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.rfx.type.deadlines',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

srm_rfx_types()

class srm_rfx_type_roles(Model):
	_name = 'srm.rfx.type.roles'
	_description = 'Role SRM RFX Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.rfx.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_rfx_type_roles()

class srm_rfx_type_deadlines(Model):
	_name = 'srm.rfx.type.deadlines'
	_description = 'Deadlines SRM RFX Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.rfx.types'),
	'sequence': fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Deadline',obj='srm.deadlines'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_rfx_type_deadlines()

class srm_rfx_type_plates(Model):
	_name = 'srm.rfx.type.plates'
	_description = 'SRM RFX Plates'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.rfx.types'),
	'seq': fields.integer(label='Sequence',required=True),
	'plate': fields.many2one(label = 'Plate',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_rfx_type_plates()


class srm_rfx_type_items(Model):
	_name = 'srm.rfx.type.items'
	_description = 'Type of SRM RFX Items'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.rfx.types'),
	'gti_id': fields.many2one(label = 'GTI',obj='md.gtis'),
	'itype_id': fields.many2one(label = 'Type Of Items',obj='md.type.items',domain=[('usage','=','p'),'|',('usage','=','a')]),
	'note': fields.text(label = 'Note')
	}

srm_rfx_type_items()



# Types & Roles
#
class srm_rfxs(Model):
	_name = 'srm.rfxs'
	_description = 'General SRM RFX'
	_inherits = {'srm.common':{'_methods':['copy_into','copy_from','_compute_fullname'],'_actions':['merge']},'common.model':{'_methods':['_calculate_amount_costs']}}
	_rec_name = 'fullname'
	_date = 'dor'
	_columns = {
	'rtype': fields.many2one(label='Type',obj='srm.rfx.types',on_change='_on_change_rtype'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'name': fields.varchar(label = 'Name'),
	'fullname': fields.composite(label='Full Name',cols=['rtype','company','name'],translate = True,required = True, compute = '_compute_composite'),
	'market': fields.many2one(label='Market',obj='srm.markets'),
	'team': fields.many2one(label='Team',obj='srm.teams'),
	'category_id': fields.many2one(label='Category',obj='srm.rfx.category'),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'origin': fields.varchar(label = 'Origin'),
	'dor': fields.date(label='Date Of RFX',required=True),
	'from_date': fields.date(label='From Date Of RFX',required=True),
	'to_date': fields.date(label='To Date Of RFX',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',on_delete='n',on_update='n',domain=[('issuplier',)]),
	'route_id': fields.many2one(label='Route',obj='srm.routes',on_delete='n',on_update='n'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'bom': fields.many2one(label='BoM',obj='md.boms',domain=[('usage','=','srm'),'|',('usage','=','all')],on_change='_on_change_bom'),
	'items': fields.one2many(label='Items',obj='srm.rfx.items',rel='rfx_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.rfx.pricing',rel='rfx_id'),
	'roles': fields.one2many(label='Roles',obj='srm.rfx.roles',rel='rfx_id'),
	'texts': fields.one2many(label='Texts',obj='srm.rfx.texts',rel='rfx_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.rfx.deadlines',rel='rfx_id'),
	'plates': fields.one2many(label='Plates',obj='srm.rfx.output.plates',rel='rfx_id'),
	'payments': fields.one2many(label='Payments',obj='srm.rfx.payment.schedules',rel='rfx_id'),
	'note': fields.text('Note')}
	
	def _on_change_rtype(self,cr,pool,uid,item,context={}):		
		roles = pool.get('srm.rfx.type.roles').select(cr,pool,uid,['role_id'],[('type_id','=',item['rtype']['name'])],context)
		for role in roles:
			item_role = pool.get('srm.rfx.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)

		deadlines = pool.get('srm.rfx.type.deadlines').select(cr,pool,uid,['sequence','deadline_id','required'],[('type_id','=',item['rtype']['name'])],context)
		for deadline in deadlines:
			item_deadline = pool.get('srm.rfx.deadlines')._buildEmptyItem()
			item_deadline['sequence'] = deadline['sequence']
			item_deadline['deadline_id'] = deadline['deadline_id']
			item_deadline['required'] = deadline['required']
			item['deadlines'].append(item_deadline)
		
		types = pool.get('srm.rfx.types').select(cr,pool,uid,['htschema'],[('name','=',item['dtype']['name'])],context)	
		texts1 = pool.get('srm.schema.texts').select(cr,pool,uid,['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = pool.get('srm.rfx.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

	def _on_change_bom(self,cr,pool,uid,item,context={}):		
		if item['bom'] and 'name' in item['bom'] and item['bom']['name']:
			p = pool.get('md.bom.input.items').select(cr,pool,uid,['product','quantity','uom'],[('bom_id','=',item['bom']['name'])],context)
			for i in p:
				ei = pool.get('purchase.order.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.now().astimezone()+timedelta(3)
				item_items = pool.get('purchase.order.items')._buildEmptyItem()
				item_items['delivery_schedules'].append(ei)
				for f in ('product','uom'):
					item_items[f] = i[f]
				item_items['price'] = 0.00
				item['items'].append(item_items)

		return None

srm_rfxs()

class srm_rfx_texts(Model):
	_name = 'srm.rfx.texts'
	_description = 'SRM RFX Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'rfx_id': fields.many2one(label='RFX',obj='srm.rfxs'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_rfx_texts()


class srm_rfx_roles(Model):
	_name = 'srm.rfx.roles'
	_description = 'SRM RFX Roles'
	_columns = {
	'rfx_id': fields.many2one(label = 'RFX',obj='srm.rfxs'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_rfx_roles()

class srm_rfx_output_plates(Model):
	_name = 'srm.rfx.output.plates'
	_description = 'SRM RFX Output Plates'
	_columns = {
	'rfx_id': fields.many2one(label = 'RFX',obj='srm.rfxs'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

class srm_rfx_deadlines(Model):
	_name = 'srm.rfx.deadlines'
	_description = 'General SRM RFX Deadlines'
	_order_by = 'start_date asc'
	_columns = {
	'rfx_id': fields.many2one(label = 'RFX',obj='srm.rfxs',on_delete='c',on_update='c'),
	'sequence':fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Type',obj='srm.deadlines',on_delete='n',on_update='n'),
	'start_date': fields.datetime(label='Start',required=True),
	'end_date': fields.datetime(label='End',required=True),
	'required': fields.boolean(label='Required'),
	'note': fields.text('Note')}

srm_rfx_deadlines()

class srm_rfx_pricing(Model):
	_name = 'srm.rfx.pricing'
	_description = 'SRM RFX Pricing'
	_columns = {
	'rfx_id': fields.many2one(label = 'RFX',obj='srm.rfxs'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','srm')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_rfx_pricing()

class srm_rfx_payment_schedules(Model):
	_name = 'srm.rfx.payment.schedules'
	_description = 'SRM RFX Payment Schedules'
	_columns = {
	'rfx_id': fields.many2one(label = 'RFX',obj='srm.rfxs'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_rfx_payment_schedules()

class srm_rfx_items(Model):
	_name = 'srm.rfx.items'
	_description = 'General SRM RFX Item'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'rfx_id': fields.many2one(obj = 'srm.rfxs',label = 'RFX',on_delete='c',on_update='c'),
	'product': fields.many2one(label='Product',obj='md.product',on_delete='n',on_update='n',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='VAT Code',obj='md.vat.code',on_delete='n',on_update='n',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'currency_id': fields.many2one(label='Currency',obj='md.currency',on_delete='n',on_update='n'),
	'delivery_schedules': fields.one2many(label='Delivery Schedules',obj='srm.rfx.item.delivery.schedules',rel='item_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.rfx.pricing.items',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='srm.rfx.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='srm.rfx.item.texts',rel='item_id'),
	'plates': fields.one2many(label='Plates',obj='srm.rfx.item.output.plates',rel='item_id'),
	'payments': fields.one2many(label='Payments',obj='srm.rfx.item.payment.schedules',rel='item_id'),
	'note': fields.text('Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.srm.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
			if len(p) > 0:
				if item['vat_code'] != p[0]['vat']:
					item['vat_code'] = p[0]['vat']				
				for f in ('uom','price','currency','unit','uop'):
					if item[f] != p[0][f]:
						item[f] = p[0][f]

		return None

	_default = {
		'quantity': 1,
		'unit': 1
	}

srm_rfx_items()

class srm_rfx_pricing_items(Model):
	_name = 'srm.rfx.pricing.items'
	_description = 'RFX Item Pricing'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.rfx.items'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','p')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'cop': fields.many2one(label='Currency Of Price',obj='md.currency',required=True),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_rfx_pricing_items()


class srm_rfx_item_texts(Model):
	_name = 'srm.rfx.item.texts'
	_description = 'SRM RFX Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='srm.rfx.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_rfx_item_texts()

class srm_rfx_item_roles(Model):
	_name = 'srm.rfx.item.roles'
	_description = 'SRM RFX Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.rfx.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_rfx_item_roles()

class srm_rfx_item_delivery_schedules(Model):
	_name = 'srm.rfx.item.delivery.schedules'
	_description = 'General SRM RFX Delivery Schedules'
	_date = "schedule"
	_columns = {
	'item_id': fields.many2one(obj = 'srm.rfx.items',label = 'Item',on_delete='c',on_update='c'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom',on_delete='n',on_update='n'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')}

srm_rfx_item_delivery_schedules()

class srm_rfx_item_output_plates(Model):
	_name = 'srm.rfx.item.output.plates'
	_description = 'RFX Item Output Plates'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.rfx.items'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

srm_rfx_item_output_plates()

class srm_rfx_item_payment_schedules(Model):
	_name = 'srm.rfx.item.payment.schedules'
	_description = 'RFX Item Payment Schedules'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.rfx.items'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_rfx_item_payment_schedules()

# SRM Auction
# Types & Roles
class srm_auction_types(Model):
	_name = 'srm.auction.types'
	_description = 'Types SRM Auction'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='srm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='srm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='srm.auction.type.roles',rel='type_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.auction.type.deadlines',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

srm_auction_types()

class srm_auction_type_roles(Model):
	_name = 'srm.auction.type.roles'
	_description = 'Role SRM Auction Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.auction.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_auction_type_roles()

class srm_auction_type_deadlines(Model):
	_name = 'srm.auction.type.deadlines'
	_description = 'Deadlines SRM Auction Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.auction.types'),
	'sequence': fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Deadline',obj='srm.deadlines'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_auction_type_deadlines()

class srm_auction_type_plates(Model):
	_name = 'srm.auction.type.plates'
	_description = 'SRM Auction Plates'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.auction.types'),
	'seq': fields.integer(label='Sequence',required=True),
	'plate': fields.many2one(label = 'Plate',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_auction_type_plates()


class srm_auction_type_items(Model):
	_name = 'srm.auction.type.items'
	_description = 'Type of SRM Auction Items'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.auction.types'),
	'gti_id': fields.many2one(label = 'GTI',obj='md.gtis'),
	'itype_id': fields.many2one(label = 'Type Of Items',obj='md.type.items',domain=[('usage','=','p'),'|',('usage','=','a')]),
	'note': fields.text(label = 'Note')
	}

srm_auction_type_items()



# Types & Roles
#
class srm_auctions(Model):
	_name = 'srm.auctions'
	_description = 'General SRM Auction'
	_inherits = {'srm.common':{'_methods':['copy_into','copy_from','_compute_fullname'],'_actions':['merge']},'common.model':{'_methods':['_calculate_amount_costs']}}
	_rec_name = 'fullname'
	_date = 'doa'
	_columns = {
	'atype': fields.many2one(label='Type',obj='srm.auction.types',on_change='_on_change_atype'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'name': fields.varchar(label = 'Name'),
	'fullname': fields.composite(label='Full Name',cols=['atype','company','name'],translate = True,required = True, compute = '_compute_composite'),
	'market': fields.many2one(label='Market',obj='srm.markets'),
	'team': fields.many2one(label='Team',obj='srm.teams'),
	'category_id': fields.many2one(label='Category',obj='srm.auction.category'),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'origin': fields.varchar(label = 'Origin'),
	'doa': fields.date(label='Date Of Auction',required=True),
	'from_date': fields.date(label='From Date Of Auction',required=True),
	'to_date': fields.date(label='To Date Of Auction',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',on_delete='n',on_update='n',domain=[('issuplier',)]),
	'route_id': fields.many2one(label='Route',obj='srm.routes',on_delete='n',on_update='n'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'bom': fields.many2one(label='BoM',obj='md.boms',domain=[('usage','=','srm'),'|',('usage','=','all')],on_change='_on_change_bom'),
	'items': fields.one2many(label='Items',obj='srm.auction.items',rel='auction_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.auction.pricing',rel='auction_id'),
	'roles': fields.one2many(label='Roles',obj='srm.auction.roles',rel='auction_id'),
	'texts': fields.one2many(label='Texts',obj='srm.auction.texts',rel='auction_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.auction.deadlines',rel='auction_id'),
	'plates': fields.one2many(label='Plates',obj='srm.auction.output.plates',rel='auction_id'),
	'payments': fields.one2many(label='Payments',obj='srm.auction.payment.schedules',rel='auction_id'),
	'note': fields.text('Note')}
	
	def _on_change_atype(self,cr,pool,uid,item,context={}):		
		roles = pool.get('srm.auction.type.roles').select(cr,pool,uid,['role_id'],[('type_id','=',item['atype']['name'])],context)
		for role in roles:
			item_role = pool.get('srm.auction.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)

		deadlines = pool.get('srm.auction.type.deadlines').select(cr,pool,uid,['sequence','deadline_id','required'],[('type_id','=',item['atype']['name'])],context)
		for deadline in deadlines:
			item_deadline = pool.get('srm.auction.deadlines')._buildEmptyItem()
			item_deadline['sequence'] = deadline['sequence']
			item_deadline['deadline_id'] = deadline['deadline_id']
			item_deadline['required'] = deadline['required']
			item['deadlines'].append(item_deadline)
		
		types = pool.get('srm.auction.types').select(cr,pool,uid,['htschema'],[('name','=',item['dtype']['name'])],context)	
		texts1 = pool.get('srm.schema.texts').select(cr,pool,uid,['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = pool.get('srm.auction.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

	def _on_change_bom(self,cr,pool,uid,item,context={}):		
		if item['bom'] and 'name' in item['bom'] and item['bom']['name']:
			p = pool.get('md.bom.input.items').select(cr,pool,uid,['product','quantity','uom'],[('bom_id','=',item['bom']['name'])],context)
			for i in p:
				ei = pool.get('purchase.order.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.now().astimezone()+timedelta(3)
				item_items = pool.get('purchase.order.items')._buildEmptyItem()
				item_items['delivery_schedules'].append(ei)
				for f in ('product','uom'):
					item_items[f] = i[f]
				item_items['price'] = 0.00
				item['items'].append(item_items)

		return None

srm_auctions()

class srm_auction_texts(Model):
	_name = 'srm.auction.texts'
	_description = 'SRM Auction Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'auction_id': fields.many2one(label='Auction',obj='srm.auctions'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_auction_texts()


class srm_auction_roles(Model):
	_name = 'srm.auction.roles'
	_description = 'SRM Auction Roles'
	_columns = {
	'auction_id': fields.many2one(label = 'Auction',obj='srm.auctions'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_auction_roles()

class srm_auction_output_plates(Model):
	_name = 'srm.auction.output.plates'
	_description = 'SRM Auction Output Plates'
	_columns = {
	'auction_id': fields.many2one(label = 'Auction',obj='srm.auctions'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

class srm_auction_deadlines(Model):
	_name = 'srm.auction.deadlines'
	_description = 'General SRM Auction Deadlines'
	_order_by = 'start_date asc'
	_columns = {
	'auction_id': fields.many2one(label = 'Auction',obj='srm.auctions',on_delete='c',on_update='c'),
	'sequence':fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Type',obj='srm.deadlines',on_delete='n',on_update='n'),
	'start_date': fields.datetime(label='Start',required=True),
	'end_date': fields.datetime(label='End',required=True),
	'required': fields.boolean(label='Required'),
	'note': fields.text('Note')}

srm_auction_deadlines()

class srm_auction_pricing(Model):
	_name = 'srm.auction.pricing'
	_description = 'SRM Auction Pricing'
	_columns = {
	'auction_id': fields.many2one(label = 'Auction',obj='srm.auctions'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','srm')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_auction_pricing()

class srm_auction_payment_schedules(Model):
	_name = 'srm.auction.payment.schedules'
	_description = 'SRM Auction Payment Schedules'
	_columns = {
	'auction_id': fields.many2one(label = 'Auction',obj='srm.auctions'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_auction_payment_schedules()

class srm_auction_items(Model):
	_name = 'srm.auction.items'
	_description = 'General SRM Auction Item'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'auction_id': fields.many2one(obj = 'srm.auctions',label = 'Auction',on_delete='c',on_update='c'),
	'product': fields.many2one(label='Product',obj='md.product',on_delete='n',on_update='n',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='VAT Code',obj='md.vat.code',on_delete='n',on_update='n',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'currency_id': fields.many2one(label='Currency',obj='md.currency',on_delete='n',on_update='n'),
	'delivery_schedules': fields.one2many(label='Delivery Schedules',obj='srm.auction.item.delivery.schedules',rel='item_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.auction.pricing.items',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='srm.auction.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='srm.auction.item.texts',rel='item_id'),
	'plates': fields.one2many(label='Plates',obj='srm.auction.item.output.plates',rel='item_id'),
	'payments': fields.one2many(label='Payments',obj='srm.auction.item.payment.schedules',rel='item_id'),
	'note': fields.text('Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.srm.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
			if len(p) > 0:
				if item['vat_code'] != p[0]['vat']:
					item['vat_code'] = p[0]['vat']				
				for f in ('uom','price','currency','unit','uop'):
					if item[f] != p[0][f]:
						item[f] = p[0][f]

		return None

	_default = {
		'quantity': 1,
		'unit': 1
	}

srm_auction_items()

class srm_auction_pricing_items(Model):
	_name = 'srm.auction.pricing.items'
	_description = 'Auction Item Pricing'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.auction.items'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','p')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'cop': fields.many2one(label='Currency Of Price',obj='md.currency',required=True),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_auction_pricing_items()


class srm_auction_item_texts(Model):
	_name = 'srm.auction.item.texts'
	_description = 'SRM Auction Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='srm.auction.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_auction_item_texts()

class srm_auction_item_roles(Model):
	_name = 'srm.auction.item.roles'
	_description = 'SRM Auction Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.auction.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_auction_item_roles()

class srm_auction_item_delivery_schedules(Model):
	_name = 'srm.auction.item.delivery.schedules'
	_description = 'General SRM Auction Delivery Schedules'
	_date = "schedule"
	_columns = {
	'item_id': fields.many2one(obj = 'srm.auction.items',label = 'Item',on_delete='c',on_update='c'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom',on_delete='n',on_update='n'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')}

srm_auction_item_delivery_schedules()

class srm_auction_item_output_plates(Model):
	_name = 'srm.auction.item.output.plates'
	_description = 'Auction Item Output Plates'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.auction.items'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

srm_auction_item_output_plates()

class srm_auction_item_payment_schedules(Model):
	_name = 'srm.auction.item.payment.schedules'
	_description = 'Auction Item Payment Schedules'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.auction.items'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_auction_item_payment_schedules()

# SRM Offer
# Types & Roles
class srm_offer_types(Model):
	_name = 'srm.offer.types'
	_description = 'Types SRM Offer'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='srm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='srm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='srm.offer.type.roles',rel='type_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.offer.type.deadlines',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

srm_offer_types()

class srm_offer_type_roles(Model):
	_name = 'srm.offer.type.roles'
	_description = 'Role SRM Offer Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.offer.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_offer_type_roles()

class srm_offer_type_deadlines(Model):
	_name = 'srm.offer.type.deadlines'
	_description = 'Deadlines SRM Offer Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.offer.types'),
	'sequence': fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Deadline',obj='srm.deadlines'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_offer_type_deadlines()

class srm_offer_type_plates(Model):
	_name = 'srm.offer.type.plates'
	_description = 'SRM Offer Plates'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.offer.types'),
	'seq': fields.integer(label='Sequence',required=True),
	'plate': fields.many2one(label = 'Plate',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_offer_type_plates()


class srm_offer_type_items(Model):
	_name = 'srm.offer.type.items'
	_description = 'Type of SRM Offer Items'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.offer.types'),
	'gti_id': fields.many2one(label = 'GTI',obj='md.gtis'),
	'itype_id': fields.many2one(label = 'Type Of Items',obj='md.type.items',domain=[('usage','=','p'),'|',('usage','=','a')]),
	'note': fields.text(label = 'Note')
	}

srm_offer_type_items()



# Types & Roles
#
class srm_offers(Model):
	_name = 'srm.offers'
	_description = 'General SRM Offer'
	_inherits = {'srm.common':{'_methods':['copy_into','copy_from','_compute_fullname'],'_actions':['merge']},'common.model':{'_methods':['_calculate_amount_costs']}}
	_rec_name = 'fullname'
	_date = 'doo'
	_columns = {
	'otype': fields.many2one(label='Type',obj='srm.offer.types',on_change='_on_change_otype'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'name': fields.varchar(label = 'Name'),
	'fullname': fields.composite(label='Full Name',cols=['otype','company','name'],translate = True,required = True, compute = '_compute_composite'),
	'market': fields.many2one(label='Market',obj='srm.markets'),
	'team': fields.many2one(label='Team',obj='srm.teams'),
	'category_id': fields.many2one(label='Category',obj='srm.offer.category'),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'origin': fields.varchar(label = 'Origin'),
	'doo': fields.date(label='Date Of Offer',required=True),
	'from_date': fields.date(label='From Date Of Offer',required=True),
	'to_date': fields.date(label='To Date Of Offer',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',on_delete='n',on_update='n',domain=[('issuplier',)]),
	'route_id': fields.many2one(label='Route',obj='srm.routes',on_delete='n',on_update='n'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'bom': fields.many2one(label='BoM',obj='md.boms',domain=[('usage','=','srm'),'|',('usage','=','all')],on_change='_on_change_bom'),
	'items': fields.one2many(label='Items',obj='srm.offer.items',rel='offer_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.offer.pricing',rel='offer_id'),
	'roles': fields.one2many(label='Roles',obj='srm.offer.roles',rel='offer_id'),
	'texts': fields.one2many(label='Texts',obj='srm.offer.texts',rel='offer_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.offer.deadlines',rel='offer_id'),
	'plates': fields.one2many(label='Plates',obj='srm.offer.output.plates',rel='offer_id'),
	'payments': fields.one2many(label='Payments',obj='srm.offer.payment.schedules',rel='offer_id'),
	'note': fields.text('Note')}
	
	def _on_change_otype(self,cr,pool,uid,item,context={}):		
		roles = pool.get('srm.offer.type.roles').select(cr,pool,uid,['role_id'],[('type_id','=',item['otype']['name'])],context)
		for role in roles:
			item_role = pool.get('srm.offer.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)

		deadlines = pool.get('srm.offer.type.deadlines').select(cr,pool,uid,['sequence','deadline_id','required'],[('type_id','=',item['otype']['name'])],context)
		for deadline in deadlines:
			item_deadline = pool.get('srm.offer.deadlines')._buildEmptyItem()
			item_deadline['sequence'] = deadline['sequence']
			item_deadline['deadline_id'] = deadline['deadline_id']
			item_deadline['required'] = deadline['required']
			item['deadlines'].append(item_deadline)
		
		types = pool.get('srm.offer.types').select(cr,pool,uid,['htschema'],[('name','=',item['dtype']['name'])],context)	
		texts1 = pool.get('srm.schema.texts').select(cr,pool,uid,['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = pool.get('srm.offer.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

	def _on_change_bom(self,cr,pool,uid,item,context={}):		
		if item['bom'] and 'name' in item['bom'] and item['bom']['name']:
			p = pool.get('md.bom.input.items').select(cr,pool,uid,['product','quantity','uom'],[('bom_id','=',item['bom']['name'])],context)
			for i in p:
				ei = pool.get('purchase.order.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.now().astimezone()+timedelta(3)
				item_items = pool.get('purchase.order.items')._buildEmptyItem()
				item_items['delivery_schedules'].append(ei)
				for f in ('product','uom'):
					item_items[f] = i[f]
				item_items['price'] = 0.00
				item['items'].append(item_items)

		return None

srm_offers()

class srm_offer_texts(Model):
	_name = 'srm.offer.texts'
	_description = 'SRM Offer Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'offer_id': fields.many2one(label='Offer',obj='srm.offers'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_offer_texts()


class srm_offer_roles(Model):
	_name = 'srm.offer.roles'
	_description = 'SRM Offer Roles'
	_columns = {
	'offer_id': fields.many2one(label = 'Offer',obj='srm.offers'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_offer_roles()

class srm_offer_output_plates(Model):
	_name = 'srm.offer.output.plates'
	_description = 'SRM Offer Output Plates'
	_columns = {
	'offer_id': fields.many2one(label = 'Offer',obj='srm.offers'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

class srm_offer_deadlines(Model):
	_name = 'srm.offer.deadlines'
	_description = 'General SRM Offer Deadlines'
	_order_by = 'start_date asc'
	_columns = {
	'offer_id': fields.many2one(label = 'Offer',obj='srm.offers',on_delete='c',on_update='c'),
	'sequence':fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Type',obj='srm.deadlines',on_delete='n',on_update='n'),
	'start_date': fields.datetime(label='Start',required=True),
	'end_date': fields.datetime(label='End',required=True),
	'required': fields.boolean(label='Required'),
	'note': fields.text('Note')}

srm_offer_deadlines()

class srm_offer_pricing(Model):
	_name = 'srm.offer.pricing'
	_description = 'SRM Offer Pricing'
	_columns = {
	'offer_id': fields.many2one(label = 'Offer',obj='srm.offers'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','srm')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_offer_pricing()

class srm_offer_payment_schedules(Model):
	_name = 'srm.offer.payment.schedules'
	_description = 'SRM Offer Payment Schedules'
	_columns = {
	'offer_id': fields.many2one(label = 'Offer',obj='srm.offers'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_offer_payment_schedules()

class srm_offer_items(Model):
	_name = 'srm.offer.items'
	_description = 'General SRM Offer Item'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'offer_id': fields.many2one(obj = 'srm.offers',label = 'Offer',on_delete='c',on_update='c'),
	'product': fields.many2one(label='Product',obj='md.product',on_delete='n',on_update='n',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='VAT Code',obj='md.vat.code',on_delete='n',on_update='n',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'currency_id': fields.many2one(label='Currency',obj='md.currency',on_delete='n',on_update='n'),
	'delivery_schedules': fields.one2many(label='Delivery Schedules',obj='srm.offer.item.delivery.schedules',rel='item_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.offer.pricing.items',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='srm.offer.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='srm.offer.item.texts',rel='item_id'),
	'plates': fields.one2many(label='Plates',obj='srm.offer.item.output.plates',rel='item_id'),
	'payments': fields.one2many(label='Payments',obj='srm.offer.item.payment.schedules',rel='item_id'),
	'note': fields.text('Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.srm.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
			if len(p) > 0:
				if item['vat_code'] != p[0]['vat']:
					item['vat_code'] = p[0]['vat']				
				for f in ('uom','price','currency','unit','uop'):
					if item[f] != p[0][f]:
						item[f] = p[0][f]

		return None

	_default = {
		'quantity': 1,
		'unit': 1
	}

srm_offer_items()

class srm_offer_pricing_items(Model):
	_name = 'srm.offer.pricing.items'
	_description = 'Offer Item Pricing'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.offer.items'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','p')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'cop': fields.many2one(label='Currency Of Price',obj='md.currency',required=True),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_offer_pricing_items()


class srm_offer_item_texts(Model):
	_name = 'srm.offer.item.texts'
	_description = 'SRM Offer Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='srm.offer.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_offer_item_texts()

class srm_offer_item_roles(Model):
	_name = 'srm.offer.item.roles'
	_description = 'SRM Offer Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.offer.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_offer_item_roles()

class srm_offer_item_delivery_schedules(Model):
	_name = 'srm.offer.item.delivery.schedules'
	_description = 'General SRM Offer Delivery Schedules'
	_date = "schedule"
	_columns = {
	'item_id': fields.many2one(obj = 'srm.offer.items',label = 'Item',on_delete='c',on_update='c'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom',on_delete='n',on_update='n'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')}

srm_offer_item_delivery_schedules()

class srm_offer_item_output_plates(Model):
	_name = 'srm.offer.item.output.plates'
	_description = 'Offer Item Output Plates'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.offer.items'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

srm_offer_item_output_plates()

class srm_offer_item_payment_schedules(Model):
	_name = 'srm.offer.item.payment.schedules'
	_description = 'Offer Item Payment Schedules'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.offer.items'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_offer_item_payment_schedules()

# SRM Evolution
# Types & Roles
class srm_evolution_types(Model):
	_name = 'srm.evolution.types'
	_description = 'Types SRM Evolution'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='srm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='srm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='srm.evolution.type.roles',rel='type_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.evolution.type.deadlines',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

srm_evolution_types()

class srm_evolution_type_roles(Model):
	_name = 'srm.evolution.type.roles'
	_description = 'Role SRM Evolution Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.evolution.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_evolution_type_roles()

class srm_evolution_type_deadlines(Model):
	_name = 'srm.evolution.type.deadlines'
	_description = 'Deadlines SRM Evolution Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.evolution.types'),
	'sequence': fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Deadline',obj='srm.deadlines'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_evolution_type_deadlines()

class srm_evolution_type_plates(Model):
	_name = 'srm.evolution.type.plates'
	_description = 'SRM Evolution Plates'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.evolution.types'),
	'seq': fields.integer(label='Sequence',required=True),
	'plate': fields.many2one(label = 'Plate',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_evolution_type_plates()


class srm_evolution_type_items(Model):
	_name = 'srm.evolution.type.items'
	_description = 'Type of SRM Evolution Items'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.evolution.types'),
	'gti_id': fields.many2one(label = 'GTI',obj='md.gtis'),
	'itype_id': fields.many2one(label = 'Type Of Items',obj='md.type.items',domain=[('usage','=','p'),'|',('usage','=','a')]),
	'note': fields.text(label = 'Note')
	}

srm_evolution_type_items()



# Types & Roles
#
class srm_evolutions(Model):
	_name = 'srm.evolutions'
	_description = 'General SRM Evolution'
	_inherits = {'srm.common':{'_methods':['copy_into','copy_from','_compute_fullname'],'_actions':['merge']},'common.model':{'_methods':['_calculate_amount_costs']}}
	_rec_name = 'fullname'
	_date = 'doe'
	_columns = {
	'etype': fields.many2one(label='Type',obj='srm.evolution.types',on_change='_on_change_etype'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'name': fields.varchar(label = 'Name'),
	'fullname': fields.composite(label='Full Name',cols=['etype','company','name'],translate = True,required = True, compute = '_compute_composite'),
	'market': fields.many2one(label='Market',obj='srm.markets'),
	'team': fields.many2one(label='Team',obj='srm.teams'),
	'category_id': fields.many2one(label='Category',obj='srm.evolution.category'),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'origin': fields.varchar(label = 'Origin'),
	'doe': fields.date(label='Date Of Evolution',required=True),
	'from_date': fields.date(label='From Date Of Evolution',required=True),
	'to_date': fields.date(label='To Date Of Evolution',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',on_delete='n',on_update='n',domain=[('issuplier',)]),
	'route_id': fields.many2one(label='Route',obj='srm.routes',on_delete='n',on_update='n'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'bom': fields.many2one(label='BoM',obj='md.boms',domain=[('usage','=','srm'),'|',('usage','=','all')],on_change='_on_change_bom'),
	'items': fields.one2many(label='Items',obj='srm.evolution.items',rel='evolution_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.evolution.pricing',rel='evolution_id'),
	'roles': fields.one2many(label='Roles',obj='srm.evolution.roles',rel='evolution_id'),
	'texts': fields.one2many(label='Texts',obj='srm.evolution.texts',rel='evolution_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.evolution.deadlines',rel='evolution_id'),
	'plates': fields.one2many(label='Plates',obj='srm.evolution.output.plates',rel='evolution_id'),
	'payments': fields.one2many(label='Payments',obj='srm.evolution.payment.schedules',rel='evolution_id'),
	'note': fields.text('Note')}
	
	def _on_change_etype(self,cr,pool,uid,item,context={}):		
		roles = pool.get('srm.evolution.type.roles').select(cr,pool,uid,['role_id'],[('type_id','=',item['etype']['name'])],context)
		for role in roles:
			item_role = pool.get('srm.evolution.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)

		deadlines = pool.get('srm.evolution.type.deadlines').select(cr,pool,uid,['sequence','deadline_id','required'],[('type_id','=',item['etype']['name'])],context)
		for deadline in deadlines:
			item_deadline = pool.get('srm.evolution.deadlines')._buildEmptyItem()
			item_deadline['sequence'] = deadline['sequence']
			item_deadline['deadline_id'] = deadline['deadline_id']
			item_deadline['required'] = deadline['required']
			item['deadlines'].append(item_deadline)
		
		types = pool.get('srm.evolution.types').select(cr,pool,uid,['htschema'],[('name','=',item['dtype']['name'])],context)	
		texts1 = pool.get('srm.schema.texts').select(cr,pool,uid,['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = pool.get('srm.evolution.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

	def _on_change_bom(self,cr,pool,uid,item,context={}):		
		if item['bom'] and 'name' in item['bom'] and item['bom']['name']:
			p = pool.get('md.bom.input.items').select(cr,pool,uid,['product','quantity','uom'],[('bom_id','=',item['bom']['name'])],context)
			for i in p:
				ei = pool.get('purchase.order.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.now().astimezone()+timedelta(3)
				item_items = pool.get('purchase.order.items')._buildEmptyItem()
				item_items['delivery_schedules'].append(ei)
				for f in ('product','uom'):
					item_items[f] = i[f]
				item_items['price'] = 0.00
				item['items'].append(item_items)

		return None

srm_evolutions()

class srm_evolution_texts(Model):
	_name = 'srm.evolution.texts'
	_description = 'SRM Evolution Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'evolution_id': fields.many2one(label='Evolution',obj='srm.evolutions'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_evolution_texts()


class srm_evolution_roles(Model):
	_name = 'srm.evolution.roles'
	_description = 'SRM Evolution Roles'
	_columns = {
	'evolution_id': fields.many2one(label = 'Evolution',obj='srm.evolutions'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_evolution_roles()

class srm_evolution_output_plates(Model):
	_name = 'srm.evolution.output.plates'
	_description = 'SRM Evolution Output Plates'
	_columns = {
	'evolution_id': fields.many2one(label = 'Evolution',obj='srm.evolutions'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

class srm_evolution_deadlines(Model):
	_name = 'srm.evolution.deadlines'
	_description = 'General SRM Evolution Deadlines'
	_order_by = 'start_date asc'
	_columns = {
	'evolution_id': fields.many2one(label = 'Evolution',obj='srm.evolutions',on_delete='c',on_update='c'),
	'sequence':fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Type',obj='srm.deadlines',on_delete='n',on_update='n'),
	'start_date': fields.datetime(label='Start',required=True),
	'end_date': fields.datetime(label='End',required=True),
	'required': fields.boolean(label='Required'),
	'note': fields.text('Note')}

srm_evolution_deadlines()

class srm_evolution_pricing(Model):
	_name = 'srm.evolution.pricing'
	_description = 'SRM Evolution Pricing'
	_columns = {
	'evolution_id': fields.many2one(label = 'Evolution',obj='srm.evolutions'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','srm')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_evolution_pricing()

class srm_evolution_payment_schedules(Model):
	_name = 'srm.evolution.payment.schedules'
	_description = 'SRM Evolution Payment Schedules'
	_columns = {
	'evolution_id': fields.many2one(label = 'Evolution',obj='srm.evolutions'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_evolution_payment_schedules()

class srm_evolution_items(Model):
	_name = 'srm.evolution.items'
	_description = 'General SRM Evolution Item'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'evolution_id': fields.many2one(obj = 'srm.evolutions',label = 'Evolution',on_delete='c',on_update='c'),
	'product': fields.many2one(label='Product',obj='md.product',on_delete='n',on_update='n',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='VAT Code',obj='md.vat.code',on_delete='n',on_update='n',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'currency_id': fields.many2one(label='Currency',obj='md.currency',on_delete='n',on_update='n'),
	'delivery_schedules': fields.one2many(label='Delivery Schedules',obj='srm.evolution.item.delivery.schedules',rel='item_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.evolution.pricing.items',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='srm.evolution.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='srm.evolution.item.texts',rel='item_id'),
	'plates': fields.one2many(label='Plates',obj='srm.evolution.item.output.plates',rel='item_id'),
	'payments': fields.one2many(label='Payments',obj='srm.evolution.item.payment.schedules',rel='item_id'),
	'note': fields.text('Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.srm.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
			if len(p) > 0:
				if item['vat_code'] != p[0]['vat']:
					item['vat_code'] = p[0]['vat']				
				for f in ('uom','price','currency','unit','uop'):
					if item[f] != p[0][f]:
						item[f] = p[0][f]

		return None

	_default = {
		'quantity': 1,
		'unit': 1
	}

srm_evolution_items()

class srm_evolution_pricing_items(Model):
	_name = 'srm.evolution.pricing.items'
	_description = 'Evolution Item Pricing'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.evolution.items'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','p')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'cop': fields.many2one(label='Currency Of Price',obj='md.currency',required=True),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_evolution_pricing_items()


class srm_evolution_item_texts(Model):
	_name = 'srm.evolution.item.texts'
	_description = 'SRM Evolution Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='srm.evolution.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_evolution_item_texts()

class srm_evolution_item_roles(Model):
	_name = 'srm.evolution.item.roles'
	_description = 'SRM Evolution Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.evolution.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_evolution_item_roles()

class srm_evolution_item_delivery_schedules(Model):
	_name = 'srm.evolution.item.delivery.schedules'
	_description = 'General SRM Evolution Delivery Schedules'
	_date = "schedule"
	_columns = {
	'item_id': fields.many2one(obj = 'srm.evolution.items',label = 'Item',on_delete='c',on_update='c'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom',on_delete='n',on_update='n'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')}

srm_evolution_item_delivery_schedules()

class srm_evolution_item_output_plates(Model):
	_name = 'srm.evolution.item.output.plates'
	_description = 'Evolution Item Output Plates'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.evolution.items'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

srm_evolution_item_output_plates()

class srm_evolution_item_payment_schedules(Model):
	_name = 'srm.evolution.item.payment.schedules'
	_description = 'Evolution Item Payment Schedules'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.evolution.items'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_evolution_item_payment_schedules()

# SRM Decision
# Types & Roles
class srm_decision_types(Model):
	_name = 'srm.decision.types'
	_description = 'Types SRM Decision'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='srm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='srm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='srm.decision.type.roles',rel='type_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.decision.type.deadlines',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

srm_decision_types()

class srm_decision_type_roles(Model):
	_name = 'srm.decision.type.roles'
	_description = 'Role SRM Decision Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.decision.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_decision_type_roles()

class srm_decision_type_deadlines(Model):
	_name = 'srm.decision.type.deadlines'
	_description = 'Deadlines SRM Decision Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.decision.types'),
	'sequence': fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Deadline',obj='srm.deadlines'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_decision_type_deadlines()

class srm_decision_type_plates(Model):
	_name = 'srm.decision.type.plates'
	_description = 'SRM Decision Plates'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.decision.types'),
	'seq': fields.integer(label='Sequence',required=True),
	'plate': fields.many2one(label = 'Plate',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_decision_type_plates()


class srm_decision_type_items(Model):
	_name = 'srm.decision.type.items'
	_description = 'Type of SRM Decision Items'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.decision.types'),
	'gti_id': fields.many2one(label = 'GTI',obj='md.gtis'),
	'itype_id': fields.many2one(label = 'Type Of Items',obj='md.type.items',domain=[('usage','=','p'),'|',('usage','=','a')]),
	'note': fields.text(label = 'Note')
	}

srm_decision_type_items()



# Types & Roles
#
class srm_decisions(Model):
	_name = 'srm.decisions'
	_description = 'General SRM Decision'
	_inherits = {'srm.common':{'_methods':['copy_into','copy_from','_compute_fullname'],'_actions':['merge']},'common.model':{'_methods':['_calculate_amount_costs']}}
	_rec_name = 'fullname'
	_date = 'dod'
	_columns = {
	'dtype': fields.many2one(label='Type',obj='srm.decision.types',on_change='_on_change_dtype'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'name': fields.varchar(label = 'Name'),
	'fullname': fields.composite(label='Full Name',cols=['dtype','company','name'],translate = True,required = True, compute = '_compute_composite'),
	'market': fields.many2one(label='Market',obj='srm.markets'),
	'team': fields.many2one(label='Team',obj='srm.teams'),
	'category_id': fields.many2one(label='Category',obj='srm.decision.category'),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'origin': fields.varchar(label = 'Origin'),
	'dod': fields.date(label='Date Of Decision',required=True),
	'from_date': fields.date(label='From Date Of Decision',required=True),
	'to_date': fields.date(label='To Date Of Decision',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',on_delete='n',on_update='n',domain=[('issuplier',)]),
	'route_id': fields.many2one(label='Route',obj='srm.routes',on_delete='n',on_update='n'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'bom': fields.many2one(label='BoM',obj='md.boms',domain=[('usage','=','srm'),'|',('usage','=','all')],on_change='_on_change_bom'),
	'items': fields.one2many(label='Items',obj='srm.decision.items',rel='decision_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.decision.pricing',rel='decision_id'),
	'roles': fields.one2many(label='Roles',obj='srm.decision.roles',rel='decision_id'),
	'texts': fields.one2many(label='Texts',obj='srm.decision.texts',rel='decision_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.decision.deadlines',rel='decision_id'),
	'plates': fields.one2many(label='Plates',obj='srm.decision.output.plates',rel='decision_id'),
	'payments': fields.one2many(label='Payments',obj='srm.decision.payment.schedules',rel='decision_id'),
	'note': fields.text('Note')}
	
	def _on_change_dtype(self,cr,pool,uid,item,context={}):		
		roles = pool.get('srm.decision.type.roles').select(cr,pool,uid,['role_id'],[('type_id','=',item['dtype']['name'])],context)
		for role in roles:
			item_role = pool.get('srm.decision.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)

		deadlines = pool.get('srm.decision.type.deadlines').select(cr,pool,uid,['sequence','deadline_id','required'],[('type_id','=',item['dtype']['name'])],context)
		for deadline in deadlines:
			item_deadline = pool.get('srm.decision.deadlines')._buildEmptyItem()
			item_deadline['sequence'] = deadline['sequence']
			item_deadline['deadline_id'] = deadline['deadline_id']
			item_deadline['required'] = deadline['required']
			item['deadlines'].append(item_deadline)
		
		types = pool.get('srm.decision.types').select(cr,pool,uid,['htschema'],[('name','=',item['dtype']['name'])],context)	
		texts1 = pool.get('srm.schema.texts').select(cr,pool,uid,['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = pool.get('srm.decision.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

	def _on_change_bom(self,cr,pool,uid,item,context={}):		
		if item['bom'] and 'name' in item['bom'] and item['bom']['name']:
			p = pool.get('md.bom.input.items').select(cr,pool,uid,['product','quantity','uom'],[('bom_id','=',item['bom']['name'])],context)
			for i in p:
				ei = pool.get('purchase.order.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.now().astimezone()+timedelta(3)
				item_items = pool.get('purchase.order.items')._buildEmptyItem()
				item_items['delivery_schedules'].append(ei)
				for f in ('product','uom'):
					item_items[f] = i[f]
				item_items['price'] = 0.00
				item['items'].append(item_items)

		return None

srm_decisions()

class srm_decision_texts(Model):
	_name = 'srm.decision.texts'
	_description = 'SRM Decision Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'decision_id': fields.many2one(label='Decision',obj='srm.decisions'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_decision_texts()


class srm_decision_roles(Model):
	_name = 'srm.decision.roles'
	_description = 'SRM Decision Roles'
	_columns = {
	'decision_id': fields.many2one(label = 'Decision',obj='srm.decisions'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_decision_roles()

class srm_decision_output_plates(Model):
	_name = 'srm.decision.output.plates'
	_description = 'SRM Decision Output Plates'
	_columns = {
	'decision_id': fields.many2one(label = 'Decision',obj='srm.decisions'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

class srm_decision_deadlines(Model):
	_name = 'srm.decision.deadlines'
	_description = 'General SRM Decision Deadlines'
	_order_by = 'start_date asc'
	_columns = {
	'decision_id': fields.many2one(label = 'Decision',obj='srm.decisions',on_delete='c',on_update='c'),
	'sequence':fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Type',obj='srm.deadlines',on_delete='n',on_update='n'),
	'start_date': fields.datetime(label='Start',required=True),
	'end_date': fields.datetime(label='End',required=True),
	'required': fields.boolean(label='Required'),
	'note': fields.text('Note')}

srm_decision_deadlines()

class srm_decision_pricing(Model):
	_name = 'srm.decision.pricing'
	_description = 'SRM Decision Pricing'
	_columns = {
	'decision_id': fields.many2one(label = 'Decision',obj='srm.decisions'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','srm')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_decision_pricing()

class srm_decision_payment_schedules(Model):
	_name = 'srm.decision.payment.schedules'
	_description = 'SRM Decision Payment Schedules'
	_columns = {
	'decision_id': fields.many2one(label = 'Decision',obj='srm.decisions'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_decision_payment_schedules()

class srm_decision_items(Model):
	_name = 'srm.decision.items'
	_description = 'General SRM Decision Item'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'decision_id': fields.many2one(obj = 'srm.decisions',label = 'Decision',on_delete='c',on_update='c'),
	'product': fields.many2one(label='Product',obj='md.product',on_delete='n',on_update='n',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='VAT Code',obj='md.vat.code',on_delete='n',on_update='n',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'currency_id': fields.many2one(label='Currency',obj='md.currency',on_delete='n',on_update='n'),
	'delivery_schedules': fields.one2many(label='Delivery Schedules',obj='srm.decision.item.delivery.schedules',rel='item_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.decision.pricing.items',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='srm.decision.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='srm.decision.item.texts',rel='item_id'),
	'plates': fields.one2many(label='Plates',obj='srm.decision.item.output.plates',rel='item_id'),
	'payments': fields.one2many(label='Payments',obj='srm.decision.item.payment.schedules',rel='item_id'),
	'note': fields.text('Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.srm.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
			if len(p) > 0:
				if item['vat_code'] != p[0]['vat']:
					item['vat_code'] = p[0]['vat']				
				for f in ('uom','price','currency','unit','uop'):
					if item[f] != p[0][f]:
						item[f] = p[0][f]

		return None

	_default = {
		'quantity': 1,
		'unit': 1
	}

srm_decision_items()

class srm_decision_pricing_items(Model):
	_name = 'srm.decision.pricing.items'
	_description = 'Decision Item Pricing'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.decision.items'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','p')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'cop': fields.many2one(label='Currency Of Price',obj='md.currency',required=True),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_decision_pricing_items()


class srm_decision_item_texts(Model):
	_name = 'srm.decision.item.texts'
	_description = 'SRM Decision Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='srm.decision.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_decision_item_texts()

class srm_decision_item_roles(Model):
	_name = 'srm.decision.item.roles'
	_description = 'SRM Decision Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.decision.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_decision_item_roles()

class srm_decision_item_delivery_schedules(Model):
	_name = 'srm.decision.item.delivery.schedules'
	_description = 'General SRM Decision Delivery Schedules'
	_date = "schedule"
	_columns = {
	'item_id': fields.many2one(obj = 'srm.decision.items',label = 'Item',on_delete='c',on_update='c'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom',on_delete='n',on_update='n'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')}

srm_decision_item_delivery_schedules()

class srm_decision_item_output_plates(Model):
	_name = 'srm.decision.item.output.plates'
	_description = 'Decision Item Output Plates'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.decision.items'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

srm_decision_item_output_plates()

class srm_decision_item_payment_schedules(Model):
	_name = 'srm.decision.item.payment.schedules'
	_description = 'Decision Item Payment Schedules'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.decision.items'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_decision_item_payment_schedules()

# SRM Contract
# Types & Roles
class srm_contract_types(Model):
	_name = 'srm.contract.types'
	_description = 'Types SRM Contract'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='srm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='srm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='srm.contract.type.roles',rel='type_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.contract.type.deadlines',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

srm_contract_types()

class srm_contract_type_roles(Model):
	_name = 'srm.contract.type.roles'
	_description = 'Role SRM Contract Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.contract.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_contract_type_roles()

class srm_contract_type_deadlines(Model):
	_name = 'srm.contract.type.deadlines'
	_description = 'Deadlines SRM Contract Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.contract.types'),
	'sequence': fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Deadline',obj='srm.deadlines'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_contract_type_deadlines()

class srm_contract_type_plates(Model):
	_name = 'srm.contract.type.plates'
	_description = 'SRM Contract Plates'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.contract.types'),
	'seq': fields.integer(label='Sequence',required=True),
	'plate': fields.many2one(label = 'Plate',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_contract_type_plates()


class srm_contract_type_items(Model):
	_name = 'srm.contract.type.items'
	_description = 'Type of SRM Contract Items'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.contract.types'),
	'gti_id': fields.many2one(label = 'GTI',obj='md.gtis'),
	'itype_id': fields.many2one(label = 'Type Of Items',obj='md.type.items',domain=[('usage','=','p'),'|',('usage','=','a')]),
	'note': fields.text(label = 'Note')
	}

srm_contract_type_items()



# Types & Roles
#
class srm_contracts(Model):
	_name = 'srm.contracts'
	_description = 'General SRM Contract'
	_inherits = {'srm.common':{'_methods':['copy_into','copy_from','_compute_fullname'],'_actions':['merge']},'common.model':{'_methods':['_calculate_amount_costs']}}
	_rec_name = 'fullname'
	_date = 'doc'
	_columns = {
	'ctype': fields.many2one(label='Type',obj='srm.contract.types',on_change='_on_change_ctype'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'name': fields.varchar(label = 'Name'),
	'fullname': fields.composite(label='Full Name',cols=['ctype','company','name'],translate = True,required = True, compute = '_compute_composite'),
	'market': fields.many2one(label='Market',obj='srm.markets'),
	'team': fields.many2one(label='Team',obj='srm.teams'),
	'category_id': fields.many2one(label='Category',obj='srm.contract.category'),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'origin': fields.varchar(label = 'Origin'),
	'doc': fields.date(label='Date Of Contract',required=True),
	'from_date': fields.date(label='From Date Of Contract',required=True),
	'to_date': fields.date(label='To Date Of Contract',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',on_delete='n',on_update='n',domain=[('issuplier',)]),
	'route_id': fields.many2one(label='Route',obj='srm.routes',on_delete='n',on_update='n'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'bom': fields.many2one(label='BoM',obj='md.boms',domain=[('usage','=','srm'),'|',('usage','=','all')],on_change='_on_change_bom'),
	'items': fields.one2many(label='Items',obj='srm.contract.items',rel='contract_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.contract.pricing',rel='contract_id'),
	'roles': fields.one2many(label='Roles',obj='srm.contract.roles',rel='contract_id'),
	'texts': fields.one2many(label='Texts',obj='srm.contract.texts',rel='contract_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.contract.deadlines',rel='contract_id'),
	'plates': fields.one2many(label='Plates',obj='srm.contract.output.plates',rel='contract_id'),
	'payments': fields.one2many(label='Payments',obj='srm.contract.payment.schedules',rel='contract_id'),
	'note': fields.text('Note')}
	
	def _on_change_ctype(self,cr,pool,uid,item,context={}):		
		roles = pool.get('srm.contract.type.roles').select(cr,pool,uid,['role_id'],[('type_id','=',item['ctype']['name'])],context)
		for role in roles:
			item_role = pool.get('srm.contract.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)

		deadlines = pool.get('srm.contract.type.deadlines').select(cr,pool,uid,['sequence','deadline_id','required'],[('type_id','=',item['ctype']['name'])],context)
		for deadline in deadlines:
			item_deadline = pool.get('srm.contract.deadlines')._buildEmptyItem()
			item_deadline['sequence'] = deadline['sequence']
			item_deadline['deadline_id'] = deadline['deadline_id']
			item_deadline['required'] = deadline['required']
			item['deadlines'].append(item_deadline)
		
		types = pool.get('srm.contract.types').select(cr,pool,uid,['htschema'],[('name','=',item['dtype']['name'])],context)	
		texts1 = pool.get('srm.schema.texts').select(cr,pool,uid,['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = pool.get('srm.contract.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

	def _on_change_bom(self,cr,pool,uid,item,context={}):		
		if item['bom'] and 'name' in item['bom'] and item['bom']['name']:
			p = pool.get('md.bom.input.items').select(cr,pool,uid,['product','quantity','uom'],[('bom_id','=',item['bom']['name'])],context)
			for i in p:
				ei = pool.get('purchase.order.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.now().astimezone()+timedelta(3)
				item_items = pool.get('purchase.order.items')._buildEmptyItem()
				item_items['delivery_schedules'].append(ei)
				for f in ('product','uom'):
					item_items[f] = i[f]
				item_items['price'] = 0.00
				item['items'].append(item_items)

		return None

srm_contracts()

class srm_contract_texts(Model):
	_name = 'srm.contract.texts'
	_description = 'SRM Contract Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'contract_id': fields.many2one(label='Contract',obj='srm.contracts'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_contract_texts()


class srm_contract_roles(Model):
	_name = 'srm.contract.roles'
	_description = 'SRM Contract Roles'
	_columns = {
	'contract_id': fields.many2one(label = 'Contract',obj='srm.contracts'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_contract_roles()

class srm_contract_output_plates(Model):
	_name = 'srm.contract.output.plates'
	_description = 'SRM Contract Output Plates'
	_columns = {
	'contract_id': fields.many2one(label = 'Contract',obj='srm.contracts'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

class srm_contract_deadlines(Model):
	_name = 'srm.contract.deadlines'
	_description = 'General SRM Contract Deadlines'
	_order_by = 'start_date asc'
	_columns = {
	'contract_id': fields.many2one(label = 'Contract',obj='srm.contracts',on_delete='c',on_update='c'),
	'sequence':fields.integer(label='Sequence'),
	'deadline_id': fields.many2one(label = 'Type',obj='srm.deadlines',on_delete='n',on_update='n'),
	'start_date': fields.datetime(label='Start',required=True),
	'end_date': fields.datetime(label='End',required=True),
	'required': fields.boolean(label='Required'),
	'note': fields.text('Note')}

srm_contract_deadlines()

class srm_contract_pricing(Model):
	_name = 'srm.contract.pricing'
	_description = 'SRM Contract Pricing'
	_columns = {
	'contract_id': fields.many2one(label = 'Contract',obj='srm.contracts'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','srm')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_contract_pricing()

class srm_contract_payment_schedules(Model):
	_name = 'srm.contract.payment.schedules'
	_description = 'SRM Contract Payment Schedules'
	_columns = {
	'contract_id': fields.many2one(label = 'Contract',obj='srm.contracts'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_contract_payment_schedules()

class srm_contract_items(Model):
	_name = 'srm.contract.items'
	_description = 'General SRM Contract Item'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'contract_id': fields.many2one(obj = 'srm.contracts',label = 'Contract',on_delete='c',on_update='c'),
	'product': fields.many2one(label='Product',obj='md.product',on_delete='n',on_update='n',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='VAT Code',obj='md.vat.code',on_delete='n',on_update='n',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'currency_id': fields.many2one(label='Currency',obj='md.currency',on_delete='n',on_update='n'),
	'delivery_schedules': fields.one2many(label='Delivery Schedules',obj='srm.contract.item.delivery.schedules',rel='item_id'),
	'pricing': fields.one2many(label='Pricing',obj='srm.contract.pricing.items',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='srm.contract.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='srm.contract.item.texts',rel='item_id'),
	'plates': fields.one2many(label='Plates',obj='srm.contract.item.output.plates',rel='item_id'),
	'payments': fields.one2many(label='Payments',obj='srm.contract.item.payment.schedules',rel='item_id'),
	'note': fields.text('Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.srm.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
			if len(p) > 0:
				if item['vat_code'] != p[0]['vat']:
					item['vat_code'] = p[0]['vat']				
				for f in ('uom','price','currency','unit','uop'):
					if item[f] != p[0][f]:
						item[f] = p[0][f]

		return None

	_default = {
		'quantity': 1,
		'unit': 1
	}

srm_contract_items()

class srm_contract_pricing_items(Model):
	_name = 'srm.contract.pricing.items'
	_description = 'Contract Item Pricing'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.contract.items'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','p')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='srm.pricing.group.levels'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'cop': fields.many2one(label='Currency Of Price',obj='md.currency',required=True),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

srm_contract_pricing_items()


class srm_contract_item_texts(Model):
	_name = 'srm.contract.item.texts'
	_description = 'SRM Contract Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='srm.contract.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_contract_item_texts()

class srm_contract_item_roles(Model):
	_name = 'srm.contract.item.roles'
	_description = 'SRM Contract Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.contract.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_contract_item_roles()

class srm_contract_item_delivery_schedules(Model):
	_name = 'srm.contract.item.delivery.schedules'
	_description = 'General SRM Contract Delivery Schedules'
	_date = "schedule"
	_columns = {
	'item_id': fields.many2one(obj = 'srm.contract.items',label = 'Item',on_delete='c',on_update='c'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom',on_delete='n',on_update='n'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')}

srm_contract_item_delivery_schedules()

class srm_contract_item_output_plates(Model):
	_name = 'srm.contract.item.output.plates'
	_description = 'Contract Item Output Plates'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.contract.items'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

srm_contract_item_output_plates()

class srm_contract_item_payment_schedules(Model):
	_name = 'srm.contract.item.payment.schedules'
	_description = 'Contract Item Payment Schedules'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.contract.items'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_contract_item_payment_schedules()

# SRM Other
class srm_blacklist_partner(Model):
	_name = 'srm.blacklist.partner'
	_description = 'General SRM Partner Blacklist'
	_columns = {
	'name': fields.varchar(label = 'Blacklist Parnter',domain=[('issuplier',)]),
	'partner_id': fields.many2one(label='Partner',obj='md.partner'),
	'dateofentry': fields.datetime(label='Date Of Entry'),
	'note': fields.text('Note')}
	
srm_blacklist_partner()

class srm_partner_validation(Model):
	_name = 'srm.partner.validation'
	_description = 'General SRM Partner Validation'
	_columns = {
	'name': fields.varchar(label = 'Validation Partner'),
	'partner_id': fields.many2one(label='Partner',obj='md.partner',domain=[('issuplier',)]),
	'categories': fields.one2many(label='Categories',obj='srm.partner.validation.category',rel='partner_validation_id'),
	'products': fields.one2many(label='Products',obj='srm.partner.validation.product',rel='partner_validation_id')}

srm_partner_validation()

class srm_partner_validation_category(Model):
	_name = 'srm.partner.validation.category'
	_description = 'General SRM Partner Validation Category'
	_columns = {
	'partner_validation_id': fields.many2one(label='Partner',obj='srm.partner.validation'),
	'category_product_id': fields.many2one(label='Product Category',obj='md.category.product'),
	'validationof': fields.datetime(label='Category Date Of Validation'),
	'nextvalidationof': fields.datetime(label='Category Next Validation'),
	'note': fields.text('Note')
	}

srm_partner_validation_category()

class srm_partner_validation_product(Model):
	_name = 'srm.partner.validation.product'
	_description = 'General SRM Partner Validation Product'
	_columns = {
	'partner_validation_id': fields.many2one(label='Partner',obj='srm.partner.validation'),
	'product_id': fields.many2one(label='Product',obj='md.product'),
	'validationof': fields.datetime(label='Product Date Of Validation'),
	'nextvalidationof': fields.datetime(label='Product Next Validation'),
	'note': fields.text('Note')
	}

srm_partner_validation_product()

class srm_product_source_supply(Model):
	_name = 'srm.product.source.supply'
	_description = 'General SRM Partner Source Of Supply'
	_columns = {
	'name': fields.varchar(label = 'Product Source Supply'),
	'partner_id': fields.many2one(label='Partner',obj='md.partner',domain=[('issuplier',)]),
	'products_id': fields.many2one(label='Products',obj='md.product'),
	'validfrom':  fields.datetime(label='Valid From'),
	'validfto':  fields.datetime(label='Valid To')
	}

srm_product_source_supply()

class srm_common_product(ModelInherit):
	_name = 'srm.common.product'
	_description = 'SRM Common Product'
	_inherit = {'md.product':{'_columns':['ppvs']},'md.partner':{'_columns':['pssv']}}
	_columns = {
	'ppvs': fields.one2many(label='Partner Validation Product',obj='srm.partner.validation.product',rel='product_id',readonly=True),
	'pssv': fields.one2many(label='Partner Source Of Supply',obj='srm.product.source.supply',rel='partner_id',readonly=True)
	}

srm_common_product()

class md_srm_product(Model):
	_name = 'md.srm.product'
	_description = 'SRM Of Product'
	_columns = {
	'product_id': fields.many2one(label='Product',obj='md.product'),
	'vat': fields.many2one(label='VAT Code',obj='md.vat.code',domain=[('type_vat','in',('p','n'))]),
	'uom': fields.many2one(label="Unit Of Measure",obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'note': fields.text(label = 'Note'),
	}

md_srm_product()

class md_srm_product_inherit(ModelInherit):
	_name = 'md.srm.product.inherit'
	_description = 'Genaral Model Inherit For SRM Product'
	_inherit = {'md.product':{'_columns':['srm']},'md.boms':{'_columns':['usage']},'seq.conditions':{'_columns':['usage']},'seq.access.schemas':{'_columns':['usage']},'seq.access':{'_columns':['usage']},'md.type.items':{'_columns':['usage']},'md.type.plates':{'_columns':['usage']}}
	_columns = {
		'srm': fields.one2many(label='SRM',obj='md.srm.product',rel='product_id'),
		'usage': fields.iProperty(selections=[('srm','SRM')])
	}
	
md_srm_product_inherit()
