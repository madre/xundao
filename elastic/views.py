# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from search import do_search
from time import clock

PAGE_SIZE = 10


def home(request):
    return render(request, 'home.html')


def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        if 'page' in request.GET:
            page = request.GET['page']
        else:
            page = 1
        start = clock()

        search_res = do_search(q, page)
        total_hits = search_res["total"]
        results = [each["_source"] for each in search_res["hits"]]
        end = clock()
        return render(request, 'res_search.html', {'results': results,
                                                   'query': q,
                                                   'count': total_hits,
                                                   'time': end - start,
                                                   'page': page,
                                                   'total_page': total_hits / PAGE_SIZE,
                                                   'host': request.META['SERVER_NAME'],
                                                   'port': request.META['SERVER_PORT'],
                                                   'nextpage': int(page) + 1})
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)
