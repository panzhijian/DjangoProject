from django.shortcuts import render
from  django.http import HttpResponse
from  django.http import HttpRequest
from  book.models import  BookInfo,PeopleInfo

def test(request):
    print('测试')
    books=BookInfo.objects.all()
    print(books)

    return HttpResponse(' 后端->app|前端')