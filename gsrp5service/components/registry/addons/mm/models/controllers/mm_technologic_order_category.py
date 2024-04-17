from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchMmTechnologicOrderCategory(ViewModelSearchController):
	_name = "search:mm.technologic.order.category"
	_view_name = "mm.technologic.order.category/search"
	_description = "Category Technologic Order"

class ViewModelFindMmTechnologicOrderCategory(ViewModelFindController):
	_name = "find:mm.technologic.order.category"
	_view_name = "mm.technologic.order.category/find"
	_description = "Category Technologic Order"

class ViewModelListMmTechnologicOrderCategory(ViewModelListController):
	_name = "list:mm.technologic.order.category"
	_view_name = "mm.technologic.order.category/list"
	_description = "Category Technologic Order"

class ViewModelFormModalMmTechnologicOrderCategory(ViewModelFormModalController):
	_name = "form.modal:mm.technologic.order.category"
	_view_name = "mm.technologic.order.category/form.modal"
	_description = "Category Technologic Order"

class ViewModelFormMmTechnologicOrderCategory(ViewModelFormController):
	_name = "form:mm.technologic.order.category"
	_view_name = "mm.technologic.order.category/form"
	_description = "Category Technologic Order"

class ViewModelTreeMmTechnologicOrderCategory(ViewModelTreeController):
	_name = "tree:mm.technologic.order.category"
	_view_name = "mm.technologic.order.category/tree"
	_description = "Category Technologic Order"
