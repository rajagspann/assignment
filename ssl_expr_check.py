#!/bin/python

# SSL expiry check of domains with python

import socket
import ssl
import datetime

#dictionary
d = {}

#print "-----Certificate details without sort-----"
#print "=========================================="
def scheck(hostname):
  #  print "%s"%(hostname)
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
    context = ssl.create_default_context()
    # to wrap a socket.
    conn = context.wrap_socket(socket.socket(socket.AF_INET),server_hostname=hostname,)
    conn.settimeout(3.0)
    conn.connect((hostname, 443))
    ssl_info = conn.getpeercert()
    Exp_ON=datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)
    d[hostname] = Exp_ON
    Days_Remaining= Exp_ON - datetime.datetime.utcnow()
   #d[hostname] = Days_Remaining
   # print "Expires ON:- %s\nRemaining:- %s" %(Exp_ON,Days_Remaining)
   # print "-----------------------------------------------"



with open('websites') as f:
    a = f.readlines()

lines = list(line for line in (l.strip() for l in a) if line)
map(scheck, lines)

print('\n')
print('\n')

print "-----Certificate details with sort-----"
print "=========================================="

#for k in sorted(d.items(), key = lambda x:datetime.datetime.strptime(x[0], '%d-%m-%Y'), reverse=True):

for k in sorted(d, key=d.get, reverse=True):
    print(k, d[k].strftime('%d/%m/%Y'))


