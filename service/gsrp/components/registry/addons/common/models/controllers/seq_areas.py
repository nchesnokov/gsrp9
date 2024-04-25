from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSeqAreas(ViewModelSearchController):
	_name = "search:seq.areas"
	_view_name = "seq.areas/search"
	_description = "Sequense Area"

class ViewModelFindSeqAreas(ViewModelFindController):
	_name = "find:seq.areas"
	_view_name = "seq.areas/find"
	_description = "Sequense Area"

class ViewModelListSeqAreas(ViewModelListController):
	_name = "list:seq.areas"
	_view_name = "seq.areas/list"
	_description = "Sequense Area"

class ViewModelFormModalSeqAreas(ViewModelFormModalController):
	_name = "form.modal:seq.areas"
	_view_name = "seq.areas/form.modal"
	_description = "Sequense Area"

class ViewModelFormSeqAreas(ViewModelFormController):
	_name = "form:seq.areas"
	_view_name = "seq.areas/form"
	_description = "Sequense Area"
