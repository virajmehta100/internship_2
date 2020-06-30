"""fitness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from calories import views as v
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from login import views
from registration import views as vi
from workout import views as vw

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',v.index),
    url(r'^login$',views.login,name='login'),
    url(r'^login$',include('login.urls')),
    url(r'^registration$',vi.registration,name='registration'),
    url(r'^workout$',vw.workout),

]

urlpatterns += staticfiles_urlpatterns()
