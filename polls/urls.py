from django.urls import path
from .views import list_datas, create_datas, update_datas, delete_datas

urlpatterns = [
    path('', list_datas, name='list_datas'),
    path('new', create_datas, name='create_datas'),
    path('update/<int:id>/', update_datas, name='update_datas'),
    path('delete/<int:id>/', delete_datas, name='delete_datas'),
]
