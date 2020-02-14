import os
import logging
from os.path import join as opj

import polib
from yandex import Translater

import datetime
from datetime import date,time,datetime

_logger = logging.getLogger('listener.' + __name__)

tr = Translater.Translater()
tr.set_key('trnsl.1.1.20181211T195911Z.dd221d8c2a232623.1e176c0b53c78e901d04472cdf7483c7c0f9a0b8') # Api key found on https://translate.yandex.com/developers/keys
tr.set_from_lang('en')

def _get_mt(p):
	res = {}
	if os.path.exists(p):
		po = polib.pofile(p)
		for entry in po:
			if entry.msgstr:
					res[entry.msgid] = entry.msgstr

	return res

def _download_i18n_tr(cr,pool,uid,path,module):
	if os.path.exists(opj(path,module,'i18n','po.pot')):
		po = polib.pofile(opj(path,module,'i18n','po.pot'))
	
		for lang in list(map(lambda x: x.split('-')[1],filter(lambda x: x[:3] == 'en-',tr.get_langs()))):
			mt = _get_mt(opj(path,module,'i18n','%s.po') % (lang,))
			#print('MT:',mt)
			#print('Translate module:%s lang:%s' % (module,lang))
			out = polib.POFile()
			out.metadata = {
			    'Project-Id-Version': '1.0',
			    'Report-Msgid-Bugs-To': 'admin@gsrp5lab.com',
			    'POT-Creation-Date': '%s' % (datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S%z"),),
			    'PO-Revision-Date': '%s' % (datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S%z"),),
			    'Last-Translator': 'you <translater@yandex.ru>',
			    'Language-Team': 'English <translaterteam@yandex.ru>',
			    'MIME-Version': '1.0',
			    'Content-Type': 'text/plain; charset=utf-8',
			    'Content-Transfer-Encoding': '8bit',
			}
	
			tr.set_to_lang(lang)
			
			for entry in po:
				#print('entry.occurrences:',entry.occurrences)
				if entry.msgid in mt:
					msgstr = mt[entry.msgid]
				else:
					tr.set_text(entry.msgid)
					msgstr=tr.translate()
					mt[entry.msgid] = msgstr
	
				out_entry = polib.POEntry(
				    msgid=entry.msgid,
				    msgstr=msgstr,
				    occurrences=entry.occurrences
				)
				out.append(out_entry)
	
	
				
			out.save(opj(path,module,'i18n','%s.po') % (lang,))
			_logger.info('Module: %s TR write file: %s' % (module,opj(path,module,'i18n','%s.po' % (lang,))));
			#print('Translated module:%s lang:%s' % (module,lang))

def Area(cr, pool, uid, registry, modules = None,context={}):
	pwd = os.getcwd()
	if not modules:
		modules = registry._depends
	else:
		modules = list(filter(lambda x: x in modules,registry._depends))
	logmodules = []
	for module in filter(lambda x:'state' in registry._modules[x] and registry._modules[x]['state'] in ('I','N'),modules):
		path = registry._modules[module]['path']
		_download_i18n_tr(cr,pool,uid,path,module)
		logmodules.append(module)
	_logger.info('Download translate i18ns of modules %s' % (logmodules,))
	
	return ['Download translate i18ns of modules %s' % (logmodules,)]


