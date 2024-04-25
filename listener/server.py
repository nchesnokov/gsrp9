import sys
from listener import server

if __name__ == "__main__":
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		sys.exit(0)


