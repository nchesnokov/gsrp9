from gsrp5service.orm import fields
from gsrp5service.orm.model import Model,ModelInherit

class md_project_product(Model):
	_name = 'md.project.product'
	_description = 'General Model Project Of Product'
	_columns = {
	'product_id': fields.many2one(label='Product',obj='md.product'),
	'vat': fields.many2one(label='VAT Code',obj='md.vat.code',domain=[('type_vat','in',('p','n'))]),
	'uom': fields.many2one(label="Unit Of Measure",obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'note': fields.text(label = 'Note'),
	}

md_project_product()

class md_project_product_inherit(ModelInherit):
	_name = 'md.project.product.inherit'
	_description = 'Genaral Model Inherit For project Product'
	_inherit = {'md.product':{'_columns':['project']},'md.recepture':{'_columns':['usage']}}
	_columns = {
		'project': fields.one2many(label='Project',obj='md.project.product',rel='product_id'),
		'usage': fields.iSelection(selections=[('j','Project')])
	}
	
md_project_product_inherit()

class project_resource_category(Model):
	_name = 'project.resource.category'
	_description = 'General Model Category Project Resource'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='project.resource.category'),
	'childs_id': fields.one2many(obj = 'project.resource.category',rel = 'parent_id',label = 'Childs'),
	'projects': fields.one2many(label='Projects',obj='project.resource',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

project_resource_category()

class project_bill_category(Model):
	_name = 'project.bill.category'
	_description = 'General Model Category Project Bill'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='project.bill.category'),
	'childs_id': fields.one2many(obj = 'project.bill.category',rel = 'parent_id',label = 'Childs'),
	'bills': fields.one2many(label='Bills',obj='project.bill',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

project_bill_category()

class project_portfolio_category(Model):
	_name = 'project.portfolio.category'
	_description = 'General Model Category Project Portfolio'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='project.portfolio.category'),
	'childs_id': fields.one2many(obj = 'project.portfolio.category',rel = 'parent_id',label = 'Childs'),
	'portfolios': fields.one2many(label='Portfolios',obj='project.portfolio',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

project_portfolio_category()

class project_project_category(Model):
	_name = 'project.project.category'
	_description = 'General Model Category Project Project'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='project.project.category'),
	'childs_id': fields.one2many(obj = 'project.project.category',rel = 'parent_id',label = 'Childs'),
	'projects': fields.one2many(label='Projects',obj='project.project',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

project_project_category()

class project_stage_category(Model):
	_name = 'project.stage.category'
	_description = 'General Model Category Project Stage'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='project.stage.category'),
	'childs_id': fields.one2many(obj = 'project.stage.category',rel = 'parent_id',label = 'Childs'),
	'stages': fields.one2many(label='Orders',obj='project.stage',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

project_stage_category()

class project_task_category(Model):
	_name = 'project.task.category'
	_description = 'General Model Category Project Task'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='project.task.category'),
	'childs_id': fields.one2many(obj = 'project.task.category',rel = 'parent_id',label = 'Childs'),
	'tasks': fields.one2many(label='Tasks',obj='project.task',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

project_task_category()

class project_element_category(Model):
	_name = 'project.element.category'
	_description = 'General Model Category Project Element'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='project.element.category'),
	'childs_id': fields.one2many(obj = 'project.element.category',rel = 'parent_id',label = 'Childs'),
	'elements': fields.one2many(label='Elements',obj='project.element',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

project_element_category()

class project_resource(Model):
	_name = 'project.resource'
	_description = 'General Model Project Resource'
	_columns = {
	'name': fields.varchar(label = 'Resource',translate=True),
	'category_id': fields.many2one(label='Category',obj='project.resource.category'),
	'cost': fields.numeric(label='Cost',size=(11,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'note': fields.text('Note')
	}

project_resource()

class project_bill(Model):
	_name = 'project.bill'
	_description = 'General Model Projects Bill'
	_columns = {
	'name': fields.varchar(label = 'Bill'),
	'category_id': fields.many2one(label='Category',obj='project.bill.category'),
	'parent_id': fields.many2one(label='Parent',obj='project.bill'),
	'childs_id': fields.one2many(label='Childs',obj='project.bill',rel='parent_id'),
	'start_date': fields.datetime(label='Start date',timezone=True,required=True),
	'end_date': fields.datetime(label='End date',timezone=True,required=True),
	'progress': fields.numeric(label='Progress',size=(5,2),check='progress <= 100.00'),
	'project_type': fields.selection(label='Project Type',selections=[('project','Project'),('milestone','Milestone'),('task','Task')],readonly=True),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'portfolios': fields.one2many(label='Portfolios',obj='project.portfolio',rel='bill_id'),
	'note': fields.text('Note')
	}

	_default = {
		'state':'draft',
		'project_type':'project'
	}

project_bill()

class project_portfolio(Model):
	_name = 'project.portfolio'
	_description = 'General Model Projects Portfolio'
	_columns = {
	'bill_id': fields.many2one(label='Bill',obj='project.bill'),
	'name': fields.varchar(label = 'Portfolio'),
	'category_id': fields.many2one(label='Category',obj='project.portfolio.category'),
	'parent_id': fields.many2one(label='Parent',obj='project.portfolio'),
	'childs_id': fields.one2many(label='Childs',obj='project.portfolio',rel='parent_id'),
	'start_date': fields.datetime(label='Start date',timezone=True,required=True),
	'end_date': fields.datetime(label='End date',timezone=True,required=True),
	'progress': fields.numeric(label='Progress',size=(5,2),check='progress <= 100.00'),
	'project_type': fields.selection(label='Project Type',selections=[('project','Project'),('milestone','Milestone'),('task','Task')],readonly=True),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'projects': fields.one2many(label='Projects',obj='project.project',rel='portfolio_id'),
	'note': fields.text('Note')
	}

	_default = {
		'state':'draft',
		'project_type':'project'

	}

project_portfolio()

class project_project(Model):
	_name = 'project.project'
	_description = 'General Model Project'
	_columns = {
	'portfolio_id': fields.many2one(label='Portfolio',obj='project.portfolio'),
	'name': fields.varchar(label = 'Project'),
	'category_id': fields.many2one(label='Category',obj='project.project.category'),
	'parent_id': fields.many2one(label='Parent',obj='project.project'),
	'childs_id': fields.one2many(label='Childs',obj='project.project',rel='parent_id'),
	'start_date': fields.datetime(label='Start date',timezone=True,required=True),
	'end_date': fields.datetime(label='End date',timezone=True,required=True),
	'progress': fields.numeric(label='Progress',size=(5,2),check='progress <= 100.00'),
	'project_type': fields.selection(label='Project Type',selections=[('project','Project'),('milestone','Milestone'),('task','Task')],readonly=True),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'stages': fields.one2many(label='Stages',obj='project.stage',rel='project_id'),
	'note': fields.text('Note')
	}

	_default = {
		'state':'draft',
		'project_type':'project'
	}

project_project()

class project_stage(Model):
	_name = 'project.stage'
	_description = 'General Model Project Stage'
	_columns = {
	'project_id': fields.many2one(label='Project',obj='project.project', on_delete='c', on_update='c'),
	'name': fields.varchar(label = 'Stage'),
	'type': fields.selection(label='Type',selections=[('b','Begin'),('e','End'),('w','Work'),('s','Situtation')]),
	'parent_id': fields.many2one(label='Parent',obj='project.stage'),
	'childs_id': fields.one2many(label='Childs',obj='project.stage',rel='parent_id'),
	'start_date': fields.datetime(label='Start date',timezone=True,required=True),
	'end_date': fields.datetime(label='End date',timezone=True,required=True),
	'progress': fields.numeric(label='Progress',size=(5,2),check='progress <= 100.00'),
	'project_type': fields.selection(label='Type',selections=[('project','Project'),('milestone','Milestone'),('task','Task')],readonly=True),	
	'state': fields.selection(label='Project State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'tasks': fields.one2many(label='Tasks',obj='project.task',rel='stage_id'),
	'elements': fields.one2many(label='Elements',obj='project.element',rel='stage_id'),
	'note': fields.text('Note')
	}

	_default = {
		'state':'draft',
		'project_type':'milestone'
	}

project_stage()

class project_task(Model):
	_name = 'project.task'
	_description = 'General Model Project Task'
	_columns = {
	'stage_id': fields.many2one(label='Stage',obj='project.stage', on_delete='c', on_update='c',selectable=True,required=True),
	'name': fields.varchar(label = 'Task',translate=True),
	'category_id': fields.many2one(label='Category',obj='project.task.category'),
	'parent_id': fields.many2one(label='Parent',obj='project.task'),
	'childs_id': fields.one2many(label='Childs',obj='project.task',rel='parent_id'),
	'start_date': fields.datetime(label='Start date',timezone=True,required=True),
	'end_date': fields.datetime(label='End date',timezone=True,required=True),
	'progress': fields.numeric(label='Progress',size=(5,2),check='progress <= 100.00'),
	'project_type': fields.selection(label='Project Type',selections=[('project','Project'),('milestone','Milestone'),('task','Task')],readonly=True),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'resources': fields.one2many(label='Recources',obj='project.task.resources',rel='task_id'),
	'note': fields.text('Note')
	}

	_default = {
		'state':'draft',
		'project_type': 'task'
	}

project_task()

class project_element(Model):
	_name = 'project.element'
	_description = 'General Model Project Element'
	_columns = {
	'stage_id': fields.many2one(label='Stage',obj='project.stage', on_delete='c', on_update='c', selectable=True, required=True),
	'name': fields.varchar(label = 'Element',translate=True),
	'parent_id': fields.many2one(label='Parent',obj='project.element'),
	'childs_id': fields.one2many(label='Childs',obj='project.element',rel='parent_id'),
	'products': fields.one2many(label='Products',obj='project.element.products',rel='element_id'),
	'resources': fields.one2many(label='Resources',obj='project.element.resources',rel='element_id'),
	'note': fields.text('Note')
	}

project_element()

class project_element_products(Model):
	_name = 'project.element.products'
	_description = 'General Model Project Element Products'
	_columns = {
	'element_id': fields.many2one(label='Element',obj='project.element', on_delete='c', on_update='c',selectable=True,required=True),
	'product_id': fields.many2one(label = 'Product',obj='md.product'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'note': fields.text('Note')
	}

project_element_products()

class project_task_resources(Model):
	_name = 'project.task.resources'
	_description = 'General Model Project Task Resources'
	_columns = {
	'task_id': fields.many2one(label = 'Task',obj='project.task', on_delete='c', on_update='c',required=True),
	'resource_id': fields.many2one(label = 'Resource',obj='project.resource', on_delete='c', on_update='c',required=True),
	'quantiny': fields.integer(label='Job',required=True),
	'uom': fields.many2one(label='Unit Of Measure',obj='md.uom',domain=[('quantity_id','=','Time')])
	}

project_task_resources()

class project_element_resources(Model):
	_name = 'project.element.resources'
	_description = 'General Model Project Element Resources'
	_columns = {
	'element_id': fields.many2one(label = 'Element',obj='project.element', on_delete='c', on_update='c',required=True),
	'resource_id': fields.many2one(label = 'Resource',obj='project.resource', on_delete='c', on_update='c',required=True),
	'quantiny': fields.integer(label='Job',required=True),
	'uom': fields.many2one(label='Unit Of Measure',obj='md.uom',domain=[('quantity_id','=','Time')])
	}

project_element_resources()
