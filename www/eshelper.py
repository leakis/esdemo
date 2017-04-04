#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lion zheng'

' es helper '

import logging; logging.basicConfig(level=logging.INFO)
from datetime import datetime
from elasticsearch import Elasticsearch


def do_search(txt):
	
	esclient = Elasticsearch(['192.168.31.189:9200'])
	rsp = esclient.search(index='social-*',
	body={"query": {"match": {"message": "myProduct"} }
	})
	logging.info('set jinja2 template path: %s' % rsp)

	users=[{"name":"world","email":"aa@qq.com"},{"name":"hello","email":"11@qq.com"},
	{"name":"hello1","email":"111@qq.com"}]


	return users
	