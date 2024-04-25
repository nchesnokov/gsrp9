from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSeqConditions(ViewModelSearchController):
	_name = "search:seq.conditions"
	_view_name = "seq.conditions/search"
	_description = "Sequence Condition"

class ViewModelFindSeqConditions(ViewModelFindController):
	_name = "find:seq.conditions"
	_view_name = "seq.conditions/find"
	_description = "Sequence Condition"

class ViewModelListSeqConditions(ViewModelListController):
	_name = "list:seq.conditions"
	_view_name = "seq.conditions/list"
	_description = "Sequence Condition"

class ViewModelFormModalSeqConditions(ViewModelFormModalController):
	_name = "form.modal:seq.conditions"
	_view_name = "seq.conditions/form.modal"
	_description = "Sequence Condition"

class ViewModelFormSeqConditions(ViewModelFormController):
	_name = "form:seq.conditions"
	_view_name = "seq.conditions/form"
	_description = "Sequence Condition"
