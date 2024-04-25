from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSeqModelColumns(ViewModelFindController):
	_name = "find:seq.model.columns"
	_view_name = "seq.model.columns/find"
	_description = "Sequence Model Columns"

class ViewModelO2MFormSeqModelColumns(ViewModelO2MFormController):
	_name = "o2m-form:seq.model.columns"
	_view_name = "seq.model.columns/o2m-form"
	_description = "Sequence Model Columns"

class ViewModelO2MListSeqModelColumns(ViewModelO2MListController):
	_name = "o2m-list:seq.model.columns"
	_view_name = "seq.model.columns/o2m-list"
	_description = "Sequence Model Columns"
