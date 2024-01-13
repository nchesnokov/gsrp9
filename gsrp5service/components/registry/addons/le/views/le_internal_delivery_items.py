from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeInternalDeliveryItems(ViewModelFind):
	_name = "model.find.le.internal.delivery.items"
	_model = "le.internal.delivery.items"
	_description = "Internal Delivery Items"
	_columns = ['delivery_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'schedule', 'amount', 'vat_code', 'vat_amount', 'total_amount']

class ViewModelListLeInternalDeliveryItems(ViewModelList):
	_name = "model.list.le.internal.delivery.items"
	_model = "le.internal.delivery.items"
	_description = "Internal Delivery Items"
	_columns = ['delivery_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'schedule', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'packlist', 'texts']

class ViewModelFormModalLeInternalDeliveryItems(ViewModelFormModal):
	_name = "model.form.modal.le.internal.delivery.items"
	_model = "le.internal.delivery.items"
	_description = "Internal Delivery Items"
	_columns = ['delivery_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'schedule', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'packlist', 'texts', 'note']

class ViewModelFormLeInternalDeliveryItems(ViewModelForm):
	_name = "model.form.le.internal.delivery.items"
	_model = "le.internal.delivery.items"
	_description = "Internal Delivery Items"
	_columns = ['delivery_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'schedule', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'packlist', 'texts', 'note']

class ViewModelO2MFormLeInternalDeliveryItems(ViewModelO2MForm):
	_name = "model.o2mform.le.internal.delivery.items"
	_model = "le.internal.delivery.items"
	_description = "Internal Delivery Items"
	_columns = ['delivery_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'schedule', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'packlist', 'texts', 'note']

class ViewModelO2MListLeInternalDeliveryItems(ViewModelO2MList):
	_name = "model.o2mlist.le.internal.delivery.items"
	_model = "le.internal.delivery.items"
	_description = "Internal Delivery Items"
	_columns = ['delivery_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'schedule', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'packlist', 'texts']
