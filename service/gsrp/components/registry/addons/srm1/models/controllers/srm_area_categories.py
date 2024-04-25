from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSrmAreaCategories(ViewModelSearchController):
	_name = "search:srm.area.categories"
	_view_name = "srm.area.categories/search"
	_description = "Categories SRM Area"

class ViewModelFindSrmAreaCategories(ViewModelFindController):
	_name = "find:srm.area.categories"
	_view_name = "srm.area.categories/find"
	_description = "Categories SRM Area"

class ViewModelListSrmAreaCategories(ViewModelListController):
	_name = "list:srm.area.categories"
	_view_name = "srm.area.categories/list"
	_description = "Categories SRM Area"

class ViewModelFormModalSrmAreaCategories(ViewModelFormModalController):
	_name = "form.modal:srm.area.categories"
	_view_name = "srm.area.categories/form.modal"
	_description = "Categories SRM Area"

class ViewModelFormSrmAreaCategories(ViewModelFormController):
	_name = "form:srm.area.categories"
	_view_name = "srm.area.categories/form"
	_description = "Categories SRM Area"

class ViewModelTreeSrmAreaCategories(ViewModelTreeController):
	_name = "tree:srm.area.categories"
	_view_name = "srm.area.categories/tree"
	_description = "Categories SRM Area"
