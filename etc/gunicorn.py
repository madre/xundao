#!/usr/bin/env python
# coding=utf-8
"""
gunicorn 启动配置
__created__ = '2015/5/13'
__author__ = 'deling.ma'
"""

import gevent.monkey
gevent.monkey.patch_all()
import multiprocessing

bind = '0.0.0.0:2015'
max_requests = 1000
keepalive = 5

proc_name = 'xundao'

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gunicorn.workers.ggevent.GeventWorker'

loglevel = 'info'
errorlog = '-'

x_forwarded_for_header = 'X-FORWARDED-FOR'
