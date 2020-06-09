from gsrp5service.orm import fields
from gsrp5service.orm.model import Model,ModelInherit

from decimal import Decimal

from datetime import datetime
from datetime import timedelta

# Customize
# Organization
class ctrm_channels(Model):
	_name = 'ctrm.channels'
	_description = 'CTRM Cannels'
	_row_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'sectors': fields.one2many(label='Sectors',obj='ctrm.sectors',rel='channel_id')
	}

ctrm_channels()

class ctrm_sectors(Model):
	_name = 'ctrm.sectors'
	_description = 'CTRM Sectors'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'channel_id': fields.many2one(label='Channel',obj='ctrm.channels'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

ctrm_sectors()

class ctrm_teams(Model):
	_name = 'ctrm.teams'
	_description = 'CTRM Teams'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'groups': fields.one2many(label='Groups',obj='ctrm.groups',rel='team_id')
	}

ctrm_teams()

class ctrm_groups(Model):
	_name = 'ctrm.groups'
	_description = 'CTRM Groups'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'team_id': fields.many2one(label='Group',obj='ctrm.teams'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

ctrm_groups()

# Organization end
# Text
class ctrm_texts(Model):
	_name = 'ctrm.texts'
	_description = 'CTRM Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

ctrm_texts()

class ctrm_schema_texts(Model):
	_name = 'ctrm.schema.texts'
	_description = 'Schema Of CTRM Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'usage': fields.selection(label='Usage',selections=[('h','Header'),('i','Item'),('b','Both')]),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'texts': fields.one2many(label='Texts',obj='ctrm.schema.text.items',rel='schema_id')
	}
	
	_default = {
		'usage':'b'
	}

ctrm_schema_texts()

class ctrm_schema_text_items(Model):
	_name = 'ctrm.schema.text.items'
	_description = 'Items Of Schema CTRM Texts'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'schema_id': fields.many2one(label = 'Schema',obj='ctrm.schema.texts'),
	'text_id': fields.many2one(label = 'Text',obj='ctrm.texts'),
	'descr': fields.referenced(ref='text_id.descr')
	}

ctrm_schema_text_items()

# Text end
class ctrm_origin_quotes(Model):
	_name = 'ctrm.origin.quotes'
	_description = 'Orgigin Quotes of CTRM'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'schema_id': fields.many2one(label = 'Schema',obj='ctrm.schema.texts'),
	'text_id': fields.many2one(label = 'Text',obj='ctrm.texts'),
	'descr': fields.referenced(ref='text_id.descr')
	}

ctrm_origin_quotes	()

# Master data


# Master data end

class ctrm_request_types(Model):
	_name = 'ctrm.request.types'
	_description = 'Types CTRM Request'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='ctrm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='ctrm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='ctrm.request.type.roles',rel='type_id'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

ctrm_request_types()

class ctrm_request_type_roles(Model):
	_name = 'ctrm.request.type.roles'
	_description = 'Role CTRM Request Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='ctrm.request.types', on_delete='c'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','a'))]),
	'note': fields.text(label = 'Note')
	}

ctrm_request_type_roles()

class ctrm_offer_types(Model):
	_name = 'ctrm.offer.types'
	_description = 'Types CTRM Offer'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='ctrm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='ctrm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='ctrm.offer.type.roles',rel='type_id'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

ctrm_offer_types()

class ctrm_offer_type_roles(Model):
	_name = 'ctrm.offer.type.roles'
	_description = 'Role CTRM Offer Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='ctrm.offer.types', on_delete='c'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','a'))]),
	'note': fields.text(label = 'Note')
	}

ctrm_offer_type_roles()

class ctrm_contract_types(Model):
	_name = 'ctrm.contract.types'
	_description = 'Types CTRM Contract'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='ctrm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='ctrm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='ctrm.contract.type.roles',rel='type_id'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

ctrm_contract_types()

class ctrm_contract_type_roles(Model):
	_name = 'ctrm.contract.type.roles'
	_description = 'Role CTRM Contract Types'
	_class_model = 'C'
	_class_category = 'delivery'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='ctrm.contract.types', on_delete='c'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','a'))]),
	'note': fields.text(label = 'Note')
	}

ctrm_contract_type_roles()

# end customize

class ctrm_request_categories(Model):
	_name = 'ctrm.request.categories'
	_description = 'Category CTRM Request'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='ctrm.request.categories'),
	'childs_id': fields.one2many(obj = 'ctrm.request.categories',rel = 'parent_id',label = 'Childs'),
	'requests': fields.one2many(label='Requests',obj='ctrm.requests',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

ctrm_request_categories()

class ctrm_offer_categories(Model):
	_name = 'ctrm.offer.categories'
	_description = 'Category CTRM Offer'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='ctrm.offer.categories'),
	'childs_id': fields.one2many(obj = 'ctrm.offer.categories',rel = 'parent_id',label = 'Childs'),
	'offers': fields.one2many(label='Offers',obj='ctrm.offers',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

ctrm_offer_categories()

class ctrm_contract_categories(Model):
	_name = 'ctrm.contract.categories'
	_description = 'Category CTRM Contract'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='ctrm.contract.categories'),
	'childs_id': fields.one2many(obj = 'ctrm.contract.categories',rel = 'parent_id',label = 'Childs'),
	'contracts': fields.one2many(label='Contracts',obj='ctrm.contracts',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

ctrm_contract_categories()

class ctrm_requests(Model):
	_name = 'ctrm.requests'
	_description = 'CTRM Request'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'dor'
	_columns = {
	'rtype': fields.many2one(label='Type',required = True,obj='ctrm.request.types',on_change='on_change_rtype'),
	'name': fields.varchar(label = 'Name'),
	'category_id': fields.many2one(label='Category',obj='ctrm.request.categories'),
	'company_id': fields.many2one(label='Company',obj='md.company'),
	'channel_id': fields.many2one(label='Cannel',obj='ctrm.channels'),
	'sector_id': fields.related(label='Sector',obj='ctrm.sectors',relatedy=['channel_id']),
	'team_id': fields.many2one(label='Team',obj='ctrm.teams'),
	'group_id': fields.related(label='Group',obj='ctrm.groups',relatedy=['team_id']),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'origin': fields.varchar(label = 'Origin'),
	'from_date': fields.date(label='Begin Date Of Request',required=True),
	'to_date': fields.date(label='End Date Of Request',required=True),
	'dor': fields.date(label='Date Of Request',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('iscustomer',)]),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'incoterms1': fields.many2one(label='Incoterms 1',obj='md.incoterms'),
	'incoterms2': fields.varchar(label = 'Incoterms 2'),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'mob': fields.many2one(label='BoM',obj='md.boms',domain=[('usage','=','sale'),'|',('usage','=','all')],on_change='_on_change_mob'),
	'items': fields.one2many(label='Items',obj='ctrm.request.items',rel='request_id'),
	'roles': fields.one2many(label='Roles',obj='ctrm.request.roles',rel='request_id'),
	'texts': fields.one2many(label='Texts',obj='ctrm.request.texts',rel='request_id'),
	'note': fields.text('Note')
	}

	def _on_change_rtype(self,cr,pool,uid,item,context={}):		
			roles = pool.get('ctrm.request.type.roles').select(cr,pool.uid,['role_id'],[('type_id','=',item['rtype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]

	def _on_change_mob(self,cr,pool,uid,item,context={}):		
		if item['mob'] and 'name' in item['mob'] and item['mob']['name']:
			p = pool.get('md.mob.output.items').select(cr,pool,uid,['product','quantity','uom'],[('mob_id','=',item['mob']['name'])],context)
			for i in p:
				ei = pool.get('sale.order.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.now().astimezone()+timedelta(3)
				item_items = pool.get('sale.order.items')._buildEmptyItem()
				item_items['delivery_schedules'].append(ei)
				for f in ('product','uom'):
					item_items[f] = i[f]
				item_items['price'] = 0.00
				item['items'].append(item_items)

		return None

	_default = {
		'state':'draft'
	}

ctrm_requests()

class ctrm_request_texts(Model):
	_name = 'ctrm.request.texts'
	_description = 'CTRM Request Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'request_id': fields.many2one(label='Request',obj='ctrm.requests'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='ctrm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

ctrm_request_texts()

class ctrm_request_roles(Model):
	_name = 'ctrm.request.roles'
	_description = 'CTRM Request Roles'
	_columns = {
	'request_id': fields.many2one(label = 'Request',obj='ctrm.requests'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

ctrm_request_roles()

class ctrm_request_items(Model):
	_name = 'ctrm.request.items'
	_description = 'CTRM Request Items'
	_inherits = {'common.model':{'_methods':['_calculate_vat_amount_costs','_calculate_items_amount_costs','_calculate_items']}}
	_columns = {
	'request_id': fields.many2one(obj = 'ctrm.requests',label = 'CTRM Request'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',compute='_calculate_items',size=(15,2)),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('s','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'delivery_schedules': fields.one2many(label='Delivery Schedule',obj='ctrm.request.item.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='ctrm.request.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='ctrm.request.item.texts',rel='item_id'),
	'note': fields.text(label = 'Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.sale.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
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


ctrm_request_items()

class ctrm_request_item_texts(Model):
	_name = 'ctrm.request.item.texts'
	_description = 'CTRM Request Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='ctrm.request.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='ctrm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

ctrm_request_item_texts()

class ctrm_request_item_roles(Model):
	_name = 'ctrm.request.item.roles'
	_description = 'CTRM Offer Item Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='ctrm.request.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

ctrm_request_item_roles()

class ctrm_request_item_delivery_schedules(Model):
	_name = 'ctrm.request.item.delivery.schedules'
	_description = 'CTRM REquest Item Delivery Schedules'
	_columns = {
	'item_id': fields.many2one(obj = 'ctrm.request.items',label = 'Request Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1
	}

ctrm_request_item_delivery_schedules()

class ctrm_offers(Model):
	_name = 'ctrm.offers'
	_description = 'CTRM Offer'
	_date = 'doo'
	_columns = {
	'otype': fields.many2one(label='Type',required = True,obj='ctrm.offer.types',on_change='on_change_otype'),
	'name': fields.varchar(label = 'Name'),
	'category_id': fields.many2one(label='Category',obj='ctrm.offer.categories'),
	'company_id': fields.many2one(label='Company',obj='md.company'),
	'channel_id': fields.many2one(label='Cannel',obj='ctrm.channels'),
	'sector_id': fields.related(label='Sector',obj='ctrm.sectors',relatedy=['channel_id']),
	'team_id': fields.many2one(label='Team',obj='ctrm.teams'),
	'group_id': fields.related(label='Group',obj='ctrm.groups',relatedy=['team_id']),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'origin': fields.varchar(label = 'Origin'),
	'doo': fields.date(label='Date Of Offer',required=True),
	'from_date': fields.date(label='Begin Date Of Offer',required=True),
	'to_date': fields.date(label='End Date Of Offer',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('iscustomer',)]),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'incoterms1': fields.many2one(label='Incoterms 1',obj='md.incoterms'),
	'incoterms2': fields.varchar(label = 'Incoterms 2'),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'mob': fields.many2one(label='BoM',obj='md.boms',domain=[('usage','=','sale'),'|',('usage','=','all')],on_change='_on_change_mob'),
	'items': fields.one2many(label='Items',obj='ctrm.offer.items',rel='offer_id'),
	'roles': fields.one2many(label='Roles',obj='ctrm.offer.roles',rel='offer_id'),
	'texts': fields.one2many(label='Texts',obj='ctrm.offer.texts',rel='offer_id'),
	'note': fields.text('Note')
	}

	def _on_change_otype(self,cr,pool,uid,item,context={}):		
			roles = pool.get('ctrm.offer.type.roles').select(cr,pool.uid,['role_id'],[('type_id','=',item['otype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]

	def _on_change_mob(self,cr,pool,uid,item,context={}):		
		if item['mob'] and 'name' in item['mob'] and item['mob']['name']:
			p = pool.get('md.mob.output.items').select(cr,pool,uid,['product','quantity','uom'],[('mob_id','=',item['mob']['name'])],context)
			for i in p:
				ei = pool.get('sale.order.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.now().astimezone()+timedelta(3)
				item_items = pool.get('sale.order.items')._buildEmptyItem()
				item_items['delivery_schedules'].append(ei)
				for f in ('product','uom'):
					item_items[f] = i[f]
				item_items['price'] = 0.00
				item['items'].append(item_items)

		return None

	_default = {
		'state':'draft'
	}

ctrm_offers()

class ctrm_offer_texts(Model):
	_name = 'ctrm.offer.texts'
	_description = 'CTRM Offer Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'offer_id': fields.many2one(label='Offer',obj='ctrm.offers'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='ctrm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

ctrm_offer_texts()

class ctrm_offer_roles(Model):
	_name = 'ctrm.offer.roles'
	_description = 'CTRM Offer Roles'
	_columns = {
	'offer_id': fields.many2one(label = 'Request',obj='ctrm.offers'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

ctrm_offer_roles()

class ctrm_offer_items(Model):
	_name = 'ctrm.offer.items'
	_description = 'CTRM Offer Items'
	_inherits = {'common.model':{'_methods':['_calculate_vat_amount_costs','_calculate_items_amount_costs','_calculate_items']}}
	_columns = {
	'offer_id': fields.many2one(obj = 'ctrm.offers',label = 'CTRM Offer'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',compute='_calculate_items',size=(15,2)),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('s','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'delivery_schedules': fields.one2many(label='Delivery Schedule',obj='ctrm.offer.item.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='ctrm.offer.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='ctrm.offer.item.texts',rel='item_id'),
	'note': fields.text(label = 'Note')
	}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.sale.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
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

ctrm_offer_items()

class ctrm_offer_item_texts(Model):
	_name = 'ctrm.offer.item.texts'
	_description = 'CTRM Offer Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='ctrm.offer.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='ctrm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

ctrm_offer_item_texts()

class ctrm_offer_item_roles(Model):
	_name = 'ctrm.offer.item.roles'
	_description = 'CTRM Offer Item Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='ctrm.offer.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

ctrm_offer_item_roles()

class ctrm_offer_item_delivery_schedules(Model):
	_name = 'ctrm.offer.item.delivery.schedules'
	_description = 'CTRM Offer Item Delivery Schedules'
	_columns = {
	'item_id': fields.many2one(obj = 'ctrm.offer.items',label = 'Offer Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
	}

ctrm_offer_item_delivery_schedules()

# Contract
class ctrm_contracts(Model):
	_name = 'ctrm.contracts'
	_description = 'CTRM Contract'
	_date = 'doc'
	_columns = {
	'ctype': fields.many2one(label='Type',obj='ctrm.contract.types',on_change='on_change_ctype'),
	'name': fields.varchar(label = 'Name'),
	'category_id': fields.many2one(label='Category',obj='ctrm.contract.categories'),
	'company_id': fields.many2one(label='Company',obj='md.company'),
	'channel_id': fields.many2one(label='Cannel',obj='ctrm.channels'),
	'sector_id': fields.related(label='Sector',obj='ctrm.sectors',relatedy=['channel_id']),
	'team_id': fields.many2one(label='Team',obj='ctrm.teams'),
	'group_id': fields.related(label='Group',obj='ctrm.groups',relatedy=['team_id']),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'origin': fields.varchar(label = 'Origin'),
	'doc': fields.date(label='Date Of Contract',required=True),
	'futures_date': fields.date(label='Futures Date Of Contract',required=True),
	'from_date': fields.date(label='Begin Date Of Contract',required=True),
	'to_date': fields.date(label='End Date Of Contract',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('iscustomer',)]),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'incoterms1': fields.many2one(label='Incoterms 1',obj='md.incoterms'),
	'incoterms2': fields.varchar(label = 'Incoterms 2'),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'mob': fields.many2one(label='BoM',obj='md.boms',domain=[('usage','=','sale'),'|',('usage','=','all')],on_change='_on_change_mob'),
	'items': fields.one2many(label='Items',obj='ctrm.contract.items',rel='contract_id'),
	'roles': fields.one2many(label='Roles',obj='ctrm.contract.roles',rel='contract_id'),
	'texts': fields.one2many(label='Texts',obj='ctrm.contract.texts',rel='contract_id'),
	'note': fields.text('Note')
	}

	def _on_change_ctype(self,cr,pool,uid,item,context={}):		
			roles = pool.get('ctrm.contract.type.roles').select(cr,pool.uid,['role_id'],[('type_id','=',item['ctype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]

	def _on_change_mob(self,cr,pool,uid,item,context={}):		
		if item['mob'] and 'name' in item['mob'] and item['mob']['name']:
			p = pool.get('md.mob.output.items').select(cr,pool,uid,['product','quantity','uom'],[('mob_id','=',item['mob']['name'])],context)
			for i in p:
				ei = pool.get('sale.order.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.now().astimezone()+timedelta(3)
				item_items = pool.get('sale.order.items')._buildEmptyItem()
				item_items['delivery_schedules'].append(ei)
				for f in ('product','uom'):
					item_items[f] = i[f]
				item_items['price'] = 0.00
				item['items'].append(item_items)

		return None

	_default = {
		'state':'draft'
	}

ctrm_contracts()

class ctrm_contract_texts(Model):
	_name = 'ctrm.contract.texts'
	_description = 'CTRM Contract Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'contract_id': fields.many2one(label='Offer',obj='ctrm.contracts'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='ctrm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

ctrm_contract_texts()

class ctrm_contract_roles(Model):
	_name = 'ctrm.contract.roles'
	_description = 'CTRM Contracts Roles'
	_columns = {
	'offer_id': fields.many2one(label = 'Request',obj='ctrm.contracts'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

ctrm_contract_roles()

class ctrm_contract_items(Model):
	_name = 'ctrm.contract.items'
	_description = 'CTRM Offer Items'
	_inherits = {'common.model':{'_methods':['_calculate_vat_amount_costs','_calculate_items_amount_costs']}}
	_columns = {
	'contract_id': fields.many2one(obj = 'ctrm.contracts',label = 'Contract'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,2)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('s','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'delivery_schedules': fields.one2many(label='Delivery Schedule',obj='ctrm.contract.item.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='ctrm.contract.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='ctrm.contract.item.texts',rel='item_id'),
	'note': fields.text(label = 'Note')
	}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product_id'] and 'name' in item['product_id'] and item['product_id']['name']:
			p = pool.get('md.sale.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product_id']['name'])],context)
			if len(p) > 0:
				for f in ('vat','uom','price','currency','unit','uop'):
					if item['item'][f] != p[0][f]:
						item['item'][f] = p[0][f]

		return None

	_default = {
		'quantity': 1,
		'unit': 1
	}

ctrm_contract_items()

class ctrm_contract_item_texts(Model):
	_name = 'ctrm.contract.item.texts'
	_description = 'CTRM Contract Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='ctrm.contract.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='ctrm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

ctrm_contract_item_texts()

class ctrm_contract_item_roles(Model):
	_name = 'ctrm.contract.item.roles'
	_description = 'CTRM Contract Item Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='ctrm.contract.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

ctrm_contract_item_roles()

class ctrm_contract_item_delivery_schedules(Model):
	_name = 'ctrm.contract.item.delivery.schedules'
	_description = 'CTRM Contract Item Delivery Schedules'
	_columns = {
	'item_id': fields.many2one(obj = 'ctrm.contract.items',label = 'Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
	}

ctrm_contract_item_delivery_schedules()





