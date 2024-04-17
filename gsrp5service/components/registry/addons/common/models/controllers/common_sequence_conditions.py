from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCommonSequenceConditions(ViewModelSearchController):
	_name = "search:common.sequence.conditions"
	_view_name = "common.sequence.conditions/search"
	_description = "Common Sequence Condition"

class ViewModelFindCommonSequenceConditions(ViewModelFindController):
	_name = "find:common.sequence.conditions"
	_view_name = "common.sequence.conditions/find"
	_description = "Common Sequence Condition"

class ViewModelListCommonSequenceConditions(ViewModelListController):
	_name = "list:common.sequence.conditions"
	_view_name = "common.sequence.conditions/list"
	_description = "Common Sequence Condition"

class ViewModelFormModalCommonSequenceConditions(ViewModelFormModalController):
	_name = "form.modal:common.sequence.conditions"
	_view_name = "common.sequence.conditions/form.modal"
	_description = "Common Sequence Condition"

class ViewModelFormCommonSequenceConditions(ViewModelFormController):
	_name = "form:common.sequence.conditions"
	_view_name = "common.sequence.conditions/form"
	_description = "Common Sequence Condition"
