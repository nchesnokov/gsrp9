from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

from decimal import Decimal

from datetime import datetime
from datetime import timedelta


# Organization structure
class srm_unit_categories(Model):
	_name = 'srm.unit.categories'
	_description = 'Categories Purchase Unit'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.unit.categories'),
	'childs_id': fields.one2many(obj = 'srm.unit.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'units': fields.one2many(label='Units',obj='srm.units',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_unit_categories()


class srm_units(Model):
	_name = 'srm.units'
	_description = 'Purchase Units'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='srm.unit.categories'),
	'company_id': fields.many2many(label='Companies',obj='md.company', rel='md_company_srm_unit_rel', id2='unit_id', id1='company_id'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'channels': fields.one2many(label='Channels',obj='srm.unit.channel.assigments',rel='unit_id'),
	'segments': fields.one2many(label='Segments',obj='srm.unit.segment.assigments',rel='unit_id'),
	'areas': fields.one2many(label='Areas',obj='srm.unit.area.assigments',rel='unit_id'),
	'regions': fields.one2many(label='Regions',obj='srm.unit.region.assigments',rel='unit_id')
	}

srm_units()

class srm_channel_categories(Model):
	_name = 'srm.channel.categories'
	_description = 'Categories Purchase Chanel'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.channel.categories'),
	'childs_id': fields.one2many(obj = 'srm.channel.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'channels': fields.one2many(label='Channels',obj='srm.channels',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_channel_categories()


class srm_channels(Model):
	_name = 'srm.channels'
	_description = 'Purchase Channels'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='srm.channel.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

srm_channels()

class srm_segment_categories(Model):
	_name = 'srm.segment.categories'
	_description = 'Categories Purchase Segment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.segment.categories'),
	'childs_id': fields.one2many(obj = 'srm.segment.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'segments': fields.one2many(label='Segments',obj='srm.segments',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_segment_categories()


class srm_segments(Model):
	_name = 'srm.segments'
	_description = 'Purchase Segments'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='srm.segment.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

srm_segments()

class srm_area_categories(Model):
	_name = 'srm.area.categories'
	_description = 'Categories Purchase Area'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.area.categories'),
	'childs_id': fields.one2many(obj = 'srm.area.categories',rel = 'parent_id',label = 'Childs'),
	'areas': fields.one2many(label='Areas',obj='srm.areas',rel='category_id',limit = 80,readonly=True),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'note': fields.text(label = 'Note')
	}

srm_area_categories()


class srm_areas(Model):
	_name = 'srm.areas'
	_description = 'Purchase Areas'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='srm.area.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

srm_areas()

class srm_region_categories(Model):
	_name = 'srm.region.categories'
	_description = 'Categories Purchase Region'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.region.categories'),
	'childs_id': fields.one2many(obj = 'srm.region.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'segments': fields.one2many(label='REgions',obj='srm.regions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_region_categories()


class srm_regions(Model):
	_name = 'srm.regions'
	_description = 'Purchase Regions'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='srm.region.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

srm_regions()


class srm_division_categories(Model):
	_name = 'srm.division.categories'
	_description = 'Categories Purchase Division'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.division.categories'),
	'childs_id': fields.one2many(obj = 'srm.division.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'divisions': fields.one2many(label='Divisions',obj='srm.divisions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_division_categories()


class srm_divisions(Model):
	_name = 'srm.divisions'
	_description = 'Purchase Divisions'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='srm.division.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'subdivisions': fields.one2many(label='SubDivisions',obj='srm.division.subdivision.assigments',rel='division_id')
	}

srm_divisions()

class srm_subdivision_categories(Model):
	_name = 'srm.subdivision.categories'
	_description = 'Categories Purchase Subdivision'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.subdivision.categories'),
	'childs_id': fields.one2many(obj = 'srm.subdivision.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'subdivisions': fields.one2many(label='Orders',obj='srm.subdivisions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_subdivision_categories()


class srm_subdivisions(Model):
	_name = 'srm.subdivisions'
	_description = 'Purchase Subdivisions'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='srm.subdivision.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

srm_subdivisions()

class srm_unit_channel_assigments(Model):
	_name = 'srm.unit.channel.assigments'
	_description = 'Purchase Unit Of Channel Assigment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='srm.units'),
	'channel_id': fields.many2one(label='Channel',obj='srm.channels',selectable=True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname')
	}

	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''

		if 'channel_id' in item and 'name' in item['channel_id'] and item['channel_id']['name']:
			v += item['channel_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

srm_unit_channel_assigments()

class srm_unit_segment_assigments(Model):
	_name = 'srm.unit.segment.assigments'
	_description = 'Purchase Unit Of Segment Assigment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='srm.units'),
	'segment_id': fields.many2one(label='Segment',obj='srm.segments',selectable=True),
	'fullname': fields.composite(label='Full Name',cols=['segment_id'],translate = True,required = True, compute = '_compute_composite'),
	}

	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''

		if 'segment_id' in item and 'name' in item['segment_id'] and item['segment_id']['name']:
			v += item['segment_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

srm_unit_segment_assigments()

class srm_unit_area_assigments(Model):
	_name = 'srm.unit.area.assigments'
	_description = 'Purchase Unit Of Area Assigment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='srm.units'),
	'area_id': fields.many2one(label='Area',obj='srm.areas',selectable=True),
	'fullname': fields.composite(label='Full Name',cols=['area_id'],translate = True,required = True, compute = '_compute_composite'),
	}

	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''

		if 'area_id' in item and 'name' in item['area_id'] and item['area_id']['name']:
			v += item['area_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

srm_unit_area_assigments()

class srm_unit_region_assigments(Model):
	_name = 'srm.unit.region.assigments'
	_description = 'Purchase Unit Of Region Assigment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='srm.units'),
	'region_id': fields.many2one(label='Region',obj='srm.regions',selectable=True),
	'fullname': fields.composite(label='Full Name',cols=['region_id'],translate = True,required = True, compute = '_compute_composite'),
	}

	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''

		if 'region_id' in item and 'name' in item['region_id'] and item['region_id']['name']:
			v += item['region_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

srm_unit_segment_assigments()



class srm_division_subdivision_assigments(Model):
	_name = 'srm.division.subdivision.assigments'
	_description = 'Purchase Division Of Subdivision Assigment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'division_id': fields.many2one(label='Division',obj='srm.divisions'),
	'subdivision_id': fields.many2one(label='Subdivision',obj='srm.subdivisions',selectable=True),
	'fullname': fields.composite(label='Full Name',cols=['subdivision_id'],translate = True,required = True, compute = '_compute_composite'),
	}

	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''

		if 'subdivision_id' in item and 'name' in item['subdivision_id'] and item['subdivision_id']['name']:
			v += item['subdivision_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

srm_division_subdivision_assigments()


class srm_markets(Model):
	_name = 'srm.markets'
	_description = 'Purchase Market'
	_class_model = 'C'
	_class_category = 'order'
	_rec_name = 'fullname'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='srm.units', required = True),
	'channel_id': fields.related(label='Channel',obj='srm.unit.channel.assigments', relatedy=['unit_id'], required = True),
	'segment_id': fields.related(label='Segment',obj='srm.unit.segment.assigments', relatedy=['unit_id'], required = True),
	'area_id': fields.related(label='Area',obj='srm.unit.area.assigments', relatedy=['unit_id'], required = True),
	'region_id': fields.related(label='Region',obj='srm.unit.region.assigments', relatedy=['unit_id'], required = True),
	'fullname': fields.composite(label='Full Name',cols=['unit_id','channel_id','segment_id','area_id','region_id'],translate = True,required = True, compute = '_compute_composite'),
	'note': fields.text(label='Note'),
	}

srm_markets()


class srm_teams(Model):
	_name = 'srm.teams'
	_description = 'Purchase Teams'
	_class_model = 'C'
	_class_category = 'order'
	_rec_name = 'fullname'
	_columns = {
	'division_id': fields.many2one(label='Division',obj='srm.divisions', required = True),
	'subdivision_id': fields.related(label='Subdivision',obj='srm.division.subdivision.assigments', relatedy=['division_id'], required = True),
	'fullname': fields.composite(label='Full Name',cols=['division_id','subdivision_id'],translate = True,required = True, compute = '_compute_composite'),
	'note': fields.text(label='Note'),
	}

srm_teams()

#Organization structure

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


	def _act_merge(self,cr,pool,uid,column,record,context={}):
		return ['Merge']

	_actions = {'merge':{'label':'Merge','tooltip':'Merge record','method':'_act_merge','icon':'list'}}

srm_common()

class srm_routes(Model):
	_name = 'srm.routes'
	_description = 'SRM Route'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Route',selectable = True),
	'items': fields.one2many(label='Items',obj='srm.route.items',rel='route_id'),
	'note': fields.text('Note')}

srm_routes()

class srm_route_items(Model):
	_name = 'srm.route.items'
	_description = 'SRM Route Items'
	_order_by="route_id asc,sequence asc"
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'route_id': fields.many2one(label='Route',obj='srm.routes',on_delete='c',on_update='c'),
	'sequence': fields.integer(label='Sequence'),
	'srm_object_type': fields.selection(label='SRM object type',selections=[('demand','Demand'),('plan','Plan')]),
	'note': fields.text('Note')}

srm_route_items()

class srm_demand_category(Model):
	_name = 'srm.demand.category'
	_description = 'Category SRM Demand'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.demand.category'),
	'childs_id': fields.one2many(obj = 'srm.demand.category',rel = 'parent_id',label = 'Childs'),
	'demands': fields.one2many(label='Demands',obj='srm.demands',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_demand_category()

class srm_part_category(Model):
	_name = 'srm.part.category'
	_description = 'Category SRM Part'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.part.category'),
	'childs_id': fields.one2many(obj = 'srm.part.category',rel = 'parent_id',label = 'Childs'),
	'parts': fields.one2many(label='Parts',obj='srm.parts',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_part_category()

class srm_plan_category(Model):
	_name = 'srm.plan.category'
	_description = 'Category SRM Plan'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.plan.category'),
	'childs_id': fields.one2many(obj = 'srm.plan.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'plans': fields.one2many(label='Plans',obj='srm.plans',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_plan_category()

class srm_request_category(Model):
	_name = 'srm.request.category'
	_description = 'Category SRM Request'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.request.category'),
	'childs_id': fields.one2many(obj = 'srm.request.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'requests': fields.one2many(label='Requests',obj='srm.requests',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_request_category()

class srm_response_category(Model):
	_name = 'srm.response.category'
	_description = 'Category SRM Response'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.response.category'),
	'childs_id': fields.one2many(obj = 'srm.response.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'responses': fields.one2many(label='Responses',obj='srm.responses',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_response_category()

class srm_rfx_category(Model):
	_name = 'srm.rfx.category'
	_description = 'Category SRM RFX'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.rfx.category'),
	'childs_id': fields.one2many(obj = 'srm.rfx.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'rfxs': fields.one2many(label='RFXs',obj='srm.rfxs',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_rfx_category()

class srm_auction_category(Model):
	_name = 'srm.auction.category'
	_description = 'Category SRM Auction'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.auction.category'),
	'childs_id': fields.one2many(obj = 'srm.auction.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'auctions': fields.one2many(label='Auctions',obj='srm.auctions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_auction_category()

class srm_offer_category(Model):
	_name = 'srm.offer.category'
	_description = 'Category SRM Offer'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.offer.category'),
	'childs_id': fields.one2many(obj = 'srm.offer.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'offers': fields.one2many(label='Offers',obj='srm.offers',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_offer_category()

class srm_evolution_category(Model):
	_name = 'srm.evolution.category'
	_description = 'Category SRM Evolution'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.evolution.category'),
	'childs_id': fields.one2many(obj = 'srm.evolution.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'evolutions': fields.one2many(label='Evolutions',obj='srm.evolutions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_evolution_category()

class srm_decision_category(Model):
	_name = 'srm.decision.category'
	_description = 'Category SRM Decision'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.decision.category'),
	'childs_id': fields.one2many(obj = 'srm.decision.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'decisions': fields.one2many(label='Decisions',obj='srm.decisions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_decision_category()

class srm_contract_category(Model):
	_name = 'srm.contract.category'
	_description = 'Category SRM Contract'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='srm.contract.category'),
	'childs_id': fields.one2many(obj = 'srm.contract.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'contracts': fields.one2many(label='Contracts',obj='srm.contracts',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

srm_contract_category()
# 
#customize
#Pricing
class srm_pricing_group_levels(Model):
	_name = 'srm.pricing.group.levels'
	_description = 'SRM Pricing Group Levels'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

srm_pricing_group_levels()

#Text
class srm_texts(Model):
	_name = 'srm.texts'
	_description = 'SRM Texts'
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
	_description = 'Schema Of SRM Texts'
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
	_description = 'Items Of Schema SRM Texts'
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
# Deadlines
class srm_deadlines(Model):
	_name = 'srm.deadlines'
	_description = 'SRM Deadlines'
	_class_model = 'C'
	_class_category = 'order'
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
