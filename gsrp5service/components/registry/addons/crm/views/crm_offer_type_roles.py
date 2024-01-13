from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmOfferTypeRoles(ViewModelFind):
	_name = "model.find.crm.offer.type.roles"
	_model = "crm.offer.type.roles"
	_description = "Role CRM Offer Types"
	_columns = ['type_id', 'role_id', 'required', 'note']

class ViewModelO2MFormCrmOfferTypeRoles(ViewModelO2MForm):
	_name = "model.o2mform.crm.offer.type.roles"
	_model = "crm.offer.type.roles"
	_description = "Role CRM Offer Types"
	_columns = ['type_id', 'role_id', 'required', 'note']

class ViewModelO2MListCrmOfferTypeRoles(ViewModelO2MList):
	_name = "model.o2mlist.crm.offer.type.roles"
	_model = "crm.offer.type.roles"
	_description = "Role CRM Offer Types"
	_columns = ['type_id', 'role_id', 'required', 'note']
