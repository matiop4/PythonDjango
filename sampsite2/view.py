from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

import random

from polls.models import Dane

User = get_user_model()


def hello_world(requset):
    return HttpResponse("Hello world")


def root_page(request):
    return HttpResponse("Root home page")


def dodanie_danych(request):
    return render(request, 'datas.html')

def years(request):
    return render(request, 'yers.html')

def random_number(request, max_rand=100):
    random_num = random.randrange(0, int(max_rand))
    msg = "random number between 0 and %s : %d " % (max_rand, random_num)
    return HttpResponse(msg)


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"customers": 10})


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)  # http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # qs_count = User.objects.all().count()
        # dane = Dane.objects.all()
        lata = [Dane.objects.all()[0].rok, Dane.objects.all()[1].rok, Dane.objects.all()[2].rok, Dane.objects.all()[3].rok]
        przychody = [Dane.objects.all()[0].przychody, Dane.objects.all()[1].przychody, Dane.objects.all()[2].przychody, Dane.objects.all()[3].przychody]
        kumulacja2015 = [Dane.objects.all()[3].przychody,Dane.objects.all()[3].zysk_brutto,Dane.objects.all()[3].dzialalnosc_finansowa,Dane.objects.all()[3].zysk_netto,Dane.objects.all()[3].dzialalnosc_operacyjna]
        kumulacja2014 = [Dane.objects.all()[2].przychody,Dane.objects.all()[2].zysk_brutto,Dane.objects.all()[2].dzialalnosc_finansowa,Dane.objects.all()[2].zysk_netto,Dane.objects.all()[2].dzialalnosc_operacyjna]
        kumulacja2013 = [Dane.objects.all()[1].przychody,Dane.objects.all()[1].zysk_brutto,Dane.objects.all()[1].dzialalnosc_finansowa,Dane.objects.all()[1].zysk_netto,Dane.objects.all()[1].dzialalnosc_operacyjna]
        kumulacja2012 = [Dane.objects.all()[0].przychody,Dane.objects.all()[0].zysk_brutto,Dane.objects.all()[0].dzialalnosc_finansowa,Dane.objects.all()[0].zysk_netto,Dane.objects.all()[0].dzialalnosc_operacyjna]
        # zysk_brutto = Dane.objects.all()[:1].get().zysk_brutto
        label2 = ["przychody","zysk brutto","działalność finansowa","zysk netto","dziłalność operacyjna"]
        data = {
            "labels": lata,
            "default": przychody,
            "all2015": kumulacja2015,
            "all2014": kumulacja2014,
            "all2013": kumulacja2013,
            "all2012": kumulacja2012,
            "allLabels": label2

        }
        return Response(data)
