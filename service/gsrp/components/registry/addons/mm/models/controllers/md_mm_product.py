from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdMmProduct(ViewModelFindController):
	_name = "find:md.mm.product"
	_view_name = "md.mm.product/find"
	_description = "Production Of Product"

class ViewModelO2MFormMdMmProduct(ViewModelO2MFormController):
	_name = "o2m-form:md.mm.product"
	_view_name = "md.mm.product/o2m-form"
	_description = "Production Of Product"

class ViewModelO2MListMdMmProduct(ViewModelO2MListController):
	_name = "o2m-list:md.mm.product"
	_view_name = "md.mm.product/o2m-list"
	_description = "Production Of Product"
