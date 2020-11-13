from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

class mrp_demand_category(Model):
	_name = 'mrp.demand.category'
	_description = 'Category MRP Demand'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='mrp.demand.category'),
	'childs_id': fields.one2many(obj = 'mrp.demand.category',rel = 'parent_id',label = 'Childs'),
	'demands': fields.one2many(label='Demands',obj='mrp.demand',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

mrp_demand_category()

class mrp_request_category(Model):
	_name = 'mrp.request.category'
	_description = 'Category MRP Request'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='mrp.request.category'),
	'childs_id': fields.one2many(obj = 'mrp.request.category',rel = 'parent_id',label = 'Childs'),
	'requests': fields.one2many(label='Requests',obj='mrp.request',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

mrp_request_category()

class mrp_demand(Model):
	_name = 'mrp.demand'
	_description = 'MRP Demand'
	_date = 'dod'
	_columns = {
	'dtype': fields.many2one(label='Type',obj='mrp.demand.types',on_change='_on_change_dtype'),
	'name': fields.varchar(label = 'Name'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'fullname': fields.composite(label='Full Name', cols = ['company','dtype','name'], translate = True,required = True, compute = '_compute_composite'),
	'category_id': fields.many2one(label='Category',obj='mrp.demand.category'),
	'origin': fields.varchar(label = 'Origin'),
	'dod': fields.date(label='Date Of Demand',required=True),
	'from_date': fields.date(label='Begin Date Of Demand',required=True),
	'to_date': fields.date(label='End Date Of Demand',required=True),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'items': fields.one2many(label='Items',obj='mrp.demand.items',rel='demand_id'),
	'roles': fields.one2many(label='Roles',obj='mrp.demand.roles',rel='demand_id'),
	'texts': fields.one2many(label='Texts',obj='mrp.demand.texts',rel='demand_id'),
	'note': fields.text('Note')}

	_default = {
		'state':'draft'
	}

	def _on_change_dtype(self,item,context={}):		
		roles = self._pool.get('mrp.demand.type.roles').select( ['role_id'],[('type_id','=',item['dtype']['name'])],context)
		for role in roles:
			item_role = self._pool.get('mrp.demand.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)
		
		types = self._pool.get('mrp.demand.types').select( ['htschema'],[('name','=',item['dtype']['name'])],context)	
		texts1 = self._pool.get('mrp.schema.texts').select( ['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = self._pool.get('mrp.demand.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)


mrp_demand()

class mrp_demand_texts(Model):
	_name = 'mrp.demand.texts'
	_description = 'MRP Demand Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'demand_id': fields.many2one(label='Demand',obj='mrp.demand', on_delete='c'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='mrp.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

mrp_demand_texts()


class mrp_demand_roles(Model):
	_name = 'mrp.demand.roles'
	_description = 'MRP Demand Roles'
	_columns = {
	'demand_id': fields.many2one(label = 'Demand',obj='mrp.demand', on_delete='c'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

mrp_demand_roles()


class mrp_demand_items(Model):
	_name = 'mrp.demand.items'
	_description = 'MRP Demand Item'
	_rec_name = None
	_hooks = {'aar':'_on_add_row'}
	_columns = {
	'demand_id': fields.many2one(obj = 'mrp.demand',label = 'Demand', on_delete='c'),
	'product': fields.many2one(label='Product',obj='md.product'),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'schedules': fields.one2many(label='Schedule',obj='mrp.demand.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='mrp.demand.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='mrp.demand.item.texts',rel='item_id'),
	'note': fields.text(label = 'Note')}

	def _on_add_row(self,item,context={}):
		data = context['data']
		types = self._pool.get('mrp.demand.types').select( ['itschema'],[('name','=',data['dtype']['name'])],context)
		texts1 = self._pool.get('mrp.schema.texts').select( ['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['itschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = self._pool.get('mrp.demand.item.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
			seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

mrp_demand_items()

class mrp_demand_item_texts(Model):
	_name = 'mrp.demand.item.texts'
	_description = 'MRP Demand Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='mrp.demand.items', on_delete='c'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='mrp.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

mrp_demand_item_texts()


class mrp_demand_item_roles(Model):
	_name = 'mrp.demand.item.roles'
	_description = 'MRP Demand Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='mrp.demand.items', on_delete='c'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

mrp_demand_item_roles()


class mrp_demand_delivery_schedules(Model):
	_name = 'mrp.demand.delivery.schedules'
	_description = 'MRP Demand Delivery Schedule'
	_rec_name = None
	_columns = {
	'item_id': fields.many2one(obj = 'mrp.demand.items',label = 'Item', on_delete='c'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
	}

mrp_demand_delivery_schedules()

####
class mrp_request(Model):
	_name = 'mrp.request'
	_description = 'MRP Request'
	_date = 'dor'
	_columns = {
	'rtype': fields.many2one(label='Type',obj='mrp.request.types',on_change='on_change_rtype'),
	'name': fields.varchar(label = 'Name'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'fullname': fields.composite(label='Full Name', cols = ['company','rtype','name'], translate = True,required = True, compute = '_compute_composite'),
	'category_id': fields.many2one(label='Category',obj='mrp.request.category'),
	'origin': fields.varchar(label = 'Origin'),
	'dor': fields.date(label='Date Of Request',required=True),
	'from_date': fields.date(label='Begin Date Of Request',required=True),
	'to_date': fields.date(label='End Date Of Request',required=True),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'items': fields.one2many(label='Items',obj='mrp.request.items',rel='request_id'),
	'roles': fields.one2many(label='Roles',obj='mrp.request.roles',rel='request_id'),
	'texts': fields.one2many(label='Texts',obj='mrp.request.texts',rel='request_id'),
	'note': fields.text('Note')}

	def _on_change_rtype(self,item,context={}):		
		roles = self._pool.get('mrp.request.type.roles').select( ['role_id'],[('type_id','=',item['rtype']['name'])],context)
		for role in roles:
			item_role = self._pool.get('mrp.request.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)
		
		types = self._pool.get('mrp.request.types').select( ['htschema'],[('name','=',item['rtype']['name'])],context)	
		texts1 = self._pool.get('mrp.schema.texts').select( ['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = self._pool.get('mrp.request.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

	_default = {
		'state':'draft'
	}

mrp_request()

class mrp_request_texts(Model):
	_name = 'mrp.request.texts'
	_description = 'MRP Request Texts'
	_class_model = 'C'
	_class_category = 'invoice'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'request_id': fields.many2one(label='Request',obj='mrp.request', on_delete='c'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='mrp.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

mrp_request_texts()


class mrp_request_roles(Model):
	_name = 'mrp.request.roles'
	_description = 'Purchase Invoice Roles'
	_columns = {
	'invoice_id': fields.many2one(label = 'Request',obj='mrp.request', on_delete='c'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

mrp_request_roles()


class mrp_request_items(Model):
	_name = 'mrp.request.items'
	_description = 'MRP Request Item'
	_rec_name = None
	_hooks = {'aar':'_on_add_row'}
	_columns = {
	'request_id': fields.many2one(obj = 'mrp.request',label = 'Request', on_delete='c'),
	'product': fields.many2one(label='Product',obj='md.product'),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'schedules': fields.one2many(label='Schedule',obj='mrp.request.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='mrp.request.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='mrp.request.item.texts',rel='item_id'),
	'note': fields.text(label = 'Note')}

	def _on_add_row(self,item,context={}):
		data = context['data']
		types = self._pool.get('mrp.request.types').select( ['itschema'],[('name','=',data['rtype']['name'])],context)
		texts1 = self._pool.get('mrp.schema.texts').select( ['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['itschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = self._pool.get('mrp.request.item.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
			seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

mrp_request_items()

class mrp_request_item_texts(Model):
	_name = 'mrp.request.item.texts'
	_description = 'MRP Request Item Texts'
	_class_model = 'C'
	_class_category = 'invoice'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='mrp.request.items', on_delete='c'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='mrp.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

mrp_request_item_texts()


class mrp_request_item_roles(Model):
	_name = 'mrp.request.item.roles'
	_description = 'MRP Request Item Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='mrp.request.items', on_delete='c'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('S','B'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

mrp_request_item_roles()


class mrp_request_delivery_schedules(Model):
	_name = 'mrp.request.delivery.schedules'
	_description = 'MRP Request Delivery Schedule'
	_rec_name = None
	_columns = {
	'item_id': fields.many2one(obj = 'mrp.request.items',label = 'Item', on_delete='c'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
	}

mrp_request_delivery_schedules()

class md_mrp_product(Model):
	_name = 'md.mrp.product'
	_description = 'Mrp Of Product'
	_columns = {
	'product_id': fields.many2one(label='Product',obj='md.product'),
	'strategy': fields.selection(label='Strategy',selections=[('l','Lot'),('p','Point of order'),('n','Not planed')]),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'reserved_quantity': fields.numeric(label='Reserve Quantity',size=(11,3)),
	'min_quantity': fields.numeric(label='Min Quantity',size=(11,3)),
	'max_quantity': fields.numeric(label='Max Quantity',size=(11,3)),
	'uom': fields.many2one(label="Unit Of Measure",obj='md.uom'),
	'note': fields.text(label = 'Note'),
	}

md_mrp_product()

class md_mrp_product_inherit(ModelInherit):
	_name = 'md.mrp.product.inherit'
	_description = 'Genaral Model Inherit For MRP Product'
	_inherit = {'md.product':{'_columns':['mrp']},'md.boms':{'_columns':['usage']},'seq.conditions':{'_columns':['usage']},'seq.access.schemas':{'_columns':['usage']},'seq.access':{'_columns':['usage']}}
	_columns = {
		'mrp': fields.one2many(label='MRP',obj='md.mrp.product',rel='product_id'),
		'usage': fields.iProperty(selections=[('mrp',"Material Planning")])
	}
	
md_mrp_product_inherit()

