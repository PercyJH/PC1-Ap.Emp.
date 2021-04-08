from django.urls import path

from . import views 

app_name = 'encuesta'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:region_id>/', views.detalle, name='detalle'),
    path('<int:region_id>/resultados/', views.resultados, name='resultados'),
    path('<int:region_id>/voto/', views.votar, name='votar'),

]