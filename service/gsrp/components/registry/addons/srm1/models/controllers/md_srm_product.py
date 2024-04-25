from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdSrmProduct(ViewModelFindController):
	_name = "find:md.srm.product"
	_view_name = "md.srm.product/find"
	_description = "SRM Of Product"

class ViewModelO2MFormMdSrmProduct(ViewModelO2MFormController):
	_name = "o2m-form:md.srm.product"
	_view_name = "md.srm.product/o2m-form"
	_description = "SRM Of Product"

class ViewModelO2MListMdSrmProduct(ViewModelO2MListController):
	_name = "o2m-list:md.srm.product"
	_view_name = "md.srm.product/o2m-list"
	_description = "SRM Of Product"
