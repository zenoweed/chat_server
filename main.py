import socket # Import socket module

add = "172.0.0.1" # IP address of host machine
port = 6098 # Port of host machine

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(add,port) # Binds the IP of the machine with the port

s.listen(1) # Listening to 1 incoming connections

print ("Server up. Waiting for connections...")

connection,address = s.accept()
# Connection is a socket object we use to send and receive data
# Address stores the IP of the client

print ("Connected to " + address + ". Start Chatting!")

while(1): # Maximum number of queed connections
  data = connection.recv(1024)
  print("--\nMessage received--\n")
connection.close()