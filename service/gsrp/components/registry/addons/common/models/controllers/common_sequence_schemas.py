from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCommonSequenceSchemas(ViewModelSearchController):
	_name = "search:common.sequence.schemas"
	_view_name = "common.sequence.schemas/search"
	_description = "Common Sequence Schemas"

class ViewModelFindCommonSequenceSchemas(ViewModelFindController):
	_name = "find:common.sequence.schemas"
	_view_name = "common.sequence.schemas/find"
	_description = "Common Sequence Schemas"

class ViewModelListCommonSequenceSchemas(ViewModelListController):
	_name = "list:common.sequence.schemas"
	_view_name = "common.sequence.schemas/list"
	_description = "Common Sequence Schemas"

class ViewModelFormModalCommonSequenceSchemas(ViewModelFormModalController):
	_name = "form.modal:common.sequence.schemas"
	_view_name = "common.sequence.schemas/form.modal"
	_description = "Common Sequence Schemas"

class ViewModelFormCommonSequenceSchemas(ViewModelFormController):
	_name = "form:common.sequence.schemas"
	_view_name = "common.sequence.schemas/form"
	_description = "Common Sequence Schemas"
