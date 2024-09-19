from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Players

def index(request):
    players = Players.objects.all().order_by('-time_create')
    paginator = Paginator(players, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj, 'paginator': paginator})