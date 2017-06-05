#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import urllib2
import json
def index(request):
    return render(request, 'index.html')

def list(request):
    return render(request, 'listing.html')

def item(request,a):
    c = int(a)
    return render(request, 'item.html', {'resultlist': c})

def map(request):
    return render(request, 'map.html')

def deliver(request):
    url = "https://vision.googleapis.com/v1/images:annotate?key=AIzaSyAyZ_Ss0Xm9Bk_MxcoJ0eMNukiM9xaN-fA"
    content = "{
                "requests":[
                    {
                    "image":{
                        "content":"http://13.65.151.139:8000/static/img/1.png"
                    },
                    "features":[
                        {
                        "type":"LABEL_DETECTION",
                        "maxResults":1
                        }
                    ]
                    }
                ]
                }"
     s = json.loads(content)
     imgurl ="http://13.65.151.139:8000/static/img/1.png"
     s["requests"]["image"]["content"] = imgurl
     data = urllib2.urlopen(s).read()
     print data
     return HttpResponse(data)

    