from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, "base.html", {'a': 'bbb'})

@login_required
def lk(request):
    return render(request, "personal_area/lk.html", {'client_name': 'Чёткий Клиент'})
