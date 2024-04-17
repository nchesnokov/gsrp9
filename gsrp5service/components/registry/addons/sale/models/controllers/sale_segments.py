from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSaleSegments(ViewModelSearchController):
	_name = "search:sale.segments"
	_view_name = "sale.segments/search"
	_description = "Sale Segments"

class ViewModelFindSaleSegments(ViewModelFindController):
	_name = "find:sale.segments"
	_view_name = "sale.segments/find"
	_description = "Sale Segments"

class ViewModelListSaleSegments(ViewModelListController):
	_name = "list:sale.segments"
	_view_name = "sale.segments/list"
	_description = "Sale Segments"

class ViewModelFormModalSaleSegments(ViewModelFormModalController):
	_name = "form.modal:sale.segments"
	_view_name = "sale.segments/form.modal"
	_description = "Sale Segments"

class ViewModelFormSaleSegments(ViewModelFormController):
	_name = "form:sale.segments"
	_view_name = "sale.segments/form"
	_description = "Sale Segments"
