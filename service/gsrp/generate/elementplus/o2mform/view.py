import os
import json
from  os.path import join as opj

frameworkdir = 'elementplus'
framework = {'element-plus':'elementplus'}
viewtype = 'form'

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
				s += _texts[key].format(column['col'])
				s += """\n\t\t</el-form-item>"""
				cs[key] = s
	
	return cs


def _generateTemplate(meta,model,pool,context):
	_texts = meta['_texts']
	_maps = meta['_maps']
	prefix = ['template',framework[frameworkdir],viewtype,'prefix'].join('-')
	s = ''
	if prefix in _maps:
		s = _maps[prefix]

	records = pool.get('bc.models').select(fields=['code','descr','momi',{'columns':['seq','col','moc']},{'inherits':['col']}],cond=[('code','=',model)],context=context)
	for record in records:
		for column in record['columns']:
			column['moc'] = json.loads(column['moc'])
			key =  ['template',framework[frameworkdir],viewtype,'item',column['moc']['type']].join('-')
			if key in _maps:
				key = _maps[key]
			
			if key in _texts:
				s += """\n\t\t<el-form-item :label="colsLabel['{0}']">\n""".format(column['col'])
				s += _texts[key].format(column['col'])
				s += """\n\t\t</el-form-item>"""
		
	suffix = ['template',framework[frameworkdir],viewtype,'suffix'].join('-')
	if suffix in _maps:
		s += _maps[suffix]

	
	return '<template>\n' + s + '\n</template>'


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
	_maps = meta['_maps']
	
	style = ['style',framework[frameworkdir],viewtype,'style'].join('-')
	if style in _texts:
		return '<style scoped>\n' + _maps[style] + '\n</style>'


GENERATE = {'template':_generateTemplate, 'script':_generateScript,'script_setup':_generateScriptSetup, 'style':_generateStyle}
