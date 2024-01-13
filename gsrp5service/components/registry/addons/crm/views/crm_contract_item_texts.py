from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmContractItemTexts(ViewModelFind):
	_name = "model.find.crm.contract.item.texts"
	_model = "crm.contract.item.texts"
	_description = "Crm Contract Item Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr']

class ViewModelO2MFormCrmContractItemTexts(ViewModelO2MForm):
	_name = "model.o2mform.crm.contract.item.texts"
	_model = "crm.contract.item.texts"
	_description = "Crm Contract Item Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MListCrmContractItemTexts(ViewModelO2MList):
	_name = "model.o2mlist.crm.contract.item.texts"
	_model = "crm.contract.item.texts"
	_description = "Crm Contract Item Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr']
