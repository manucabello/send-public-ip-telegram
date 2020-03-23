#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from getPublicIP import getPublicIP

def checkActualIP():
	dir = os.path.dirname(os.path.abspath(__file__))
	filename = os.path.join(dir,'publicIPs.txt')
	if os.path.exists(filename):
		file = open(filename, 'r')
	else:
		file = open(filename, 'w+')
	publicIpActual = getPublicIP().split('\n')[0]
	
	linea = file.readline()
	publicIP = ""
	while linea != '':
		publicIP = linea
		linea = file.readline()
	file.close()

	if publicIP == "" or publicIP != publicIpActual:
		publicIP = publicIpActual
		file = open(filename, 'w')
		file.write(publicIP)
		file.close()
		return False
	else:
		return True
