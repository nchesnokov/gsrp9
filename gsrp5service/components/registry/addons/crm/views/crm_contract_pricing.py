from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmContractPricing(ViewModelFind):
	_name = "model.find.crm.contract.pricing"
	_model = "crm.contract.pricing"
	_description = "Crm Contract Pricing"
	_columns = ['contract_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'amount', 'currency']

class ViewModelO2MFormCrmContractPricing(ViewModelO2MForm):
	_name = "model.o2mform.crm.contract.pricing"
	_model = "crm.contract.pricing"
	_description = "Crm Contract Pricing"
	_columns = ['contract_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'amount', 'currency']

class ViewModelO2MListCrmContractPricing(ViewModelO2MList):
	_name = "model.o2mlist.crm.contract.pricing"
	_model = "crm.contract.pricing"
	_description = "Crm Contract Pricing"
	_columns = ['contract_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'amount', 'currency']
