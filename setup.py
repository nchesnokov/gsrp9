import os
import sys
from functools import reduce
from os.path import join as opj
from distutils.core import setup, Extension
from Cython.Distutils import build_ext
from DistUtilsExtra.command import build_i18n,build_help,build_icons,build_extra
__package_name__ = 'gsrp5server'
__package_file__ = 'gsrp5-server'

modules = []

package_data = {'gsrp5server':['*.rng','certs/*']}

data_files = [('/lib/systemd/system',[opj(__package_name__,'conf','gsrp5-server.service')]),('/etc/gsrp5-server.d',[opj(__package_name__,'conf','gsrp5-server.conf')])]

for lang in os.listdir(opj(__package_name__,'locale')):
	data_files.append((os.path.join(sys.prefix,'share', 'locale', lang, 'LC_MESSAGES'),[opj(__package_name__,'locale', lang, 'LC_MESSAGES','gsrp5server.mo')]))

for d in os.walk('gsrp5server'):
	l = list(map(lambda x:x[:-2],list(filter(lambda x: x[0] != '.' and x[-2:]=='.c',d[2]))))
	if len(l) > 0:
		a=list(map(lambda x:opj(d[0],x), l ))
		for n in a:
			modules.append(Extension('%s' % (n.replace(os.path.sep,'.'),), sources = ['%s' % (n + '.c')],language='clang'))
for sd in ('root','addons'):			
	for d in os.walk(opj('gsrp5server',sd)):
		l = list(map(lambda x:x,list(filter(lambda x: x[-4:] in ('.xml','.csv','.pot','.rml') or x[-5:] in ('.yaml','.docx','.xlsx') or x[-3:] == '.po' or x == '__manifest__.info',d[2]))))
		if len(l) > 0:
			a=list(map(lambda x:opj(d[0],x), l ))
			for n in a:
				data_files.append((opj(sys.base_prefix,'lib64','python'+('%s.%s') % (sys.version_info.major,sys.version_info.minor),'site-packages',d[0]),[n]))

packages = ['gsrp5server']

setup (name = __package_name__,package_data = package_data, data_files = data_files, scripts = [opj(__package_name__,'script/gsrp5-server')], packages = packages,package_dir = {__package_name__:'gsrp5server'},version = '1.0.1', description = 'Global System Resource Planing',long_description = 'Global System Resource Planing & Executing', author='Nikolay Chesnokov', author_email='nikolaychesnokov@gmail.com' , url='http://www.gsrp5.org', license='AGPL-3'
,cmdclass = { 'build_ext': build_ext, "build" : build_extra.build_extra,'build_i18n':build_i18n.build_i18n}, ext_modules = modules)



