#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import urllib2
import json
import os
import argparse
import io
from google.cloud import vision

dict_for_vision = {"Old Gate of Tsinghua University":"1","Tsinghua University Central Main Building":"2","Jinchun Garden":"6"}
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
    vision_client = vision.Client()
    uri = "http://13.65.151.139:8000/static/img/1.jpg"
    image = vision_client.image(source_uri=uri)
    landmarks = image.detect_landmarks()
    for landmark in landmarks:
        print("landmark")
        print landmark
        print(landmark.description)
        a = dict_for_vision(landmark.description)
        return HttpResponse(a)
    return HttpResponse("0") 


    
    # uri ="http://13.65.151.139:8000/static/img/2.jpg"
    # image = vision_client.image(source_uri=uri)
    # landmarks = image.detect_landmarks()

    # for landmark in landmarks:
    #     print("landmark")
    #     print landmark
    #     print(landmark.description)
    # uri ="http://13.65.151.139:8000/static/img/3.jpg"
    # image = vision_client.image(source_uri=uri)
    # landmarks = image.detect_landmarks()

    # for landmark in landmarks:
    #     print("landmark")
    #     print landmark
    #     print(landmark.description)
    # uri ="http://13.65.151.139:8000/static/img/4.jpg"
    # image = vision_client.image(source_uri=uri)
    # landmarks = image.detect_landmarks()

    # for landmark in landmarks:
    #     print("landmark")
    #     print landmark
    #     print(landmark.description)
    # uri ="http://13.65.151.139:8000/static/img/5.jpg"
    # image = vision_client.image(source_uri=uri)
    # landmarks = image.detect_landmarks()

    # for landmark in landmarks:
    #     print("landmark")
    #     print landmark
    #     print(landmark.description)
    # uri ="http://13.65.151.139:8000/static/img/6.jpg"
    # image = vision_client.image(source_uri=uri)
    # landmarks = image.detect_landmarks()

    # for landmark in landmarks:
    #     print("landmark")
    #     print landmark
    #     print(landmark.description)
    # uri ="http://13.65.151.139:8000/static/img/7.jpg"
    # image = vision_client.image(source_uri=uri)
    # landmarks = image.detect_landmarks()

    # for landmark in landmarks:
    #     print("landmark")
    #     print landmark
    #     print(landmark.description)
    # uri ="http://13.65.151.139:8000/static/img/8.jpg"
    # image = vision_client.image(source_uri=uri)
    # landmarks = image.detect_landmarks()

    # for landmark in landmarks:
    #     print("landmark")
    #     print landmark
    #     print(landmark.description)
    # uri ="http://13.65.151.139:8000/static/img/9.jpg"
    # image = vision_client.image(source_uri=uri)
    # landmarks = image.detect_landmarks()

    # for landmark in landmarks:
    #     print("landmark")
    #     print landmark
    #     print(landmark.description)
    # uri ="http://13.65.151.139:8000/static/img/10.jpg"
    # image = vision_client.image(source_uri=uri)
    # landmarks = image.detect_landmarks()

    # for landmark in landmarks:
    #     print("landmark")
    #     print landmark
    #     print(landmark.description)
    
    