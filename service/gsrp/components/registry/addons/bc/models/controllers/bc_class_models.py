from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcClassModels(ViewModelSearchController):
	_name = "search:bc.class.models"
	_view_name = "bc.class.models/search"
	_description = "Class M<odels"

class ViewModelFindBcClassModels(ViewModelFindController):
	_name = "find:bc.class.models"
	_view_name = "bc.class.models/find"
	_description = "Class M<odels"

class ViewModelListBcClassModels(ViewModelListController):
	_name = "list:bc.class.models"
	_view_name = "bc.class.models/list"
	_description = "Class M<odels"

class ViewModelFormModalBcClassModels(ViewModelFormModalController):
	_name = "form.modal:bc.class.models"
	_view_name = "bc.class.models/form.modal"
	_description = "Class M<odels"

class ViewModelFormBcClassModels(ViewModelFormController):
	_name = "form:bc.class.models"
	_view_name = "bc.class.models/form"
	_description = "Class M<odels"
