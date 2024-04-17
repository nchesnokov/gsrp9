from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelKanbanController

class ViewModelSearchTmTemplateEquipment(ViewModelSearchController):
	_name = "search:tm.template.equipment"
	_view_name = "tm.template.equipment/search"
	_description = "Template Equipment"

class ViewModelFindTmTemplateEquipment(ViewModelFindController):
	_name = "find:tm.template.equipment"
	_view_name = "tm.template.equipment/find"
	_description = "Template Equipment"

class ViewModelListTmTemplateEquipment(ViewModelListController):
	_name = "list:tm.template.equipment"
	_view_name = "tm.template.equipment/list"
	_description = "Template Equipment"

class ViewModelFormModalTmTemplateEquipment(ViewModelFormModalController):
	_name = "form.modal:tm.template.equipment"
	_view_name = "tm.template.equipment/form.modal"
	_description = "Template Equipment"

class ViewModelFormTmTemplateEquipment(ViewModelFormController):
	_name = "form:tm.template.equipment"
	_view_name = "tm.template.equipment/form"
	_description = "Template Equipment"

class ViewModelKanbanTmTemplateEquipment(ViewModelKanbanController):
	_name = "kanban:tm.template.equipment"
	_view_name = "tm.template.equipment/kanban"
	_description = "Template Equipment"
