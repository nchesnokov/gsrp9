from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

from decimal import Decimal

from datetime import datetime
from datetime import timedelta

#customize
# Organization structure
class purchase_unit_categories(Model):
	_name = 'purchase.unit.categories'
	_description = 'Categories Purchase Unit'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='purchase.unit.categories'),
	'childs_id': fields.one2many(obj = 'purchase.unit.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'units': fields.one2many(label='Units',obj='purchase.units',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

purchase_unit_categories()


class purchase_units(Model):
	_name = 'purchase.units'
	_description = 'Purchase Units'
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
	_description = 'Categories Purchase Chanel'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='purchase.channel.categories'),
	'childs_id': fields.one2many(obj = 'purchase.channel.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'channels': fields.one2many(label='Channels',obj='purchase.channels',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

purchase_channel_categories()


class purchase_channels(Model):
	_name = 'purchase.channels'
	_description = 'Purchase Channels'
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
	_description = 'Categories Purchase Segment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='purchase.segment.categories'),
	'childs_id': fields.one2many(obj = 'purchase.segment.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'segments': fields.one2many(label='Segments',obj='purchase.segments',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

purchase_segment_categories()


class purchase_segments(Model):
	_name = 'purchase.segments'
	_description = 'Purchase Segments'
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
	_description = 'Categories Purchase Area'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='purchase.area.categories'),
	'childs_id': fields.one2many(obj = 'purchase.area.categories',rel = 'parent_id',label = 'Childs'),
	'areas': fields.one2many(label='Areas',obj='purchase.areas',rel='category_id',limit = 80,readonly=True),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'note': fields.text(label = 'Note')
	}

purchase_area_categories()


class purchase_areas(Model):
	_name = 'purchase.areas'
	_description = 'Purchase Areas'
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
	_description = 'Categories Purchase Region'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='purchase.region.categories'),
	'childs_id': fields.one2many(obj = 'purchase.region.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'segments': fields.one2many(label='REgions',obj='purchase.regions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

purchase_region_categories()


class purchase_regions(Model):
	_name = 'purchase.regions'
	_description = 'Purchase Regions'
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
	_description = 'Categories Purchase Division'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='purchase.division.categories'),
	'childs_id': fields.one2many(obj = 'purchase.division.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'divisions': fields.one2many(label='Divisions',obj='purchase.divisions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

purchase_division_categories()


class purchase_divisions(Model):
	_name = 'purchase.divisions'
	_description = 'Purchase Divisions'
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
	_description = 'Categories Purchase Subdivision'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='purchase.subdivision.categories'),
	'childs_id': fields.one2many(obj = 'purchase.subdivision.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'subdivisions': fields.one2many(label='Orders',obj='purchase.subdivisions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

purchase_subdivision_categories()


class purchase_subdivisions(Model):
	_name = 'purchase.subdivisions'
	_description = 'Purchase Subdivisions'
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
	_description = 'Purchase Unit Of Channel Assigment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='purchase.units'),
	'channel_id': fields.many2one(label='Channel',obj='purchase.channels',selectable=True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname')
	}

	def _compute_fullname(self ,item,context):
		v=''

		if 'channel_id' in item and 'name' in item['channel_id'] and item['channel_id']['name']:
			v += item['channel_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

purchase_unit_channel_assigments()

class purchase_unit_segment_assigments(Model):
	_name = 'purchase.unit.segment.assigments'
	_description = 'Purchase Unit Of Segment Assigment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='purchase.units'),
	'segment_id': fields.many2one(label='Segment',obj='purchase.segments',selectable=True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname')
	}

	def _compute_fullname(self ,item,context):
		v=''

		if 'segment_id' in item and 'name' in item['segment_id'] and item['segment_id']['name']:
			v += item['segment_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

purchase_unit_segment_assigments()

class purchase_unit_area_assigments(Model):
	_name = 'purchase.unit.area.assigments'
	_description = 'Purchase Unit Of Area Assigment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='purchase.units'),
	'area_id': fields.many2one(label='Area',obj='purchase.areas',selectable=True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname')
	}

	def _compute_fullname(self ,item,context):
		v=''

		if 'area_id' in item and 'name' in item['area_id'] and item['area_id']['name']:
			v += item['area_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

purchase_unit_area_assigments()

class purchase_unit_region_assigments(Model):
	_name = 'purchase.unit.region.assigments'
	_description = 'Purchase Unit Of Region Assigment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='purchase.units'),
	'region_id': fields.many2one(label='Region',obj='purchase.regions',selectable=True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname')
	}

	def _compute_fullname(self ,item,context):
		v=''

		if 'region_id' in item and 'name' in item['region_id'] and item['region_id']['name']:
			v += item['region_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

purchase_unit_segment_assigments()



class purchase_division_subdivision_assigments(Model):
	_name = 'purchase.division.subdivision.assigments'
	_description = 'Purchase Division Of Subdivision Assigment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'division_id': fields.many2one(label='Division',obj='purchase.divisions'),
	'subdivision_id': fields.many2one(label='Subdivision',obj='purchase.subdivisions',selectable=True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname'),
	}

	def _compute_fullname(self ,item,context):
		v=''

		if 'subdivision_id' in item and 'name' in item['subdivision_id'] and item['subdivision_id']['name']:
			v += item['subdivision_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

purchase_division_subdivision_assigments()


class purchase_markets(Model):
	_name = 'purchase.markets'
	_description = 'Purchase Market'
	_class_model = 'C'
	_class_category = 'order'
	_rec_name = 'fullname'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='purchase.units', required = True),
	'channel_id': fields.related(label='Channel',obj='purchase.unit.channel.assigments', relatedy=['unit_id'], required = True),
	'segment_id': fields.related(label='Segment',obj='purchase.unit.segment.assigments', relatedy=['unit_id'], required = True),
	'area_id': fields.related(label='Area',obj='purchase.unit.area.assigments', relatedy=['unit_id'], required = True),
	'region_id': fields.related(label='Region',obj='purchase.unit.region.assigments', relatedy=['unit_id'], required = True),
	'fullname': fields.composite(label='Full Name',cols=['unit_id','channel_id','segment_id','area_id','region_id'],translate = True,required = True, compute = '_compute_composite'),
	'note': fields.text(label='Note'),
	}

purchase_markets()


class purchase_teams(Model):
	_name = 'purchase.teams'
	_description = 'Purchase Teams'
	_class_model = 'C'
	_class_category = 'order'
	_rec_name = 'fullname'
	_columns = {
	'division_id': fields.many2one(label='Division',obj='purchase.divisions', required = True),
	'subdivision_id': fields.related(label='Subdivision',obj='purchase.division.subdivision.assigments', relatedy=['division_id'], required = True),
	'fullname': fields.composite(label='Full Name',cols=['division_id','subdivision_id'],translate = True,required = True, compute = '_compute_composite'),
	'note': fields.text(label='Note'),
	}

purchase_teams()


#Organization structure
#Pricing
class purchase_pricing_group_levels(Model):
	_name = 'purchase.pricing.group.levels'
	_description = 'Purchase Pricing Group Levels'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

purchase_pricing_group_levels()

#Text
class purchase_texts(Model):
	_name = 'purchase.texts'
	_description = 'Purchase Texts'
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
	_description = 'Schema Of Purchase Texts'
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
	_description = 'Items Of Schema Purchase Texts'
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
	_description = 'Types Purchase Order'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'otype': fields.selection(label='Type',selections=[('ord','Order'),('ap','Advance Payment'),('ps','Pseduo'),('dm','Debit Request'),('cr','Credit Request'),('rо','Return')]),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='purchase.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='purchase.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='purchase.order.type.roles',rel='type_id'),
	'plates': fields.one2many(label='Plates',obj='purchase.order.type.plates',rel='type_id'),
	'tis': fields.one2many(label='TIs',obj='purchase.order.type.items',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

purchase_order_types()

class purchase_order_type_roles(Model):
	_name = 'purchase.order.type.roles'
	_description = 'Role Purchase Order Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='purchase.order.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

purchase_order_type_roles()


class purchase_order_type_plates(Model):
	_name = 'purchase.order.type.plates'
	_description = 'Purchase Order Plates'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='purchase.order.types'),
	'seq': fields.integer(label='Sequence',required=True),
	'plate': fields.many2one(label = 'Plate',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

purchase_order_type_plates()


class purchase_order_type_items(Model):
	_name = 'purchase.order.type.items'
	_description = 'Plates Of Purchase Order Items'
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
	_description = 'Types Purchase Invoice'
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
	_description = 'Role Purchase Invoice Types'
	_class_model = 'C'
	_class_category = 'invoice'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='purchase.invoice.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

purchase_invoice_type_roles()


class purchase_order_categories(Model):
	_name = 'purchase.order.categories'
	_description = 'Categories Purchase Order'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='purchase.order.categories'),
	'childs_id': fields.one2many(obj = 'purchase.order.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'orders': fields.one2many(label='Orders',obj='purchase.orders',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

purchase_order_categories()

class purchase_invoce_categories(Model):
	_name = 'purchase.invoce.categories'
	_description = 'Categories Purchase Invoce'
	_class_model = 'C'
	_class_category = 'invoice'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='purchase.invoce.categories'),
	'childs_id': fields.one2many(obj = 'purchase.invoce.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'invoices': fields.one2many(label='Orders',obj='purchase.invoices',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

purchase_invoce_categories()


# end customize
