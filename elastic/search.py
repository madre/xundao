#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '20/7/15'
__author__ = 'deling.ma'
"""
from elasticsearch import Elasticsearch

PAGE_SIZE = 10


def do_search(query, page):
    es = Elasticsearch(['114.215.104.130:9200'], timeout=5)

    page = int(page)
    if page < 1:
        page = 1

    search_res = es.search(index='zhidao', doc_type='QuestionItem', q=query, from_=page)
    results = search_res["hits"]
    return results
