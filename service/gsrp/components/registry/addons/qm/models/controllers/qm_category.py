from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchQmCategory(ViewModelSearchController):
	_name = "search:qm.category"
	_view_name = "qm.category/search"
	_description = "Quantity Category"

class ViewModelFindQmCategory(ViewModelFindController):
	_name = "find:qm.category"
	_view_name = "qm.category/find"
	_description = "Quantity Category"

class ViewModelListQmCategory(ViewModelListController):
	_name = "list:qm.category"
	_view_name = "qm.category/list"
	_description = "Quantity Category"

class ViewModelFormModalQmCategory(ViewModelFormModalController):
	_name = "form.modal:qm.category"
	_view_name = "qm.category/form.modal"
	_description = "Quantity Category"

class ViewModelFormQmCategory(ViewModelFormController):
	_name = "form:qm.category"
	_view_name = "qm.category/form"
	_description = "Quantity Category"
