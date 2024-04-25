from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSaleOrderTypes(ViewModelSearchController):
	_name = "search:sale.order.types"
	_view_name = "sale.order.types/search"
	_description = "Types Sale Order"

class ViewModelFindSaleOrderTypes(ViewModelFindController):
	_name = "find:sale.order.types"
	_view_name = "sale.order.types/find"
	_description = "Types Sale Order"

class ViewModelListSaleOrderTypes(ViewModelListController):
	_name = "list:sale.order.types"
	_view_name = "sale.order.types/list"
	_description = "Types Sale Order"

class ViewModelFormModalSaleOrderTypes(ViewModelFormModalController):
	_name = "form.modal:sale.order.types"
	_view_name = "sale.order.types/form.modal"
	_description = "Types Sale Order"

class ViewModelFormSaleOrderTypes(ViewModelFormController):
	_name = "form:sale.order.types"
	_view_name = "sale.order.types/form"
	_description = "Types Sale Order"
