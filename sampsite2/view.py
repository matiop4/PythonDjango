from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from django.db.models.functions import Length
from rest_framework.views import APIView
from rest_framework.response import Response
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from scipy import special, optimize
import matplotlib.pyplot as plt
import numpy as np
import django
import random
import argparse
from polls.models import Dane
import  io
User = get_user_model()

# len = Dane.objects.all().count()


def hello_world(requset):
    return HttpResponse("Hello world")


def root_page(request):
    return HttpResponse("Root home page")


def dodanie_danych(request):
    return render(request, 'datas.html')

def years(request):
    return render(request, 'yers.html')

def mplimage(request):
    fig = Figure()
    canvas = FigureCanvasAgg(fig)
    buf = io.BytesIO()
    f = lambda x: -special.jv(3, x)
    sol = optimize.minimize(f, 1.0)
    zysk_brutto1 = [Dane.objects.all()[0].zysk_brutto, Dane.objects.all()[1].zysk_brutto,
                     Dane.objects.all()[2].zysk_brutto, Dane.objects.all()[3].zysk_brutto,
                     Dane.objects.all()[4].zysk_brutto]

    # Plot
    zysk_brutto2 = np.asarray(zysk_brutto1)
    zysk_brutto2 = list(map(int, zysk_brutto2))

    x = np.linspace(0, 1, 5)
    t = np.arange(0., 1., 0.2)
    # sorted(zysk_brutto1)
    # plt.axis([2000,2100])
    newdata = np.squeeze(zysk_brutto1)
    plt.plot( [2012,2013,2014,2015,2016],zysk_brutto2,'o')
    plt.savefig(buf, format='png')
    plt.close(fig)
    response=django.http.HttpResponse(buf.getvalue(),content_type='image/png')
    return response

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
        dane1 = Dane.objects.all()
        print(dane1)
        lata = []
        przychody = []
        zysk_netto = []
        print()
        zysk_brutto1  = []

        avg = 0

        dzialalnosc_finansowa =[]

        len = Dane.objects.all().count()
        i = 0
        while i < len:
            zysk_brutto1.append(Dane.objects.all()[i].zysk_brutto),
            zysk_netto.append(Dane.objects.all()[i].zysk_netto),
            przychody.append(Dane.objects.all()[i].przychody),
            dzialalnosc_finansowa.append(Dane.objects.all()[i].dzialalnosc_finansowa),
            lata.append(Dane.objects.all()[i].rok),
            i +=1

        kumulacja2015 = [Dane.objects.all()[3].przychody,Dane.objects.all()[3].zysk_brutto,Dane.objects.all()[3].dzialalnosc_finansowa,Dane.objects.all()[3].zysk_netto,Dane.objects.all()[3].dzialalnosc_operacyjna]
        kumulacja2014 = [Dane.objects.all()[2].przychody,Dane.objects.all()[2].zysk_brutto,Dane.objects.all()[2].dzialalnosc_finansowa,Dane.objects.all()[2].zysk_netto,Dane.objects.all()[2].dzialalnosc_operacyjna]
        kumulacja2013 = [Dane.objects.all()[1].przychody,Dane.objects.all()[1].zysk_brutto,Dane.objects.all()[1].dzialalnosc_finansowa,Dane.objects.all()[1].zysk_netto,Dane.objects.all()[1].dzialalnosc_operacyjna]
        kumulacja2012 = [Dane.objects.all()[0].przychody,Dane.objects.all()[0].zysk_brutto,Dane.objects.all()[0].dzialalnosc_finansowa,Dane.objects.all()[0].zysk_netto,Dane.objects.all()[0].dzialalnosc_operacyjna]
        # zysk_brutto = Dane.objects.all()[:1].get().zysk_brutto
        label2 = ["przychody","zysk brutto","działalność finansowa","zysk netto","dziłalność operacyjna"]
        przychody1 = np.asarray(przychody)
        zysk_netto2 = np.asarray(zysk_netto)
        zysk_brutto2 = np.asarray(zysk_brutto1)
        przychody1 = list(map(int, przychody1))
        zysk_netto2 = list(map(int, zysk_netto2))
        zysk_brutto2= list(map(int, zysk_brutto2))
        avg1 = np.average(przychody1)
        avg2 = np.average(zysk_netto2)
        avg3 = np.average(zysk_brutto2)
        data = {
            "labels": lata,
            "default": przychody,
            "all2015": kumulacja2015,
            "all2014": kumulacja2014,
            "all2013": kumulacja2013,
            "all2012": kumulacja2012,
            "zyskN":zysk_netto,
            "zyskB":zysk_brutto1,
            "allLabels": label2,
            "avgPrzy" : avg1,
            "avgZyskB" : avg3,
            "avgZyskN" : avg2,
            "przychodyplot": przychody1

        }
        return Response(data)
