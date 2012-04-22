
import json
import os.path
import sys

_rootDir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(_rootDir, 'libs', 'tornado', 'build', 'lib'))

import tornado.httpclient

with open(os.path.join(_rootDir, 'settings.json')) as jsonf:
	settings = json.load(jsonf)

def github_request(path,handle_request, io_loop=None):
	url = 'https://api.github.com' + path
	req = tornado.httpclient.HTTPRequest(url, auth_username=settings['auth']['github']['username'], auth_password=settings['auth']['github']['password'])
	http_client = tornado.httpclient.AsyncHTTPClient(io_loop)
	http_client.fetch(req, handle_request)
