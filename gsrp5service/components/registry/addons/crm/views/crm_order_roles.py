from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmOrderRoles(ViewModelFind):
	_name = "model.find.crm.order.roles"
	_model = "crm.order.roles"
	_description = "CRM Order Roles"
	_columns = ['order_id', 'role_id', 'patner_id']

class ViewModelO2MFormCrmOrderRoles(ViewModelO2MForm):
	_name = "model.o2mform.crm.order.roles"
	_model = "crm.order.roles"
	_description = "CRM Order Roles"
	_columns = ['order_id', 'role_id', 'patner_id']

class ViewModelO2MListCrmOrderRoles(ViewModelO2MList):
	_name = "model.o2mlist.crm.order.roles"
	_model = "crm.order.roles"
	_description = "CRM Order Roles"
	_columns = ['order_id', 'role_id', 'patner_id']
