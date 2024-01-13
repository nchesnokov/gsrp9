from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm

class ViewModelSearchCrmUnitChannelAssigments(ViewModelSearch):
	_name = "model.search.crm.unit.channel.assigments"
	_model = "crm.unit.channel.assigments"
	_description = "CRM Unit Of Channel Assigment"
	_columns = ['unit_id', 'channel_id', 'fullname']

class ViewModelFindCrmUnitChannelAssigments(ViewModelFind):
	_name = "model.find.crm.unit.channel.assigments"
	_model = "crm.unit.channel.assigments"
	_description = "CRM Unit Of Channel Assigment"
	_columns = ['unit_id', 'channel_id', 'fullname']

class ViewModelListCrmUnitChannelAssigments(ViewModelList):
	_name = "model.list.crm.unit.channel.assigments"
	_model = "crm.unit.channel.assigments"
	_description = "CRM Unit Of Channel Assigment"
	_columns = ['unit_id', 'channel_id', 'fullname']

class ViewModelFormModalCrmUnitChannelAssigments(ViewModelFormModal):
	_name = "model.form.modal.crm.unit.channel.assigments"
	_model = "crm.unit.channel.assigments"
	_description = "CRM Unit Of Channel Assigment"
	_columns = ['unit_id', 'channel_id', 'fullname']

class ViewModelFormCrmUnitChannelAssigments(ViewModelForm):
	_name = "model.form.crm.unit.channel.assigments"
	_model = "crm.unit.channel.assigments"
	_description = "CRM Unit Of Channel Assigment"
	_columns = ['unit_id', 'channel_id', 'fullname']
