from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeInboundDeliveryItems(ViewModelFind):
	_name = "model.find.le.inbound.delivery.items"
	_model = "le.inbound.delivery.items"
	_description = "Inbound Delivery Items"
	_columns = ['delivery_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'schedule', 'amount', 'vat_code', 'vat_amount', 'total_amount']

class ViewModelListLeInboundDeliveryItems(ViewModelList):
	_name = "model.list.le.inbound.delivery.items"
	_model = "le.inbound.delivery.items"
	_description = "Inbound Delivery Items"
	_columns = ['delivery_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'schedule', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'packlist', 'texts']

class ViewModelFormModalLeInboundDeliveryItems(ViewModelFormModal):
	_name = "model.form.modal.le.inbound.delivery.items"
	_model = "le.inbound.delivery.items"
	_description = "Inbound Delivery Items"
	_columns = ['delivery_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'schedule', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'packlist', 'texts', 'note']

class ViewModelFormLeInboundDeliveryItems(ViewModelForm):
	_name = "model.form.le.inbound.delivery.items"
	_model = "le.inbound.delivery.items"
	_description = "Inbound Delivery Items"
	_columns = ['delivery_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'schedule', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'packlist', 'texts', 'note']

class ViewModelO2MFormLeInboundDeliveryItems(ViewModelO2MForm):
	_name = "model.o2mform.le.inbound.delivery.items"
	_model = "le.inbound.delivery.items"
	_description = "Inbound Delivery Items"
	_columns = ['delivery_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'schedule', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'packlist', 'texts', 'note']

class ViewModelO2MListLeInboundDeliveryItems(ViewModelO2MList):
	_name = "model.o2mlist.le.inbound.delivery.items"
	_model = "le.inbound.delivery.items"
	_description = "Inbound Delivery Items"
	_columns = ['delivery_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'schedule', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'packlist', 'texts']
