from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindBcObjObjectAccess(ViewModelFindController):
	_name = "find:bc.obj.object.access"
	_view_name = "bc.obj.object.access/find"
	_description = "Object Access"

class ViewModelO2MFormBcObjObjectAccess(ViewModelO2MFormController):
	_name = "o2m-form:bc.obj.object.access"
	_view_name = "bc.obj.object.access/o2m-form"
	_description = "Object Access"

class ViewModelO2MListBcObjObjectAccess(ViewModelO2MListController):
	_name = "o2m-list:bc.obj.object.access"
	_view_name = "bc.obj.object.access/o2m-list"
	_description = "Object Access"
