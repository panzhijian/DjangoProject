from django.shortcuts import render
from  django.http import HttpResponse
from  django.http import HttpRequest
from  book.models import  BookInfo,PeopleInfo
from django.core.paginator import  Paginator
import  json
from  django.http import JsonResponse
from  django.http import HttpResponseServerError,HttpResponseBadRequest,HttpResponseForbidden,HttpResponseNotFound
from django.views.generic import  View


def test(request,name,age):
    # peoples=PeopleInfo.objects.all()
    print(name ,age)
    '''  分页测试
        #获取分页器试列
    paginator = Paginator(peoples, 2)
    # 获取指定页码的数据
    page_skus = paginator.page(1)
    print('page_skus 分页对象',page_skus)
    # 获取分页数据
    total_page = paginator.num_pages
    print('total_page',total_page)
    
    '''
    return HttpResponse(' 后端->app|前端')


def test_get_post(request):

    # print('GET',request.GET)
    # print(request.GET.get('name'))
    # print(request.GET.get('age'))
    # print(request.GET.getlist('age'))


    #post 表单
    # print('POST',request.POST)
    # print(request.POST.get('name'))
    # print(request.POST.get('age'))
    # print(request.POST.getlist('age'))


    #post 非表单
    # json_str = request.body #bytes数据类型
    # print(type(json_str))
    # print(json_str)
    #
    # req_data = json.loads(json_str) #json字符串转化为字典
    # print(req_data['name'])
    # print(req_data['age'])


    print(request.user)
    print(request.path)
    print(request.method)
    print(request.META)

    # response = HttpResponse()
    # response.status_code = 200
    # response['itcast'] = 'Python'
    # return  response


    #返回json给 app |前端  状态码也一同放在json字符串里面 统一处理
    # return  JsonResponse({'city': 'beijing', 'subject': 'python', 'stats': 200})


    #设置cookie 过期时间max_age=30秒 浏览器的cook 会自动删除的
    response=HttpResponse('返回给你的内容')
    response.set_cookie('name', value='panzhijian',max_age=30*60*60*24)


    #处理session
    # request.session['names'] = 'zhangsan'
    # print(request.session.get('name'))

    return response








class GetPostView(View):
    #处理get请求
    def get(self,request):
        bookinfos=BookInfo.objects.all()

        # 将模型转字典
        books = []
        for book in bookinfos:
            books.append({
                'id': book.id,
                'name': book.name
            })
        request.session['names'] = 'zhangsan'
        print(request.session.get('name'))

        return JsonResponse({'code': '200', 'errmsg': 'OK', 'books': books})


    #处理post请求
    def post(self,request):
        bookinfos=BookInfo.objects.all()

        # 将模型转字典
        books = []
        for book in bookinfos:
            books.append({
                'id': book.id,
                'name': book.name
            })

        return JsonResponse({'code': '200', 'errmsg': 'OK', 'books': books})







