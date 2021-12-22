from django.urls import path  
from . import views

urlpatterns = [
    path('',views.regpg, name = 'class'),
    path('?grade=1grade-1class#/', views.onetwo),
]