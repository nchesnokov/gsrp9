from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmOfferRoles(ViewModelFind):
	_name = "model.find.crm.offer.roles"
	_model = "crm.offer.roles"
	_description = "CRM Offer Roles"
	_columns = ['offer_id', 'role_id', 'patner_id']

class ViewModelO2MFormCrmOfferRoles(ViewModelO2MForm):
	_name = "model.o2mform.crm.offer.roles"
	_model = "crm.offer.roles"
	_description = "CRM Offer Roles"
	_columns = ['offer_id', 'role_id', 'patner_id']

class ViewModelO2MListCrmOfferRoles(ViewModelO2MList):
	_name = "model.o2mlist.crm.offer.roles"
	_model = "crm.offer.roles"
	_description = "CRM Offer Roles"
	_columns = ['offer_id', 'role_id', 'patner_id']
