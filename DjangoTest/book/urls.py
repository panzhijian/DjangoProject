from django.urls import path
from django.urls import re_path

from book.views import  test,test_get_post
from  book.views import GetPostView

urlpatterns = [
    #关键字参数
    re_path('(?P<name>\d+)/(?P<age>\d+)/',test),
    # re_path('test_get_post', test_get_post)
    path('test_get_post', GetPostView.as_view())

]