from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSrmSubdivisionCategories(ViewModelSearchController):
	_name = "search:srm.subdivision.categories"
	_view_name = "srm.subdivision.categories/search"
	_description = "Categories SRM Subdivision"

class ViewModelFindSrmSubdivisionCategories(ViewModelFindController):
	_name = "find:srm.subdivision.categories"
	_view_name = "srm.subdivision.categories/find"
	_description = "Categories SRM Subdivision"

class ViewModelListSrmSubdivisionCategories(ViewModelListController):
	_name = "list:srm.subdivision.categories"
	_view_name = "srm.subdivision.categories/list"
	_description = "Categories SRM Subdivision"

class ViewModelFormModalSrmSubdivisionCategories(ViewModelFormModalController):
	_name = "form.modal:srm.subdivision.categories"
	_view_name = "srm.subdivision.categories/form.modal"
	_description = "Categories SRM Subdivision"

class ViewModelFormSrmSubdivisionCategories(ViewModelFormController):
	_name = "form:srm.subdivision.categories"
	_view_name = "srm.subdivision.categories/form"
	_description = "Categories SRM Subdivision"

class ViewModelTreeSrmSubdivisionCategories(ViewModelTreeController):
	_name = "tree:srm.subdivision.categories"
	_view_name = "srm.subdivision.categories/tree"
	_description = "Categories SRM Subdivision"
