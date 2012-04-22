#!/usr/bin/env python3

import functools

import util
import tornado.ioloop

def handle_request(io_loop, response):
	print(str(response.headers['X-Ratelimit-Remaining']) + ' / ' + str(response.headers['X-Ratelimit-Limit']))
	io_loop.stop()

def main():
	io_loop = tornado.ioloop.IOLoop()
	util.github_request('/', functools.partial(handle_request, io_loop), io_loop)
	io_loop.start()

if __name__ == '__main__':
	main()