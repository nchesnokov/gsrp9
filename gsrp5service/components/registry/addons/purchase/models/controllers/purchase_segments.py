from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPurchaseSegments(ViewModelSearchController):
	_name = "search:purchase.segments"
	_view_name = "purchase.segments/search"
	_description = "Purchase Segments"

class ViewModelFindPurchaseSegments(ViewModelFindController):
	_name = "find:purchase.segments"
	_view_name = "purchase.segments/find"
	_description = "Purchase Segments"

class ViewModelListPurchaseSegments(ViewModelListController):
	_name = "list:purchase.segments"
	_view_name = "purchase.segments/list"
	_description = "Purchase Segments"

class ViewModelFormModalPurchaseSegments(ViewModelFormModalController):
	_name = "form.modal:purchase.segments"
	_view_name = "purchase.segments/form.modal"
	_description = "Purchase Segments"

class ViewModelFormPurchaseSegments(ViewModelFormController):
	_name = "form:purchase.segments"
	_view_name = "purchase.segments/form"
	_description = "Purchase Segments"
