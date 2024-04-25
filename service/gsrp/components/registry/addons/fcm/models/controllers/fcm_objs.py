from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFcmObjs(ViewModelSearchController):
	_name = "search:fcm.objs"
	_view_name = "fcm.objs/search"
	_description = "FCM Object"

class ViewModelFindFcmObjs(ViewModelFindController):
	_name = "find:fcm.objs"
	_view_name = "fcm.objs/find"
	_description = "FCM Object"

class ViewModelListFcmObjs(ViewModelListController):
	_name = "list:fcm.objs"
	_view_name = "fcm.objs/list"
	_description = "FCM Object"

class ViewModelFormModalFcmObjs(ViewModelFormModalController):
	_name = "form.modal:fcm.objs"
	_view_name = "fcm.objs/form.modal"
	_description = "FCM Object"

class ViewModelFormFcmObjs(ViewModelFormController):
	_name = "form:fcm.objs"
	_view_name = "fcm.objs/form"
	_description = "FCM Object"
