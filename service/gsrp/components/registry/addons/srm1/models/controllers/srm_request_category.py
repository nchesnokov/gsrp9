from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSrmRequestCategory(ViewModelSearchController):
	_name = "search:srm.request.category"
	_view_name = "srm.request.category/search"
	_description = "Category SRM Request"

class ViewModelFindSrmRequestCategory(ViewModelFindController):
	_name = "find:srm.request.category"
	_view_name = "srm.request.category/find"
	_description = "Category SRM Request"

class ViewModelListSrmRequestCategory(ViewModelListController):
	_name = "list:srm.request.category"
	_view_name = "srm.request.category/list"
	_description = "Category SRM Request"

class ViewModelFormModalSrmRequestCategory(ViewModelFormModalController):
	_name = "form.modal:srm.request.category"
	_view_name = "srm.request.category/form.modal"
	_description = "Category SRM Request"

class ViewModelFormSrmRequestCategory(ViewModelFormController):
	_name = "form:srm.request.category"
	_view_name = "srm.request.category/form"
	_description = "Category SRM Request"

class ViewModelTreeSrmRequestCategory(ViewModelTreeController):
	_name = "tree:srm.request.category"
	_view_name = "srm.request.category/tree"
	_description = "Category SRM Request"
