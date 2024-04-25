from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchLeShippingPoints(ViewModelSearchController):
	_name = "search:le.shipping.points"
	_view_name = "le.shipping.points/search"
	_description = "Shipping Points"

class ViewModelFindLeShippingPoints(ViewModelFindController):
	_name = "find:le.shipping.points"
	_view_name = "le.shipping.points/find"
	_description = "Shipping Points"

class ViewModelListLeShippingPoints(ViewModelListController):
	_name = "list:le.shipping.points"
	_view_name = "le.shipping.points/list"
	_description = "Shipping Points"

class ViewModelFormModalLeShippingPoints(ViewModelFormModalController):
	_name = "form.modal:le.shipping.points"
	_view_name = "le.shipping.points/form.modal"
	_description = "Shipping Points"

class ViewModelFormLeShippingPoints(ViewModelFormController):
	_name = "form:le.shipping.points"
	_view_name = "le.shipping.points/form"
	_description = "Shipping Points"
