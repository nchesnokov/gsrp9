from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchMdCategoryLocation(ViewModelSearchController):
	_name = "search:md.category.location"
	_view_name = "md.category.location/search"
	_description = "Category Location"

class ViewModelFindMdCategoryLocation(ViewModelFindController):
	_name = "find:md.category.location"
	_view_name = "md.category.location/find"
	_description = "Category Location"

class ViewModelListMdCategoryLocation(ViewModelListController):
	_name = "list:md.category.location"
	_view_name = "md.category.location/list"
	_description = "Category Location"

class ViewModelFormModalMdCategoryLocation(ViewModelFormModalController):
	_name = "form.modal:md.category.location"
	_view_name = "md.category.location/form.modal"
	_description = "Category Location"

class ViewModelFormMdCategoryLocation(ViewModelFormController):
	_name = "form:md.category.location"
	_view_name = "md.category.location/form"
	_description = "Category Location"

class ViewModelTreeMdCategoryLocation(ViewModelTreeController):
	_name = "tree:md.category.location"
	_view_name = "md.category.location/tree"
	_description = "Category Location"
