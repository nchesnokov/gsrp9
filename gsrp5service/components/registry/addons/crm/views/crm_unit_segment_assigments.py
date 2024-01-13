from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm

class ViewModelSearchCrmUnitSegmentAssigments(ViewModelSearch):
	_name = "model.search.crm.unit.segment.assigments"
	_model = "crm.unit.segment.assigments"
	_description = "CRM Unit Of Segment Assigment"
	_columns = ['unit_id', 'segment_id', 'fullname']

class ViewModelFindCrmUnitSegmentAssigments(ViewModelFind):
	_name = "model.find.crm.unit.segment.assigments"
	_model = "crm.unit.segment.assigments"
	_description = "CRM Unit Of Segment Assigment"
	_columns = ['unit_id', 'segment_id', 'fullname']

class ViewModelListCrmUnitSegmentAssigments(ViewModelList):
	_name = "model.list.crm.unit.segment.assigments"
	_model = "crm.unit.segment.assigments"
	_description = "CRM Unit Of Segment Assigment"
	_columns = ['unit_id', 'segment_id', 'fullname']

class ViewModelFormModalCrmUnitSegmentAssigments(ViewModelFormModal):
	_name = "model.form.modal.crm.unit.segment.assigments"
	_model = "crm.unit.segment.assigments"
	_description = "CRM Unit Of Segment Assigment"
	_columns = ['unit_id', 'segment_id', 'fullname']

class ViewModelFormCrmUnitSegmentAssigments(ViewModelForm):
	_name = "model.form.crm.unit.segment.assigments"
	_model = "crm.unit.segment.assigments"
	_description = "CRM Unit Of Segment Assigment"
	_columns = ['unit_id', 'segment_id', 'fullname']
