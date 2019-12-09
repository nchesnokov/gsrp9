from orm import fields
from orm.model import Model

class wkf1_workplaces(Model):
	_name = 'wkf1.workplace'
	_description = 'General Workflow Workplaces'
	_columns = {
	'name': fields.varchar(label = 'Workplace'),
	'note': fields.text('Note')}

wkf1_workplaces()

class wkf1_element_categories(Model):
	_name = 'wkf1.element.categories'
	_description = 'General Workflow Element Category'
	_rec_name = None
	_columns = {
	'name': fields.varchar(label = 'Element'),
	'parent_id': fields.many2one(label='Parent',obj='wkf1.element.categories'),
	'childs_id': fields.one2many(label='Childs',obj='wkf1.element.categories',rel='parent_id'),
	'note': fields.text(label = 'Note')}

wkf1_element_categories()


class wkf1_elements(Model):
	_name = 'wkf1.elements'
	_description = 'General Workflow Element'
	_rec_name = None
	_columns = {
	'name': fields.varchar(label = 'Element'),
	'wkf_element_category_id': fields.many2one(label='Category',obj='wkf1.element.categories'),
	'etype': fields.selection(label='Type',selections=[('R','Route'),('P','Phase'),('T','Task'),('S','Stage'),('W','Workflow'),('I','Inode'),('C','Check'),('D','Deduction'),('A','Action'),('?','Multipleхor'),('I','Or'),('&','And'),('!','Not'),('^','Xor'),('#','Selector'),(';','Terminator')]),
	'note': fields.text(label = 'Note')}

wkf1_elements()


