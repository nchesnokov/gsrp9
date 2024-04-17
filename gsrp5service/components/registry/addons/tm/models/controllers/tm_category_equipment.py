from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchTmCategoryEquipment(ViewModelSearchController):
	_name = "search:tm.category.equipment"
	_view_name = "tm.category.equipment/search"
	_description = "Category Equipment"

class ViewModelFindTmCategoryEquipment(ViewModelFindController):
	_name = "find:tm.category.equipment"
	_view_name = "tm.category.equipment/find"
	_description = "Category Equipment"

class ViewModelListTmCategoryEquipment(ViewModelListController):
	_name = "list:tm.category.equipment"
	_view_name = "tm.category.equipment/list"
	_description = "Category Equipment"

class ViewModelFormModalTmCategoryEquipment(ViewModelFormModalController):
	_name = "form.modal:tm.category.equipment"
	_view_name = "tm.category.equipment/form.modal"
	_description = "Category Equipment"

class ViewModelFormTmCategoryEquipment(ViewModelFormController):
	_name = "form:tm.category.equipment"
	_view_name = "tm.category.equipment/form"
	_description = "Category Equipment"

class ViewModelTreeTmCategoryEquipment(ViewModelTreeController):
	_name = "tree:tm.category.equipment"
	_view_name = "tm.category.equipment/tree"
	_description = "Category Equipment"
