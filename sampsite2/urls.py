"""sampsite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import path

from sampsite2.view import hello_world, root_page, random_number

from .view import HomeView, get_data, ChartData, dodanie_danych, years, mplimage, pdf
import polls.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^helloworld/$', hello_world),
    # url(r'^$',root_page),
    url(r'^random/(\d+)/$', random_number),
    path('polls2', years, name='years'),
    path('pdf', pdf, name='pdf'),
    path('mplimage.png', mplimage, name='mplimage'),
    path('polls', dodanie_danych, name='dodanie_danych'),
    url(r'^polls/', include('polls.urls')),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/$', ChartData.as_view()),

]
