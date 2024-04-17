from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelKanbanController

class ViewModelSearchTmUnitEquipments(ViewModelSearchController):
	_name = "search:tm.unit.equipments"
	_view_name = "tm.unit.equipments/search"
	_description = "Unit Equipments"

class ViewModelFindTmUnitEquipments(ViewModelFindController):
	_name = "find:tm.unit.equipments"
	_view_name = "tm.unit.equipments/find"
	_description = "Unit Equipments"

class ViewModelListTmUnitEquipments(ViewModelListController):
	_name = "list:tm.unit.equipments"
	_view_name = "tm.unit.equipments/list"
	_description = "Unit Equipments"

class ViewModelFormModalTmUnitEquipments(ViewModelFormModalController):
	_name = "form.modal:tm.unit.equipments"
	_view_name = "tm.unit.equipments/form.modal"
	_description = "Unit Equipments"

class ViewModelFormTmUnitEquipments(ViewModelFormController):
	_name = "form:tm.unit.equipments"
	_view_name = "tm.unit.equipments/form"
	_description = "Unit Equipments"

class ViewModelKanbanTmUnitEquipments(ViewModelKanbanController):
	_name = "kanban:tm.unit.equipments"
	_view_name = "tm.unit.equipments/kanban"
	_description = "Unit Equipments"
