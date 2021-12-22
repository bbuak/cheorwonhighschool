from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from cwhapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.eating, name = 'start'),
    path('select/', include('cwhapp.urls')),
]
