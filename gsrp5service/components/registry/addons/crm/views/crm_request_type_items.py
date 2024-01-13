from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmRequestTypeItems(ViewModelFind):
	_name = "model.find.crm.request.type.items"
	_model = "crm.request.type.items"
	_description = "Role CRM Request Items"
	_columns = ['type_id', 'gti_id', 'itype_id', 'note']

class ViewModelO2MFormCrmRequestTypeItems(ViewModelO2MForm):
	_name = "model.o2mform.crm.request.type.items"
	_model = "crm.request.type.items"
	_description = "Role CRM Request Items"
	_columns = ['type_id', 'gti_id', 'itype_id', 'note']

class ViewModelO2MListCrmRequestTypeItems(ViewModelO2MList):
	_name = "model.o2mlist.crm.request.type.items"
	_model = "crm.request.type.items"
	_description = "Role CRM Request Items"
	_columns = ['type_id', 'gti_id', 'itype_id', 'note']
