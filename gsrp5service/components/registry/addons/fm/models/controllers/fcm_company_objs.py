from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFcmCompanyObjs(ViewModelSearchController):
	_name = "search:fcm.company.objs"
	_view_name = "fcm.company.objs/search"
	_description = "FCM Object Of Company"

class ViewModelFindFcmCompanyObjs(ViewModelFindController):
	_name = "find:fcm.company.objs"
	_view_name = "fcm.company.objs/find"
	_description = "FCM Object Of Company"

class ViewModelListFcmCompanyObjs(ViewModelListController):
	_name = "list:fcm.company.objs"
	_view_name = "fcm.company.objs/list"
	_description = "FCM Object Of Company"

class ViewModelFormModalFcmCompanyObjs(ViewModelFormModalController):
	_name = "form.modal:fcm.company.objs"
	_view_name = "fcm.company.objs/form.modal"
	_description = "FCM Object Of Company"

class ViewModelFormFcmCompanyObjs(ViewModelFormController):
	_name = "form:fcm.company.objs"
	_view_name = "fcm.company.objs/form"
	_description = "FCM Object Of Company"
