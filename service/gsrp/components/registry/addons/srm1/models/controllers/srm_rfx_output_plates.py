from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRfxOutputPlates(ViewModelFindController):
	_name = "find:srm.rfx.output.plates"
	_view_name = "srm.rfx.output.plates/find"
	_description = "SRM RFX Output Plates"

class ViewModelO2MFormSrmRfxOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.rfx.output.plates"
	_view_name = "srm.rfx.output.plates/o2m-form"
	_description = "SRM RFX Output Plates"

class ViewModelO2MKanbanSrmRfxOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.rfx.output.plates"
	_view_name = "srm.rfx.output.plates/o2m-kanban"
	_description = "SRM RFX Output Plates"

class ViewModelO2MListSrmRfxOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.rfx.output.plates"
	_view_name = "srm.rfx.output.plates/o2m-list"
	_description = "SRM RFX Output Plates"
