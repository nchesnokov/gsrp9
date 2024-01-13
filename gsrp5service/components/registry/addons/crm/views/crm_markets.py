from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm

class ViewModelSearchCrmMarkets(ViewModelSearch):
	_name = "model.search.crm.markets"
	_model = "crm.markets"
	_description = "CRM Market"
	_columns = ['unit_id', 'channel_id', 'segment_id', 'area_id', 'region_id', 'fullname', 'note']

class ViewModelFindCrmMarkets(ViewModelFind):
	_name = "model.find.crm.markets"
	_model = "crm.markets"
	_description = "CRM Market"
	_columns = ['unit_id', 'channel_id', 'segment_id', 'area_id', 'region_id', 'fullname', 'note']

class ViewModelListCrmMarkets(ViewModelList):
	_name = "model.list.crm.markets"
	_model = "crm.markets"
	_description = "CRM Market"
	_columns = ['unit_id', 'channel_id', 'segment_id', 'area_id', 'region_id', 'fullname', 'note']

class ViewModelFormModalCrmMarkets(ViewModelFormModal):
	_name = "model.form.modal.crm.markets"
	_model = "crm.markets"
	_description = "CRM Market"
	_columns = ['unit_id', 'channel_id', 'segment_id', 'area_id', 'region_id', 'fullname', 'note']

class ViewModelFormCrmMarkets(ViewModelForm):
	_name = "model.form.crm.markets"
	_model = "crm.markets"
	_description = "CRM Market"
	_columns = ['unit_id', 'channel_id', 'segment_id', 'area_id', 'region_id', 'fullname', 'note']
