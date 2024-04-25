from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindBcUiModelViewWebcomponents(ViewModelFindController):
	_name = "find:bc.ui.model.view.webcomponents"
	_view_name = "bc.ui.model.view.webcomponents/find"
	_description = "UI Model View Webcomponent"

class ViewModelO2MFormBcUiModelViewWebcomponents(ViewModelO2MFormController):
	_name = "o2m-form:bc.ui.model.view.webcomponents"
	_view_name = "bc.ui.model.view.webcomponents/o2m-form"
	_description = "UI Model View Webcomponent"

class ViewModelO2MListBcUiModelViewWebcomponents(ViewModelO2MListController):
	_name = "o2m-list:bc.ui.model.view.webcomponents"
	_view_name = "bc.ui.model.view.webcomponents/o2m-list"
	_description = "UI Model View Webcomponent"
