from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSeqAccessSchemaItems(ViewModelFindController):
	_name = "find:seq.access.schema.items"
	_view_name = "seq.access.schema.items/find"
	_description = "Sequence Access Items Of Schema"

class ViewModelO2MFormSeqAccessSchemaItems(ViewModelO2MFormController):
	_name = "o2m-form:seq.access.schema.items"
	_view_name = "seq.access.schema.items/o2m-form"
	_description = "Sequence Access Items Of Schema"

class ViewModelO2MListSeqAccessSchemaItems(ViewModelO2MListController):
	_name = "o2m-list:seq.access.schema.items"
	_view_name = "seq.access.schema.items/o2m-list"
	_description = "Sequence Access Items Of Schema"
