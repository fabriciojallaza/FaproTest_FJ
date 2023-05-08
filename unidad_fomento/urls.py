from django.urls import path

from unidad_fomento import views

app_name = 'unidad_fomento'

urlpatterns = [
    path('', views.get_uf_values, name='uf'),

]