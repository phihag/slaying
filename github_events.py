#!/usr/bin/env python3

import datetime
import functools
import os
import optparse

import util

import tornado.ioloop

INTERVAL = 1000

GITHUB_EVENTS_DIR = os.path.join(util.DATADIR, 'github-events')

def handle_request(sendTime, opts, response):
	basename = 'events-' + sendTime.isoformat() + '.json'
	fn = os.path.join(GITHUB_EVENTS_DIR, basename)
	with open(fn, 'wb') as f:
		f.write(response.body)
	if opts.verbose:
		print(basename)

def main():
	parser = optparse.OptionParser()
	parser.add_option('-v', '--verbose', action='store_true')
	opts,args = parser.parse_args()

	util.ensureDir(GITHUB_EVENTS_DIR)

	io_loop = tornado.ioloop.IOLoop()
	pc = tornado.ioloop.PeriodicCallback(
		lambda:	util.github_request('/events?per_page=100', functools.partial(handle_request, datetime.datetime.utcnow(), opts), io_loop=io_loop),
		INTERVAL, io_loop=io_loop)
	pc.start()
	io_loop.start()


if __name__ == '__main__':
	main()
