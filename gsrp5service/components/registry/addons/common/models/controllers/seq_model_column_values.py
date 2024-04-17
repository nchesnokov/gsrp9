from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSeqModelColumnValues(ViewModelFindController):
	_name = "find:seq.model.column.values"
	_view_name = "seq.model.column.values/find"
	_description = "Sequence Model Columns"

class ViewModelO2MFormSeqModelColumnValues(ViewModelO2MFormController):
	_name = "o2m-form:seq.model.column.values"
	_view_name = "seq.model.column.values/o2m-form"
	_description = "Sequence Model Columns"

class ViewModelO2MListSeqModelColumnValues(ViewModelO2MListController):
	_name = "o2m-list:seq.model.column.values"
	_view_name = "seq.model.column.values/o2m-list"
	_description = "Sequence Model Columns"
