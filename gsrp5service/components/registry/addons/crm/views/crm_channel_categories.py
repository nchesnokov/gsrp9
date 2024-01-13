from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelTree
from gsrp5service.obj.view import ViewModelO2MTree
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmChannelCategories(ViewModelSearch):
	_name = "model.search.crm.channel.categories"
	_model = "crm.channel.categories"
	_description = "Categories CRM Chanel"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelFindCrmChannelCategories(ViewModelFind):
	_name = "model.find.crm.channel.categories"
	_model = "crm.channel.categories"
	_description = "Categories CRM Chanel"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MFormCrmChannelCategories(ViewModelO2MForm):
	_name = "model.o2mform.crm.channel.categories"
	_model = "crm.channel.categories"
	_description = "Categories CRM Chanel"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'channels', 'note']

class ViewModelTreeCrmChannelCategories(ViewModelTree):
	_name = "model.tree.crm.channel.categories"
	_model = "crm.channel.categories"
	_description = "Categories CRM Chanel"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MTreeCrmChannelCategories(ViewModelO2MTree):
	_name = "model.o2mtree.crm.channel.categories"
	_model = "crm.channel.categories"
	_description = "Categories CRM Chanel"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MListCrmChannelCategories(ViewModelO2MList):
	_name = "model.o2mlist.crm.channel.categories"
	_model = "crm.channel.categories"
	_description = "Categories CRM Chanel"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'channels', 'note']
