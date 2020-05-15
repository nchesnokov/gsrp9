import qrcode

from psycopg2 import Binary
from io import BytesIO
from gsrp5service.orm import fields
from gsrp5service.orm.model import Model

from passlib.hash import pbkdf2_sha256

import re

from base64 import b64encode

class md_category_country(Model):
	_name = 'md.category.country'
	_description = 'General Model Category Country'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='md.category.country'),
	'childs_id': fields.one2many(obj = 'md.category.country',rel = 'parent_id',label = 'Childs'),
	'note': fields.text(label = 'Note')
	}

md_category_country()

class md_country_group(Model):
	_name = 'md.country.group'
	_description = 'General Model Country Group'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'country_ids': fields.many2many(label='Countries',obj='md.country',rel='md_country_md_country_group_rel',id1='group_pd',id2='country_id')
	}

md_country_group()

class md_country(Model):
	"""
	Страны мира
	"""
	_name = 'md.country'
	_description = 'General Model Country'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'shortname': fields.varchar(label = 'Short Name',size=32),
	'code': fields.varchar(label = 'Code',size=3),
	'alpha2': fields.varchar(label = 'Alpha2',size=2),
	'alpha3': fields.varchar(label = 'Alpha3',size=3),
	'group_ids': fields.many2many(label='Group',obj='md.country.group',rel='md_country_md_country_group_rel',id2='group_pd',id1='country_id'),
	'states': fields.one2many(label='States',obj='md.country.states',rel='country_id')
	}

md_country()

class md_country_states(Model):
	_description = "General Model Country States"
	_name = 'md.country.states'
	_order = 'code'
	_columns = {
	'country_id': fields.many2one(obj='md.country', label='Country', required=True),
	'name': fields.varchar(label='State Name', help='Administrative divisions of a country. E.g. Fed. State, Departement, Canton'),
	'code': fields.varchar(label='State Code', help='The state code.', required=True)
	}

	_sql_constraints = [
		('name_code_uniq', 'unique(country_id, code)', 'The code of the state must be unique by country !')
	]

md_country_states()

class md_category_language(Model):
	_name = 'md.category.language'
	_description = 'General Model Category Language'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='md.category.language'),
	'childs_id': fields.one2many(obj = 'md.category.language',rel = 'parent_id',label = 'Childs'),
	'note': fields.text(label = 'Note')
	}

md_category_language()

class md_language(Model):
	_name = 'md.language'
	_description = 'General Model Language'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'iso631_1': fields.varchar(label = 'Code ISO 639-1',size=2,selectable = True),
	'iso631_2t': fields.varchar(label = 'Code ISO 639-2T',size=3,selectable = True),
	'iso631_2b': fields.varchar(label = 'Code ISO 639-2B',size=3,selectable = True)
	}

md_language()

class md_group_quantity(Model):
	_name = 'md.group.quantity'
	_description = 'General Model Group Quantity'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'numerator': fields.integer(label='Numerator'),
	'denominator': fields.integer(label='Denomerator'),
	'parent_id': fields.many2one(label='Parent',obj='md.group.quantity'),
	'childs_id': fields.one2many(obj = 'md.group.quantity',rel = 'parent_id',label = 'Childs'),
	'note': fields.text(label = 'Note')
	}

md_group_quantity()

class md_quantity_uom(Model):
	_name = 'md.quantity.uom'
	_description = 'General Model Quantity Unit of Measure'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'group_id': fields.many2one(label='Group Quantity',obj='md.group.quantity'),
	'meter': fields.integer(label='Meter',check='meter >= 0'),
	'weight': fields.integer(label='Weight',check='weight >= 0'),
	'tense': fields.integer(label='Tense',check='tense >= 0'),
	'ampere': fields.integer(label='Ampere',check='ampere >= 0'),
	'kelvin': fields.integer(label='Kelvin',check='kelvin >= 0'),
	'mole': fields.integer(label='Mole',check='mole >= 0'),
	'candelle': fields.integer(label = 'Candelle',check='candelle >= 0'),
	'uoms': fields.one2many(label='UoM',obj='md.uom',rel='quantity_id'),
	'note': fields.text(label = 'Note')
	}

	_sql_constraints = [('full_quantity_unique','unique (meter, tense, ampere, kelvin, mole, candelle,group_id)', 'Quantity unique')]
	
	_default = {
	'meter':0,
	'weight':0,
	'tense':0,
	'ampere':0,
	'kelvin':0,
	'mole':0,
	'candelle':0
	}

md_quantity_uom()

class md_uom(Model):
	_name = 'md.uom'
	_description = 'General Model Unit of Measure'
	_columns = {
	'quantity_id': fields.many2one(label='Quantity',obj='md.quantity.uom'),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'shortname': fields.varchar(label = 'Short Name',size=32),
	'code': fields.varchar(label = 'Code',size=3),
	'isocode': fields.varchar(label = 'ISO Code',size=3), 
	'places': fields.integer(label='Decimal places'),
	'numerator': fields.integer(label='Numerator'),
	'denominator': fields.integer(label='Denomerator'),
	'round': fields.integer(label='Rounding off'),
	'extconst': fields.float(label='Extend Constant'),
	'quantity_id': fields.many2one(label='Quantity',obj='md.quantity.uom')
	}

md_uom()

class md_currency(Model):
	_name = 'md.currency'
	_description = 'General Model Currency'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'shortname': fields.varchar(label = 'Short Name',size=32),
	'code': fields.varchar(label = 'Code',size=3),
	'isocode': fields.varchar(label = 'ISO Code',size=3),
	'currency_rate': fields.one2many(label='Currency Rate',obj='md.currency.rate',rel='currency_id'),
	'note': fields.text(label = 'Note')
	}

md_currency()

class md_vat_code(Model):
	_name = 'md.vat.code'
	_description = 'General Model Vat Code'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'subtype_vat': fields.selection(label='Subtype VAT',selections=[('i','Include'),('e','Exclude'),('n','None')]),
	'code': fields.varchar(label = 'Code',size=16),
	'value': fields.integer(label='Percent'),
	'type_vat': fields.selection(label='Type VAT',selections=[('s','Sales'),('p','Purchses'),('n','None')])
	}
	
	_default = {
		'subtype_vat': 'e'
	}

md_vat_code()


class md_excise_code(Model):
	_name = 'md.excise.code'
	_description = 'General Model Excise Code'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'subtype_excise': fields.selection(label='Subtype Excise',selections=[('i','Include'),('e','Exclude'),('n','None')]),
	'code': fields.varchar(label = 'Code',size=16),
	'value': fields.integer(label='Percent'),
	'type_vat': fields.selection(label='Type Excise',selections=[('s','Sales'),('p','Purchses'),('n','None')])
	}
	
	_default = {
		'subtype_vat': 'i'
	}

md_excise_code()


class md_category_product(Model):
	_name = 'md.category.product'
	_description = 'General Model Category Product'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='md.category.product'),
	'childs_id': fields.one2many(obj = 'md.category.product',rel = 'parent_id',label = 'Childs'),
	'note': fields.text(label = 'Note')
	}

md_category_product()

class md_gtis(Model):
	_name = 'md.gtis'
	_description = 'General Model Group Of Type Items'
	_rec_name = 'code'
	_columns = {
	'code': fields.varchar(label = 'Code',size=64,translate=True),
	'descr': fields.text(label = 'Description')
	}

md_gtis()

class md_type_items(Model):
	_name = 'md.type.items'
	_description = 'General Model Type Of Items'
	_rec_name = 'code'
	_columns = {
	'usage': fields.selection(label='Usage',selections=[('a','All')]),
	'code': fields.varchar(label='Code',size=32,translate=True),
	'descr': fields.varchar(label='Description',size=128,translate=True),
	'note': fields.text(label = 'Note')
}

md_type_items()

class md_type_plates(Model):
	_name = 'md.type.plates'
	_description = 'General Model Type Of Plates'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'usage': fields.selection(label='Usage',selections=[('a','All')]),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'note': fields.text(label = 'Note')
	}

md_type_plates()


class md_products_template(Model):
	_name = 'md.products.template'
	_description = 'General Model Product Template'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'category_id': fields.many2one(label='Category',obj='md.category.product'),
	'mtype': fields.selection(label='Type',selections=[('p','Product'),('s','Service'),('w','Work'),('c','Consumable')]),
	'products': fields.one2many(label = 'Products',obj='md.product',rel='template_id'),
	'note': fields.text(label = 'Note')
	}

md_products_template()

class md_product(Model):
	_name = 'md.product'
	_description = 'General Model Product'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'template_id': fields.many2one(label='Template',obj='md.products.template'),
	'code': fields.varchar(label = 'Code',size=16),
	'uom': fields.many2one(label="Unit Of Measure",obj='md.uom'),
	#'isexcise': fields.boolean(label='Is Excise')
	#'excise': fields.many2one(label='Excise',obj='md.excise.code',invisible='_excise_invisible'),
	'gti': fields.many2one(label='Group Of Type Items',obj='md.gtis'),
	'volume': fields.float(label='Volume',invisible='_service_invisible'),
	'volume_uom': fields.many2one(label="Volume UoM",obj='md.uom',invisible='_service_invisible',domain=[('quantity_id','=','Volume')]),
	'weight': fields.float(label='Weight',invisible='_service_invisible'),
	'weight_uom': fields.many2one(label="Weight UoM",obj='md.uom',invisible='_service_invisible',domain=[('quantity_id','=','Weight')]),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closing','Closing'),('closed','Closed'),('canceled','Canceled')]),
	'qrcode': fields.binary(label="QRCode", accept='image/*', help="This field holds the image QRCode",readonly=True),
	'image': fields.binary(label="Photo", accept='image/*', help="This field holds the image used as photo for the employee, limited to 1024x1024px."),
	'image_medium': fields.binary(label="Medium-sized photo", accept='image/*', help="Medium-sized photo of the employee. It is automatically "
			 "resized as a 128x128px image, with aspect ratio preserved. "
			 "Use this field in form views or some kanban views."),
	'image_small': fields.binary(label=	"Small-sized photo", accept='image/*', help="Small-sized photo of the product. It is automatically "
			 "resized as a 64x64px image, with aspect ratio preserved. "
			 "Use this field anywhere a small image is required."),
	'link': fields.varchar(label='Link',size=255),
	'note': fields.text(label = 'Note')
	}

	def _excise_invisible(self,cr,pool,uid,fields,record,context):
		res = {}
		for field in fields:
			res[field] = record['isexcise']

		return res

	def _service_invisible(self,cr,pool,uid,fields,record,context):
		res = {}
		if 'template_id' in record and record['template_id']:
			if record['template_id']['name']:
				r = pool.get('md.products.template').select(cr,pool,uid,['mtype'],[('name','=',record['template_id']['name'])])
				if len(r) > 0 and r[0]['mtype'] == 's':
					return True
					for field in fields:
						res[field] = True
		
		return res

	def create(self,cr,pool,uid,records,context={}):
		if type(records) in (list,tuple):
			for record in records:
				if 'code' in record and 'name' in record:
					b = BytesIO()
					q = qrcode.make("UC: %s - UN: %s" % (record['code'],record['name'])) 
					q.save(b,'jpeg')
					record['qrcode'] = Binary(b'data:image/jpeg;base64,'+b64encode(b.getvalue()))

		elif type(records) == dict:
			if 'code' in records and 'name' in records:
				b = BytesIO()
				q  = qrcode.make("UC: %s - UN: %s" % (records['code'],records['name'])) 
				q.save(b,'jpeg')
				records['qrcode'] = Binary(b'data:image/jpeg;base64,'+b64encode(b.getvalue()))

		return super(Model,self).create(cr, pool, uid, records, context)

	def write(self, cr, pool, uid, records, context = {}):
		if type(records) in (list,tuple):
			for record in records:
				if 'code' in record and 'name' in record:
					b = BytesIO()
					q = qrcode.make("UC: %s - UN: %s" % (record['code'],record['name'])) 
					q.save(b,'jpeg')
					record['qrcode'] = Binary(b'data:image/jpeg;base64,'+b64encode(b.getvalue()))

		elif type(records) == dict:
			if 'code' in records and 'name' in records:
				b = BytesIO()
				q  = qrcode.make("UC: %s - UN: %s" % (records['code'],records['name'])) 
				q.save(b,'jpeg')
				records['qrcode'] = Binary(b'data:image/jpeg;base64,'+b64encode(b.getvalue()))

		return super(Model,self).write(cr, pool, uid, records, context)

	def modify(self, cr, pool, uid, records, context = {}):
		if type(records) in (list,tuple):
			for record in records:
				if 'code' in record and 'name' in record:
					b = BytesIO()
					q = qrcode.make("UC: %s - UN: %s" % (record['code'],record['name'])) 
					q.save(b,'jpeg')
					record['qrcode'] = Binary(b'data:image/jpeg;base64,'+b64encode(b.getvalue()))

		elif type(records) == dict:
			if 'code' in records and 'name' in records:
				b = BytesIO()
				q  = qrcode.make("UC: %s - UN: %s" % (records['code'],records['name'])) 
				q.save(b,'jpeg')
				records['qrcode'] = Binary(b'data:image/jpeg;base64,'+b64encode(b.getvalue()))

		return super(Model,self).modify(cr, pool, uid, records, context)

	def insert(self, cr, pool, uid, fields, values,context = {}):
		fm = {}
		for idx,f in enumerate(fields):
			fm[f] = idx
		for idx,f in enumerate(fields):
			if f == 'qrcode':
				for value in values:
					if 'code' in fm and 'name' in fm:
						b = BytesIO()
						q = qrcode.make("UC: %s - UN: %s" % (value[fm['code']],value[fm['name']])) 
						q.save(b,'jpeg')
						value[idx] = Binary(b'data:image/jpeg;base64,'+b64encode(b.getvalue()))

		return super(Model,self).insert(cr, pool, uid, fields, values,context)

	def upsert(self, cr, pool, uid, fields, values,context = {}):
		fm = {}
		for idx,f in enumerate(fields):
			fm[f] = idx
		for idx,f in enumerate(fields):
			if f == 'qrcode':
				for value in values:
					if 'code' in fm and 'name' in fm:
						b = BytesIO()
						q = qrcode.make("UC: %s - UN: %s" % (value[fm['code']],value[fm['name']])) 
						q.save(b,'jpeg')
						value[idx] = Binary(b'data:image/jpeg;base64,'+b64encode(b.getvalue()))

		return super(Model,self).upsert(cr, pool, uid, fields, values,context)

	_default = {
		'state':'draft'
	}

md_product()

class md_incoterms(Model):
	_name = 'md.incoterms'
	_description = 'General Model Incoterms'
	_columns = {
	'name': fields.varchar(label = 'Name',size=4,translate=True),
	'descr': fields.varchar(label = 'Description',size=64,translate=True),
	'mode': fields.selection(label='Mode Of Transport',selections=[('А','All Mode Of Transport'),('S','Sea & Water Mode oF Transport')],translate=True),
	'grp': fields.selection(label='Group',selections=[('E','Departure'),('F','Main Carriage Unpaid'),('C','Main Carriage Paid'),('D','Arrival')],translate=True),
	'mot': fields.selection(label='Momemt Of Transition',selections=[('se','Seller'),('sc','Customs Of Seller'),('ssh','Seller Shipping'),('ste','Seller Terminal'),('ld','Loading'),('dl','Delivery'),('ul','Unloading'),('bte','Buyer Terminal'),('bsh','Buyer Shipping'),('bc','Customs Of Buyer'),('ba','Buyer')],translate=True),
	'note': fields.text(label = 'Note')
	}

md_incoterms()


class md_category_partner(Model):
	_name = 'md.category.partner'
	_description = 'General Model Category Partner'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='md.category.partner'),
	'childs_id': fields.one2many(obj = 'md.category.partner',rel = 'parent_id',label = 'Childs'),
	'note': fields.text(label = 'Note')
	}

md_category_partner()

class md_category_location(Model):
	_name = 'md.category.location'
	_description = 'General Model Category Location'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='md.category.location'),
	'childs_id': fields.one2many(obj = 'md.category.location',rel = 'parent_id',label = 'Childs'),
	'note': fields.text(label = 'Note')
	}

md_category_location()

class md_location(Model):
	_name = 'md.location'
	_description = 'General Master Data Location'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='md.category.location'),
	'usage': fields.selection(label='Usage',selections=[('partner', 'Partner'),('company', 'Company'),('stock', 'Stock'),('all','All')]),
	'name': fields.varchar(label = 'Name'),
	'latitude': fields.float(label='Latitude'),
	'longitude': fields.float(label='Longitude'),
	'note': fields.text('Note')}

md_location()

class md_partner(Model):
	_name = 'md.partner'
	_description = 'General Model Partner'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='md.category.partner'),
	'country_id': fields.many2one(label='Country',obj='md.country',required=True),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'code': fields.varchar(label = 'Code',size=16),
	'ispeople': fields.boolean(label = 'People'),
	'iscustomer': fields.boolean(label = 'Customer'),
	'issuplier': fields.boolean(label = 'Suplier'),
	'vat_number': fields.varchar(label='VAT Number',selectable=True,size=64),
	'vat_reason': fields.selection(label='VAT Reason',selections=[('y','Yes'),('n','No')]),
	'latitude': fields.float(label='Latitude'),
	'longitude': fields.float(label='Longitude'),
	'products': fields.one2many(label='Products',obj='md.partner.products',rel='partner_id'),
	'addresses': fields.one2many(label='Addresses',obj='md.partner.addresses',rel='partner_id'),
	'contacts': fields.one2many(label='Contacts',obj='md.partner.contacts',rel='partner_id'),
	'roles': fields.one2many(label='Roles',obj='md.partner.roles',rel='partner_id'),
	}

md_partner()

class md_partner_addresses(Model):
	_name = 'md.partner.addresses'
	_description = 'General Model Partner Addresses'
	_columns = {
	'partner_id': fields.many2one(label='Partner',obj='md.partner'),
	'taddr': fields.selection(label='Type Of Address',selections=[('l','Location'),('p','Postal'),('a','Situtation')]),
	'country': fields.many2one(label='Country',obj='md.country'),
	'state': fields.related(label = 'State Of Coutry',obj='md.country.states',relatedy=['country']),
	'sity': fields.varchar(label = 'City',size=64,translate=True),
	'street': fields.varchar(label = 'Street',size=64,translate=True),
	'street2': fields.varchar(label = 'Street 2',size=64,translate=True),
	'house': fields.varchar(label = 'House',size=64,translate=True),
	'room': fields.varchar(label = 'Room',size=64,translate=True)
	}

md_partner_addresses()

class md_partner_contacts(Model):
	_name = 'md.partner.contacts'
	_description = 'General Model Partner Contacts'
	_columns = {
	'partner_id': fields.many2one(label='Partner',obj='md.partner'),
	'usage': fields.selection(label='Usage',selections=[('d','Dear')]),
	'sequence': fields.integer(label='Sequence'),
	'firstname': fields.varchar(label = 'First Name',size=64,translate=True),
	'lastname': fields.varchar(label = 'Last Name',size=64,translate=True),
	'middlename': fields.varchar(label = 'Middle Name',size=64,translate=True),
	'fullname': fields.varchar(label = 'Full Name',compute = ["(CONCAT(firstname,' ',lastname,' ',middlename,':',birthday::STRING))",True]),
	'gender': fields.selection(selections=[('male', 'Male'),('female', 'Female'),('other', 'Other')],label="Gender"),
	'marital': fields.selection(selections=[('single', 'Single'),('married', 'Married'),('widower', 'Widower'),('divorced', 'Divorced')], label='Marital Status'),
	'birthday': fields.date(label='Date of Birth'),
	'image': fields.binary(label="Photo", accept='image/*', help="This field holds the image used as photo for the employee, limited to 1024x1024px."),
	'image_medium': fields.binary(label="Medium-sized photo", accept='image/*', help="Medium-sized photo of the employee. It is automatically "
			 "resized as a 128x128px image, with aspect ratio preserved. "
			 "Use this field in form views or some kanban views."),
	'image_small': fields.binary(label=	"Small-sized photo", accept='image/*', help="Small-sized photo of the employee. It is automatically "
			 "resized as a 64x64px image, with aspect ratio preserved. "
			 "Use this field anywhere a small image is required."),
	# work
	'address_id': fields.many2one(obj='md.partner', label='Work Address'),
	'work_phone':  fields.varchar(label='Work Phone'),
	'mobile_phone': fields.varchar(label='Work Mobile'),
	'work_email': fields.varchar(label='Work Email'),
	'work_location': fields.varchar('Work Location'),
	'note': fields.text(label = 'Note')
	}

md_partner_contacts()


class md_partner_products(Model):
	_name = 'md.partner.products'
	_description = 'General Model Partner Products'
	_columns = {
	'partner_id': fields.many2one(label='Partner',obj='md.partner'),
	'product_id': fields.many2one(label='Product',obj='md.product'),
	'uom': fields.referenced(label='UoM',ref='product_id.uom'),
	'minqty': fields.numeric(label='Min Quantity',size=(11,3),required=True),
	'image': fields.binary(label="Photo", help="This field holds the image used as photo for the employee, limited to 1024x1024px."),
	'image_medium': fields.binary(label="Medium-sized photo", help="Medium-sized photo of the employee. It is automatically "
			 "resized as a 128x128px image, with aspect ratio preserved. "
			 "Use this field in form views or some kanban views."),
	'image_small': fields.binary(label=	"Small-sized photo", help="Small-sized photo of the employee. It is automatically "
			 "resized as a 64x64px image, with aspect ratio preserved. "
			 "Use this field anywhere a small image is required."),
	'link': fields.varchar(label='Link',size=255),
	'prices': fields.one2many(label='Prices',obj='md.pricelist.partner.products',rel='partner_product_id'),
	'note': fields.text(label = 'Note')
}

md_partner_products()

class md_role_partners(Model):
	_name = 'md.role.partners'
	_description = 'General Model Role Partners'
	_columns = {
	'trole': fields.selection(label='Type Of Role',selections=[('c','Customer'),('s','Supplier'),('i','Internal'),('p','Person'),('a','All')]),
	'name': fields.varchar(label='Role',size=32,translate=True),
	'descr': fields.varchar(label='Description',size=128,translate=True),
	'note': fields.text(label = 'Note')
}

md_role_partners()


class md_partner_roles(Model):
	_name = 'md.partner.roles'
	_description = 'General Model Partner Roles'
	_columns = {
	'role_id': fields.many2one(label='Role',obj='md.role.partners'),
	'name': fields.referenced(ref='role_id.descr'),
	'partner_id': fields.many2one(label='Partner',obj='md.partner')
}

md_partner_roles()


class md_pricelist_partner_products(Model):
	_name = 'md.pricelist.partner.products'
	_description = 'General Model Pricelist Partner Products'
	_columns = {
	'partner_product_id': fields.many2one(label='Partner Product',obj='md.partner.products'),
	'valid_from': fields.date(label='Valid From',required=True),
	'valid_to': fields.date(label='Valid to',required=True),
	'currency_id': fields.many2one(label='Currency',obj='md.currency',required=True),
	'qty': fields.integer(label='Qty Price',required=True),
	'price': fields.numeric(label='Price',size=(11,2),required=True),
	'note': fields.text(label = 'Note')
}

	_default = {
		'qty':1
	}
md_pricelist_partner_products()

class md_company(Model):
	_name = 'md.company'
	_description = 'General Model Company'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'country_id': fields.many2one(label='Country',obj='md.country'),
	'currency_id': fields.many2one(label='Currency',obj='md.currency'),
	'currency_rate': fields.one2many(label='Currency Rate',obj='md.currency.rate',rel='company_id'),
	'note': fields.text(label = 'Note')
	}

md_company()

class md_currency_rate(Model):
	_name = 'md.currency.rate'
	_description = 'General Model Currency Rate'
	_columns = {
	'currency_id': fields.many2one(label = 'From Currency',obj='md.currency'),
	'currency_id1': fields.many2one(label = 'To Currency',obj='md.currency'),
	'company_id': fields.many2one(label = 'Company',obj='md.company'),
	'date': fields.date(label = 'Date'),
	'account': fields.integer(label='Accout',check='account > 0'),
	'type': fields.selection(label='Type',selections=[('m','Monthly'),('d','Day'),('w','Week')]),
	'rate': fields.numeric(label = 'Currency Rate',size=(9,5), required = True,check='rate > 0.00000')
	}

	_default = {
		'account':1,
		'rate': 1.00000,
		'type': 'd'
	}

md_currency_rate()

class md_banks(Model):
	_name = 'md.banks'
	_description = 'General Model Bank'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'street': fields.varchar(label='Street'),
	'street2': fields.varchar(label='Street2'),
	'zip': fields.varchar(label='ZIP'),
	'city': fields.varchar(label='City'),
	'country_id': fields.many2one(label='Country',obj='md.country'),
	'state_id': fields.related(label='Fed. State',obj='md.country.states',relatedy=['country_id']),
	'email': fields.varchar(label='Email',pattern='.+@.+\..+'),
	'phone': fields.varchar(label='Phone'),
	'bic': fields.varchar(label='Bank Identifier Code', help="Sometimes called BIC or Swift."),
	'partners': fields.one2many(label='Partners',obj='md.partners.bank',rel='bank_id'),
	'inactive': fields.boolean(label='Inactive'),
	'note': fields.text(label = 'Note')
	}

	_indicies = {
		'bic':['bic']
	}

md_banks()

class md_partners_bank(Model):
	_name = 'md.partners.bank'
	_description = 'General Model Bank of Partner'
	_columns = {
	'acc_type': fields.varchar(label = 'ACC Type',compute='_compute_acc_type', help='Bank account type, inferred from account number'),
	'acc_number': fields.varchar(label='Account Number', required=True),
	'sanitized_acc_number': fields.varchar(compute='_compute_sanitized_acc_number', label='Sanitized Account Number', readonly=True),
	'partner_id': fields.many2one(obj='md.partner', label='Account Holder', on_delete='c', domain=[ ('issuplier', )]),
	'bank_id': fields.many2one(obj='md.banks', label='Bank'),
	'bank_name': fields.referenced(label='Bank Name',ref='bank_id.name'),
	'bank_bic': fields.referenced(ref='bank_id.bic'),
	'sequence': fields.integer(label='Sequence'),
	'currency_id': fields.many2one(obj='md.currency', label='Currency'),
	'company_id': fields.many2one(obj='md.company', label='Company',  on_delete='c'),
	'note': fields.text(label = 'Note')
	}

	def _compute_acc_type(self,cr,pool,uid,record,context = {}):
		return {'acc_type':'bank'}


	def _compute_sanitized_acc_number(self,cr,pool,uid,record,context = {}):
		if 'acc_number' in record:
			return {'sanitized_acc_number':re.sub(r'\W+', '', record['acc_number']).upper()}
		return  {'sanitized_acc_number':''}

	_sql_constraints = [
		('unique_number', 'unique(sanitized_acc_number, company_id)', 'Account Number must be unique'),
	]

md_partners_bank()

class md_recepture(Model):
	_name = 'md.recepture'
	_description = 'General Model Recipe'
	_columns = {
	'name': fields.varchar(label="Name"),
	'type': fields.selection(label='Type',selections=[('real','Real'),('kvazi','Kwazi')]),
	'subtype': fields.selection(label='Subtype',selections=[('bom','BoM'),('mob','MoB'),('bob',"BoB")]),
	'usage': fields.selection(label='Usage',selections=[('a','All')]),
	'partition': fields.integer(label='Partition',required=True,check='partition > 0'),
	'input_items': fields.one2many(label='Input',obj='md.recepture.input',rel='recepture_id'),
	'output_items': fields.one2many(label='Output',obj='md.recepture.output',rel='recepture_id'),
	}

md_recepture()

class md_recepture_input(Model):
	_name = 'md.recepture.input'
	_description = 'General Model Input Recipe'
	_columns = {
	'recepture_id': fields.many2one(label="Recepture",obj='md.recepture'),
	'product': fields.many2one(label='Product',obj='md.product'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1
	}

md_recepture_input()

class md_recepture_output(Model):
	_name = 'md.recepture.output'
	_description = 'General Model Output Recipe'
	_columns = {
	'recepture_id': fields.many2one(label="Recepture",obj='md.recepture'),
	'product': fields.many2one(label='Product',obj='md.product'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1
	}


md_recepture_output()
