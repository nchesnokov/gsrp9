from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFcmArticles(ViewModelSearchController):
	_name = "search:fcm.articles"
	_view_name = "fcm.articles/search"
	_description = "FCM Article"

class ViewModelFindFcmArticles(ViewModelFindController):
	_name = "find:fcm.articles"
	_view_name = "fcm.articles/find"
	_description = "FCM Article"

class ViewModelListFcmArticles(ViewModelListController):
	_name = "list:fcm.articles"
	_view_name = "fcm.articles/list"
	_description = "FCM Article"

class ViewModelFormModalFcmArticles(ViewModelFormModalController):
	_name = "form.modal:fcm.articles"
	_view_name = "fcm.articles/form.modal"
	_description = "FCM Article"

class ViewModelFormFcmArticles(ViewModelFormController):
	_name = "form:fcm.articles"
	_view_name = "fcm.articles/form"
	_description = "FCM Article"
