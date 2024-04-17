from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdQualityProduct(ViewModelFindController):
	_name = "find:md.quality.product"
	_view_name = "md.quality.product/find"
	_description = "Quality Of Product"

class ViewModelO2MFormMdQualityProduct(ViewModelO2MFormController):
	_name = "o2m-form:md.quality.product"
	_view_name = "md.quality.product/o2m-form"
	_description = "Quality Of Product"

class ViewModelO2MListMdQualityProduct(ViewModelO2MListController):
	_name = "o2m-list:md.quality.product"
	_view_name = "md.quality.product/o2m-list"
	_description = "Quality Of Product"
