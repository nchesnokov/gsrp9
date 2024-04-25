from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSeqAccess(ViewModelSearchController):
	_name = "search:seq.access"
	_view_name = "seq.access/search"
	_description = "Sequence Access"

class ViewModelFindSeqAccess(ViewModelFindController):
	_name = "find:seq.access"
	_view_name = "seq.access/find"
	_description = "Sequence Access"

class ViewModelListSeqAccess(ViewModelListController):
	_name = "list:seq.access"
	_view_name = "seq.access/list"
	_description = "Sequence Access"

class ViewModelFormModalSeqAccess(ViewModelFormModalController):
	_name = "form.modal:seq.access"
	_view_name = "seq.access/form.modal"
	_description = "Sequence Access"

class ViewModelFormSeqAccess(ViewModelFormController):
	_name = "form:seq.access"
	_view_name = "seq.access/form"
	_description = "Sequence Access"
