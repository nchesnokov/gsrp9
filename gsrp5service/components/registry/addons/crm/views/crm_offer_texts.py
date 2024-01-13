from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmOfferTexts(ViewModelFind):
	_name = "model.find.crm.offer.texts"
	_model = "crm.offer.texts"
	_description = "CRM Offer Texts"
	_columns = ['offer_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MFormCrmOfferTexts(ViewModelO2MForm):
	_name = "model.o2mform.crm.offer.texts"
	_model = "crm.offer.texts"
	_description = "CRM Offer Texts"
	_columns = ['offer_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MListCrmOfferTexts(ViewModelO2MList):
	_name = "model.o2mlist.crm.offer.texts"
	_model = "crm.offer.texts"
	_description = "CRM Offer Texts"
	_columns = ['offer_id', 'seq', 'text_id', 'descr', 'content']
