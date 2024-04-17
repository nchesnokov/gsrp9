from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchFcmObjCategories(ViewModelSearchController):
	_name = "search:fcm.obj.categories"
	_view_name = "fcm.obj.categories/search"
	_description = "FCM Object Category"

class ViewModelFindFcmObjCategories(ViewModelFindController):
	_name = "find:fcm.obj.categories"
	_view_name = "fcm.obj.categories/find"
	_description = "FCM Object Category"

class ViewModelListFcmObjCategories(ViewModelListController):
	_name = "list:fcm.obj.categories"
	_view_name = "fcm.obj.categories/list"
	_description = "FCM Object Category"

class ViewModelFormModalFcmObjCategories(ViewModelFormModalController):
	_name = "form.modal:fcm.obj.categories"
	_view_name = "fcm.obj.categories/form.modal"
	_description = "FCM Object Category"

class ViewModelFormFcmObjCategories(ViewModelFormController):
	_name = "form:fcm.obj.categories"
	_view_name = "fcm.obj.categories/form"
	_description = "FCM Object Category"

class ViewModelTreeFcmObjCategories(ViewModelTreeController):
	_name = "tree:fcm.obj.categories"
	_view_name = "fcm.obj.categories/tree"
	_description = "FCM Object Category"
