from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeOutboundDeliveryItems(ViewModelFind):
	_name = "model.find.le.outbound.delivery.items"
	_model = "le.outbound.delivery.items"
	_description = "Outbound Delivery Items"
	_columns = ['delivery_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'schedule', 'amount', 'vat_code', 'vat_amount', 'total_amount']

class ViewModelListLeOutboundDeliveryItems(ViewModelList):
	_name = "model.list.le.outbound.delivery.items"
	_model = "le.outbound.delivery.items"
	_description = "Outbound Delivery Items"
	_columns = ['delivery_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'schedule', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'packlist', 'texts']

class ViewModelFormModalLeOutboundDeliveryItems(ViewModelFormModal):
	_name = "model.form.modal.le.outbound.delivery.items"
	_model = "le.outbound.delivery.items"
	_description = "Outbound Delivery Items"
	_columns = ['delivery_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'schedule', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'packlist', 'texts', 'note']

class ViewModelFormLeOutboundDeliveryItems(ViewModelForm):
	_name = "model.form.le.outbound.delivery.items"
	_model = "le.outbound.delivery.items"
	_description = "Outbound Delivery Items"
	_columns = ['delivery_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'schedule', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'packlist', 'texts', 'note']

class ViewModelO2MFormLeOutboundDeliveryItems(ViewModelO2MForm):
	_name = "model.o2mform.le.outbound.delivery.items"
	_model = "le.outbound.delivery.items"
	_description = "Outbound Delivery Items"
	_columns = ['delivery_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'schedule', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'packlist', 'texts', 'note']

class ViewModelO2MListLeOutboundDeliveryItems(ViewModelO2MList):
	_name = "model.o2mlist.le.outbound.delivery.items"
	_model = "le.outbound.delivery.items"
	_description = "Outbound Delivery Items"
	_columns = ['delivery_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'schedule', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'packlist', 'texts']
