from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSrmRegionCategories(ViewModelSearchController):
	_name = "search:srm.region.categories"
	_view_name = "srm.region.categories/search"
	_description = "Categories SRM Region"

class ViewModelFindSrmRegionCategories(ViewModelFindController):
	_name = "find:srm.region.categories"
	_view_name = "srm.region.categories/find"
	_description = "Categories SRM Region"

class ViewModelListSrmRegionCategories(ViewModelListController):
	_name = "list:srm.region.categories"
	_view_name = "srm.region.categories/list"
	_description = "Categories SRM Region"

class ViewModelFormModalSrmRegionCategories(ViewModelFormModalController):
	_name = "form.modal:srm.region.categories"
	_view_name = "srm.region.categories/form.modal"
	_description = "Categories SRM Region"

class ViewModelFormSrmRegionCategories(ViewModelFormController):
	_name = "form:srm.region.categories"
	_view_name = "srm.region.categories/form"
	_description = "Categories SRM Region"

class ViewModelTreeSrmRegionCategories(ViewModelTreeController):
	_name = "tree:srm.region.categories"
	_view_name = "srm.region.categories/tree"
	_description = "Categories SRM Region"
