from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmContractPricingItems(ViewModelFind):
	_name = "model.find.crm.contract.pricing.items"
	_model = "crm.contract.pricing.items"
	_description = "Crm Contract Item Pricing"
	_columns = ['item_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'price', 'cop', 'unit', 'uop', 'amount', 'currency']

class ViewModelO2MFormCrmContractPricingItems(ViewModelO2MForm):
	_name = "model.o2mform.crm.contract.pricing.items"
	_model = "crm.contract.pricing.items"
	_description = "Crm Contract Item Pricing"
	_columns = ['item_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'price', 'cop', 'unit', 'uop', 'amount', 'currency']

class ViewModelO2MListCrmContractPricingItems(ViewModelO2MList):
	_name = "model.o2mlist.crm.contract.pricing.items"
	_model = "crm.contract.pricing.items"
	_description = "Crm Contract Item Pricing"
	_columns = ['item_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'price', 'cop', 'unit', 'uop', 'amount', 'currency']
