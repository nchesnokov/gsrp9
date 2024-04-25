from gsrp5service.orm import fields
from gsrp5service.orm.model import Model,ModelInherit

#customize
# Organization structure
class prj_unit_categories(Model):
	_name = 'prj.unit.categories'
	_description = 'Categories Project Unit'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='prj.unit.categories'),
	'childs_id': fields.one2many(obj = 'prj.unit.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'units': fields.one2many(label='Units',obj='prj.units',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

prj_unit_categories()


class prj_units(Model):
	_name = 'prj.units'
	_description = 'Project Units'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='prj.unit.categories'),
	'company_ids': fields.many2many(label='Companies',obj='md.company', rel='md_company_prj_unit_rel', id2='unit_id', id1='company_id'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'channels': fields.one2many(label='Channels',obj='prj.unit.channel.assigments',rel='unit_id'),
	'segments': fields.one2many(label='Segments',obj='prj.unit.segment.assigments',rel='unit_id'),
	'areas': fields.one2many(label='Areas',obj='prj.unit.area.assigments',rel='unit_id'),
	'regions': fields.one2many(label='Regions',obj='prj.unit.region.assigments',rel='unit_id')
	}

prj_units()

class prj_channel_categories(Model):
	_name = 'prj.channel.categories'
	_description = 'Categories Project Chanel'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='prj.channel.categories'),
	'childs_id': fields.one2many(obj = 'prj.channel.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'channels': fields.one2many(label='Channels',obj='prj.channels',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

prj_channel_categories()


class prj_channels(Model):
	_name = 'prj.channels'
	_description = 'Project Channels'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='prj.channel.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

prj_channels()

class prj_segment_categories(Model):
	_name = 'prj.segment.categories'
	_description = 'Categories Project Segment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='prj.segment.categories'),
	'childs_id': fields.one2many(obj = 'prj.segment.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'segments': fields.one2many(label='Segments',obj='prj.segments',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

prj_segment_categories()


class prj_segments(Model):
	_name = 'prj.segments'
	_description = 'Project Segments'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='prj.segment.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

prj_segments()

class prj_area_categories(Model):
	_name = 'prj.area.categories'
	_description = 'Categories Project Area'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='prj.area.categories'),
	'childs_id': fields.one2many(obj = 'prj.area.categories',rel = 'parent_id',label = 'Childs'),
	'areas': fields.one2many(label='Areas',obj='prj.areas',rel='category_id',limit = 80,readonly=True),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'note': fields.text(label = 'Note')
	}

prj_area_categories()


class prj_areas(Model):
	_name = 'prj.areas'
	_description = 'Project Areas'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='prj.area.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

prj_areas()

class prj_region_categories(Model):
	_name = 'prj.region.categories'
	_description = 'Categories Project Region'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='prj.region.categories'),
	'childs_id': fields.one2many(obj = 'prj.region.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'segments': fields.one2many(label='REgions',obj='prj.regions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

prj_region_categories()


class prj_regions(Model):
	_name = 'prj.regions'
	_description = 'Project Regions'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='prj.region.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

prj_regions()


class prj_division_categories(Model):
	_name = 'prj.division.categories'
	_description = 'Categories Project Division'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='prj.division.categories'),
	'childs_id': fields.one2many(obj = 'prj.division.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'divisions': fields.one2many(label='Divisions',obj='prj.divisions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

prj_division_categories()


class prj_divisions(Model):
	_name = 'prj.divisions'
	_description = 'Project Divisions'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='prj.division.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'subdivisions': fields.one2many(label='SubDivisions',obj='prj.division.subdivision.assigments',rel='division_id')
	}

prj_divisions()

class prj_subdivision_categories(Model):
	_name = 'prj.subdivision.categories'
	_description = 'Categories Project Subdivision'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='prj.subdivision.categories'),
	'childs_id': fields.one2many(obj = 'prj.subdivision.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'subdivisions': fields.one2many(label='Orders',obj='prj.subdivisions',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

prj_subdivision_categories()


class prj_subdivisions(Model):
	_name = 'prj.subdivisions'
	_description = 'Project Subdivisions'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='prj.subdivision.categories'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

prj_subdivisions()

class prj_unit_channel_assigments(Model):
	_name = 'prj.unit.channel.assigments'
	_description = 'Project Unit Of Channel Assigment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='prj.units'),
	'channel_id': fields.many2one(label='Channel',obj='prj.channels',selectable=True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname')
	}

	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''

		if 'channel_id' in item and 'name' in item['channel_id'] and item['channel_id']['name']:
			v += item['channel_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

prj_unit_channel_assigments()

class prj_unit_segment_assigments(Model):
	_name = 'prj.unit.segment.assigments'
	_description = 'Project Unit Of Segment Assigment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='prj.units'),
	'segment_id': fields.many2one(label='Segment',obj='prj.segments',selectable=True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname')
	}

	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''

		if 'segment_id' in item and 'name' in item['segment_id'] and item['segment_id']['name']:
			v += item['segment_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

prj_unit_segment_assigments()

class prj_unit_area_assigments(Model):
	_name = 'prj.unit.area.assigments'
	_description = 'Project Unit Of Area Assigment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='prj.units'),
	'area_id': fields.many2one(label='Area',obj='prj.areas',selectable=True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname')
	}

	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''

		if 'area_id' in item and 'name' in item['area_id'] and item['area_id']['name']:
			v += item['area_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

prj_unit_area_assigments()

class prj_unit_region_assigments(Model):
	_name = 'prj.unit.region.assigments'
	_description = 'Project Unit Of Region Assigment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='prj.units'),
	'region_id': fields.many2one(label='Region',obj='prj.regions',selectable=True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname')
	}

	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''

		if 'region_id' in item and 'name' in item['region_id'] and item['region_id']['name']:
			v += item['region_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

prj_unit_segment_assigments()



class prj_division_subdivision_assigments(Model):
	_name = 'prj.division.subdivision.assigments'
	_description = 'Project Division Of Subdivision Assigment'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'division_id': fields.many2one(label='Division',obj='prj.divisions'),
	'subdivision_id': fields.many2one(label='Subdivision',obj='prj.subdivisions',selectable=True),
	'fullname': fields.varchar(label='Full Name',translate = True,required = True, compute = '_compute_fullname'),
	}

	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''

		if 'subdivision_id' in item and 'name' in item['subdivision_id'] and item['subdivision_id']['name']:
			v += item['subdivision_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

prj_division_subdivision_assigments()


class prj_markets(Model):
	_name = 'prj.markets'
	_description = 'Project Market'
	_class_model = 'C'
	_class_category = 'order'
	_rec_name = 'fullname'
	_columns = {
	'unit_id': fields.many2one(label='Unit',obj='prj.units', required = True),
	'channel_id': fields.related(label='Channel',obj='prj.unit.channel.assigments', relatedy=['unit_id'], required = True),
	'segment_id': fields.related(label='Segment',obj='prj.unit.segment.assigments', relatedy=['unit_id'], required = True),
	'area_id': fields.related(label='Area',obj='prj.unit.area.assigments', relatedy=['unit_id'], required = True),
	'region_id': fields.related(label='Region',obj='prj.unit.region.assigments', relatedy=['unit_id'], required = True),
	'fullname': fields.tree(label='Full Name',translate = True,required = True),
	'note': fields.text(label='Note'),
	}

prj_markets()


class prj_teams(Model):
	_name = 'prj.teams'
	_description = 'Project Teams'
	_class_model = 'C'
	_class_category = 'order'
	_rec_name = 'fullname'
	_columns = {
	'division_id': fields.many2one(label='Division',obj='prj.divisions', required = True),
	'subdivision_id': fields.related(label='Subdivision',obj='prj.division.subdivision.assigments', relatedy=['division_id'], required = True),
	'fullname': fields.composite(label='Full Name',cols=['division_id','subdivision_id'],translate = True,required = True),
	'note': fields.text(label='Note'),
	}

prj_teams()


#Organization structure

#Organization structure
#Pricing
class prj_pricing_group_levels(Model):
	_name = 'prj.pricing.group.levels'
	_description = 'Project Pricing Group Levels'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

prj_pricing_group_levels()

#Text
class prj_texts(Model):
	_name = 'prj.texts'
	_description = 'Project Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

prj_texts()

class prj_schema_texts(Model):
	_name = 'prj.schema.texts'
	_description = 'Schema Of Project Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'usage': fields.selection(label='Usage',selections=[('h','Header'),('i','Item'),('b','Both')]),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'texts': fields.one2many(label='Texts',obj='prj.schema.text.items',rel='schema_id')
	}

prj_schema_texts()

class prj_schema_text_items(Model):
	_name = 'prj.schema.text.items'
	_description = 'Items Of Schema Project Texts'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'schema_id': fields.many2one(label = 'Schema',obj='prj.schema.texts'),
	'seq': fields.integer(label='Sequence'),
	'text_id': fields.many2one(label = 'Text',obj='prj.texts'),
	'descr': fields.link(ref='text_id.descr')
	}

prj_schema_text_items()

# Text end
class prj_bill_types(Model):
	_name = 'prj.bill.types'
	_description = 'Types Project Bill'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'ptype': fields.selection(label='Type',selections=[('ord','Order'),('ap','Advance Payment'),('ps','Pseduo'),('dm','Debit Request'),('cr','Credit Request'),('rо','Return')]),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='prj.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='prj.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='prj.bill.type.roles',rel='type_id'),
	'plates': fields.one2many(label='Plates',obj='prj.bill.type.plates',rel='type_id'),
	'tis': fields.one2many(label='TIs',obj='prj.bill.type.items',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

prj_bill_types()

class prj_bill_type_roles(Model):
	_name = 'prj.bill.type.roles'
	_description = 'Role Project BIll Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='prj.bill.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

prj_bill_type_roles()


class prj_bill_type_plates(Model):
	_name = 'prj.bill.type.plates'
	_description = 'Project Bill Plates'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='prj.bill.types'),
	'seq': fields.integer(label='Sequence',required=True),
	'plate': fields.many2one(label = 'Plate',obj='md.type.plates',required=True,domain=[('usage','=','prj'),'|',('usage','=','prj')]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

prj_bill_type_plates()

class prj_bill_type_items(Model):
	_name = 'prj.bill.type.items'
	_description = 'Plates Of Project Bill Items'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='prj.bill.types'),
	'gti_id': fields.many2one(label = 'GTI',obj='md.gtis'),
	'itype_id': fields.many2one(label = 'Type Of Items',obj='md.type.items',domain=[('usage','=','prj'),'|',('usage','=','a')]),
	'note': fields.text(label = 'Note')
	}

prj_bill_type_items()


class prj_resource_category(Model):
	_name = 'prj.resource.category'
	_description = 'Category Project Resource'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='prj.resource.category'),
	'childs_id': fields.one2many(obj = 'prj.resource.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'projects': fields.one2many(label='Projects',obj='prj.resource',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

prj_resource_category()

class prj_bill_category(Model):
	_name = 'prj.bill.category'
	_description = 'Category Project Bill'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='prj.bill.category'),
	'childs_id': fields.one2many(obj = 'prj.bill.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'bills': fields.one2many(label='Bills',obj='prj.bill',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

prj_bill_category()

class prj_portfolio_category(Model):
	_name = 'prj.portfolio.category'
	_description = 'Category Project Portfolio'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='prj.portfolio.category'),
	'childs_id': fields.one2many(obj = 'prj.portfolio.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'portfolios': fields.one2many(label='Portfolios',obj='prj.portfolio',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

prj_portfolio_category()

class prj_prj_category(Model):
	_name = 'prj.prj.category'
	_description = 'Category Project Project'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='prj.prj.category'),
	'childs_id': fields.one2many(obj = 'prj.prj.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'projects': fields.one2many(label='Projects',obj='prj.project',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

prj_prj_category()

class prj_stage_category(Model):
	_name = 'prj.stage.category'
	_description = 'Category Project Stage'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='prj.stage.category'),
	'childs_id': fields.one2many(obj = 'prj.stage.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'stages': fields.one2many(label='Orders',obj='prj.stage',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

prj_stage_category()

class prj_task_category(Model):
	_name = 'prj.task.category'
	_description = 'Category Project Task'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='prj.task.category'),
	'childs_id': fields.one2many(obj = 'prj.task.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'tasks': fields.one2many(label='Tasks',obj='prj.task',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

prj_task_category()

class prj_element_category(Model):
	_name = 'prj.element.category'
	_description = 'Category Project Element'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='prj.element.category'),
	'childs_id': fields.one2many(obj = 'prj.element.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'elements': fields.one2many(label='Elements',obj='prj.element',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

prj_element_category()

