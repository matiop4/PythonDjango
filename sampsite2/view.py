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
        # zysk_brutto = Dane.objects.all()[:1].get().zysk_brutto
        # labels = ["Przychody", "Zysk brutto", "Dzialalnosc operacyjna", "Dzialalnosc finansowa", "Zysk netto"]
        data = {
            "labels": lata,
            "default": przychody,
        }
        return Response(data)
