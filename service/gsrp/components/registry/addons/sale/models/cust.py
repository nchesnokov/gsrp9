from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

from decimal import Decimal

from datetime import datetime
from datetime import timedelta

#customize
# Organization structure
class sale_unit_categories(Model):
	_name = 'sale.unit.categories'
	_description = 'Categories Sale Unit'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='sale.unit.categories'),
	'childs_id': fields.one2many(obj = 'sale.unit.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'units': fields.one2many(label='Units',obj='sale.units',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

sale_unit_categories()


class sale_units(Model):
	_name = 'sale.units'
	_description = 'Sale Units'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='sale.unit.categories'),
	'company_ids': fields.many2many(label='Companies',obj='md.company', rel='md_company_sale_unit_rel', id2='unit_id', id1='company_id'),
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
	_description = 'Categories Sale Chanel'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='sale.channel.categories'),
	'childs_id': fields.one2many(obj = 'sale.channel.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'channels': fields.one2many(label='Channels',obj='sale.channels',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

sale_channel_categories()


class sale_channels(Model):
	_name = 'sale.channels'
	_description = 'Sale Channels'
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
	_description = 'Categories Sale Segment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='sale.segment.categories'),
	'childs_id': fields.one2many(obj = 'sale.segment.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'segments': fields.one2many(label='Segments',obj='sale.segments',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

sale_segment_categories()


class sale_segments(Model):
	_name = 'sale.segments'
	_description = 'Sale Segments'
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
	_description = 'Categories Sale Area'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='sale.area.categories'),
	'childs_id': fields.one2many(obj = 'sale.area.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'areas': fields.one2many(label='Areas',obj='sale.areas',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

sale_area_categories()


class sale_areas(Model):
	_name = 'sale.areas'
	_description = 'Sale Areas'
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
	_description = 'Categories Sale Region'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='sale.region.categories'),
	'childs_id': fields.one2many(obj = 'sale.region.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'segments': fields.one2many(label='REgions',obj='sale.regions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

sale_region_categories()


class sale_regions(Model):
	_name = 'sale.regions'
	_description = 'Sale Regions'
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
	_description = 'Categories Sale Division'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='sale.division.categories'),
	'childs_id': fields.one2many(obj = 'sale.division.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'divisions': fields.one2many(label='Divisions',obj='sale.divisions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

sale_division_categories()


class sale_divisions(Model):
	_name = 'sale.divisions'
	_description = 'Sale Divisions'
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
	_description = 'Categories Sale Subdivision'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='sale.subdivision.categories'),
	'childs_id': fields.one2many(obj = 'sale.subdivision.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'subdivisions': fields.one2many(label='Orders',obj='sale.subdivisions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

sale_subdivision_categories()


class sale_subdivisions(Model):
	_name = 'sale.subdivisions'
	_description = 'Sale Subdivisions'
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
	_description = 'Sale Unit Of Channel Assigment'
	_rec_name = 'fullname'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='sale.units'),
	'channel_id': fields.many2one(label='Channel',obj='sale.channels',selectable=True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname')
	}

	def _compute_fullname(self ,item,context):
		v=''

		if 'channel_id' in item and 'name' in item['channel_id'] and item['channel_id']['name']:
			v += item['channel_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

sale_unit_channel_assigments()

class sale_unit_segment_assigments(Model):
	_name = 'sale.unit.segment.assigments'
	_description = 'Sale Unit Of Segment Assigment'
	_rec_name = 'fullname'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='sale.units'),
	'segment_id': fields.many2one(label='Segment',obj='sale.segments',selectable=True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname')
	}

	def _compute_fullname(self ,item,context):
		v=''

		if 'segment_id' in item and 'name' in item['segment_id'] and item['segment_id']['name']:
			v += item['segment_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

sale_unit_segment_assigments()

class sale_unit_area_assigments(Model):
	_name = 'sale.unit.area.assigments'
	_description = 'Sale Unit Of Area Assigment'
	_rec_name = 'fullname'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='sale.units'),
	'area_id': fields.many2one(label='Area',obj='sale.areas',selectable=True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname')
	}

	def _compute_fullname(self ,item,context):
		v=''

		if 'area_id' in item and 'name' in item['area_id'] and item['area_id']['name']:
			v += item['area_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

sale_unit_area_assigments()

class sale_unit_region_assigments(Model):
	_name = 'sale.unit.region.assigments'
	_description = 'Sale Unit Of Region Assigment'
	_rec_name = 'fullname'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='sale.units'),
	'region_id': fields.many2one(label='Region',obj='sale.regions',selectable=True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname')
	}

	def _compute_fullname(self ,item,context):
		v=''

		if 'region_id' in item and 'name' in item['region_id'] and item['region_id']['name']:
			v += item['region_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

sale_unit_segment_assigments()

class sale_division_subdivision_assigments(Model):
	_name = 'sale.division.subdivision.assigments'
	_description = 'Sale Division Of Subdivision Assigment'
	_rec_name = 'fullname'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'division_id': fields.many2one(label='Division',obj='sale.divisions'),
	'subdivision_id': fields.many2one(label='Subdivision',obj='sale.subdivisions',selectable=True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname'),
	}

	def _compute_fullname(self ,item,context):
		v=''

		if 'subdivision_id' in item and 'name' in item['subdivision_id'] and item['subdivision_id']['name']:
			v += item['subdivision_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

sale_division_subdivision_assigments()

class sale_markets(Model):
	_name = 'sale.markets'
	_description = 'Sale Market'
	_class_model = 'C'
	_class_category = 'order'
	_rec_name = 'fullname'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='sale.units', required = True),
	'channel_id': fields.related(label='Channel',obj='sale.unit.channel.assigments', relatedy=['unit_id'], required = True),
	'segment_id': fields.related(label='Segment',obj='sale.unit.segment.assigments', relatedy=['unit_id'], required = True),
	'area_id': fields.related(label='Area',obj='sale.unit.area.assigments', relatedy=['unit_id'], required = True),
	'region_id': fields.related(label='Region',obj='sale.unit.region.assigments', relatedy=['unit_id'], required = True),
	'fullname': fields.composite(label='Full Name',cols=['unit_id','channel_id','segment_id','area_id','region_id'],translate = True,required = True),
	'note': fields.text(label='Note'),
	}

sale_markets()

class sale_teams(Model):
	_name = 'sale.teams'
	_description = 'Sale Teams'
	_class_model = 'C'
	_class_category = 'order'
	_rec_name = 'fullname'
	_columns = {
	'division_id': fields.many2one(label='Division',obj='sale.divisions', required = True),
	'subdivision_id': fields.related(label='Subdivision',obj='sale.division.subdivision.assigments', relatedy=['division_id'], required = True),
	'fullname': fields.composite(label='Full Name',cols=['division_id','subdivision_id'],translate = True,required = True),
	'note': fields.text(label='Note'),
	}

sale_teams()

#Organization structure
#Pricing
class sale_pricing_group_levels(Model):
	_name = 'sale.pricing.group.levels'
	_description = 'Sale Pricing Group Levels'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

sale_pricing_group_levels()

#Text
class sale_texts(Model):
	_name = 'sale.texts'
	_description = 'Sale Texts'
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
	_description = 'Schema Of Sale Texts'
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
	_description = 'Items Of Schema Sale Texts'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'schema_id': fields.many2one(label = 'Schema',obj='sale.schema.texts'),
	'seq': fields.integer(label='Sequence'),
	'text_id': fields.many2one(label = 'Text',obj='sale.texts'),
	'descr': fields.link(ref='text_id.descr')
	}

sale_schema_text_items()

# Text end

class sale_order_types(Model):
	_name = 'sale.order.types'
	_description = 'Types Sale Order'
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
	_description = 'Role Sale Order Types'
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
	_description = 'Role Sale Order Items'
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
	_description = 'Types Sale Invoice'
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
	_description = 'Role sale Invoice Types'
	_class_model = 'C'
	_class_category = 'invoice'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='sale.invoice.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

sale_invoice_type_roles()

class sales_order_categories(Model):
	_name = 'sale.order.categories'
	_description = 'Category Sale Order'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='sale.order.categories'),
	'childs_id': fields.one2many(obj = 'sale.order.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'orders': fields.one2many(label='Orders',obj='sale.orders',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

sales_order_categories()

class sale_invoice_categories(Model):
	_name = 'sale.invoice.categories'
	_description = 'Category Sale Invoice'
	_class_model = 'C'
	_class_category = 'invoice'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='sale.invoice.categories'),
	'childs_id': fields.one2many(obj = 'sale.invoice.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'invoices': fields.one2many(label='Orders',obj='sale.invoices',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

sale_invoice_categories()

class sale_units_md_company_inherit(ModelInherit):
	_name = 'sale.units.md.company.inherit'
	_description = 'Sale Units Master Data Company Inherit'
	_inherit = {'md.company':{'_columns':['sale_units']}}
	_columns={
	'sale_units': fields.many2many(label='Sale Units',obj='sale.units',rel='md_company_sale_unit_rel',id1='unit_id',id2='company_id'),
	}

# end customize
