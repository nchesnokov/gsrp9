from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmOrderItemRoles(ViewModelFind):
	_name = "model.find.crm.order.item.roles"
	_model = "crm.order.item.roles"
	_description = "CRM Order Roles"
	_columns = ['item_id', 'role_id', 'patner_id']

class ViewModelO2MFormCrmOrderItemRoles(ViewModelO2MForm):
	_name = "model.o2mform.crm.order.item.roles"
	_model = "crm.order.item.roles"
	_description = "CRM Order Roles"
	_columns = ['item_id', 'role_id', 'patner_id']

class ViewModelO2MListCrmOrderItemRoles(ViewModelO2MList):
	_name = "model.o2mlist.crm.order.item.roles"
	_model = "crm.order.item.roles"
	_description = "CRM Order Roles"
	_columns = ['item_id', 'role_id', 'patner_id']
