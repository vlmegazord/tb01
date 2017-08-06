from django.shortcuts import render
import datetime as dt
from django.utils.timezone import now

def home(request):
    today = dt.date.today()
    return render(request, 'taskbuster/index.html', {'today': today, 'now': now()})
    # return render(request, 'taskbuster/index.html', {'today': today, 'now': now() })

def home_files(request, filename):
    return render(request, filename, {})#, content_type="text/plain")

# def robots(request):
#     return render(request, 'robots.txt', {}, content_type="text/plain")
#
# def humans(request):
#     return render(request, 'humans.txt', {}, content_type="text/plain")
