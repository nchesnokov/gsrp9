from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdQuantityUom(ViewModelSearchController):
	_name = "search:md.quantity.uom"
	_view_name = "md.quantity.uom/search"
	_description = "Quantity Unit of Measure"

class ViewModelFindMdQuantityUom(ViewModelFindController):
	_name = "find:md.quantity.uom"
	_view_name = "md.quantity.uom/find"
	_description = "Quantity Unit of Measure"

class ViewModelListMdQuantityUom(ViewModelListController):
	_name = "list:md.quantity.uom"
	_view_name = "md.quantity.uom/list"
	_description = "Quantity Unit of Measure"

class ViewModelFormModalMdQuantityUom(ViewModelFormModalController):
	_name = "form.modal:md.quantity.uom"
	_view_name = "md.quantity.uom/form.modal"
	_description = "Quantity Unit of Measure"

class ViewModelFormMdQuantityUom(ViewModelFormController):
	_name = "form:md.quantity.uom"
	_view_name = "md.quantity.uom/form"
	_description = "Quantity Unit of Measure"
