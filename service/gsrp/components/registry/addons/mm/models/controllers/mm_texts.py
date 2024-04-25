from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMmTexts(ViewModelSearchController):
	_name = "search:mm.texts"
	_view_name = "mm.texts/search"
	_description = "Manufactured Texts"

class ViewModelFindMmTexts(ViewModelFindController):
	_name = "find:mm.texts"
	_view_name = "mm.texts/find"
	_description = "Manufactured Texts"

class ViewModelListMmTexts(ViewModelListController):
	_name = "list:mm.texts"
	_view_name = "mm.texts/list"
	_description = "Manufactured Texts"

class ViewModelFormModalMmTexts(ViewModelFormModalController):
	_name = "form.modal:mm.texts"
	_view_name = "mm.texts/form.modal"
	_description = "Manufactured Texts"

class ViewModelFormMmTexts(ViewModelFormController):
	_name = "form:mm.texts"
	_view_name = "mm.texts/form"
	_description = "Manufactured Texts"
