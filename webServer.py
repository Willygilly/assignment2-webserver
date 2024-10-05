# import socket module
from socket import *
# In order to terminate the program
import sys

  


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(('localhost',port))
  
  #Fill in start
  serverSocket.listen(1)

  #Fill in end

  while True:
    #Establish the connection
    
    print('Ready to serve...')
    #Fill in start  
    connectionSocket, addr = serverSocket.accept()
    #    #Fill in end
    
    try:
      #Fill in start
      message = connectionSocket.recv(1024).decode('utf-8')  
      #Fill in end 
      filename = message.split()[1]
      #filename = message.split()[1]
      
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:],'+r') #fill in start #fill in end)
    
      #fill in end
      

      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
      #Fill in start 
      isValid = "200 OK\r\n"

      #Content-Type is an example on how to send a header as bytes. There are more!
      outputdata = b"Accept-Ranges: bytes\nVary: Accept-Encoding\nConnection: close\nContent-Type: text/html; charset=UTF-8\r\n\r\n"


      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
      #Fill in end

  
      content = ""      
      
      for i in f: #for line in file
      #Fill in start 
        content += i 
      #  #Fill in end 
      

      #Send the content of the requested file to the client (don't forget the headers you created)!
      #Send everything as one send command, do not send one line/item at a time!
      modMsg = isValid + outputdata.decode('utf-8') + content
      # Fill in start
      connectionSocket.send(modMsg.encode())

      # Fill in end

      f.close()
      connectionSocket.close()  #closing the connection socket
      sys.exit
    except Exception as e:
       
      print(e.args)
      # Send response message for invalid request due to the file not being found (404)
      # # Remember the format you used in the try: block!
      #Fill in start
      isValid = "404 Not Found\r\n"
      modMsg = isValid
      connectionSocket.send(modMsg.encode())
      #Fill in end
      
 
      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

      # Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop. 
      # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
      #serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data
      #   
      
      
      
if __name__ == "__main__":
        webServer(13331)   



