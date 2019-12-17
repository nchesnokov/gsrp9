from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

from decimal import Decimal

class srm_common(ModelInherit):
	_name = 'srm.common'
	_description = 'SRM Common'
	def copy_into(self,dest):
		return [self,dest,'copy into']

	def copy_from(self,src):
		return [self,src,'copy from']

	_columns = {
	'note1': fields.text(label='Note1'),
	'note2': fields.text(label='Note2')
	}
	
	def _act_merge(self,cr,pool,uid,column,record,context={}):
		return ['Merge']

	_actions = {'merge':{'label':'Merge','tooltip':'Merge record','method':'_act_merge','icon':'list'}}

srm_common()

class srm_routes(Model):
	_name = 'srm.routes'
	_description = 'General SRM Route'
	_columns = {
	'name': fields.varchar(label = 'Route',selectable = True),
	'items': fields.one2many(label='Items',obj='srm.route.items',rel='route_id'),
	'note': fields.text('Note')}

srm_routes()

class srm_route_items(Model):
	_name = 'srm.route.items'
	_description = 'General SRM Route Items'
	_order_by="route_id asc,sequence asc"
	_columns = {
	'route_id': fields.many2one(label='Route',obj='srm.routes',on_delete='c',on_update='c'),
	'sequence': fields.integer(label='Sequence'),
	'srm_object_type': fields.selection(label='SRM object type',selections=[('demand','Demand'),('plan','Plan')]),
	'note': fields.text('Note')}

srm_route_items()

class srm_demand_category(Model):
	_name = 'srm.demand.category'
	_description = 'General Model Category SRM Demand'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.demand.category'),
	'childs_id': fields.one2many(obj = 'srm.demand.category',rel = 'parent_id',label = 'Childs'),
	'demands': fields.one2many(label='Demands',obj='srm.demand',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_demand_category()

class srm_part_category(Model):
	_name = 'srm.part.category'
	_description = 'General Model Category SRM Part'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.part.category'),
	'childs_id': fields.one2many(obj = 'srm.part.category',rel = 'parent_id',label = 'Childs'),
	'parts': fields.one2many(label='Parts',obj='srm.part',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_part_category()

class srm_plan_category(Model):
	_name = 'srm.plan.category'
	_description = 'General Model Category SRM Plan'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.plan.category'),
	'childs_id': fields.one2many(obj = 'srm.plan.category',rel = 'parent_id',label = 'Childs'),
	'plans': fields.one2many(label='Plans',obj='srm.plan',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_plan_category()

class srm_request_category(Model):
	_name = 'srm.request.category'
	_description = 'General Model Category SRM Request'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.request.category'),
	'childs_id': fields.one2many(obj = 'srm.request.category',rel = 'parent_id',label = 'Childs'),
	'requests': fields.one2many(label='Requests',obj='srm.request',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_request_category()

class srm_rfx_category(Model):
	_name = 'srm.rfx.category'
	_description = 'General Model Category SRM RFX'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.rfx.category'),
	'childs_id': fields.one2many(obj = 'srm.rfx.category',rel = 'parent_id',label = 'Childs'),
	'rfxs': fields.one2many(label='RFXs',obj='srm.rfx',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_rfx_category()

class srm_auction_category(Model):
	_name = 'srm.auction.category'
	_description = 'General Model Category SRM Auction'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.auction.category'),
	'childs_id': fields.one2many(obj = 'srm.auction.category',rel = 'parent_id',label = 'Childs'),
	'auctions': fields.one2many(label='Auctions',obj='srm.auction',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_auction_category()

class srm_offer_category(Model):
	_name = 'srm.offer.category'
	_description = 'General Model Category SRM Offer'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.offer.category'),
	'childs_id': fields.one2many(obj = 'srm.offer.category',rel = 'parent_id',label = 'Childs'),
	'offers': fields.one2many(label='Offers',obj='srm.offer',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_offer_category()

class srm_evolution_category(Model):
	_name = 'srm.evolution.category'
	_description = 'General Model Category SRM Evolution'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.evolution.category'),
	'childs_id': fields.one2many(obj = 'srm.evolution.category',rel = 'parent_id',label = 'Childs'),
	'evolutions': fields.one2many(label='Evolutions',obj='srm.evolution',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_evolution_category()

class srm_decision_category(Model):
	_name = 'srm.decision.category'
	_description = 'General Model Category SRM Decision'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.decision.category'),
	'childs_id': fields.one2many(obj = 'srm.decision.category',rel = 'parent_id',label = 'Childs'),
	'decisions': fields.one2many(label='Decisions',obj='srm.decision',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_decision_category()

class srm_contract_category(Model):
	_name = 'srm.contract.category'
	_description = 'General Model Category SRM Contract'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.contract.category'),
	'childs_id': fields.one2many(obj = 'srm.contract.category',rel = 'parent_id',label = 'Childs'),
	'contracts': fields.one2many(label='Contracts',obj='srm.contracts',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_contract_category()
# 
#customize
#Text
class srm_texts(Model):
	_name = 'srm.texts'
	_description = 'General Model SRM Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

srm_texts()

class srm_schema_texts(Model):
	_name = 'srm.schema.texts'
	_description = 'General Model Schema Of SRM Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'usage': fields.selection(label='Usage',selections=[('h','Header'),('i','Item'),('b','Both')]),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'texts': fields.one2many(label='Texts',obj='srm.schema.text.items',rel='schema_id')
	}

srm_schema_texts()

class srm_schema_text_items(Model):
	_name = 'srm.schema.text.items'
	_description = 'General Model Items Of Schema SRM Texts'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'schema_id': fields.many2one(label = 'Schema',obj='srm.schema.texts'),
	'seq': fields.integer(label='Sequence'),
	'text_id': fields.many2one(label = 'Text',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr')
	}

srm_schema_text_items()

# Text end
# Types & Roles
class srm_demand_types(Model):
	_name = 'srm.demand.types'
	_description = 'General Model Types SRM Demand'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='srm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='srm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='srm.demand.type.roles',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

srm_demand_types()

class srm_demand_type_roles(Model):
	_name = 'srm.demand.type.roles'
	_description = 'General Model Role SRM Demand Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.demand.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_demand_type_roles()

# Types & Roles
#
class srm_demand(Model):
	_name = 'srm.demand'
	_description = 'General SRM Demand'
	_inherits = {'srm.common':{'_methods':['copy_into','copy_from'],'_columns':['note1','note2'],'_actions':['merge']},'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'dod'
	_columns = {
	'dtype': fields.many2one(label='Type',obj='srm.demand.types',on_change='on_change_dtype'),
	'name': fields.varchar(label = 'Demand',selectable = True),
	'company': fields.many2one(label='Company',obj='md.company'),
	'category_id': fields.many2one(label='Category',obj='srm.demand.category'),
	'origin': fields.varchar(label = 'Origin'),
	'dod': fields.date(label='Date Of Demand',required=True),
	'from_date': fields.date(label='From Date Of Demand',required=True),
	'to_date': fields.date(label='To Date Of Demand',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',on_delete='n',on_update='n',domain=[('issuplier',)]),
	'route_id': fields.many2one(label='Route',obj='srm.routes',on_delete='n',on_update='n'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'recepture': fields.many2one(label='Recepture',obj='md.recepture',domain=[('usage','=','p'),'|',('usage','=','a')]),
	'items': fields.one2many(label='Items',obj='srm.demand.items',rel='demand_id'),
	'roles': fields.one2many(label='Roles',obj='srm.demand.roles',rel='demand_id'),
	'texts': fields.one2many(label='Texts',obj='srm.demand.texts',rel='demand_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.demand.deadlines',rel='demand_id'),
	'note': fields.text('Note')}
	
	def _on_change_dtype(self,cr,pool,uid,item,context={}):		
			roles = pool.get('srm.demand.type.roles').select(cr,pool.uid,['role_id'],[('type_id','=',item['dtype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]

srm_demand()

class srm_demand_texts(Model):
	_name = 'srm.demand.texts'
	_description = 'General Model SRM Demand Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'demand_id': fields.many2one(label='Demand',obj='srm.demand'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_demand_texts()


class srm_demand_roles(Model):
	_name = 'srm.demand.roles'
	_description = 'General Model SRM Demand Roles'
	_columns = {
	'demand_id': fields.many2one(label = 'Demand',obj='srm.demand'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_demand_roles()


class srm_demand_type_deadlines(Model):
	_name = 'srm.demand.type.deadlines'
	_description = 'General SRM Demand Type Deadlines'
	_columns = {
	'name': fields.varchar(label = 'Type'),
	'note': fields.text('Note')}

srm_demand_type_deadlines()

class srm_demand_deadlines(Model):
	_name = 'srm.demand.deadlines'
	_description = 'General SRM Demand Deadlines'
	_order_by = 'start_date asc'
	_columns = {
	'demand_id': fields.many2one(label = 'Demand',obj='srm.demand',on_delete='c',on_update='c'),
	'demand_type_deadline_id': fields.many2one(label = 'Type',obj='srm.demand.type.deadlines',on_delete='n',on_update='n'),
	'start_date': fields.datetime(label='Start',required=True),
	'end_date': fields.datetime(label='End',required=True),
	'note': fields.text('Note')}

srm_demand_deadlines()

class srm_demand_items(Model):
	_name = 'srm.demand.items'
	_description = 'General SRM Demant Item'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'demand_id': fields.many2one(obj = 'srm.demand',label = 'Demand',on_delete='c',on_update='c'),
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
	'delivery_schedules': fields.one2many(label='Delivery Schedules',obj='srm.demand.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='srm.demand.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='srm.demand.item.texts',rel='item_id'),
	'note': fields.text('Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.purchase.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
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

class srm_demand_item_texts(Model):
	_name = 'srm.demand.item.texts'
	_description = 'General Model SRM Demand Item Texts'
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
	_description = 'General Model SRM Demand Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.demand.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_demand_item_roles()

class srm_demand_delivery_schedules(Model):
	_name = 'srm.demand.delivery.schedules'
	_description = 'General SRM Demand Delivery Schedules'
	_date = "schedule"
	_columns = {
	'item_id': fields.many2one(obj = 'srm.demand.items',label = 'Demand Item',on_delete='c',on_update='c'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom',on_delete='n',on_update='n'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')}

srm_demand_delivery_schedules()

class srm_part_types(Model):
	_name = 'srm.part.types'
	_description = 'General Model Types SRM Part'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='srm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='srm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='srm.part.type.roles',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

srm_part_types()

class srm_part_type_roles(Model):
	_name = 'srm.part.type.roles'
	_description = 'General Model Role SRM Part Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.part.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_part_type_roles()


class srm_part(Model):
	_name = 'srm.part'
	_description = 'General SRM Part'
	_inherits = {'srm.common':{'_methods':['copy_into','copy_from']},'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'dop'
	_columns = {
	'ptype': fields.many2one(label='Type',obj='srm.part.types',on_change='on_change_ptype'),
	'name': fields.varchar(label = 'Part',selectable = True),
	'company': fields.many2one(label='Company',obj='md.company'),
	'category_id': fields.many2one(label='Category',obj='srm.part.category'),
	'origin': fields.varchar(label = 'Origin'),
	'dop': fields.date(label='Date Of Part',required=True),
	'from_date': fields.date(label='From Date Of Part',required=True),
	'to_date': fields.date(label='To Date Of Part',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('issuplier',)]),
	'route_id': fields.many2one(label='Route',obj='srm.routes'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'recepture': fields.many2one(label='Recepture',obj='md.recepture',domain=[('usage','=','p'),'|',('usage','=','a')]),
	'items': fields.one2many(label='Items',obj='srm.part.items',rel='part_id'),
	'roles': fields.one2many(label='Roles',obj='srm.part.roles',rel='part_id'),
	'texts': fields.one2many(label='Texts',obj='srm.part.texts',rel='part_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.part.deadlines',rel='part_id'),
	'note': fields.text('Note')}

	def _on_change_ptype(self,cr,pool,uid,item,context={}):		
			roles = pool.get('srm.part.type.roles').select(cr,pool.uid,['role_id'],[('type_id','=',item['ptype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]


srm_part()

class srm_part_texts(Model):
	_name = 'srm.part.texts'
	_description = 'General Model SRM Part Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'part_id': fields.many2one(label='Part',obj='srm.part'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_part_texts()


class srm_part_roles(Model):
	_name = 'srm.part.roles'
	_description = 'General Model SRM Part Roles'
	_columns = {
	'part_id': fields.many2one(label = 'Part',obj='srm.part'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_part_roles()


class srm_part_type_deadlines(Model):
	_name = 'srm.part.type.deadlines'
	_description = 'General SRM Part Type Deadlines'
	_columns = {
	'name': fields.varchar(label = 'Type'),
	'note': fields.text('Note')}

srm_part_type_deadlines()

class srm_part_deadlines(Model):
	_name = 'srm.part.deadlines'
	_description = 'General SRM Part Deadlines'
	_order_by = 'start_date asc'
	_columns = {
	'part_id': fields.many2one(label = 'Part',obj='srm.part'),
	'part_type_deadline_id': fields.many2one(label = 'Type',obj='srm.part.type.deadlines'),
	'start_date': fields.datetime(label='Start',required=True),
	'end_date': fields.datetime(label='End',required=True),
	'note': fields.text('Note')}

srm_part_deadlines()

class srm_part_items(Model):
	_name = 'srm.part.items'
	_description = 'General SRM Part Item'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'part_id': fields.many2one(obj = 'srm.part',label = 'Part'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='VAT Code',obj='md.vat.code',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'delivery_schedules': fields.one2many(label='Delivery Schedules',obj='srm.part.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='srm.part.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='srm.part.item.texts',rel='item_id'),
	'note': fields.text('Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.purchase.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
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

class srm_part_item_texts(Model):
	_name = 'srm.part.item.texts'
	_description = 'General Model SRM Part Item Texts'
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
	_description = 'General Model SRM Part Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.part.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_part_item_roles()


class srm_part_delivery_schedules(Model):
	_name = 'srm.part.delivery.schedules'
	_description = 'General SRM Part Delivery Schedules'
	_date = "schedule"
	_columns = {
	'item_id': fields.many2one(obj = 'srm.part.items',label = 'Part Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')}

srm_part_delivery_schedules()

class srm_plan_types(Model):
	_name = 'srm.plan.types'
	_description = 'General Model Types SRM Plan'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='srm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='srm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='srm.plan.type.roles',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

srm_plan_types()

class srm_plan_type_roles(Model):
	_name = 'srm.plan.type.roles'
	_description = 'General Model Role SRM Plan Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.plan.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_plan_type_roles()



class srm_plan(Model):
	_name = 'srm.plan'
	_description = 'General SRM Plan'
	_inherits = {'srm.common':{'_methods':['copy_into','copy_from']}}
	_date = 'dop'
	_columns = {
	'ptype': fields.many2one(label='Type',obj='srm.plan.types',on_change='on_change_ptype'),
	'name': fields.varchar(label = 'Plan',selectable = True),
	'company': fields.many2one(label='Company',obj='md.company'),
	'category_id': fields.many2one(label='Category',obj='srm.plan.category'),
	'origin': fields.varchar(label = 'Origin'),
	'dop': fields.date(label='Date Of Plan',required=True),
	'from_date': fields.date(label='From Date Of Plan',required=True),
	'to_date': fields.date(label='To Date Of Plan',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('issuplier',)]),
	'route_id': fields.many2one(label='Route',obj='srm.routes'),
	'recepture': fields.many2one(label='Recepture',obj='md.recepture',domain=[('usage','=','p'),'|',('usage','=','a')]),
	'items': fields.one2many(label='Items',obj='srm.plan.items',rel='plan_id'),
	'roles': fields.one2many(label='Roles',obj='srm.plan.roles',rel='plan_id'),
	'texts': fields.one2many(label='Texts',obj='srm.plan.texts',rel='plan_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.plan.deadlines',rel='plan_id'),
	'note': fields.text('Note')}

	def _on_change_ptype(self,cr,pool,uid,item,context={}):		
			roles = pool.get('srm.plan.type.roles').select(cr,pool.uid,['role_id'],[('type_id','=',item['ptype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]

srm_plan()

class srm_plan_texts(Model):
	_name = 'srm.plan.texts'
	_description = 'General Model SRM Plan Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'plan_id': fields.many2one(label='Plan',obj='srm.plan'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_plan_texts()


class srm_plan_roles(Model):
	_name = 'srm.plan.roles'
	_description = 'General Model SRM Plan Roles'
	_columns = {
	'plan_id': fields.many2one(label = 'Plan',obj='srm.plan'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_plan_roles()


class srm_plan_type_deadlines(Model):
	_name = 'srm.plan.type.deadlines'
	_description = 'General SRM Plan Type Deadlines'
	_columns = {
	'name': fields.varchar(label = 'Type'),
	'note': fields.text('Note')}

srm_plan_type_deadlines()

class srm_plan_deadlines(Model):
	_name = 'srm.plan.deadlines'
	_description = 'General SRM Plan Deadlines'
	_order_by = 'start_date asc'
	_columns = {
	'plan_id': fields.many2one(label = 'Plan',obj='srm.plan'),
	'plan_type_deadline_id': fields.many2one(label = 'Type',obj='srm.plan.type.deadlines'),
	'start_date': fields.datetime(label='Start',required=True),
	'end_date': fields.datetime(label='End',required=True),
	'note': fields.text('Note')}

srm_plan_deadlines()

class srm_plan_items(Model):
	_name = 'srm.plan.items'
	_description = 'General SRM Plan Items'
	_columns = {
	'plan_id': fields.many2one(obj = 'srm.plan',label = 'Plan'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='VAT Code',obj='md.vat.code',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'delivery_schedules': fields.one2many(label='Delivery Schedules',obj='srm.plan.delivery.schedules',rel='item_id'),	
	'roles': fields.one2many(label='Roles',obj='srm.plan.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='srm.plan.item.texts',rel='item_id'),
	'note': fields.text('Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.purchase.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
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

class srm_plan_item_texts(Model):
	_name = 'srm.plan.item.texts'
	_description = 'General Model SRM Plan Item Texts'
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
	_description = 'General Model SRM Plan Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.plan.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_plan_item_roles()



class srm_plan_delivery_schedules(Model):
	_name = 'srm.plan.delivery.schedules'
	_description = 'General SRM Plan Delivery Schedules'
	_date = "schedule"
	_columns = {
	'item_id': fields.many2one(obj = 'srm.plan.items',label = 'Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')}

srm_plan_delivery_schedules()

class srm_request_types(Model):
	_name = 'srm.request.types'
	_description = 'General Model Types SRM Request'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='srm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='srm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='srm.request.type.roles',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

srm_request_types()

class srm_request_type_roles(Model):
	_name = 'srm.request.type.roles'
	_description = 'General Model Role SRM Request Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.request.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_request_type_roles()


class srm_request(Model):
	_name = 'srm.request'
	_description = 'General SRM Request'
	_inherits = {'srm.common':{'_methods':['copy_into','copy_from']},'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'dor'
	_columns = {
	'rtype': fields.many2one(label='Type',obj='srm.request.types',on_change='on_change_rtype'),
	'name': fields.varchar(label = 'Request',selectable = True),
	'company': fields.many2one(label='Company',obj='md.company'),
	'category_id': fields.many2one(label='Category',obj='srm.request.category'),
	'origin': fields.varchar(label = 'Origin'),
	'dor': fields.date(label='Date Of Request',required=True),
	'from_date': fields.date(label='From Date Of Request',required=True),
	'to_date': fields.date(label='To Date Of Request',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('issuplier',)]),
	'route_id': fields.many2one(label='Route',obj='srm.routes'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'recepture': fields.many2one(label='Recepture',obj='md.recepture',domain=[('usage','=','p'),'|',('usage','=','a')]),
	'items': fields.one2many(label='Items',obj='srm.request.items',rel='request_id'),
	'roles': fields.one2many(label='Roles',obj='srm.plan.roles',rel='request_id'),
	'texts': fields.one2many(label='Texts',obj='srm.plan.texts',rel='request_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.request.deadlines',rel='request_id'),
	'note': fields.text(label='Note')}

	def _on_change_rtype(self,cr,pool,uid,item,context={}):		
			roles = pool.get('srm.request.type.roles').select(cr,pool.uid,['role_id'],[('type_id','=',item['ptype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]

srm_request()

class srm_request_texts(Model):
	_name = 'srm.request.texts'
	_description = 'General Model SRM Request Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'request_id': fields.many2one(label='Request',obj='srm.request'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_request_texts()


class srm_request_roles(Model):
	_name = 'srm.request.roles'
	_description = 'General Model SRM Request Roles'
	_columns = {
	'request_id': fields.many2one(label = 'Request',obj='srm.request'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_request_roles()

class srm_request_type_deadlines(Model):
	_name = 'srm.request.type.deadlines'
	_description = 'General SRM Request Type Deadlines'
	_columns = {
	'name': fields.varchar(label = 'Type'),
	'note': fields.text(label='Note')}

srm_request_type_deadlines()

class srm_request_deadlines(Model):
	_name = 'srm.request.deadlines'
	_description = 'General SRM Request Deadlines'
	_order_by = 'start_date asc'
	_columns = {
	'request_id': fields.many2one(label = 'Request',obj='srm.request'),
	'request_type_deadline_id': fields.many2one(label = 'Type',obj='srm.request.type.deadlines'),
	'start_date': fields.datetime(label='Start',required=True),
	'end_date': fields.datetime(label='End',required=True),
	'note': fields.text(label='Note')}

srm_request_deadlines()

class srm_request_items(Model):
	_name = 'srm.request.items'
	_description = 'General SRM Request Items'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'request_id': fields.many2one(obj = 'srm.request',label = 'Request'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='VAT Code',obj='md.vat.code',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'delivery_schedules': fields.one2many(label='Delivery Schedules',obj='srm.request.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='srm.request.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='srm.request.item.texts',rel='item_id'),
	'note': fields.text(label='Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.purchase.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
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

class srm_request_item_texts(Model):
	_name = 'srm.request.item.texts'
	_description = 'General Model SRM Кequest Item Texts'
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
	_description = 'General Model SRM Кequest Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.request.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_request_item_roles()


class srm_request_delivery_schedules(Model):
	_name = 'srm.request.delivery.schedules'
	_description = 'General SRM Request Delivery Schedules'
	_date = "schedule"
	_columns = {
	'item_id': fields.many2one(obj = 'srm.request.items',label = 'Request Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')}

srm_request_delivery_schedules()

class srm_rfx(Model):
	_name = 'srm.rfx'
	_description = 'General SRM RFX'
	_inherits = {'srm.common':{'_methods':['copy_into','copy_from']}}
	_date = 'dorfx'
	_columns = {
	'name': fields.varchar(label = 'Name',selectable = True),
	'company': fields.many2one(label='Company',obj='md.company'),
	'category_id': fields.many2one(label='Category',obj='srm.rfx.category'),
	'origin': fields.varchar(label = 'Origin'),
	'dorfx': fields.date(label='Date Of RFX',required=True),
	'from_date': fields.date(label='From Date Of RFX',required=True),
	'to_date': fields.date(label='To Date Of RFX',required=True),
	'rfxtype': fields.selection(label='Type',selections=[('O','Opened'),('C','Closed')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('issuplier',)]),
	'route_id': fields.many2one(label='Route',obj='srm.routes'),
	'items': fields.one2many(label='Items',obj='srm.rfx.items',rel='rfx_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.rfx.deadlines',rel='rfx_id'),
	'partners': fields.one2many(label='Partners',obj='srm.rfx.partner',rel='partner_id'),
	'note': fields.text('Note')}

srm_rfx()

class srm_rfx_partner(Model):
	_name = 'srm.rfx.partner'
	_description = 'General SRM RFX Partner'
	_columns = {
	'partner_id': fields.many2one(label='Partner',obj='md.partner',domain=[('issuplier',)]),
	'state': fields.selection(label='State',selections=[('N','None'),('I','Invite'),('R','Resolve'),('O','Offer'),('B','Backup')]),
	'note': fields.text('Note')}

srm_rfx_partner()

class srm_rfx_type_deadlines(Model):
	_name = 'srm.rfx.type.deadlines'
	_description = 'General SRM RFX Type Deadlines'
	_columns = {
	'name': fields.varchar(label = 'Type'),
	'note': fields.text('Note')}

srm_rfx_type_deadlines()

class srm_rfx_deadlines(Model):
	_name = 'srm.rfx.deadlines'
	_description = 'General SRM RFX Deadlines'
	_order_by = 'start_date asc'
	_columns = {
	'rfx_id': fields.many2one(label = 'Name',obj='srm.rfx'),
	'rfx_type_deadline_id': fields.many2one(label = 'Type',obj='srm.rfx.type.deadlines'),
	'start_date': fields.datetime(label='Start',required=True),
	'end_date': fields.datetime(label='End',required=True),
	'note': fields.text('Note')}

srm_rfx_deadlines()

class srm_rfx_items(Model):
	_name = 'srm.rfx.items'
	_description = 'General SRM Contract Items'
	_columns = {
	'rfx_id': fields.many2one(obj = 'srm.rfx',label = 'RFX'),
	'part_id': fields.many2one(obj = 'srm.part',label = 'Part'),
	'note': fields.text('Note')}

srm_rfx_items()

class srm_auction(Model):
	_name = 'srm.auction'
	_description = 'General SRM Auction'
	_inherits = {'srm.common':{'_methods':['copy_into','copy_from']}}
	_date = 'doa'
	_columns = {
	'name': fields.varchar(label = 'Name',selectable = True),
	'company': fields.many2one(label='Company',obj='md.company'),
	'category_id': fields.many2one(label='Category',obj='srm.auction.category'),
	'origin': fields.varchar(label = 'Origin'),
	'doa': fields.date(label='Date Of Auction',required=True),
	'from_date': fields.date(label='From Date Of Auction',required=True),
	'to_date': fields.date(label='To Date Of Auction',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('issuplier',)]),
	'route_id': fields.many2one(label='Route',obj='srm.routes'),
	'items': fields.one2many(label='Items',obj='srm.auction.items',rel='auction_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.auction.deadlines',rel='auction_id'),
	'partners': fields.one2many(label='Partners',obj='srm.auction.partner',rel='auction_id'),
	'note': fields.text('Note')}

srm_auction()

class srm_auction_partner(Model):
	_name = 'srm.auction.partner'
	_description = 'General SRM Auction Partner'
	_columns = {
	'auction_id': fields.many2one(label = 'Auction',obj='srm.auction'),
	'partner_id': fields.many2one(label='Partner',obj='md.partner',domain=[('issuplier',)]),
	'state': fields.selection(label='State',selections=[('N','None'),('I','Invite'),('R','Resolve'),('O','offer'),('B','Backup')]),
	'note': fields.text('Note')}


class srm_auction_type_deadlines(Model):
	_name = 'srm.auction.type.deadlines'
	_description = 'General SRM Auction Type Deadlines'
	_columns = {
	'name': fields.varchar(label = 'Type'),
	'note': fields.text('Note')}

srm_auction_type_deadlines()

class srm_auction_deadlines(Model):
	_name = 'srm.auction.deadlines'
	_description = 'General SRM Auction Deadlines'
	_order_by = 'start_date asc'
	_columns = {
	'auction_id': fields.many2one(label = 'Auction',obj='srm.auction'),
	'auction_type_deadline_id': fields.many2one(label = 'Type',obj='srm.auction.type.deadlines'),
	'start_date': fields.datetime(label='Start',required=True),
	'end_date': fields.datetime(label='Start',required=True),
	'note': fields.text('Note')}

srm_auction_deadlines()

class srm_auction_items(Model):
	_name = 'srm.auction.items'
	_description = 'General SRM Auction Items'
	_columns = {
	'auction_id': fields.many2one(obj = 'srm.auction',label = 'Auction'),
	'part_id': fields.many2one(obj = 'srm.part',label = 'Part'),
	'note': fields.text('Note')}

srm_auction_items()

class srm_offer_types(Model):
	_name = 'srm.offer.types'
	_description = 'General Model Types SRM Offer'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='srm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='srm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='srm.offer.type.roles',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

srm_offer_types()

class srm_offer_type_roles(Model):
	_name = 'srm.offer.type.roles'
	_description = 'General Model Role SRM Offer Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.offer.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_offer_type_roles()

class srm_offer(Model):
	_name = 'srm.offer'
	_description = 'General SRM Offer'
	_inherits = {'srm.common':{'_methods':['copy_into','copy_from']},'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'doo'
	_columns = {
	'otype': fields.many2one(label='Type',obj='srm.offer.types',on_change='on_change_otype'),
	'name': fields.varchar(label = 'Offer',selectable = True),
	'company': fields.many2one(label='Company',obj='md.company'),
	'category_id': fields.many2one(label='Category',obj='srm.offer.category'),
	'origin': fields.varchar(label = 'Origin'),
	'doo': fields.date(label='Date Of Offer',required=True),
	'from_date': fields.date(label='From Date Of Offer',required=True),
	'to_date': fields.date(label='To Date Of Offer',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('issuplier',)]),
	'route_id': fields.many2one(label='Route',obj='srm.routes'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'recepture': fields.many2one(label='Recepture',obj='md.recepture',domain=[('usage','=','p'),'|',('usage','=','a')]),
	'items': fields.one2many(label='Items',obj='srm.offer.items',rel='offer_id'),
	'roles': fields.one2many(label='Roles',obj='srm.offer.roles',rel='offer_id'),
	'texts': fields.one2many(label='Texts',obj='srm.offer.texts',rel='offer_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.offer.deadlines',rel='offer_id'),
	'note': fields.text('Note')}

	def _on_change_otype(self,cr,pool,uid,item,context={}):		
			roles = pool.get('srm.offer.type.roles').select(cr,pool.uid,['role_id'],[('type_id','=',item['dtype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]

srm_offer()

class srm_offer_texts(Model):
	_name = 'srm.offer.texts'
	_description = 'General Model SRM Offer Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'offer_id': fields.many2one(label='Offer',obj='srm.offer'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_offer_texts()

class srm_offer_roles(Model):
	_name = 'srm.offer.roles'
	_description = 'General Model SRM Offer Roles'
	_columns = {
	'offer_id': fields.many2one(label = 'Offer',obj='srm.offer'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_offer_roles()

class srm_offer_type_deadlines(Model):
	_name = 'srm.offer.type.deadlines'
	_description = 'General SRM Offer Type Deadlines'
	_columns = {
	'name': fields.varchar(label='Type Deadlines',selectable=True),
	'note': fields.text(label='Note')
	}

srm_offer_type_deadlines()

class srm_offer_deadlines(Model):
	_name = 'srm.offer.deadlines'
	_description = 'General SRM Offer Deadlines'
	_order_by = 'start_date asc'
	_columns = {
	'offer_id': fields.many2one(label = 'offer',obj='srm.offer'),
	'offer_type_deadline_id': fields.many2one(label = 'Type',obj='srm.offer.type.deadlines'),
	'start_date': fields.datetime(label='Start',required=True),
	'end_date': fields.datetime(label='End',required=True),
	'note': fields.text('Note')}

srm_offer_deadlines()

class srm_offer_items(Model):
	_name = 'srm.offer.items'
	_description = 'General SRM Offer Items'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'offer_id': fields.many2one(obj = 'srm.offer',label = 'offer'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='VAT Code',obj='md.vat.code',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'delivery_schedules': fields.one2many(label='Delivery Schedules',obj='srm.offer.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='srm.offer.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='srm.offer.item.texts',rel='item_id'),
	'note': fields.text('Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.purchase.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
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

class srm_offer_item_texts(Model):
	_name = 'srm.offer.item.texts'
	_description = 'General Model SRM Offer Item Texts'
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
	_description = 'General Model SRM Offer Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.offer.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_offer_item_roles()

class srm_offer_delivery_schedules(Model):
	_name = 'srm.offer.delivery.schedules'
	_description = 'General SRM Offer Delivery Schedules'
	_date = "schedule"
	_columns = {
	'item_id': fields.many2one(obj = 'srm.offer.items',label = 'offer Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')}

srm_offer_delivery_schedules()

# start evolution
# Types & Roles
class srm_evolution_types(Model):
	_name = 'srm.evolution.types'
	_description = 'General Model Types SRM Evolution'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='srm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='srm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='srm.evolution.type.roles',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

srm_evolution_types()

class srm_evolution_type_roles(Model):
	_name = 'srm.evolution.type.roles'
	_description = 'General Model Role SRM Evolution Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.evolution.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_evolution_type_roles()

# Types & Roles
class srm_evolution(Model):
	_name = 'srm.evolution'
	_description = 'General SRM Evolution'
	_inherits = {'srm.common':{'_methods':['copy_into','copy_from']},'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'doe'
	_columns = {
	'etype': fields.many2one(label='Type',obj='srm.evolution.types',on_change='on_change_etype'),
	'name': fields.varchar(label = 'Evolution',selectable = True),
	'company': fields.many2one(label='Company',obj='md.company'),
	'category_id': fields.many2one(label='Category',obj='srm.evolution.category'),
	'origin': fields.varchar(label = 'Origin'),
	'doe': fields.date(label='Date Of Evolution',required=True),
	'from_date': fields.date(label='From Date Of Evolution',required=True),
	'to_date': fields.date(label='To Date Of Evolution',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('issuplier',)]),
	'route_id': fields.many2one(label='Route',obj='srm.routes'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'recepture': fields.many2one(label='Recepture',obj='md.recepture',domain=[('usage','=','p'),'|',('usage','=','a')]),
	'items': fields.one2many(label='Items',obj='srm.evolution.items',rel='evolution_id'),
	'roles': fields.one2many(label='Roles',obj='srm.evolution.roles',rel='evolution_id'),
	'texts': fields.one2many(label='Texts',obj='srm.evolution.texts',rel='evolution_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.evolution.deadlines',rel='evolution_id'),
	'note': fields.text('Note')}

	def _on_change_etype(self,cr,pool,uid,item,context={}):		
			roles = pool.get('srm.evolution.type.roles').select(cr,pool.uid,['role_id'],[('type_id','=',item['dtype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]

srm_evolution()

class srm_evolution_texts(Model):
	_name = 'srm.evolution.texts'
	_description = 'General Model SRM Evolution Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'evolution_id': fields.many2one(label='Evolution',obj='srm.evolution'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_evolution_texts()

class srm_evolution_roles(Model):
	_name = 'srm.evolution.roles'
	_description = 'General Model SRM Evolution Roles'
	_columns = {
	'evolution_id': fields.many2one(label = 'Evolution',obj='srm.evolution'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_evolution_roles()


class srm_evolution_type_deadlines(Model):
	_name = 'srm.evolution.type.deadlines'
	_description = 'General SRM Evolution Type Deadlines'
	_columns = {
	'name': fields.varchar(label = 'Type'),
	'note': fields.text('Note')}

srm_evolution_type_deadlines()

class srm_evolution_deadlines(Model):
	_name = 'srm.evolution.deadlines'
	_description = 'General SRM Evolution Deadlines'
	_order_by = 'start_date asc'
	_columns = {
	'evolution_id': fields.many2one(label = 'Evolution',obj='srm.evolution'),
	'evolution_type_deadline_id': fields.many2one(label = 'Type',obj='srm.evolution.type.deadlines'),
	'start_date': fields.datetime(label='Start',required=True),
	'end_date': fields.datetime(label='End',required=True),
	'note': fields.text('Note')}

srm_evolution_deadlines()

class srm_evolution_items(Model):
	_name = 'srm.evolution.items'
	_description = 'General SRM Evolution Item'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'evolution_id': fields.many2one(obj = 'srm.evolution',label = 'Evolution'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='VAT Code',obj='md.vat.code',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'delivery_schedules': fields.one2many(label='Delivery Schedules',obj='srm.evolution.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='srm.evolution.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='srm.evolution.item.texts',rel='item_id'),

	'note': fields.text('Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.purchase.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
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

class srm_evolution_item_texts(Model):
	_name = 'srm.evolution.item.texts'
	_description = 'General Model SRM Evolution Item Texts'
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
	_description = 'General Model SRM Evolution Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.evolution.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_evolution_item_roles()

class srm_evolution_delivery_schedules(Model):
	_name = 'srm.evolution.delivery.schedules'
	_description = 'General SRM Evolution Delivery Schedules'
	_date = "schedule"
	_columns = {
	'item_id': fields.many2one(obj = 'srm.evolution.items',label = 'Evolution Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')}

srm_evolution_delivery_schedules()

# Types & Roles
class srm_decision_types(Model):
	_name = 'srm.decision.types'
	_description = 'General Model Types SRM Decision'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='srm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='srm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='srm.decision.type.roles',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

srm_decision_types()

class srm_decision_type_roles(Model):
	_name = 'srm.decision.type.roles'
	_description = 'General Model Role SRM Decision Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.decision.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_decision_type_roles()

# Types & Roles

class srm_decision(Model):
	_name = 'srm.decision'
	_description = 'General SRM Decision'
	_inherits = {'srm.common':{'_methods':['copy_into','copy_from']},'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'don'
	_columns = {
	'dtype': fields.many2one(label='Type',obj='srm.decision.types',on_change='on_change_dtype'),
	'name': fields.varchar(label = 'Decision',selectable = True),
	'company': fields.many2one(label='Company',obj='md.company'),
	'category_id': fields.many2one(label='Category',obj='srm.decision.category'),
	'origin': fields.varchar(label = 'Origin'),
	'don': fields.date(label='Date Of Decision',required=True),
	'from_date': fields.date(label='From Date Of Decision',required=True),
	'to_date': fields.date(label='To Date Of Decision',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('issuplier',)]),
	'route_id': fields.many2one(label='Route',obj='srm.routes'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'recepture': fields.many2one(label='Recepture',obj='md.recepture',domain=[('usage','=','p'),'|',('usage','=','a')]),
	'items': fields.one2many(label='Items',obj='srm.decision.items',rel='decision_id'),
	'roles': fields.one2many(label='Roles',obj='srm.decision.roles',rel='evolution_id'),
	'texts': fields.one2many(label='Texts',obj='srm.decision.texts',rel='evolution_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.decision.deadlines',rel='decision_id'),
	'note': fields.text(label='Note')}

	def _on_change_dtype(self,cr,pool,uid,item,context={}):		
			roles = pool.get('srm.decision.type.roles').select(cr,pool.uid,['role_id'],[('type_id','=',item['dtype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]


srm_decision()

class srm_decision_texts(Model):
	_name = 'srm.decision.texts'
	_description = 'General Model SRM Decision Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'decision_id': fields.many2one(label='Decision',obj='srm.decision'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='srm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

srm_decision_texts()


class srm_decision_roles(Model):
	_name = 'srm.decision.roles'
	_description = 'General Model SRM Decision Roles'
	_columns = {
	'evolution_id': fields.many2one(label = 'Decision',obj='srm.decision'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_decision_roles()


class srm_decision_type_deadlines(Model):
	_name = 'srm.decision.type.deadlines'
	_description = 'General SRM Decision Type Deadlines'
	_columns = {
	'name': fields.varchar(label = 'Type'),
	'note': fields.text(label='Note')}

srm_decision_type_deadlines()

class srm_decision_deadlines(Model):
	_name = 'srm.decision.deadlines'
	_description = 'General SRM Decision Deadlines'
	_order_by = 'start_date asc'
	_columns = {
	'decision_id': fields.many2one(label = 'Decision',obj='srm.decision'),
	'decision_type_deadline_id': fields.many2one(label = 'Type',obj='srm.decision.type.deadlines'),
	'start_date': fields.datetime(label='Start',required=True),
	'end_date': fields.datetime(label='End',required=True),
	'note': fields.text(label='Note')}

srm_decision_deadlines()

class srm_decision_items(Model):
	_name = 'srm.decision.items'
	_description = 'General SRM Decision Items'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'decision_id': fields.many2one(obj = 'srm.decision',label = 'Decision'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='VAT Code',obj='md.vat.code',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'delivery_schedules': fields.one2many(label='Delivery Schedules',obj='srm.decision.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='srm.decision.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='srm.decision.item.texts',rel='item_id'),
	'note': fields.text('Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.purchase.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
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

class srm_decision_item_texts(Model):
	_name = 'srm.decision.item.texts'
	_description = 'General Model SRM Decision Item Texts'
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
	_description = 'General Model SRM Decision Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.decision.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_decision_item_roles()


class srm_decision_delivery_schedules(Model):
	_name = 'srm.decision.delivery.schedules'
	_description = 'General SRM Decision Delivery Schedules'
	_date = "schedule"
	_columns = {
	'item_id': fields.many2one(obj = 'srm.decision.items',label = 'Decision Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')}

srm_decision_delivery_schedules()

# end decision
# Types & Roles
class srm_contract_types(Model):
	_name = 'srm.contract.types'
	_description = 'General Model Types SRM Contact'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='srm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='srm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='srm.contract.type.roles',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

srm_contract_types()

class srm_contract_type_roles(Model):
	_name = 'srm.contract.type.roles'
	_description = 'General Model Role SRM Contact Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='srm.contract.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

srm_contract_type_roles()

# Types & Roles

class srm_contracts(Model):
	_name = 'srm.contracts'
	_description = 'General SRM Contract'
	_inherits = {'srm.common':{'_methods':['copy_into','copy_from']},'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'doc'
	_columns = {
	'ctype': fields.many2one(label='Type',obj='srm.contract.types',on_change='on_change_ctype'),
	'name': fields.varchar(label = 'Name',selectable = True),
	'company': fields.many2one(label='Company',obj='md.company'),
	'category_id': fields.many2one(label='Category',obj='srm.contract.category'),
	'origin': fields.varchar(label = 'Origin'),
	'doc': fields.date(label='Date Of Contract',required=True),
	'from_date': fields.date(label='From Date Of Contract',required=True),
	'to_date': fields.date(label='To Date Of Contract',required=True),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('issuplier',)]),
	'route_id': fields.many2one(label='Route',obj='srm.routes'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'recepture': fields.many2one(label='Recepture',obj='md.recepture',domain=[('usage','=','p'),'|',('usage','=','a')]),
	'items': fields.one2many(label='Items',obj='srm.contract.items',rel='contract_id'),
	'roles': fields.one2many(label='Roles',obj='srm.contract.roles',rel='contract_id'),
	'texts': fields.one2many(label='Texts',obj='srm.contract.texts',rel='contract_id'),
	'payments': fields.one2many(label='Payments',obj='srm.contract.payment.schedules',rel='contarct_id'),
	'deadlines': fields.one2many(label='Deadlines',obj='srm.contract.deadlines',rel='contract_id'),
	'note': fields.text('Note')}

	def _on_change_ctype(self,cr,pool,uid,item,context={}):		
			roles = pool.get('srm.contract.type.roles').select(cr,pool.uid,['role_id'],[('type_id','=',item['dtype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]


srm_contracts()

class srm_contract_texts(Model):
	_name = 'srm.contract.texts'
	_description = 'General Model SRM Contact Texts'
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

class srm_contract_payment_schedules(Model):
	_name = 'srm.contract.payment.schedules'
	_description = 'General Model SRM Contract Payment Schedules'
	_columns = {
	'contract_id': fields.many2one(label='Contract',obj='srm.contracts'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_contract_payment_schedules()

class srm_contract_roles(Model):
	_name = 'srm.contract.roles'
	_description = 'General Model SRM Contact Roles'
	_columns = {
	'contract_id': fields.many2one(label = 'Contract',obj='srm.contracts'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_contract_roles()


class srm_contract_type_deadlines(Model):
	_name = 'srm.contract.type.deadlines'
	_description = 'General SRM Contract Type Deadlines'
	_columns = {
	'name': fields.varchar(label = 'Type'),
	'note': fields.text('Note')}

srm_contract_type_deadlines()

class srm_contract_deadlines(Model):
	_name = 'srm.contract.deadlines'
	_description = 'General SRM Contract Deadlines'
	_order_by = 'start_date asc'
	_columns = {
	'contract_id': fields.many2one(label = 'Name',obj='srm.contracts'),
	'contract_type_deadline_id': fields.many2one(label = 'Type',obj='srm.contract.type.deadlines'),
	'start_date': fields.datetime(label='Start',required=True),
	'end_date': fields.datetime(label='End',required=True),
	'note': fields.text('Note')}

srm_contract_deadlines()

class srm_contract_items(Model):
	_name = 'srm.contract.items'
	_description = 'General SRM Contract Items'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'contract_id': fields.many2one(obj = 'srm.contracts',label = 'Contract'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='VAT Code',obj='md.vat.code',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'currency': fields.referenced(label='Currency',ref='contract_id.currency'),
	'delivery_schedules': fields.one2many(label='Delivery Schedules',obj='srm.contract.delivery.schedules',rel='contract_item_id'),
	'payments': fields.one2many(label='Payments',obj='srm.contract.item.payment.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='srm.contract.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='srm.contract.item.texts',rel='item_id'),
	'note': fields.text('Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.purchase.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
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

class srm_contract_item_texts(Model):
	_name = 'srm.contract.item.texts'
	_description = 'General Model SRM Contact Item Texts'
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
	_description = 'General Model SRM Contact Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.contract.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

srm_contract_item_roles()


class srm_contract_delivery_schedules(Model):
	_name = 'srm.contract.delivery.schedules'
	_description = 'General SRM Contract Delivery Schedules'
	_date = "schedule"
	_columns = {
	'contract_item_id': fields.many2one(obj = 'srm.contract.items',label = 'Contract Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')}

srm_contract_delivery_schedules()

class srm_contarct_item_payment_schedules(Model):
	_name = 'srm.contract.item.payment.schedules'
	_description = 'General Model SRM Contract Item Payment Schedules'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='srm.contract.items'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

srm_contarct_item_payment_schedules()


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
	'categories': fields.one2many(label='Categories',obj='srm.partner.validation.category',rel='parner_validation_id'),
	'products': fields.one2many(label='Products',obj='srm.partner.validation.product',rel='parner_validation_id')}

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
