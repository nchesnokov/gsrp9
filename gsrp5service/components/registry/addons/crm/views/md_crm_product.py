from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindMdCrmProduct(ViewModelFind):
	_name = "model.find.md.crm.product"
	_model = "md.crm.product"
	_description = "CRM Of Product"
	_columns = ['product_id', 'vat', 'uom', 'price', 'currency', 'unit', 'uop', 'note']

class ViewModelO2MFormMdCrmProduct(ViewModelO2MForm):
	_name = "model.o2mform.md.crm.product"
	_model = "md.crm.product"
	_description = "CRM Of Product"
	_columns = ['product_id', 'vat', 'uom', 'price', 'currency', 'unit', 'uop', 'note']

class ViewModelO2MListMdCrmProduct(ViewModelO2MList):
	_name = "model.o2mlist.md.crm.product"
	_model = "md.crm.product"
	_description = "CRM Of Product"
	_columns = ['product_id', 'vat', 'uom', 'price', 'currency', 'unit', 'uop', 'note']
