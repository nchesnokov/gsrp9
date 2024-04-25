import os
import sys
import time
import logging
from functools import reduce
from gsrp5service.obj.metaobjects import MetaObjects
from tools.translations import trlocal as _
#from . import mm
#from .mm import orm_exception
#from .mm import Access

_logger = logging.getLogger(__name__)


class ViewController(object, metaclass = MetaObjects):
	_name = None
	_description = None

class ViewInheritController(object, metaclass = MetaObjects):
	_name = None

class ViewModelController(ViewController):
	_name = None
	_model_name = None
	_columns = []
	_standalone = True
	_actions = {}
	_order_actions = []

	def _action(self,name, kwargs):
		return self._actions[name]['method'](self, **kwargs)


class ViewModelInheritController(ViewInheritController):
	_model = None

class ViewModelCalendarController(ViewModelController):
	_view_type = 'ModelCalendar'

class ViewModelFormController(ViewModelController):
	_view_type = 'ModelForm'

class ViewModelFormModalController(ViewModelController):
	_view_type = 'ModelFormModal'

class ViewModelFindController(ViewModelController):
	_view_type = 'ModelFind'

class ViewModelFlowController(ViewModelController):
	_view_type = 'ModelFlow'

class ViewModelGanttController(ViewModelController):
	_view_type = 'ModelGantt'

class ViewModelGeoController(ViewModelController):
	_view_type = 'ModelGeo'

class ViewModelGraphController(ViewModelController):
	_view_type = 'ModelGraph'

class ViewModelKanbanController(ViewModelController):
	_view_type = 'ModelKanban'

class ViewModelListController(ViewModelController):
	_view_type = 'ModelList'

class ViewModelM2MListController(ViewModelController):
	_view_type = 'ModelM2MList'

class ViewModelMdxController(ViewModelController):
	_view_type = 'ModelMdx'

class ViewModelSearchController(ViewModelController):
	_view_type = 'ModelSearch'

	def __init__(self, kwargs=None):
		self._actions['sys:find'] = {'element':'button','type':'primaty','size':'small','icon':'Search','method':'_sys_action_find'}
		self._actions['sys:copy'] = {'element':'button','type':'primaty','size':'small','icon':'DocumentCopy','method':'_sys_action_copy'}
		self._actions['sys:new'] = {'element':'button','type':'primaty','size':'small','icon':'DocumentAdd','method':'_sys_action_new'}
		self._actions['sys:lookup'] = {'element':'button','type':'primaty','size':'small','icon':'View','method':'_sys_action_lookup'}
		self._actions['sys:new'] = {'element':'button','type':'primaty','size':'small','icon':'Edit','method':'_sys_action_edit'}
		self._actions['sys:new'] = {'element':'button','type':'primaty','size':'small','icon':'Delete','method':'_sys_action_delete'}
		self._actions['sys:upload'] = {'element':'button','type':'primaty','size':'small','icon':'Upload','method':'_sys_action_upload'}
		self._actions['sys:download'] = {'element':'button','type':'primaty','size':'small','icon':'Download','method':'_sys_action_download'}
		self._actions['sys:setting'] = {'element':'button','type':'primaty','size':'small','icon':'Setting','method':'_sys_action_view_setting'}

	def _show_toolbar_search(self):
		return True

	def _sys_action_find(self, kwargs):
		return ["call:action","find"]

	def _sys_action_copy(self, kwargs):
		return true

	def _sys_action_new(self, kwargs):
		return true

	def _sys_action_lookup(self, kwargs):
		return true

	def _sys_action_edit(self, kwargs):
		return true

	def _sys_action_delete(self, kwargs):
		return true

	def _sys_action_upload(self, kwargs):
		return true

	def _sys_action_download(self, kwargs):
		return true

	def _sys_action_view_setting(self, kwargs):
		return true

	def _sys_action_view_select_rows(self, kwargs):
		return true

class ViewModelScheduleController(ViewModelController):
	_view_type = 'ModelSchedule'

class ViewModelTreeController(ViewModelController):
	_view_type = 'ModelTree'

class ViewModelO2MCalendarController(ViewModelController):
	_view_type = 'ModelCalendar'

class ViewModelO2MFormController(ViewModelController):
	_view_type = 'ModelForm'

class ViewModelO2MFormModalController(ViewModelController):
	_view_type = 'ModelFormModal'

class ViewModelO2MFlowController(ViewModelController):
	_view_type = 'ModelFlow'

class ViewModelO2MGanttController(ViewModelController):
	_view_type = 'ModelGantt'

class ViewModelO2MGeoController(ViewModelController):
	_view_type = 'ModelGeo'

class ViewModelO2MGraphController(ViewModelController):
	_view_type = 'ModelGraph'

class ViewModelO2MKanbanController(ViewModelController):
	_view_type = 'ModelKanban'

class ViewModelO2MListController(ViewModelController):
	_view_type = 'ModelList'

class ViewModelO2MMdxController(ViewModelController):
	_view_type = 'ModelMdx'

class ViewModelO2MScheduleController(ViewModelController):
	_view_type = 'ModelSchedule'

class ViewModelO2MTreeController(ViewModelController):
	_view_type = 'ModelTree'
