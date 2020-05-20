
from gsrp5service.orm import fields
from gsrp5service.orm.model import Model

class trm_inode_category(Model):
	_name = 'trm.inode.category'
	_description = 'Node Category'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='trm.inode.category'),
	'childs_id': fields.one2many(obj = 'trm.inode.category',rel = 'parent_id',label = 'Childs'),
	'note': fields.text(label='Note')
	}

trm_inode_category()

class trm_vehicle_category(Model):
	_name = 'trm.vehicle.category'
	_description = 'Vehicle Category'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='trm.vehicle.category'),
	'childs_id': fields.one2many(obj = 'trm.vehicle.category',rel = 'parent_id',label = 'Childs'),
	'note': fields.text(label='Note')
	}

trm_inode_category()


class trm_inode(Model):
	_name = 'trm.inode'
	_description = 'Node'
	_columns = {
	'itype': fields.selection(label='Type Of Node',selections=[('rs','Rayboard Station'),('rp','River Port'),('sp','Sea Port'),('tp','Transshipment Point'),('ap','Air Port'),('lo','Location'),('ps','Post Station'),('cb','Crossing The Border'),('cu','Customs')],required = True),
	'category_id': fields.many2one(label='Category',obj='trm.inode.category'),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'code': fields.varchar(label = 'Code',size=64),
	'note': fields.text(label='Note')
	}
	
	_default = {
		'itype':'rs'
	}

trm_inode()

class trm_vehicle(Model):
	_name = 'trm.vehicle'
	_description = 'Vehicle'
	_columns = {
	'vtype': fields.selection(label='Type Of Node',selections=[('rw','Rayway'),('av','Auto'),('ac','Aircraft'),('rv','Кiverboat'),('sb','Sea Ship'),('rs','River Sea Ship'),('po','Post'),('pi','Pipeline')],required = True),
	'category_id': fields.many2one(label='Category',obj='trm.vehicle.category'),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'code': fields.varchar(label = 'Code',size=64),
	'note': fields.text(label='Note')
	}
	
	_default = {
		'vtype':'rw'
	}

trm_vehicle()

class trm_unit_vehicle(Model):
	_name = 'trm.unit.vehicle'
	_description = 'Unit Vehicle'
	_columns = {
	'vihicle_id': fields.many2one(label='Vehicle',obj='trm.vehicle'),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'code': fields.varchar(label = 'Code',size=64),
	'note': fields.text(label='Note')
	}

trm_unit_vehicle()
