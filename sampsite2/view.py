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
        #qs_count = User.objects.all().count()
        #all_entries = Dane.objects.all()
        #dane = Dane.objects.all()
        #rok = Dane.objects.get(id=1)
        #przychody = Dane.objects.values('przychody')
        labels = ["Rok", "Przychody", "Zysk brutto", "Dzialalnosc operacyjna", "Dzialalnosc finansowa", "Zysk netto"]
        default_item = [123]
        data = {
            "labels": labels,
            "default": default_item,
        }
        return Response(data)
