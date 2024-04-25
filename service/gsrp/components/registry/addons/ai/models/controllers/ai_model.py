from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchAiModel(ViewModelSearchController):
	_name = "search:ai.model"
	_view_name = "ai.model/search"
	_description = "Artificial Intelligence Model"

class ViewModelFindAiModel(ViewModelFindController):
	_name = "find:ai.model"
	_view_name = "ai.model/find"
	_description = "Artificial Intelligence Model"

class ViewModelListAiModel(ViewModelListController):
	_name = "list:ai.model"
	_view_name = "ai.model/list"
	_description = "Artificial Intelligence Model"

class ViewModelFormModalAiModel(ViewModelFormModalController):
	_name = "form.modal:ai.model"
	_view_name = "ai.model/form.modal"
	_description = "Artificial Intelligence Model"

class ViewModelFormAiModel(ViewModelFormController):
	_name = "form:ai.model"
	_view_name = "ai.model/form"
	_description = "Artificial Intelligence Model"
