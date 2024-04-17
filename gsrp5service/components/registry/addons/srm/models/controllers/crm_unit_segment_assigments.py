from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmUnitSegmentAssigments(ViewModelSearchController):
	_name = "search:crm.unit.segment.assigments"
	_view_name = "crm.unit.segment.assigments/search"
	_description = "CRM Unit Of Segment Assigment"

class ViewModelFindCrmUnitSegmentAssigments(ViewModelFindController):
	_name = "find:crm.unit.segment.assigments"
	_view_name = "crm.unit.segment.assigments/find"
	_description = "CRM Unit Of Segment Assigment"

class ViewModelListCrmUnitSegmentAssigments(ViewModelListController):
	_name = "list:crm.unit.segment.assigments"
	_view_name = "crm.unit.segment.assigments/list"
	_description = "CRM Unit Of Segment Assigment"

class ViewModelFormModalCrmUnitSegmentAssigments(ViewModelFormModalController):
	_name = "form.modal:crm.unit.segment.assigments"
	_view_name = "crm.unit.segment.assigments/form.modal"
	_description = "CRM Unit Of Segment Assigment"

class ViewModelFormCrmUnitSegmentAssigments(ViewModelFormController):
	_name = "form:crm.unit.segment.assigments"
	_view_name = "crm.unit.segment.assigments/form"
	_description = "CRM Unit Of Segment Assigment"
