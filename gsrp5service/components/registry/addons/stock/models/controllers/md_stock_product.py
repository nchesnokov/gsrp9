from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdStockProduct(ViewModelFindController):
	_name = "find:md.stock.product"
	_view_name = "md.stock.product/find"
	_description = "Stock Of Product"

class ViewModelO2MFormMdStockProduct(ViewModelO2MFormController):
	_name = "o2m-form:md.stock.product"
	_view_name = "md.stock.product/o2m-form"
	_description = "Stock Of Product"

class ViewModelO2MListMdStockProduct(ViewModelO2MListController):
	_name = "o2m-list:md.stock.product"
	_view_name = "md.stock.product/o2m-list"
	_description = "Stock Of Product"
