from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdPartnerProducts(ViewModelFindController):
	_name = "find:md.partner.products"
	_view_name = "md.partner.products/find"
	_description = "Partner Products"

class ViewModelO2MFormMdPartnerProducts(ViewModelO2MFormController):
	_name = "o2m-form:md.partner.products"
	_view_name = "md.partner.products/o2m-form"
	_description = "Partner Products"

class ViewModelO2MListMdPartnerProducts(ViewModelO2MListController):
	_name = "o2m-list:md.partner.products"
	_view_name = "md.partner.products/o2m-list"
	_description = "Partner Products"
