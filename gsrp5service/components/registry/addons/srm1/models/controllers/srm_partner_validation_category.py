from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPartnerValidationCategory(ViewModelFindController):
	_name = "find:srm.partner.validation.category"
	_view_name = "srm.partner.validation.category/find"
	_description = "SRM Partner Validation Category"

class ViewModelO2MFormSrmPartnerValidationCategory(ViewModelO2MFormController):
	_name = "o2m-form:srm.partner.validation.category"
	_view_name = "srm.partner.validation.category/o2m-form"
	_description = "SRM Partner Validation Category"

class ViewModelO2MListSrmPartnerValidationCategory(ViewModelO2MListController):
	_name = "o2m-list:srm.partner.validation.category"
	_view_name = "srm.partner.validation.category/o2m-list"
	_description = "SRM Partner Validation Category"
