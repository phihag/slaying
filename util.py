
import datetime
import json
import os.path
import platform
import re
import sys

_rootDir = os.path.dirname(os.path.abspath(__file__))
pyvTuple = platform.python_version_tuple()
platformStr = '%s-%s-%s.%s' % (platform.uname()[0].lower(), platform.machine(), pyvTuple [0], pyvTuple [1])
sys.path.append(os.path.join(_rootDir, 'libs', 'tornado', 'build', 'lib.' + platformStr))
sys.path.append(os.path.join(_rootDir, 'libs', 'tornado', 'build', 'lib'))

import tornado.httpclient

with open(os.path.join(_rootDir, 'settings.json')) as jsonf:
	settings = json.load(jsonf)

USER_AGENT = 'slaying productivity project @ HHUD (hagemeister@cs.uni-duesseldorf.de)'
DATADIR = os.path.join('.', 'data')

def github_request(path,handle_request, io_loop=None):
	url = 'https://api.github.com' + path
	req = tornado.httpclient.HTTPRequest(url,
		auth_username=settings['auth']['github']['username'],
		auth_password=settings['auth']['github']['password'],
		user_agent=USER_AGENT
	)
	http_client = tornado.httpclient.AsyncHTTPClient(io_loop)
	http_client.fetch(req, handle_request)

def ensureDir(d):
	if not os.path.exists(d):
		os.makedirs(d)

def extractDate(filename):
	m = re.match(r'[a-z]+-(\d{4})-(\d{2})-(\d{2})T[0-9:.]+\.[a-z0-9]+', filename)
	assert m
	return datetime.date(*map(int, m.groups()))
