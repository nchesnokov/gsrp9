from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSeqSegments(ViewModelSearchController):
	_name = "search:seq.segments"
	_view_name = "seq.segments/search"
	_description = "Sequense Segment"

class ViewModelFindSeqSegments(ViewModelFindController):
	_name = "find:seq.segments"
	_view_name = "seq.segments/find"
	_description = "Sequense Segment"

class ViewModelListSeqSegments(ViewModelListController):
	_name = "list:seq.segments"
	_view_name = "seq.segments/list"
	_description = "Sequense Segment"

class ViewModelFormModalSeqSegments(ViewModelFormModalController):
	_name = "form.modal:seq.segments"
	_view_name = "seq.segments/form.modal"
	_description = "Sequense Segment"

class ViewModelFormSeqSegments(ViewModelFormController):
	_name = "form:seq.segments"
	_view_name = "seq.segments/form"
	_description = "Sequense Segment"
