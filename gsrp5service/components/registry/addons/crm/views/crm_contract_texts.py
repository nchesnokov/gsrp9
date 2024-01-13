from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmContractTexts(ViewModelFind):
	_name = "model.find.crm.contract.texts"
	_model = "crm.contract.texts"
	_description = "Crm Contract Texts"
	_columns = ['contract_id', 'seq', 'text_id', 'descr']

class ViewModelO2MFormCrmContractTexts(ViewModelO2MForm):
	_name = "model.o2mform.crm.contract.texts"
	_model = "crm.contract.texts"
	_description = "Crm Contract Texts"
	_columns = ['contract_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MListCrmContractTexts(ViewModelO2MList):
	_name = "model.o2mlist.crm.contract.texts"
	_model = "crm.contract.texts"
	_description = "Crm Contract Texts"
	_columns = ['contract_id', 'seq', 'text_id', 'descr']
