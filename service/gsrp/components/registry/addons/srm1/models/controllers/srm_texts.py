from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmTexts(ViewModelSearchController):
	_name = "search:srm.texts"
	_view_name = "srm.texts/search"
	_description = "SRM Texts"

class ViewModelFindSrmTexts(ViewModelFindController):
	_name = "find:srm.texts"
	_view_name = "srm.texts/find"
	_description = "SRM Texts"

class ViewModelListSrmTexts(ViewModelListController):
	_name = "list:srm.texts"
	_view_name = "srm.texts/list"
	_description = "SRM Texts"

class ViewModelFormModalSrmTexts(ViewModelFormModalController):
	_name = "form.modal:srm.texts"
	_view_name = "srm.texts/form.modal"
	_description = "SRM Texts"

class ViewModelFormSrmTexts(ViewModelFormController):
	_name = "form:srm.texts"
	_view_name = "srm.texts/form"
	_description = "SRM Texts"
