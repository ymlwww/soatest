#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import urllib2
import json
import os
import argparse
import io
from google.cloud import vision
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
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    uri ="http://13.65.151.139:8000/static/img/1/1.jpg"
    vision_client = vision.Client()
    image = vision_client.image(source_uri=uri)

    labels = image.detect_labels()
    print('Labels:')

    for label in labels:
        print(label.description)
    return HttpResponse(label.description)

    