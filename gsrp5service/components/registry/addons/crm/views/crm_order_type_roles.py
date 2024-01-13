from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmOrderTypeRoles(ViewModelFind):
	_name = "model.find.crm.order.type.roles"
	_model = "crm.order.type.roles"
	_description = "Role Sale Order Types"
	_columns = ['type_id', 'role_id']

class ViewModelO2MFormCrmOrderTypeRoles(ViewModelO2MForm):
	_name = "model.o2mform.crm.order.type.roles"
	_model = "crm.order.type.roles"
	_description = "Role Sale Order Types"
	_columns = ['type_id', 'role_id', 'note']

class ViewModelO2MListCrmOrderTypeRoles(ViewModelO2MList):
	_name = "model.o2mlist.crm.order.type.roles"
	_model = "crm.order.type.roles"
	_description = "Role Sale Order Types"
	_columns = ['type_id', 'role_id']
