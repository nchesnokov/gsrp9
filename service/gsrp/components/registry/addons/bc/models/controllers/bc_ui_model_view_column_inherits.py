from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindBcUiModelViewColumnInherits(ViewModelFindController):
	_name = "find:bc.ui.model.view.column.inherits"
	_view_name = "bc.ui.model.view.column.inherits/find"
	_description = "UI Model View Columns Inherit"

class ViewModelO2MFormBcUiModelViewColumnInherits(ViewModelO2MFormController):
	_name = "o2m-form:bc.ui.model.view.column.inherits"
	_view_name = "bc.ui.model.view.column.inherits/o2m-form"
	_description = "UI Model View Columns Inherit"

class ViewModelO2MListBcUiModelViewColumnInherits(ViewModelO2MListController):
	_name = "o2m-list:bc.ui.model.view.column.inherits"
	_view_name = "bc.ui.model.view.column.inherits/o2m-list"
	_description = "UI Model View Columns Inherit"
