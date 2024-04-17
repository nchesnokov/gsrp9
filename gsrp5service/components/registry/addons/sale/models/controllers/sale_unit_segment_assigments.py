from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSaleUnitSegmentAssigments(ViewModelSearchController):
	_name = "search:sale.unit.segment.assigments"
	_view_name = "sale.unit.segment.assigments/search"
	_description = "Sale Unit Of Segment Assigment"

class ViewModelFindSaleUnitSegmentAssigments(ViewModelFindController):
	_name = "find:sale.unit.segment.assigments"
	_view_name = "sale.unit.segment.assigments/find"
	_description = "Sale Unit Of Segment Assigment"

class ViewModelListSaleUnitSegmentAssigments(ViewModelListController):
	_name = "list:sale.unit.segment.assigments"
	_view_name = "sale.unit.segment.assigments/list"
	_description = "Sale Unit Of Segment Assigment"

class ViewModelFormModalSaleUnitSegmentAssigments(ViewModelFormModalController):
	_name = "form.modal:sale.unit.segment.assigments"
	_view_name = "sale.unit.segment.assigments/form.modal"
	_description = "Sale Unit Of Segment Assigment"

class ViewModelFormSaleUnitSegmentAssigments(ViewModelFormController):
	_name = "form:sale.unit.segment.assigments"
	_view_name = "sale.unit.segment.assigments/form"
	_description = "Sale Unit Of Segment Assigment"
