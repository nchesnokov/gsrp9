from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmResponseTypes(ViewModelSearchController):
	_name = "search:srm.response.types"
	_view_name = "srm.response.types/search"
	_description = "Types SRM Response"

class ViewModelFindSrmResponseTypes(ViewModelFindController):
	_name = "find:srm.response.types"
	_view_name = "srm.response.types/find"
	_description = "Types SRM Response"

class ViewModelListSrmResponseTypes(ViewModelListController):
	_name = "list:srm.response.types"
	_view_name = "srm.response.types/list"
	_description = "Types SRM Response"

class ViewModelFormModalSrmResponseTypes(ViewModelFormModalController):
	_name = "form.modal:srm.response.types"
	_view_name = "srm.response.types/form.modal"
	_description = "Types SRM Response"

class ViewModelFormSrmResponseTypes(ViewModelFormController):
	_name = "form:srm.response.types"
	_view_name = "srm.response.types/form"
	_description = "Types SRM Response"
