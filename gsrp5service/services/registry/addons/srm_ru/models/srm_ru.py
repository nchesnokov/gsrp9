from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

class i18n_ru_md_okpd2(Model):
	_name = 'i18n.ru.md.okpd2'
	_description = 'General Model Classifiers OKPD2'
	_rec_name = 'code'
	_columns= {
	'name': fields.varchar(label='Name',size=128,selectable=True),
	'code': fields.varchar(label='Code',size=12)
	}

i18n_ru_md_okpd2()

class i18n_ru_md_okved2(Model):
	_name = 'i18n.ru.md.okved2'
	_description = 'General Model Classifiers OKVED2'
	_rec_name ='code'
	_columns= {
	'name': fields.varchar(label='Name',size=128,selectable=True),
	'code': fields.varchar(label='Code',size=8)
	}

i18n_ru_md_okved2()

class i18n_ru_md_okof(Model):
	_name = 'i18n.ru.md.okof'
	_description = 'General Model Classifiers OKOF'
	_rec_name = 'code'
	_columns= {
	'name': fields.varchar(label='Name',size=128,selectable=True),
	'code': fields.varchar(label='Code',size=17)
	}

i18n_ru_md_okof()

class i18n_ru_md_okmto(Model):
	_name = 'i18n.ru.md.okmto'
	_description = 'General Model Classifiers OKMTO'
	_rec_name = 'code'
	_columns= {
	'name': fields.varchar(label='Name',size=128,selectable=True),
	'code': fields.varchar(label='Code',size=24)
	}

i18n_ru_md_okmto()


class i18n_ru_md_okato(Model):
	_name = 'i18n.ru.md.okato'
	_description = 'General Model Classifiers OKATO'
	_rec_name = 'code'
	_columns= {
	'name': fields.varchar(label='Name',size=128,selectable=True),
	'code': fields.varchar(label='Code',size=10)
	}

i18n_ru_md_okato()

class i18n_ru_md_okso(Model):
	_name = 'i18n.ru.md.okso'
	_description = 'General Model Classifiers OKSO'
	_recname = 'code'
	_columns= {
	'name': fields.varchar(label='Name',size=128,selectable=True),
	'code': fields.varchar(label='Code',size=13)
	}

i18n_ru_md_okso()

class i18n_ru_md_okopf(Model):
	_name = 'i18n.ru.md.okopf'
	_description = 'General Model Classifiers OKOPF'
	_recname = 'code'
	_columns= {
	'name': fields.varchar(label='Name',size=128,selectable=True),
	'code': fields.varchar(label='Code',size=5)
	}

i18n_ru_md_okopf()

class i18n_ru_md_okud(Model):
	_name = 'i18n.ru.md.okud'
	_description = 'General Model Classifiers OKUD'
	_rec_name = 'code'
	_columns= {
	'name': fields.varchar(label='Name',size=128,selectable=True),
	'code': fields.varchar(label='Code',size=7)
	}

i18n_ru_md_okud()

class i18n_ru_md_tnved(Model):
	_name = 'i18n.ru.md.tnved'
	_description = 'General Model Classifiers TNVED'
	_rec_name = 'code'
	_columns= {
	'name': fields.varchar(label='Name',size=128,selectable=True),
	'code': fields.varchar(label='Code',size=10)
	}

i18n_ru_md_tnved()

class i18n_ru_md_okei(Model):
	_name = 'i18n.ru.md.okei'
	_description = 'General Model Classifiers OKEI'
	_rec_name = 'code'
	_columns= {
	'name': fields.varchar(label='Name',size=128,selectable=True),
	'code': fields.varchar(label='Code',size=3),
	'shortname': fields.varchar(label='Short Name',size=3),
	}

i18n_ru_md_okei()

class i18n_ru_md_okz(Model):
	_name = 'i18n.ru.md.okz'
	_description = 'General Model Classifiers OKZ'
	_rec_name = 'code'
	_columns= {
	'name': fields.varchar(label='Name',size=128,selectable=True),
	'code': fields.varchar(label='Code',size=3),
	'shortname': fields.varchar(label='Short Name',size=3),
	}

i18n_ru_md_okz()


class i18n_ru_srm_classifiers(ModelInherit):
	_name = 'i18n.ru.srm.classifiers'
	_description = 'General Model Classifiers OKEI'
	_inherit = {'srm.demand.items':{'_columns':['okpd2_id','okved2_id','okato_id']},'srm.part.items':{'_columns':['okpd2_id','okved2_id','okato_id']},'srm.request.items':{'_columns':['okpd2_id','okved2_id','okato_id']},'srm.offer.items':{'_columns':['okpd2_id','okved2_id','okato_id']},'srm.evolution.items':{'_columns':['okpd2_id','okved2_id','okato_id']},'srm.decision.items':{'_columns':['okpd2_id','okved2_id','okato_id']},'srm.contract.items':{'_columns':['okpd2_id','okved2_id','okato_id']}}
	_columns = {
	'okpd2_id': fields.many2one(label='OKPD2',obj='i18n.ru.md.okpd2',selectable=True),
	'okved2_id': fields.many2one(label='OKVED2',obj='i18n.ru.md.okved2',selectable=True),
	'okato_id': fields.many2one(label='OKATO',obj='i18n.ru.md.okato',selectable=True)
	}

i18n_ru_srm_classifiers()
