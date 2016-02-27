from socket import *
import time
serverName='localhost'
servePort=12000
clientSocket=socket(AF_INET,SOCK_DGRAM)
clientSocket.settimeout(1)
for x in range(0,10):
	start=time.time()
	clientSocket.sendto("ping",(serverName,servePort))
	
	newSentence,serverAddress=clientSocket.recvfrom(2048)
	end=time.time()
	print (str(start)+" "+str(end)+ " " +str(end-start))
clientSocket.close()