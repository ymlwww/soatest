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
    return render(request, 'item.html', {'resultlist': c})

def map(request):
    return render(request, 'map.html')    