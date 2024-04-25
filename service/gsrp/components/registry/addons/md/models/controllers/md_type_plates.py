from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdTypePlates(ViewModelSearchController):
	_name = "search:md.type.plates"
	_view_name = "md.type.plates/search"
	_description = "Type Of Plates"

class ViewModelFindMdTypePlates(ViewModelFindController):
	_name = "find:md.type.plates"
	_view_name = "md.type.plates/find"
	_description = "Type Of Plates"

class ViewModelListMdTypePlates(ViewModelListController):
	_name = "list:md.type.plates"
	_view_name = "md.type.plates/list"
	_description = "Type Of Plates"

class ViewModelFormModalMdTypePlates(ViewModelFormModalController):
	_name = "form.modal:md.type.plates"
	_view_name = "md.type.plates/form.modal"
	_description = "Type Of Plates"

class ViewModelFormMdTypePlates(ViewModelFormController):
	_name = "form:md.type.plates"
	_view_name = "md.type.plates/form"
	_description = "Type Of Plates"
