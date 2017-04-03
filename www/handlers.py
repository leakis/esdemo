#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lion zheng'

' url handlers '

from coroweb import get, post

@get('/')
async def index(request):
    #users = await User.findAll()
    users=[{"name":"world","email":"aa@qq.com"},{"name":"hello","email":"11@qq.com"}]
    return {
        '__template__': 'test.html',
        'users': users
    }