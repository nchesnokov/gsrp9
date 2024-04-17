from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPurchaseUnitSegmentAssigments(ViewModelSearchController):
	_name = "search:purchase.unit.segment.assigments"
	_view_name = "purchase.unit.segment.assigments/search"
	_description = "Purchase Unit Of Segment Assigment"

class ViewModelFindPurchaseUnitSegmentAssigments(ViewModelFindController):
	_name = "find:purchase.unit.segment.assigments"
	_view_name = "purchase.unit.segment.assigments/find"
	_description = "Purchase Unit Of Segment Assigment"

class ViewModelListPurchaseUnitSegmentAssigments(ViewModelListController):
	_name = "list:purchase.unit.segment.assigments"
	_view_name = "purchase.unit.segment.assigments/list"
	_description = "Purchase Unit Of Segment Assigment"

class ViewModelFormModalPurchaseUnitSegmentAssigments(ViewModelFormModalController):
	_name = "form.modal:purchase.unit.segment.assigments"
	_view_name = "purchase.unit.segment.assigments/form.modal"
	_description = "Purchase Unit Of Segment Assigment"

class ViewModelFormPurchaseUnitSegmentAssigments(ViewModelFormController):
	_name = "form:purchase.unit.segment.assigments"
	_view_name = "purchase.unit.segment.assigments/form"
	_description = "Purchase Unit Of Segment Assigment"
