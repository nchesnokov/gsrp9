from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindDevelUiModelViewColumnInherits(ViewModelFindController):
	_name = "find:devel.ui.model.view.column.inherits"
	_view_name = "devel.ui.model.view.column.inherits/find"
	_description = "UI Model View Columns Inherit"

class ViewModelO2MFormDevelUiModelViewColumnInherits(ViewModelO2MFormController):
	_name = "o2m-form:devel.ui.model.view.column.inherits"
	_view_name = "devel.ui.model.view.column.inherits/o2m-form"
	_description = "UI Model View Columns Inherit"

class ViewModelO2MListDevelUiModelViewColumnInherits(ViewModelO2MListController):
	_name = "o2m-list:devel.ui.model.view.column.inherits"
	_view_name = "devel.ui.model.view.column.inherits/o2m-list"
	_description = "UI Model View Columns Inherit"
