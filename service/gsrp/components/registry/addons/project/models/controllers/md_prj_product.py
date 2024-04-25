from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdPrjProduct(ViewModelFindController):
	_name = "find:md.prj.product"
	_view_name = "md.prj.product/find"
	_description = "Project Of Product"

class ViewModelO2MFormMdPrjProduct(ViewModelO2MFormController):
	_name = "o2m-form:md.prj.product"
	_view_name = "md.prj.product/o2m-form"
	_description = "Project Of Product"

class ViewModelO2MListMdPrjProduct(ViewModelO2MListController):
	_name = "o2m-list:md.prj.product"
	_view_name = "md.prj.product/o2m-list"
	_description = "Project Of Product"
