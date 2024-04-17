from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSrmRfxCategory(ViewModelSearchController):
	_name = "search:srm.rfx.category"
	_view_name = "srm.rfx.category/search"
	_description = "Category SRM RFX"

class ViewModelFindSrmRfxCategory(ViewModelFindController):
	_name = "find:srm.rfx.category"
	_view_name = "srm.rfx.category/find"
	_description = "Category SRM RFX"

class ViewModelListSrmRfxCategory(ViewModelListController):
	_name = "list:srm.rfx.category"
	_view_name = "srm.rfx.category/list"
	_description = "Category SRM RFX"

class ViewModelFormModalSrmRfxCategory(ViewModelFormModalController):
	_name = "form.modal:srm.rfx.category"
	_view_name = "srm.rfx.category/form.modal"
	_description = "Category SRM RFX"

class ViewModelFormSrmRfxCategory(ViewModelFormController):
	_name = "form:srm.rfx.category"
	_view_name = "srm.rfx.category/form"
	_description = "Category SRM RFX"

class ViewModelTreeSrmRfxCategory(ViewModelTreeController):
	_name = "tree:srm.rfx.category"
	_view_name = "srm.rfx.category/tree"
	_description = "Category SRM RFX"
