from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelKanbanController

class ViewModelSearchMdProduct(ViewModelSearchController):
	_name = "search:md.product"
	_view_name = "md.product/search"
	_description = "Product"

class ViewModelFindMdProduct(ViewModelFindController):
	_name = "find:md.product"
	_view_name = "md.product/find"
	_description = "Product"

class ViewModelListMdProduct(ViewModelListController):
	_name = "list:md.product"
	_view_name = "md.product/list"
	_description = "Product"

class ViewModelFormModalMdProduct(ViewModelFormModalController):
	_name = "form.modal:md.product"
	_view_name = "md.product/form.modal"
	_description = "Product"

class ViewModelFormMdProduct(ViewModelFormController):
	_name = "form:md.product"
	_view_name = "md.product/form"
	_description = "Product"

class ViewModelKanbanMdProduct(ViewModelKanbanController):
	_name = "kanban:md.product"
	_view_name = "md.product/kanban"
	_description = "Product"
