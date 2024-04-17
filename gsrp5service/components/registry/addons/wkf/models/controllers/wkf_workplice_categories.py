from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchWkfWorkpliceCategories(ViewModelSearchController):
	_name = "search:wkf.workplice.categories"
	_view_name = "wkf.workplice.categories/search"
	_description = "Workflow Workplice Category"

class ViewModelFindWkfWorkpliceCategories(ViewModelFindController):
	_name = "find:wkf.workplice.categories"
	_view_name = "wkf.workplice.categories/find"
	_description = "Workflow Workplice Category"

class ViewModelListWkfWorkpliceCategories(ViewModelListController):
	_name = "list:wkf.workplice.categories"
	_view_name = "wkf.workplice.categories/list"
	_description = "Workflow Workplice Category"

class ViewModelFormModalWkfWorkpliceCategories(ViewModelFormModalController):
	_name = "form.modal:wkf.workplice.categories"
	_view_name = "wkf.workplice.categories/form.modal"
	_description = "Workflow Workplice Category"

class ViewModelFormWkfWorkpliceCategories(ViewModelFormController):
	_name = "form:wkf.workplice.categories"
	_view_name = "wkf.workplice.categories/form"
	_description = "Workflow Workplice Category"

class ViewModelTreeWkfWorkpliceCategories(ViewModelTreeController):
	_name = "tree:wkf.workplice.categories"
	_view_name = "wkf.workplice.categories/tree"
	_description = "Workflow Workplice Category"
