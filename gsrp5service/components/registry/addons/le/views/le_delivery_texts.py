from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm

class ViewModelSearchLeDeliveryTexts(ViewModelSearch):
	_name = "model.search.le.delivery.texts"
	_model = "le.delivery.texts"
	_description = "Delivery Texts"
	_columns = ['code', 'descr']

class ViewModelFindLeDeliveryTexts(ViewModelFind):
	_name = "model.find.le.delivery.texts"
	_model = "le.delivery.texts"
	_description = "Delivery Texts"
	_columns = ['code', 'descr']

class ViewModelListLeDeliveryTexts(ViewModelList):
	_name = "model.list.le.delivery.texts"
	_model = "le.delivery.texts"
	_description = "Delivery Texts"
	_columns = ['code', 'descr']

class ViewModelFormModalLeDeliveryTexts(ViewModelFormModal):
	_name = "model.form.modal.le.delivery.texts"
	_model = "le.delivery.texts"
	_description = "Delivery Texts"
	_columns = ['code', 'descr']

class ViewModelFormLeDeliveryTexts(ViewModelForm):
	_name = "model.form.le.delivery.texts"
	_model = "le.delivery.texts"
	_description = "Delivery Texts"
	_columns = ['code', 'descr']
