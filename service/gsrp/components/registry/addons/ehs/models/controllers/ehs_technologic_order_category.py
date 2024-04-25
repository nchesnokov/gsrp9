from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchEhsTechnologicOrderCategory(ViewModelSearchController):
	_name = "search:ehs.technologic.order.category"
	_view_name = "ehs.technologic.order.category/search"
	_description = "Category Technologic Order"

class ViewModelFindEhsTechnologicOrderCategory(ViewModelFindController):
	_name = "find:ehs.technologic.order.category"
	_view_name = "ehs.technologic.order.category/find"
	_description = "Category Technologic Order"

class ViewModelListEhsTechnologicOrderCategory(ViewModelListController):
	_name = "list:ehs.technologic.order.category"
	_view_name = "ehs.technologic.order.category/list"
	_description = "Category Technologic Order"

class ViewModelFormModalEhsTechnologicOrderCategory(ViewModelFormModalController):
	_name = "form.modal:ehs.technologic.order.category"
	_view_name = "ehs.technologic.order.category/form.modal"
	_description = "Category Technologic Order"

class ViewModelFormEhsTechnologicOrderCategory(ViewModelFormController):
	_name = "form:ehs.technologic.order.category"
	_view_name = "ehs.technologic.order.category/form"
	_description = "Category Technologic Order"

class ViewModelTreeEhsTechnologicOrderCategory(ViewModelTreeController):
	_name = "tree:ehs.technologic.order.category"
	_view_name = "ehs.technologic.order.category/tree"
	_description = "Category Technologic Order"
