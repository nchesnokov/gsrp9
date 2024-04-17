from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindBcUserPreferences(ViewModelFindController):
	_name = "find:bc.user.preferences"
	_view_name = "bc.user.preferences/find"
	_description = "User Preferncess"

class ViewModelO2MFormBcUserPreferences(ViewModelO2MFormController):
	_name = "o2m-form:bc.user.preferences"
	_view_name = "bc.user.preferences/o2m-form"
	_description = "User Preferncess"

class ViewModelO2MListBcUserPreferences(ViewModelO2MListController):
	_name = "o2m-list:bc.user.preferences"
	_view_name = "bc.user.preferences/o2m-list"
	_description = "User Preferncess"
