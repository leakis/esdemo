#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lion zheng'

' url handlers '

from coroweb import get, post
import eshelper

@get('/')
async def index(request):
    #users = await User.findAll()
    users=eshelper.do_search("a")
    return {
        '__template__': 'test.html',
        'users': users
    }