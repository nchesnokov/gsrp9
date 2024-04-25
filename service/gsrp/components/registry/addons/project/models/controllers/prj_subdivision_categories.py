from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPrjSubdivisionCategories(ViewModelSearchController):
	_name = "search:prj.subdivision.categories"
	_view_name = "prj.subdivision.categories/search"
	_description = "Categories Project Subdivision"

class ViewModelFindPrjSubdivisionCategories(ViewModelFindController):
	_name = "find:prj.subdivision.categories"
	_view_name = "prj.subdivision.categories/find"
	_description = "Categories Project Subdivision"

class ViewModelListPrjSubdivisionCategories(ViewModelListController):
	_name = "list:prj.subdivision.categories"
	_view_name = "prj.subdivision.categories/list"
	_description = "Categories Project Subdivision"

class ViewModelFormModalPrjSubdivisionCategories(ViewModelFormModalController):
	_name = "form.modal:prj.subdivision.categories"
	_view_name = "prj.subdivision.categories/form.modal"
	_description = "Categories Project Subdivision"

class ViewModelFormPrjSubdivisionCategories(ViewModelFormController):
	_name = "form:prj.subdivision.categories"
	_view_name = "prj.subdivision.categories/form"
	_description = "Categories Project Subdivision"

class ViewModelTreePrjSubdivisionCategories(ViewModelTreeController):
	_name = "tree:prj.subdivision.categories"
	_view_name = "prj.subdivision.categories/tree"
	_description = "Categories Project Subdivision"
