from django.http import HttpResponse
from django.shortcuts import redirect, render
import datetime


def home(request):
    date = datetime.datetime.now().date()
    name = 'Viktor'
    _context = {
        'date' : date,
        'name' : name
    }
    return render(request, 'home.html', _context)