from django.shortcuts import render
from django.http import HttpResponse

def index(request):
     return HttpResponse("<h2>Hello python</h2>")

