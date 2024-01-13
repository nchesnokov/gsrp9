from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmRequestPricing(ViewModelFind):
	_name = "model.find.crm.request.pricing"
	_model = "crm.request.pricing"
	_description = "CRM Request Pricing"
	_columns = ['request_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'amount', 'currency']

class ViewModelO2MFormCrmRequestPricing(ViewModelO2MForm):
	_name = "model.o2mform.crm.request.pricing"
	_model = "crm.request.pricing"
	_description = "CRM Request Pricing"
	_columns = ['request_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'amount', 'currency']

class ViewModelO2MListCrmRequestPricing(ViewModelO2MList):
	_name = "model.o2mlist.crm.request.pricing"
	_model = "crm.request.pricing"
	_description = "CRM Request Pricing"
	_columns = ['request_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'amount', 'currency']
