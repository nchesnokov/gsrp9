from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCfFiles(ViewModelSearchController):
	_name = "search:cf.files"
	_view_name = "cf.files/search"
	_description = "Colobrative Files"

class ViewModelFindCfFiles(ViewModelFindController):
	_name = "find:cf.files"
	_view_name = "cf.files/find"
	_description = "Colobrative Files"

class ViewModelListCfFiles(ViewModelListController):
	_name = "list:cf.files"
	_view_name = "cf.files/list"
	_description = "Colobrative Files"

class ViewModelM2MListCfTags(ViewModelM2MListController):
	_name = "m2mlist:cf.tags"
	_view_name = "cf.tags/m2mlist"
	_description = "Colobrative Files"

class ViewModelFormModalCfFiles(ViewModelFormModalController):
	_name = "form.modal:cf.files"
	_view_name = "cf.files/form.modal"
	_description = "Colobrative Files"

class ViewModelFormCfFiles(ViewModelFormController):
	_name = "form:cf.files"
	_view_name = "cf.files/form"
	_description = "Colobrative Files"
