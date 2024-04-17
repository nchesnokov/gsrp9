from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCtrmSectors(ViewModelSearchController):
	_name = "search:ctrm.sectors"
	_view_name = "ctrm.sectors/search"
	_description = "CTRM Sectors"

class ViewModelFindCtrmSectors(ViewModelFindController):
	_name = "find:ctrm.sectors"
	_view_name = "ctrm.sectors/find"
	_description = "CTRM Sectors"

class ViewModelListCtrmSectors(ViewModelListController):
	_name = "list:ctrm.sectors"
	_view_name = "ctrm.sectors/list"
	_description = "CTRM Sectors"

class ViewModelFormModalCtrmSectors(ViewModelFormModalController):
	_name = "form.modal:ctrm.sectors"
	_view_name = "ctrm.sectors/form.modal"
	_description = "CTRM Sectors"

class ViewModelFormCtrmSectors(ViewModelFormController):
	_name = "form:ctrm.sectors"
	_view_name = "ctrm.sectors/form"
	_description = "CTRM Sectors"
