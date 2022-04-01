from django.urls import URLPattern
from . import views
from django.urls import path

app_name = 'login'

urlpatterns =[
    path('show/', views.show, name = 'show'),
    path('show/<int:id>/', views.show_one, name = 'show_one'),
    path('book/<int:id>/', views.book, name = 'book'),
]