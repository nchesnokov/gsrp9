from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmUnitAreaAssigments(ViewModelSearchController):
	_name = "search:srm.unit.area.assigments"
	_view_name = "srm.unit.area.assigments/search"
	_description = "SRM Unit Of Area Assigment"

class ViewModelFindSrmUnitAreaAssigments(ViewModelFindController):
	_name = "find:srm.unit.area.assigments"
	_view_name = "srm.unit.area.assigments/find"
	_description = "SRM Unit Of Area Assigment"

class ViewModelListSrmUnitAreaAssigments(ViewModelListController):
	_name = "list:srm.unit.area.assigments"
	_view_name = "srm.unit.area.assigments/list"
	_description = "SRM Unit Of Area Assigment"

class ViewModelFormModalSrmUnitAreaAssigments(ViewModelFormModalController):
	_name = "form.modal:srm.unit.area.assigments"
	_view_name = "srm.unit.area.assigments/form.modal"
	_description = "SRM Unit Of Area Assigment"

class ViewModelFormSrmUnitAreaAssigments(ViewModelFormController):
	_name = "form:srm.unit.area.assigments"
	_view_name = "srm.unit.area.assigments/form"
	_description = "SRM Unit Of Area Assigment"
