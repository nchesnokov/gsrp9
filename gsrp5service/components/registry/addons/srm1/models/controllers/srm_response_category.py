from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSrmResponseCategory(ViewModelSearchController):
	_name = "search:srm.response.category"
	_view_name = "srm.response.category/search"
	_description = "Category SRM Response"

class ViewModelFindSrmResponseCategory(ViewModelFindController):
	_name = "find:srm.response.category"
	_view_name = "srm.response.category/find"
	_description = "Category SRM Response"

class ViewModelListSrmResponseCategory(ViewModelListController):
	_name = "list:srm.response.category"
	_view_name = "srm.response.category/list"
	_description = "Category SRM Response"

class ViewModelFormModalSrmResponseCategory(ViewModelFormModalController):
	_name = "form.modal:srm.response.category"
	_view_name = "srm.response.category/form.modal"
	_description = "Category SRM Response"

class ViewModelFormSrmResponseCategory(ViewModelFormController):
	_name = "form:srm.response.category"
	_view_name = "srm.response.category/form"
	_description = "Category SRM Response"

class ViewModelTreeSrmResponseCategory(ViewModelTreeController):
	_name = "tree:srm.response.category"
	_view_name = "srm.response.category/tree"
	_description = "Category SRM Response"
