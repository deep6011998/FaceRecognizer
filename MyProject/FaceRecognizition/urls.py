from django.conf.urls import url,include
from .import views

urlpatterns = [
    url(r'^Home',views.Home,name='Home'),
    url(r'^ImageProcessing',views.ImageProcessing,name='ImageProcessing')
]