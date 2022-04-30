import socket
import threading
import sys
from IPy import IP
def scan_port(ipaddress,port):
    try:   
        sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)      
        sock.settimeout(1)
        sock.connect((ipaddress,port))
        try:           
            infotc=socket.getservbyport(port,'tcp')
            infoud=socket.getservbyport(port,'udp')
            if infotc =='https' or infotc=='http':
                data='GET /HTTP/1.1 \r\n'
                sock.send(data.encode())
                infob=sock.recv(1024).decode()
                infob=infob.split("\n")[1].split("Server:")[1]   #manipulating the string variable to get info about server 
            else:
                infob=sock.recv(1024).decode()     
            print(str(port)+'\t\t '+str(infotc)+'\t\t '+str(infoud)+'\t\t'+str(infob))
            sock.close()
        except Exception as e:
             print(str(port)+'\t\t '+str(infotc)+'\t ')
    except :
        pass
def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)
def main():
    if (len(sys.argv)==2): 
        if str(sys.argv[1])=='--help':
             print("Usage: script, IP address(or website), Port(Start), Port(End)")
    elif len(sys.argv) != 4:
        print("Error! Type --help for help")
        exit()
    else:
        ipaddress=str(sys.argv[1]) # scanner.py <argv[1]> <argv[2]> <argv[3]>
        ipaddress=check_ip(ipaddress)
        print(str(ipaddress))
        sPort =(int)(sys.argv[2])
        ePort=(int)(sys.argv[3])
        print("OPEN PORTS \t SERVICE(TCP) \t SERVICE(UDP) \t\t  BANNER")
        for i in range(sPort,ePort+1):
          thread = threading.Thread(target=scan_port, args=[ipaddress,i])
          thread.start()

if __name__ =='__main__': #calls the main method
    main()
    
    
   
    




