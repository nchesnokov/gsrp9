from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdEwmProduct(ViewModelFindController):
	_name = "find:md.ewm.product"
	_view_name = "md.ewm.product/find"
	_description = "Stock Of Product"

class ViewModelO2MFormMdEwmProduct(ViewModelO2MFormController):
	_name = "o2m-form:md.ewm.product"
	_view_name = "md.ewm.product/o2m-form"
	_description = "Stock Of Product"

class ViewModelO2MListMdEwmProduct(ViewModelO2MListController):
	_name = "o2m-list:md.ewm.product"
	_view_name = "md.ewm.product/o2m-list"
	_description = "Stock Of Product"
