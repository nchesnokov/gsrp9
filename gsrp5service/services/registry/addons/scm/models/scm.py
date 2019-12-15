from gsrp5service.orm import fields
from gsrp5service.orm.model import Model

class scm_workcenter_category(Model):
	_name = 'scm.workcenter.category'
	_description = 'General Model Category Workcenter'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='scm.workcenter.category'),
	'childs_id': fields.one2many(obj = 'scm.workcenter.category',rel = 'parent_id',label = 'Childs'),
	'workcenters': fields.one2many(label='Orders',obj='scm.workcenter',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

scm_workcenter_category()

class scm_route_category(Model):
	_name = 'scm.route.category'
	_description = 'General Model Category Route'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='scm.route.category'),
	'childs_id': fields.one2many(obj = 'scm.route.category',rel = 'parent_id',label = 'Childs'),
	'routes': fields.one2many(label='Orders',obj='scm.route',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

scm_route_category()


class scm_production_order_category(Model):
	_name = 'scm.production.order.category'
	_description = 'General Model Category Production Order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='scm.production.order.category'),
	'childs_id': fields.one2many(obj = 'scm.production.order.category',rel = 'parent_id',label = 'Childs'),
	'orders': fields.one2many(label='Orders',obj='scm.production.order',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

scm_production_order_category()

class scm_technologic_order_category(Model):
	_name = 'scm.technologic.order.category'
	_description = 'General Model Category Technologic Order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='scm.technologic.order.category'),
	'childs_id': fields.one2many(obj = 'scm.technologic.order.category',rel = 'parent_id',label = 'Childs'),
	'orders': fields.one2many(label='Orders',obj='scm.technologic.order',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

scm_technologic_order_category()

class scm_disassembly_order_category(Model):
	_name = 'scm.disassembly.order.category'
	_description = 'General Model Category Disassembly Order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='scm.disassembly.order.category'),
	'childs_id': fields.one2many(obj = 'scm.disassembly.order.category',rel = 'parent_id',label = 'Childs'),
	'orders': fields.one2many(label='Orders',obj='scm.disassembly.order',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

scm_disassembly_order_category()
# workcenter
class scm_workcenter(Model):
	_name = 'scm.workcenter'
	_description = 'General Model Workcenter'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'wctype': fields.selection(label='Type',selections=[('p','Production'),('t','Technology'),('d','Disassembly'),('a','All')]),
	'cost_peer_hour': fields.numeric(label='Cost Peer Hours',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'products': fields.one2many(label='Products',obj='scm.workcenter.products',rel='workcenter_id',limit = 80),
	'note': fields.text(label = 'Note')
	}

scm_workcenter()

class scm_workcenter_products(Model):
	_name = 'scm.workcenter.products'
	_description = 'General Model Workcenter Products'
	_columns = {
	'workcenter_id': fields.many2one(label='Workcenter',obj='scm.workcenter'),
	'product': fields.many2one(label='Product',obj='md.product'),
	'prices': fields.one2many(label='Prices',obj='scm.workcenter.product.prices',rel='product_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

scm_workcenter_products()

class scm_workcenter_product_prices(Model):
	_name = 'scm.workcenter.product.prices'
	_description = 'General Model Workcenter Product Prices'
	_columns = {
	'product_id': fields.many2one(label='Product',obj='scm.workcenter.products'),
	'from_date': fields.datetime(label='From',timezone=True),
	'to_date': fields.datetime(label='To',timezone=True),
	'price': fields.numeric(label='Price Peer Hours',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price Peer Hours",obj='md.uom',),
	'note': fields.text(label = 'Note')
	}

scm_workcenter_product_prices()

#route
class scm_route(Model):
	_name = 'scm.route'
	_description = 'General Model Route'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'category_id': fields.many2one(label='Category',obj='scm.route.category'),
	'rtype': fields.selection(label='Type',selections=[('p','Production'),('t','Technology'),('d','Disassembly'),('a','All')]),
	'items': fields.one2many(obj = 'scm.route.items',rel = 'route_id',label = 'Items'),
	'note': fields.text(label = 'Note')
	}

scm_route()

class scm_route_items(Model):
	_name = 'scm.route.items'
	_description = 'General Model Route Items'
	_columns = {
	'route_id': fields.many2one(label='Route',obj='scm.route'),
	'workcenter': fields.many2one(label='Workcenter',obj='scm.workcenter'),
	'parent_id': fields.many2one(label='Parent',obj='scm.route.items'),
	'childs_id': fields.one2many(obj = 'scm.route.items',rel = 'parent_id',label = 'Childs'),
	'note': fields.text(label = 'Note')
	}

scm_route_items()

#production
class scm_production_order(Model):
	_name = 'scm.production.order'
	_description = 'General Model Production Order'
	_date = 'dopo'
	_columns = {
	'name': fields.varchar(label = 'Name'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'category_id': fields.many2one(label='Category',obj='scm.production.order.category'),
	'origin': fields.varchar(label = 'Origin'),
	'dopo': fields.date(label='Date Of Production Order',required=True),
	'from_date': fields.date(label='Start Date Of Production Order',required=True),
	'to_date': fields.date(label='End Date Of Production Order',required=True),
	'route': fields.many2one(label='Route',obj='scm.route',domain=[('rtype','in',('p','a'))]),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'items': fields.one2many(label='Items',obj='scm.production.order.items',rel='order_id'),
	'note': fields.text('Note')}

	_default = {
		'state':'draft'
	}

scm_production_order()

class scm_production_order_items(Model):
	_name = 'scm.production.order.items'
	_description = 'General Model Production Order Items'
	_columns = {
	'order_id': fields.many2one(obj = 'scm.production.order',label = 'Production Order'),
	'recepture_id': fields.many2one(label='Recepture',obj='md.recepture',domain=[('type','=','real'),('subtype','=','bom'),[('usage','=','m'),'|',('usage','=','a')]],on_change='_on_change_recepture'),
	'product': fields.many2one(label='Product',obj='md.product',readonly=True),
	'parent_id': fields.many2one(label='Parent',obj='scm.production.order.items'),
	'childs_id': fields.one2many(obj = 'scm.production.order.items',rel = 'parent_id',label = 'Childs'),
	'boms': fields.one2many(label='BoM',obj='scm.production.order.item.bom',rel='item_id'),
	'schedules': fields.one2many(label='Schedule',obj='scm.production.order.delivery.schedules',rel='item_id'),
	'note': fields.text(label = 'Note')}

	def _on_change_recepture(self,cr,pool,uid,item,context={}):		
		if item['recepture_id'] and 'name' in item['recepture_id'] and item['recepture_id']['name']:
			p = pool.get('md.recepture.input').select(cr,pool,uid,['product','quantity','uom'],[('recepture_id','=',item['recepture_id']['name'])],context)
			for i in p:
				r = {'product':i['product'],'quantity':i['quantity'],'uom':i['uom']}
				r['price'] = 0.00
				r['amount'] = 0.00
				item['boms'].append(r)
				
			b = pool.get('md.recepture.output').select(cr,pool,uid,['product'],[('recepture_id','=',item['recepture_id']['name'])],context)
			if len(b) > 0:
				item['product'] = b[0]['product']
	
		return None


scm_production_order_items()

class scm_production_order_item_bom(Model):
	_name = 'scm.production.order.item.bom'
	_description = 'General Model Production Order Items BoM'
	_columns = {
	'item_id': fields.many2one(obj = 'scm.production.order.items',label = 'Item'),
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


scm_production_order_item_bom()

class scm_production_order_delivery_schedules(Model):
	_name = 'scm.production.order.delivery.schedules'
	_description = 'General Model Production Order Delivery Schedule'
	_columns = {
	'item_id': fields.many2one(obj = 'scm.production.order.items',label = 'Item'),
	'part': fields.numeric(label='Part',size=(11,3),required=True,check='part > 0.000'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'part': 1.000
	}

scm_production_order_delivery_schedules()

# Technologic
class scm_technologic_order(Model):
	_name = 'scm.technologic.order'
	_description = 'General Model Technologic Order'
	_date = 'doto'
	_columns = {
	'name': fields.varchar(label = 'Name'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'category_id': fields.many2one(label='Category',obj='scm.technologic.order.category'),
	'origin': fields.varchar(label = 'Origin'),
	'doto': fields.date(label='Date Of Technologic Order',required=True),
	'from_date': fields.date(label='Start Date Of Technologic Order',required=True),
	'to_date': fields.date(label='End Date Of Technologic Order',required=True),
	'route': fields.many2one(label='Route',obj='scm.route',domain=[('rtype','in',('p','a'))]),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'items': fields.one2many(label='Items',obj='scm.technologic.order.items',rel='order_id'),
	'note': fields.text('Note')}

	_default = {
		'state':'draft'
	}

scm_technologic_order()

class scm_technologic_order_items(Model):
	_name = 'scm.technologic.order.items'
	_description = 'General Model Technologic Order Items'
	_columns = {
	'order_id': fields.many2one(obj = 'scm.technologic.order',label = 'Technologic Order'),
	'recepture_id': fields.many2one(label='Recepture',obj='md.recepture',domain=[('type','=','real'),('subtype','=','bob'),[('usage','=','m'),'|',('usage','=','a')]],on_change='_on_change_recepture'),
	'parent_id': fields.many2one(label='Parent',obj='scm.technologic.order.items'),
	'childs_id': fields.one2many(obj = 'scm.technologic.order.items',rel = 'parent_id',label = 'Childs'),
	'ibobs': fields.one2many(label='InBoB',obj='scm.technologic.order.item.ibob',rel='item_id'),
	'obobs': fields.one2many(label='OutBoB',obj='scm.technologic.order.item.obob',rel='item_id'),
	'schedules': fields.one2many(label='Schedule',obj='scm.technologic.order.delivery.schedules',rel='item_id'),
	'note': fields.text(label = 'Note')}

	def _on_change_recepture(self,cr,pool,uid,item,context={}):		
		if item['recepture_id'] and 'name' in item['recepture_id'] and item['recepture_id']['name']:
			p = pool.get('md.recepture.input').select(cr,pool,uid,['product','quantity','uom'],[('recepture_id','=',item['recepture_id']['name'])],context)
			for i in p:
				r = {'product':i['product'],'quantity':i['quantity'],'uom':i['uom']}
				r['price'] = 0.00
				r['amount'] = 0.00
				item['ibobs'].append(r)
				
			p = pool.get('md.recepture.output').select(cr,pool,uid,['product','quantity','uom'],[('recepture_id','=',item['recepture_id']['name'])],context)
			for i in p:
				r = {'product':i['product'],'quantity':i['quantity'],'uom':i['uom']}
				r['price'] = 0.00
				r['amount'] = 0.00
				item['obobs'].append(r)
				
		return None

scm_technologic_order_items()

class scm_technologic_order_item_ibob(Model):
	_name = 'scm.technologic.order.item.ibob'
	_description = 'General Model Technologic Order Items InBoB'
	_columns = {
	'item_id': fields.many2one(obj = 'scm.technologic.order.items',label = 'Item'),
	'product': fields.many2one(label='Product',obj='md.product'),
	'quantity': fields.numeric(label='Quantity',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'note': fields.text(label = 'Note')}

scm_technologic_order_item_ibob()

class scm_technologic_order_item_obob(Model):
	_name = 'scm.technologic.order.item.obob'
	_description = 'General Model Technologic Order Items OutBoB'
	_columns = {
	'item_id': fields.many2one(obj = 'scm.technologic.order.items',label = 'Item'),
	'product': fields.many2one(label='Product',obj='md.product'),
	'quantity': fields.numeric(label='Quantity',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'note': fields.text(label = 'Note')}

scm_technologic_order_item_obob()

class scm_technologic_order_delivery_schedules(Model):
	_name = 'scm.technologic.order.delivery.schedules'
	_description = 'General Model Technologic Order Delivery Schedule'
	_columns = {
	'item_id': fields.many2one(obj = 'scm.technologic.order.items',label = 'Item'),
	'part': fields.numeric(label='Part',size=(11,3),required=True,check='part > 0.000'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'part': 1.000
	}

scm_technologic_order_delivery_schedules()

# Disassebly
class scm_disassembly_order(Model):
	_name = 'scm.disassembly.order'
	_description = 'General Model Disassembly Order'
	_date = 'dodo'
	_columns = {
	'name': fields.varchar(label = 'Name'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'category_id': fields.many2one(label='Category',obj='scm.disassembly.order.category'),
	'origin': fields.varchar(label = 'Origin'),
	'dodo': fields.date(label='Date Of Disassembly Order',required=True),
	'from_date': fields.date(label='Start Date Of Disassembly Order',required=True),
	'to_date': fields.date(label='End Date Of Disassembly Order',required=True),
	'route': fields.many2one(label='Route',obj='scm.route',domain=[('rtype','in',('p','a'))]),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'items': fields.one2many(label='Items',obj='scm.disassembly.order.items',rel='order_id'),
	'note': fields.text('Note')}

	_default = {
		'state':'draft'
	}

scm_disassembly_order()

class scm_disassembly_order_items(Model):
	_name = 'scm.disassembly.order.items'
	_description = 'General Model Disassembly Order Items'
	_columns = {
	'order_id': fields.many2one(obj = 'scm.disassembly.order',label = 'Technologic Order'),
	'recepture_id': fields.many2one(label='Recepture',obj='md.recepture',domain=[('type','=','real'),('subtype','=','mob'),[('usage','=','m'),'|',('usage','=','a')]],on_change='_on_change_recepture'),
	'product': fields.many2one(label='Product',obj='md.product',readonly=True),
	'parent_id': fields.many2one(label='Parent',obj='scm.disassembly.order.items'),
	'childs_id': fields.one2many(obj = 'scm.disassembly.order.items',rel = 'parent_id',label = 'Childs'),
	'mobs': fields.one2many(label='MoB',obj='scm.disassembly.order.item.mob',rel='item_id'),
	'schedules': fields.one2many(label='Schedule',obj='scm.disassembly.order.delivery.schedules',rel='item_id'),
	'note': fields.text(label = 'Note')}

	def _on_change_recepture(self,cr,pool,uid,item,context={}):		
		if item['recepture_id'] and 'name' in item['recepture_id'] and item['recepture_id']['name']:
			p = pool.get('md.recepture.output').select(cr,pool,uid,['product','quantity','uom'],[('recepture_id','=',item['recepture_id']['name'])],context)
			for i in p:
				r = {'product':i['product'],'quantity':i['quantity'],'uom':i['uom']}
				r['price'] = 0.00
				r['amount'] = 0.00
				item['mobs'].append(r)
				
			b = pool.get('md.recepture.input').select(cr,pool,uid,['product'],[('recepture_id','=',item['recepture_id']['name'])],context)
			if len(b) > 0:
				item['product'] = b[0]['product']

		return None

scm_disassembly_order_items()

class scm_disassembly_order_item_mob(Model):
	_name = 'scm.disassembly.order.item.mob'
	_description = 'General Model Disassembly Order Items MoB'
	_columns = {
	'item_id': fields.many2one(obj = 'scm.disassembly.order.items',label = 'Item'),
	'product': fields.many2one(label='Product',obj='md.product'),
	'quantity': fields.numeric(label='Quantity',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'note': fields.text(label = 'Note')}

scm_disassembly_order_item_mob()

class scm_disassembly_order_delivery_schedules(Model):
	_name = 'scm.disassembly.order.delivery.schedules'
	_description = 'General Model Disassembly Order Delivery Schedule'
	_columns = {
	'item_id': fields.many2one(obj = 'scm.disassembly.order.items',label = 'Item'),
	'part': fields.numeric(label='Part',size=(11,3),required=True,check='part > 0.000'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'part': 1.000
	}

scm_disassembly_order_delivery_schedules()

