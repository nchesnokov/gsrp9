from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdMrpProduct(ViewModelFindController):
	_name = "find:md.mrp.product"
	_view_name = "md.mrp.product/find"
	_description = "Mrp Of Product"

class ViewModelO2MFormMdMrpProduct(ViewModelO2MFormController):
	_name = "o2m-form:md.mrp.product"
	_view_name = "md.mrp.product/o2m-form"
	_description = "Mrp Of Product"

class ViewModelO2MListMdMrpProduct(ViewModelO2MListController):
	_name = "o2m-list:md.mrp.product"
	_view_name = "md.mrp.product/o2m-list"
	_description = "Mrp Of Product"
