import argparse
import os
import urllib
import sys
import itertools
import socket
from socket import socket as Socket

def main():
	parser=argparse.ArgumentParser()
	parser.add_argument('--port','-p',default=2000,type=int,help='port to use')
	args=parser.parse_args()
	server_socket=Socket(socket.AF_INET,socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	server_socket.bind(('',args.port))
	server_socket.listen(1)
	print "server running"
	while True:
		connection_socket=server_socket.accept()[0]
		request=connection_socket.recv(1024)
		reply=http_handler(request)
		connection_socket.send("HTTP/1.1 200 OK\n") 
		connection_socket.send("\n")

		connection_socket.send(reply)
		connection_socket.close()

		print "received request"
		print "reply sent"

	return 0

def http_handler(request):
	return request
	start=request.find('/')
	end=request.find('HTTP')
	path=request[start+1:end]
	path=os.path.abspath(path).rstrip()
	path=urllib.unquote(path)
	print os.path.exists(path)
	print path
	if os.path.exists(path):
		print type(open(path).read())
		return open(path).read()
	else:
		return "404 ERROR \n"+path+" file not found"




if __name__=="__main__" :
	sys.exit(main())


