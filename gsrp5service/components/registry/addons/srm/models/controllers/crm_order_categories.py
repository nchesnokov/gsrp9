from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchCrmOrderCategories(ViewModelSearchController):
	_name = "search:crm.order.categories"
	_view_name = "crm.order.categories/search"
	_description = "Category CRM Order"

class ViewModelFindCrmOrderCategories(ViewModelFindController):
	_name = "find:crm.order.categories"
	_view_name = "crm.order.categories/find"
	_description = "Category CRM Order"

class ViewModelListCrmOrderCategories(ViewModelListController):
	_name = "list:crm.order.categories"
	_view_name = "crm.order.categories/list"
	_description = "Category CRM Order"

class ViewModelFormModalCrmOrderCategories(ViewModelFormModalController):
	_name = "form.modal:crm.order.categories"
	_view_name = "crm.order.categories/form.modal"
	_description = "Category CRM Order"

class ViewModelFormCrmOrderCategories(ViewModelFormController):
	_name = "form:crm.order.categories"
	_view_name = "crm.order.categories/form"
	_description = "Category CRM Order"

class ViewModelTreeCrmOrderCategories(ViewModelTreeController):
	_name = "tree:crm.order.categories"
	_view_name = "crm.order.categories/tree"
	_description = "Category CRM Order"
