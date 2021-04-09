import qrcode
import psycopg2
from psycopg2 import Binary
from io import BytesIO
from base64 import b64encode
record = {'code':'a','name':'Hello'}
b = BytesIO()
q = qrcode.make("UC: %s - UN: %s" % (record['code'],record['name'])) 
q.save(b,'jpeg')
record['qrcode'] = Binary(b.getvalue())

conn = psycopg2.connect(database = 'test001', user = 'test', password = 'test', host = 'localhost', port=26257, sslmode = 'verify-full', sslrootcert = None, sslrootkey = None, sslcert = 'certs/client.test.crt',sslkey = 'certs/client.test.key');

cr = conn.cursor()
cr.execute("select name,qrcode from md_product where name='Gasoline'")
data = cr.fetchall()
print('data:',data[0][1].tobytes())
s = data[0][1].tobytes().decode('utf-8').split('::bytea')[0]
m = s[:s.find(',')+1]
v = s[s.find(','):]
#print(data[0][1].tobytes().decode('utf-8').split('::bytea')[0])
b = b64encode(bytes(v.encode('utf-8')))
#print(m+b.decode('utf-8'))
