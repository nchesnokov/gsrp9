from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelTree
from gsrp5service.obj.view import ViewModelO2MTree
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmOfferCategories(ViewModelSearch):
	_name = "model.search.crm.offer.categories"
	_model = "crm.offer.categories"
	_description = "Category CRM Offer"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelFindCrmOfferCategories(ViewModelFind):
	_name = "model.find.crm.offer.categories"
	_model = "crm.offer.categories"
	_description = "Category CRM Offer"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MFormCrmOfferCategories(ViewModelO2MForm):
	_name = "model.o2mform.crm.offer.categories"
	_model = "crm.offer.categories"
	_description = "Category CRM Offer"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'offers', 'note']

class ViewModelTreeCrmOfferCategories(ViewModelTree):
	_name = "model.tree.crm.offer.categories"
	_model = "crm.offer.categories"
	_description = "Category CRM Offer"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MTreeCrmOfferCategories(ViewModelO2MTree):
	_name = "model.o2mtree.crm.offer.categories"
	_model = "crm.offer.categories"
	_description = "Category CRM Offer"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MListCrmOfferCategories(ViewModelO2MList):
	_name = "model.o2mlist.crm.offer.categories"
	_model = "crm.offer.categories"
	_description = "Category CRM Offer"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'offers', 'note']
