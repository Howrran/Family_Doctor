from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def Helo(request):
    return render(request, 'index.html')