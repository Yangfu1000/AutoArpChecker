import subprocess, sys, re, time

whitelist = open('whitelist.txt', 'a')
cleanedUp = open('unknownList.txt', 'w')
network = open('ipList.txt', 'w')
ignore = open('ignore.txt', 'w')
whitelist.close
cleanedUp.close
network.close
ignore.close

while True:
    
    cleanedUp = open('unknownList.txt', 'a')
    
    cleanedUp.write('\n')
    cleanedUp.write('New Log Update')
    cleanedUp.write('\n')
    
    print('\n')
    print('\n')
    print('New Log Update')

    ipsOnNetwork = subprocess.check_output('arp -a')
    stringNetworkIps = str(ipsOnNetwork)
    network = open('ipList.txt', 'w')
    network.write(stringNetworkIps)
    network.close

    whitelist = open('whitelist.txt', 'r')
    network = open('ipList.txt', 'r')

    unknown = set(network).difference(whitelist)
    unknownString = str(unknown)

    ignore = open('ignore.txt', 'w')
    ignore.write(unknownString)

    ignore = open('ignore.txt', 'r')

    ips = []
    for text in ignore.readlines():
        found = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',text)
        if found:
            ips.extend(found)
    
    for ip in ips:
        cleanedUp.write(ip)
        cleanedUp.write('\n')
        print(ip)

    time.sleep(5)
        
