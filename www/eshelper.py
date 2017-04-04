#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lion zheng'

' es helper '

import logging; logging.basicConfig(level=logging.INFO)
from datetime import datetime
from elasticsearch import Elasticsearch

def init_es():
	esclient = Elasticsearch(['192.168.31.189:9200'])
	return esclient

def do_search(txt):
	query={	
    "query": {
        "filtered": {
            "query": {
                "match": {
                    "contents": "很好玩"
                }
            },
            "filter": {
                "term": {
                    "areaId": 1
                }
            }
        }
        },
        "highlight": {
                "pre_tags": [
                    "<b>"
                ],
                "post_tags": [
                    "</b>"
                ],
                "fields": {
                    "contents": {}
                }
            }   
	}

	esclient = init_es()
	rsp = esclient.search(index='test_*',
	body=query)
	
	logging.info('do search')
	logging.info('had index today: %s' % rsp["hits"])
	#sync_data()

	users=[{"name":"world","email":"aa@qq.com"},{"name":"hello","email":"11@qq.com"},
	{"name":"hello1","email":"111@qq.com"}]


	return users

def check_exists(index_name):
	esclient = init_es()
	is_ex=esclient.indices.exists(index=index_name)
	return is_ex


def  create_index(index_name):
	index_mapping={
	"mappings":{
    "logs": {
        "properties": {
          "contents": {
            "type": "string",
            "analyzer": "ik_smart"
          },
          "logDate": {
            "type": "date",
            "format": "strict_date_optional_time||epoch_millis"
          },
          "logId": {
            "type": "long"
          },
          "characterId": {
            "type": "long"
          },
          "areaId": {
            "type": "long"
          }
        }
      }
    }
    }
	esclient=init_es()
	esclient.indices.create(index=index_name,
	body=index_mapping)


def send_data(index_name):
	data={
	"contents": "龙之谷很好玩",
    "logDate":"2017-01-01",
    "logId": 2,
    "characterId": 100,
    "areaId":1
	}
	esclient=init_es()
	esclient.create(index=index_name,doc_type='logs',id=2,
	body=data)


def  sync_data():
	index_name='test_20170405'
	is_ex=check_exists(index_name)
	if is_ex:
		logging.info('had index today do not create')
	else:
		create_index(index_name)	
	send_data(index_name)
	

	