from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchLeDeliveryTexts(ViewModelSearchController):
	_name = "search:le.delivery.texts"
	_view_name = "le.delivery.texts/search"
	_description = "Delivery Texts"

class ViewModelFindLeDeliveryTexts(ViewModelFindController):
	_name = "find:le.delivery.texts"
	_view_name = "le.delivery.texts/find"
	_description = "Delivery Texts"

class ViewModelListLeDeliveryTexts(ViewModelListController):
	_name = "list:le.delivery.texts"
	_view_name = "le.delivery.texts/list"
	_description = "Delivery Texts"

class ViewModelFormModalLeDeliveryTexts(ViewModelFormModalController):
	_name = "form.modal:le.delivery.texts"
	_view_name = "le.delivery.texts/form.modal"
	_description = "Delivery Texts"

class ViewModelFormLeDeliveryTexts(ViewModelFormController):
	_name = "form:le.delivery.texts"
	_view_name = "le.delivery.texts/form"
	_description = "Delivery Texts"
