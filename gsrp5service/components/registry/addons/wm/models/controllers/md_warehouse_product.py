from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdWarehouseProduct(ViewModelFindController):
	_name = "find:md.warehouse.product"
	_view_name = "md.warehouse.product/find"
	_description = "Warehouse Of Product"

class ViewModelO2MFormMdWarehouseProduct(ViewModelO2MFormController):
	_name = "o2m-form:md.warehouse.product"
	_view_name = "md.warehouse.product/o2m-form"
	_description = "Warehouse Of Product"

class ViewModelO2MListMdWarehouseProduct(ViewModelO2MListController):
	_name = "o2m-list:md.warehouse.product"
	_view_name = "md.warehouse.product/o2m-list"
	_description = "Warehouse Of Product"
