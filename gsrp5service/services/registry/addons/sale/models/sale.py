from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

from decimal import Decimal

from datetime import datetime
from datetime import timedelta

#customize
# Organization structure
class sale_unit_categories(Model):
	_name = 'sale.unit.categories'
	_description = 'General Model Categories Sale Unit'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='sale.unit.categories'),
	'childs_id': fields.one2many(obj = 'sale.unit.categories',rel = 'parent_id',label = 'Childs'),
	'units': fields.one2many(label='Units',obj='sale.units',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

sale_unit_categories()


class sale_units(Model):
	_name = 'sale.units'
	_description = 'General Model Sale Units'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='sale.unit.categories'),
	'company_id': fields.many2many(label='Companies',obj='md.company', rel='md_company_sale_unit_rel', id2='unit_id', id1='company_id'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'channels': fields.one2many(label='Channels',obj='sale.unit.channel.assigments',rel='unit_id'),
	'segments': fields.one2many(label='Segments',obj='sale.unit.segment.assigments',rel='unit_id'),
	'areas': fields.one2many(label='Areas',obj='sale.unit.area.assigments',rel='unit_id'),
	'regions': fields.one2many(label='Regions',obj='sale.unit.region.assigments',rel='unit_id')
	}

sale_units()

class sale_channel_categories(Model):
	_name = 'sale.channel.categories'
	_description = 'General Model Categories Sale Chanel'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='sale.channel.categories'),
	'childs_id': fields.one2many(obj = 'sale.channel.categories',rel = 'parent_id',label = 'Childs'),
	'channels': fields.one2many(label='Channels',obj='sale.channels',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

sale_channel_categories()


class sale_channels(Model):
	_name = 'sale.channels'
	_description = 'General Model Sale Channels'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='sale.channel.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

sale_channels()

class sale_segment_categories(Model):
	_name = 'sale.segment.categories'
	_description = 'General Model Categories Sale Segment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='sale.segment.categories'),
	'childs_id': fields.one2many(obj = 'sale.segment.categories',rel = 'parent_id',label = 'Childs'),
	'segments': fields.one2many(label='Segments',obj='sale.segments',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

sale_segment_categories()


class sale_segments(Model):
	_name = 'sale.segments'
	_description = 'General Model Sale Segments'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='sale.segment.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

sale_segments()

class sale_area_categories(Model):
	_name = 'sale.area.categories'
	_description = 'General Model Categories Sale Area'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='sale.area.categories'),
	'childs_id': fields.one2many(obj = 'sale.area.categories',rel = 'parent_id',label = 'Childs'),
	'areas': fields.one2many(label='Areas',obj='sale.areas',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

sale_area_categories()


class sale_areas(Model):
	_name = 'sale.areas'
	_description = 'General Model Sale Areas'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='sale.area.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

sale_areas()

class sale_region_categories(Model):
	_name = 'sale.region.categories'
	_description = 'General Model Categories Sale Region'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='sale.region.categories'),
	'childs_id': fields.one2many(obj = 'sale.region.categories',rel = 'parent_id',label = 'Childs'),
	'segments': fields.one2many(label='REgions',obj='sale.regions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

sale_region_categories()


class sale_regions(Model):
	_name = 'sale.regions'
	_description = 'General Model Sale Regions'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='sale.region.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

sale_regions()


class sale_division_categories(Model):
	_name = 'sale.division.categories'
	_description = 'General Model Categories Sale Division'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='sale.division.categories'),
	'childs_id': fields.one2many(obj = 'sale.division.categories',rel = 'parent_id',label = 'Childs'),
	'divisions': fields.one2many(label='Divisions',obj='sale.divisions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

sale_division_categories()


class sale_divisions(Model):
	_name = 'sale.divisions'
	_description = 'General Model Sale Divisions'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='sale.division.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'subdivisions': fields.one2many(label='SubDivisions',obj='sale.division.subdivision.assigments',rel='division_id')
	}

sale_divisions()

class sale_subdivision_categories(Model):
	_name = 'sale.subdivision.categories'
	_description = 'General Model Categories Sale Subdivision'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='sale.subdivision.categories'),
	'childs_id': fields.one2many(obj = 'sale.subdivision.categories',rel = 'parent_id',label = 'Childs'),
	'subdivisions': fields.one2many(label='Orders',obj='sale.subdivisions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

sale_subdivision_categories()


class sale_subdivisions(Model):
	_name = 'sale.subdivisions'
	_description = 'General Model Sale Subdivisions'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='sale.subdivision.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

sale_subdivisions()

class sale_unit_channel_assigments(Model):
	_name = 'sale.unit.channel.assigments'
	_description = 'General Model Sale Unit Of Channel Assigment'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='sale.units'),
	'channel_id': fields.many2one(label='Channel',obj='sale.channels',selectable=True),
	'descr': fields.referenced(ref='channel_id.descr'),
	}

sale_unit_channel_assigments()

class sale_unit_segment_assigments(Model):
	_name = 'sale.unit.segment.assigments'
	_description = 'General Model Sale Unit Of Segment Assigment'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='sale.units'),
	'segment_id': fields.many2one(label='Segment',obj='sale.segments',selectable=True),
	'descr': fields.referenced(ref='segment_id.descr'),
	}

sale_unit_segment_assigments()

class sale_unit_area_assigments(Model):
	_name = 'sale.unit.area.assigments'
	_description = 'General Model Sale Unit Of Area Assigment'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='sale.units'),
	'area_id': fields.many2one(label='Area',obj='sale.areas',selectable=True),
	'descr': fields.referenced(ref='area_id.descr'),
	}

sale_unit_area_assigments()

class sale_unit_region_assigments(Model):
	_name = 'sale.unit.region.assigments'
	_description = 'General Model Sale Unit Of Region Assigment'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='sale.units'),
	'region_id': fields.many2one(label='Region',obj='sale.regions',selectable=True),
	'descr': fields.referenced(ref='region_id.descr'),
	}

sale_unit_segment_assigments()



class sale_division_subdivision_assigments(Model):
	_name = 'sale.division.subdivision.assigments'
	_description = 'General Model Sale Division Of Subdivision Assigment'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'division_id': fields.many2one(label='Division',obj='sale.divisions'),
	'subdivision_id': fields.many2one(label='Subdivision',obj='sale.subdivisions',selectable=True),
	'descr': fields.referenced(ref='subdivision_id.descr'),
	}

sale_division_subdivision_assigments()


class sale_markets(Model):
	_name = 'sale.markets'
	_description = 'General Model Sale Market'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_rec_name = 'fullname'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='sale.units', required = True),
	'channel_id': fields.related(label='Channel',obj='sale.unit.channel.assigments', relatedy=['unit_id'], required = True),
	'segment_id': fields.related(label='Segment',obj='sale.unit.segment.assigments', relatedy=['unit_id'], required = True),
	'area_id': fields.related(label='Area',obj='sale.unit.area.assigments', relatedy=['unit_id'], required = True),
	'region_id': fields.related(label='Region',obj='sale.unit.region.assigments', relatedy=['unit_id'], required = True),
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


sale_markets()


class sale_teams(Model):
	_name = 'sale.teams'
	_description = 'General Model Sale Teams'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_rec_name = 'fullname'
	_columns = {
	'division_id': fields.many2one(label='Division',obj='sale.divisions', required = True),
	'subdivision_id': fields.related(label='Subdivision',obj='sale.subdivisions', relatedy=['division_id'], required = True),
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

sale_teams()


#Organization structure

#Text
class sale_texts(Model):
	_name = 'sale.texts'
	_description = 'General Model Sale Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

sale_texts()

class sale_schema_texts(Model):
	_name = 'sale.schema.texts'
	_description = 'General Model Schema Of Sale Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'usage': fields.selection(label='Usage',selections=[('h','Header'),('i','Item'),('b','Both')]),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'texts': fields.one2many(label='Texts',obj='sale.schema.text.items',rel='schema_id')
	}

sale_schema_texts()

class sale_schema_text_items(Model):
	_name = 'sale.schema.text.items'
	_description = 'General Model Items Of Schema Sale Texts'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'schema_id': fields.many2one(label = 'Schema',obj='sale.schema.texts'),
	'seq': fields.integer(label='Sequence'),
	'text_id': fields.many2one(label = 'Text',obj='sale.texts'),
	'descr': fields.referenced(ref='text_id.descr')
	}

sale_schema_text_items()

# Text end

class sale_order_types(Model):
	_name = 'sale.order.types'
	_description = 'General Model Types Sale Order'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'otype': fields.selection(label='Type',selections=[('ord','Order'),('ap','Advance Payment'),('ps','Pseduo'),('dm','Debit Request'),('cr','Credit Request'),('rо','Return')]),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='sale.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='sale.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='sale.order.type.roles',rel='type_id'),
	'tis': fields.one2many(label='TIs',obj='sale.order.type.items',rel='type_id'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

sale_order_types()

class sale_order_type_roles(Model):
	_name = 'sale.order.type.roles'
	_description = 'General Model Role Sale Order Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='sale.order.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','a'))]),
	'note': fields.text(label = 'Note')
	}

sale_order_type_roles()

class sale_order_type_items(Model):
	_name = 'sale.order.type.items'
	_description = 'General Model Role Sale Order Items'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='sale.order.types'),
	'gti_id': fields.many2one(label = 'GTI',obj='md.gtis'),
	'itype_id': fields.many2one(label = 'Type Of Items',obj='md.type.items',domain=[('usage','=','s'),'|',('usage','=','a')]),
	'note': fields.text(label = 'Note')
	}

sale_order_type_items()


class sale_invoice_types(Model):
	_name = 'sale.invoice.types'
	_description = 'General Model Types Sale Invoice'
	_class_model = 'C'
	_class_category = 'invoice'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='sale.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='sale.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='sale.invoice.type.roles',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

sale_invoice_types()

class sale_invoice_type_roles(Model):
	_name = 'sale.invoice.type.roles'
	_description = 'General Model Role sale Invoice Types'
	_class_model = 'C'
	_class_category = 'invoice'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='sale.invoice.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

sale_invoice_type_roles()

# end customize

class sales_order_categories(Model):
	_name = 'sale.order.categories'
	_description = 'General Model Category Sale Order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='sale.order.categories'),
	'childs_id': fields.one2many(obj = 'sale.order.categories',rel = 'parent_id',label = 'Childs'),
	'orders': fields.one2many(label='Orders',obj='sale.orders',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

sales_order_categories()

class sale_invoice_categories(Model):
	_name = 'sale.invoice.categories'
	_description = 'General Model Category Sale Invoice'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='sale.invoice.categories'),
	'childs_id': fields.one2many(obj = 'sale.invoice.categories',rel = 'parent_id',label = 'Childs'),
	'invoices': fields.one2many(label='Orders',obj='sale.invoices',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

sale_invoice_categories()

class sale_orders(Model):
	_name = 'sale.orders'
	_description = 'General Model Sale Orders'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'doo'
	_columns = {
	'otype': fields.many2one(label='Type',obj='sale.order.types',on_change='_on_change_otype'),
	'company_id': fields.many2one(label='Company',obj='md.company'),
	'name': fields.varchar(label = 'Name'),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname'),
	'market_id': fields.many2one(label='Market',obj='sale.markets'),
	'team_id': fields.many2one(label='Team',obj='sale.teams'),
	'category_id': fields.many2one(label='Category',obj='sale.order.categories'),
	'origin': fields.varchar(label = 'Origin'),
	'doo': fields.date(label='Date Of Order',required=True),
	'from_date': fields.date(label='Begin Date Of Order',required=True),
	'to_date': fields.date(label='End Date Of Order',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('iscustomer',)]),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'incoterms1': fields.many2one(label='Incoterms 1',obj='md.incoterms'),
	'incoterms2': fields.varchar(label = 'Incoterms 2'),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'recepture': fields.many2one(label='Recepture',obj='md.recepture',domain=[('usage','=','s'),'|',('usage','=','a')],on_change='_on_change_recepture'),
	'items': fields.one2many(label='Items',obj='sale.order.items',rel='order_id'),
	'roles': fields.one2many(label='Roles',obj='sale.order.roles',rel='order_id'),
	'texts': fields.one2many(label='Texts',obj='sale.order.texts',rel='order_id'),
	'plates': fields.one2many(label='Plates',obj='sale.order.output.plates',rel='order_id'),
	'payments': fields.one2many(label='Payments',obj='sale.order.payment.schedules',rel='order_id'),
	'note': fields.text('Note')
	}

#
	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''
		if 'company_id' in item and 'name' in item['company_id'] and item['company_id']['name']:
			v += item['company_id']['name']

		if 'otype' in item and 'name' in item['otype'] and item['otype']['name']:
			v += '/' + item['otype']['name']

		if item['name']:
			v += '/' + item['name']
		
		if len(v) > 0:
			item['fullname'] = v

	def _on_change_otype(self,cr,pool,uid,item,context={}):		
		roles = pool.get('sale.order.type.roles').select(cr,pool,uid,['role_id'],[('type_id','=',item['otype']['name'])],context)
		for role in roles:
			item_role = pool.get('sale.order.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)
		
		types = pool.get('sale.order.types').select(cr,pool,uid,['htschema'],[('name','=',item['otype']['name'])],context)	
		texts1 = pool.get('sale.schema.texts').select(cr,pool,uid,['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = pool.get('sale.order.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

	def _on_change_recepture(self,cr,pool,uid,item,context={}):		
		if item['recepture'] and 'name' in item['recepture'] and item['recepture']['name']:
			p = pool.get('md.recepture.output').select(cr,pool,uid,['product','quantity','uom'],[('recepture_id','=',item['recepture']['name'])],context)
			for i in p:
				ei = pool.get('sale.order.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.utcnow()+timedelta(3)
				item_items = pool.get('sale.order.items')._buildEmptyItem()
				item_items['delivery_schedules'].append(ei)
				for f in ('product','uom'):
					item_items[f] = i[f]
				item_items['price'] = 0.00
				item['items'].append(item_items)
				
		return None

#

	_default = {
		'state':'draft'
	}

sale_orders()

class sale_order_texts(Model):
	_name = 'sale.order.texts'
	_description = 'General Model Sale Order Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'order_id': fields.many2one(label='Order',obj='sale.orders'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='sale.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

sale_order_texts()

class sale_order_roles(Model):
	_name = 'sale.order.roles'
	_description = 'General Model Sale Order Roles'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='sale.orders'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

sale_order_roles()

class sale_order_payment_schedules(Model):
	_name = 'sale.order.payment.schedules'
	_description = 'General Model Sale Order Payment Schedules'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='sale.orders'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

sale_order_payment_schedules()

class sale_order_output_plates(Model):
	_name = 'sale.order.output.plates'
	_description = 'General Model Sale Order Output Plates'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='sale.orders'),
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

sale_order_output_plates()



class sale_order_items(Model):
	_name = 'sale.order.items'
	_description = 'General Model Sale Order Items'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'order_id': fields.many2one(obj = 'sale.orders',label = 'Sales Order'),
	'itype_id': fields.many2one(label='Group Of Type Items', obj='md.type.items',domain=[('usage','in',('s','a'))]),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,3)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('s','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'volume': fields.float(label='Volume', readonly=True),
	'volume_total': fields.float(label='Volume Total', readonly=True),
	'volume_uom': fields.many2one(label="Volume UoM",obj='md.uom', readonly=True,domain=[('quantity_id','=','Volume')]),
	'weight': fields.float(label='Weight', readonly=True),
	'weight_total': fields.float(label='Weight Total', readonly=True),
	'weight_uom': fields.many2one(label="Weight UoM",obj='md.uom', readonly=True,domain=[('quantity_id','=','Weight')]),
	'delivery_schedules': fields.one2many(label='Delivery Schedule',obj='sale.order.item.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='sale.order.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='sale.order.item.texts',rel='item_id'),
	'plates': fields.one2many(label='Plates',obj='sale.order.item.output.plates',rel='item_id'),
	'payments': fields.one2many(label='Payments',obj='sale.order.item.payment.schedules',rel='item_id'),
	'note': fields.text(label = 'Note')
	}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			i = pool.get('sale.order.type.items').select(cr,pool,uid,['gti_id','itype_id'],[],context)
			gti = {}
			if len(i) > 0:
				for r in i:
					gti[r['gti_id']['name']] = r['itype_id']
			p = pool.get('md.product').select(cr,pool,uid,['name','gti','volume','volume_uom','weight','weight_uom',{'sale':['vat','uom','price','currency','unit','uop']}],[('name','=',item['product']['name'])],context)
			if len(p) > 0:
				for f in ('gti','volume','volume_uom','weight','weight_uom','sale'):
					if f == 'sale':
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

	_default = {
		'quantity': 1,
		'unit': 1
	}

sale_order_items()

class sale_order_item_texts(Model):
	_name = 'sale.order.item.texts'
	_description = 'General Model Sale Order Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='sale.order.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='sale.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

sale_order_item_texts()


class sale_order_item_roles(Model):
	_name = 'sale.order.item.roles'
	_description = 'General Model Sale Order Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='sale.order.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

sale_order_item_roles()


class sale_order_item_delivery_schedules(Model):
	_name = 'sale.order.item.delivery.schedules'
	_description = 'General Model Sales Order Item Delivery Schedules'
	_columns = {
	'item_id': fields.many2one(obj = 'sale.order.items',label = 'Order Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
	}

sale_order_item_delivery_schedules()

class sale_order_item_output_plates(Model):
	_name = 'sale.order.item.output.plates'
	_description = 'General Model Sale Order Item Output Plates'
	_columns = {
	'item_id': fields.many2one(label = 'Order',obj='sale.order.items'),
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

sale_order_item_output_plates()

class sale_order_item_payment_schedules(Model):
	_name = 'sale.order.item.payment.schedules'
	_description = 'General Model Sale Order Item Payment Schedules'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='sale.order.items'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

sale_order_item_payment_schedules()

# Invoice
class sale_invoices(Model):
	_name = 'sale.invoices'
	_description = 'General Model Sale Invoices'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'doi'
	_columns = {
	'itype': fields.many2one(label='Type',obj='sale.invoice.types',on_change='on_change_itype'),
	'company_id': fields.many2one(label='Company',obj='md.company'),
	'category_id': fields.many2one(label='Category',obj='sale.invoice.categories'),
	'name': fields.varchar(label = 'Name'),
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
	'items': fields.one2many(label='Items',obj='sale.invoice.items',rel='invoice_id'),
	'roles': fields.one2many(label='Roles',obj='sale.invoice.roles',rel='invoice_id'),
	'texts': fields.one2many(label='Texts',obj='sale.invoice.texts',rel='invoice_id'),
	'note': fields.text('Note')
	}

	def _on_change_itype(self,cr,pool,uid,item,context={}):		
			roles = pool.get('sale.invoice.type.roles').select(cr,pool.uid,['role_id'],[('type_id','=',item['otype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]


	_default = {
		'state':'draft'
	}

sale_invoices()

class sale_invoice_texts(Model):
	_name = 'sale.invoice.texts'
	_description = 'General Model Sale Invoce Texts'
	_class_model = 'C'
	_class_category = 'invoice'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'invoice_id': fields.many2one(label='Order',obj='sale.invoices'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='sale.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

sale_invoice_texts()

class sale_invoice_roles(Model):
	_name = 'sale.invoice.roles'
	_description = 'General Model sale Invoice Roles'
	_columns = {
	'invoice_id': fields.many2one(label = 'Invoice',obj='sale.invoices'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

sale_invoice_roles()

class sales_invoice_items(Model):
	_name = 'sale.invoice.items'
	_description = 'General Model Sales Invoice Items'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'invoice_id': fields.many2one(obj = 'sale.invoices',label = 'Invoice'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'	),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,3)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('s','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'delivery_schedules': fields.one2many(label='Delivery Schedule',obj='sale.invoice.item.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='sale.invoice.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='sale.invoice.item.texts',rel='item_id'),
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

sales_invoice_items()

class sale_invoice_item_texts(Model):
	_name = 'sale.invoice.item.texts'
	_description = 'General Model Sale Invoce Item Texts'
	_class_model = 'C'
	_class_category = 'invoice'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Order',obj='sale.invoice.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='sale.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

sale_invoice_item_texts()

class sale_invoice_item_roles(Model):
	_name = 'sale.invoice.item.roles'
	_description = 'General Model Sale Invoice Item Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='sale.invoice.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

sale_invoice_item_roles()

class sales_invoce_item_delivery_schedules(Model):
	_name = 'sale.invoice.item.delivery.schedules'
	_description = 'General Model Sales Order Item Delivery Schedules'
	_columns = {
	'item_id': fields.many2one(obj = 'sale.invoice.items',label = 'Order Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
	}

sales_invoce_item_delivery_schedules()

#inherit

class md_sale_product(Model):
	_name = 'md.sale.product'
	_description = 'General Model Sale Of Product'
	_columns = {
	'product_id': fields.many2one(label='Product',obj='md.product'),
	'vat': fields.many2one(label='VAT Code',obj='md.vat.code',domain=[('type_vat','in',('s','n'))]),
	'uom': fields.many2one(label="Unit Of Measure",obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'note': fields.text(label = 'Note'),
	}

md_sale_product()

class md_sale_product_inherit(ModelInherit):
	_name = 'md.sale.product.inherit'
	_description = 'Genaral Model Inherit For Sale Product'
	_inherit = {'md.product':{'_columns':['sale']},'md.recepture':{'_columns':['usage']},'md.type.items':{'_columns':['usage']}}
	_columns = {
		'sale': fields.one2many(label='Sales',obj='md.sale.product',rel='product_id'),
		'usage': fields.iSelection(selections=[('s','Sale')])
	}
	
md_sale_product_inherit()

