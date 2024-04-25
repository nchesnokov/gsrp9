from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdCrmProduct(ViewModelFindController):
	_name = "find:md.crm.product"
	_view_name = "md.crm.product/find"
	_description = "CRM Of Product"

class ViewModelO2MFormMdCrmProduct(ViewModelO2MFormController):
	_name = "o2m-form:md.crm.product"
	_view_name = "md.crm.product/o2m-form"
	_description = "CRM Of Product"

class ViewModelO2MListMdCrmProduct(ViewModelO2MListController):
	_name = "o2m-list:md.crm.product"
	_view_name = "md.crm.product/o2m-list"
	_description = "CRM Of Product"
