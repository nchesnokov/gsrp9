from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelTree
from gsrp5service.obj.view import ViewModelO2MTree
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchLeOutboundDeliveryCategory(ViewModelSearch):
	_name = "model.search.le.outbound.delivery.category"
	_model = "le.outbound.delivery.category"
	_description = "Category Outbound Delivery"
	_columns = ['name', 'parent_id']

class ViewModelFindLeOutboundDeliveryCategory(ViewModelFind):
	_name = "model.find.le.outbound.delivery.category"
	_model = "le.outbound.delivery.category"
	_description = "Category Outbound Delivery"
	_columns = ['name', 'parent_id']

class ViewModelListLeOutboundDeliveryCategory(ViewModelList):
	_name = "model.list.le.outbound.delivery.category"
	_model = "le.outbound.delivery.category"
	_description = "Category Outbound Delivery"
	_columns = ['name', 'parent_id', 'childs_id', 'deliveries']

class ViewModelFormModalLeOutboundDeliveryCategory(ViewModelFormModal):
	_name = "model.form.modal.le.outbound.delivery.category"
	_model = "le.outbound.delivery.category"
	_description = "Category Outbound Delivery"
	_columns = ['name', 'parent_id', 'childs_id', 'deliveries', 'note']

class ViewModelFormLeOutboundDeliveryCategory(ViewModelForm):
	_name = "model.form.le.outbound.delivery.category"
	_model = "le.outbound.delivery.category"
	_description = "Category Outbound Delivery"
	_columns = ['name', 'parent_id', 'childs_id', 'deliveries', 'note']

class ViewModelO2MFormLeOutboundDeliveryCategory(ViewModelO2MForm):
	_name = "model.o2mform.le.outbound.delivery.category"
	_model = "le.outbound.delivery.category"
	_description = "Category Outbound Delivery"
	_columns = ['name', 'parent_id', 'childs_id', 'deliveries', 'note']

class ViewModelTreeLeOutboundDeliveryCategory(ViewModelTree):
	_name = "model.tree.le.outbound.delivery.category"
	_model = "le.outbound.delivery.category"
	_description = "Category Outbound Delivery"
	_columns = ['name', 'parent_id']

class ViewModelO2MTreeLeOutboundDeliveryCategory(ViewModelO2MTree):
	_name = "model.o2mtree.le.outbound.delivery.category"
	_model = "le.outbound.delivery.category"
	_description = "Category Outbound Delivery"
	_columns = ['name', 'parent_id']

class ViewModelO2MListLeOutboundDeliveryCategory(ViewModelO2MList):
	_name = "model.o2mlist.le.outbound.delivery.category"
	_model = "le.outbound.delivery.category"
	_description = "Category Outbound Delivery"
	_columns = ['name', 'parent_id', 'childs_id', 'deliveries']
