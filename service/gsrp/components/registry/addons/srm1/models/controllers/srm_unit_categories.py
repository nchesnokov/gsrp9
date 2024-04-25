from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSrmUnitCategories(ViewModelSearchController):
	_name = "search:srm.unit.categories"
	_view_name = "srm.unit.categories/search"
	_description = "Categories SRM Unit"

class ViewModelFindSrmUnitCategories(ViewModelFindController):
	_name = "find:srm.unit.categories"
	_view_name = "srm.unit.categories/find"
	_description = "Categories SRM Unit"

class ViewModelListSrmUnitCategories(ViewModelListController):
	_name = "list:srm.unit.categories"
	_view_name = "srm.unit.categories/list"
	_description = "Categories SRM Unit"

class ViewModelFormModalSrmUnitCategories(ViewModelFormModalController):
	_name = "form.modal:srm.unit.categories"
	_view_name = "srm.unit.categories/form.modal"
	_description = "Categories SRM Unit"

class ViewModelFormSrmUnitCategories(ViewModelFormController):
	_name = "form:srm.unit.categories"
	_view_name = "srm.unit.categories/form"
	_description = "Categories SRM Unit"

class ViewModelTreeSrmUnitCategories(ViewModelTreeController):
	_name = "tree:srm.unit.categories"
	_view_name = "srm.unit.categories/tree"
	_description = "Categories SRM Unit"
