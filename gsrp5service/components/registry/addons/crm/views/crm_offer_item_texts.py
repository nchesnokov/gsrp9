from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmOfferItemTexts(ViewModelFind):
	_name = "model.find.crm.offer.item.texts"
	_model = "crm.offer.item.texts"
	_description = "CRM Offer Item Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MFormCrmOfferItemTexts(ViewModelO2MForm):
	_name = "model.o2mform.crm.offer.item.texts"
	_model = "crm.offer.item.texts"
	_description = "CRM Offer Item Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MListCrmOfferItemTexts(ViewModelO2MList):
	_name = "model.o2mlist.crm.offer.item.texts"
	_model = "crm.offer.item.texts"
	_description = "CRM Offer Item Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr', 'content']
