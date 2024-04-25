from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindBcObjTranslationInherits(ViewModelFindController):
	_name = "find:bc.obj.translation.inherits"
	_view_name = "bc.obj.translation.inherits/find"
	_description = "Object Translations Inherit"

class ViewModelO2MFormBcObjTranslationInherits(ViewModelO2MFormController):
	_name = "o2m-form:bc.obj.translation.inherits"
	_view_name = "bc.obj.translation.inherits/o2m-form"
	_description = "Object Translations Inherit"

class ViewModelO2MListBcObjTranslationInherits(ViewModelO2MListController):
	_name = "o2m-list:bc.obj.translation.inherits"
	_view_name = "bc.obj.translation.inherits/o2m-list"
	_description = "Object Translations Inherit"
