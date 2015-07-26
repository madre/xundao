# coding=utf-8
"""查询页 view定义"""
from django.shortcuts import render
from django.http import HttpResponse
from .search import do_search
from time import clock

PAGE_SIZE = 10


def home(request):
    """首页"""
    return render(request, 'home.html')


def search(request):
    """查询接口"""
    if 'q' in request.GET:
        query = request.GET['q']
        if 'page' in request.GET:
            page = request.GET['page']
        else:
            page = 1
        start = clock()

        search_res = do_search(query, page)
        total_hits = search_res["total"]
        # results = [each["_source"] for each in search_res["hits"]]
        results = []
        for each in search_res["hits"]:
            for highlight in each["highlight"].keys():
                each["_source"][highlight] = each["highlight"][highlight][0]
            results.append(each["_source"])
        end = clock()
        total_page = total_hits / PAGE_SIZE
        if total_page < 10:
            page_list = range(1, total_page)
        elif int(page)+10 < total_page:
            page_list = range(int(page), int(page)+10)
        else:
            page_list = range(page, total_page)
        next_page = 0 if int(page) + 1 >= total_page else int(page) + 1
        return render(request, 'res_search.html', {'results': results,
                                                   'query': query,
                                                   'count': total_hits,
                                                   'time': end - start,
                                                   'page': page,
                                                   'total_page': total_page or 1,
                                                   'page_list': page_list,
                                                   'host': request.META['SERVER_NAME'],
                                                   'port': request.META['SERVER_PORT'],
                                                   'previous_page': int(page)-1,
                                                   'next_page': next_page})
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)

