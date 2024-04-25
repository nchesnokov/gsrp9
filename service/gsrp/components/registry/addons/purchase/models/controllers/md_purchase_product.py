from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdPurchaseProduct(ViewModelFindController):
	_name = "find:md.purchase.product"
	_view_name = "md.purchase.product/find"
	_description = "Purchase Of Product"

class ViewModelO2MFormMdPurchaseProduct(ViewModelO2MFormController):
	_name = "o2m-form:md.purchase.product"
	_view_name = "md.purchase.product/o2m-form"
	_description = "Purchase Of Product"

class ViewModelO2MListMdPurchaseProduct(ViewModelO2MListController):
	_name = "o2m-list:md.purchase.product"
	_view_name = "md.purchase.product/o2m-list"
	_description = "Purchase Of Product"
