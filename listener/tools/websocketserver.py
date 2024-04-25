import sys
import ssl
import logging
import socketserver

from serviceloader.tools.common import default_service_loader,default_tree_service_loader, _service_loader 

from wsproto import ConnectionType, WSConnection
from wsproto.events import (
    AcceptConnection,
    CloseConnection,
    Message,
    Ping,
    Request,
    TextMessage,
    BytesMessage,
)

MAX_CONNECTS = 5
RECEIVE_BYTES = 4096 << 16


_logger = logging.getLogger(__name__)

class WebSocketHandler(socketserver.StreamRequestHandler):

	def handle(self):
		if self.server._using_ssl:
			self.connection = self.server.context.wrap_socket(self.connection, server_side=True)
			self.connection.timeout(9000)
		ws = WSConnection(ConnectionType.SERVER)
		running = True
		if self.server.dispatcher:
			self.dispatcher = self.server.dispatcher
		else:
			self.dispatcher = _service_loader(self.server.service_config_file)
		
		self._connected = False
		
		while running:
			# 1) Read data from network
			in_data = self.connection.recv(RECEIVE_BYTES)
			if self._connected:
				fin = in_data[0] & 0x80
				rsv1 = in_data[0] & 0x40
				rsv2 = in_data[0] & 0x20
				rsv3 = in_data[0] & 0x10
				opcode = in_data[0] & 0x0f
				mask = in_data[1] & 0x80
				pld = in_data[1] & 0x7f
				pm = 0
				if mask:
					pm = 4
				pz =1
				if pld < 126:
					pl = in_data[1] & 127
				elif pld == 126:
					pl = int.from_bytes(in_data[2:4],'big')
					pz = 3
				elif pld == 127:
					pl = int.from_bytes(in_data[2:10],'big')
					pz = 9

				offset = 1 + pz + pm
				#print('DATA fin=%s,rsv1=%s,rsv2=%s,rsv3=%s,opcode=%s,mask=%s,pld=%s,pl=%s,offset=%s,in_data[:16]=%s,len(in_data)=%s:' % (fin,rsv1,rsv2,rsv3,opcode,mask,pld,pl,offset,in_data[:16],len(in_data),))
				chunks = pl - (len(in_data)- offset)
				while chunks > 0:
					chunk_data = self.connection.recv(RECEIVE_BYTES)
					chunks -= len(chunk_data)
					in_data += chunk_data

			ws.receive_data(in_data)
	
			# 2) Get new events and handle them
			out_data = b""
			for event in ws.events():
				if isinstance(event, Request):
					# Negotiate new WebSocket connection
					#print("Accepting WebSocket upgrade")
					out_data += ws.send(AcceptConnection())
					self.server.on_connection_open(self.connection)
					self._connected = True
				elif isinstance(event, CloseConnection):
					# Print log message and break out
					_logger.info(
						"Connection closed: code={} reason={}".format(
							event.code, event.reason
						)
					)
					out_data += ws.send(event.response())
					self.server.on_connection_close(self.connection)
					running = False
				elif isinstance(event, TextMessage):
					# Reverse text and send it back to wsproto
					#print("Received request and sending response-text",event.data)
					omsg = self.server.on_data_receive(self.dispatcher,self.connection,event.data)
					#out_data += ws.send(Message(data=event.data[::-1]))
					out_data += ws.send(Message(data=omsg))
				elif isinstance(event, BytesMessage):
					# Reverse text and send it back to wsproto
					#print("Received request and sending response-binary",event.data)
					omsg = self.server.on_data_receive(self.dispatcher,self.connection,event.data)
					#out_data += ws.send(Message(data=event.data[::-1]))
					out_data += ws.send(Message(data=omsg))
					
				elif isinstance(event, Ping):
					# wsproto handles ping events for you by placing a pong frame in
					# the outgoing buffer. You should not call pong() unless you want to
					# send an unsolicited pong frame.
					_logger.info("Received ping and sending pong")
					out_data += ws.send(event.response())
				else:
					_logger.error("Unknown event: {!r}".format(event))
	
			# 4) Send data from wsproto to network
			_logger.info("Sending {} bytes".format(len(out_data)))
			self.connection.send(out_data)

if sys.platform == 'win32':
	from socketserver import ThreadingTCPServer as webserver
else:
	from socketserver import ForkingTCPServer as webserver

webserver.allow_reuse_address = True

class WebSocketServer(webserver):
	_LOGS_FILE = "ws.log"
	def __init__(self, host, port, handler=WebSocketHandler,allow_reuse_address=False,certfile=None, keyfile=None, ssl_version=ssl.PROTOCOL_TLSv1, on_data_receive=None, on_connection_open=None, on_connection_close=None, on_error=None, service_config_file = None, preload = False,DEBUG=False):
		# Initialize log file format.
		logging.basicConfig(
			filename=WebSocketServer._LOGS_FILE,
			filemode='w',
			format='%(levelname)s:%(threadName)s\n\t%(message)s',
			level=logging.DEBUG if DEBUG else logging.INFO
		)

		super(WebSocketServer,self).__init__((host,port),handler)

		self.host = host
		self.port = port
		self.allow_reuse_address = allow_reuse_address
		self._using_ssl = bool(certfile and keyfile)
		self.on_data_receive = on_data_receive if on_data_receive is not None else self._default_func
		self.on_connection_open = on_connection_open if on_connection_open is not None else self._default_func
		self.on_connection_close = on_connection_close if on_connection_close is not None else self._default_func
		self.on_error = on_error if on_error is not None else self._default_func
		self.service_config_file = service_config_file
		self.dispatcher = None
		if preload:
			self.dispatcher = _service_loader(self.service_config_file)
		self.DEBUG = DEBUG

		if self._using_ssl:
			self.context = ssl.SSLContext(ssl_version)
			self.context.load_cert_chain(certfile, keyfile)


	def _default_func(self, *args, **kwargs):
		"""Default function if the user does not define one.
		"""
		pass


