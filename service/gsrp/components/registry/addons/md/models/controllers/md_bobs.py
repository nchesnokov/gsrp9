from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdBobs(ViewModelSearchController):
	_name = "search:md.bobs"
	_view_name = "md.bobs/search"
	_description = "Bill of Bills"

class ViewModelFindMdBobs(ViewModelFindController):
	_name = "find:md.bobs"
	_view_name = "md.bobs/find"
	_description = "Bill of Bills"

class ViewModelListMdBobs(ViewModelListController):
	_name = "list:md.bobs"
	_view_name = "md.bobs/list"
	_description = "Bill of Bills"

class ViewModelFormModalMdBobs(ViewModelFormModalController):
	_name = "form.modal:md.bobs"
	_view_name = "md.bobs/form.modal"
	_description = "Bill of Bills"

class ViewModelFormMdBobs(ViewModelFormController):
	_name = "form:md.bobs"
	_view_name = "md.bobs/form"
	_description = "Bill of Bills"
