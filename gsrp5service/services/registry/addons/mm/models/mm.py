from gsrp5service.orm import fields
from gsrp5service.orm.model import Model

class mm_workcenter_category(Model):
	_name = 'mm.workcenter.category'
	_description = 'General Model Category Workcenter'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='mm.workcenter.category'),
	'childs_id': fields.one2many(obj = 'mm.workcenter.category',rel = 'parent_id',label = 'Childs'),
	'workcenters': fields.one2many(label='Orders',obj='mm.workcenter',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

mm_workcenter_category()

class mm_route_category(Model):
	_name = 'mm.route.category'
	_description = 'General Model Category Route'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='mm.route.category'),
	'childs_id': fields.one2many(obj = 'mm.route.category',rel = 'parent_id',label = 'Childs'),
	'routes': fields.one2many(label='Orders',obj='mm.route',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

mm_route_category()


class mm_production_order_category(Model):
	_name = 'mm.production.order.category'
	_description = 'General Model Category Production Order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='mm.production.order.category'),
	'childs_id': fields.one2many(obj = 'mm.production.order.category',rel = 'parent_id',label = 'Childs'),
	'orders': fields.one2many(label='Orders',obj='mm.production.order',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

mm_production_order_category()

class mm_technologic_order_category(Model):
	_name = 'mm.technologic.order.category'
	_description = 'General Model Category Technologic Order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='mm.technologic.order.category'),
	'childs_id': fields.one2many(obj = 'mm.technologic.order.category',rel = 'parent_id',label = 'Childs'),
	'orders': fields.one2many(label='Orders',obj='mm.technologic.order',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

mm_technologic_order_category()

class mm_disassembly_order_category(Model):
	_name = 'mm.disassembly.order.category'
	_description = 'General Model Category Disassembly Order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='mm.disassembly.order.category'),
	'childs_id': fields.one2many(obj = 'mm.disassembly.order.category',rel = 'parent_id',label = 'Childs'),
	'orders': fields.one2many(label='Orders',obj='mm.disassembly.order',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

mm_disassembly_order_category()
# workcenter
class mm_workcenter(Model):
	_name = 'mm.workcenter'
	_description = 'General Model Workcenter'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'wctype': fields.selection(label='Type',selections=[('p','Production'),('t','Technology'),('d','Disassembly'),('a','All')]),
	'cost_peer_hour': fields.numeric(label='Cost Peer Hours',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'products': fields.one2many(label='Products',obj='mm.workcenter.products',rel='workcenter_id',limit = 80),
	'note': fields.text(label = 'Note')
	}

mm_workcenter()

class mm_workcenter_products(Model):
	_name = 'mm.workcenter.products'
	_description = 'General Model Workcenter Products'
	_columns = {
	'workcenter_id': fields.many2one(label='Workcenter',obj='mm.workcenter'),
	'product': fields.many2one(label='Product',obj='md.product'),
	'prices': fields.one2many(label='Prices',obj='mm.workcenter.product.prices',rel='product_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

mm_workcenter_products()

class mm_workcenter_product_prices(Model):
	_name = 'mm.workcenter.product.prices'
	_description = 'General Model Workcenter Product Prices'
	_columns = {
	'product_id': fields.many2one(label='Product',obj='mm.workcenter.products'),
	'from_date': fields.datetime(label='From',timezone=True),
	'to_date': fields.datetime(label='To',timezone=True),
	'price': fields.numeric(label='Price Peer Hours',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price Peer Hours",obj='md.uom',),
	'note': fields.text(label = 'Note')
	}

mm_workcenter_product_prices()

#route
class mm_route(Model):
	_name = 'mm.route'
	_description = 'General Model Route'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'category_id': fields.many2one(label='Category',obj='mm.route.category'),
	'rtype': fields.selection(label='Type',selections=[('p','Production'),('t','Technology'),('d','Disassembly'),('a','All')]),
	'items': fields.one2many(obj = 'mm.route.items',rel = 'route_id',label = 'Items'),
	'note': fields.text(label = 'Note')
	}

mm_route()

class mm_route_items(Model):
	_name = 'mm.route.items'
	_description = 'General Model Route Items'
	_columns = {
	'route_id': fields.many2one(label='Route',obj='mm.route'),
	'workcenter': fields.many2one(label='Workcenter',obj='mm.workcenter'),
	'parent_id': fields.many2one(label='Parent',obj='mm.route.items'),
	'childs_id': fields.one2many(obj = 'mm.route.items',rel = 'parent_id',label = 'Childs'),
	'note': fields.text(label = 'Note')
	}

mm_route_items()

#production
class mm_production_order(Model):
	_name = 'mm.production.order'
	_description = 'General Model Production Order'
	_date = 'dopo'
	_columns = {
	'name': fields.varchar(label = 'Name'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'category_id': fields.many2one(label='Category',obj='mm.production.order.category'),
	'origin': fields.varchar(label = 'Origin'),
	'dopo': fields.date(label='Date Of Production Order',required=True),
	'from_date': fields.date(label='Start Date Of Production Order',required=True),
	'to_date': fields.date(label='End Date Of Production Order',required=True),
	'route': fields.many2one(label='Route',obj='mm.route',domain=[('rtype','in',('p','a'))]),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'items': fields.one2many(label='Items',obj='mm.production.order.items',rel='order_id'),
	'note': fields.text('Note')}

	_default = {
		'state':'draft'
	}

mm_production_order()

class mm_production_order_items(Model):
	_name = 'mm.production.order.items'
	_description = 'General Model Production Order Items'
	_columns = {
	'order_id': fields.many2one(obj = 'mm.production.order',label = 'Production Order'),
	'recepture_id': fields.many2one(label='Recepture',obj='md.recepture',domain=[('type','=','real'),('subtype','=','bom'),[('usage','=','m'),'|',('usage','=','a')]],on_change='_on_change_recepture'),
	'product': fields.many2one(label='Product',obj='md.product',readonly=True),
	'parent_id': fields.many2one(label='Parent',obj='mm.production.order.items'),
	'childs_id': fields.one2many(obj = 'mm.production.order.items',rel = 'parent_id',label = 'Childs'),
	'boms': fields.one2many(label='BoM',obj='mm.production.order.item.bom',rel='item_id'),
	'schedules': fields.one2many(label='Schedule',obj='mm.production.order.delivery.schedules',rel='item_id'),
	'note': fields.text(label = 'Note')}

	def _on_change_recepture(self,cr,pool,uid,item,context={}):		
		if item['recepture_id'] and 'name' in item['recepture_id'] and item['recepture_id']['name']:
			p = pool.get('md.recepture.input').select(cr,pool,uid,['product','quantity','uom'],[('recepture_id','=',item['recepture_id']['name'])],context)
			for i in p:
				ei = pool.get('mm.production.order.item.bom')._buildEmptyItem()
				ei['product'] = i['product']
				ei['quantity'] = i['quantity']
				ei['uom'] = i['uom']
				ei['price'] = 0.00
				ei['amount'] = 0.00
				item['boms'].append(ei)
				
			b = pool.get('md.recepture.output').select(cr,pool,uid,['product'],[('recepture_id','=',item['recepture_id']['name'])],context)
			if len(b) > 0:
				item['product'] = b[0]['product']
	
		return None

mm_production_order_items()

class mm_production_order_item_bom(Model):
	_name = 'mm.production.order.item.bom'
	_description = 'General Model Production Order Items BoM'
	_columns = {
	'item_id': fields.many2one(obj = 'mm.production.order.items',label = 'Item'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='calculate_item_bom'),
	'note': fields.text(label = 'Note')}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.cost.product').select(cr,pool,uid,['uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
			if len(p) > 0:
				for f in ('uom','price','currency','unit','uop'):
					if f not in item or item[f] != p[0][f]:
						item[f] = p[0][f]
			else:
				for f in ('uom','price','currency','unit','uop'):
					if f in ('price','unit'):
						if f in self._default:
							item[f] = self._default[f]
						else:
							item[f] = None
					else:
						item[f] = {'id':None,'name':None}

		return None

	def _calculate_item_bom(self,cr,pool,uid,item,context={}):		
		if 'quantity' in item and 'oum' in item and 'price' in item and 'currency' in item and 'unit' in item and 'uop' in item:
			item['amount'] = item['price'] / item['unit'] * item['quantity']

		return None


mm_production_order_item_bom()

class mm_production_order_delivery_schedules(Model):
	_name = 'mm.production.order.delivery.schedules'
	_description = 'General Model Production Order Delivery Schedule'
	_columns = {
	'item_id': fields.many2one(obj = 'mm.production.order.items',label = 'Item'),
	'part': fields.numeric(label='Part',size=(11,3),required=True,check='part > 0.000'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'part': 1.000
	}

mm_production_order_delivery_schedules()

# Technologic
class mm_technologic_order(Model):
	_name = 'mm.technologic.order'
	_description = 'General Model Technologic Order'
	_date = 'doto'
	_columns = {
	'name': fields.varchar(label = 'Name'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'category_id': fields.many2one(label='Category',obj='mm.technologic.order.category'),
	'origin': fields.varchar(label = 'Origin'),
	'doto': fields.date(label='Date Of Technologic Order',required=True),
	'from_date': fields.date(label='Start Date Of Technologic Order',required=True),
	'to_date': fields.date(label='End Date Of Technologic Order',required=True),
	'route': fields.many2one(label='Route',obj='mm.route',domain=[('rtype','in',('p','a'))]),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'items': fields.one2many(label='Items',obj='mm.technologic.order.items',rel='order_id'),
	'note': fields.text('Note')}

	_default = {
		'state':'draft'
	}

mm_technologic_order()

class mm_technologic_order_items(Model):
	_name = 'mm.technologic.order.items'
	_description = 'General Model Technologic Order Items'
	_columns = {
	'order_id': fields.many2one(obj = 'mm.technologic.order',label = 'Technologic Order'),
	'recepture_id': fields.many2one(label='Recepture',obj='md.recepture',domain=[('type','=','real'),('subtype','=','bob'),[('usage','=','m'),'|',('usage','=','a')]],on_change='_on_change_recepture'),
	'parent_id': fields.many2one(label='Parent',obj='mm.technologic.order.items'),
	'childs_id': fields.one2many(obj = 'mm.technologic.order.items',rel = 'parent_id',label = 'Childs'),
	'ibobs': fields.one2many(label='InBoB',obj='mm.technologic.order.item.ibob',rel='item_id'),
	'obobs': fields.one2many(label='OutBoB',obj='mm.technologic.order.item.obob',rel='item_id'),
	'schedules': fields.one2many(label='Schedule',obj='mm.technologic.order.delivery.schedules',rel='item_id'),
	'note': fields.text(label = 'Note')}

	def _on_change_recepture(self,cr,pool,uid,item,context={}):		
		if item['recepture_id'] and 'name' in item['recepture_id'] and item['recepture_id']['name']:
			p = pool.get('md.recepture.input').select(cr,pool,uid,['product','quantity','uom'],[('recepture_id','=',item['recepture_id']['name'])],context)
			for i in p:
				ei = pool.get('mm.technologic.order.item.ibob')._buildEmptyItem()
				ei['product'] = i['product']
				ei['quantity'] = i['quantity']
				ei['uom'] = i['uom']
				ei['price'] = 0.00
				ei['amount'] = 0.00
				item['ibobs'].append(ei)
				
			p = pool.get('md.recepture.output').select(cr,pool,uid,['product','quantity','uom'],[('recepture_id','=',item['recepture_id']['name'])],context)
			for i in p:
				ei = pool.get('mm.technologic.order.item.obob')._buildEmptyItem()
				ei['product'] = i['product']
				ei['quantity'] = i['quantity']
				ei['uom'] = i['uom']
				ei['price'] = 0.00
				ei['amount'] = 0.00
				item['obobs'].append(ei)
				
		return None

mm_technologic_order_items()

class mm_technologic_order_item_ibob(Model):
	_name = 'mm.technologic.order.item.ibob'
	_description = 'General Model Technologic Order Items InBoB'
	_columns = {
	'item_id': fields.many2one(obj = 'mm.technologic.order.items',label = 'Item'),
	'product': fields.many2one(label='Product',obj='md.product'),
	'quantity': fields.numeric(label='Quantity',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'note': fields.text(label = 'Note')}

mm_technologic_order_item_ibob()

class mm_technologic_order_item_obob(Model):
	_name = 'mm.technologic.order.item.obob'
	_description = 'General Model Technologic Order Items OutBoB'
	_columns = {
	'item_id': fields.many2one(obj = 'mm.technologic.order.items',label = 'Item'),
	'product': fields.many2one(label='Product',obj='md.product'),
	'quantity': fields.numeric(label='Quantity',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'note': fields.text(label = 'Note')}

mm_technologic_order_item_obob()

class mm_technologic_order_delivery_schedules(Model):
	_name = 'mm.technologic.order.delivery.schedules'
	_description = 'General Model Technologic Order Delivery Schedule'
	_columns = {
	'item_id': fields.many2one(obj = 'mm.technologic.order.items',label = 'Item'),
	'part': fields.numeric(label='Part',size=(11,3),required=True,check='part > 0.000'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'part': 1.000
	}

mm_technologic_order_delivery_schedules()

# Disassebly
class mm_disassembly_order(Model):
	_name = 'mm.disassembly.order'
	_description = 'General Model Disassembly Order'
	_date = 'dodo'
	_columns = {
	'name': fields.varchar(label = 'Name'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'category_id': fields.many2one(label='Category',obj='mm.disassembly.order.category'),
	'origin': fields.varchar(label = 'Origin'),
	'dodo': fields.date(label='Date Of Disassembly Order',required=True),
	'from_date': fields.date(label='Start Date Of Disassembly Order',required=True),
	'to_date': fields.date(label='End Date Of Disassembly Order',required=True),
	'route': fields.many2one(label='Route',obj='mm.route',domain=[('rtype','in',('p','a'))]),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'items': fields.one2many(label='Items',obj='mm.disassembly.order.items',rel='order_id'),
	'note': fields.text('Note')}

	_default = {
		'state':'draft'
	}

mm_disassembly_order()

class mm_disassembly_order_items(Model):
	_name = 'mm.disassembly.order.items'
	_description = 'General Model Disassembly Order Items'
	_columns = {
	'order_id': fields.many2one(obj = 'mm.disassembly.order',label = 'Technologic Order'),
	'recepture_id': fields.many2one(label='Recepture',obj='md.recepture',domain=[('type','=','real'),('subtype','=','mob'),[('usage','=','m'),'|',('usage','=','a')]],on_change='_on_change_recepture'),
	'product': fields.many2one(label='Product',obj='md.product',readonly=True),
	'parent_id': fields.many2one(label='Parent',obj='mm.disassembly.order.items'),
	'childs_id': fields.one2many(obj = 'mm.disassembly.order.items',rel = 'parent_id',label = 'Childs'),
	'mobs': fields.one2many(label='MoB',obj='mm.disassembly.order.item.mob',rel='item_id'),
	'schedules': fields.one2many(label='Schedule',obj='mm.disassembly.order.delivery.schedules',rel='item_id'),
	'note': fields.text(label = 'Note')}

	def _on_change_recepture(self,cr,pool,uid,item,context={}):		
		if item['recepture_id'] and 'name' in item['recepture_id'] and item['recepture_id']['name']:				
			p = pool.get('md.recepture.output').select(cr,pool,uid,['product','quantity','uom'],[('recepture_id','=',item['recepture_id']['name'])],context)
			for i in p:
				ei = pool.get('mm.disassembly.order.item.mob')._buildEmptyItem()
				ei['product'] = i['product']
				ei['quantity'] = i['quantity']
				ei['uom'] = i['uom']
				ei['price'] = 0.00
				ei['amount'] = 0.00
				item['mobs'].append(ei)
				
			b = pool.get('md.recepture.input').select(cr,pool,uid,['product'],[('recepture_id','=',item['recepture_id']['name'])],context)
			if len(b) > 0:
				item['product'] = b[0]['product']

		return None

mm_disassembly_order_items()

class mm_disassembly_order_item_mob(Model):
	_name = 'mm.disassembly.order.item.mob'
	_description = 'General Model Disassembly Order Items MoB'
	_columns = {
	'item_id': fields.many2one(obj = 'mm.disassembly.order.items',label = 'Item'),
	'product': fields.many2one(label='Product',obj='md.product'),
	'quantity': fields.numeric(label='Quantity',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'note': fields.text(label = 'Note')}

mm_disassembly_order_item_mob()

class mm_disassembly_order_delivery_schedules(Model):
	_name = 'mm.disassembly.order.delivery.schedules'
	_description = 'General Model Disassembly Order Delivery Schedule'
	_columns = {
	'item_id': fields.many2one(obj = 'mm.disassembly.order.items',label = 'Item'),
	'part': fields.numeric(label='Part',size=(11,3),required=True,check='part > 0.000'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'part': 1.000
	}

mm_disassembly_order_delivery_schedules()

