from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm

class ViewModelSearchLePricingGroupLevels(ViewModelSearch):
	_name = "model.search.le.pricing.group.levels"
	_model = "le.pricing.group.levels"
	_description = "Sale Pricing Group Levels"
	_columns = ['code', 'descr']

class ViewModelFindLePricingGroupLevels(ViewModelFind):
	_name = "model.find.le.pricing.group.levels"
	_model = "le.pricing.group.levels"
	_description = "Sale Pricing Group Levels"
	_columns = ['code', 'descr']

class ViewModelListLePricingGroupLevels(ViewModelList):
	_name = "model.list.le.pricing.group.levels"
	_model = "le.pricing.group.levels"
	_description = "Sale Pricing Group Levels"
	_columns = ['code', 'descr']

class ViewModelFormModalLePricingGroupLevels(ViewModelFormModal):
	_name = "model.form.modal.le.pricing.group.levels"
	_model = "le.pricing.group.levels"
	_description = "Sale Pricing Group Levels"
	_columns = ['code', 'descr']

class ViewModelFormLePricingGroupLevels(ViewModelForm):
	_name = "model.form.le.pricing.group.levels"
	_model = "le.pricing.group.levels"
	_description = "Sale Pricing Group Levels"
	_columns = ['code', 'descr']
