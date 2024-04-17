from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchFcmDepartamentCategories(ViewModelSearchController):
	_name = "search:fcm.departament.categories"
	_view_name = "fcm.departament.categories/search"
	_description = "FCM Departament Category"

class ViewModelFindFcmDepartamentCategories(ViewModelFindController):
	_name = "find:fcm.departament.categories"
	_view_name = "fcm.departament.categories/find"
	_description = "FCM Departament Category"

class ViewModelListFcmDepartamentCategories(ViewModelListController):
	_name = "list:fcm.departament.categories"
	_view_name = "fcm.departament.categories/list"
	_description = "FCM Departament Category"

class ViewModelFormModalFcmDepartamentCategories(ViewModelFormModalController):
	_name = "form.modal:fcm.departament.categories"
	_view_name = "fcm.departament.categories/form.modal"
	_description = "FCM Departament Category"

class ViewModelFormFcmDepartamentCategories(ViewModelFormController):
	_name = "form:fcm.departament.categories"
	_view_name = "fcm.departament.categories/form"
	_description = "FCM Departament Category"

class ViewModelTreeFcmDepartamentCategories(ViewModelTreeController):
	_name = "tree:fcm.departament.categories"
	_view_name = "fcm.departament.categories/tree"
	_description = "FCM Departament Category"
