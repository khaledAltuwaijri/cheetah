from django.shortcuts import render
from django.http import HttpResponse

from .forms import NameForm

def index(request):
    return render(request, 'search/index.html')

def getSongRequest(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
