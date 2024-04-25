from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchScmTechnologicOrderCategory(ViewModelSearchController):
	_name = "search:scm.technologic.order.category"
	_view_name = "scm.technologic.order.category/search"
	_description = "Category Technologic Order"

class ViewModelFindScmTechnologicOrderCategory(ViewModelFindController):
	_name = "find:scm.technologic.order.category"
	_view_name = "scm.technologic.order.category/find"
	_description = "Category Technologic Order"

class ViewModelListScmTechnologicOrderCategory(ViewModelListController):
	_name = "list:scm.technologic.order.category"
	_view_name = "scm.technologic.order.category/list"
	_description = "Category Technologic Order"

class ViewModelFormModalScmTechnologicOrderCategory(ViewModelFormModalController):
	_name = "form.modal:scm.technologic.order.category"
	_view_name = "scm.technologic.order.category/form.modal"
	_description = "Category Technologic Order"

class ViewModelFormScmTechnologicOrderCategory(ViewModelFormController):
	_name = "form:scm.technologic.order.category"
	_view_name = "scm.technologic.order.category/form"
	_description = "Category Technologic Order"

class ViewModelTreeScmTechnologicOrderCategory(ViewModelTreeController):
	_name = "tree:scm.technologic.order.category"
	_view_name = "scm.technologic.order.category/tree"
	_description = "Category Technologic Order"
