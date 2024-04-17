from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRfxItemOutputPlates(ViewModelFindController):
	_name = "find:srm.rfx.item.output.plates"
	_view_name = "srm.rfx.item.output.plates/find"
	_description = "RFX Item Output Plates"

class ViewModelO2MFormSrmRfxItemOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.rfx.item.output.plates"
	_view_name = "srm.rfx.item.output.plates/o2m-form"
	_description = "RFX Item Output Plates"

class ViewModelO2MKanbanSrmRfxItemOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.rfx.item.output.plates"
	_view_name = "srm.rfx.item.output.plates/o2m-kanban"
	_description = "RFX Item Output Plates"

class ViewModelO2MListSrmRfxItemOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.rfx.item.output.plates"
	_view_name = "srm.rfx.item.output.plates/o2m-list"
	_description = "RFX Item Output Plates"
