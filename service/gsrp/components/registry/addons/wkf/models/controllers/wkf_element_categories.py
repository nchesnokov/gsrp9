from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchWkfElementCategories(ViewModelSearchController):
	_name = "search:wkf.element.categories"
	_view_name = "wkf.element.categories/search"
	_description = "Workflow Element Category"

class ViewModelFindWkfElementCategories(ViewModelFindController):
	_name = "find:wkf.element.categories"
	_view_name = "wkf.element.categories/find"
	_description = "Workflow Element Category"

class ViewModelListWkfElementCategories(ViewModelListController):
	_name = "list:wkf.element.categories"
	_view_name = "wkf.element.categories/list"
	_description = "Workflow Element Category"

class ViewModelFormModalWkfElementCategories(ViewModelFormModalController):
	_name = "form.modal:wkf.element.categories"
	_view_name = "wkf.element.categories/form.modal"
	_description = "Workflow Element Category"

class ViewModelFormWkfElementCategories(ViewModelFormController):
	_name = "form:wkf.element.categories"
	_view_name = "wkf.element.categories/form"
	_description = "Workflow Element Category"

class ViewModelTreeWkfElementCategories(ViewModelTreeController):
	_name = "tree:wkf.element.categories"
	_view_name = "wkf.element.categories/tree"
	_description = "Workflow Element Category"
