import socket
import termcolor
def scan(targets,port):
    for port in range(1,port):
        scan_port(targets,port)

def scan_port(ipaddress,port):
    try:
        
        sock=socket.socket()
        sock.connect((ipaddress,port))
        print("[+] port Opened! "+str(port))
        sock.close()
    except:
        print("[-] port closed! "+str(port)) 
        # if we wnat to print only open ports to be shown up,we can pass this statement by simply commenting pass

        

targets=input("[*] Enter targets to scan (split them by ,): ") #192.168.1.1,192.168.2.1
port=int(input("[*] Enter how many ports you want to scan: "))
if ',' in targets:
    print(termcolor.colored(("[*] Scanning multiple Targets:"),'green'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '),port)
else:
    scan(targets,port)