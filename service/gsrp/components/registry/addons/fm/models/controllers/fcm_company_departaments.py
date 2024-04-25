from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFcmCompanyDepartaments(ViewModelSearchController):
	_name = "search:fcm.company.departaments"
	_view_name = "fcm.company.departaments/search"
	_description = "FCM Departament Of Company"

class ViewModelFindFcmCompanyDepartaments(ViewModelFindController):
	_name = "find:fcm.company.departaments"
	_view_name = "fcm.company.departaments/find"
	_description = "FCM Departament Of Company"

class ViewModelListFcmCompanyDepartaments(ViewModelListController):
	_name = "list:fcm.company.departaments"
	_view_name = "fcm.company.departaments/list"
	_description = "FCM Departament Of Company"

class ViewModelFormModalFcmCompanyDepartaments(ViewModelFormModalController):
	_name = "form.modal:fcm.company.departaments"
	_view_name = "fcm.company.departaments/form.modal"
	_description = "FCM Departament Of Company"

class ViewModelFormFcmCompanyDepartaments(ViewModelFormController):
	_name = "form:fcm.company.departaments"
	_view_name = "fcm.company.departaments/form"
	_description = "FCM Departament Of Company"
