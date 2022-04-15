import os
import json
from  os.path import join as opj

framework = 'element-plus'
viewtype = 'form'

def _generateTemplate(meta,model,pool,context):
	_texts = meta['_texts']
	_maps = meta['_maps']
	prefix = '-'.join(['template',framework,viewtype,'prefix'])
	s = ''
	if prefix in _texts:
		s = _texts[prefix]

	records = pool.get('bc.models').select(fields=['code','descr','momi',{'columns':['seq','col','moc']},{'inherits':['col']}],cond=[('code','=',model)],context=context)
	for record in records:
		o2m = True
		for column in record['columns']:
			column['moc'] = json.loads(column['moc'])
			key =  '-'.join(['template',framework,viewtype,'item',column['moc']['type']])
			if key in _maps:
				key = _maps[key]
			if key in _texts:
				if column['moc']['type'] == 'one2many' and o2m or column['moc']['type'] != 'one2many':
					s += """\n\t\t<el-form-item :label="colsLabel['{0}']">\n""".format(column['col'])
					#s += _texts[key].format(column['col'])
					s += _texts[key] % tuple([column['col']] * _texts[key].count("'%s'"))
					s += """\n\t\t</el-form-item>"""
					if column['moc']['type'] == 'one2many' and o2m:
						o2m = False
		
	suffix = '-'.join(['template',framework,viewtype,'suffix'])
	if suffix in _texts:
		s += '\n\t' +_texts[suffix]

	
	return '<template>\n' + s + '</template>'


def _generateScript(meta,model,pool,context):
	_texts = meta['_texts']
	
	s = ''
	script = '-'.join(['script',framework,viewtype,'script'])
	if script in _texts:
		s += '<script>\n' + _texts[script] % (model.replace('.','-'),) + '\n</script>'

	scriptsetup = '-'.join(['script',framework,viewtype,'setup'])
	if scriptsetup in _texts:
		s += '\n<script setup>\n' + _texts[scriptsetup] + '\n</script>'
	
	return s

def _generateStyle(meta,model,pool,context):
	_texts = meta['_texts']
	
	style = '-'.join(['style',framework,viewtype,'style'])
	if style in _texts:
		return '<style scoped>\n' + _texts[style] + '\n</style>'


GENERATE = {'template':_generateTemplate, 'script':_generateScript, 'style':_generateStyle}
