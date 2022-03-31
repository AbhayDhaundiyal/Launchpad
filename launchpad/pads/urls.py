from django.urls import URLPattern
from . import views
from django.urls import path

app_name = 'login'

urlpatterns =[
    path('hello/', views.hello, name = 'hello'),
]