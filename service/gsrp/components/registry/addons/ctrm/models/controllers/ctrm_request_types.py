from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCtrmRequestTypes(ViewModelSearchController):
	_name = "search:ctrm.request.types"
	_view_name = "ctrm.request.types/search"
	_description = "Types CTRM Request"

class ViewModelFindCtrmRequestTypes(ViewModelFindController):
	_name = "find:ctrm.request.types"
	_view_name = "ctrm.request.types/find"
	_description = "Types CTRM Request"

class ViewModelListCtrmRequestTypes(ViewModelListController):
	_name = "list:ctrm.request.types"
	_view_name = "ctrm.request.types/list"
	_description = "Types CTRM Request"

class ViewModelFormModalCtrmRequestTypes(ViewModelFormModalController):
	_name = "form.modal:ctrm.request.types"
	_view_name = "ctrm.request.types/form.modal"
	_description = "Types CTRM Request"

class ViewModelFormCtrmRequestTypes(ViewModelFormController):
	_name = "form:ctrm.request.types"
	_view_name = "ctrm.request.types/form"
	_description = "Types CTRM Request"
