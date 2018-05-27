import numpy as np
from .models import Dane
from .forms import DataForm
from django.shortcuts import render, redirect
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from scipy import special, optimize
import matplotlib.pyplot as plt
import django

import io
def list_datas(request):
    datas = Dane.objects.all()
    return render(request, 'datas.html', {'datas': datas})





def create_datas(request):
    form = DataForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_datas')

    return render(request, 'datas-form.html', {'form': form})


def update_datas(request, id):
    data = Dane.objects.get(id=id)
    form = DataForm(request.POST or None, instance=data)

    if form.is_valid():
        form.save()
        return redirect('list_datas')

    return render(request, 'datas-form.html', {'form': form, 'data': data})


def delete_datas(request, id):
    data = Dane.objects.get(id=id)

    if request.method == 'POST':
        data.delete()
        return redirect('list_datas')

    return render(request, 'data-delete-confirm.html', {'data': data})
