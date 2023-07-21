#---------------------DEMONSTRATION OF NETWORK ADDRESS TRANSLATION-----------------

#Client class

class Client:
    def __init__(self,client_ip,client_port,msgreq):
        self.client_ip=client_ip;
        self.msgreq=msgreq;
        print("------------CLIENT---------")
        print("My IP Address: ",client_ip)
        print("My port: ",client_port)
        print("My friend nat will request server behalf of me")
        print("client msg to server:",msgreq)
        
    def getrequest(self):
         return self.msgreq
    def getclientip(self):
        return self.client_ip
        
#NAT CLASS      
       
        
class Nat(Client):
    
    #Translation table
    
    def __init__(self):
        print("--------------NAT------------")
        client_ipadr=client_obj.getclientip();
        if client_ipadr=="192.168.1.101":
            nat_ip="65.96.14.76"
            nat_port=1
            print("NAT IP:",nat_ip)
            print("NAT PORT:",nat_port)
        
        elif client_ipadr=="192.168.1.103":
            nat_ip="65.96.14.76"
            nat_port=2
            print("NAT IP:",nat_ip)
            print("NAT PORT:",nat_port)
        
        elif client_ipadr=="192.168.1.104":
            nat_ip="65.96.14.76"
            nat_port=3
            print("NAT IP:",nat_ip)
            print("NAT PORT:",nat_port)
        
        elif client_ipadr=="192.168.1.102":
            nat_ip="65.96.14.76"
            nat_port=4
            print("NAT IP:",nat_ip)
            print("NAT PORT:",nat_port)
        
        elif client_ipadr=="192.168.0.1":
            nat_ip="200.200.200.1"
            nat_port=18
            print("NAT IP:",nat_ip)
            print("NAT PORT:",nat_port)
        
        elif client_ipadr=="192.168.0.2":
            nat_ip="200.200.200.1"
            nat_port=19
            print("NAT IP:",nat_ip)
            print("NAT PORT:",nat_port)
        
        elif client_ipadr=="192.168.0.3":
            nat_ip="200.200.200.1"
            nat_port=20
            print("NAT IP:",nat_ip)
            print("NAT PORT:",nat_port)
        
        elif client_ipadr=="192.168.0.4":
            nat_ip="200.200.200.1"
            nat_port=21
            print("NAT IP:",nat_ip)
            print("NAT PORT:",nat_port)
        
        else:
            print("sorry,client ip is not in translation table")
    
#SERVER CLASS      

class Server(Nat):
    def __init__(self,server_ip,server_port):
        self.server_ip=server_ip
        self.server_port=server_port
        print("---------SERVER--------")
       
        print("MY IP:",server_ip)
        print("MY PORT:",server_port)
        
    def msg_reqarea(self,clientmsg):
        self.clientmsg=clientmsg
        if clientmsg=="HII":
            print("server msg to client:HELLO")
        elif clientmsg=="HOW ARE YOU":
            print("server msg to client :FINE")
        elif clientmsg=="WHAT ARE YOU DOING":
            print("server msg to client:NOTHING")
        elif clientmsg=="BYE":
            print("server message to client:BYE MEET YOU SOON...")
        else:
            print("..")
# DRIVER CLASS

for i in range(0,4):
#Asking request for client
    msgreq=input("Enter msgreq: ")

#object created for client
    client_ip=input('Enter client IP Address: ')
    client_port=input('Enter client Port: ');
    client_obj=Client(client_ip,client_port,msgreq)

#Object created for NAT
    nat_obj=Nat()

#object created for client
    clientmsg=client_obj.getrequest()

#object created for server
    server_ip="244.46.1.1"
    server_port=18
    server_obj=Server(server_ip,server_port)
    server_obj.msg_reqarea(clientmsg)
    print("____________________________________________")

