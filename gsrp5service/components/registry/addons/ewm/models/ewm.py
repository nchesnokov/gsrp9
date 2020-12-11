from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

class st_company_product_quantites(Model):
	_name = 'st.company.product.quantites'
	_description = 'Company Product Quantity'
	_rec_name = None
	_columns = {
	'company_id':  fields.many2one(label='Company',obj='st.stock', readonly=True),
	'stoсk_type': fields.selection(label='Stock type',selections=[('vs','Valuated Stock'),('us','Unvalued Stock'),('vbs','Valuated Blocked Stock'),('ubs','Unvalued Blocked Stock')], readonly=True),
	'product': fields.many2one(label='Product',obj='md.product', readonly=True),
	'quantity': fields.numeric('Quantity',size=(11,3), readonly=True),
	'uom': fields.many2one(label='Unit of Measure',obj='md.uom', readonly=True),
	'amount': fields.numeric('Amount',size=(15,2), readonly=True),
	'currency': fields.many2one(label='Currency',obj='md.currency', readonly=True)
	}

st_company_product_quantites()


class st_stock_product_quantites(Model):
	_name = 'st.stock.product.quantites'
	_description = 'Stock Product Quantity'
	_rec_name = None
	_columns = {
	'stock_id':  fields.many2one(label='Stock',obj='st.stock', readonly=True),
	'stoсk_type': fields.selection(label='Stock type',selections=[('vs','Valuated Stock'),('us','Unvalued Stock'),('vbs','Valuated Blocked Stock'),('ubs','Unvalued Blocked Stock')], readonly=True),
	'product': fields.many2one(label='Product',obj='md.product', readonly=True),
	'quantity': fields.numeric('Quantity',size=(11,3), readonly=True),
	'uom': fields.many2one(label='Unit of Measure',obj='md.uom', readonly=True),
	'amount': fields.numeric('Amount',size=(15,2), readonly=True),
	'currency': fields.many2one(label='Currency',obj='md.currency', readonly=True)
	}

st_stock_product_quantites()

class md_ewm_product(Model):
	_name = 'md.ewm.product'
	_description = 'Stock Of Product'
	_columns = {
	'product_id': fields.many2one(label='Product',obj='md.product'),
	'uom': fields.many2one(label="Unit Of Measure",obj='md.uom'),
	'note': fields.text(label = 'Note'),
	}

md_ewm_product()

# class st_stock_documents(Model):
	# _name = 'st.stock.documents'
	# _description = 'Stock Documents'
	# _inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	# _date = "dsd"
	# _rec_name = 'fullname'
	# _columns = {
	# 'company': fields.many2one(label='Company',obj='md.company', required = True),
	# 'year':fields.varchar(label = 'Year', required = True),
	# 'code':fields.varchar(label = 'Year', required = True),
	# 'fullname': fields.composite(label='Full Name', cols = ['company','year','code'], translate = True,required = True, compute = '_compute_composite'),
	# 'category_id': fields.many2one(label='Category',obj='st.stock.document.categories'),
	# 'manager': fields.many2one(label='Manager',obj='bc.users'),
	# 'origin': fields.varchar(label = 'Origin'),
	# 'dsd': fields.date(label='Date Of Stock Document',required=True),
	# 'dsa': fields.date(label='Date Of Stock Document Applyed',required=True),
	# 'currency': fields.many2one(label='Currency',obj='md.currency',state={'approved':{'ro':True}}),
	# 'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	# 'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	# 'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	# 'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	# 'bom': fields.many2one(label='BoM',obj='md.boms',domain=[('usage','=','pur'),'|',('usage','=','all')],on_change='_on_change_bom'),
	# 'items': fields.one2many(label='Items',obj='st.stock.document.items',rel='document_id'),
	# 'pricing': fields.one2many(label='Pricing',obj='st.stock.document.pricing',rel='document_id'),
	# 'roles': fields.one2many(label='Roles',obj='st.stock.document.roles',rel='document_id'),
	# 'texts': fields.one2many(label='Texts',obj='st.stock.document..texts',rel='document_id'),
	# 'note': fields.text('Note')
	# }

# class purchase_order_items(Model):
	# _name = 'st.stok.document.items'
	# _description = 'Stock Document Items'
	# _columns = {
	# 'document_id': fields.many2one(obj = 'st.stock.documents',label = 'Stock Document'),
	# 'product': fields.many2one(label='Product',obj='md.product'),
	# 'quantity': fields.numeric(label='Quantity',size=(13,3)),
	# 'uom': fields.many2one(label='UoM',obj='md.uom'),
	# 'price': fields.numeric(label='Price',size=(13,2)),
	# 'currency': fields.many2one(label='Currency',obj='md.currency'),
	# 'unit': fields.integer(label='Unit'),
	# 'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	# 'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	# 'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('p','n'))]),
	# 'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	# 'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	# 'volume': fields.float(label='Volume', readonly=True),
	# 'volume_total': fields.float(label='Volume Total', readonly=True),
	# 'volume_uom': fields.many2one(label="Volume UoM",obj='md.uom', readonly=True,domain=[('quantity_id','=','Volume')]),
	# 'weight': fields.float(label='Weight', readonly=True),
	# 'weight_total': fields.float(label='Weight Total', readonly=True),
	# 'weight_uom': fields.many2one(label="Weight UoM",obj='md.uom', readonly=True,domain=[('quantity_id','=','Weight')]),
	# 'roles': fields.one2many(label='Roles',obj='st.stock.documentitem.roles',rel='item_id'),
	# 'texts': fields.one2many(label='Texts',obj='st.stock.document.item.texts',rel='item_id'),
	# 'note': fields.text(label = 'Note')}


class md_ewm_product_inherit(ModelInherit):
	_name = 'md.ewm.product.inherit'
	_description = 'Inherit For Stock Product'
	_inherit = {'md.product':{'_columns':['ewms']}}
	_columns = {
		'ewms': fields.one2many(label='Ewms',obj='md.wm.product',rel='product_id')
	}
	
md_ewm_product_inherit()

#
class md_stock_company_inherit(ModelInherit):
	_name = 'md.stock.company.inherit'
	_description = 'Inherit For Stock Company'
	_inherit = {'md.company':{'_columns':['stocks']}}
	_columns = {
		'stocks': fields.one2many(label='Stock',obj='st.stock',rel='company')
	}
	
md_stock_company_inherit()
#
