from socket import *
import sys

if len(sys.argv) <= 1:
  print ('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
  sys.exit(2)

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
print ("Socket successfully created")

# Fill in start.
tcpSerProt = 8888
tcpSerSock.bind(('', tcpSerProt))
print ("socket binded to %s" %(tcpSerProt))
 
# put the socket into listening mode
tcpSerSock.listen(5)
print ("socket is listening")  
# Fill in end.

while 1:
  # Start receiving data from the client
  print ('\n\nReady to serve...')
  tcpCliSock, addr = tcpSerSock.accept()
  print ('Received a connection from:', addr)
  message = tcpCliSock.recv(1024).decode() # Fill in start. # Fill in end.
  print (message)
  # Extract the filename from the given message
  print (message.split()[1])
  filename = message.split()[1].partition("/")[2]
  print (filename)
  fileExist = "false"
  filetouse = "/" + filename
  print (filetouse)

  # Implementing URL Filter
  isFilteredURL = False
  filterdURL = open("filter.txt", "r")
  print("filterdURL", filterdURL)
  for line in filterdURL:
    # print("FilterdURL lines: ", line[0:-1])
    # print("Filetouse lines: ", filetouse[1:])
    # print("FilterdURL lines length: ", len(line[0:-1]))
    # print("filetouse lines length: ", len(filetouse[1:]))

    # print(line.strip() == filetouse[1:])
    # Checking wehter requested url is filtered or not
    if (line.strip() == filetouse[1:]):
      isFilteredURL = True
      break;

  try:
    # Check wether the file exist in the cache
    f = open(filetouse[1:], "r")
    print("fileTouse: ",filetouse[1:])
    outputdata = f.readlines()
    print("outputData: ", outputdata)
    fileExist = "true"
    # ProxyServer finds a cache hit and generates a response message
    tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
    tcpCliSock.send("Content-Type:text/html\r\n".encode())
    # Fill in start.
    for line in outputdata:
      print("outputdata lines: ", line)
      tcpCliSock.send(line.encode())
    # Fill in end.
    print ('Read from cache')
  # Error handling for file not found in cache
  except IOError:
    if (fileExist == "false" and not isFilteredURL):
      # Create a socket on the proxyserver
      c = socket(AF_INET, SOCK_STREAM)# Fill in start. # Fill in end.
      hostn = filename.replace("www.","",1)
      print (hostn)

      try:
        # Connect to the socket to port 80
        # Fill in start.
        c.connect((hostn, 80))
        print('Conected to port 80')
        # Fill in end.
        # Create a temporary file on this socket and ask port 80 for the file requested by the client
        # fileobj = c.makefile('r', 0)
        fileobj = c.makefile('w')
        print("fileObj before")
        print(fileobj)
        fileobj.write(("GET "+"http://" + filename + " HTTP/1.0\n\n"))
        print(fileobj)
        print("fileObj after")
        # Read the response into buffer
        # Fill in start.
        fileobj = c.makefile('r')
        buffer = fileobj.readlines()
        print("buffer: ")
        print(buffer)
        # Fill in end.
        # Create a new file in the cache for the requested file.
        # Also send the response in the buffer to client socket and the corresponding file in the cache
        tmpFile = open("./" + filename,"w")
        print("TMPFILE: ",tmpFile)
        # Fill in start.
        for line in buffer:
          print("Buffer Lines:", line)
          tmpFile.write(line)
          tcpCliSock.send(line.encode())

        print("Done Wrting")
        # Fill in end.
      except Exception as e:
        print(e)
        print ("Illegal request")

    elif isFilteredURL:
      tcpCliSock.send("HTTP/1.0 403 Blocked URL \r\n".encode())
      tcpCliSock.send("This URL is Blocked".encode())

    else:
      print("Error 404 not found")
      # HTTP response message for file not found
      # Fill in start.
      tcpCliSock.send("'HTTP/1.0 404 Not Found\r\n".encode())
      # Fill in end.
  # Close the client and the server sockets
  tcpCliSock.close()
# Fill in start.
# Fill in end.