from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchFmUnitCategories(ViewModelSearchController):
	_name = "search:fm.unit.categories"
	_view_name = "fm.unit.categories/search"
	_description = "Categories Financial Management Unit"

class ViewModelFindFmUnitCategories(ViewModelFindController):
	_name = "find:fm.unit.categories"
	_view_name = "fm.unit.categories/find"
	_description = "Categories Financial Management Unit"

class ViewModelListFmUnitCategories(ViewModelListController):
	_name = "list:fm.unit.categories"
	_view_name = "fm.unit.categories/list"
	_description = "Categories Financial Management Unit"

class ViewModelFormModalFmUnitCategories(ViewModelFormModalController):
	_name = "form.modal:fm.unit.categories"
	_view_name = "fm.unit.categories/form.modal"
	_description = "Categories Financial Management Unit"

class ViewModelFormFmUnitCategories(ViewModelFormController):
	_name = "form:fm.unit.categories"
	_view_name = "fm.unit.categories/form"
	_description = "Categories Financial Management Unit"

class ViewModelTreeFmUnitCategories(ViewModelTreeController):
	_name = "tree:fm.unit.categories"
	_view_name = "fm.unit.categories/tree"
	_description = "Categories Financial Management Unit"
