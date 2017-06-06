#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
import urllib2
import json
import os
import argparse
import io
global zans
zans=[0,0,0,0,0,0,0,0,0,0]

def index(request):
    return render(request, 'index.html')

def list(request):
    return render(request, 'listing.html')

def item(request,a):
    c = int(a)
    print c
    name=["二校门","主楼","大礼堂","新清华学堂","工字厅","荷塘","综合体育馆","图书馆","西门","万人食堂"]
    musicurl = "http://13.65.151.139:8000/static/music/"+a+".mp3"
    imgurl = "http://13.65.151.139:8000/static/img/"+a+".jpg"
    texturl = "http://13.65.151.139:8000/static/text/"+a+".txt"
    text = urllib2.urlopen(texturl).read()
    global zans
    zan = zans[c-1]
    comment_form = CommentForm({'author': request.user.username,
                        'email': request.user.email,
                        'url': request.user.url,
                        'article': id} if request.user.is_authenticated() else{'article': id})
    return render(request, 'item.html', {'result': c,'spotname': name[c-1],'musicurl':musicurl,'imgurl':imgurl,'text':text,'zan':zan,'comment_post':comment_post})

def addzan(request,a):
    c = int(a)
    global zans
    zans [c-1] = zans[c-1]+1
    print "yes"
    return HttpResponse("SUCCESS")

def delzan(request,a):
    c = int(a)
    global zans
    zans [c-1] = zans[c-1]-1
    return HttpResponse("SUCCESS")

def map(request):
    return render(request, 'map.html')    


def bashroom(request):
    return render(request, 'bashroom.html')

def activity(request):
    return render(request, 'activity.html')

def canteen(request):
    return render(request, 'canteen.html')


# 提交评论
def comment_post(request):
    try:
        #获取表单内填入的内容
        comment_form=CommentForm(request.POST)
        #进行验证的第一个表单验证
        if comment_form.is_vaild():
            #获取表单信息
            #cleaned_data()用来把接收到的文字清洗为符合django的字符
            #create是一个在一步操作中同时创建对象并且保存的便捷方法。
            comment=Comment.objects.create(username=comment_form.cleaned_data["author"],
                eamil=comment_form.cleaned_data["email"],
                url=comment_form.cleaned_data["url"],
                content=comment_form.cleaned_data["comment"],
                article_id=comment_form.cleaned_data["article"],
                #如果用户已经登录，则获取已经登录的用户，非登录用户将返回None
                #此处用的if语句有些特殊。
                user=request.user if request.user.is_authenticated() else None)
            comment.save()  #保存实例
        else:
            return render(request, "item.html", {"reason":comment_form.erros})
    except Exception as e:
        logger.error(e)
        #重定向到进来之前的网页
        #HTTP_REFERER是http的头文件的一部分，当浏览器向web服务器发送请求的时候，一般会带上Referer,告诉服务器我是从哪个页面链接过来的，服务器借此获得一些信息用于处理。
    return redirect(request.META['HTTP_REFERER'])




