#!/bin/python

# SSL expiry check of domains with python

import socket
import ssl
import datetime


class ssl_check():


    def __init__(self, hostname):
        print "%s"%(hostname)
        ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
        context = ssl.create_default_context()
        # to wrap a socket.
        conn = context.wrap_socket(socket.socket(socket.AF_INET),server_hostname=hostname,)
        conn.settimeout(3.0)
        conn.connect((hostname, 443))
        ssl_info = conn.getpeercert()
        Exp_ON=datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)
        Days_Remaining= Exp_ON - datetime.datetime.utcnow()
        print "Expires ON:- %s\nRemaining:- %s" %(Exp_ON,Days_Remaining)
        print "-----------------------------------------------"



domains = ['apple.com', 'google.com', 'facebook.com', 'netflix.com', 'yahoo.com']


# I am using map function to iterate through the list


map(ssl_check, domains)

