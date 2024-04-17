from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchMrpRequestCategory(ViewModelSearchController):
	_name = "search:mrp.request.category"
	_view_name = "mrp.request.category/search"
	_description = "Category MRP Request"

class ViewModelFindMrpRequestCategory(ViewModelFindController):
	_name = "find:mrp.request.category"
	_view_name = "mrp.request.category/find"
	_description = "Category MRP Request"

class ViewModelListMrpRequestCategory(ViewModelListController):
	_name = "list:mrp.request.category"
	_view_name = "mrp.request.category/list"
	_description = "Category MRP Request"

class ViewModelFormModalMrpRequestCategory(ViewModelFormModalController):
	_name = "form.modal:mrp.request.category"
	_view_name = "mrp.request.category/form.modal"
	_description = "Category MRP Request"

class ViewModelFormMrpRequestCategory(ViewModelFormController):
	_name = "form:mrp.request.category"
	_view_name = "mrp.request.category/form"
	_description = "Category MRP Request"

class ViewModelTreeMrpRequestCategory(ViewModelTreeController):
	_name = "tree:mrp.request.category"
	_view_name = "mrp.request.category/tree"
	_description = "Category MRP Request"
