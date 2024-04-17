from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdUom(ViewModelSearchController):
	_name = "search:md.uom"
	_view_name = "md.uom/search"
	_description = "Unit of Measure"

class ViewModelFindMdUom(ViewModelFindController):
	_name = "find:md.uom"
	_view_name = "md.uom/find"
	_description = "Unit of Measure"

class ViewModelListMdUom(ViewModelListController):
	_name = "list:md.uom"
	_view_name = "md.uom/list"
	_description = "Unit of Measure"

class ViewModelFormModalMdUom(ViewModelFormModalController):
	_name = "form.modal:md.uom"
	_view_name = "md.uom/form.modal"
	_description = "Unit of Measure"

class ViewModelFormMdUom(ViewModelFormController):
	_name = "form:md.uom"
	_view_name = "md.uom/form"
	_description = "Unit of Measure"
