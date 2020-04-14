
from gsrp5service.orm import fields
from gsrp5service.orm.model import Model,ModelInherit


#Organization structure
class fm_unit_categories(Model):
	_name = 'fm.unit.categories'
	_description = 'General Model Categories Financial Management Unit'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='fm.unit.categories'),
	'childs_id': fields.one2many(obj = 'fm.unit.categories',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'units': fields.one2many(label='Units',obj='fm.units',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

fm_unit_categories()


class fm_units(Model):
	_name = 'fm.units'
	_description = 'General Model Financial Management Units'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='fm.unit.categories'),
	'company_id': fields.many2many(label='Companies',obj='md.company', rel='md_company_fm_unit_rel', id2='unit_id', id1='company_id'),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	#'channels': fields.one2many(label='Channels',obj='srm.unit.channel.assigments',rel='unit_id'),
	#'segments': fields.one2many(label='Segments',obj='srm.unit.segment.assigments',rel='unit_id'),
	#'areas': fields.one2many(label='Areas',obj='srm.unit.area.assigments',rel='unit_id'),
	#'regions': fields.one2many(label='Regions',obj='srm.unit.region.assigments',rel='unit_id')
	}

fm_units()

class fm_currency_exchanges(Model):
	_name = 'fm.currency.exchanges'
	_description = 'General Model Currency Exchange'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'code': fields.varchar(label = 'Code',size=12,translate=True),
	'short_name': fields.varchar(label = 'Short Name',translate=True),
	'name': fields.varchar(label = 'Name',translate=True),
	'country': fields.many2one(label='Country',obj='md.country'),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'pob': fields.boolean(label='Place of Bidding'),
	'note':fields.text(label = 'Note',translate=True)
	}

fm_currency_exchanges()

# old
class fcm_departament_categories(Model):
	_name = 'fcm.departament.categories'
	_description = 'General Model FCM Departament Category'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='fcm.departament.categories'),
	'childs_id': fields.one2many(obj = 'fcm.departament.categories',rel = 'parent_id',label = 'Childs'),
	'departaments': fields.one2many(label='Departaments',obj='fcm.departaments',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

fcm_departament_categories()


class fcm_obj_categories(Model):
	_name = 'fcm.obj.categories'
	_description = 'General Model FCM Object Category'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='fcm.obj.categories'),
	'childs_id': fields.one2many(obj = 'fcm.obj.categories',rel = 'parent_id',label = 'Childs'),
	'objs': fields.one2many(label='Objects',obj='fcm.objs',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

fcm_obj_categories()

class fcm_article_categories(Model):
	_name = 'fcm.article.categories'
	_description = 'General Model FCM Article Category'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='fcm.article.categories'),
	'childs_id': fields.one2many(obj = 'fcm.article.categories',rel = 'parent_id',label = 'Childs'),
	'articles': fields.one2many(label='Articles',obj='fcm.articles',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

fcm_article_categories()


class fcm_departaments(Model):
	_name = 'fcm.departaments'
	_description = 'General Model FCM Departament'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='fcm.departament.categories'),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'note': fields.text(label = 'Note')
	}
	
fcm_departaments()

class fcm_objs(Model):
	_name = 'fcm.objs'
	_description = 'General Model FCM Object'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'usage': fields.selection(label='Usage',selections=[('f','Fund'),('g','Grant')]),
	'category_id': fields.many2one(label='Category',obj='fcm.obj.categories'),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
	'usage':'f'
	}
	
fcm_objs()

class fcm_articles(Model):
	_name = 'fcm.articles'
	_description = 'General Model FCM Article'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='fcm.article.categories'),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'note': fields.text(label = 'Note')
	}
	
fcm_articles()

# for company
class fcm_company_departaments(Model):
	_name = 'fcm.company.departaments'
	_description = 'General Model FCM Departament Of Company'
	_columns = {
	'company_id': fields.many2one(label='Company',obj='md.company',required=True),
	'departament_id': fields.many2one(label='Departamant',obj='fcm.departaments'),
	'fullname': fields.varchar(label='Fullname', compute='_compute_fullname'),
	'note': fields.text(label = 'Note')
	}
	
	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''
		if 'company_id' in item and 'name' in item['company_id'] and item['company_id']['name']:
			v += item['company_id']['name']

		if 'departament_id' in item and 'name' in item['departament_id'] and item['departament_id']['name']:
			v += '/' + item['departament_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v
			
fcm_company_departaments()

class fcm_company_objs(Model):
	_name = 'fcm.company.objs'
	_description = 'General Model FCM Object Of Company'
	_columns = {
	'company_id': fields.many2one(label='Company',obj='md.company',required=True),
	'obj_id': fields.many2one(label='Object',obj='fcm.objs'),
	'fullname': fields.varchar(label='Fullname', compute='_compute_fullname'),
	'note': fields.text(label = 'Note')
	}
	
	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''
		if 'company_id' in item and 'name' in item['company_id'] and item['company_id']['name']:
			v += item['company_id']['name']

		if 'obj_id' in item and 'name' in item['obj_id'] and item['obj_id']['name']:
			v += '/' + item['obj_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v

fcm_company_objs()

class fcm_company_articles(Model):
	_name = 'fcm.company.articles'
	_description = 'General Model FCM Article Of Company'
	_columns = {
	'company_id': fields.many2one(label='Company',obj='md.company',required=True),
	'article_id': fields.many2one(label='Article',obj='fcm.articles'),
	'fullname': fields.varchar(label='Fullname', compute='_compute_fullname'),
	'note': fields.text(label = 'Note')
	}
	
	def _compute_fullname(self,cr,pool,uid,item,context):
		v=''
		if 'company_id' in item and 'name' in item['company_id'] and item['company_id']['name']:
			v += item['company_id']['name']

		if 'article_id' in item and 'name' in item['article_id'] and item['article_id']['name']:
			v += '/' + item['article_id']['name']
		
		if len(v) > 0:
			item['fullname'] = v
		
fcm_company_articles()

# for company end

class md_fcm_company_inherit(ModelInherit):
	_name = 'md.fcm.company.inherit'
	_description = 'Genaral Model Inherit For Company'
	_inherit = {'md.company':{'_columns':['fcm_departaments','fcm_objs','fcm_articles']}}
	_columns = {
		'fcm_departaments': fields.one2many(label='Departaments',obj='fcm.company.departaments',rel='company_id'),
		'fcm_objs': fields.one2many(label='Objects',obj='fcm.company.objs',rel='company_id'),
		'fcm_articles': fields.one2many(label='Articles',obj='fcm.company.articles',rel='company_id'),
	}
	
md_fcm_company_inherit()
