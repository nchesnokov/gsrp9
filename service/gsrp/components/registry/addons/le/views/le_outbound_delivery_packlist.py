from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeOutboundDeliveryPacklist(ViewModelFind):
	_name = "model.find.le.outbound.delivery.packlist"
	_model = "le.outbound.delivery.packlist"
	_description = "Packlist Of Outbound Delivery"
	_columns = ['item_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount']

class ViewModelListLeOutboundDeliveryPacklist(ViewModelList):
	_name = "model.list.le.outbound.delivery.packlist"
	_model = "le.outbound.delivery.packlist"
	_description = "Packlist Of Outbound Delivery"
	_columns = ['item_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount']

class ViewModelFormModalLeOutboundDeliveryPacklist(ViewModelFormModal):
	_name = "model.form.modal.le.outbound.delivery.packlist"
	_model = "le.outbound.delivery.packlist"
	_description = "Packlist Of Outbound Delivery"
	_columns = ['item_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'note']

class ViewModelFormLeOutboundDeliveryPacklist(ViewModelForm):
	_name = "model.form.le.outbound.delivery.packlist"
	_model = "le.outbound.delivery.packlist"
	_description = "Packlist Of Outbound Delivery"
	_columns = ['item_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'note']

class ViewModelO2MFormLeOutboundDeliveryPacklist(ViewModelO2MForm):
	_name = "model.o2mform.le.outbound.delivery.packlist"
	_model = "le.outbound.delivery.packlist"
	_description = "Packlist Of Outbound Delivery"
	_columns = ['item_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'note']

class ViewModelO2MListLeOutboundDeliveryPacklist(ViewModelO2MList):
	_name = "model.o2mlist.le.outbound.delivery.packlist"
	_model = "le.outbound.delivery.packlist"
	_description = "Packlist Of Outbound Delivery"
	_columns = ['item_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount']
