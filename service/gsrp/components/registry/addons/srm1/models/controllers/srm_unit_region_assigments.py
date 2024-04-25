from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmUnitRegionAssigments(ViewModelSearchController):
	_name = "search:srm.unit.region.assigments"
	_view_name = "srm.unit.region.assigments/search"
	_description = "SRM Unit Of Region Assigment"

class ViewModelFindSrmUnitRegionAssigments(ViewModelFindController):
	_name = "find:srm.unit.region.assigments"
	_view_name = "srm.unit.region.assigments/find"
	_description = "SRM Unit Of Region Assigment"

class ViewModelListSrmUnitRegionAssigments(ViewModelListController):
	_name = "list:srm.unit.region.assigments"
	_view_name = "srm.unit.region.assigments/list"
	_description = "SRM Unit Of Region Assigment"

class ViewModelFormModalSrmUnitRegionAssigments(ViewModelFormModalController):
	_name = "form.modal:srm.unit.region.assigments"
	_view_name = "srm.unit.region.assigments/form.modal"
	_description = "SRM Unit Of Region Assigment"

class ViewModelFormSrmUnitRegionAssigments(ViewModelFormController):
	_name = "form:srm.unit.region.assigments"
	_view_name = "srm.unit.region.assigments/form"
	_description = "SRM Unit Of Region Assigment"
