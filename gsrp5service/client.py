
import asyncio
import os
from os.path import join as opj
import pickle
import ssl
import websockets
import time

uid = None

from orm.model import Model,ModelInherit

secure = False

from lxml import etree
from io import BytesIO

ssl_ctx = None
if secure:
	ssl_ctx = ssl.create_default_context(purpose = ssl.Purpose.CLIENT_AUTH)
	ssl_ctx.load_cert_chain(opj(os.getcwd(),"server.crt"),opj(os.getcwd(),"server.key"))

async def _execute(args):
	global uid
	ws = args[0]
	if uid:
		msg = [uid]
	else:
		msg=['0' * 32]
	msg.extend(args[1:])
	print('MSG:',msg)
	imsg = pickle.dumps(msg)
	await ws.send(imsg)
	omsg = await ws.recv()
	rmsg =pickle.loads(omsg)
	print('RMSG:',rmsg)
	if hasattr(rmsg,'_class__') and issubclass(rmsg,Exception):
		print('Exception: %s' % (rmsg,))
		return None
	if uid is None and args[1] == '_open':
		uid = rmsg[0]
	return rmsg

#print('ssl_ctx:',ssl_ctx)
async def hello():
	if secure:
		async with websockets.connect('wss://localhost:8170', ssl=True) as ws:
			for m in ('open',):
				if m == 'open':
					msg = await _execute([ws, 'sids', m, {'name':'testsid001','preload':True}])
				else:
					msg = await _execute([ws, 'cursors', m])
			if True:
				msg = await _execute([ws, 'modules','uninstall',{'name':'md'}])
				msg = await _execute([ws, 'modules','install',{'name':'md'}])
			for i in range(1,10):
				msg = await _execute([ws, 'models','bc.users','create',{'records':{'login_id':i+1,'login':'admin%s' % (i,),'password':'Administartor%s' % (i,),'firstname':'Administartor%s' % (i,),'lastname':'of system%s' % (i,)}}])
			
			msg = await _execute([ws, 'models','bc.users','search',{'cond':[('login','=','admin9')]}])

			msg = await _execute([ws, 'models','bc.users','read',{'ids':msg,'fields':['login','password']}])
			
			msg = await _execute([ws, 'models','bc.users','unlink',{'ids':msg}])
			
			msg = await _execute([ws, 'models','bc.users','unlink',{'cond':[('login','=','admin9')]}])

			msg =	 await _execute([ws, 'cursors','commit'])
	
			ws.close()

	else:
		#async with websockets.connect('ws://www.gsrp5labs.com:8170') as ws:
		#async with websockets.connect('ws://localhost:8170/ws') as ws:
		async with websockets.connect('ws://localhost:8170') as ws:
			if True:
				uid = await _execute([ws, '_open','gsrp5.system',{'profile':'system'}])
				#msg = await _execute([ws, uid[0],'modules','upgrademoduleslist',{'db':'test001'}])
				#msg = await _execute([ws, 'slots','initialize'])
				#msg = await _execute([ws, 'gens','ui',{'modules': ['ai','bc','cm','crm','fa','hcm','md','ml','mm','md3','mrp','oil','oil2','project','purchase','sale','le','srm','srm_ru','stock','qm','wkf','wkf_srm','tm','trm','cf','common','wm','ctrm']}])
				
				msg = await _execute([ws, 'login',{'user':'admin','password':'admin','slot':'test001'}])

				#msg = await _execute([ws, 'gens','tr',{'modules': ['sale']}])
				msg = await _execute([ws, 'gens','examples',{'modules': ['purchase']}])
				#msg = await _execute([ws, 'gens','examples',{'modules': ['ai','bc','cm','crm','fa','hcm','md','ml','mm','md3','mrp','oil','oil2','project','purchase','sale','le','srm','srm_ru','stock','qm','wkf','wkf_srm','tm','trm','cf','common','wm','ctrm']}])				
				#msg = await _execute([ws, 'login',{'user':'admin','password':'admin','slot':'test001'}])
				#msg = await _execute([ws, 'gens','tr',{'modules': ['l10n_uy']}])
				#msg = await _execute([ws, 'gens','ui',{'modules': ['md','purchase','sale']}])
				#msg = await _execute([ws, 'gens','examples',{'modules': ['sale']}])
				#msg = await _execute([ws, 'gens','ui',{'modules': ['sale']}])
				#msg = await _execute([ws, 'gens','ui',{'modules': ['md','common','purchase','sale']}])
				#msg = await _execute([ws, 'gens','examples',{'modules': ['md','purchase','sale','srm']}])
				#msg = await _execute([ws, 'gens','examples',{'modules': ['ai','bc','cm','crm','fa','hcm','ml','mm','mrp','purchase','sale','srm','srm_ru','stock','qm','wkf','wkf_srm','tm','trm','cf','common','wm']}])
				#msg = await _execute([ws, 'gens','tests',{'modules': ['crm','purchase','sale','le','cf','ai','cm','fa','hcm']}])
				
				#msg = await _execute([ws, 'gens','ui',{'modules': ['md']}])
				#msg = await _execute([ws, 'gens','view',{'modules': ['trm','ehs','scm']}])
				#msg = await _execute([ws, 'gens','menu',{'modules': ['trm','ehs','scm']}])
				#msg = await _execute([ws, 'gens','role',{'modules': ['trm','ehs','scm']}])
				#msg = await _execute([ws, 'gens','tr',{'modules': ['common']}])
				#msg = await _execute([ws, 'gens','tr',{'modules': ['ai','bc','cm','crm','fa','hcm','md','ml','mm','md3','mrp','oil','oil2','project','purchase','sale','le','srm','srm_ru','stock','qm','wkf','wkf_srm','tm','trm','cf','common','wm']}])
				
				#msg = await _execute([ws, 'modules','install',{'modules':['wkf_srm']}])
				
				return
				msg = await _execute([ws, 'slots','drop',{'sid':'test001'}])
				#msg = await _execute([ws, 'slots','drop',{'sid':'test002'}])
				#msg = await _execute([ws, 'slots','drop',{'sid':'test003'}])
				#msg = await _execute([ws, '_reload'])
				msg = await _execute([ws, 'slots','create',{'name':'test001','db_user':'test'}])
				#msg = await _execute([ws, 'modules','sysinstall'])
				#msg = await _execute([ws, 'slots','create',{'sid':'test002','host':'localhost','port':26257,'database':'test002','db_user':'test','db_password':'test','sslmode':'verify-full'}])
				#msg = await _execute([ws, 'slots','create',{'sid':'test001','host':'localhost','port':26257,'database':'test001','db_user':'test','db_password':'test','sslmode':'verify-full'}])
				msg = await _execute([ws, '_commit'])
				return
			else:
				#msg = await _execute([ws, '_slots'])
				#return
				msg = await _execute([ws, '_open','gsrp5.user',{'profile':'test001'}])
				msg = await _execute([ws, 'login',{'user':'admin','password':'admin'}])
				#msg=await _execute([ws,'models','md.category.product','tree',{'fields':['name','parent_id','childs_id']}])
				#msg = await _execute([ws, 'modules','install',{'modules':['hcm','wkf_srm','project']}])
				#msg = await _execute([ws, 'modules','install',{'modules':['cf','crm','hcm','le','purchase','sale','fa','stock','tm','mm','mrp']}])
				#msg = await _execute([ws, 'modules','install',{'modules':['cf','ai','cm','hcm','ml','tm','trm','crm','srm','qm','trm','wkf_srm','srm_ru']}])
				#msg = await _execute([ws, 'modules','install',{'modules':['project','crm','mm','mrp','purchase','sale','le','stock','wkf_srm','fa']}])
				#msg = await _execute([ws, 'modules','install',{'modules':['crm','purchase','sale','le','cf','ai','fa','hcm']}])
				#msg = await _execute([ws, 'modules','install',{'modules':['ehs','scm','hcm','wm']}])
				#msg = await _execute([ws, 'modules','install',{'modules':['srm']}])
				#msg = await _execute([ws, 'modules','install',{'modules':{'srm':['env','view','example','data','demo','test','i18n']}}])
				msg = await _execute([ws, 'modules','install',{'modules':{'sale':['example']}}])
				#msg = await _execute([ws, 'modules','install',{'modules': ['cm','ctrm','ai','fa','hcm','md','ml','mm','mrp','oil','project','purchase','sale','le','srm','srm_ru','stock','qm','wkf','wkf_srm','tm','trm','cf','common','wm','ehs','scm']}])
				msg = await _execute([ws, '_commit'])

if __name__ == "__main__":
	asyncio.get_event_loop().run_until_complete(hello())
