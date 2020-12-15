from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

from decimal import Decimal

from datetime import datetime
from datetime import timedelta

# Organization structure
class md_category_country(Model):
	_name = 'md.category.country'
	_description = 'Category Country'
	_class_model = 'C'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='md.category.country'),
	'childs_id': fields.one2many(obj = 'md.category.country',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'note': fields.text(label = 'Note')
	}

md_category_country()

class md_category_language(Model):
	_name = 'md.category.language'
	_description = 'Category Language'
	_class_model = 'C'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='md.category.language'),
	'childs_id': fields.one2many(obj = 'md.category.language',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'note': fields.text(label = 'Note')
	}

md_category_language()

class md_category_product(Model):
	_name = 'md.category.product'
	_description = 'Category Product'
	_class_model = 'C'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='md.category.product'),
	'childs_id': fields.one2many(obj = 'md.category.product',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'note': fields.text(label = 'Note')
	}

md_category_product()

class md_gtis(Model):
	_name = 'md.gtis'
	_description = 'Group Of Type Items'
	_class_model = 'C'
	_rec_name = 'code'
	_columns = {
	'code': fields.varchar(label = 'Code',size=64,translate=True),
	'descr': fields.text(label = 'Description')
	}

md_gtis()

class md_type_items(Model):
	_name = 'md.type.items'
	_description = 'Type Of Items'
	_rec_name = 'code'
	_class_model = 'C'
	_columns = {
	'usage': fields.selection(label='Usage',selections=[('a','All')]),
	'code': fields.varchar(label='Code',size=32,translate=True),
	'descr': fields.varchar(label='Description',size=128,translate=True),
	'note': fields.text(label = 'Note')
}

md_type_items()

class md_type_plates(Model):
	_name = 'md.type.plates'
	_description = 'Type Of Plates'
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
	_description = 'Product Template'
	_class_model = 'C'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'category_id': fields.many2one(label='Category',obj='md.category.product'),
	'mtype': fields.selection(label='Type',selections=[('p','Product'),('s','Service'),('w','Work'),('c','Consumable')]),
	'products': fields.one2many(label = 'Products',obj='md.product',rel='template_id'),
	'note': fields.text(label = 'Note')
	}

md_products_template()

class md_category_partner(Model):
	_name = 'md.category.partner'
	_description = 'Category Partner'
	_class_model = 'C'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='md.category.partner'),
	'childs_id': fields.one2many(obj = 'md.category.partner',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'note': fields.text(label = 'Note')
	}

md_category_partner()

class md_category_location(Model):
	_name = 'md.category.location'
	_description = 'Category Location'
	_class_model = 'C'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='md.category.location'),
	'childs_id': fields.one2many(obj = 'md.category.location',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'note': fields.text(label = 'Note')
	}

md_category_location()

class md_location(Model):
	_name = 'md.location'
	_description = 'Location'
	_class_model = 'C'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='md.category.location'),
	'usage': fields.selection(label='Usage',selections=[('partner', 'Partner'),('company', 'Company'),('stock', 'Stock'),('all','All')]),
	'name': fields.varchar(label = 'Name'),
	'latitude': fields.float(label='Latitude'),
	'longitude': fields.float(label='Longitude'),
	'note': fields.text('Note')}

md_location()

class md_role_partners(Model):
	_name = 'md.role.partners'
	_description = 'Role Partners'
	_class_model = 'C'
	_columns = {
	'trole': fields.selection(label='Type Of Role',selections=[('c','Customer'),('s','Supplier'),('i','Internal'),('p','Person'),('a','All')]),
	'name': fields.varchar(label='Role',size=32,translate=True),
	'descr': fields.varchar(label='Description',size=128,translate=True),
	'note': fields.text(label = 'Note')
}

md_role_partners()

class md_group_quantity(Model):
	_name = 'md.group.quantity'
	_description = 'Group Quantity'
	_class_model = 'C'
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
	_description = 'Quantity Unit of Measure'
	_class_model = 'C'
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
	_description = 'Unit of Measure'
	_class_model = 'C'
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

class md_vat_code(Model):
	_name = 'md.vat.code'
	_description = 'Vat Code'
	_class_model = 'C'
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
	_description = 'Excise Code'
	_class_model = 'C'
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

class md_currency(Model):
	_name = 'md.currency'
	_description = 'Currency'
	_class_model = 'C'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'shortname': fields.varchar(label = 'Short Name',size=32),
	'code': fields.varchar(label = 'Code',size=3),
	'isocode': fields.varchar(label = 'ISO Code',size=3),
	'currency_rate': fields.one2many(label='Currency Rate',obj='md.currency.rate',rel='currency_id'),
	'note': fields.text(label = 'Note')
	}

md_currency()

class md_key_currencies(Model):
	_name = 'md.key.currencies'
	_description = 'Currencies Key'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'note': fields.text(label = 'Note')
	}

md_key_currencies()

class md_incoterms(Model):
	_name = 'md.incoterms'
	_description = 'Incoterms'
	_class_model = 'C'
	_columns = {
	'name': fields.varchar(label = 'Name',size=4,translate=True),
	'descr': fields.varchar(label = 'Description',size=64,translate=True),
	'mode': fields.selection(label='Mode Of Transport',selections=[('А','All Mode Of Transport'),('S','Sea & Water Mode oF Transport')],translate=True),
	'grp': fields.selection(label='Group',selections=[('E','Departure'),('F','Main Carriage Unpaid'),('C','Main Carriage Paid'),('D','Arrival')],translate=True),
	'mot': fields.selection(label='Momemt Of Transition',selections=[('se','Seller'),('sc','Customs Of Seller'),('ssh','Seller Shipping'),('ste','Seller Terminal'),('ld','Loading'),('dl','Delivery'),('ul','Unloading'),('bte','Buyer Terminal'),('bsh','Buyer Shipping'),('bc','Customs Of Buyer'),('ba','Buyer')],translate=True),
	'note': fields.text(label = 'Note')
	}

md_incoterms()

class md_company(Model):
	_name = 'md.company'
	_description = 'Company'
	_class_model = 'C'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'country_id': fields.many2one(label='Country',obj='md.country'),
	'currency_id': fields.many2one(label='Currency',obj='md.currency'),
	'currency_rate': fields.one2many(label='Currency Rate',obj='md.currency.rate',rel='company_id'),
	'note': fields.text(label = 'Note')
	}

md_company()

