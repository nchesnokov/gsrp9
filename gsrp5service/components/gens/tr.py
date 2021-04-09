import os
import logging
from os.path import join as opj

import polib
from yandex import Translater

from deep_translator import GoogleTranslator

import datetime
from datetime import date,time,datetime

import web_pdb

_logger = logging.getLogger('listener.' + __name__)

tr = Translater.Translater()
tr.set_key('trnsl.1.1.20181211T195911Z.dd221d8c2a232623.1e176c0b53c78e901d04472cdf7483c7c0f9a0b8') # Api key found on https://translate.yandex.com/developers/keys
tr.set_from_lang('en')

langs_list = dict(list(map(lambda x: list(reversed(x)),GoogleTranslator().get_supported_languages(as_dict=True).items())))



def _get_mt(p):
	res = {}
	if os.path.exists(p):
		po = polib.pofile(p)
		for entry in po:
			if entry.msgstr:
				res[entry.msgid] = entry.msgstr

	return res

def _download_i18n_tr(path,module):
	if os.path.exists(opj(path,module,'i18n','po.pot')):
		po = polib.pofile(opj(path,module,'i18n','po.pot'))
	
		#for lang in list(map(lambda x: x.split('-')[1],filter(lambda x: x[:3] == 'en-',tr.get_langs()))):
		for lang in langs_list.keys():
			mt = _get_mt(opj(path,module,'i18n','%s.po') % (lang,))
			#web_pdb.set_trace()
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
	
			#tr.set_to_lang(lang)
			tr_msgid = []
			tr_batch = []
			tr_list = []
			tr_occurrences = []
			for entry in po:
				tr_msgid.append(entry.msgid)
				tr_occurrences.append(entry.occurrences)
				if entry.msgid in mt:
					tr_list.append(mt[entry.msgid])

			for entry in po:
				tr_msgid.append(entry.msgid)
				tr_occurrences.append(entry.occurrences)
				if not entry.msgid in mt:
					tr_batch.append(entry.msgid)


			#tr_list.extend(YandexTranslator(yandex_key).translate_batch(source='en',target=lang,batch=tr_batch))
			for msgid,msgstr,occurrences in zip(tr_msgid,tr_list,tr_occurrences):
				out_entry = polib.POEntry(
				    msgid=msgid,
				    msgstr=msgstr,
				    occurrences=occurrences
				)

				# out_entry = polib.POEntry(
				    # msgid=entry.msgid,
				    # msgstr=msgstr,
				    # occurrences=entry.occurrences
				# )
				out.append(out_entry)
	
	
				
			out.save(opj(path,module,'i18n','%s.po') % (lang,))
			_logger.info('Module: %s TR write file: %s' % (module,opj(path,module,'i18n','%s.po' % (lang,))));
			#print('Translated module:%s lang:%s' % (module,lang))

def Area(self, modules = None,context={}):
	pwd = os.getcwd()
	pool = self._models
	registry = self._registry
	if not modules:
		modules = registry._depends
	else:
		modules = list(filter(lambda x: x in modules,registry._depends))
	logmodules = []
	for module in filter(lambda x:'state' in registry._modules[x] and registry._modules[x]['state'] in ('I','N'),modules):
		path = registry._modules[module]['path']
		_download_i18n_tr(path,module)
		logmodules.append(module)
	_logger.info('Download translate i18ns of modules %s' % (logmodules,))
	
	return ['Download translate i18ns of modules %s' % (logmodules,)]


