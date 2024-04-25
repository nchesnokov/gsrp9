from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdPartnersBank(ViewModelFindController):
	_name = "find:md.partners.bank"
	_view_name = "md.partners.bank/find"
	_description = "Bank of Partner"

class ViewModelO2MFormMdPartnersBank(ViewModelO2MFormController):
	_name = "o2m-form:md.partners.bank"
	_view_name = "md.partners.bank/o2m-form"
	_description = "Bank of Partner"

class ViewModelO2MListMdPartnersBank(ViewModelO2MListController):
	_name = "o2m-list:md.partners.bank"
	_view_name = "md.partners.bank/o2m-list"
	_description = "Bank of Partner"
