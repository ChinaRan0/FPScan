import re
f = open('baidu','r')
whois = f.read()
obj = re.compile(r'(?P<content>.*?)  URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf',re.S)
if re.findall('(?P<content>.*?)  URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/',whois) :

    print('yes')
    chuli = obj.finditer(whois)
    print(chuli)
    for it in  chuli :
            print(it.group("content")) 