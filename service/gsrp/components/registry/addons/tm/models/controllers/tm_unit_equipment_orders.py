from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindTmUnitEquipmentOrders(ViewModelFindController):
	_name = "find:tm.unit.equipment.orders"
	_view_name = "tm.unit.equipment.orders/find"
	_description = "Unit Equipment Orders"

class ViewModelO2MFormTmUnitEquipmentOrders(ViewModelO2MFormController):
	_name = "o2m-form:tm.unit.equipment.orders"
	_view_name = "tm.unit.equipment.orders/o2m-form"
	_description = "Unit Equipment Orders"

class ViewModelO2MListTmUnitEquipmentOrders(ViewModelO2MListController):
	_name = "o2m-list:tm.unit.equipment.orders"
	_view_name = "tm.unit.equipment.orders/o2m-list"
	_description = "Unit Equipment Orders"
