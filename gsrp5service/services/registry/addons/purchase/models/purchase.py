from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

from decimal import Decimal

from datetime import datetime
from datetime import timedelta

#customize
# Organization structure
class purchase_unit_categories(Model):
	_name = 'purchase.unit.categories'
	_description = 'General Model Categories Purchase Unit'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='purchase.unit.categories'),
	'childs_id': fields.one2many(obj = 'purchase.unit.categories',rel = 'parent_id',label = 'Childs'),
	'units': fields.one2many(label='Units',obj='purchase.units',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

purchase_unit_categories()


class purchase_units(Model):
	_name = 'purchase.units'
	_description = 'General Model Purchase Units'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='purchase.unit.categories'),
	'company_id': fields.many2many(label='Companies',obj='md.company', rel='md_company_purchase_unit_rel', id2='unit_id', id1='company_id'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'channels': fields.one2many(label='Channels',obj='purchase.unit.channel.assigments',rel='unit_id'),
	'segments': fields.one2many(label='Segments',obj='purchase.unit.segment.assigments',rel='unit_id'),
	'areas': fields.one2many(label='Areas',obj='purchase.unit.area.assigments',rel='unit_id'),
	'regions': fields.one2many(label='Regions',obj='purchase.unit.region.assigments',rel='unit_id')
	}

purchase_units()

class purchase_channel_categories(Model):
	_name = 'purchase.channel.categories'
	_description = 'General Model Categories Purchase Chanel'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='purchase.channel.categories'),
	'childs_id': fields.one2many(obj = 'purchase.channel.categories',rel = 'parent_id',label = 'Childs'),
	'channels': fields.one2many(label='Channels',obj='purchase.channels',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

purchase_channel_categories()


class purchase_channels(Model):
	_name = 'purchase.channels'
	_description = 'General Model Purchase Channels'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='purchase.channel.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

purchase_channels()

class purchase_segment_categories(Model):
	_name = 'purchase.segment.categories'
	_description = 'General Model Categories Purchase Segment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='purchase.segment.categories'),
	'childs_id': fields.one2many(obj = 'purchase.segment.categories',rel = 'parent_id',label = 'Childs'),
	'segments': fields.one2many(label='Segments',obj='purchase.segments',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

purchase_segment_categories()


class purchase_segments(Model):
	_name = 'purchase.segments'
	_description = 'General Model Purchase Segments'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='purchase.segment.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

purchase_segments()

class purchase_area_categories(Model):
	_name = 'purchase.area.categories'
	_description = 'General Model Categories Purchase Area'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='purchase.area.categories'),
	'childs_id': fields.one2many(obj = 'purchase.area.categories',rel = 'parent_id',label = 'Childs'),
	'areas': fields.one2many(label='Areas',obj='purchase.areas',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

purchase_area_categories()


class purchase_areas(Model):
	_name = 'purchase.areas'
	_description = 'General Model Purchase Areas'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='purchase.area.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

purchase_areas()

class purchase_region_categories(Model):
	_name = 'purchase.region.categories'
	_description = 'General Model Categories Purchase Region'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='purchase.region.categories'),
	'childs_id': fields.one2many(obj = 'purchase.region.categories',rel = 'parent_id',label = 'Childs'),
	'segments': fields.one2many(label='REgions',obj='purchase.regions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

purchase_region_categories()


class purchase_regions(Model):
	_name = 'purchase.regions'
	_description = 'General Model Purchase Regions'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='purchase.region.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

purchase_regions()


class purchase_division_categories(Model):
	_name = 'purchase.division.categories'
	_description = 'General Model Categories Purchase Division'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='purchase.division.categories'),
	'childs_id': fields.one2many(obj = 'purchase.division.categories',rel = 'parent_id',label = 'Childs'),
	'divisions': fields.one2many(label='Divisions',obj='purchase.divisions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

purchase_division_categories()


class purchase_divisions(Model):
	_name = 'purchase.divisions'
	_description = 'General Model Purchase Divisions'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='purchase.division.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'subdivisions': fields.one2many(label='SubDivisions',obj='purchase.division.subdivision.assigments',rel='division_id')
	}

purchase_divisions()

class purchase_subdivision_categories(Model):
	_name = 'purchase.subdivision.categories'
	_description = 'General Model Categories Purchase Subdivision'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='purchase.subdivision.categories'),
	'childs_id': fields.one2many(obj = 'purchase.subdivision.categories',rel = 'parent_id',label = 'Childs'),
	'subdivisions': fields.one2many(label='Orders',obj='purchase.subdivisions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

purchase_subdivision_categories()


class purchase_subdivisions(Model):
	_name = 'purchase.subdivisions'
	_description = 'General Model Purchase Subdivisions'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='purchase.subdivision.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

purchase_subdivisions()

class purchase_unit_channel_assigments(Model):
	_name = 'purchase.unit.channel.assigments'
	_description = 'General Model Purchase Unit Of Channel Assigment'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='purchase.units'),
	'channel_id': fields.many2one(label='Channel',obj='purchase.channels'),
	'descr': fields.referenced(ref='channel_id.descr'),
	}

purchase_unit_channel_assigments()

class purchase_unit_segment_assigments(Model):
	_name = 'purchase.unit.segment.assigments'
	_description = 'General Model Purchase Unit Of Segment Assigment'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='purchase.units'),
	'segment_id': fields.many2one(label='Segment',obj='purchase.segments'),
	'descr': fields.referenced(ref='segment_id.descr'),
	}

purchase_unit_segment_assigments()

class purchase_unit_area_assigments(Model):
	_name = 'purchase.unit.area.assigments'
	_description = 'General Model Purchase Unit Of Area Assigment'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='purchase.units'),
	'area_id': fields.many2one(label='Area',obj='purchase.areas'),
	'descr': fields.referenced(ref='area_id.descr'),
	}

purchase_unit_area_assigments()

class purchase_unit_region_assigments(Model):
	_name = 'purchase.unit.region.assigments'
	_description = 'General Model Purchase Unit Of Region Assigment'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='purchase.units'),
	'region_id': fields.many2one(label='Region',obj='purchase.regions'),
	'descr': fields.referenced(ref='region_id.descr'),
	}

purchase_unit_segment_assigments()



class purchase_division_subdivision_assigments(Model):
	_name = 'purchase.division.subdivision.assigments'
	_description = 'General Model Purchase Division Of Subdivision Assigment'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'division_id': fields.many2one(label='Division',obj='purchase.divisions'),
	'subdivision_id': fields.many2one(label='Subdivision',obj='purchase.subdivisions'),
	'descr': fields.referenced(ref='subdivision_id.descr'),
	}

purchase_division_subdivision_assigments()


class purchase_markets(Model):
	_name = 'purchase.markets'
	_description = 'General Model Purchase Market'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_rec_name = 'fullname'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='purchase.units', required = True),
	'channel_id': fields.related(label='Channel',obj='purchase.unit.channel.assigments', relatedy=['unit_id'], required = True),
	'segment_id': fields.related(label='Segment',obj='purchase.unit.segment.assigments', relatedy=['unit_id'], required = True),
	'area_id': fields.related(label='Area',obj='purchase.unit.area.assigments', relatedy=['unit_id'], required = True),
	'region_id': fields.related(label='Region',obj='purchase.unit.region.assigments', relatedy=['unit_id'], required = True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname'),
	'note': fields.text(label='Note'),
	}

	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''
		if 'unit_id' in item and 'name' in item['unit_id'] and item['unit_id']['name']:
			v += item['unit_id']['name']

		if 'channel_id' in item and 'name' in item['channel_id'] and item['channel_id']['name']:
			v += '/' + item['channel_id']['name']

		if 'segment_id' in item and 'name' in item['segment_id'] and item['segment_id']['name']:
			v += '/' + item['segment_id']['name']

		if 'area_id' in item and 'name' in item['area_id'] and item['area_id']['name']:
			v += '/' + item['are_id']['name']

		if 'region_id' in item and 'name' in item['region_id'] and item['region_id']['name']:
			v += '/' + item['region_id']['name']

		
		if len(v) > 0:
			item['fullname'] = v


purchase_markets()


class purchase_teams(Model):
	_name = 'purchase.teams'
	_description = 'General Model Purchase Teams'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_rec_name = 'fullname'
	_columns = {
	'division_id': fields.many2one(label='Division',obj='purchase.divisions', required = True),
	'subdivision_id': fields.related(label='Subdivision',obj='purchase.subdivisions', relatedy=['division_id'], required = True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname'),
	'note': fields.text(label='Note'),
	}

	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''
		if 'division_id' in item and 'name' in item['division_id'] and item['division_id']['name']:
			v += item['division_id']['name']

		if 'subdivision_id' in item and 'name' in item['subdivision_id'] and item['subdivision_id']['name']:
			v += '/' + item['subdivison_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

purchase_teams()


#Organization structure
#Text
class purchase_texts(Model):
	_name = 'purchase.texts'
	_description = 'General Model Purchase Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

purchase_texts()

class purchase_schema_texts(Model):
	_name = 'purchase.schema.texts'
	_description = 'General Model Schema Of Purchase Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'usage': fields.selection(label='Usage',selections=[('h','Header'),('i','Item'),('b','Both')]),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'texts': fields.one2many(label='Texts',obj='purchase.schema.text.items',rel='schema_id')
	}

purchase_schema_texts()

class purchase_schema_text_items(Model):
	_name = 'purchase.schema.text.items'
	_description = 'General Model Items Of Schema Purchase Texts'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'schema_id': fields.many2one(label = 'Schema',obj='purchase.schema.texts'),
	'seq': fields.integer(label='Sequence'),
	'text_id': fields.many2one(label = 'Text',obj='purchase.texts'),
	'descr': fields.referenced(ref='text_id.descr')
	}

purchase_schema_text_items()

# Text end

class purchase_order_types(Model):
	_name = 'purchase.order.types'
	_description = 'General Model Types Purchase Order'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'otype': fields.selection(label='Type',selections=[('ord','Order'),('ap','Advance Payment'),('ps','Pseduo'),('dm','Debit Request'),('cr','Credit Request'),('rо','Return')]),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='purchase.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='purchase.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='purchase.order.type.roles',rel='type_id'),
	'tis': fields.one2many(label='TIs',obj='purchase.order.type.items',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

purchase_order_types()

class purchase_order_type_roles(Model):
	_name = 'purchase.order.type.roles'
	_description = 'General Model Role Purchase Order Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='purchase.order.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

purchase_order_type_roles()

class purchase_order_type_items(Model):
	_name = 'purchase.order.type.items'
	_description = 'General Model Role Purchase Order Items'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='purchase.order.types'),
	'gti_id': fields.many2one(label = 'GTI',obj='md.gtis'),
	'itype_id': fields.many2one(label = 'Type Of Items',obj='md.type.items',domain=[('usage','=','p'),'|',('usage','=','a')]),
	'note': fields.text(label = 'Note')
	}

purchase_order_type_items()

class purchase_invoice_types(Model):
	_name = 'purchase.invoice.types'
	_description = 'General Model Types Purchase Invoice'
	_class_model = 'C'
	_class_category = 'invoice'
	_columns = {
	'itype': fields.selection(label='Type',selections=[('in','Invoice'),('ap','Advance Payment'),('ps','Pseduo'),('dm','Debit Memo'),('cr','Credit Memo'),('rin','Reversal Invoice'),('rap','Reversal Advance Payment'),('rps','Reversal Pseduo'),('rdm','Reversal Debit Memo'),('rcr','Reversal Credit Memo') ]),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='purchase.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='purchase.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='purchase.invoice.type.roles',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

purchase_invoice_types()

class purchase_invoice_type_roles(Model):
	_name = 'purchase.invoice.type.roles'
	_description = 'General Model Role Purchase Invoice Types'
	_class_model = 'C'
	_class_category = 'invoice'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='purchase.invoice.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

purchase_invoice_type_roles()

# end customize

class purchase_order_categories(Model):
	_name = 'purchase.order.categories'
	_description = 'General Model Categories Purchase Order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='purchase.order.categories'),
	'childs_id': fields.one2many(obj = 'purchase.order.categories',rel = 'parent_id',label = 'Childs'),
	'orders': fields.one2many(label='Orders',obj='purchase.orders',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

purchase_order_categories()

class purchase_invoce_categories(Model):
	_name = 'purchase.invoce.categories'
	_description = 'General Model Categories Purchase Invoce'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='purchase.invoce.categories'),
	'childs_id': fields.one2many(obj = 'purchase.invoce.categories',rel = 'parent_id',label = 'Childs'),
	'invoices': fields.one2many(label='Orders',obj='purchase.invoices',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

purchase_invoce_categories()

class purchase_orders(Model):
	_name = 'purchase.orders'
	_description = 'General Model Purchase Order'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'doo'
	_rec_name = 'fullname'
	_columns = {
	'otype': fields.many2one(label='Type',obj='purchase.order.types',on_change='_on_change_otype', required = True),
	'name': fields.varchar(label = 'Name', required = True),
	'company': fields.many2one(label='Company',obj='md.company', required = True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname'),
	'market_id': fields.many2one(label='Market',obj='purchase.markets'),
	'team_id': fields.many2one(label='Team',obj='purchase.teams'),
	'category_id': fields.many2one(label='Category',obj='purchase.order.categories'),
	'origin': fields.varchar(label = 'Origin'),
	'doo': fields.date(label='Date Of Order',required=True),
	'from_date': fields.date(label='Begin Date Of Order',required=True),
	'to_date': fields.date(label='End Date Of Order',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('issuplier',)]),
	'currency': fields.many2one(label='Currency',obj='md.currency',state={'approved':{'attrs':{'ro':True}}}),
	'incoterms1': fields.many2one(label='Incoterms 1',obj='md.incoterms'),
	'incoterms2': fields.varchar(label = 'Incoterms 2'),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'recepture': fields.many2one(label='Recepture',obj='md.recepture',domain=[('usage','=','p'),'|',('usage','=','a')],on_change='_on_change_recepture'),
	'items': fields.one2many(label='Items',obj='purchase.order.items',rel='order_id'),
	'roles': fields.one2many(label='Roles',obj='purchase.order.roles',rel='order_id'),
	'texts': fields.one2many(label='Texts',obj='purchase.order.texts',rel='order_id'),
	'payments': fields.one2many(label='Payments',obj='purchase.order.payment.schedules',rel='order_id'),
	'note': fields.text('Note')
	}

	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''
		if 'company' in item and 'name' in item['company'] and item['company']['name']:
			v += item['company']['name']

		if 'otype' in item and 'name' in item['otype'] and item['otype']['name']:
			v += '/' + item['otype']['name']

		if item['name']:
			v += '/' + item['name']
		
		if len(v) > 0:
			item['fullname'] = v

	def _on_change_otype(self,cr,pool,uid,item,context={}):		
		roles = pool.get('purchase.order.type.roles').select(cr,pool,uid,['role_id'],[('type_id','=',item['otype']['name'])],context)
		for role in roles:
			item_role = pool.get('purchase.order.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)
		
		types = pool.get('purchase.order.types').select(cr,pool,uid,['htschema'],[('name','=',item['otype']['name'])],context)	
		texts1 = pool.get('purchase.schema.texts').select(cr,pool,uid,['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = pool.get('purchase.order.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

	def _on_change_recepture(self,cr,pool,uid,item,context={}):		
		if item['recepture'] and 'name' in item['recepture'] and item['recepture']['name']:
			p = pool.get('md.recepture.input').select(cr,pool,uid,['product','quantity','uom'],[('recepture_id','=',item['recepture']['name'])],context)
			for i in p:
				ei = pool.get('purchase.order.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.utcnow()+timedelta(3)
				item_items = pool.get('purchase.order.items')._buildEmptyItem()
				item_items['delivery_schedules'].append(ei)
				for f in ('product','uom'):
					item_items[f] = i[f]
				item_items['price'] = 0.00
				item['items'].append(item_items)
				
		return None

	def _act_copy_to(self,cr,pool,uid,column,record,context={}):				
		return 'Copy to'

	def _act_copy_from(self,cr,pool,uid,column,record,context={}):				
		return 'Copy from'


	_actions = {'copy_to':{'label':'Copy To Model','tooltip':'Copy to other model','method':'_act_copy_to','icon':'add'},'copy_from':{'label':'Copy From Model','tooltip':'Copy from other model','method':'_act_copy_from','icon':'list'}}

	_default = {
		'state':'draft',
		'otype':'ord'
	}

purchase_orders()

class purchase_order_texts(Model):
	_name = 'purchase.order.texts'
	_description = 'General Model Purchase Order Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'order_id': fields.many2one(label='Order',obj='purchase.orders'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='purchase.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

purchase_order_texts()


class purchase_order_roles(Model):
	_name = 'purchase.order.roles'
	_description = 'General Model Purchase Order Roles'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='purchase.orders'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

purchase_order_roles()

class purchase_order_payment_schedules(Model):
	_name = 'purchase.order.payment.schedules'
	_description = 'General Model Purchase Order Payment Schedules'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='purchase.orders'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

purchase_order_payment_schedules()


class purchase_order_items(Model):
	_name = 'purchase.order.items'
	_description = 'General Model Purchase Order Items'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'order_id': fields.many2one(obj = 'purchase.orders',label = 'Purchase Order'),
	'itype_id': fields.many2one(label='Group Of Type Items', obj='md.type.items',domain=[('usage','in',('p','a'))]),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'volume': fields.float(label='Volume', readonly=True),
	'volume_total': fields.float(label='Volume Total', readonly=True),
	'volume_uom': fields.many2one(label="Volume UoM",obj='md.uom', readonly=True,domain=[('quantity_id','=','Volume')]),
	'weight': fields.float(label='Weight', readonly=True),
	'weight_total': fields.float(label='Weight Total', readonly=True),
	'weight_uom': fields.many2one(label="Weight UoM",obj='md.uom', readonly=True,domain=[('quantity_id','=','Weight')]),
	'delivery_schedules': fields.one2many(label='Delivery Schedule',obj='purchase.order.item.delivery.schedules',rel='item_id'),
	'payments': fields.one2many(label='Payments',obj='purchase.order.item.payment.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='purchase.order.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='purchase.order.item.texts',rel='item_id'),
	'note': fields.text(label = 'Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			i = pool.get('purchase.order.type.items').select(cr,pool,uid,['gti_id','itype_id'],[],context)
			gti = {}
			if len(i) > 0:
				for r in i:
					gti[r['gti_id']['name']] = r['itype_id']
			p = pool.get('md.product').select(cr,pool,uid,['name','gti','volume','volume_uom','weight','weight_uom',{'purchase':['vat','uom','price','currency','unit','uop']}],[('name','=',item['product']['name'])],context)
			if len(p) > 0:
				for f in ('gti','volume','volume_uom','weight','weight_uom','purchase'):
					if f == 'purchase':
						if len(p[0][f]) > 0:
							d = p[0][f][0]
							for m in ('uom','price','currency','unit','uop','vat'):
								if m not in item or item[m] != d[m]:
									if m == 'vat':
										item['vat_code'] = d['vat']				
									else:
										item[m] = d[m]
					else:
						if f == 'gti':
							if p[0]['gti']['name'] in gti:
								item['itype_id'] = gti[p[0][f]['name']]
						else:
							if f not in item or item[f] != p[0][f]:
								item[f] = p[0][f]

			else:
				for f in ('vat_code','uom','price','currency','unit','uop'):
					if f in ('price','unit'):
						if f in self._default:
							item[f] = self._default[f]
						else:
							item[f] = None
					else:
						item[f] = {'id':None,'name':None}

		return None

	def _trgForEachRowBeforeInsertIB1(self,cr,pool,uid,record,context):
		print('Triger For Each Row Before Insert')

	def _trgForEachRowAfterInsertIA1(self,cr,pool,uid,record,context):
		print('Triger For Each Row After Insert')

	def _trgBeforeInsertIBA1(self,cr,pool,uid,records,context):
		print('Triger Before Insert')

	def _trgAfterInsertIAA1(self,cr,pool,uid,records,context):
		print('Triger After Insert')

#
	def _trgForEachRowBeforeUpdateUB1(self,cr,pool,uid,record,context):
		print('Triger For Each Row Before Update')

	def _trgForEachRowAfterUpdateUA1(self,cr,pool,uid,record,context):
		print('Triger For Each Row After Update')

	def _trgBeforeUpdateUBA1(self,cr,pool,uid,records,context):
		print('Triger Before Update')

	def _trgAfterUpdateIUA1(self,cr,pool,uid,records,context):
		print('Triger After Update')
#
	def _trgForEachRowBeforeDeleteDB1(self,cr,pool,uid,oid,context):
		print('Triger For Each Row Before Delete')

	def _trgForEachRowAfterDeleteDA1(self,cr,pool,uid,oid,context):
		print('Triger For Each Row After Delete')

	def _trgBeforeDeleteDBA1(self,cr,pool,uid,oids,context):
		print('Triger Before Delete')

	def _trgAfterDeleteDA1(self,cr,pool,uid,oids,context):
		print('Triger After Delete')



	_default = {
		'unit': 1
	}

purchase_order_items()

class purchase_order_item_texts(Model):
	_name = 'purchase.order.item.texts'
	_description = 'General Model Purchase Order Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='purchase.order.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='purchase.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

purchase_order_item_texts()


class purchase_order_item_roles(Model):
	_name = 'purchase.order.item.roles'
	_description = 'General Model Purchase Order Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='purchase.order.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

purchase_order_item_roles()

class purchase_order_item_delivery_schedules(Model):
	_name = 'purchase.order.item.delivery.schedules'
	_description = 'General Model Purchase Order Item Delivery Schedules'
	_columns = {
	'item_id': fields.many2one(obj = 'purchase.order.items',label = 'Order Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
	}

purchase_order_item_delivery_schedules()

class purchase_order_item_payment_schedules(Model):
	_name = 'purchase.order.item.payment.schedules'
	_description = 'General Model Purchase Order Item Payment Schedules'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='purchase.order.items'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

purchase_order_item_payment_schedules()


# Invoice
class purchase_invoices(Model):
	_name = 'purchase.invoices'
	_description = 'General Model Purchase Invoice'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'doi'
	_rec_name = 'fullname'
	_columns = {
	'itype': fields.many2one(label='Type',obj='purchase.invoice.types',on_change='on_change_itype'),
	'name': fields.varchar(label = 'Name'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname'),
	'category_id': fields.many2one(label='Category',obj='purchase.invoce.categories'),
	'origin': fields.varchar(label = 'Origin'),
	'doi': fields.date(label='Date Of Invoice',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('iscustomer',)]),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'incoterms1': fields.many2one(label='Incoterms 1',obj='md.incoterms'),
	'incoterms2': fields.varchar(label = 'Incoterms 2'),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'items': fields.one2many(label='Items',obj='purchase.invoice.items',rel='invoice_id'),
	'roles': fields.one2many(label='Roles',obj='purchase.invoice.roles',rel='invoice_id'),
	'texts': fields.one2many(label='Texts',obj='purchase.invoice.texts',rel='invoice_id'),
	'note': fields.text('Note')
	}

	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''
		if 'company' in item and 'name' in item['company'] and item['company']['name']:
			v += item['company']['name']

		if 'itype' in item and 'name' in item['itype'] and item['itype']['name']:
			v += '/' + item['itype']['name']

		if item['name']:
			v += '/' + item['name']
		
		if len(v) > 0:
			item['fullname'] = v

	def _on_change_itype(self,cr,pool,uid,item,context={}):		
			roles = pool.get('purchase.invoice.type.roles').select(cr,pool.uid,['role_id'],[('type_id','=',item['otype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]


	_default = {
		'state':'draft',
		'itype':'in'
	}

purchase_invoices()

class purchase_invoice_texts(Model):
	_name = 'purchase.invoice.texts'
	_description = 'General Model Purchase Invoce Texts'
	_class_model = 'C'
	_class_category = 'invoice'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'invoice_id': fields.many2one(label='Order',obj='purchase.invoices'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='purchase.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

purchase_invoice_texts()


class purchase_invoice_roles(Model):
	_name = 'purchase.invoice.roles'
	_description = 'General Model Purchase Invoice Roles'
	_columns = {
	'invoice_id': fields.many2one(label = 'Invoice',obj='purchase.invoices'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

purchase_invoice_roles()

class purchase_invoice_items(Model):
	_name = 'purchase.invoice.items'
	_description = 'General Model Purchase Invoice Items'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'invoice_id': fields.many2one(obj = 'purchase.invoices',label = 'Invoice'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('s','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'delivery_schedules': fields.one2many(label='Delivery Schedule',obj='purchase.invoce.item.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='purchase.invoice.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='purchase.invoice.item.texts',rel='item_id'),
	'note': fields.text(label = 'Note')
	}

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

purchase_invoice_items()

class purchase_invoice_item_texts(Model):
	_name = 'purchase.invoice.item.texts'
	_description = 'General Model Purchase Invoce Item Texts'
	_class_model = 'C'
	_class_category = 'invoice'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='purchase.invoice.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='purchase.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

purchase_invoice_item_texts()


class purchase_invoice_item_roles(Model):
	_name = 'purchase.invoice.item.roles'
	_description = 'General Model Purchase Invoice Item Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='purchase.invoice.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

purchase_invoice_item_roles()

class purchase_invoce_item_delivery_schedules(Model):
	_name = 'purchase.invoce.item.delivery.schedules'
	_description = 'General Model Purchase Invoice Item Delivery Schedules'
	_columns = {
	'item_id': fields.many2one(obj = 'purchase.invoice.items',label = 'Order Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
	}

purchase_invoce_item_delivery_schedules()

# inherit

class md_purchase_product(Model):
	_name = 'md.purchase.product'
	_description = 'General Model Purchase Of Product'
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

md_purchase_product()

class md_purchase_product_inherit(ModelInherit):
	_name = 'md.purchase.product.inherit'
	_description = 'Genaral Model Inherit For Purchase Product'
	_inherit = {'md.product':{'_columns':['purchase']},'md.recepture':{'_columns':['usage']},'md.type.items':{'_columns':['usage']}}
	_columns = {
		'purchase': fields.one2many(label='Purchase',obj='md.purchase.product',rel='product_id'),
		'usage': fields.iSelection(selections=[('p','Purchase')])
	}
	
md_purchase_product_inherit()
