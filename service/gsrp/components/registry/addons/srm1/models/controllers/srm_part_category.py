from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSrmPartCategory(ViewModelSearchController):
	_name = "search:srm.part.category"
	_view_name = "srm.part.category/search"
	_description = "Category SRM Part"

class ViewModelFindSrmPartCategory(ViewModelFindController):
	_name = "find:srm.part.category"
	_view_name = "srm.part.category/find"
	_description = "Category SRM Part"

class ViewModelListSrmPartCategory(ViewModelListController):
	_name = "list:srm.part.category"
	_view_name = "srm.part.category/list"
	_description = "Category SRM Part"

class ViewModelFormModalSrmPartCategory(ViewModelFormModalController):
	_name = "form.modal:srm.part.category"
	_view_name = "srm.part.category/form.modal"
	_description = "Category SRM Part"

class ViewModelFormSrmPartCategory(ViewModelFormController):
	_name = "form:srm.part.category"
	_view_name = "srm.part.category/form"
	_description = "Category SRM Part"

class ViewModelTreeSrmPartCategory(ViewModelTreeController):
	_name = "tree:srm.part.category"
	_view_name = "srm.part.category/tree"
	_description = "Category SRM Part"
