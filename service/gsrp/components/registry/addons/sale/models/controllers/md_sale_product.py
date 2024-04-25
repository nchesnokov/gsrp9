from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdSaleProduct(ViewModelFindController):
	_name = "find:md.sale.product"
	_view_name = "md.sale.product/find"
	_description = "Sale Of Product"

class ViewModelO2MFormMdSaleProduct(ViewModelO2MFormController):
	_name = "o2m-form:md.sale.product"
	_view_name = "md.sale.product/o2m-form"
	_description = "Sale Of Product"

class ViewModelO2MListMdSaleProduct(ViewModelO2MListController):
	_name = "o2m-list:md.sale.product"
	_view_name = "md.sale.product/o2m-list"
	_description = "Sale Of Product"
