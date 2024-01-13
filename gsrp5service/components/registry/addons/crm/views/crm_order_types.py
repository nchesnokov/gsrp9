from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmOrderTypes(ViewModelSearch):
	_name = "model.search.crm.order.types"
	_model = "crm.order.types"
	_description = "Types CRM Order"
	_columns = ['otype', 'name', 'htschema', 'itschema', 'required']

class ViewModelFindCrmOrderTypes(ViewModelFind):
	_name = "model.find.crm.order.types"
	_model = "crm.order.types"
	_description = "Types CRM Order"
	_columns = ['otype', 'name', 'htschema', 'itschema', 'required']

class ViewModelO2MFormCrmOrderTypes(ViewModelO2MForm):
	_name = "model.o2mform.crm.order.types"
	_model = "crm.order.types"
	_description = "Types CRM Order"
	_columns = ['otype', 'name', 'htschema', 'itschema', 'roles', 'tis', 'required', 'note']

class ViewModelO2MListCrmOrderTypes(ViewModelO2MList):
	_name = "model.o2mlist.crm.order.types"
	_model = "crm.order.types"
	_description = "Types CRM Order"
	_columns = ['otype', 'name', 'htschema', 'itschema', 'roles', 'tis', 'required']
