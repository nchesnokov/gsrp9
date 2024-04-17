from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeMdGroupFreightCargoProduct(ViewModelFindController):
	_name = "find:le.md.group.freight.cargo.product"
	_view_name = "le.md.group.freight.cargo.product/find"
	_description = "Fleight Cargo Group Product"

class ViewModelO2MFormLeMdGroupFreightCargoProduct(ViewModelO2MFormController):
	_name = "o2m-form:le.md.group.freight.cargo.product"
	_view_name = "le.md.group.freight.cargo.product/o2m-form"
	_description = "Fleight Cargo Group Product"

class ViewModelO2MListLeMdGroupFreightCargoProduct(ViewModelO2MListController):
	_name = "o2m-list:le.md.group.freight.cargo.product"
	_view_name = "le.md.group.freight.cargo.product/o2m-list"
	_description = "Fleight Cargo Group Product"
