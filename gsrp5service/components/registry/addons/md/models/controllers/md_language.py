from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdLanguage(ViewModelSearchController):
	_name = "search:md.language"
	_view_name = "md.language/search"
	_description = "Language"

class ViewModelFindMdLanguage(ViewModelFindController):
	_name = "find:md.language"
	_view_name = "md.language/find"
	_description = "Language"

class ViewModelListMdLanguage(ViewModelListController):
	_name = "list:md.language"
	_view_name = "md.language/list"
	_description = "Language"

class ViewModelFormModalMdLanguage(ViewModelFormModalController):
	_name = "form.modal:md.language"
	_view_name = "md.language/form.modal"
	_description = "Language"

class ViewModelFormMdLanguage(ViewModelFormController):
	_name = "form:md.language"
	_view_name = "md.language/form"
	_description = "Language"
