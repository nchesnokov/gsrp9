from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

from decimal import Decimal

from datetime import datetime
from datetime import timedelta

class crm_requests(Model):
	_name = 'crm.requests'
	_description = 'CRM Requests'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_rec_name = 'fullname'
	_class_category = 'crm-request'
	_date = 'doo'
	_columns = {
	'otype': fields.referenced(label='Type',obj='crm.request.types',on_change='_on_change_otype',required=True),
	'name': fields.i18n(fields.varchar(label = 'Name',required=True)),
	'company': fields.referenced(label='Company',obj='md.company',required=True),
	'fullname': fields.i18n(fields.composite(label='Full Name', cols = ['company','otype','name'],required = True)),
	'market': fields.referenced(label='Market',obj='crm.markets',required=True),
	'team': fields.many2one(label='Team',obj='crm.teams',required=True),
	'category_id': fields.many2one(label='Category',obj='crm.request.categories',required=True),
	'origin': fields.varchar(label = 'Origin'),
	'manager': fields.many2one(label='Manager',obj='bc.users',required=True),
	'doo': fields.date(label='Date Of Order',required=True),
	'from_date': fields.date(label='Begin Date Of Order',required=True),
	'to_date': fields.date(label='End Date Of Order',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('iscustomer',)]),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	'incoterms1': fields.many2one(label='Incoterms 1',obj='md.incoterms',required=True),
	'incoterms2': fields.varchar(label = 'Incoterms 2',required=True),
	'state': fields.i18n(fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')],required=True)),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'mob': fields.referenced(label='BoM',obj='md.boms',domain=[('usage','=','crm'),'|',('usage','=','all')],on_change='_on_change_mob'),
	'items': fields.one2many(label='Items',obj='crm.request.items',rel='request_id'),
	'pricing': fields.one2many(label='Pricing',obj='crm.request.pricing',rel='request_id'),
	'roles': fields.one2many(label='Roles',obj='crm.request.roles',rel='request_id'),
	'texts': fields.one2many(label='Texts',obj='crm.request.texts',rel='request_id'),
	'plates': fields.one2many(label='Plates',obj='crm.request.output.plates',rel='request_id'),
	'payments': fields.one2many(label='Payments',obj='crm.request.payment.schedules',rel='request_id'),
	'note': fields.i18n(fields.text('Note'))
	}

	def _on_change_otype(self ,item,context={}):		
		roles = self.selectFor('crm.request.type.roles',['role_id'],[('type_id','=',item['otype']['name'])],context)
		for role in roles:
			item_role = self._model('crm.request.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)
		
		types = self.selectFor('crm.request.types', ['htschema'],[('name','=',item['otype']['name'])],context)	
		texts1 = self.selectFor('crm.schema.texts', ['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		if len(texts1) > 0:
			texts = texts1[0]['texts']
			seq = 0
			for text in texts:
				item_text = self._model('crm.request.texts')._buildEmptyItem()
				if text['seq']:
					item_text['seq'] = text['seq']
				else:
					item_text['seq'] = seq
					seq += 10
				item_text['text_id'] = text['text_id']
				item['texts'].append(item_text)

	def _on_change_mob(self ,item,context={}):		
		if item['mob'] and 'name' in item['mob'] and item['mob']['name']:
			p = self.selectFor('md.mob.output.items', ['product','quantity','uom'],[('mob_id','=',item['mob']['name'])],context)
			for i in p:
				ei = self._model('crm.request.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.now().astimezone()+timedelta(3)
				item_items = self._model('crm.request.items')._buildEmptyItem()
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

#crm_requests()

class crm_request_texts(Model):
	_name = 'crm.request.texts'
	_description = 'CRM Request Texts'
	_class_model = 'C'
	_class_category = 'crm-request'
	_request_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'request_id': fields.many2one(label='Request',obj='crm.requests',rel='texts'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.referenced(label='Text ID',obj='crm.texts'),
	'descr': fields.link(ref='text_id.descr'),
	'content':fields.i18n(fields.text(label = 'Content'))
	}

#crm_request_texts()

class crm_request_roles(Model):
	_name = 'crm.request.roles'
	_description = 'CRM Request Roles'
	_class_category = 'crm-request'
	_columns = {
	'request_id': fields.many2one(label = 'Request',obj='crm.requests',rel='roles'),
	'role_id': fields.referenced(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.referenced(label = 'Parther',obj='md.partner',required=True)
	}

#crm_request_roles()

class crm_request_pricing(Model):
	_name = 'crm.request.pricing'
	_description = 'CRM Request Pricing'
	_class_category = 'crm-request'
	_columns = {
	'request_id': fields.many2one(label = 'Request',obj='crm.requests',rel='pricing'),
	'level': fields.integer(label = 'Level',required=True),
	'cond': fields.referenced(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','s')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.referenced(label = 'Group Level',obj='crm.pricing.group.levels'),
	'amount': fields.numeric(label='Amount',size=(15,2),required=True),
	'currency': fields.referenced(label='Currency',obj='md.currency',required=True),
	}

#crm_request_pricing()

class crm_request_payment_schedules(Model):
	_name = 'crm.request.payment.schedules'
	_description = 'CRM Request Payment Schedules'
	_class_category = 'crm-request'
	_columns = {
	'request_id': fields.many2one(label = 'Request',obj='crm.requests'),
	'amount': fields.numeric(label='Amount',size=(15,2),required=True),
	'currency': fields.referenced(label='Currency',obj='md.currency',required=True),
	'schedule': fields.datetime(label='Schedule',required=True),
	'note': fields.i18n(fields.text(label = 'Note'))
	}

#crm_request_payment_schedules()

class crm_request_output_plates(Model):
	_name = 'crm.request.output.plates'
	_description = 'CRM Request Output Plates'
	_class_category = 'crm-request'
	_columns = {
	'request_id': fields.many2one(label = 'Request',obj='crm.requests'),
	'state': fields.i18n(fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True)),
	'otype': fields.referenced(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.referenced(label='Partner',obj='md.partner',required=True,domain=[('iscustomer',)]),
	'role': fields.referenced(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('c','i','p','a'))]),
	'language': fields.referenced(label = 'language',obj='md.language',required=True),
	'msm': fields.i18n(fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True)),
	'schedule': fields.datetime(label='Schedule',required=True),
	'note': fields.i18n(fields.text(label = 'Note'))
	}
	
	_default = {
		'state':'c'
	}

#crm_request_output_plates()

class crm_request_items(Model):
	_name = 'crm.request.items'
	_description = 'CRM Request Items'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_class_category = 'crm-request'
	_columns = {
	'request_id': fields.many2one(obj = 'crm.requests',label = 'CRM Request'),
	'itype_id': fields.referenced(label='Group Of Type Items', obj='md.type.items',required=True,domain=[('usage','in',('s','a'))]),
	'product': fields.referenced(label='Product',obj='md.product',required=True,on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.referenced(label='UoM',obj='md.uom',required=True),
	'price': fields.numeric(label='Price',size=(13,3),required=True),
	'currency': fields.referenced(label='Currency',obj='md.currency',required=True),
	'unit': fields.integer(label='Unit',required=True),
	'uop': fields.referenced(label="Unit Of Price",obj='md.uom',required=True),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.referenced(label='Vat code',obj='md.vat.code',required=True,domain=[('type_vat','in',('s','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'volume': fields.float(label='Volume', readonly=True),
	'volume_total': fields.float(label='Volume Total', readonly=True),
	'volume_uom': fields.many2one(label="Volume UoM",obj='md.uom', readonly=True,domain=[('quantity_id','=','Volume')]),
	'weight': fields.float(label='Weight', readonly=True),
	'weight_total': fields.float(label='Weight Total', readonly=True),
	'weight_uom': fields.many2one(label="Weight UoM",obj='md.uom', readonly=True,domain=[('quantity_id','=','Weight')]),
	'delivery_schedules': fields.one2many(label='Delivery Schedule',obj='crm.request.item.delivery.schedules',rel='item_id'),
	'pricing': fields.one2many(label='Pricing',obj='crm.request.pricing.items',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='crm.request.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='crm.request.item.texts',rel='item_id'),
	'plates': fields.one2many(label='Plates',obj='crm.request.item.output.plates',rel='item_id'),
	'payments': fields.one2many(label='Payments',obj='crm.request.item.payment.schedules',rel='item_id'),
	'note': fields.i18n(fields.text(label = 'Note'))
	}

	def _on_change_product(self ,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			i = self._proxy.get('crm.request.type.items').select( ['gti_id','itype_id'],[],context)
			gti = {}
			if len(i) > 0:
				for r in i:
					gti[r['gti_id']['name']] = r['itype_id']
			p = self._proxy.get('md.product').select( ['name','gti','volume','volume_uom','weight','weight_uom',{'crm':['vat','uom','price','currency','unit','uop']}],[('name','=',item['product']['name'])],context)
			if len(p) > 0:
				for f in ('gti','volume','volume_uom','weight','weight_uom','crm'):
					if f == 'crm':
						if len(p[0][f]) > 0:
							d = p[0][f][0]
							for m in ('uom','price','currency','unit','uop','vat'):
								if m not in item or item[m] != d[m]:
									if m == 'vat':
										item['vat_code'] = d['vat']				
									else:
										item[m] = d[m]
					else:
						if f == 'gti':
							if p[0]['gti']['name'] in gti:
								item['itype_id'] = gti[p[0][f]['name']]
						else:
							if f not in item or item[f] != p[0][f]:
								item[f] = p[0][f]

			else:
				for f in ('vat_code','uom','price','currency','unit','uop'):
					if f in ('price','unit'):
						if f in self._default:
							item[f] = self._default[f]
						else:
							item[f] = None
					else:
						item[f] = {'id':None,'name':None}

		return None

	_default = {
		'quantity': 1,
		'unit': 1
	}

#crm_request_items()

class crm_request_pricing_items(Model):
	_name = 'crm.request.pricing.items'
	_description = 'CRM Request Item Pricing'
	_class_category = 'crm-request'
	_columns = {
	'item_id': fields.many2one(label = 'Request',obj='crm.request.items',rel='pricing'),
	'level': fields.integer(label = 'Level',required=True),
	'cond': fields.referenced(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','s')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.referenced(label = 'Group Level',obj='crm.pricing.group.levels'),
	'price': fields.numeric(label='Price',size=(13,2),required=True),
	'cop': fields.referenced(label='Currency Of Price',obj='md.currency',required=True),
	'unit': fields.integer(label='Unit',required=True),
	'uop': fields.referenced(label="Unit Of Price",obj='md.uom',required=True),
	'amount': fields.numeric(label='Amount',size=(15,2),required=True),
	'currency': fields.referenced(label='Currency',obj='md.currency',required=True),
	}

#crm_request_pricing_items()

class crm_request_item_texts(Model):
	_name = 'crm.request.item.texts'
	_description = 'CRM Request Item Texts'
	_class_category = 'crm-request'
	_request_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='crm.request.items',rel='texts'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.referenced(label='Text ID',obj='crm.texts',required=True),
	'descr': fields.link(ref='text_id.descr'),
	'content':fields.i18n(fields.text(label = 'Content'))
	}

#crm_request_item_texts()


class crm_request_item_roles(Model):
	_name = 'crm.request.item.roles'
	_description = 'CRM Request Roles'
	_class_category = 'crm-request'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='crm.request.items',rel='roles'),
	'role_id': fields.referenced(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.referenced(label = 'Parther',obj='md.partner',required=True)
	}

#crm_request_item_roles()


class crm_request_item_delivery_schedules(Model):
	_name = 'crm.request.item.delivery.schedules'
	_description = 'CRM Request Item Delivery Schedules'
	_class_category = 'crm-request'
	_columns = {
	'item_id': fields.many2one(obj = 'crm.request.items',label = 'Order Item',rel='delivery_schedules'),
	'quantity': fields.numeric(label='Quantity',size=(11,3),required=True),
	'schedule': fields.datetime(label='Schedule',required=True),
	'note': fields.i18n(fields.text(label = 'Note'))
	}

	_default = {
		'quantity': 1.000
	}

#crm_request_item_delivery_schedules()

class crm_request_item_output_plates(Model):
	_name = 'crm.request.item.output.plates'
	_description = 'CRM Request Item Output Plates'
	_class_category = 'crm-request'
	_columns = {
	'item_id': fields.many2one(label = 'Request',obj='crm.request.items',rel='plates'),
	'state': fields.i18n(fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True)),
	'otype': fields.referenced(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.referenced(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.referenced(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.referenced(label = 'language',obj='md.language',required=True),
	'msm': fields.i18n(fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True)),
	'schedule': fields.datetime(label='Schedule',required=True),
	'note': fields.i18n(fields.text(label = 'Note'))
	}
	
	_default = {
		'state':'c'
	}

#crm_request_item_output_plates()

class crm_request_item_payment_schedules(Model):
	_name = 'crm.request.item.payment.schedules'
	_description = 'CRM Request Item Payment Schedules'
	_class_category = 'crm-request'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='crm.request.items',rel='payments'),
	'amount': fields.numeric(label='Amount',size=(15,2),required=True),
	'currency': fields.referenced(label='Currency',obj='md.currency',required=True),
	'schedule': fields.datetime(label='Schedule',required=True),
	'note': fields.i18n(fields.text(label = 'Note'))
	}

#crm_request_item_payment_schedules()

# Offer
class crm_offers(Model):
	_name = 'crm.offers'
	_description = 'CRM Offers'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'doi'
	_class_category = 'crm-offer'
	_columns = {
	'itype': fields.referenced(label='Type',obj='crm.offer.types',required = True,on_change='on_change_itype'),
	'name': fields.varchar(label = 'Name',required = True),
	'company': fields.referenced(label='Company',obj='md.company',required = True),
	'fullname': fields.i18n(fields.composite(label='Full Name', cols = ['company','itype','name'],required = True)),
	'market': fields.referenced(label='Market',obj='crm.markets',required = True),
	'team': fields.referenced(label='Team',obj='crm.teams',required = True),
	'category_id': fields.many2one(label='Category',obj='crm.offer.categories',rel='offers',required = True),
	'origin': fields.varchar(label = 'Origin'),
	'doi': fields.date(label='Date Of Invoice',required=True),
	'partner': fields.referenced(label='Partner',obj='md.partner',required = True,domain=[('iscustomer',)]),
	'currency': fields.referenced(label='Currency',obj='md.currency',required = True),
	'incoterms1': fields.referenced(label='Incoterms 1',obj='md.incoterms',required = True),
	'incoterms2': fields.varchar(label = 'Incoterms 2',required = True),
	'state': fields.i18n(fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')])),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'items': fields.one2many(label='Items',obj='crm.offer.items',rel='offer_id'),
	'roles': fields.one2many(label='Roles',obj='crm.offer.roles',rel='offer_id'),
	'texts': fields.one2many(label='Texts',obj='crm.offer.texts',rel='offer_id'),
	'note': fields.i18n(fields.text('Note'))
	}

	def _on_change_itype(self ,item,context={}):		
		roles = self.selectFor('crm.offer.type.roles',['role_id'],[('type_id','=',item['otype']['name'])],context)
		for role in roles:
			item_role = self._model('crm.offer.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)
		
		types = self.selectFor('crm.offer.types', ['htschema'],[('name','=',item['otype']['name'])],context)	
		texts1 = self.selectFor('crm.schema.texts', ['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		if len(texts1) > 0:
			texts = texts1[0]['texts']
			seq = 0
			for text in texts:
				item_text = self._model('crm.offer.texts')._buildEmptyItem()
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

#crm_offers()

class crm_offer_texts(Model):
	_name = 'crm.offer.texts'
	_description = 'CRM Offer Texts'
	_class_category = 'crm-offer'
	_request_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'offer_id': fields.many2one(label='Offer',obj='crm.offers',rel='texts'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.referenced(label='Text ID',obj='crm.texts',required=True),
	'descr': fields.link(ref='text_id.descr'),
	'content':fields.i18n(fields.text(label = 'Content'))
	}

#crm_offer_texts()

class crm_offer_roles(Model):
	_name = 'crm.offer.roles'
	_description = 'CRM Offer Roles'
	_class_category = 'crm-offer'
	_columns = {
	'offer_id': fields.many2one(label = 'Offer',obj='crm.offers',rel='roles'),
	'role_id': fields.referenced(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.referenced(label = 'Parther',obj='md.partner',required=True)
	}

#crm_offer_roles()

class crm_offer_items(Model):
	_name = 'crm.offer.items'
	_description = 'CRM Offer Items'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_class_category = 'crm-offer'
	_columns = {
	'offer_id': fields.many2one(obj = 'crm.offers',label = 'Offer',rel='items'),
	'product': fields.referenced(label='Product',obj='md.product',required=True,on_change='_on_change_product'	),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.referenced(label='UoM',obj='md.uom',required=True),
	'price': fields.numeric(label='Price',size=(13,3),required=True),
	'currency': fields.referenced(label='Currency',obj='md.currency',required=True),
	'unit': fields.integer(label='Unit',required=True),
	'uop': fields.referenced(label="Unit Of Price",obj='md.uom',required=True),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.referenced(label='Vat code',obj='md.vat.code',required=True,domain=[('type_vat','in',('s','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'delivery_schedules': fields.one2many(label='Delivery Schedule',obj='crm.offer.item.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='crm.offer.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='crm.offer.item.texts',rel='item_id'),
	'note': fields.i18n(fields.text(label = 'Note'))
	}

	def _on_change_product(self ,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = self.selectFor('md.crm.product',['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
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

#sales_offer_items()

class crm_offer_item_texts(Model):
	_name = 'crm.offer.item.texts'
	_description = 'CRM Offer Item Texts'
	_class_model = 'C'
	_class_category = 'crm-offer'
	_request_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Request',obj='crm.offer.items',rel='texts'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.referenced(label='Text ID',obj='crm.texts',required=True),
	'descr': fields.link(ref='text_id.descr'),
	'content':fields.i18n(fields.text(label = 'Content'))
	}

#crm_offer_item_texts()

class crm_offer_item_roles(Model):
	_name = 'crm.offer.item.roles'
	_description = 'CRM Offer Item Roles'
	_class_category = 'crm-offer'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='crm.offer.items',rel='roles'),
	'role_id': fields.referenced(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.referenced(label = 'Parther',obj='md.partner',required=True)
	}

#crm_offer_item_roles()

class crm_offer_item_delivery_schedules(Model):
	_name = 'crm.offer.item.delivery.schedules'
	_description = 'CRM Offer Item Delivery Schedules'
	_class_category = 'crm-offer'
	_columns = {
	'item_id': fields.many2one(obj = 'crm.offer.items',label = 'Order Item',rel='delivery_schedules'),
	'quantity': fields.numeric(label='Quantity',size=(11,3),required=True),
	'schedule': fields.datetime(label='Schedule',required=True),
	'note': fields.i18n(fields.text(label = 'Note'))
	}

	_default = {
		'quantity': 1.000
	}

#sales_invoce_item_delivery_schedules()
##########
class crm_contracts(Model):
	_name = 'crm.contracts'
	_description = 'Crm Contracts'
	_class_category = 'crm-contract'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_rec_name = 'fullname'
	_date = 'doo'
	_columns = {
	'otype': fields.many2one(label='Type',obj='crm.contract.types',on_change='_on_change_otype'),
	'name': fields.varchar(label = 'Name'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'fullname': fields.composite(label='Full Name', cols = ['company','otype','name'], translate = True,required = True),
	'market': fields.many2one(label='Market',obj='crm.markets'),
	'team': fields.many2one(label='Team',obj='crm.teams'),
	'category_id': fields.many2one(label='Category',obj='crm.contract.categories'),
	'origin': fields.varchar(label = 'Origin'),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'doo': fields.date(label='Date Of Order',required=True),
	'from_date': fields.date(label='Begin Date Of Order',required=True),
	'to_date': fields.date(label='End Date Of Order',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('iscustomer',)]),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'incoterms1': fields.many2one(label='Incoterms 1',obj='md.incoterms'),
	'incoterms2': fields.varchar(label = 'Incoterms 2'),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'mob': fields.many2one(label='BoM',obj='md.boms',domain=[('usage','=','sale'),'|',('usage','=','all')],on_change='_on_change_mob'),
	'items': fields.one2many(label='Items',obj='crm.contract.items',rel='contract_id'),
	'pricing': fields.one2many(label='Pricing',obj='crm.contract.pricing',rel='contract_id'),
	'roles': fields.one2many(label='Roles',obj='crm.contract.roles',rel='contract_id'),
	'texts': fields.one2many(label='Texts',obj='crm.contract.texts',rel='contract_id'),
	'plates': fields.one2many(label='Plates',obj='crm.contract.output.plates',rel='contract_id'),
	'payments': fields.one2many(label='Payments',obj='crm.contract.payment.schedules',rel='contract_id'),
	'note': fields.text('Note')
	}

	def _on_change_otype(self ,item,context={}):		
		roles = self._proxy.get('crm.contract.type.roles').select(['role_id'],[('type_id','=',item['otype']['name'])],context)
		for role in roles:
			item_role = self._proxy.get('crm.contract.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)
		
		types = self._proxy.get('crm.contract.types').select( ['htschema'],[('name','=',item['otype']['name'])],context)	
		texts1 = self._proxy.get('crm.schema.texts').select( ['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		if len(texts1) > 0:
			texts = texts1[0]['texts']
			seq = 0
			for text in texts:
				item_text = self._proxy.get('crm.contract.texts')._buildEmptyItem()
				if text['seq']:
					item_text['seq'] = text['seq']
				else:
					item_text['seq'] = seq
					seq += 10
				item_text['text_id'] = text['text_id']
				item['texts'].append(item_text)

	def _on_change_mob(self ,item,context={}):		
		if item['mob'] and 'name' in item['mob'] and item['mob']['name']:
			p = self._proxy.get('md.mob.output.items').select( ['product','quantity','uom'],[('mob_id','=',item['mob']['name'])],context)
			for i in p:
				ei = self._proxy.get('crm.contract.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.now().astimezone()+timedelta(3)
				item_items = self._proxy.get('crm.contract.items')._buildEmptyItem()
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

class crm_contract_texts(Model):
	_name = 'crm.contract.texts'
	_description = 'Crm Contract Texts'
	_class_model = 'C'
	_class_category = 'crm-contract'
	_contract_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'contract_id': fields.many2one(label='Order',obj='crm.contracts'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='crm.texts'),
	'descr': fields.link(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

class crm_contract_roles(Model):
	_name = 'crm.contract.roles'
	_description = 'Crm Contract Roles'
	_class_category = 'crm-contract'
	_columns = {
	'contract_id': fields.many2one(label = 'Order',obj='crm.contracts'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

class crm_contract_pricing(Model):
	_name = 'crm.contract.pricing'
	_description = 'Crm Contract Pricing'
	_class_category = 'crm-contract'
	_columns = {
	'contract_id': fields.many2one(label = 'Order',obj='crm.contracts'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','s')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='crm.pricing.group.levels'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

class crm_contract_payment_schedules(Model):
	_name = 'crm.contract.payment.schedules'
	_description = 'Crm Contract Payment Schedules'
	_class_category = 'crm-contract'
	_columns = {
	'contract_id': fields.many2one(label = 'Order',obj='crm.contracts'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

class crm_contract_output_plates(Model):
	_name = 'crm.contract.output.plates'
	_description = 'Crm Contract Output Plates'
	_class_category = 'crm-contract'
	_columns = {
	'contract_id': fields.many2one(label = 'Order',obj='crm.contracts'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('iscustomer',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('c','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

class crm_contract_items(Model):
	_name = 'crm.contract.items'
	_description = 'Crm Contract Items'
	_class_category = 'crm-contract'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'contract_id': fields.many2one(obj = 'crm.contracts',label = 'Contract'),
	'itype_id': fields.many2one(label='Group Of Type Items', obj='md.type.items',domain=[('usage','in',('s','a'))]),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,3)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('s','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'volume': fields.float(label='Volume', readonly=True),
	'volume_total': fields.float(label='Volume Total', readonly=True),
	'volume_uom': fields.many2one(label="Volume UoM",obj='md.uom', readonly=True,domain=[('quantity_id','=','Volume')]),
	'weight': fields.float(label='Weight', readonly=True),
	'weight_total': fields.float(label='Weight Total', readonly=True),
	'weight_uom': fields.many2one(label="Weight UoM",obj='md.uom', readonly=True,domain=[('quantity_id','=','Weight')]),
	'delivery_schedules': fields.one2many(label='Delivery Schedule',obj='crm.contract.item.delivery.schedules',rel='item_id'),
	'pricing': fields.one2many(label='Pricing',obj='crm.contract.pricing.items',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='crm.contract.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='crm.contract.item.texts',rel='item_id'),
	'plates': fields.one2many(label='Plates',obj='crm.contract.item.output.plates',rel='item_id'),
	'payments': fields.one2many(label='Payments',obj='crm.contract.item.payment.schedules',rel='item_id'),
	'note': fields.text(label = 'Note')
	}

	def _on_change_product(self ,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			i = self._proxy.get('crm.contract.type.items').select( ['gti_id','itype_id'],[],context)
			gti = {}
			if len(i) > 0:
				for r in i:
					gti[r['gti_id']['name']] = r['itype_id']
			p = self._proxy.get('md.product').select( ['name','gti','volume','volume_uom','weight','weight_uom',{'sale':['vat','uom','price','currency','unit','uop']}],[('name','=',item['product']['name'])],context)
			if len(p) > 0:
				for f in ('gti','volume','volume_uom','weight','weight_uom','sale'):
					if f == 'sale':
						if len(p[0][f]) > 0:
							d = p[0][f][0]
							for m in ('uom','price','currency','unit','uop','vat'):
								if m not in item or item[m] != d[m]:
									if m == 'vat':
										item['vat_code'] = d['vat']				
									else:
										item[m] = d[m]
					else:
						if f == 'gti':
							if p[0]['gti']['name'] in gti:
								item['itype_id'] = gti[p[0][f]['name']]
						else:
							if f not in item or item[f] != p[0][f]:
								item[f] = p[0][f]

			else:
				for f in ('vat_code','uom','price','currency','unit','uop'):
					if f in ('price','unit'):
						if f in self._default:
							item[f] = self._default[f]
						else:
							item[f] = None
					else:
						item[f] = {'id':None,'name':None}

		return None

	_trg_upd_cols = ['product','guantity','amount']

	_trigers = {
		'bir': '_trgForEachRowBeforeInsertIB1',
		'bur': '_trgForEachRowBeforeUpdateUB1',
		'bdr': '_trgForEachRowBeforeDeleteDB1',
		'air': '_trgForEachRowAfterInsertIA1',
		'aur': '_trgForEachRowAfterUpdateUA1',
		'adr': '_trgForEachRowAfterDeleteDA1',
		'bi': '_trgBeforeInsertIBA1',
		'bu': '_trgBeforeUpdateUBA1',
		'bd': '_trgBeforeDeleteDBA1',
		'ai': '_trgBeforeInsertIBA1',
		'au': '_trgAfterUpdateIUA1',
		'ad': '_trgAfterDeleteDA1',
		}

	def _trgForEachRowBeforeInsertIB1(self ,r1,context):
		print('Triger For Each Row Before Insert')

	def _trgForEachRowAfterInsertIA1(self ,r1,context):
		print('Triger For Each Row After Insert')

	def _trgBeforeInsertIBA1(self ,r1,context):
		print('Triger Before Insert')

	def _trgAfterInsertIAA1(self ,r1,context):
		print('Triger After Insert')

#
	def _trgForEachRowBeforeUpdateUB1(self ,r1,r2,context):
		print('Triger For Each Row Before Update')

	def _trgForEachRowAfterUpdateUA1(self ,r1,r2,context):
		print('Triger For Each Row After Update')

	def _trgBeforeUpdateUBA1(self ,r1,r2,context):
		print('Triger Before Update')

	def _trgAfterUpdateIUA1(self ,r1,r2,context):
		print('Triger After Update')
#
	def _trgForEachRowBeforeDeleteDB1(self ,r2,context):
		print('Triger For Each Row Before Delete')

	def _trgForEachRowAfterDeleteDA1(self ,r2,context):
		print('Triger For Each Row After Delete')

	def _trgBeforeDeleteDBA1(self ,r2,context):
		print('Triger Before Delete')

	def _trgAfterDeleteDA1(self ,r2,context):
		print('Triger After Delete')

	_default = {
		'quantity': 1,
		'unit': 1
	}

class crm_contract_pricing_items(Model):
	_name = 'crm.contract.pricing.items'
	_description = 'Crm Contract Item Pricing'
	_class_category = 'crm-contract'
	_columns = {
	'item_id': fields.many2one(label = 'Order',obj='crm.contract.items'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','s')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='crm.pricing.group.levels'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'cop': fields.many2one(label='Currency Of Price',obj='md.currency',required=True),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

class crm_contract_item_texts(Model):
	_name = 'crm.contract.item.texts'
	_description = 'Crm Contract Item Texts'
	_class_model = 'C'
	_class_category = 'crm-contract'
	_contract_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='crm.contract.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='crm.texts'),
	'descr': fields.link(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}


class crm_contract_item_roles(Model):
	_name = 'crm.contract.item.roles'
	_description = 'Crm Contract Roles'
	_class_category = 'crm-contract'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='crm.contract.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

class crm_contract_item_delivery_schedules(Model):
	_name = 'crm.contract.item.delivery.schedules'
	_description = 'Crm Contract Item Delivery Schedules'
	_class_category = 'crm-contract'
	_columns = {
	'item_id': fields.many2one(obj = 'crm.contract.items',label = 'Order Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
	}

class crm_contract_item_output_plates(Model):
	_name = 'crm.contract.item.output.plates'
	_description = 'Crm Contract Item Output Plates'
	_class_category = 'crm-contract'
	_columns = {
	'item_id': fields.many2one(label = 'Order',obj='crm.contract.items'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

class crm_contract_item_payment_schedules(Model):
	_name = 'crm.contract.item.payment.schedules'
	_description = 'Crm Contract Item Payment Schedules'
	_class_category = 'crm-contract'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='crm.contract.items'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

class crm_orders(Model):
	_name = 'crm.orders'
	_description = 'CRM Orders'
	_class_category = 'crm-order'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_rec_name = 'fullname'
	_date = 'doo'
	_columns = {
	'otype': fields.many2one(label='Type',obj='crm.order.types',on_change='_on_change_otype'),
	'name': fields.varchar(label = 'Name'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'fullname': fields.composite(label='Full Name', cols = ['company','otype','name'], translate = True,required = True),
	'market': fields.many2one(label='Market',obj='crm.markets'),
	'team': fields.many2one(label='Team',obj='crm.teams'),
	'category_id': fields.many2one(label='Category',obj='crm.order.categories'),
	'origin': fields.varchar(label = 'Origin'),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'doo': fields.date(label='Date Of Order',required=True),
	'from_date': fields.date(label='Begin Date Of Order',required=True),
	'to_date': fields.date(label='End Date Of Order',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('iscustomer',)]),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'incoterms1': fields.many2one(label='Incoterms 1',obj='md.incoterms'),
	'incoterms2': fields.varchar(label = 'Incoterms 2'),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'mob': fields.many2one(label='BoM',obj='md.boms',domain=[('usage','=','sale'),'|',('usage','=','all')],on_change='_on_change_mob'),
	'items': fields.one2many(label='Items',obj='crm.order.items',rel='order_id'),
	'pricing': fields.one2many(label='Pricing',obj='crm.order.pricing',rel='order_id'),
	'roles': fields.one2many(label='Roles',obj='crm.order.roles',rel='order_id'),
	'texts': fields.one2many(label='Texts',obj='crm.order.texts',rel='order_id'),
	'plates': fields.one2many(label='Plates',obj='crm.order.output.plates',rel='order_id'),
	'payments': fields.one2many(label='Payments',obj='crm.order.payment.schedules',rel='order_id'),
	'note': fields.text('Note')
	}

	def _on_change_otype(self ,item,context={}):		
		roles = self._proxy.get('crm.order.type.roles').select(['role_id'],[('type_id','=',item['otype']['name'])],context)
		for role in roles:
			item_role = self._proxy.get('crm.order.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)
		
		types = self._proxy.get('crm.order.types').select( ['htschema'],[('name','=',item['otype']['name'])],context)	
		texts1 = self._proxy.get('crm.schema.texts').select( ['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		if len(texts1) > 0:
			texts = texts1[0]['texts']
			seq = 0
			for text in texts:
				item_text = self._proxy.get('crm.order.texts')._buildEmptyItem()
				if text['seq']:
					item_text['seq'] = text['seq']
				else:
					item_text['seq'] = seq
					seq += 10
				item_text['text_id'] = text['text_id']
				item['texts'].append(item_text)

	def _on_change_mob(self ,item,context={}):		
		if item['mob'] and 'name' in item['mob'] and item['mob']['name']:
			p = self._proxy.get('md.mob.output.items').select( ['product','quantity','uom'],[('mob_id','=',item['mob']['name'])],context)
			for i in p:
				ei = self._proxy.get('crm.order.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.now().astimezone()+timedelta(3)
				item_items = self._proxy.get('crm.order.items')._buildEmptyItem()
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

class crm_order_texts(Model):
	_name = 'crm.order.texts'
	_description = 'CRM Order Texts'
	_class_model = 'C'
	_class_category = 'crm-order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'order_id': fields.many2one(label='Order',obj='crm.orders'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='crm.texts'),
	'descr': fields.link(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

class crm_order_roles(Model):
	_name = 'crm.order.roles'
	_description = 'CRM Order Roles'
	_class_category = 'crm-order'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='crm.orders'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

class crm_order_pricing(Model):
	_name = 'crm.order.pricing'
	_description = 'CRM Order Pricing'
	_class_category = 'crm-order'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='crm.orders'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','s')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='crm.pricing.group.levels'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

class crm_order_payment_schedules(Model):
	_name = 'crm.order.payment.schedules'
	_description = 'CRM Order Payment Schedules'
	_class_category = 'crm-order'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='crm.orders'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

class crm_order_output_plates(Model):
	_name = 'crm.order.output.plates'
	_description = 'CRM Order Output Plates'
	_class_category = 'crm-order'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='crm.orders'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('iscustomer',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('c','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

class crm_order_items(Model):
	_name = 'crm.order.items'
	_description = 'CRM Order Items'
	_class_category = 'crm-order'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'order_id': fields.many2one(obj = 'crm.orders',label = 'CRMs Order'),
	'itype_id': fields.many2one(label='Group Of Type Items', obj='md.type.items',domain=[('usage','in',('s','a'))]),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,3)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('s','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'volume': fields.float(label='Volume', readonly=True),
	'volume_total': fields.float(label='Volume Total', readonly=True),
	'volume_uom': fields.many2one(label="Volume UoM",obj='md.uom', readonly=True,domain=[('quantity_id','=','Volume')]),
	'weight': fields.float(label='Weight', readonly=True),
	'weight_total': fields.float(label='Weight Total', readonly=True),
	'weight_uom': fields.many2one(label="Weight UoM",obj='md.uom', readonly=True,domain=[('quantity_id','=','Weight')]),
	'delivery_schedules': fields.one2many(label='Delivery Schedule',obj='crm.order.item.delivery.schedules',rel='item_id'),
	'pricing': fields.one2many(label='Pricing',obj='crm.order.pricing.items',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='crm.order.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='crm.order.item.texts',rel='item_id'),
	'plates': fields.one2many(label='Plates',obj='crm.order.item.output.plates',rel='item_id'),
	'payments': fields.one2many(label='Payments',obj='crm.order.item.payment.schedules',rel='item_id'),
	'note': fields.text(label = 'Note')
	}

	def _on_change_product(self ,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			i = self._proxy.get('crm.order.type.items').select( ['gti_id','itype_id'],[],context)
			gti = {}
			if len(i) > 0:
				for r in i:
					gti[r['gti_id']['name']] = r['itype_id']
			p = self._proxy.get('md.product').select( ['name','gti','volume','volume_uom','weight','weight_uom',{'sale':['vat','uom','price','currency','unit','uop']}],[('name','=',item['product']['name'])],context)
			if len(p) > 0:
				for f in ('gti','volume','volume_uom','weight','weight_uom','sale'):
					if f == 'sale':
						if len(p[0][f]) > 0:
							d = p[0][f][0]
							for m in ('uom','price','currency','unit','uop','vat'):
								if m not in item or item[m] != d[m]:
									if m == 'vat':
										item['vat_code'] = d['vat']				
									else:
										item[m] = d[m]
					else:
						if f == 'gti':
							if p[0]['gti']['name'] in gti:
								item['itype_id'] = gti[p[0][f]['name']]
						else:
							if f not in item or item[f] != p[0][f]:
								item[f] = p[0][f]

			else:
				for f in ('vat_code','uom','price','currency','unit','uop'):
					if f in ('price','unit'):
						if f in self._default:
							item[f] = self._default[f]
						else:
							item[f] = None
					else:
						item[f] = {'id':None,'name':None}

		return None

	_trg_upd_cols = ['product','guantity','amount']

	_trigers = {
		'bir': '_trgForEachRowBeforeInsertIB1',
		'bur': '_trgForEachRowBeforeUpdateUB1',
		'bdr': '_trgForEachRowBeforeDeleteDB1',
		'air': '_trgForEachRowAfterInsertIA1',
		'aur': '_trgForEachRowAfterUpdateUA1',
		'adr': '_trgForEachRowAfterDeleteDA1',
		'bi': '_trgBeforeInsertIBA1',
		'bu': '_trgBeforeUpdateUBA1',
		'bd': '_trgBeforeDeleteDBA1',
		'ai': '_trgBeforeInsertIBA1',
		'au': '_trgAfterUpdateIUA1',
		'ad': '_trgAfterDeleteDA1',
		}

	def _trgForEachRowBeforeInsertIB1(self ,r1,context):
		print('Triger For Each Row Before Insert')

	def _trgForEachRowAfterInsertIA1(self ,r1,context):
		print('Triger For Each Row After Insert')

	def _trgBeforeInsertIBA1(self ,r1,context):
		print('Triger Before Insert')

	def _trgAfterInsertIAA1(self ,r1,context):
		print('Triger After Insert')

#
	def _trgForEachRowBeforeUpdateUB1(self ,r1,r2,context):
		print('Triger For Each Row Before Update')

	def _trgForEachRowAfterUpdateUA1(self ,r1,r2,context):
		print('Triger For Each Row After Update')

	def _trgBeforeUpdateUBA1(self ,r1,r2,context):
		print('Triger Before Update')

	def _trgAfterUpdateIUA1(self ,r1,r2,context):
		print('Triger After Update')
#
	def _trgForEachRowBeforeDeleteDB1(self ,r2,context):
		print('Triger For Each Row Before Delete')

	def _trgForEachRowAfterDeleteDA1(self ,r2,context):
		print('Triger For Each Row After Delete')

	def _trgBeforeDeleteDBA1(self ,r2,context):
		print('Triger Before Delete')

	def _trgAfterDeleteDA1(self ,r2,context):
		print('Triger After Delete')

	_default = {
		'quantity': 1,
		'unit': 1
	}

class crm_order_pricing_items(Model):
	_name = 'crm.order.pricing.items'
	_description = 'CRM Order Item Pricing'
	_class_category = 'crm-order'
	_columns = {
	'item_id': fields.many2one(label = 'Order',obj='crm.order.items'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','s')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='crm.pricing.group.levels'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'cop': fields.many2one(label='Currency Of Price',obj='md.currency',required=True),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

class crm_order_item_texts(Model):
	_name = 'crm.order.item.texts'
	_description = 'CRM Order Item Texts'
	_class_model = 'C'
	_class_category = 'crm-order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='crm.order.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='crm.texts'),
	'descr': fields.link(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

class crm_order_item_roles(Model):
	_name = 'crm.order.item.roles'
	_description = 'CRM Order Roles'
	_class_category = 'crm-order'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='crm.order.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

class crm_order_item_delivery_schedules(Model):
	_name = 'crm.order.item.delivery.schedules'
	_description = 'CRMs Order Item Delivery Schedules'
	_class_category = 'crm-order'
	_columns = {
	'item_id': fields.many2one(obj = 'crm.order.items',label = 'Order Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
	}

class crm_order_item_output_plates(Model):
	_name = 'crm.order.item.output.plates'
	_description = 'CRM Order Item Output Plates'
	_class_category = 'crm-order'
	_columns = {
	'item_id': fields.many2one(label = 'Order',obj='crm.order.items'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

class crm_order_item_payment_schedules(Model):
	_name = 'crm.order.item.payment.schedules'
	_description = 'CRM Order Item Payment Schedules'
	_class_category = 'crm-order'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='crm.order.items'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

# Invoice
class crm_invoices(Model):
	_name = 'crm.invoices'
	_description = 'CRM Invoices'
	_class_category = 'crm-invoice'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'doi'
	_columns = {
	'itype': fields.many2one(label='Type',obj='crm.invoice.types',on_change='on_change_itype'),
	'name': fields.varchar(label = 'Name'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'fullname': fields.composite(label='Full Name', cols = ['company','itype','name'], translate = True,required = True),
	'market_id': fields.many2one(label='Market',obj='crm.markets'),
	'team_id': fields.many2one(label='Team',obj='crm.teams'),
	'category_id': fields.many2one(label='Category',obj='crm.invoice.categories'),
	'origin': fields.varchar(label = 'Origin'),
	'doi': fields.date(label='Date Of Invoice',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('iscustomer',)]),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'incoterms1': fields.many2one(label='Incoterms 1',obj='md.incoterms'),
	'incoterms2': fields.varchar(label = 'Incoterms 2'),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'items': fields.one2many(label='Items',obj='crm.invoice.items',rel='invoice_id'),
	'roles': fields.one2many(label='Roles',obj='crm.invoice.roles',rel='invoice_id'),
	'texts': fields.one2many(label='Texts',obj='crm.invoice.texts',rel='invoice_id'),
	'note': fields.text('Note')
	}

	def _on_change_itype(self ,item,context={}):		
			roles = self._proxy.get('crm.invoice.type.roles').select(['role_id'],[('type_id','=',item['otype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]


	_default = {
		'state':'draft'
	}

class crm_invoice_texts(Model):
	_name = 'crm.invoice.texts'
	_description = 'CRM Invoce Texts'
	_class_model = 'C'
	_class_category = 'crm-invoice'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'invoice_id': fields.many2one(label='Order',obj='crm.invoices'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='crm.texts'),
	'descr': fields.link(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

class crm_invoice_roles(Model):
	_name = 'crm.invoice.roles'
	_description = 'sale Invoice Roles'
	_class_category = 'crm-invoice'
	_columns = {
	'invoice_id': fields.many2one(label = 'Invoice',obj='crm.invoices'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

class crm_invoice_items(Model):
	_name = 'crm.invoice.items'
	_description = 'CRMs Invoice Items'
	_class_category = 'crm-invoice'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'invoice_id': fields.many2one(obj = 'crm.invoices',label = 'Invoice'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'	),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,3)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('s','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'delivery_schedules': fields.one2many(label='Delivery Schedule',obj='crm.invoice.item.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='crm.invoice.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='crm.invoice.item.texts',rel='item_id'),
	'note': fields.text(label = 'Note')
	}

	def _on_change_product(self ,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = self._proxy.get('md.sale.product').select(['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
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

class crm_invoice_item_texts(Model):
	_name = 'crm.invoice.item.texts'
	_description = 'CRM Invoce Item Texts'
	_class_model = 'C'
	_class_category = 'crm-invoice'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Order',obj='crm.invoice.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='crm.texts'),
	'descr': fields.link(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

class crm_invoice_item_roles(Model):
	_name = 'crm.invoice.item.roles'
	_description = 'CRM Invoice Item Roles'
	_class_category = 'crm-invoice'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='crm.invoice.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

class crm_invoce_item_delivery_schedules(Model):
	_name = 'crm.invoice.item.delivery.schedules'
	_description = 'CRMs Order Item Delivery Schedules'
	_class_category = 'crm-invoice'
	_columns = {
	'item_id': fields.many2one(obj = 'crm.invoice.items',label = 'Order Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
	}

#inherit

class md_crm_product(Model):
	_name = 'md.crm.product'
	_description = 'CRM Of Product'
	_class_category = 'crm-md-product'
	_columns = {
	'product_id': fields.many2one(label='Product',obj='md.product',rel='crm'),
	'vat': fields.referenced(label='VAT Code',obj='md.vat.code',required=True,domain=[('type_vat','in',('s','n'))]),
	'uom': fields.referenced(label="Unit Of Measure",obj='md.uom',required=True),
	'price': fields.numeric(label='Price',size=(13,2),required=True),
	'currency': fields.referenced(label='Currency',obj='md.currency',required=True),
	'unit': fields.integer(label='Unit',required=True),
	'uop': fields.referenced(label="Unit Of Price",obj='md.uom',required=True),
	'note': fields.i18n(fields.text(label = 'Note'))
	}

#md_crm_product()

class md_crm_product_inherit(ModelInherit):
	_name = 'md.crm.product.inherit'
	_description = 'Genaral Model Inherit For CRM Product'
	_inherit = {'md.product':{'_columns':['crm']},'md.mobs':{'_columns':['usage']},'md.type.items':{'_columns':['usage']},'seq.conditions':{'_columns':['usage']},'seq.access.schemas':{'_columns':['usage']},'seq.access':{'_columns':['usage']}}
	_columns = {
		'crm': fields.one2many(label='CRMs',obj='md.crm.product',rel='product_id'),
		'usage': fields.iProperty(selections=[('crm','CRM')])
	}
	
#md_crm_product_inherit()

