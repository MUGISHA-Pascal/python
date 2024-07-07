# # web browser
# import socket
# mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# mysock.connect(("data.pr4e.org",80))
# cmd="GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n".encode()
# mysock.send(cmd)

# while True:
#     data=mysock.recv(512)
#     if len(data)<1:
#         break
#     print(data.decode(),end=" ") 
# mysock.close()
# # a simple web server 
# from socket import *
# def createserver():
#     serverphone=socket(AF_INET,SOCK_STREAM)
#     try:
#         serverphone.bind(('localhost',3000))
#         serverphone.listen(5)
#         while(1):
#             (clientsocket,address)=serverphone.accept()
#             rd=clientsocket.recv(5000).decode()
#             pieces=rd.split("\n")
#             if (len(pieces)>0):print(pieces[0])
#             data="HTTP/1.1 200 OK\r\n"
#             data+="Content-Type:text/html;charset=utf-8\r\n"
#             data+="\r\n"
#             data+="<html><body>Hello World </body></html>\r\n\r\n"
#             clientsocket.sendall(data.encode())
#             clientsocket.shutdown(SHUT_WR)
#     except KeyboardInterrupt:
#         print("\nshutting down...\n")
#     except Exception as exc:
#         print("Error:\n")
#         print(exc)
        
#     serverphone.close()
    
# print("Access http://localhost:3000")
# createserver()
#  # a simple web client
# import socket
# mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# mysock.connect(('127.0.0.1',3000))
# cmd="GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n".encode()
# mysock.send(cmd)
# while True:
#     data=mysock.recv(512)
#     if len(data<1):
#         break
#     print(data.decode(),end=" ")
# mysock.close()
# #an even simpler web client
# import urllib.request
# fhand=urllib.request.urlopen(" http://127.0.0.1:3000/romeo.txt")
# for line in fhand:
#     print(line.decode().strip())
# #web server 2
# from socket import *
# server=socket(AF_INET,SOCK_STREAM)
# try:
#     server.bind(("localhost",2000))
#     server.listen(5)
#     while(1):
#         (clientsocket,address)=server.accept()
#         rd=clientsocket.recv(5000).decode()
#         pieces=rd.split("\n")
#         if (len(pieces)>0 ): print(pieces[0])
#         data='HTTP/1.1 200 OK\r\n'
#         data+="Content-Type:text/html;charset=utf-8\r\n"
#         data+="\r\n"
#         data+="<html><body>mugisha pascal</body></html>\r\n\r\n"
#         clientsocket.sendall(data.encode())
#         clientsocket.shutdown(SHUT_WR)
# except KeyboardInterrupt:
#     print("shutting")
# except Exception as exc:
#     print(exc)
# server.close()

        