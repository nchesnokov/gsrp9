from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSeqModels(ViewModelFindController):
	_name = "find:seq.models"
	_view_name = "seq.models/find"
	_description = "Sequence Models"

class ViewModelO2MFormSeqModels(ViewModelO2MFormController):
	_name = "o2m-form:seq.models"
	_view_name = "seq.models/o2m-form"
	_description = "Sequence Models"

class ViewModelO2MListSeqModels(ViewModelO2MListController):
	_name = "o2m-list:seq.models"
	_view_name = "seq.models/o2m-list"
	_description = "Sequence Models"
