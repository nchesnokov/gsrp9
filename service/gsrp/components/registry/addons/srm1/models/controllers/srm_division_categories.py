from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSrmDivisionCategories(ViewModelSearchController):
	_name = "search:srm.division.categories"
	_view_name = "srm.division.categories/search"
	_description = "Categories SRM Division"

class ViewModelFindSrmDivisionCategories(ViewModelFindController):
	_name = "find:srm.division.categories"
	_view_name = "srm.division.categories/find"
	_description = "Categories SRM Division"

class ViewModelListSrmDivisionCategories(ViewModelListController):
	_name = "list:srm.division.categories"
	_view_name = "srm.division.categories/list"
	_description = "Categories SRM Division"

class ViewModelFormModalSrmDivisionCategories(ViewModelFormModalController):
	_name = "form.modal:srm.division.categories"
	_view_name = "srm.division.categories/form.modal"
	_description = "Categories SRM Division"

class ViewModelFormSrmDivisionCategories(ViewModelFormController):
	_name = "form:srm.division.categories"
	_view_name = "srm.division.categories/form"
	_description = "Categories SRM Division"

class ViewModelTreeSrmDivisionCategories(ViewModelTreeController):
	_name = "tree:srm.division.categories"
	_view_name = "srm.division.categories/tree"
	_description = "Categories SRM Division"
