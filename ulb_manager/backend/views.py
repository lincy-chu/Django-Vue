from django.shortcuts import HttpResponse
from backend.models import bookInfo, siteInfo
from django.utils import timezone
from django.core import serializers
from django.http import JsonResponse
import json


def add(request):  # 新增
    time = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")  # 当前时间 年月日 时分秒
    data = bookInfo(fromUser='robin', fromSite='site', bookName='崛起', updateTime=time)
    res = data.save()
    print(res)
    return HttpResponse("添加成功!")


def delete(request):  # 删除
    bookInfo.objects.filter(bookName='崛起').delete()
    bookInfo.objects.all().delete()
    return HttpResponse("删除成功!")


def update(request):  # 修改
    bookInfo.objects.filter(bookName='崛起').update(fromUser='lincy chu')
    bookInfo.objects.all().update(fromUser='lincy chu')
    return HttpResponse("修改成功!")


def get(request):  # 查询
    list_info = bookInfo.objects.all()
    json_data = serializers.serialize('json', list_info)
    json_data = json.loads(json_data)
    return JsonResponse(json_data, safe=False)
