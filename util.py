
import json
import os.path
import sys

_rootDir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(_rootDir, 'libs', 'tornado', 'build', 'lib'))

import tornado.httpclient

with open(os.path.join(_rootDir, 'settings.json')) as jsonf:
	settings = json.load(jsonf)

USER_AGENT = 'slaying productivity project @ HHUD (hagemeister@cs.uni-duesseldorf.de)'
DATADIR = os.path.join(_rootDir, 'data')

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
