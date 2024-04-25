from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPrjUnitSegmentAssigments(ViewModelSearchController):
	_name = "search:prj.unit.segment.assigments"
	_view_name = "prj.unit.segment.assigments/search"
	_description = "Project Unit Of Segment Assigment"

class ViewModelFindPrjUnitSegmentAssigments(ViewModelFindController):
	_name = "find:prj.unit.segment.assigments"
	_view_name = "prj.unit.segment.assigments/find"
	_description = "Project Unit Of Segment Assigment"

class ViewModelListPrjUnitSegmentAssigments(ViewModelListController):
	_name = "list:prj.unit.segment.assigments"
	_view_name = "prj.unit.segment.assigments/list"
	_description = "Project Unit Of Segment Assigment"

class ViewModelFormModalPrjUnitSegmentAssigments(ViewModelFormModalController):
	_name = "form.modal:prj.unit.segment.assigments"
	_view_name = "prj.unit.segment.assigments/form.modal"
	_description = "Project Unit Of Segment Assigment"

class ViewModelFormPrjUnitSegmentAssigments(ViewModelFormController):
	_name = "form:prj.unit.segment.assigments"
	_view_name = "prj.unit.segment.assigments/form"
	_description = "Project Unit Of Segment Assigment"
