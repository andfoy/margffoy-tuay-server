import redis
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def map_view(request):
    return render(request, 'maps/index.html', locals())

def send_position(request):
    return HttpResponse("Wait for it")
