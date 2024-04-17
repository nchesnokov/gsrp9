from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCfTags(ViewModelSearchController):
	_name = "search:cf.tags"
	_view_name = "cf.tags/search"
	_description = "Colobrative Folders File Tags"

class ViewModelFindCfTags(ViewModelFindController):
	_name = "find:cf.tags"
	_view_name = "cf.tags/find"
	_description = "Colobrative Folders File Tags"

class ViewModelListCfTags(ViewModelListController):
	_name = "list:cf.tags"
	_view_name = "cf.tags/list"
	_description = "Colobrative Folders File Tags"

class ViewModelM2MListCfFolders(ViewModelM2MListController):
	_name = "m2mlist:cf.folders"
	_view_name = "cf.folders/m2mlist"
	_description = "Colobrative Folders File Tags"

class ViewModelM2MListCfFiles(ViewModelM2MListController):
	_name = "m2mlist:cf.files"
	_view_name = "cf.files/m2mlist"
	_description = "Colobrative Folders File Tags"

class ViewModelM2MListCfLinks(ViewModelM2MListController):
	_name = "m2mlist:cf.links"
	_view_name = "cf.links/m2mlist"
	_description = "Colobrative Folders File Tags"

class ViewModelFormModalCfTags(ViewModelFormModalController):
	_name = "form.modal:cf.tags"
	_view_name = "cf.tags/form.modal"
	_description = "Colobrative Folders File Tags"

class ViewModelFormCfTags(ViewModelFormController):
	_name = "form:cf.tags"
	_view_name = "cf.tags/form"
	_description = "Colobrative Folders File Tags"
