#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import urllib2
import json
import os
import argparse
import io
from google.cloud import vision

face_num = [0]
dict_for_vision = {"Old Gate of Tsinghua University":"1","Tsinghua University Central Main Building":"2","Jinchun Garden":"6"}
def index(request):
    return render(request, 'index.html')

def list(request):
    return render(request, 'listing.html')

def item(request,a):
    c = int(a)
    if c == 0:
        return HttpResponse("<center>sorry~ google vision can not dectect what your photo is~</center><br/><center><a href = 13.65.151.139:8000>click to return to the homepage</a></center>") 
    return render(request, 'item.html', {'resultlist': c})

def map(request):
    return render(request, 'map.html')    

def detect(request):
    return render(request, 'detect.html')   

@csrf_exempt
def deliver(request):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    response_total = {}
    response_data = {"landmark":"0"}
    response_total["status"] = 200
    if request.method is not "POST":
        response_total["data"] = response_data
        return JsonResponse(response_total)
    img_data = request.POST['img']
    face_num[0] += 1
    img_data = base64.b64decode(img_data)
    if (face_num[0] % 1000 == 0):
        if(face_num[0] >= 1000):
            for i in range(1000):
                os.remove('yml/static/img/'+str(i)+".png")
    file = open('yml/static/img/'+str(face_num[0]%1000)+'.png', 'wb')
    file.write(img_data)
    file.close()
    uri= "http://13.65.151.139:8000/static/img/"+str(face_num[0]%1000)+'.png')
    vision_client = vision.Client()
    image = vision_client.image(source_uri=uri)
    landmarks = image.detect_landmarks()
    for landmark in landmarks:
        print("landmark")
        print landmark
        print(landmark.description)
        if dict_for_vision.has_key(landmark.description):
            a = dict_for_vision[landmark.description]
            response_data["landmark"] = a
            response_total["data"] = response_data
    return JsonResponse(response_total)