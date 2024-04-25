from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdTmProduct(ViewModelFindController):
	_name = "find:md.tm.product"
	_view_name = "md.tm.product/find"
	_description = "TM Of Product"

class ViewModelO2MFormMdTmProduct(ViewModelO2MFormController):
	_name = "o2m-form:md.tm.product"
	_view_name = "md.tm.product/o2m-form"
	_description = "TM Of Product"

class ViewModelO2MListMdTmProduct(ViewModelO2MListController):
	_name = "o2m-list:md.tm.product"
	_view_name = "md.tm.product/o2m-list"
	_description = "TM Of Product"
