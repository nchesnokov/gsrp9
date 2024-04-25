from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchCfFolders(ViewModelSearchController):
	_name = "search:cf.folders"
	_view_name = "cf.folders/search"
	_description = "Colobrative Folders"

class ViewModelFindCfFolders(ViewModelFindController):
	_name = "find:cf.folders"
	_view_name = "cf.folders/find"
	_description = "Colobrative Folders"

class ViewModelListCfFolders(ViewModelListController):
	_name = "list:cf.folders"
	_view_name = "cf.folders/list"
	_description = "Colobrative Folders"

class ViewModelM2MListCfTags(ViewModelM2MListController):
	_name = "m2mlist:cf.tags"
	_view_name = "cf.tags/m2mlist"
	_description = "Colobrative Folders"

class ViewModelFormModalCfFolders(ViewModelFormModalController):
	_name = "form.modal:cf.folders"
	_view_name = "cf.folders/form.modal"
	_description = "Colobrative Folders"

class ViewModelFormCfFolders(ViewModelFormController):
	_name = "form:cf.folders"
	_view_name = "cf.folders/form"
	_description = "Colobrative Folders"

class ViewModelTreeCfFolders(ViewModelTreeController):
	_name = "tree:cf.folders"
	_view_name = "cf.folders/tree"
	_description = "Colobrative Folders"
