from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm

class ViewModelSearchCrmOfferTypes(ViewModelSearch):
	_name = "model.search.crm.offer.types"
	_model = "crm.offer.types"
	_description = "Types CRM Offer"
	_columns = ['name', 'htschema', 'itschema', 'note']

class ViewModelFindCrmOfferTypes(ViewModelFind):
	_name = "model.find.crm.offer.types"
	_model = "crm.offer.types"
	_description = "Types CRM Offer"
	_columns = ['name', 'htschema', 'itschema', 'note']

class ViewModelListCrmOfferTypes(ViewModelList):
	_name = "model.list.crm.offer.types"
	_model = "crm.offer.types"
	_description = "Types CRM Offer"
	_columns = ['name', 'htschema', 'itschema', 'roles', 'note']

class ViewModelFormModalCrmOfferTypes(ViewModelFormModal):
	_name = "model.form.modal.crm.offer.types"
	_model = "crm.offer.types"
	_description = "Types CRM Offer"
	_columns = ['name', 'htschema', 'itschema', 'roles', 'note']

class ViewModelFormCrmOfferTypes(ViewModelForm):
	_name = "model.form.crm.offer.types"
	_model = "crm.offer.types"
	_description = "Types CRM Offer"
	_columns = ['name', 'htschema', 'itschema', 'roles', 'note']
