from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindMdPackProduct(ViewModelFind):
	_name = "model.find.md.pack.product"
	_model = "md.pack.product"
	_description = "Pack Of Product"
	_columns = ['product_id', 'vat', 'uom', 'price', 'currency', 'unit', 'uop']

class ViewModelListMdPackProduct(ViewModelList):
	_name = "model.list.md.pack.product"
	_model = "md.pack.product"
	_description = "Pack Of Product"
	_columns = ['product_id', 'vat', 'uom', 'price', 'currency', 'unit', 'uop']

class ViewModelFormModalMdPackProduct(ViewModelFormModal):
	_name = "model.form.modal.md.pack.product"
	_model = "md.pack.product"
	_description = "Pack Of Product"
	_columns = ['product_id', 'vat', 'uom', 'price', 'currency', 'unit', 'uop', 'note']

class ViewModelFormMdPackProduct(ViewModelForm):
	_name = "model.form.md.pack.product"
	_model = "md.pack.product"
	_description = "Pack Of Product"
	_columns = ['product_id', 'vat', 'uom', 'price', 'currency', 'unit', 'uop', 'note']

class ViewModelO2MFormMdPackProduct(ViewModelO2MForm):
	_name = "model.o2mform.md.pack.product"
	_model = "md.pack.product"
	_description = "Pack Of Product"
	_columns = ['product_id', 'vat', 'uom', 'price', 'currency', 'unit', 'uop', 'note']

class ViewModelO2MListMdPackProduct(ViewModelO2MList):
	_name = "model.o2mlist.md.pack.product"
	_model = "md.pack.product"
	_description = "Pack Of Product"
	_columns = ['product_id', 'vat', 'uom', 'price', 'currency', 'unit', 'uop']
