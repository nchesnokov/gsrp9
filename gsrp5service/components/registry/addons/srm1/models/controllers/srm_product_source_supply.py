from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmProductSourceSupply(ViewModelSearchController):
	_name = "search:srm.product.source.supply"
	_view_name = "srm.product.source.supply/search"
	_description = "SRM Partner Source Of Supply"

class ViewModelFindSrmProductSourceSupply(ViewModelFindController):
	_name = "find:srm.product.source.supply"
	_view_name = "srm.product.source.supply/find"
	_description = "SRM Partner Source Of Supply"

class ViewModelListSrmProductSourceSupply(ViewModelListController):
	_name = "list:srm.product.source.supply"
	_view_name = "srm.product.source.supply/list"
	_description = "SRM Partner Source Of Supply"

class ViewModelFormModalSrmProductSourceSupply(ViewModelFormModalController):
	_name = "form.modal:srm.product.source.supply"
	_view_name = "srm.product.source.supply/form.modal"
	_description = "SRM Partner Source Of Supply"

class ViewModelFormSrmProductSourceSupply(ViewModelFormController):
	_name = "form:srm.product.source.supply"
	_view_name = "srm.product.source.supply/form"
	_description = "SRM Partner Source Of Supply"
