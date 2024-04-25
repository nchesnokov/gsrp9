from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmPartnerValidation(ViewModelSearchController):
	_name = "search:srm.partner.validation"
	_view_name = "srm.partner.validation/search"
	_description = "SRM Partner Validation"

class ViewModelFindSrmPartnerValidation(ViewModelFindController):
	_name = "find:srm.partner.validation"
	_view_name = "srm.partner.validation/find"
	_description = "SRM Partner Validation"

class ViewModelListSrmPartnerValidation(ViewModelListController):
	_name = "list:srm.partner.validation"
	_view_name = "srm.partner.validation/list"
	_description = "SRM Partner Validation"

class ViewModelFormModalSrmPartnerValidation(ViewModelFormModalController):
	_name = "form.modal:srm.partner.validation"
	_view_name = "srm.partner.validation/form.modal"
	_description = "SRM Partner Validation"

class ViewModelFormSrmPartnerValidation(ViewModelFormController):
	_name = "form:srm.partner.validation"
	_view_name = "srm.partner.validation/form"
	_description = "SRM Partner Validation"
