# encoding : utf-8
from socket import *


IP = "127.0.0.1"
SENDPORT = 8888
RECVPORT = 8889      # configure ip and port number





def Setting(mode):

    global SENDPORT, RECVPORT

    sock = socket(AF_INET, SOCK_DGRAM)

    

    if(mode == "server"):
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.bind((IP, RECVPORT))
    


    return sock




#def Receive_Data(server, queue):
    
#    while True:
#        s, addr = server.recvfrom(1024)        
#        queue.put(s)


        


def Data_Split(s, node, nodenum):
    
    #s = queue.get()  

    for i in range(nodenum):           # total node count
        k = i * 32
        node[i].current_x = ord(s[k+8]) | ord(s[k+9]) << 8 | ord(s[k+10]) << 16 | ord(s[k+11]) << 24
        node[i].current_y = ord(s[k+12]) | ord(s[k+13]) << 8 | ord(s[k+14]) << 16 | ord(s[k+15]) << 24
        #print node[i].current_x, node[i].current_y
        #node[i].destination_x = ord(s[k+20]) | ord(s[k+21]) << 8 | ord(s[k+22]) << 16 | ord(s[k+23]) << 24
        #node[i].destination_y = ord(s[k+24]) | ord(s[k+25]) << 8 | ord(s[k+26]) << 16 | ord(s[k+27]) << 24

    

