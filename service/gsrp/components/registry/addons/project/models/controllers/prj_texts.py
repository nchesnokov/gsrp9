from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPrjTexts(ViewModelSearchController):
	_name = "search:prj.texts"
	_view_name = "prj.texts/search"
	_description = "Project Texts"

class ViewModelFindPrjTexts(ViewModelFindController):
	_name = "find:prj.texts"
	_view_name = "prj.texts/find"
	_description = "Project Texts"

class ViewModelListPrjTexts(ViewModelListController):
	_name = "list:prj.texts"
	_view_name = "prj.texts/list"
	_description = "Project Texts"

class ViewModelFormModalPrjTexts(ViewModelFormModalController):
	_name = "form.modal:prj.texts"
	_view_name = "prj.texts/form.modal"
	_description = "Project Texts"

class ViewModelFormPrjTexts(ViewModelFormController):
	_name = "form:prj.texts"
	_view_name = "prj.texts/form"
	_description = "Project Texts"
