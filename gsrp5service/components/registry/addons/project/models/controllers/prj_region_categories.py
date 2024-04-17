from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPrjRegionCategories(ViewModelSearchController):
	_name = "search:prj.region.categories"
	_view_name = "prj.region.categories/search"
	_description = "Categories Project Region"

class ViewModelFindPrjRegionCategories(ViewModelFindController):
	_name = "find:prj.region.categories"
	_view_name = "prj.region.categories/find"
	_description = "Categories Project Region"

class ViewModelListPrjRegionCategories(ViewModelListController):
	_name = "list:prj.region.categories"
	_view_name = "prj.region.categories/list"
	_description = "Categories Project Region"

class ViewModelFormModalPrjRegionCategories(ViewModelFormModalController):
	_name = "form.modal:prj.region.categories"
	_view_name = "prj.region.categories/form.modal"
	_description = "Categories Project Region"

class ViewModelFormPrjRegionCategories(ViewModelFormController):
	_name = "form:prj.region.categories"
	_view_name = "prj.region.categories/form"
	_description = "Categories Project Region"

class ViewModelTreePrjRegionCategories(ViewModelTreeController):
	_name = "tree:prj.region.categories"
	_view_name = "prj.region.categories/tree"
	_description = "Categories Project Region"
