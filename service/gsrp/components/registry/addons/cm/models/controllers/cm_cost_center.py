from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCmCostCenter(ViewModelSearchController):
	_name = "search:cm.cost.center"
	_view_name = "cm.cost.center/search"
	_description = "Cost Center"

class ViewModelFindCmCostCenter(ViewModelFindController):
	_name = "find:cm.cost.center"
	_view_name = "cm.cost.center/find"
	_description = "Cost Center"

class ViewModelListCmCostCenter(ViewModelListController):
	_name = "list:cm.cost.center"
	_view_name = "cm.cost.center/list"
	_description = "Cost Center"

class ViewModelFormModalCmCostCenter(ViewModelFormModalController):
	_name = "form.modal:cm.cost.center"
	_view_name = "cm.cost.center/form.modal"
	_description = "Cost Center"

class ViewModelFormCmCostCenter(ViewModelFormController):
	_name = "form:cm.cost.center"
	_view_name = "cm.cost.center/form"
	_description = "Cost Center"
