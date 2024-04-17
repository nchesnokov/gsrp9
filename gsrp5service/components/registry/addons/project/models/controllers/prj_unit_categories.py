from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPrjUnitCategories(ViewModelSearchController):
	_name = "search:prj.unit.categories"
	_view_name = "prj.unit.categories/search"
	_description = "Categories Project Unit"

class ViewModelFindPrjUnitCategories(ViewModelFindController):
	_name = "find:prj.unit.categories"
	_view_name = "prj.unit.categories/find"
	_description = "Categories Project Unit"

class ViewModelListPrjUnitCategories(ViewModelListController):
	_name = "list:prj.unit.categories"
	_view_name = "prj.unit.categories/list"
	_description = "Categories Project Unit"

class ViewModelFormModalPrjUnitCategories(ViewModelFormModalController):
	_name = "form.modal:prj.unit.categories"
	_view_name = "prj.unit.categories/form.modal"
	_description = "Categories Project Unit"

class ViewModelFormPrjUnitCategories(ViewModelFormController):
	_name = "form:prj.unit.categories"
	_view_name = "prj.unit.categories/form"
	_description = "Categories Project Unit"

class ViewModelTreePrjUnitCategories(ViewModelTreeController):
	_name = "tree:prj.unit.categories"
	_view_name = "prj.unit.categories/tree"
	_description = "Categories Project Unit"
