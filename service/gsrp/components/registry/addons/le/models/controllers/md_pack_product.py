from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdPackProduct(ViewModelFindController):
	_name = "find:md.pack.product"
	_view_name = "md.pack.product/find"
	_description = "Pack Of Product"

class ViewModelO2MFormMdPackProduct(ViewModelO2MFormController):
	_name = "o2m-form:md.pack.product"
	_view_name = "md.pack.product/o2m-form"
	_description = "Pack Of Product"

class ViewModelO2MListMdPackProduct(ViewModelO2MListController):
	_name = "o2m-list:md.pack.product"
	_view_name = "md.pack.product/o2m-list"
	_description = "Pack Of Product"
