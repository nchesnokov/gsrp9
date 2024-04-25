from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMrpRequestTypes(ViewModelSearchController):
	_name = "search:mrp.request.types"
	_view_name = "mrp.request.types/search"
	_description = "Types MRP Request"

class ViewModelFindMrpRequestTypes(ViewModelFindController):
	_name = "find:mrp.request.types"
	_view_name = "mrp.request.types/find"
	_description = "Types MRP Request"

class ViewModelListMrpRequestTypes(ViewModelListController):
	_name = "list:mrp.request.types"
	_view_name = "mrp.request.types/list"
	_description = "Types MRP Request"

class ViewModelFormModalMrpRequestTypes(ViewModelFormModalController):
	_name = "form.modal:mrp.request.types"
	_view_name = "mrp.request.types/form.modal"
	_description = "Types MRP Request"

class ViewModelFormMrpRequestTypes(ViewModelFormController):
	_name = "form:mrp.request.types"
	_view_name = "mrp.request.types/form"
	_description = "Types MRP Request"
