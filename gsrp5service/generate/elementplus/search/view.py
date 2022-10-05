import os
import yaml
from yaml import Dumper
import json
from  os.path import join as opj

frameworkdir = 'elementplus'
framework = {'element-plus':'elementplus'}
viewtype = 'search'

def _generateTemplateColumns(meta,model,pool,context):
	_texts = meta['_texts']
	_maps = meta['_maps']
	prefix = ['template',framework[frameworkdir],viewtype,'prefix'].join('-')
	cs = {}

	records = pool.get('bc.models').select(fields=['code','descr','momi',{'columns':['seq','col','moc']},{'inherits':['col']}],cond=[('code','=',model)],context=context)
	for record in records:
		for column in record['columns']:
			column['moc'] = json.loads(column['moc'])
			key =  ['template',framework[frameworkdir],viewtype,'item',column['moc']['type']].join('-')
			if key in _maps:
				key = _maps[key]
			
			if key in _texts:
				s = """\n\t\t<el-form-item :label="colsLabel['{0}']">\n""".format(column['col'])
				s += _text[key].format(column['col'])
				s += """\n\t\t</el-form-item>"""
				cs[key] = s
	
	return cs

def _generateTemplate(meta,model,pool,context):
	_texts = meta['_texts']
	_maps = meta['_maps']
	# prefix = '-'.join(['template',framework,viewtype,'prefix'])
	# s = ''
	# if prefix in _texts:
		# s = _texts[prefix]

	# #records = pool.get('bc.models').select(fields=['code','descr','momi',{'columns':['seq','col','moc']},{'inherits':['col']}],cond=[('code','=',model)],context=context)
	# columnsInfo = pool.get(model).columnsInfo()
	# for k in columnsInfo.keys():
		# if columnsInfo[k]['type'] in ('one2many','one2related'):
			# continue
		# key =  '-'.join(['template',framework,viewtype,'item',columnsInfo[k]['type']])
		# if key in _maps:
			# key = _maps[key]
		# if key in _texts:
			# s += """\n\t\t<el-form-item :label="t(colsLabel['{0}'])">\n""".format(k)
			# s += _texts[key] % tuple([k] * _texts[key].count("'%s'"))
			# s += """\n\t\t</el-form-item>"""
		
	# if  len(pool.get(model)._o2mfields) > 0:
		# key =  '-'.join(['template',framework,viewtype,'item','one2many'])
		# #s += """\n\t\t<el-form-item>\n"""
		# s += _texts[key]
		# #s += """\n\t\t</el-form-item>"""
		
	# suffix = '-'.join(['template',framework,viewtype,'suffix'])
	# if suffix in _texts:
		# s += '\n\t' +_texts[suffix]
	prefix = '-'.join(['template',framework,viewtype,'template'])
	s = ''
	if prefix in _texts:
		s = _texts[prefix]
	
	
	return '<template>\n' + s + '</template>\n'


def _generateScript(meta,model,pool,context):
	_texts = meta['_texts']
	
	s = ''
	script = '-'.join(['script',framework,viewtype,'script'])
	if script in _texts:
		s += '<script>\n' + _texts[script] % (model.replace('.','-'),) + '\n</script>'
	
	return s

def _generateScriptSetup(meta,model,pool,context):
	_texts = meta['_texts']
	
	s = ''
	scriptsetup = '-'.join(['script',framework,viewtype,'setup'])
	if scriptsetup in _texts:
		s += '\n<script setup>\n' + _texts[scriptsetup] + '\n</script>'
	
	return s


def _generateStyle(meta,model,pool,context):
	_texts = meta['_texts']
	
	style = '-'.join(['style',framework,viewtype,'style'])
	if style in _texts:
		return '\n<style scoped>\n' + _texts[style] + '\n</style>'

def _generateI18N(meta,model,pool,context):
	langs = pool.get('bc.langs').select(fields=['code'],cond=[],context=context)
	records = pool.get('bc.models').select(fields=['code','descr','momi',{'columns':['seq','col','moc']},{'inherits':['col']}],cond=[('code','=',model)],context=context)
	i18ns = {}
	for record in records:
		for column in record['columns']:
			#column['moc'] = json.loads(column['moc'])
			label = column['moc']['label']
			for lang in langs: 
				i18ns.setdefault(lang['code'],{})[label] = label
	
	return '\n<i18n lang="yaml">\n' + str(yaml.dump(i18ns)) + '\n</i18n>'



GENERATE = {'template':_generateTemplate, 'script':_generateScript,'script_setup':_generateScriptSetup, 'style':_generateStyle,'i18n':_generateI18N}
