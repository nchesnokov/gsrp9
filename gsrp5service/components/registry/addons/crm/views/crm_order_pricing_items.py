from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmOrderPricingItems(ViewModelFind):
	_name = "model.find.crm.order.pricing.items"
	_model = "crm.order.pricing.items"
	_description = "CRM Order Item Pricing"
	_columns = ['item_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'price', 'cop', 'unit', 'uop', 'amount', 'currency']

class ViewModelO2MFormCrmOrderPricingItems(ViewModelO2MForm):
	_name = "model.o2mform.crm.order.pricing.items"
	_model = "crm.order.pricing.items"
	_description = "CRM Order Item Pricing"
	_columns = ['item_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'price', 'cop', 'unit', 'uop', 'amount', 'currency']

class ViewModelO2MListCrmOrderPricingItems(ViewModelO2MList):
	_name = "model.o2mlist.crm.order.pricing.items"
	_model = "crm.order.pricing.items"
	_description = "CRM Order Item Pricing"
	_columns = ['item_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'price', 'cop', 'unit', 'uop', 'amount', 'currency']
