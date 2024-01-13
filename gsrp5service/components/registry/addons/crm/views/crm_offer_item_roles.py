from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmOfferItemRoles(ViewModelFind):
	_name = "model.find.crm.offer.item.roles"
	_model = "crm.offer.item.roles"
	_description = "CRM Offer Item Roles"
	_columns = ['item_id', 'role_id', 'patner_id']

class ViewModelO2MFormCrmOfferItemRoles(ViewModelO2MForm):
	_name = "model.o2mform.crm.offer.item.roles"
	_model = "crm.offer.item.roles"
	_description = "CRM Offer Item Roles"
	_columns = ['item_id', 'role_id', 'patner_id']

class ViewModelO2MListCrmOfferItemRoles(ViewModelO2MList):
	_name = "model.o2mlist.crm.offer.item.roles"
	_model = "crm.offer.item.roles"
	_description = "CRM Offer Item Roles"
	_columns = ['item_id', 'role_id', 'patner_id']
