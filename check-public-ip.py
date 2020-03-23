#!/usr/bin/python
# -*- coding: utf-8 -*-

from getPublicIP import getPublicIP
from checkActualIP import checkActualIP
from sendTelegram import send_warning

def checkPublicIP():
	if (not checkActualIP()):
		send_warning("Nueva IP pública: "+getPublicIP())

checkPublicIP()
