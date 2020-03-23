#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json
import requests

def send_warning(message):
	dir = os.path.dirname(os.path.abspath(__file__))
	filename = os.path.join(dir,'keys.json')
	f = open(filename, 'r')
	content = f.read()
	f.close()
	data = json.loads(content)
	url = 'https://api.telegram.org/bot{0}/sendMessage'.format(data['token'])
	data = {'chat_id': data['channel_id'], 'text': message}
	r = requests.post(url, data)
