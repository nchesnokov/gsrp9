from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmRequestTypes(ViewModelSearchController):
	_name = "search:srm.request.types"
	_view_name = "srm.request.types/search"
	_description = "Types SRM Request"

class ViewModelFindSrmRequestTypes(ViewModelFindController):
	_name = "find:srm.request.types"
	_view_name = "srm.request.types/find"
	_description = "Types SRM Request"

class ViewModelListSrmRequestTypes(ViewModelListController):
	_name = "list:srm.request.types"
	_view_name = "srm.request.types/list"
	_description = "Types SRM Request"

class ViewModelFormModalSrmRequestTypes(ViewModelFormModalController):
	_name = "form.modal:srm.request.types"
	_view_name = "srm.request.types/form.modal"
	_description = "Types SRM Request"

class ViewModelFormSrmRequestTypes(ViewModelFormController):
	_name = "form:srm.request.types"
	_view_name = "srm.request.types/form"
	_description = "Types SRM Request"
