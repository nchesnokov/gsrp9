from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmRequestPricingItems(ViewModelFind):
	_name = "model.find.crm.request.pricing.items"
	_model = "crm.request.pricing.items"
	_description = "CRM Request Item Pricing"
	_columns = ['item_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'price', 'cop', 'unit', 'uop', 'amount', 'currency']

class ViewModelO2MFormCrmRequestPricingItems(ViewModelO2MForm):
	_name = "model.o2mform.crm.request.pricing.items"
	_model = "crm.request.pricing.items"
	_description = "CRM Request Item Pricing"
	_columns = ['item_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'price', 'cop', 'unit', 'uop', 'amount', 'currency']

class ViewModelO2MListCrmRequestPricingItems(ViewModelO2MList):
	_name = "model.o2mlist.crm.request.pricing.items"
	_model = "crm.request.pricing.items"
	_description = "CRM Request Item Pricing"
	_columns = ['item_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'price', 'cop', 'unit', 'uop', 'amount', 'currency']
