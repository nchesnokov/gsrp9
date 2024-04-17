from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchLeMdGroupFreightCargo(ViewModelSearchController):
	_name = "search:le.md.group.freight.cargo"
	_view_name = "le.md.group.freight.cargo/search"
	_description = "Fleight Cargo Group"

class ViewModelFindLeMdGroupFreightCargo(ViewModelFindController):
	_name = "find:le.md.group.freight.cargo"
	_view_name = "le.md.group.freight.cargo/find"
	_description = "Fleight Cargo Group"

class ViewModelListLeMdGroupFreightCargo(ViewModelListController):
	_name = "list:le.md.group.freight.cargo"
	_view_name = "le.md.group.freight.cargo/list"
	_description = "Fleight Cargo Group"

class ViewModelFormModalLeMdGroupFreightCargo(ViewModelFormModalController):
	_name = "form.modal:le.md.group.freight.cargo"
	_view_name = "le.md.group.freight.cargo/form.modal"
	_description = "Fleight Cargo Group"

class ViewModelFormLeMdGroupFreightCargo(ViewModelFormController):
	_name = "form:le.md.group.freight.cargo"
	_view_name = "le.md.group.freight.cargo/form"
	_description = "Fleight Cargo Group"
