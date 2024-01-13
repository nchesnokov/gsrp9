from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmOrderPricing(ViewModelFind):
	_name = "model.find.crm.order.pricing"
	_model = "crm.order.pricing"
	_description = "CRM Order Pricing"
	_columns = ['order_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'amount', 'currency']

class ViewModelO2MFormCrmOrderPricing(ViewModelO2MForm):
	_name = "model.o2mform.crm.order.pricing"
	_model = "crm.order.pricing"
	_description = "CRM Order Pricing"
	_columns = ['order_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'amount', 'currency']

class ViewModelO2MListCrmOrderPricing(ViewModelO2MList):
	_name = "model.o2mlist.crm.order.pricing"
	_model = "crm.order.pricing"
	_description = "CRM Order Pricing"
	_columns = ['order_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'amount', 'currency']
