from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmUnitSegmentAssigments(ViewModelSearchController):
	_name = "search:srm.unit.segment.assigments"
	_view_name = "srm.unit.segment.assigments/search"
	_description = "SRM Unit Of Segment Assigment"

class ViewModelFindSrmUnitSegmentAssigments(ViewModelFindController):
	_name = "find:srm.unit.segment.assigments"
	_view_name = "srm.unit.segment.assigments/find"
	_description = "SRM Unit Of Segment Assigment"

class ViewModelListSrmUnitSegmentAssigments(ViewModelListController):
	_name = "list:srm.unit.segment.assigments"
	_view_name = "srm.unit.segment.assigments/list"
	_description = "SRM Unit Of Segment Assigment"

class ViewModelFormModalSrmUnitSegmentAssigments(ViewModelFormModalController):
	_name = "form.modal:srm.unit.segment.assigments"
	_view_name = "srm.unit.segment.assigments/form.modal"
	_description = "SRM Unit Of Segment Assigment"

class ViewModelFormSrmUnitSegmentAssigments(ViewModelFormController):
	_name = "form:srm.unit.segment.assigments"
	_view_name = "srm.unit.segment.assigments/form"
	_description = "SRM Unit Of Segment Assigment"
