from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeInboundDeliveryPacklist(ViewModelFind):
	_name = "model.find.le.inbound.delivery.packlist"
	_model = "le.inbound.delivery.packlist"
	_description = "Packlist Of Inbound Delivery"
	_columns = ['item_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount']

class ViewModelListLeInboundDeliveryPacklist(ViewModelList):
	_name = "model.list.le.inbound.delivery.packlist"
	_model = "le.inbound.delivery.packlist"
	_description = "Packlist Of Inbound Delivery"
	_columns = ['item_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount']

class ViewModelFormModalLeInboundDeliveryPacklist(ViewModelFormModal):
	_name = "model.form.modal.le.inbound.delivery.packlist"
	_model = "le.inbound.delivery.packlist"
	_description = "Packlist Of Inbound Delivery"
	_columns = ['item_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'note']

class ViewModelFormLeInboundDeliveryPacklist(ViewModelForm):
	_name = "model.form.le.inbound.delivery.packlist"
	_model = "le.inbound.delivery.packlist"
	_description = "Packlist Of Inbound Delivery"
	_columns = ['item_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'note']

class ViewModelO2MFormLeInboundDeliveryPacklist(ViewModelO2MForm):
	_name = "model.o2mform.le.inbound.delivery.packlist"
	_model = "le.inbound.delivery.packlist"
	_description = "Packlist Of Inbound Delivery"
	_columns = ['item_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'note']

class ViewModelO2MListLeInboundDeliveryPacklist(ViewModelO2MList):
	_name = "model.o2mlist.le.inbound.delivery.packlist"
	_model = "le.inbound.delivery.packlist"
	_description = "Packlist Of Inbound Delivery"
	_columns = ['item_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount']
