from gsrp5service.orm import fields
from gsrp5service.orm.model import Model,ModelInherit

from decimal import Decimal

from datetime import datetime
from datetime import timedelta

# Customize
# Organization structure
class crm_unit_categories(Model):
	_name = 'crm_unit.categories'
	_description = 'General Model Categories CRM Unit'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='crm_unit.categories'),
	'childs_id': fields.one2many(obj = 'crm_unit.categories',rel = 'parent_id',label = 'Childs'),
	'units': fields.one2many(label='Units',obj='crm_units',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

crm_unit_categories()


class crm_units(Model):
	_name = 'crm_units'
	_description = 'General Model CRM Units'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='crm_unit.categories'),
	'company_id': fields.many2many(label='Companies',obj='md.company', rel='md_company_crm_unit_rel', id2='unit_id', id1='company_id'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'channels': fields.one2many(label='Channels',obj='crm_unit.channel.assigments',rel='unit_id'),
	'segments': fields.one2many(label='Segments',obj='crm_unit.segment.assigments',rel='unit_id'),
	'areas': fields.one2many(label='Areas',obj='crm_unit.area.assigments',rel='unit_id'),
	'regions': fields.one2many(label='Regions',obj='crm_unit.region.assigments',rel='unit_id')
	}

crm_units()

class crm_channel_categories(Model):
	_name = 'crm_channel.categories'
	_description = 'General Model Categories CRM Chanel'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='crm_channel.categories'),
	'childs_id': fields.one2many(obj = 'crm_channel.categories',rel = 'parent_id',label = 'Childs'),
	'channels': fields.one2many(label='Channels',obj='crm_channels',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

crm_channel_categories()


class crm_channels(Model):
	_name = 'crm_channels'
	_description = 'General Model CRM Channels'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='crm_channel.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

crm_channels()

class crm_segment_categories(Model):
	_name = 'crm_segment.categories'
	_description = 'General Model Categories CRM Segment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='crm_segment.categories'),
	'childs_id': fields.one2many(obj = 'crm_segment.categories',rel = 'parent_id',label = 'Childs'),
	'segments': fields.one2many(label='Segments',obj='crm_segments',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

crm_segment_categories()


class crm_segments(Model):
	_name = 'crm_segments'
	_description = 'General Model CRM Segments'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='crm_segment.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

crm_segments()

class crm_area_categories(Model):
	_name = 'crm_area.categories'
	_description = 'General Model Categories CRM Area'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='crm_area.categories'),
	'childs_id': fields.one2many(obj = 'crm_area.categories',rel = 'parent_id',label = 'Childs'),
	'areas': fields.one2many(label='Areas',obj='crm_areas',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

crm_area_categories()


class crm_areas(Model):
	_name = 'crm_areas'
	_description = 'General Model CRM Areas'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='crm_area.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

crm_areas()

class crm_region_categories(Model):
	_name = 'crm_region.categories'
	_description = 'General Model Categories CRM Region'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='crm_region.categories'),
	'childs_id': fields.one2many(obj = 'crm_region.categories',rel = 'parent_id',label = 'Childs'),
	'segments': fields.one2many(label='REgions',obj='crm_regions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

crm_region_categories()


class crm_regions(Model):
	_name = 'crm_regions'
	_description = 'General Model CRM Regions'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='crm_region.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

crm_regions()


class crm_division_categories(Model):
	_name = 'crm_division.categories'
	_description = 'General Model Categories CRM Division'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='crm_division.categories'),
	'childs_id': fields.one2many(obj = 'crm_division.categories',rel = 'parent_id',label = 'Childs'),
	'divisions': fields.one2many(label='Divisions',obj='crm_divisions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

crm_division_categories()


class crm_divisions(Model):
	_name = 'crm_divisions'
	_description = 'General Model CRM Divisions'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='crm_division.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'subdivisions': fields.one2many(label='SubDivisions',obj='crm_division.subdivision.assigments',rel='division_id')
	}

crm_divisions()

class crm_subdivision_categories(Model):
	_name = 'crm_subdivision.categories'
	_description = 'General Model Categories CRM Subdivision'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='crm_subdivision.categories'),
	'childs_id': fields.one2many(obj = 'crm_subdivision.categories',rel = 'parent_id',label = 'Childs'),
	'subdivisions': fields.one2many(label='Orders',obj='crm_subdivisions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

crm_subdivision_categories()


class crm_subdivisions(Model):
	_name = 'crm_subdivisions'
	_description = 'General Model CRM Subdivisions'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='crm_subdivision.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

crm_subdivisions()

class crm_unit_channel_assigments(Model):
	_name = 'crm_unit.channel.assigments'
	_description = 'General Model CRM Unit Of Channel Assigment'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='crm_units'),
	'channel_id': fields.many2one(label='Channel',obj='crm_channels'),
	'descr': fields.referenced(ref='channel_id.descr'),
	}

crm_unit_channel_assigments()

class crm_unit_segment_assigments(Model):
	_name = 'crm_unit.segment.assigments'
	_description = 'General Model CRM Unit Of Segment Assigment'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='crm_units'),
	'segment_id': fields.many2one(label='Segment',obj='crm_segments'),
	'descr': fields.referenced(ref='segment_id.descr'),
	}

crm_unit_segment_assigments()

class crm_unit_area_assigments(Model):
	_name = 'crm_unit.area.assigments'
	_description = 'General Model CRM Unit Of Area Assigment'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='crm_units'),
	'area_id': fields.many2one(label='Area',obj='crm_areas'),
	'descr': fields.referenced(ref='area_id.descr'),
	}

crm_unit_area_assigments()

class crm_unit_region_assigments(Model):
	_name = 'crm_unit.region.assigments'
	_description = 'General Model CRM Unit Of Region Assigment'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='crm_units'),
	'region_id': fields.many2one(label='Region',obj='crm_regions'),
	'descr': fields.referenced(ref='region_id.descr'),
	}

crm_unit_segment_assigments()



class crm_division_subdivision_assigments(Model):
	_name = 'crm_division.subdivision.assigments'
	_description = 'General Model CRM Division Of Subdivision Assigment'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'division_id': fields.many2one(label='Division',obj='crm_divisions'),
	'subdivision_id': fields.many2one(label='Subdivision',obj='crm_subdivisions'),
	'descr': fields.referenced(ref='subdivision_id.descr'),
	}

crm_division_subdivision_assigments()


class crm_markets(Model):
	_name = 'crm_markets'
	_description = 'General Model CRM Market'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_rec_name = 'fullname'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='crm_units', required = True),
	'channel_id': fields.related(label='Channel',obj='crm_unit.channel.assigments', relatedy=['unit_id'], required = True),
	'segment_id': fields.related(label='Segment',obj='crm_unit.segment.assigments', relatedy=['unit_id'], required = True),
	'area_id': fields.related(label='Area',obj='crm_unit.area.assigments', relatedy=['unit_id'], required = True),
	'region_id': fields.related(label='Region',obj='crm_unit.region.assigments', relatedy=['unit_id'], required = True),
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


crm_markets()


class crm_teams(Model):
	_name = 'crm_teams'
	_description = 'General Model CRM Teams'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_rec_name = 'fullname'
	_columns = {
	'division_id': fields.many2one(label='Division',obj='crm_divisions', required = True),
	'subdivision_id': fields.related(label='Subdivision',obj='crm_subdivisions', relatedy=['division_id'], required = True),
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

crm_teams()


#Organization structure

# Organization
class crm_channels(Model):
	_name = 'crm.channels'
	_description = 'General Model CRM Cannels'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'sectors': fields.one2many(label='Sectors',obj='crm.sectors',rel='channel_id')
	}

crm_channels()

class crm_sectors(Model):
	_name = 'crm.sectors'
	_description = 'General Model CRM Sectors'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'channel_id': fields.many2one(label='Channel',obj='crm.channels'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

crm_sectors()

class crm_teams(Model):
	_name = 'crm.teams'
	_description = 'General Model CRM Teams'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'groups': fields.one2many(label='Groups',obj='crm.groups',rel='team_id')
	}

crm_teams()

class crm_groups(Model):
	_name = 'crm.groups'
	_description = 'General Model CRM Groups'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'team_id': fields.many2one(label='Group',obj='crm.teams'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

crm_groups()

# Organization end
# Text
class crm_texts(Model):
	_name = 'crm.texts'
	_description = 'General Model CRM Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

crm_texts()

class crm_schema_texts(Model):
	_name = 'crm.schema.texts'
	_description = 'General Model Schema Of CRM Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'usage': fields.selection(label='Usage',selections=[('h','Header'),('i','Item'),('b','Both')]),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'texts': fields.one2many(label='Texts',obj='crm.schema.text.items',rel='schema_id')
	}
	
	_default = {
		'usage':'b'
	}

crm_schema_texts()

class crm_schema_text_items(Model):
	_name = 'crm.schema.text.items'
	_description = 'General Model Items Of Schema CRM Texts'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'schema_id': fields.many2one(label = 'Schema',obj='crm.schema.texts'),
	'text_id': fields.many2one(label = 'Text',obj='crm.texts'),
	'descr': fields.referenced(ref='text_id.descr')
	}

crm_schema_text_items()

# Text end

class crm_request_types(Model):
	_name = 'crm.request.types'
	_description = 'General Model Types CRM Request'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'rtype': fields.selection(label='Type',selections=[('ord','Order'),('ap','Advance Payment'),('ps','Pseduo'),('dm','Debit Request'),('cr','Credit Request'),('rо','Return')]),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='crm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='crm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='crm.request.type.roles',rel='type_id'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

crm_request_types()

class crm_request_type_roles(Model):
	_name = 'crm.request.type.roles'
	_description = 'General Model Role CRM Request Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='crm.request.types', on_delete='c'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','a'))]),
	'note': fields.text(label = 'Note')
	}

crm_request_type_roles()

class crm_offer_types(Model):
	_name = 'crm.offer.types'
	_description = 'General Model Types CRM Offer'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'otype': fields.selection(label='Type',selections=[('ord','Order'),('ap','Advance Payment'),('ps','Pseduo'),('dm','Debit Request'),('cr','Credit Request'),('rо','Return')]),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='crm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='crm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='crm.offer.type.roles',rel='type_id'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

crm_offer_types()

class crm_offer_type_roles(Model):
	_name = 'crm.offer.type.roles'
	_description = 'General Model Role CRM Offer Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='crm.offer.types', on_delete='c'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','a'))]),
	'note': fields.text(label = 'Note')
	}

crm_offer_type_roles()

class crm_contract_types(Model):
	_name = 'crm.contract.types'
	_description = 'General Model Types CRM Contract'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='crm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='crm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='crm.contract.type.roles',rel='type_id'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

crm_contract_types()

class crm_contract_type_roles(Model):
	_name = 'crm.contract.type.roles'
	_description = 'General Model Role CRM Contract Types'
	_class_model = 'C'
	_class_category = 'delivery'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='crm.contract.types', on_delete='c'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','a'))]),
	'note': fields.text(label = 'Note')
	}

crm_contract_type_roles()

# end customize

class crm_request_categories(Model):
	_name = 'crm.request.categories'
	_description = 'General Model Category CRM Request'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='crm.request.categories'),
	'childs_id': fields.one2many(obj = 'crm.request.categories',rel = 'parent_id',label = 'Childs'),
	'requests': fields.one2many(label='Requests',obj='crm.requests',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

crm_request_categories()

class crm_offer_categories(Model):
	_name = 'crm.offer.categories'
	_description = 'General Model Category CRM Offer'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='crm.offer.categories'),
	'childs_id': fields.one2many(obj = 'crm.offer.categories',rel = 'parent_id',label = 'Childs'),
	'offers': fields.one2many(label='Offers',obj='crm.offers',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

crm_offer_categories()

class crm_contract_categories(Model):
	_name = 'crm.contract.categories'
	_description = 'General Model Category CRM Contract'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='crm.contract.categories'),
	'childs_id': fields.one2many(obj = 'crm.contract.categories',rel = 'parent_id',label = 'Childs'),
	'contracts': fields.one2many(label='Contracts',obj='crm.contracts',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

crm_contract_categories()

class crm_requests(Model):
	_name = 'crm.requests'
	_description = 'General Model CRM Request'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'dor'
	_columns = {
	'rtype': fields.many2one(label='Type',required = True,obj='crm.request.types',on_change='_on_change_rtype'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'name': fields.varchar(label = 'Name'),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname'),
	'market': fields.many2one(label='Market',obj='crm.markets'),
	'team': fields.many2one(label='Team',obj='crm.teams'),
	'category': fields.many2one(label='Category',obj='crm.request.categories'),
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
	'recepture': fields.many2one(label='Recepture',obj='md.recepture',domain=[('usage','=','s'),'|',('usage','=','a')],on_change='_on_change_recepture'),
	'items': fields.one2many(label='Items',obj='crm.request.items',rel='request_id'),
	'roles': fields.one2many(label='Roles',obj='crm.request.roles',rel='request_id'),
	'texts': fields.one2many(label='Texts',obj='crm.request.texts',rel='request_id'),
	'note': fields.text('Note')
	}
#
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

	def _on_change_rtype(self,cr,pool,uid,item,context={}):		
		roles = pool.get('crm.request.type.roles').select(cr,pool,uid,['role_id'],[('type_id','=',item['otype']['name'])],context)
		for role in roles:
			item_role = pool.get('crm.request.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)
		
		types = pool.get('crm.request.types').select(cr,pool,uid,['htschema'],[('name','=',item['otype']['name'])],context)	
		texts1 = pool.get('crm.schema.texts').select(cr,pool,uid,['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = pool.get('crm.request.texts')._buildEmptyItem()
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
				ei = pool.get('crm.request.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.utcnow()+timedelta(3)
				item_items = pool.get('crm.request.items')._buildEmptyItem()
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

crm_requests()

class crm_request_texts(Model):
	_name = 'crm.request.texts'
	_description = 'General Model CRM Request Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'request_id': fields.many2one(label='Request',obj='crm.requests'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='crm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

crm_request_texts()

class crm_request_roles(Model):
	_name = 'crm.request.roles'
	_description = 'General Model CRM Request Roles'
	_columns = {
	'request_id': fields.many2one(label = 'Request',obj='crm.requests'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

crm_request_roles()

class crm_request_items(Model):
	_name = 'crm.request.items'
	_description = 'General Model CRM Request Items'
	_inherits = {'common.model':{'_methods':['_calculate_vat_amount_costs','_calculate_items_amount_costs','_calculate_items']}}
	_columns = {
	'request_id': fields.many2one(obj = 'crm.requests',label = 'CRM Request'),
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
	'delivery_schedules': fields.one2many(label='Delivery Schedule',obj='crm.request.item.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='crm.request.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='crm.request.item.texts',rel='item_id'),
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


crm_request_items()

class crm_request_item_texts(Model):
	_name = 'crm.request.item.texts'
	_description = 'General Model CRM Request Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='crm.request.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='crm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

crm_request_item_texts()

class crm_request_item_roles(Model):
	_name = 'crm.request.item.roles'
	_description = 'General Model CRM Offer Item Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='crm.request.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

crm_request_item_roles()

class crm_request_item_delivery_schedules(Model):
	_name = 'crm.request.item.delivery.schedules'
	_description = 'General Model CRM REquest Item Delivery Schedules'
	_columns = {
	'item_id': fields.many2one(obj = 'crm.request.items',label = 'Request Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1
	}

crm_request_item_delivery_schedules()

class crm_offers(Model):
	_name = 'crm.offers'
	_description = 'General Model CRM Offer'
	_date = 'doo'
	_columns = {
	'otype': fields.many2one(label='Type',required = True,obj='crm.offer.types',on_change='_on_change_otype'),
	'name': fields.varchar(label = 'Name'),
	'category_id': fields.many2one(label='Category',obj='crm.offer.categories'),
	'company_id': fields.many2one(label='Company',obj='md.company'),
	'channel_id': fields.many2one(label='Cannel',obj='crm.channels'),
	'sector_id': fields.related(label='Sector',obj='crm.sectors',relatedy=['channel_id']),
	'team_id': fields.many2one(label='Team',obj='crm.teams'),
	'group_id': fields.related(label='Group',obj='crm.groups',relatedy=['team_id']),
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
	'recepture': fields.many2one(label='Recepture',obj='md.recepture',domain=[('usage','=','s'),'|',('usage','=','a')],on_change='_on_change_recepture'),
	'items': fields.one2many(label='Items',obj='crm.offer.items',rel='offer_id'),
	'roles': fields.one2many(label='Roles',obj='crm.offer.roles',rel='offer_id'),
	'texts': fields.one2many(label='Texts',obj='crm.offer.texts',rel='offer_id'),
	'note': fields.text('Note')
	}
#
	def _on_change_otype(self,cr,pool,uid,item,context={}):		
		roles = pool.get('crm.offer.type.roles').select(cr,pool,uid,['role_id'],[('type_id','=',item['otype']['name'])],context)
		for role in roles:
			item_role = pool.get('crm.offer.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)
		
		types = pool.get('crm.offer.types').select(cr,pool,uid,['htschema'],[('name','=',item['otype']['name'])],context)	
		texts1 = pool.get('crm.schema.texts').select(cr,pool,uid,['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = pool.get('crm.offer.texts')._buildEmptyItem()
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
				ei = pool.get('crm.offer.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.utcnow()+timedelta(3)
				item_items = pool.get('crm.offer.items')._buildEmptyItem()
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

crm_offers()

class crm_offer_texts(Model):
	_name = 'crm.offer.texts'
	_description = 'General Model CRM Offer Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'offer_id': fields.many2one(label='Offer',obj='crm.offers'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='crm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

crm_offer_texts()

class crm_offer_roles(Model):
	_name = 'crm.offer.roles'
	_description = 'General Model CRM Offer Roles'
	_columns = {
	'offer_id': fields.many2one(label = 'Request',obj='crm.offers'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

crm_offer_roles()

class crm_offer_items(Model):
	_name = 'crm.offer.items'
	_description = 'General Model CRM Offer Items'
	_inherits = {'common.model':{'_methods':['_calculate_vat_amount_costs','_calculate_items_amount_costs','_calculate_items']}}
	_columns = {
	'offer_id': fields.many2one(obj = 'crm.offers',label = 'CRM Offer'),
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
	'delivery_schedules': fields.one2many(label='Delivery Schedule',obj='crm.offer.item.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='crm.offer.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='crm.offer.item.texts',rel='item_id'),
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

crm_offer_items()

class crm_offer_item_texts(Model):
	_name = 'crm.offer.item.texts'
	_description = 'General Model CRM Offer Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='crm.offer.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='crm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

crm_offer_item_texts()

class crm_offer_item_roles(Model):
	_name = 'crm.offer.item.roles'
	_description = 'General Model CRM Offer Item Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='crm.offer.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

crm_offer_item_roles()

class crm_offer_item_delivery_schedules(Model):
	_name = 'crm.offer.item.delivery.schedules'
	_description = 'General Model CRM Offer Item Delivery Schedules'
	_columns = {
	'item_id': fields.many2one(obj = 'crm.offer.items',label = 'Offer Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
	}

crm_offer_item_delivery_schedules()

# Contract
class crm_contracts(Model):
	_name = 'crm.contracts'
	_description = 'General Model CRM Contract'
	_date = 'doc'
	_columns = {
	'ctype': fields.many2one(label='Type',obj='crm.contract.types',on_change='_on_change_ctype'),
	'name': fields.varchar(label = 'Name'),
	'category_id': fields.many2one(label='Category',obj='crm.contract.categories'),
	'company_id': fields.many2one(label='Company',obj='md.company'),
	'channel_id': fields.many2one(label='Cannel',obj='crm.channels'),
	'sector_id': fields.related(label='Sector',obj='crm.sectors',relatedy=['channel_id']),
	'team_id': fields.many2one(label='Team',obj='crm.teams'),
	'group_id': fields.related(label='Group',obj='crm.groups',relatedy=['team_id']),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'origin': fields.varchar(label = 'Origin'),
	'doc': fields.date(label='Date Of Contract',required=True),
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
	'recepture': fields.many2one(label='Recepture',obj='md.recepture',domain=[('usage','=','s'),'|',('usage','=','a')],on_change='_on_change_recepture'),
	'items': fields.one2many(label='Items',obj='crm.contract.items',rel='contract_id'),
	'roles': fields.one2many(label='Roles',obj='crm.contract.roles',rel='contract_id'),
	'texts': fields.one2many(label='Texts',obj='crm.contract.texts',rel='contract_id'),
	'payments': fields.one2many(label='Payments',obj='crm.contract.payment.schedules',rel='contarct_id'),
	'note': fields.text('Note')
	}
#
	def _on_change_ctype(self,cr,pool,uid,item,context={}):		
		roles = pool.get('crm.contract.type.roles').select(cr,pool,uid,['role_id'],[('type_id','=',item['otype']['name'])],context)
		for role in roles:
			item_role = pool.get('crm.contract.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)
		
		types = pool.get('crm.contract.types').select(cr,pool,uid,['htschema'],[('name','=',item['otype']['name'])],context)	
		texts1 = pool.get('crm.schema.texts').select(cr,pool,uid,['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = pool.get('crm.contract.texts')._buildEmptyItem()
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
				ei = pool.get('crm.contract.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.utcnow()+timedelta(3)
				item_items = pool.get('crm.contract.items')._buildEmptyItem()
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

crm_contracts()

class crm_contract_texts(Model):
	_name = 'crm.contract.texts'
	_description = 'General Model CRM Contract Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'contract_id': fields.many2one(label='Offer',obj='crm.contracts'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='crm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

crm_contract_texts()

class crm_contract_roles(Model):
	_name = 'crm.contract.roles'
	_description = 'General Model CRM Contracts Roles'
	_columns = {
	'offer_id': fields.many2one(label = 'Request',obj='crm.contracts'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

crm_contract_roles()

class crm_contract_payment_schedules(Model):
	_name = 'crm.contract.payment.schedules'
	_description = 'General Model CRM Contract Payment Schedules'
	_columns = {
	'contract_id': fields.many2one(label='Contract',obj='crm.contracts'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

crm_contract_payment_schedules()


class crm_contract_items(Model):
	_name = 'crm.contract.items'
	_description = 'General Model CRM Offer Items'
	_inherits = {'common.model':{'_methods':['_calculate_vat_amount_costs','_calculate_items_amount_costs']}}
	_columns = {
	'contract_id': fields.many2one(obj = 'crm.contracts',label = 'Contract'),
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
	'delivery_schedules': fields.one2many(label='Delivery Schedule',obj='crm.contract.item.delivery.schedules',rel='item_id'),
	'payments': fields.one2many(label='Payments',obj='crm.contract.item.payment.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='crm.contract.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='crm.contract.item.texts',rel='item_id'),
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

crm_contract_items()

class crm_contract_item_texts(Model):
	_name = 'crm.contract.item.texts'
	_description = 'General Model CRM Contract Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='crm.contract.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='crm.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

crm_contract_item_texts()

class crm_contract_item_roles(Model):
	_name = 'crm.contract.item.roles'
	_description = 'General Model CRM Contract Item Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='crm.contract.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

crm_contract_item_roles()

class crm_contract_item_delivery_schedules(Model):
	_name = 'crm.contract.item.delivery.schedules'
	_description = 'General Model CRM Contract Item Delivery Schedules'
	_columns = {
	'item_id': fields.many2one(obj = 'crm.contract.items',label = 'Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
	}

crm_contract_item_delivery_schedules()

class crm_contract_item_payment_schedules(Model):
	_name = 'crm.contract.item.payment.schedules'
	_description = 'General Model CRM Contract Item Payment Schedules'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='crm.contract.items'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

crm_contract_item_payment_schedules()




