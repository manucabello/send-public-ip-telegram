#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

def getPublicIP():
	publicIP = requests.get('http://icanhazip.com').text
	return publicIP
