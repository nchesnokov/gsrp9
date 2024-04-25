from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPartnerValidationProduct(ViewModelFindController):
	_name = "find:srm.partner.validation.product"
	_view_name = "srm.partner.validation.product/find"
	_description = "SRM Partner Validation Product"

class ViewModelO2MFormSrmPartnerValidationProduct(ViewModelO2MFormController):
	_name = "o2m-form:srm.partner.validation.product"
	_view_name = "srm.partner.validation.product/o2m-form"
	_description = "SRM Partner Validation Product"

class ViewModelO2MListSrmPartnerValidationProduct(ViewModelO2MListController):
	_name = "o2m-list:srm.partner.validation.product"
	_view_name = "srm.partner.validation.product/o2m-list"
	_description = "SRM Partner Validation Product"
