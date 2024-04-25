from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmTechnologicOrderOps(ViewModelFindController):
	_name = "find:mm.technologic.order.ops"
	_view_name = "mm.technologic.order.ops/find"
	_description = "Operations of technologic order"

class ViewModelO2MFormMmTechnologicOrderOps(ViewModelO2MFormController):
	_name = "o2m-form:mm.technologic.order.ops"
	_view_name = "mm.technologic.order.ops/o2m-form"
	_description = "Operations of technologic order"

class ViewModelO2MListMmTechnologicOrderOps(ViewModelO2MListController):
	_name = "o2m-list:mm.technologic.order.ops"
	_view_name = "mm.technologic.order.ops/o2m-list"
	_description = "Operations of technologic order"
