from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdCostProduct(ViewModelFindController):
	_name = "find:md.cost.product"
	_view_name = "md.cost.product/find"
	_description = "Cost Of Product"

class ViewModelO2MFormMdCostProduct(ViewModelO2MFormController):
	_name = "o2m-form:md.cost.product"
	_view_name = "md.cost.product/o2m-form"
	_description = "Cost Of Product"

class ViewModelO2MListMdCostProduct(ViewModelO2MListController):
	_name = "o2m-list:md.cost.product"
	_view_name = "md.cost.product/o2m-list"
	_description = "Cost Of Product"
