from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSeqAccessSchemas(ViewModelSearchController):
	_name = "search:seq.access.schemas"
	_view_name = "seq.access.schemas/search"
	_description = "Sequence Access Schema"

class ViewModelFindSeqAccessSchemas(ViewModelFindController):
	_name = "find:seq.access.schemas"
	_view_name = "seq.access.schemas/find"
	_description = "Sequence Access Schema"

class ViewModelListSeqAccessSchemas(ViewModelListController):
	_name = "list:seq.access.schemas"
	_view_name = "seq.access.schemas/list"
	_description = "Sequence Access Schema"

class ViewModelFormModalSeqAccessSchemas(ViewModelFormModalController):
	_name = "form.modal:seq.access.schemas"
	_view_name = "seq.access.schemas/form.modal"
	_description = "Sequence Access Schema"

class ViewModelFormSeqAccessSchemas(ViewModelFormController):
	_name = "form:seq.access.schemas"
	_view_name = "seq.access.schemas/form"
	_description = "Sequence Access Schema"
