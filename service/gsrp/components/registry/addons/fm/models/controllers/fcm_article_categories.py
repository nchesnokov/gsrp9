from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchFcmArticleCategories(ViewModelSearchController):
	_name = "search:fcm.article.categories"
	_view_name = "fcm.article.categories/search"
	_description = "FCM Article Category"

class ViewModelFindFcmArticleCategories(ViewModelFindController):
	_name = "find:fcm.article.categories"
	_view_name = "fcm.article.categories/find"
	_description = "FCM Article Category"

class ViewModelListFcmArticleCategories(ViewModelListController):
	_name = "list:fcm.article.categories"
	_view_name = "fcm.article.categories/list"
	_description = "FCM Article Category"

class ViewModelFormModalFcmArticleCategories(ViewModelFormModalController):
	_name = "form.modal:fcm.article.categories"
	_view_name = "fcm.article.categories/form.modal"
	_description = "FCM Article Category"

class ViewModelFormFcmArticleCategories(ViewModelFormController):
	_name = "form:fcm.article.categories"
	_view_name = "fcm.article.categories/form"
	_description = "FCM Article Category"

class ViewModelTreeFcmArticleCategories(ViewModelTreeController):
	_name = "tree:fcm.article.categories"
	_view_name = "fcm.article.categories/tree"
	_description = "FCM Article Category"
