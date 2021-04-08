from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse 

from .models import Opcion, Region
# Create your views here.

def index(request):
    latest_question_list = Region.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'encuesta/index.html', context)

def detalle(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    return render(request, 'encuesta/detalle.html', {'region': region})

def votar(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    try:
        selected_opcion = region.opcion_set.get(pk=request.POST['opcion'])
    except (KeyError, Opcion.DoesNotExist):
        return render(request, 'encuesta/detalle.html',{
            'region': region,
            'error_message': "No has seleccionado una opcion.",
        })
    else: 
        selected_opcion.votos += 1 
        selected_opcion.save()
        return HttpResponseRedirect(reverse('encuesta:resultados', args=(region.id,)))

def resultados(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    return render(request, 'encuesta/resultados.html',{'region':region})
