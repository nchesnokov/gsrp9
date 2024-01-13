from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm

class ViewModelSearchCrmDivisionSubdivisionAssigments(ViewModelSearch):
	_name = "model.search.crm.division.subdivision.assigments"
	_model = "crm.division.subdivision.assigments"
	_description = "CRM Division Of Subdivision Assigment"
	_columns = ['division_id', 'subdivision_id', 'fullname']

class ViewModelFindCrmDivisionSubdivisionAssigments(ViewModelFind):
	_name = "model.find.crm.division.subdivision.assigments"
	_model = "crm.division.subdivision.assigments"
	_description = "CRM Division Of Subdivision Assigment"
	_columns = ['division_id', 'subdivision_id', 'fullname']

class ViewModelListCrmDivisionSubdivisionAssigments(ViewModelList):
	_name = "model.list.crm.division.subdivision.assigments"
	_model = "crm.division.subdivision.assigments"
	_description = "CRM Division Of Subdivision Assigment"
	_columns = ['division_id', 'subdivision_id', 'fullname']

class ViewModelFormModalCrmDivisionSubdivisionAssigments(ViewModelFormModal):
	_name = "model.form.modal.crm.division.subdivision.assigments"
	_model = "crm.division.subdivision.assigments"
	_description = "CRM Division Of Subdivision Assigment"
	_columns = ['division_id', 'subdivision_id', 'fullname']

class ViewModelFormCrmDivisionSubdivisionAssigments(ViewModelForm):
	_name = "model.form.crm.division.subdivision.assigments"
	_model = "crm.division.subdivision.assigments"
	_description = "CRM Division Of Subdivision Assigment"
	_columns = ['division_id', 'subdivision_id', 'fullname']
