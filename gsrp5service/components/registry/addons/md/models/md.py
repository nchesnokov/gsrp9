import qrcode

from psycopg2 import Binary
from io import BytesIO
from gsrp5service.orm import fields
from gsrp5service.orm.model import Model

from passlib.hash import pbkdf2_sha256

import re

from base64 import b64encode

class md_product(Model):
	_name = 'md.product'
	_description = 'Product'
	_class_model = 'B'
	_columns = {
	'name': fields.i18n(fields.varchar(label = 'Name',size=64)),
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
	'note': fields.i18n(fields.text(label = 'Note'))
	}

	def _excise_invisible(self, fields,record,context):
		res = {}
		for field in fields:
			res[field] = record['isexcise']

		return res

	def _service_invisible(self, fields,record,context):
		res = {}
		if 'template_id' in record and record['template_id']:
			if type(record['template_id']) == dict and record['template_id']['name']:
				r = self._pool.get('md.products.template').select(['mtype'],[('name','=',record['template_id']['name'])],context)
			elif type(record['template_id']) == str :
				r = self._pool.get('md.products.template').read(record['template_id'],['mtype'],context)

			if len(r) > 0 and r[0]['mtype'] == 's':
				for field in fields:
					res[field] = True
		
		return res

	def create(self, records,context={}):
		if type(records) in (list,tuple):
			for record in records:
				if 'code' in record and 'name' in record:
					b = BytesIO()
					q = qrcode.make("UC: %s - UN: %s" % (record['code'],record['name'])) 
					q.save(b,'jpeg')
					record['qrcode'] = Binary(b64encode(b.getvalue()))

		elif type(records) == dict:
			if 'code' in records and 'name' in records:
				b = BytesIO()
				q  = qrcode.make("UC: %s - UN: %s" % (records['code'],records['name'])) 
				q.save(b,'jpeg')
				records['qrcode'] = Binary(b64encode(b.getvalue()))

		return super(Model,self).create(  records, context)

	def write(self,   records, context = {}):
		if type(records) in (list,tuple):
			for record in records:
				if 'code' in record and 'name' in record:
					b = BytesIO()
					q = qrcode.make("UC: %s - UN: %s" % (record['code'],record['name'])) 
					q.save(b,'jpeg')
					record['qrcode'] = Binary(b64encode(b.getvalue()))

		elif type(records) == dict:
			if 'code' in records and 'name' in records:
				b = BytesIO()
				q  = qrcode.make("UC: %s - UN: %s" % (records['code'],records['name'])) 
				q.save(b,'jpeg')
				records['qrcode'] = Binary( b64encode(b.getvalue()))

		return super(Model,self).write(  records, context)

	def modify(self,   records, context = {}):
		if type(records) in (list,tuple):
			for record in records:
				if 'code' in record and 'name' in record:
					b = BytesIO()
					q = qrcode.make("UC: %s - UN: %s" % (record['code'],record['name'])) 
					q.save(b,'jpeg')
					record['qrcode'] = Binary(b64encode(b.getvalue()))

		elif type(records) == dict:
			if 'code' in records and 'name' in records:
				b = BytesIO()
				q  = qrcode.make("UC: %s - UN: %s" % (records['code'],records['name'])) 
				q.save(b,'jpeg')
				records['qrcode'] = Binary(b64encode(b.getvalue()))

		return super(Model,self).modify(  records, context)

	def insert(self,   fields, values,context = {}):
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
						value[idx] = Binary(b64encode(b.getvalue()))

		return super(Model,self).insert(  fields, values,context)

	def upsert(self,   fields, values,context = {}):
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
						value[idx] = Binary(b64encode(b.getvalue()))

		return super(Model,self).upsert(  fields, values,context)

	_default = {
		'state':'draft'
	}

md_product()

class md_partner(Model):
	_name = 'md.partner'
	_description = 'Partner'
	_class_model = 'B'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='md.category.partner'),
	'country_id': fields.many2one(label='Country',obj='md.country',required=True),
	'name': fields.i18n(fields.varchar(label = 'Name',size=64)),
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
	_description = 'Partner Addresses'
	_class_model = 'B'
	_columns = {
	'partner_id': fields.many2one(label='Partner',obj='md.partner'),
	'taddr': fields.selection(label='Type Of Address',selections=[('l','Location'),('p','Postal'),('a','Situtation')]),
	'country': fields.many2one(label='Country',obj='md.country'),
	'state': fields.related(label = 'State Of Coutry',obj='md.country.states',relatedy=[('country','country_id')]),
	'sity': fields.related(label = 'Sity',obj='md.country.state.sities',relatedy=[('state','state_id')]),
	'street': fields.i18n(fields.varchar(label = 'Street',size=64)),
	'street2': fields.i18n(fields.varchar(label = 'Street 2',size=64)),
	'house': fields.i18n(fields.varchar(label = 'House',size=64)),
	'room': fields.i18n(fields.varchar(label = 'Room',size=64))
	}

md_partner_addresses()

class md_partner_contacts(Model):
	_name = 'md.partner.contacts'
	_description = 'Partner Contacts'
	_class_model = 'B'
	_columns = {
	'partner_id': fields.many2one(label='Partner',obj='md.partner'),
	'usage': fields.selection(label='Usage',selections=[('d','Dear')]),
	'sequence': fields.integer(label='Sequence'),
	'firstname': fields.i18n(fields.varchar(label = 'First Name',size=64)),
	'lastname': fields.i18n(fields.varchar(label = 'Last Name',size=64)),
	'middlename': fields.i18n(fields.varchar(label = 'Middle Name',size=64)),
	'fullname': fields.i18n(fields.composite(label='Full Name', cols = ['firstname','lastname','middlename','birthday'], translate = True,required = True, compute = '_compute_composite')),
	#'fullname': fields.varchar(label = 'Full Name',compute = ["(CONCAT(firstname,' ',lastname,' ',middlename,':',birthday::STRING))",True]),
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
	_description = 'Partner Products'
	_class_model = 'B'
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

class md_partner_roles(Model):
	_name = 'md.partner.roles'
	_description = 'Partner Roles'
	_class_model = 'B'
	_columns = {
	'role_id': fields.many2one(label='Role',obj='md.role.partners'),
	'name': fields.referenced(ref='role_id.descr'),
	'partner_id': fields.many2one(label='Partner',obj='md.partner')
}

md_partner_roles()

class md_pricelist_partner_products(Model):
	_name = 'md.pricelist.partner.products'
	_description = 'Pricelist Partner Products'
	_class_model = 'B'
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

class md_currency_rate(Model):
	_name = 'md.currency.rate'
	_description = 'Currency Rate'
	_class_model = 'B'
	_columns = {
	'currency_id': fields.many2one(label = 'From Currency',obj='md.currency'),
	'currency_id1': fields.many2one(label = 'To Currency',obj='md.currency'),
	'company_id': fields.many2one(label = 'Company',obj='md.company'),
	'key_id': fields.many2one(label = 'Key',obj='md.key.currencies'),
	'date': fields.date(label = 'Date'),
	'account': fields.integer(label='Account',check='account > 0'),
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
	_description = 'Bank'
	_class_model = 'B'
	_columns = {
	'name': fields.i18n(fields.varchar(label = 'Name',size=64)),
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
	'note': fields.i18n(fields.text(label = 'Note'))
	}

	_indicies = {
		'bic':['bic']
	}

md_banks()

class md_partners_bank(Model):
	_name = 'md.partners.bank'
	_description = 'Bank of Partner'
	_class_model = 'B'
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

	def _compute_acc_type(self, record,context = {}):
		return {'acc_type':'bank'}


	def _compute_sanitized_acc_number(self, record,context = {}):
		if 'acc_number' in record and record['acc_number']:
			return {'sanitized_acc_number':re.sub(r'\W+', '', record['acc_number']).upper()}
		return  {'sanitized_acc_number':''}

	_sql_constraints = [
		('unique_number', 'unique(sanitized_acc_number, company_id)', 'Account Number must be unique'),
	]

md_partners_bank()

# bom
class md_boms(Model):
	_name = 'md.boms'
	_description = 'Bill of Material'
	_class_model = 'B'
	_columns = {
	'name': fields.varchar(label="Name"),
	'company': fields.many2one(label='Company', obj='md.company'),
	'fullname': fields.i18n(fields.composite(label='Full Name', cols = ['company','name'], required = True, compute = '_compute_composite')),
	'type': fields.selection(label='Type',selections=[('real','Real'),('kvazi','Kwazi')]),
	'usage': fields.selection(label='Usage',selections=[('all','All')]),
	'product': fields.many2one(label='Product',obj='md.product'),
	'partition': fields.integer(label='Partition',required=True,check='partition > 0'),
	'items': fields.one2many(label='Input',obj='md.bom.items',rel='bom_id')
	}

md_boms()

class md_bom_items(Model):
	_name = 'md.bom.items'
	_description = 'BoM items'
	_class_model = 'B'
	_columns = {
	'bom_id': fields.many2one(label="BoM",obj='md.boms'),
	'product': fields.many2one(label='Product',obj='md.product'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1
	}

md_bom_items()

class md_mobs(Model):
	_name = 'md.mobs'
	_description = 'Material of Bills'
	_class_model = 'B'
	_columns = {
	'name': fields.varchar(label="Name"),
	'company': fields.many2one(label='Company', obj='md.company'),
	'fullname': fields.i18n(fields.composite(label='Full Name', cols = ['company','name'], required = True, compute = '_compute_composite')),
	'type': fields.selection(label='Type',selections=[('real','Real'),('kvazi','Kwazi')]),
	'usage': fields.selection(label='Usage',selections=[('all','All')]),
	'product': fields.many2one(label='Product',obj='md.product'),
	'partition': fields.integer(label='Partition',required=True,check='partition > 0'),
	'items': fields.one2many(label='Input',obj='md.mob.items',rel='mob_id')
	}

md_mobs()

class md_mob_items(Model):
	_name = 'md.mob.items'
	_description = 'MoB items'
	_class_model = 'B'
	_columns = {
	'mob_id': fields.many2one(label="MoB",obj='md.mobs'),
	'product': fields.many2one(label='Product',obj='md.product'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1
	}

md_mob_items()

class md_bobs(Model):
	_name = 'md.bobs'
	_description = 'Bill of Bills'
	_class_model = 'B'
	_columns = {
	'name': fields.varchar(label="Name"),
	'company': fields.many2one(label='Company', obj='md.company'),
	'fullname': fields.i18n(fields.composite(label='Full Name', cols = ['company','name'], required = True, compute = '_compute_composite')),
	'type': fields.selection(label='Type',selections=[('real','Real'),('kvazi','Kwazi')]),
	'usage': fields.selection(label='Usage',selections=[('all','All')]),
	'partition': fields.integer(label='Partition',required=True,check='partition > 0'),
	'input_items': fields.one2many(label='Input',obj='md.bob.input.items',rel='bob_id'),
	'output_items': fields.one2many(label='output',obj='md.bob.output.items',rel='bob_id')
	}

md_bobs()

class md_bob_input_items(Model):
	_name = 'md.bob.input.items'
	_description = 'BoB Input items'
	_class_model = 'B'
	_columns = {
	'bob_id': fields.many2one(label="BoM",obj='md.bobs'),
	'product': fields.many2one(label='Product',obj='md.product'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1
	}

md_bob_input_items()

class md_bob_output_items(Model):
	_name = 'md.bob.output.items'
	_description = 'BoB Output items'
	_class_model = 'B'
	_columns = {
	'bob_id': fields.many2one(label="BoM",obj='md.bobs'),
	'product': fields.many2one(label='Product',obj='md.product'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1
	}

md_bob_output_items()

# 
