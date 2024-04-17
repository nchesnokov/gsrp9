from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPrjTaskCategory(ViewModelSearchController):
	_name = "search:prj.task.category"
	_view_name = "prj.task.category/search"
	_description = "Category Project Task"

class ViewModelFindPrjTaskCategory(ViewModelFindController):
	_name = "find:prj.task.category"
	_view_name = "prj.task.category/find"
	_description = "Category Project Task"

class ViewModelListPrjTaskCategory(ViewModelListController):
	_name = "list:prj.task.category"
	_view_name = "prj.task.category/list"
	_description = "Category Project Task"

class ViewModelFormModalPrjTaskCategory(ViewModelFormModalController):
	_name = "form.modal:prj.task.category"
	_view_name = "prj.task.category/form.modal"
	_description = "Category Project Task"

class ViewModelFormPrjTaskCategory(ViewModelFormController):
	_name = "form:prj.task.category"
	_view_name = "prj.task.category/form"
	_description = "Category Project Task"

class ViewModelTreePrjTaskCategory(ViewModelTreeController):
	_name = "tree:prj.task.category"
	_view_name = "prj.task.category/tree"
	_description = "Category Project Task"
