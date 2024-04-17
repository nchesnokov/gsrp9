from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchWkf1ElementCategories(ViewModelSearchController):
	_name = "search:wkf1.element.categories"
	_view_name = "wkf1.element.categories/search"
	_description = "Workflow Element Category"

class ViewModelFindWkf1ElementCategories(ViewModelFindController):
	_name = "find:wkf1.element.categories"
	_view_name = "wkf1.element.categories/find"
	_description = "Workflow Element Category"

class ViewModelListWkf1ElementCategories(ViewModelListController):
	_name = "list:wkf1.element.categories"
	_view_name = "wkf1.element.categories/list"
	_description = "Workflow Element Category"

class ViewModelFormModalWkf1ElementCategories(ViewModelFormModalController):
	_name = "form.modal:wkf1.element.categories"
	_view_name = "wkf1.element.categories/form.modal"
	_description = "Workflow Element Category"

class ViewModelFormWkf1ElementCategories(ViewModelFormController):
	_name = "form:wkf1.element.categories"
	_view_name = "wkf1.element.categories/form"
	_description = "Workflow Element Category"

class ViewModelTreeWkf1ElementCategories(ViewModelTreeController):
	_name = "tree:wkf1.element.categories"
	_view_name = "wkf1.element.categories/tree"
	_description = "Workflow Element Category"
