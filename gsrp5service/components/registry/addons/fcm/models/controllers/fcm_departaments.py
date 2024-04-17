from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFcmDepartaments(ViewModelSearchController):
	_name = "search:fcm.departaments"
	_view_name = "fcm.departaments/search"
	_description = "FCM Departament"

class ViewModelFindFcmDepartaments(ViewModelFindController):
	_name = "find:fcm.departaments"
	_view_name = "fcm.departaments/find"
	_description = "FCM Departament"

class ViewModelListFcmDepartaments(ViewModelListController):
	_name = "list:fcm.departaments"
	_view_name = "fcm.departaments/list"
	_description = "FCM Departament"

class ViewModelFormModalFcmDepartaments(ViewModelFormModalController):
	_name = "form.modal:fcm.departaments"
	_view_name = "fcm.departaments/form.modal"
	_description = "FCM Departament"

class ViewModelFormFcmDepartaments(ViewModelFormController):
	_name = "form:fcm.departaments"
	_view_name = "fcm.departaments/form"
	_description = "FCM Departament"
