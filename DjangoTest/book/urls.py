from django.urls import path
from book.views import  test

urlpatterns = [
    path('test',test)
]