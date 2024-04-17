from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSrmDecisionCategory(ViewModelSearchController):
	_name = "search:srm.decision.category"
	_view_name = "srm.decision.category/search"
	_description = "Category SRM Decision"

class ViewModelFindSrmDecisionCategory(ViewModelFindController):
	_name = "find:srm.decision.category"
	_view_name = "srm.decision.category/find"
	_description = "Category SRM Decision"

class ViewModelListSrmDecisionCategory(ViewModelListController):
	_name = "list:srm.decision.category"
	_view_name = "srm.decision.category/list"
	_description = "Category SRM Decision"

class ViewModelFormModalSrmDecisionCategory(ViewModelFormModalController):
	_name = "form.modal:srm.decision.category"
	_view_name = "srm.decision.category/form.modal"
	_description = "Category SRM Decision"

class ViewModelFormSrmDecisionCategory(ViewModelFormController):
	_name = "form:srm.decision.category"
	_view_name = "srm.decision.category/form"
	_description = "Category SRM Decision"

class ViewModelTreeSrmDecisionCategory(ViewModelTreeController):
	_name = "tree:srm.decision.category"
	_view_name = "srm.decision.category/tree"
	_description = "Category SRM Decision"
