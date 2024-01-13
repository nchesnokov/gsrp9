from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm

class ViewModelSearchCrmUnitAreaAssigments(ViewModelSearch):
	_name = "model.search.crm.unit.area.assigments"
	_model = "crm.unit.area.assigments"
	_description = "CRM Unit Of Area Assigment"
	_columns = ['unit_id', 'area_id', 'fullname']

class ViewModelFindCrmUnitAreaAssigments(ViewModelFind):
	_name = "model.find.crm.unit.area.assigments"
	_model = "crm.unit.area.assigments"
	_description = "CRM Unit Of Area Assigment"
	_columns = ['unit_id', 'area_id', 'fullname']

class ViewModelListCrmUnitAreaAssigments(ViewModelList):
	_name = "model.list.crm.unit.area.assigments"
	_model = "crm.unit.area.assigments"
	_description = "CRM Unit Of Area Assigment"
	_columns = ['unit_id', 'area_id', 'fullname']

class ViewModelFormModalCrmUnitAreaAssigments(ViewModelFormModal):
	_name = "model.form.modal.crm.unit.area.assigments"
	_model = "crm.unit.area.assigments"
	_description = "CRM Unit Of Area Assigment"
	_columns = ['unit_id', 'area_id', 'fullname']

class ViewModelFormCrmUnitAreaAssigments(ViewModelForm):
	_name = "model.form.crm.unit.area.assigments"
	_model = "crm.unit.area.assigments"
	_description = "CRM Unit Of Area Assigment"
	_columns = ['unit_id', 'area_id', 'fullname']
