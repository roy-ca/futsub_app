from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home),
    url(r'clicked/',views.out),
    url(r'reg/',views.reg),
    url(r'regsub/',views.regsub),
]
