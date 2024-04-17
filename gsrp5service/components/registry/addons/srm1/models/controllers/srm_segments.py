from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmSegments(ViewModelSearchController):
	_name = "search:srm.segments"
	_view_name = "srm.segments/search"
	_description = "SRM Segments"

class ViewModelFindSrmSegments(ViewModelFindController):
	_name = "find:srm.segments"
	_view_name = "srm.segments/find"
	_description = "SRM Segments"

class ViewModelListSrmSegments(ViewModelListController):
	_name = "list:srm.segments"
	_view_name = "srm.segments/list"
	_description = "SRM Segments"

class ViewModelFormModalSrmSegments(ViewModelFormModalController):
	_name = "form.modal:srm.segments"
	_view_name = "srm.segments/form.modal"
	_description = "SRM Segments"

class ViewModelFormSrmSegments(ViewModelFormController):
	_name = "form:srm.segments"
	_view_name = "srm.segments/form"
	_description = "SRM Segments"
