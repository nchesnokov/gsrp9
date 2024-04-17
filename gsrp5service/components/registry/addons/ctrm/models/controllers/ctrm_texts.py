from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCtrmTexts(ViewModelSearchController):
	_name = "search:ctrm.texts"
	_view_name = "ctrm.texts/search"
	_description = "CTRM Texts"

class ViewModelFindCtrmTexts(ViewModelFindController):
	_name = "find:ctrm.texts"
	_view_name = "ctrm.texts/find"
	_description = "CTRM Texts"

class ViewModelListCtrmTexts(ViewModelListController):
	_name = "list:ctrm.texts"
	_view_name = "ctrm.texts/list"
	_description = "CTRM Texts"

class ViewModelFormModalCtrmTexts(ViewModelFormModalController):
	_name = "form.modal:ctrm.texts"
	_view_name = "ctrm.texts/form.modal"
	_description = "CTRM Texts"

class ViewModelFormCtrmTexts(ViewModelFormController):
	_name = "form:ctrm.texts"
	_view_name = "ctrm.texts/form"
	_description = "CTRM Texts"
