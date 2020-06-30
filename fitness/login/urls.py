from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from registration import views as vi
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [


    url(r'^registration$',vi.registration,name='registration'),

]

urlpatterns += staticfiles_urlpatterns()
