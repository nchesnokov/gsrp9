from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmDecisionTypes(ViewModelSearchController):
	_name = "search:srm.decision.types"
	_view_name = "srm.decision.types/search"
	_description = "Types SRM Decision"

class ViewModelFindSrmDecisionTypes(ViewModelFindController):
	_name = "find:srm.decision.types"
	_view_name = "srm.decision.types/find"
	_description = "Types SRM Decision"

class ViewModelListSrmDecisionTypes(ViewModelListController):
	_name = "list:srm.decision.types"
	_view_name = "srm.decision.types/list"
	_description = "Types SRM Decision"

class ViewModelFormModalSrmDecisionTypes(ViewModelFormModalController):
	_name = "form.modal:srm.decision.types"
	_view_name = "srm.decision.types/form.modal"
	_description = "Types SRM Decision"

class ViewModelFormSrmDecisionTypes(ViewModelFormController):
	_name = "form:srm.decision.types"
	_view_name = "srm.decision.types/form"
	_description = "Types SRM Decision"
