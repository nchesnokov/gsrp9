from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

from decimal import Decimal

from datetime import datetime
from datetime import timedelta

#customize
# Organization structure
class crm_unit_categories(Model):
	_name = 'crm.unit.categories'
	_description = 'Categories CRM Unit'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.i18n(fields.varchar(label = 'Name',size=64)),
	'parent_id': fields.many2one(label='Parent',obj='crm.unit.categories',rel='childs_id'),
	'childs_id': fields.one2many(obj = 'crm.unit.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.i18n(fields.tree(label='Full Name', required = True)),
	'units': fields.one2many(label='Units',obj='crm.units',rel='category_id'),
	'note': fields.i18n(fields.text(label = 'Note'))
	}

#crm_unit_categories()


class crm_units(Model):
	_name = 'crm.units'
	_description = 'CRM Units'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'crm-org'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='crm.unit.categories',rel='units'),
	'company_ids': fields.many2many(label='Companies',obj='md.company', rel='md_company_crm_unit_rel', id2='unit_id', id1='company_id'),
	'code': fields.i18n(fields.varchar(label = 'Code',size=8)),
	'descr':fields.i18n(fields.varchar(label = 'Description',size=128)),
	'channels': fields.one2many(label='Channels',obj='crm.unit.channel.assigments',rel='unit_id'),
	'segments': fields.one2many(label='Segments',obj='crm.unit.segment.assigments',rel='unit_id'),
	'areas': fields.one2many(label='Areas',obj='crm.unit.area.assigments',rel='unit_id'),
	'regions': fields.one2many(label='Regions',obj='crm.unit.region.assigments',rel='unit_id')
	}

#crm_units()

class crm_channel_categories(Model):
	_name = 'crm.channel.categories'
	_description = 'Categories CRM Chanel'
	_class_model = 'C'
	_class_category = 'crm-org'
	_columns = {
	'name': fields.i18n(fields.varchar(label = 'Name',size=64)),
	'parent_id': fields.many2one(label='Parent',obj='crm.channel.categories'),
	'childs_id': fields.one2many(obj = 'crm.channel.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.i18n(fields.tree(label='Full Name', required = True)),
	'channels': fields.one2many(label='Channels',obj='crm.channels',rel='category_id'),
	'note': fields.i18n(fields.text(label = 'Note'))
	}

#crm_channel_categories()


class crm_channels(Model):
	_name = 'crm.channels'
	_description = 'CRM Channels'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'crm-org'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='crm.channel.categories',rel='channels'),
	'code': fields.i18n(fields.varchar(label = 'Code',size=8)),
	'descr':fields.i18n(fields.varchar(label = 'Description',size=128)),
	}

#crm_channels()

class crm_segment_categories(Model):
	_name = 'crm.segment.categories'
	_description = 'Categories CRM Segment'
	_class_model = 'C'
	_class_category = 'crm-org'
	_columns = {
	'name': fields.i18n(fields.varchar(label = 'Name',size=64)),
	'parent_id': fields.many2one(label='Parent',obj='crm.segment.categories',rel='childs_id'),
	'childs_id': fields.one2many(obj = 'crm.segment.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.i18n(fields.tree(label='Full Name',required = True)),
	'segments': fields.one2many(label='Segments',obj='crm.segments',rel='category_id'),
	'note': fields.i18n(fields.text(label = 'Note'))
	}

#crm_segment_categories()


class crm_segments(Model):
	_name = 'crm.segments'
	_description = 'CRM Segments'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'crm-org'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='crm.segment.categories',rel='segments'),
	'code': fields.i18n(fields.varchar(label = 'Code',size=8)),
	'descr':fields.i18n(fields.varchar(label = 'Description',size=128)),
	}

#crm_segments()

class crm_area_categories(Model):
	_name = 'crm.area.categories'
	_description = 'Categories CRM Area'
	_class_model = 'C'
	_class_category = 'crm-org'
	_columns = {
	'name': fields.i18n(fields.varchar(label = 'Name',size=64)),
	'parent_id': fields.many2one(label='Parent',obj='crm.area.categories',rel='childs_id'),
	'childs_id': fields.one2many(obj = 'crm.area.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.i18n(fields.tree(label='Full Name',required = True)),
	'areas': fields.one2many(label='Areas',obj='crm.areas',rel='category_id'),
	'note': fields.i18n(fields.text(label = 'Note'))
	}

#crm_area_categories()


class crm_areas(Model):
	_name = 'crm.areas'
	_description = 'CRM Areas'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'crm-org'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='crm.area.categories',rel='areas'),
	'code': fields.i18n(fields.varchar(label = 'Code',size=8)),
	'descr':fields.i18n(fields.varchar(label = 'Description',size=128))
	}

#crm_areas()

class crm_region_categories(Model):
	_name = 'crm.region.categories'
	_description = 'Categories CRM Region'
	_class_model = 'C'
	_class_category = 'crm-org'
	_columns = {
	'name': fields.i18n(fields.varchar(label = 'Name',size=64)),
	'parent_id': fields.many2one(label='Parent',obj='crm.region.categories',rel='childs_id'),
	'childs_id': fields.one2many(obj = 'crm.region.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.i18n(fields.tree(label='Full Name',required = True)),
	'segments': fields.one2many(label='REgions',obj='crm.regions',rel='category_id'),
	'note': fields.i18n(fields.text(label = 'Note'))
	}

#crm_region_categories()


class crm_regions(Model):
	_name = 'crm.regions'
	_description = 'CRM Regions'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'crm-org'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='crm.region.categories',rel='regions'),
	'code': fields.i18n(fields.varchar(label = 'Code',size=8)),
	'descr':fields.i18n(fields.varchar(label = 'Description',size=128)),
	}

#crm_regions()


class crm_division_categories(Model):
	_name = 'crm.division.categories'
	_description = 'Categories CRM Division'
	_class_model = 'C'
	_class_category = 'crm-org'
	_columns = {
	'name': fields.i18n(fields.varchar(label = 'Name',size=64)),
	'parent_id': fields.many2one(label='Parent',obj='crm.division.categories',rel='childs_id'),
	'childs_id': fields.one2many(obj = 'crm.division.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.i18n(fields.tree(label='Full Name', required = True)),
	'divisions': fields.one2many(label='Divisions',obj='crm.divisions',rel='category_id'),
	'note': fields.i18n(fields.text(label = 'Note'))
	}

#crm_division_categories()


class crm_divisions(Model):
	_name = 'crm.divisions'
	_description = 'CRM Divisions'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'crm-org'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='crm.division.categories',rel='divisions'),
	'code': fields.i18n(fields.varchar(label = 'Code',size=8)),
	'descr':fields.i18n(fields.varchar(label = 'Description',size=128)),
	'subdivisions': fields.one2many(label='SubDivisions',obj='crm.division.subdivision.assigments',rel='division_id')
	}

#crm_divisions()

class crm_subdivision_categories(Model):
	_name = 'crm.subdivision.categories'
	_description = 'Categories CRM Subdivision'
	_class_model = 'C'
	_class_category = 'crm-org'
	_columns = {
	'name': fields.i18n(fields.varchar(label = 'Name',size=64)),
	'parent_id': fields.many2one(label='Parent',obj='crm.subdivision.categories',rel='childs_id'),
	'childs_id': fields.one2many(obj = 'crm.subdivision.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.i18n(fields.tree(label='Full Name',required = True)),
	'subdivisions': fields.one2many(label='Orders',obj='crm.subdivisions',rel='category_id'),
	'note': fields.i18n(fields.text(label = 'Note'))
	}

#crm_subdivision_categories()


class crm_subdivisions(Model):
	_name = 'crm.subdivisions'
	_description = 'CRM Subdivisions'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'crm-org'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='crm.subdivision.categories',rel='subdivisions'),
	'code': fields.i18n(fields.varchar(label = 'Code',size=8)),
	'descr':fields.i18n(fields.varchar(label = 'Description',size=128))
	}

#crm_subdivisions()

class crm_unit_channel_assigments(Model):
	_name = 'crm.unit.channel.assigments'
	_description = 'CRM Unit Of Channel Assigment'
	_rec_name = 'fullname'
	_class_model = 'C'
	_class_category = 'crm-org-assign'
	_columns = {
	'unit_id': fields.referenced(label='Unit',obj='crm.units',selectable=True),
	'channel_id': fields.referenced(label='Channel',obj='crm.channels',selectable=True),
	'fullname': fields.i18n(fields.composite(label='Full Name',cols=['unit_id','channel_id'],required = True))
	}

#crm_unit_channel_assigments()

class crm_unit_segment_assigments(Model):
	_name = 'crm.unit.segment.assigments'
	_description = 'CRM Unit Of Segment Assigment'
	_rec_name = 'fullname'
	_class_model = 'C'
	_class_category = 'crm-org-assign'
	_columns = {
	'unit_id': fields.referenced(label='Unit',obj='crm.units',selectable=True),
	'segment_id': fields.referenced(label='Segment',obj='crm.segments',selectable=True),
	'fullname': fields.i18n(fields.composite(label='Full Name',required = True, cols=['unit_id','segment_id']))
	}

#crm_unit_segment_assigments()

class crm_unit_area_assigments(Model):
	_name = 'crm.unit.area.assigments'
	_description = 'CRM Unit Of Area Assigment'
	_rec_name = 'fullname'
	_class_model = 'C'
	_class_category = 'crm-org-assign'
	_columns = {
	'unit_id': fields.referenced(label='Unit',obj='crm.units',selectable=True),
	'area_id': fields.referenced(label='Area',obj='crm.areas',selectable=True),
	'fullname': fields.i18n(fields.composite(label='Full Name',translate = True,required = True, cols=['unit_id','area_id']))
	}

#crm_unit_area_assigments()

class crm_unit_region_assigments(Model):
	_name = 'crm.unit.region.assigments'
	_description = 'CRM Unit Of Region Assigment'
	_rec_name = 'fullname'
	_class_model = 'C'
	_class_category = 'crm-org-assign'
	_columns = {
	'unit_id': fields.referenced(label='Unit',obj='crm.units',selectable=True),
	'region_id': fields.referenced(label='Region',obj='crm.regions',selectable=True),
	'fullname': fields.i18n(fields.composite(label='Full Name',translate = True,required = True, cols = ['unit_id','region_id']))
	}

#crm_unit_segment_assigments()

class crm_division_subdivision_assigments(Model):
	_name = 'crm.division.subdivision.assigments'
	_description = 'CRM Division Of Subdivision Assigment'
	_rec_name = 'fullname'
	_class_model = 'C'
	_class_category = 'crm-org-assign'
	_columns = {
	'division_id': fields.referenced(label='Division',obj='crm.divisions',selectable=True),
	'subdivision_id': fields.referenced(label='Subdivision',obj='crm.subdivisions',selectable=True),
	'fullname': fields.i18n(fields.composite(label='Full Name',required = True, cols = ['division_id','subdivision_id'])),
	}

#crm_division_subdivision_assigments()

class crm_markets(Model):
	_name = 'crm.markets'
	_description = 'CRM Market'
	_class_model = 'C'
	_class_category = 'crm-org-full'
	_rec_name = 'fullname'
	_columns = {
	'unit_id': fields.referenced(label='Unit',obj='crm.units', required = True),
	'channel_id': fields.related(label='Channel',obj='crm.unit.channel.assigments', relatedy=['unit_id'], required = True),
	'segment_id': fields.related(label='Segment',obj='crm.unit.segment.assigments', relatedy=['unit_id'], required = True),
	'area_id': fields.related(label='Area',obj='crm.unit.area.assigments', relatedy=['unit_id'], required = True),
	'region_id': fields.related(label='Region',obj='crm.unit.region.assigments', relatedy=['unit_id'], required = True),
	'fullname': fields.i18n(fields.composite(label='Full Name',cols=['unit_id','channel_id','segment_id','area_id','region_id'],required = True)),
	'note': fields.i18n(fields.text(label='Note')),
	}

#crm_markets()

class crm_teams(Model):
	_name = 'crm.teams'
	_description = 'CRM Teams'
	_class_model = 'C'
	_class_category = 'crm-org=full'
	_rec_name = 'fullname'
	_columns = {
	'division_id': fields.referenced(label='Division',obj='crm.divisions', required = True),
	'subdivision_id': fields.related(label='Subdivision',obj='crm.division.subdivision.assigments', relatedy=['division_id'], required = True),
	'fullname': fields.i18n(fields.composite(label='Full Name',cols=['division_id','subdivision_id'],required = True)),
	'note': fields.i18n(fields.text(label='Note'))
	}

#crm_teams()

#Organization structure
#Pricing
class crm_pricing_group_levels(Model):
	_name = 'crm.pricing.group.levels'
	_description = 'CRM Pricing Group Levels'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'crm-pricing'
	_columns = {
	'code': fields.i18n(fields.varchar(label = 'Code',size=8)),
	'descr':fields.i18n(fields.varchar(label = 'Description',size=128))
	}

#crm_pricing_group_levels()

#Text
class crm_texts(Model):
	_name = 'crm.texts'
	_description = 'CRM Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'crm-text'
	_columns = {
	'code': fields.i18n(fields.varchar(label = 'Code',size=8)),
	'descr':fields.i18n(fields.varchar(label = 'Description',size=128))
	}

#crm_texts()

class crm_schema_texts(Model):
	_name = 'crm.schema.texts'
	_description = 'Schema Of CRM Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'crm-text'
	_columns = {
	'usage': fields.i18n(fields.selection(label='Usage',selections=[('h','Header'),('i','Item'),('b','Both')])),
	'code': fields.i18n(fields.varchar(label = 'Code',size=8)),
	'descr':fields.i18n(fields.varchar(label = 'Description',size=128)),
	'texts': fields.one2many(label='Texts',obj='crm.schema.text.items',rel='schema_id')
	}

#crm_schema_texts()

class crm_schema_text_items(Model):
	_name = 'crm.schema.text.items'
	_description = 'Items Of Schema CRM Texts'
	_class_model = 'C'
	_class_category = 'crm-text'
	_columns = {
	'schema_id': fields.many2one(label = 'Schema',obj='crm.schema.texts',rel='texts'),
	'seq': fields.integer(label='Sequence'),
	'text_id': fields.referenced(label = 'Text',obj='crm.texts'),
	'descr': fields.link(ref='text_id.descr')
	}

#crm_schema_text_items()

# Text end

class crm_request_types(Model):
	_name = 'crm.request.types'
	_description = 'Types CRM Request'
	_class_model = 'C'
	_class_category = 'crm-obj'
	_columns = {
	'otype': fields.i18n(fields.selection(label='Type',selections=[('ord','Order'),('ap','Advance Payment'),('ps','Pseduo'),('dm','Debit Request'),('cr','Credit Request'),('rо','Return')])),
	'name': fields.i18n(fields.varchar(label = 'Name',size=64)),
	'htschema': fields.referenced(label='Text Schema Of Head',obj='crm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.referenced(label='Text Schema Of Item',obj='crm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='crm.request.type.roles',rel='type_id'),
	'tis': fields.one2many(label='TIs',obj='crm.request.type.items',rel='type_id'),
	'required': fields.boolean(label='Required'),
	'note': fields.i18n(fields.text(label = 'Note'))
	}

#crm_request_types()

class crm_request_type_roles(Model):
	_name = 'crm.request.type.roles'
	_description = 'Role CRM Request Types'
	_class_model = 'C'
	_class_category = 'crm-obj'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='crm.request.types',rel='roles'),
	'role_id': fields.referenced(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','a'))]),
	'note': fields.i18n(fields.text(label = 'Note'))
	}

#crm_request_type_roles()

class crm_request_type_items(Model):
	_name = 'crm.request.type.items'
	_description = 'Role CRM Request Items'
	_class_model = 'C'
	_class_category = 'crm-obj'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='crm.request.types',rel='tis'),
	'gti_id': fields.referenced(label = 'GTI',obj='md.gtis',required=True),
	'itype_id': fields.referenced(label = 'Type Of Items',obj='md.type.items',domain=[('usage','=','s'),'|',('usage','=','a')]),
	'note': fields.i18n(fields.text(label = 'Note'))
	}

#crm_request_type_items()

class crm_offer_types(Model):
	_name = 'crm.offer.types'
	_description = 'Types CRM Offer'
	_class_model = 'C'
	_class_category = 'crm-obj'
	_columns = {
	'name': fields.i18n(fields.varchar(label = 'Name',size=64)),
	'htschema': fields.referenced(label='Text Schema Of Head',obj='crm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.referenced(label='Text Schema Of Item',obj='crm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='crm.offer.type.roles',rel='type_id'),
	'note': fields.i18n(fields.text(label = 'Note'))
	}

#crm_offer_types()

class crm_offer_type_roles(Model):
	_name = 'crm.offer.type.roles'
	_description = 'Role CRM Offer Types'
	_class_model = 'C'
	_class_category = 'crm-obj'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='crm.offer.types',rel='roles'),
	'role_id': fields.referenced(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.i18n(fields.text(label = 'Note'))
	}

#crm_offer_type_roles()

class crm_request_categories(Model):
	_name = 'crm.request.categories'
	_description = 'Category CRM Regiset'
	_class_model = 'C'
	_class_category = 'crm-obj'
	_columns = {
	'name': fields.i18n(fields.varchar(label = 'Name',size=64)),
	'parent_id': fields.many2one(label='Parent',obj='crm.request.categories',rel='childs_id'),
	'childs_id': fields.one2many(obj = 'crm.request.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.i18n(fields.tree(label='Full Name',required = True)),
	'requests': fields.one2many(label='Orders',obj='crm.requests',rel='category_id'),
	'note': fields.i18n(fields.text(label = 'Note'))
	}

#sales_request_categories()

class crm_offer_categories(Model):
	_name = 'crm.offer.categories'
	_description = 'Category CRM Offer'
	_class_model = 'C'
	_class_category = 'crm-obj'
	_columns = {
	'name': fields.i18n(fields.varchar(label = 'Name',size=64)),
	'parent_id': fields.many2one(label='Parent',obj='crm.offer.categories',rel='childs_id'),
	'childs_id': fields.one2many(obj = 'crm.offer.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.i18n(fields.tree(label='Full Name',required = True)),
	'offers': fields.one2many(label='Orders',obj='crm.offers',rel='category_id'),
	'note': fields.i18n(fields.text(label = 'Note'))
	}

#crm_offer_categories()

class crm_units_md_company_inherit(ModelInherit):
	_name = 'crm.units.md.company.inherit'
	_description = 'CRM Units Master Data Company Inherit'
	_inherit = {'md.company':{'_columns':['crm_units']}}
	_columns={
	'crm_units': fields.many2many(label='CRM Units',obj='crm.units',rel='md_company_crm_unit_rel',id1='unit_id',id2='company_id'),
	}

# end customize
