from django.shortcuts import render
import datetime as dt

def home(request):
    today = dt.date.today()
    return render(request, 'taskbuster/index.html', {'today': today})

def home_files(request):
    return render(request, filename, {}, content_type="text/plain")
