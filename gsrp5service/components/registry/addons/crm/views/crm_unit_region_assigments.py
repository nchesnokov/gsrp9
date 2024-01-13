from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm

class ViewModelSearchCrmUnitRegionAssigments(ViewModelSearch):
	_name = "model.search.crm.unit.region.assigments"
	_model = "crm.unit.region.assigments"
	_description = "CRM Unit Of Region Assigment"
	_columns = ['unit_id', 'region_id', 'fullname']

class ViewModelFindCrmUnitRegionAssigments(ViewModelFind):
	_name = "model.find.crm.unit.region.assigments"
	_model = "crm.unit.region.assigments"
	_description = "CRM Unit Of Region Assigment"
	_columns = ['unit_id', 'region_id', 'fullname']

class ViewModelListCrmUnitRegionAssigments(ViewModelList):
	_name = "model.list.crm.unit.region.assigments"
	_model = "crm.unit.region.assigments"
	_description = "CRM Unit Of Region Assigment"
	_columns = ['unit_id', 'region_id', 'fullname']

class ViewModelFormModalCrmUnitRegionAssigments(ViewModelFormModal):
	_name = "model.form.modal.crm.unit.region.assigments"
	_model = "crm.unit.region.assigments"
	_description = "CRM Unit Of Region Assigment"
	_columns = ['unit_id', 'region_id', 'fullname']

class ViewModelFormCrmUnitRegionAssigments(ViewModelForm):
	_name = "model.form.crm.unit.region.assigments"
	_model = "crm.unit.region.assigments"
	_description = "CRM Unit Of Region Assigment"
	_columns = ['unit_id', 'region_id', 'fullname']
