from django.shortcuts import render, get_object_or_404
from .models import Service

def service_list(request):
    services = Service.objects.all()
    return render(request, 'service.html', {'services': services})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'service-details.html', {'service': service})
