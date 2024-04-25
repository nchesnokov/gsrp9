from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPrjAreaCategories(ViewModelSearchController):
	_name = "search:prj.area.categories"
	_view_name = "prj.area.categories/search"
	_description = "Categories Project Area"

class ViewModelFindPrjAreaCategories(ViewModelFindController):
	_name = "find:prj.area.categories"
	_view_name = "prj.area.categories/find"
	_description = "Categories Project Area"

class ViewModelListPrjAreaCategories(ViewModelListController):
	_name = "list:prj.area.categories"
	_view_name = "prj.area.categories/list"
	_description = "Categories Project Area"

class ViewModelFormModalPrjAreaCategories(ViewModelFormModalController):
	_name = "form.modal:prj.area.categories"
	_view_name = "prj.area.categories/form.modal"
	_description = "Categories Project Area"

class ViewModelFormPrjAreaCategories(ViewModelFormController):
	_name = "form:prj.area.categories"
	_view_name = "prj.area.categories/form"
	_description = "Categories Project Area"

class ViewModelTreePrjAreaCategories(ViewModelTreeController):
	_name = "tree:prj.area.categories"
	_view_name = "prj.area.categories/tree"
	_description = "Categories Project Area"
