#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
import urllib2
import json
import os
import argparse
import io

def index(request):
    return render(request, 'index.html')

def list(request):
    return render(request, 'listing.html')

def item(request,a):
    c = int(a)
    print c
    name=["二校门","主楼","大礼堂","新清华学堂","工字厅","荷塘","综合体育馆","图书馆","西门","万人食堂"]
    print name[c-1]
    return render(request, 'item.html', {'result': c,'spotname': name[c-1]})

def map(request):
    return render(request, 'map.html')    