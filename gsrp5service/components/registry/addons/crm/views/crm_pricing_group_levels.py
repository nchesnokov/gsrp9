from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm

class ViewModelSearchCrmPricingGroupLevels(ViewModelSearch):
	_name = "model.search.crm.pricing.group.levels"
	_model = "crm.pricing.group.levels"
	_description = "CRM Pricing Group Levels"
	_columns = ['code', 'descr']

class ViewModelFindCrmPricingGroupLevels(ViewModelFind):
	_name = "model.find.crm.pricing.group.levels"
	_model = "crm.pricing.group.levels"
	_description = "CRM Pricing Group Levels"
	_columns = ['code', 'descr']

class ViewModelListCrmPricingGroupLevels(ViewModelList):
	_name = "model.list.crm.pricing.group.levels"
	_model = "crm.pricing.group.levels"
	_description = "CRM Pricing Group Levels"
	_columns = ['code', 'descr']

class ViewModelFormModalCrmPricingGroupLevels(ViewModelFormModal):
	_name = "model.form.modal.crm.pricing.group.levels"
	_model = "crm.pricing.group.levels"
	_description = "CRM Pricing Group Levels"
	_columns = ['code', 'descr']

class ViewModelFormCrmPricingGroupLevels(ViewModelForm):
	_name = "model.form.crm.pricing.group.levels"
	_model = "crm.pricing.group.levels"
	_description = "CRM Pricing Group Levels"
	_columns = ['code', 'descr']
