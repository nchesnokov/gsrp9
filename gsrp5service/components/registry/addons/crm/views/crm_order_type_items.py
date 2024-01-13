from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmOrderTypeItems(ViewModelFind):
	_name = "model.find.crm.order.type.items"
	_model = "crm.order.type.items"
	_description = "Role CRM Order Items"
	_columns = ['type_id', 'gti_id', 'itype_id']

class ViewModelO2MFormCrmOrderTypeItems(ViewModelO2MForm):
	_name = "model.o2mform.crm.order.type.items"
	_model = "crm.order.type.items"
	_description = "Role CRM Order Items"
	_columns = ['type_id', 'gti_id', 'itype_id', 'note']

class ViewModelO2MListCrmOrderTypeItems(ViewModelO2MList):
	_name = "model.o2mlist.crm.order.type.items"
	_model = "crm.order.type.items"
	_description = "Role CRM Order Items"
	_columns = ['type_id', 'gti_id', 'itype_id']
