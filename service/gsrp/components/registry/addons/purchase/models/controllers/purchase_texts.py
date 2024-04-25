from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPurchaseTexts(ViewModelSearchController):
	_name = "search:purchase.texts"
	_view_name = "purchase.texts/search"
	_description = "Purchase Texts"

class ViewModelFindPurchaseTexts(ViewModelFindController):
	_name = "find:purchase.texts"
	_view_name = "purchase.texts/find"
	_description = "Purchase Texts"

class ViewModelListPurchaseTexts(ViewModelListController):
	_name = "list:purchase.texts"
	_view_name = "purchase.texts/list"
	_description = "Purchase Texts"

class ViewModelFormModalPurchaseTexts(ViewModelFormModalController):
	_name = "form.modal:purchase.texts"
	_view_name = "purchase.texts/form.modal"
	_description = "Purchase Texts"

class ViewModelFormPurchaseTexts(ViewModelFormController):
	_name = "form:purchase.texts"
	_view_name = "purchase.texts/form"
	_description = "Purchase Texts"
