from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelTree
from gsrp5service.obj.view import ViewModelO2MTree
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchLeInternalDeliveryCategory(ViewModelSearch):
	_name = "model.search.le.internal.delivery.category"
	_model = "le.internal.delivery.category"
	_description = "Category Internal Delivery"
	_columns = ['name', 'parent_id']

class ViewModelFindLeInternalDeliveryCategory(ViewModelFind):
	_name = "model.find.le.internal.delivery.category"
	_model = "le.internal.delivery.category"
	_description = "Category Internal Delivery"
	_columns = ['name', 'parent_id']

class ViewModelListLeInternalDeliveryCategory(ViewModelList):
	_name = "model.list.le.internal.delivery.category"
	_model = "le.internal.delivery.category"
	_description = "Category Internal Delivery"
	_columns = ['name', 'parent_id', 'childs_id', 'deliveries']

class ViewModelFormModalLeInternalDeliveryCategory(ViewModelFormModal):
	_name = "model.form.modal.le.internal.delivery.category"
	_model = "le.internal.delivery.category"
	_description = "Category Internal Delivery"
	_columns = ['name', 'parent_id', 'childs_id', 'deliveries', 'note']

class ViewModelFormLeInternalDeliveryCategory(ViewModelForm):
	_name = "model.form.le.internal.delivery.category"
	_model = "le.internal.delivery.category"
	_description = "Category Internal Delivery"
	_columns = ['name', 'parent_id', 'childs_id', 'deliveries', 'note']

class ViewModelO2MFormLeInternalDeliveryCategory(ViewModelO2MForm):
	_name = "model.o2mform.le.internal.delivery.category"
	_model = "le.internal.delivery.category"
	_description = "Category Internal Delivery"
	_columns = ['name', 'parent_id', 'childs_id', 'deliveries', 'note']

class ViewModelTreeLeInternalDeliveryCategory(ViewModelTree):
	_name = "model.tree.le.internal.delivery.category"
	_model = "le.internal.delivery.category"
	_description = "Category Internal Delivery"
	_columns = ['name', 'parent_id']

class ViewModelO2MTreeLeInternalDeliveryCategory(ViewModelO2MTree):
	_name = "model.o2mtree.le.internal.delivery.category"
	_model = "le.internal.delivery.category"
	_description = "Category Internal Delivery"
	_columns = ['name', 'parent_id']

class ViewModelO2MListLeInternalDeliveryCategory(ViewModelO2MList):
	_name = "model.o2mlist.le.internal.delivery.category"
	_model = "le.internal.delivery.category"
	_description = "Category Internal Delivery"
	_columns = ['name', 'parent_id', 'childs_id', 'deliveries']
