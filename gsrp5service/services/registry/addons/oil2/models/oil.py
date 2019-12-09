from orm import fields
from orm.model import Model

class oil_field_category(Model):
	_name = 'oil.field.category'
	_description = 'General Model Field Category'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='oil.field.category'),
	'childs_id': fields.one2many(obj = 'oil.field.category',rel = 'parent_id',label = 'Childs'),
	'fields': fields.one2many(label='Fields',obj='oil.field',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')

	}

oil_field_category()

class oil_reservoir_category(Model):
	_name = 'oil.reservoir.category'
	_description = 'General Model Reservoir Category'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='oil.reservoir.category'),
	'childs_id': fields.one2many(obj = 'oil.reservoir.category',rel = 'parent_id',label = 'Childs'),
	'reservoirs': fields.one2many(label='Reservoirs',obj='oil.reservoir',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')

	}

oil_reservoir_category()

class oil_platform_category(Model):
	_name = 'oil.platform.category'
	_description = 'General Model Platform Category'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='oil.platform.category'),
	'childs_id': fields.one2many(obj = 'oil.platform.category',rel = 'parent_id',label = 'Childs'),
	'platforms': fields.one2many(label='Platforms',obj='oil.platform',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')

	}

oil_reservoir_category()

class oil_well_category(Model):
	_name = 'oil.well.category'
	_description = 'General Model Well Category'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='oil.well.category'),
	'childs_id': fields.one2many(obj = 'oil.well.category',rel = 'parent_id',label = 'Childs'),
	'wells': fields.one2many(label='Wells',obj='oil.well',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')

	}

oil_well_category()



class oil_field(Model):
	_name = 'oil.field'
	_description = 'General Model Field'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='oil.field.category'),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'fid': fields.varchar(label = 'ID',size=16,translate=True),
	'tproduct': fields.selection(label = 'Product Type',selections=[('1','Oil'),('2','Natura Gas'),('3','Condensate'),('4','Plant NGLS'),('5','Water'),('7','Sulfur'),('9','Injectants')]),
	'wdu': fields.many2one(label='Water Depth Unit',obj='md.uom'),
	'wd': fields.numeric(label='Water Depth Unit',size=(13,3)),
	'descr': fields.text(label='Description')
	}
	
	_default = {
		'tproduct':'1'
	}

oil_field()

class oil_reservoir(Model):
	_name = 'oil.reservoir'
	_description = 'General Model Reservoir'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='oil.reservoir.category'),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'rid': fields.varchar(label = 'ID',size=16,translate=True),
	'descr': fields.text(label='Description')
	}
	
oil_reservoir()

class oil_platform(Model):
	_name = 'oil.platform'
	_description = 'General Model Platform'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='oil.platform.category'),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'pid': fields.varchar(label = 'ID',size=16,translate=True),
	'fpd': fields.date(label='First production date'),
	'pid': fields.date(label='Installation Date'),
	'nlatitude': fields.numeric(label='Latitude number',size=(8,6)),
	'dclatitude': fields.varchar(label='Latitude direction code',size=1),
	'descr': fields.text(label='Description')
	}
	
oil_platform()

class oil_well(Model):
	_name = 'oil.well'
	_description = 'General Model Well'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='oil.well.category'),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'wid': fields.varchar(label = 'ID',size=16,translate=True),
	'descr': fields.text(label='Description')
	}
	
oil_well()
