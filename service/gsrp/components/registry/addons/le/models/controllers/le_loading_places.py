from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchLeLoadingPlaces(ViewModelSearchController):
	_name = "search:le.loading.places"
	_view_name = "le.loading.places/search"
	_description = "Loading Places"

class ViewModelFindLeLoadingPlaces(ViewModelFindController):
	_name = "find:le.loading.places"
	_view_name = "le.loading.places/find"
	_description = "Loading Places"

class ViewModelListLeLoadingPlaces(ViewModelListController):
	_name = "list:le.loading.places"
	_view_name = "le.loading.places/list"
	_description = "Loading Places"

class ViewModelFormModalLeLoadingPlaces(ViewModelFormModalController):
	_name = "form.modal:le.loading.places"
	_view_name = "le.loading.places/form.modal"
	_description = "Loading Places"

class ViewModelFormLeLoadingPlaces(ViewModelFormController):
	_name = "form:le.loading.places"
	_view_name = "le.loading.places/form"
	_description = "Loading Places"
