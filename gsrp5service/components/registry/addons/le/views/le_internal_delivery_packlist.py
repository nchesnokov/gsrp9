from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeInternalDeliveryPacklist(ViewModelFind):
	_name = "model.find.le.internal.delivery.packlist"
	_model = "le.internal.delivery.packlist"
	_description = "Packlist Of Internal Delivery"
	_columns = ['item_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount']

class ViewModelListLeInternalDeliveryPacklist(ViewModelList):
	_name = "model.list.le.internal.delivery.packlist"
	_model = "le.internal.delivery.packlist"
	_description = "Packlist Of Internal Delivery"
	_columns = ['item_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount']

class ViewModelFormModalLeInternalDeliveryPacklist(ViewModelFormModal):
	_name = "model.form.modal.le.internal.delivery.packlist"
	_model = "le.internal.delivery.packlist"
	_description = "Packlist Of Internal Delivery"
	_columns = ['item_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'note']

class ViewModelFormLeInternalDeliveryPacklist(ViewModelForm):
	_name = "model.form.le.internal.delivery.packlist"
	_model = "le.internal.delivery.packlist"
	_description = "Packlist Of Internal Delivery"
	_columns = ['item_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'note']

class ViewModelO2MFormLeInternalDeliveryPacklist(ViewModelO2MForm):
	_name = "model.o2mform.le.internal.delivery.packlist"
	_model = "le.internal.delivery.packlist"
	_description = "Packlist Of Internal Delivery"
	_columns = ['item_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'note']

class ViewModelO2MListLeInternalDeliveryPacklist(ViewModelO2MList):
	_name = "model.o2mlist.le.internal.delivery.packlist"
	_model = "le.internal.delivery.packlist"
	_description = "Packlist Of Internal Delivery"
	_columns = ['item_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount']
