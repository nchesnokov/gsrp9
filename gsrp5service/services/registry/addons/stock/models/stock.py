from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

class st_location(Model):
	_name = 'st.location'
	_description = 'General Stock Location'
	_columns = {
	'usage': fields.selection(label='Usage',selections=[('supplier', 'Vendor Location'),
        ('view', 'View'),
        ('internal', 'Internal Location'),
        ('customer', 'Customer Location'),
        ('inventory', 'Inventory Loss'),
        ('procurement', 'Procurement'),
        ('production', 'Production'),
        ('transit', 'Transit Location')]),
	'name': fields.varchar(label = 'Name'),
	'location_id': fields.many2one(label='Location',obj='md.location',domain=[('usage','in',('stock','all'))]),
	'parent_id': fields.many2one(label = 'Parent',obj='st.location'),
	'childs_id': fields.one2many(label='Childs',obj='st.location',rel='parent_id'),
	'note': fields.text('Note')}

st_location()

class st_stock(Model):
	_name = 'st.stock'
	_description = 'General Stock'
	_columns = {
	'company_id': fields.many2one(label='Company',obj='md.company'),
	'name': fields.varchar(label = 'Name'),
	'location': fields.many2one(label='Location',obj='st.location'),
	'products': fields.one2many(label='Products',readonly=True,obj='st.products',rel='stock_id',limit=80),
	'note': fields.text(label = 'Note')}

st_stock()

class st_product(Model):
	_name = 'st.products'
	_description = 'General Product'
	_rec_name = None
	_columns = {
	'stock_id':  fields.many2one(label='Stock',obj='st.stock'),
	'product': fields.many2one(label='Product',obj='md.product'),
	'quantity': fields.numeric('Quantity',size=(15,3)),
	'uom': fields.many2one(label='Unit of Measure',obj='md.uom')}

st_product()

class md_stock_product(Model):
	_name = 'md.stock.product'
	_description = 'General Model Stock Of Product'
	_columns = {
	'product_id': fields.many2one(label='Product',obj='md.product'),
	'uom': fields.many2one(label="Unit Of Measure",obj='md.uom'),
	'note': fields.text(label = 'Note'),
	}

md_stock_product()

class md_stock_product_inherit(ModelInherit):
	_name = 'md.stock.product.inherit'
	_description = 'Genaral Model Inherit For Stock Product'
	_inherit = {'md.product':{'_columns':['stocks']}}
	_columns = {
		'stocks': fields.one2many(label='Stocks',obj='md.stock.product',rel='product_id')
	}
	
md_stock_product_inherit()

#
class md_stock_company_inherit(ModelInherit):
	_name = 'md.stock.company.inherit'
	_description = 'Genaral Model Inherit For Stock Company'
	_inherit = {'md.company':{'_columns':['stocks']}}
	_columns = {
		'stocks': fields.one2many(label='Stock',obj='st.stock',rel='company_id')
	}
	
md_stock_company_inherit()
#
