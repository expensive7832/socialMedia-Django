from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
import os

def Home(req):
    
    return HttpResponse('<h1>Hello World<h1/>')

def index(req):
    return render(req, "core/index.html" )