from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSaleTexts(ViewModelSearchController):
	_name = "search:sale.texts"
	_view_name = "sale.texts/search"
	_description = "Sale Texts"

class ViewModelFindSaleTexts(ViewModelFindController):
	_name = "find:sale.texts"
	_view_name = "sale.texts/find"
	_description = "Sale Texts"

class ViewModelListSaleTexts(ViewModelListController):
	_name = "list:sale.texts"
	_view_name = "sale.texts/list"
	_description = "Sale Texts"

class ViewModelFormModalSaleTexts(ViewModelFormModalController):
	_name = "form.modal:sale.texts"
	_view_name = "sale.texts/form.modal"
	_description = "Sale Texts"

class ViewModelFormSaleTexts(ViewModelFormController):
	_name = "form:sale.texts"
	_view_name = "sale.texts/form"
	_description = "Sale Texts"
