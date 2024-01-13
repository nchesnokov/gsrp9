from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelTree
from gsrp5service.obj.view import ViewModelO2MTree
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchLeInboundDeliveryCategory(ViewModelSearch):
	_name = "model.search.le.inbound.delivery.category"
	_model = "le.inbound.delivery.category"
	_description = "Category Inbound Delivery"
	_columns = ['name', 'parent_id']

class ViewModelFindLeInboundDeliveryCategory(ViewModelFind):
	_name = "model.find.le.inbound.delivery.category"
	_model = "le.inbound.delivery.category"
	_description = "Category Inbound Delivery"
	_columns = ['name', 'parent_id']

class ViewModelListLeInboundDeliveryCategory(ViewModelList):
	_name = "model.list.le.inbound.delivery.category"
	_model = "le.inbound.delivery.category"
	_description = "Category Inbound Delivery"
	_columns = ['name', 'parent_id', 'childs_id', 'deliveries']

class ViewModelFormModalLeInboundDeliveryCategory(ViewModelFormModal):
	_name = "model.form.modal.le.inbound.delivery.category"
	_model = "le.inbound.delivery.category"
	_description = "Category Inbound Delivery"
	_columns = ['name', 'parent_id', 'childs_id', 'deliveries', 'note']

class ViewModelFormLeInboundDeliveryCategory(ViewModelForm):
	_name = "model.form.le.inbound.delivery.category"
	_model = "le.inbound.delivery.category"
	_description = "Category Inbound Delivery"
	_columns = ['name', 'parent_id', 'childs_id', 'deliveries', 'note']

class ViewModelO2MFormLeInboundDeliveryCategory(ViewModelO2MForm):
	_name = "model.o2mform.le.inbound.delivery.category"
	_model = "le.inbound.delivery.category"
	_description = "Category Inbound Delivery"
	_columns = ['name', 'parent_id', 'childs_id', 'deliveries', 'note']

class ViewModelTreeLeInboundDeliveryCategory(ViewModelTree):
	_name = "model.tree.le.inbound.delivery.category"
	_model = "le.inbound.delivery.category"
	_description = "Category Inbound Delivery"
	_columns = ['name', 'parent_id']

class ViewModelO2MTreeLeInboundDeliveryCategory(ViewModelO2MTree):
	_name = "model.o2mtree.le.inbound.delivery.category"
	_model = "le.inbound.delivery.category"
	_description = "Category Inbound Delivery"
	_columns = ['name', 'parent_id']

class ViewModelO2MListLeInboundDeliveryCategory(ViewModelO2MList):
	_name = "model.o2mlist.le.inbound.delivery.category"
	_model = "le.inbound.delivery.category"
	_description = "Category Inbound Delivery"
	_columns = ['name', 'parent_id', 'childs_id', 'deliveries']
