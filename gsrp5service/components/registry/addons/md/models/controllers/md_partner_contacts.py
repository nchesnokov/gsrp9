from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdPartnerContacts(ViewModelSearchController):
	_name = "search:md.partner.contacts"
	_view_name = "md.partner.contacts/search"
	_description = "Partner Contacts"

class ViewModelFindMdPartnerContacts(ViewModelFindController):
	_name = "find:md.partner.contacts"
	_view_name = "md.partner.contacts/find"
	_description = "Partner Contacts"

class ViewModelListMdPartnerContacts(ViewModelListController):
	_name = "list:md.partner.contacts"
	_view_name = "md.partner.contacts/list"
	_description = "Partner Contacts"

class ViewModelFormModalMdPartnerContacts(ViewModelFormModalController):
	_name = "form.modal:md.partner.contacts"
	_view_name = "md.partner.contacts/form.modal"
	_description = "Partner Contacts"

class ViewModelFormMdPartnerContacts(ViewModelFormController):
	_name = "form:md.partner.contacts"
	_view_name = "md.partner.contacts/form"
	_description = "Partner Contacts"
