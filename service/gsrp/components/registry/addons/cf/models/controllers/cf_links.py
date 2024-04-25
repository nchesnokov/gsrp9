from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCfLinks(ViewModelSearchController):
	_name = "search:cf.links"
	_view_name = "cf.links/search"
	_description = "Colobrative Links"

class ViewModelFindCfLinks(ViewModelFindController):
	_name = "find:cf.links"
	_view_name = "cf.links/find"
	_description = "Colobrative Links"

class ViewModelListCfLinks(ViewModelListController):
	_name = "list:cf.links"
	_view_name = "cf.links/list"
	_description = "Colobrative Links"

class ViewModelM2MListCfTags(ViewModelM2MListController):
	_name = "m2mlist:cf.tags"
	_view_name = "cf.tags/m2mlist"
	_description = "Colobrative Links"

class ViewModelFormModalCfLinks(ViewModelFormModalController):
	_name = "form.modal:cf.links"
	_view_name = "cf.links/form.modal"
	_description = "Colobrative Links"

class ViewModelFormCfLinks(ViewModelFormController):
	_name = "form:cf.links"
	_view_name = "cf.links/form"
	_description = "Colobrative Links"
