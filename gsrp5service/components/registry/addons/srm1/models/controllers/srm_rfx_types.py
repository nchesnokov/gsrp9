from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmRfxTypes(ViewModelSearchController):
	_name = "search:srm.rfx.types"
	_view_name = "srm.rfx.types/search"
	_description = "Types SRM RFX"

class ViewModelFindSrmRfxTypes(ViewModelFindController):
	_name = "find:srm.rfx.types"
	_view_name = "srm.rfx.types/find"
	_description = "Types SRM RFX"

class ViewModelListSrmRfxTypes(ViewModelListController):
	_name = "list:srm.rfx.types"
	_view_name = "srm.rfx.types/list"
	_description = "Types SRM RFX"

class ViewModelFormModalSrmRfxTypes(ViewModelFormModalController):
	_name = "form.modal:srm.rfx.types"
	_view_name = "srm.rfx.types/form.modal"
	_description = "Types SRM RFX"

class ViewModelFormSrmRfxTypes(ViewModelFormController):
	_name = "form:srm.rfx.types"
	_view_name = "srm.rfx.types/form"
	_description = "Types SRM RFX"
