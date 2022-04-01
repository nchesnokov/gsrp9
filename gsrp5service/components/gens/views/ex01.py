import os
import json
from  os.path import join as opj
import web_pdb

_texts = {}
_gens = {}
_maps = {}

def _loadFiles(path):
	folders = []
	for i in os.walk(path):
		folders.append(i)
		
	for address, dirs, files in folders:
		print(address, dirs, files)
		if address == path:
			continue
		for name in files:
			a1 = address.replace('./','').replace('/','-')
			#web_pdb.set_trace()
			bbb = name.split('.')
			nm,ext = bbb[0],bbb[1]
			if ext in ('template','script','style'):
				path = opj(address,name)
				#print('path:',path,ext,os.path.islink(path))
				if os.path.exists(path):
					if os.path.isfile(path) and not os.path.islink(path):
						with open(opj(address,name), 'r') as f:
							_texts[ext+ '-' + a1 + '-' +nm] = f.read()
					elif os.path.islink(path):
						link = os.readlink(path)
						a2 = link.split('.')[0]
						_maps[ext+ '-' + a1 + '-' +nm] = ext+ '-' + a1 + '-' + a2
				elif ext == 'py':
					print('module:',a1+'.'+nm)
					_gens[a1] = __import__(name=a1+'.'+nm,globals=globals(),locals=locals(),fromlist=[],level=0)
					print('DIR:',dir(_gens[a1]))

_loadFiles('./')

#for k in _texts.keys():
#	print('texts:',k,'\n',_texts[k])

print('maps:',_maps)
print('texts:',_texts.keys())
print('gens:',_gens)

META = {'_texts':_texts,'_maps':_maps,'_gens':_gens}
