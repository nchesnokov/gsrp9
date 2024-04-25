from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPrjDivisionCategories(ViewModelSearchController):
	_name = "search:prj.division.categories"
	_view_name = "prj.division.categories/search"
	_description = "Categories Project Division"

class ViewModelFindPrjDivisionCategories(ViewModelFindController):
	_name = "find:prj.division.categories"
	_view_name = "prj.division.categories/find"
	_description = "Categories Project Division"

class ViewModelListPrjDivisionCategories(ViewModelListController):
	_name = "list:prj.division.categories"
	_view_name = "prj.division.categories/list"
	_description = "Categories Project Division"

class ViewModelFormModalPrjDivisionCategories(ViewModelFormModalController):
	_name = "form.modal:prj.division.categories"
	_view_name = "prj.division.categories/form.modal"
	_description = "Categories Project Division"

class ViewModelFormPrjDivisionCategories(ViewModelFormController):
	_name = "form:prj.division.categories"
	_view_name = "prj.division.categories/form"
	_description = "Categories Project Division"

class ViewModelTreePrjDivisionCategories(ViewModelTreeController):
	_name = "tree:prj.division.categories"
	_view_name = "prj.division.categories/tree"
	_description = "Categories Project Division"
