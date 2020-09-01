from django.contrib import admin
from django.urls import path
from django.urls import re_path
from landing import views

urlpatterns = [
    re_path(r'^aster', admin.site.urls),
    path('', views.index, name='home'),
    re_path(r'/+', views.error),
]
