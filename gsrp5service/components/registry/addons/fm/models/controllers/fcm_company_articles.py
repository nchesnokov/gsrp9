from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFcmCompanyArticles(ViewModelSearchController):
	_name = "search:fcm.company.articles"
	_view_name = "fcm.company.articles/search"
	_description = "FCM Article Of Company"

class ViewModelFindFcmCompanyArticles(ViewModelFindController):
	_name = "find:fcm.company.articles"
	_view_name = "fcm.company.articles/find"
	_description = "FCM Article Of Company"

class ViewModelListFcmCompanyArticles(ViewModelListController):
	_name = "list:fcm.company.articles"
	_view_name = "fcm.company.articles/list"
	_description = "FCM Article Of Company"

class ViewModelFormModalFcmCompanyArticles(ViewModelFormModalController):
	_name = "form.modal:fcm.company.articles"
	_view_name = "fcm.company.articles/form.modal"
	_description = "FCM Article Of Company"

class ViewModelFormFcmCompanyArticles(ViewModelFormController):
	_name = "form:fcm.company.articles"
	_view_name = "fcm.company.articles/form"
	_description = "FCM Article Of Company"
