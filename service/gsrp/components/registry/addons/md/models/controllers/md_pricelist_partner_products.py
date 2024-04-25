from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdPricelistPartnerProducts(ViewModelFindController):
	_name = "find:md.pricelist.partner.products"
	_view_name = "md.pricelist.partner.products/find"
	_description = "Pricelist Partner Products"

class ViewModelO2MFormMdPricelistPartnerProducts(ViewModelO2MFormController):
	_name = "o2m-form:md.pricelist.partner.products"
	_view_name = "md.pricelist.partner.products/o2m-form"
	_description = "Pricelist Partner Products"

class ViewModelO2MListMdPricelistPartnerProducts(ViewModelO2MListController):
	_name = "o2m-list:md.pricelist.partner.products"
	_view_name = "md.pricelist.partner.products/o2m-list"
	_description = "Pricelist Partner Products"
