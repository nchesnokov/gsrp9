from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPrjPrjCategory(ViewModelSearchController):
	_name = "search:prj.prj.category"
	_view_name = "prj.prj.category/search"
	_description = "Category Project Project"

class ViewModelFindPrjPrjCategory(ViewModelFindController):
	_name = "find:prj.prj.category"
	_view_name = "prj.prj.category/find"
	_description = "Category Project Project"

class ViewModelListPrjPrjCategory(ViewModelListController):
	_name = "list:prj.prj.category"
	_view_name = "prj.prj.category/list"
	_description = "Category Project Project"

class ViewModelFormModalPrjPrjCategory(ViewModelFormModalController):
	_name = "form.modal:prj.prj.category"
	_view_name = "prj.prj.category/form.modal"
	_description = "Category Project Project"

class ViewModelFormPrjPrjCategory(ViewModelFormController):
	_name = "form:prj.prj.category"
	_view_name = "prj.prj.category/form"
	_description = "Category Project Project"

class ViewModelTreePrjPrjCategory(ViewModelTreeController):
	_name = "tree:prj.prj.category"
	_view_name = "prj.prj.category/tree"
	_description = "Category Project Project"
